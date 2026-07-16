#!/usr/bin/env python3
"""Tests fuer build/build_book.py — den Compiler.

Jeder Test hier ist ein **Grabstein**. Er steht fuer einen Fehler, der am 16.07.2026 real war,
und er sorgt dafuer, dass genau dieser Fehler nie wieder still zurueckkommt. Kein Test misst
Abdeckung; jeder misst eine Narbe.

Ausfuehren:  python -m unittest discover -s tests -v
Ohne Fremdabhaengigkeiten (stdlib unittest) — die CI installiert kein pip-Paket dafuer.
"""

from __future__ import annotations

import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "build"))

import build_book  # noqa: E402


def kompiliere() -> str:
    """Baut das Werk und gibt den kompilierten Text zurueck."""
    build_book.compile_book()
    with open(os.path.join(ROOT, "dist", "compiled_book.md"), encoding="utf-8") as f:
        return f.read()


class TestDasWerkIstVollstaendig(unittest.TestCase):
    """Narbe (Eintrag XCVI): Der Compiler las NUR chapters/. Das gebaute Buch hatte kein Vorwort.

    Sechs Dateien fehlten lautlos ueber Monate — darunter die Lesekarte, die den Schluessel
    zum ganzen Werk traegt. Sie lagen im Repo. Sie waren nicht im Buch.
    """

    @classmethod
    def setUpClass(cls):
        cls.buch = kompiliere()

    def test_das_vorwort_ist_im_buch(self):
        self.assertIn("# **VORWORT**", self.buch,
                      "Das Buch hat kein Vorwort. Genau das war der Defekt vom 16.07.")

    def test_das_buch_beginnt_mit_dem_vorwort(self):
        erste = next(z for z in self.buch.splitlines() if z.startswith("# "))
        self.assertIn("VORWORT", erste,
                      f"Das Buch beginnt mit '{erste}' statt mit dem Vorwort.")

    def test_die_lesekarte_das_dreieck_ist_im_buch(self):
        for stueck in ("Das Dreieck", "MASTER — der Wille", "SYSTEM — die Logik",
                       "MATRIX — das Management", "Hoffnung ist keine Strategie"):
            self.assertIn(stueck, self.buch,
                          f"Die Lesekarte fehlt im Buch: '{stueck}' nicht gefunden.")

    def test_die_methode_ist_im_buch(self):
        self.assertIn("DIE METHODE", self.buch,
                      "backmatter/die-methode.md fehlt im Buch.")

    def test_die_ouvertuere_ist_im_buch(self):
        self.assertIn("Schicht A", self.buch)  # jede Ouvertuere/Kapitel traegt die Dual-Layer-Form

    def test_alle_teile_aus_allen_drei_ordnern(self):
        plan = []
        for ordner, liste in build_book.TEILE:
            plan += build_book.dateien_des_teils(ordner, liste)
        self.assertGreaterEqual(len(plan), 25, "Zu wenige Teile — sammelt der Compiler alles ein?")


class TestDieOrdnungIstEineEntscheidung(unittest.TestCase):
    """Narbe: sorted() haette 'the-all-seeing-eye.md' VOR 'vorwort.md' gestellt.

    Die Reihenfolge eines Buches darf kein Zufall des Alphabets sein.
    """

    def test_vorwort_kommt_vor_der_ouvertuere(self):
        self.assertLess(build_book.FRONTMATTER.index("vorwort.md"),
                        build_book.FRONTMATTER.index("the-all-seeing-eye.md"),
                        "Das Vorwort muss vor der Ouvertuere stehen — alphabetisch waere es umgekehrt.")

    def test_die_methode_steht_zuerst_im_backmatter(self):
        self.assertEqual(build_book.BACKMATTER[0], "die-methode.md",
                         "Wer anwenden statt lesen will, faengt bei der Methode an.")

    def test_frontmatter_vor_chapters_vor_backmatter(self):
        self.assertEqual([o for o, _ in build_book.TEILE],
                         ["frontmatter", "chapters", "backmatter"])

    def test_kapitel_in_richtiger_folge(self):
        k = build_book.dateien_des_teils("chapters", None)
        self.assertTrue(k[0].startswith("00_prolog"), f"Erstes Kapitel ist {k[0]}")
        self.assertTrue(k[1].startswith("00b_"), f"Zweites Kapitel ist {k[1]}")
        self.assertTrue(k[-1].startswith("99_epilog"), f"Letztes Kapitel ist {k[-1]}")


class TestDasGateFeuert(unittest.TestCase):
    """Narbe (Regel 3): Ein Teil des Werks darf nicht lautlos fehlen — er muss LAUT scheitern."""

    def test_ungelistete_datei_bricht_den_build_ab(self):
        pfad = os.path.join(ROOT, "backmatter", "_test_ungelistet.md")
        with open(pfad, "w", encoding="utf-8") as f:
            f.write("# Testdatei — darf nicht stillschweigend aus dem Buch fallen.\n")
        try:
            p = subprocess.run([sys.executable, os.path.join(ROOT, "build", "build_book.py")],
                               cwd=ROOT, capture_output=True, text=True, timeout=120)
            self.assertNotEqual(p.returncode, 0,
                                "Der Build laeuft trotz ungelisteter Datei durch — das Gate feuert nicht.")
            self.assertIn("nicht gelistet", p.stderr,
                          "Das Gate nennt die Datei nicht beim Namen.")
        finally:
            os.remove(pfad)

    def test_nach_dem_aufraeumen_ist_der_build_wieder_gruen(self):
        p = subprocess.run([sys.executable, os.path.join(ROOT, "build", "build_book.py")],
                           cwd=ROOT, capture_output=True, timeout=120)
        self.assertEqual(p.returncode, 0, "Der Build ist rot, obwohl nichts fehlt.")


class TestKeinUnlesbaresWissen(unittest.TestCase):
    """Narbe (Eintraege XCIV/XCVIII): Die Merkle-Formeln waren base64-PNGs.

    Das Beweissubstrat eines Werks, dessen These 'klone es, pruefe es' lautet, war die einzige
    Stelle, die keine Maschine lesen konnte. Es hat ein Kapitel zum Interludium degradiert,
    weil das pruefende System seine Kernaussage nicht sehen konnte.
    """

    def test_keine_eingebetteten_base64_bilder(self):
        treffer = []
        for ordner, liste in build_book.TEILE:
            for name in build_book.dateien_des_teils(ordner, liste):
                pfad = os.path.join(ROOT, ordner, name)
                with open(pfad, encoding="utf-8") as f:
                    for nr, zeile in enumerate(f, 1):
                        if zeile.startswith("[image") and "base64," in zeile:
                            treffer.append(f"{ordner}/{name}:{nr}")
        self.assertEqual(treffer, [],
                         "Wissen in Bildern gesperrt — keine Maschine kann es lesen:\n  "
                         + "\n  ".join(treffer))


if __name__ == "__main__":
    unittest.main(verbosity=2)
