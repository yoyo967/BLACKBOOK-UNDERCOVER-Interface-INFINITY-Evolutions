#!/usr/bin/env python3
"""BLACKBOOK UNDERCOVER — Book Compiler.

Fuehrt das Werk zu EINER Markdown-Datei zusammen (dist/compiled_book.md), mit Seitenumbruch
zwischen den Teilen (LaTeX \\newpage). Liest metadata.json und schreibt eine Build-Summary.

Reihenfolge:  frontmatter/  ->  chapters/  ->  backmatter/

  * frontmatter und backmatter sind EXPLIZIT geordnet (siehe FRONTMATTER / BACKMATTER unten).
    Die Reihenfolge eines Buches ist eine Entscheidung, kein Zufall des Alphabets:
    `vorwort.md` muss vor `the-all-seeing-eye.md` stehen, sortiert() wuerde es umdrehen.
  * chapters/ wird sortiert eingesammelt — die numerischen Praefixe (00, 00b, 01..18, 99)
    ergeben die richtige Folge, neue Kapitel reihen sich von selbst ein.

DAS GATE (siehe backmatter/die-methode.md, Regel 3 — "Setz das Gate dorthin, wo die Folge steht"):
Liegt in frontmatter/ oder backmatter/ eine .md-Datei, die NICHT in der Liste steht, bricht der
Build ab. Grund: Bis zum 16.07.2026 sammelte dieser Compiler ausschliesslich chapters/ ein. Das
Vorwort — mit der Lesekarte "Das Dreieck", dem Schluessel zum ganzen Werk — war deshalb im Repo,
aber nicht im Buch. Ebenso die Ouvertuere, die Methode, der Codex, das Glossar. Sechs Dateien,
lautlos, ueber Monate. Ein fehlender Teil muss LAUT scheitern, nicht still fehlen.

Aufruf:  python build/build_book.py
"""

from __future__ import annotations

import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HIER)
META = os.path.join(ROOT, "metadata.json")
DIST = os.path.join(ROOT, "dist")
OUT = os.path.join(DIST, "compiled_book.md")

# --- Die Ordnung des Werks (explizit, absichtlich, aenderbar nur hier) -------------------

FRONTMATTER = [
    "vorwort.md",              # die Lesekarte: das Dreieck, drei Ebenen, "Hoffnung ist keine Strategie"
    "the-all-seeing-eye.md",   # Ouvertuere
]

BACKMATTER = [
    "die-methode.md",          # die extrahierbare Fassung — acht Regeln. Wer anwenden will, faengt hier an.
    "codex.md",
    "glossar.md",
    "soundtrack.md",
]

TEILE = [("frontmatter", FRONTMATTER), ("chapters", None), ("backmatter", BACKMATTER)]

SEITENUMBRUCH = "\n\n```{=latex}\n\\newpage\n```\n\n"


def dateien_des_teils(ordner: str, liste: list[str] | None) -> list[str]:
    """Liefert die Dateien eines Teils in der richtigen Reihenfolge — und laesst nichts stillschweigend fallen."""
    pfad = os.path.join(ROOT, ordner)
    if not os.path.isdir(pfad):
        print(f"FEHLER: Ordner fehlt: {ordner}/", file=sys.stderr)
        sys.exit(1)

    vorhanden = {f for f in os.listdir(pfad) if f.endswith(".md")}
    if not vorhanden:
        print(f"FEHLER: keine .md-Dateien in {ordner}/ gefunden.", file=sys.stderr)
        sys.exit(1)

    if liste is None:  # chapters/: numerische Praefixe sortieren korrekt
        return sorted(vorhanden)

    fehlend = [f for f in liste if f not in vorhanden]
    if fehlend:
        print(f"FEHLER: in {ordner}/ gelistet, aber nicht vorhanden: {', '.join(fehlend)}", file=sys.stderr)
        sys.exit(1)

    # Das Gate: was da liegt und nicht gelistet ist, wuerde stumm aus dem Buch fallen.
    ungelistet = sorted(vorhanden - set(liste))
    if ungelistet:
        print(f"FEHLER: {ordner}/ enthaelt Dateien, die in build/build_book.py nicht gelistet sind:", file=sys.stderr)
        for f in ungelistet:
            print(f"        - {f}", file=sys.stderr)
        print("        Trag sie in FRONTMATTER/BACKMATTER ein — oder loesche sie.", file=sys.stderr)
        print("        Ein Teil des Werks darf nicht lautlos fehlen. (Regel 3: das Gate steht, wo die Folge steht.)",
              file=sys.stderr)
        sys.exit(1)

    return list(liste)


def compile_book() -> str:
    os.makedirs(DIST, exist_ok=True)
    with open(META, encoding="utf-8") as f:
        meta = json.load(f)

    plan: list[tuple[str, str]] = []
    for ordner, liste in TEILE:
        for name in dateien_des_teils(ordner, liste):
            plan.append((ordner, name))

    print(f"Kompiliere: {meta['title']} v{meta.get('version', '?')} — {len(plan)} Teile")

    teile: list[str] = []
    for i, (ordner, name) in enumerate(plan):
        with open(os.path.join(ROOT, ordner, name), encoding="utf-8") as cf:
            teile.append(cf.read().strip())
        print(f"  + {ordner}/{name}")
        if i < len(plan) - 1:
            teile.append(SEITENUMBRUCH)  # Seitenumbruch nur im PDF

    with open(OUT, "w", encoding="utf-8") as out:
        out.write("\n\n".join(teile) + "\n")

    kb = os.path.getsize(OUT) // 1024
    zaehlung = {o: sum(1 for x, _ in plan if x == o) for o, _ in TEILE}
    print(f"\nOK -> {os.path.relpath(OUT, ROOT)} ({kb} KB)")
    print(f"     frontmatter: {zaehlung['frontmatter']} · chapters: {zaehlung['chapters']} · "
          f"backmatter: {zaehlung['backmatter']}")
    return OUT


if __name__ == "__main__":
    compile_book()
