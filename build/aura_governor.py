#!/usr/bin/env python3
"""build/aura_governor.py — Der Aura-Governor. Der Resonanz-Koeffizient R_t, gemessen.

SPEZIFIKATION:  chapters/06_dephora-aura.md, Schicht B
GEBAUT:         16.07.2026 — vier Tage nachdem das Kapitel behauptete, dieses Skript laufe bereits.

================================================================================
WAS AUS DER SPEZIFIKATION UEBERNOMMEN IST
================================================================================
  * Die Formel:       R_t = alpha*K_sim + beta*I_align + gamma*E_pass
  * Die Gewichte:     alpha=0.4 (Wissen), beta=0.4 (Wollen), gamma=0.2 (Koennen); Summe = 1.0
  * Der Schwellwert:  R_t >= 0.90 -> Resonanz, Release frei. R_t < 0.90 -> Divergenz, blockiert.
  * Die Bones-Ordnung 322.
  * Das Dreieck:      Wissen (k_sim) · Wollen (i_align) · Koennen (e_pass).

================================================================================
WAS BEWUSST ANDERS IST — UND WARUM
================================================================================
1. KEINE SIMULIERTEN EINGABEN.
   Die Spezifikation schreibt woertlich:

       # Simuliere die Berechnung des Resonanz-Koeffizienten R_t
       r_t = self.calculate_resonance_coefficient(k_sim=0.95, i_align=0.98, e_pass=1.0)

   Drei Konstanten. Damit ist R_t immer 0.972 — das Gate kann NIE ausloesen. Ein Governor,
   dessen Eingaben feststehen, misst nichts; er behauptet. Das bricht Regel 4 des Hauses
   ("Miss, bevor du behauptest. Keine Zahl ohne Messung — und wenn die Zahl nicht da ist,
   schreib hin, DASS sie nicht da ist, nicht eine plausible"), und zwar im Quelltext genau
   des Kapitels, das die Regel formalisiert. Dieses Modul misst die drei Ecken am realen
   Zustand des Repositoriums. Jede Zahl unten hat eine Herkunft, die im Bericht steht.

2. KEIN DAEMON.
   Die Spezifikation laesst eine Endlosschleife mit 2.4-Sekunden-Takt laufen, die nichts
   pollt. Dasselbe Kapitel sagt aber selbst, wann R_t gebraucht wird: "Der PROJECTMANAGER
   berechnet den Koeffizienten R_t VOR JEDEM RELEASE-VERSUCH." Genau das ist dies: ein Gate,
   kein Hintergrundgeraeusch. Exit 0 = Resonanz. Exit 1 = Divergenz.

3. KEIN PASSWORT, KEIN SCHLUESSEL IM QUELLTEXT.
   Die Spezifikation traegt `handshake_word = "madonna"` und einen `gpg_key_seal`-String.
   Das Repositorium ist oeffentlich; Secrets gehoeren nie in den Code (Non-Negotiable).
   Der genannte "Schluessel" ist ohnehin Dekoration — die Zeichenfolge ist der bekannte
   SHA-256 von "test". Beides ist entfallen. Die menschliche Freigabe leistet das
   Review-Gate mit einem echten Menschen, nicht ein Wort in einer Datei.

4. E_PASS MISST DEN BUILD, NICHT UNIT-TESTS.
   Die Spezifikation definiert E_pass als "Bestehensquote der automatisierten Unit-Tests".
   Dieses Repositorium hat keine Unit-Tests. Es hat genau eine automatisierte Pruefung: den
   Compiler. Der Bericht nennt darum immer den Nenner ("1 von 1 Pruefung"), damit niemand
   eine Testabdeckung liest, die es nicht gibt. Das ist eine offene Luecke, kein erfuellter
   Wert.

Aufruf:  python build/aura_governor.py [--json]
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HIER)
AUDIT = os.path.join(ROOT, "docs", "AUDIT-BAND-1.md")
TEILE_ORDNER = ("frontmatter", "chapters", "backmatter")

BONES = 322
SCHWELLE = 0.90
ALPHA, BETA, GAMMA = 0.4, 0.4, 0.2  # Wissen, Wollen, Koennen — Summe 1.0

RE_BASE64 = re.compile(r"^\[image\d+\]: <data:image/", re.M)
RE_IMGREF = re.compile(r"!\[\]\[image\d+\]")
RE_CODESPAN = re.compile(r"`[^`\n]*`")
RE_AUDIT_ZEILE = re.compile(r"^\|\s*\*\*(P[01]-[0-9][^*|]*)\*\*\s*\|\s*([^|]+)\|", re.M)


def _teile() -> list[str]:
    pfade = []
    for ordner in TEILE_ORDNER:
        p = os.path.join(ROOT, ordner)
        if os.path.isdir(p):
            pfade += [os.path.join(p, f) for f in sorted(os.listdir(p)) if f.endswith(".md")]
    return pfade


def messe_wissen() -> tuple[float, dict]:
    """K_sim — Wissen. Wissen, das keine Maschine lesen kann, hat das Werk nicht.

    Gemessen: Anteil der Teile, deren Wissen vollstaendig maschinenlesbar ist.
    Defekt = eingebettete base64-Bilder oder Bildreferenzen ohne Text-Entsprechung.
    (Referenzen INNERHALB von Code-Spans zaehlen nicht — das ist Text ueber eine Referenz,
    keine Referenz. Genau so steht sie im Prolog-Nachklang als Gestaendnis.)
    """
    teile = _teile()
    defekt = []
    for pfad in teile:
        text = open(pfad, encoding="utf-8").read()
        b64 = len(RE_BASE64.findall(text))
        refs = len(RE_IMGREF.findall(RE_CODESPAN.sub("", text)))
        if b64 or refs:
            defekt.append({"teil": os.path.relpath(pfad, ROOT).replace("\\", "/"),
                           "base64": b64, "bildrefs": refs})
    k = 1.0 - (len(defekt) / len(teile)) if teile else 0.0
    return k, {"teile": len(teile), "defekte_teile": len(defekt), "details": defekt}


def messe_wollen() -> tuple[float, dict]:
    """I_align — Wollen. Deckt sich die Arbeit mit dem erklaerten Willen?

    Der erklaerte Wille steht im Audit. Gemessen: Anteil der dort gefuehrten Befunde,
    die geschlossen sind. Offen (○ / ⚠) zaehlt voll, teilweise (◐) halb.
    """
    if not os.path.exists(AUDIT):
        return 0.0, {"fehler": "docs/AUDIT-BAND-1.md nicht gefunden"}
    text = open(AUDIT, encoding="utf-8").read()
    befunde, offen = [], 0.0
    for name, status in RE_AUDIT_ZEILE.findall(text):
        if "✅" in status:
            gewicht = 0.0
        elif "◐" in status:
            gewicht = 0.5
        elif "○" in status or "⚠" in status:
            gewicht = 1.0
        else:
            continue
        offen += gewicht
        befunde.append({"befund": name.strip(), "offen": gewicht})
    if not befunde:
        return 0.0, {"fehler": "keine Befunde im Audit erkannt"}
    i = 1.0 - (offen / len(befunde))
    return i, {"befunde": len(befunde), "offen_gewichtet": round(offen, 2),
               "details": [b for b in befunde if b["offen"] > 0]}


def messe_koennen() -> tuple[float, dict]:
    """E_pass — Koennen. Laeuft es wirklich, oder steht es nur da?

    Gemessen: Anteil der bestandenen automatisierten Pruefungen. Dieses Repositorium hat
    genau eine — den Compiler. Der Nenner steht im Bericht, damit niemand eine Testabdeckung
    hineinliest, die es nicht gibt.
    """
    pruefungen = [("build/build_book.py", [sys.executable, os.path.join(HIER, "build_book.py")])]
    bestanden, details = 0, []
    for name, cmd in pruefungen:
        try:
            p = subprocess.run(cmd, cwd=ROOT, capture_output=True, timeout=180)
            ok = p.returncode == 0
        except Exception as e:  # noqa: BLE001 — jede Ausnahme ist ein Nichtbestehen
            ok, p = False, None
            details.append({"pruefung": name, "bestanden": False, "fehler": str(e)})
            continue
        bestanden += int(ok)
        details.append({"pruefung": name, "bestanden": ok,
                        "exit": p.returncode if p else None})
    e = bestanden / len(pruefungen)
    return e, {"pruefungen_gesamt": len(pruefungen), "bestanden": bestanden, "details": details}


def resonanz(k_sim: float, i_align: float, e_pass: float) -> float:
    """R_t = alpha*K_sim + beta*I_align + gamma*E_pass — die Formel aus Kapitel VI, unveraendert."""
    return (ALPHA * k_sim) + (BETA * i_align) + (GAMMA * e_pass)


def main() -> int:
    als_json = "--json" in sys.argv
    k, k_d = messe_wissen()
    i, i_d = messe_wollen()
    e, e_d = messe_koennen()
    r_t = resonanz(k, i, e)
    in_resonanz = r_t >= SCHWELLE

    bericht = {
        "zeitpunkt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "bones": BONES,
        "gewichte": {"alpha_wissen": ALPHA, "beta_wollen": BETA, "gamma_koennen": GAMMA},
        "wissen_k_sim": round(k, 4), "wollen_i_align": round(i, 4), "koennen_e_pass": round(e, 4),
        "R_t": round(r_t, 4), "schwelle": SCHWELLE,
        "urteil": "RESONANZ" if in_resonanz else "DIVERGENZ",
        "messung": {"wissen": k_d, "wollen": i_d, "koennen": e_d},
    }

    if als_json:
        print(json.dumps(bericht, ensure_ascii=False, indent=2))
        return 0 if in_resonanz else 1

    print(f"[+] AURA-GOVERNOR — Resonanz-Koeffizient (Bones {BONES})")
    print(f"    {bericht['zeitpunkt']}\n")
    print(f"  Wissen   K_sim   = {k:.4f}   ({k_d['teile'] - k_d['defekte_teile']}/{k_d['teile']} Teile maschinenlesbar)")
    for d in k_d.get("details", []):
        print(f"             ! {d['teil']}: {d['base64']} base64, {d['bildrefs']} Bildrefs")
    print(f"  Wollen   I_align = {i:.4f}   ({i_d.get('offen_gewichtet')} von {i_d.get('befunde')} Audit-Befunden offen)")
    for d in i_d.get("details", []):
        print(f"             ! offen ({d['offen']}): {d['befund']}")
    print(f"  Koennen  E_pass  = {e:.4f}   ({e_d['bestanden']}/{e_d['pruefungen_gesamt']} Pruefung — dieses Repo hat keine Unit-Tests)")
    for d in e_d.get("details", []):
        if not d["bestanden"]:
            print(f"             ! FEHLGESCHLAGEN: {d['pruefung']}")
    print(f"\n  R_t = {ALPHA}*{k:.4f} + {BETA}*{i:.4f} + {GAMMA}*{e:.4f} = {r_t:.4f}")
    if in_resonanz:
        print(f"  [+] RESONANZ: R_t = {r_t:.4f} >= {SCHWELLE}. Der Release ist frei.")
        return 0
    print(f"  [-] DIVERGENZ: R_t = {r_t:.4f} < {SCHWELLE}. Der Release ist blockiert.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
