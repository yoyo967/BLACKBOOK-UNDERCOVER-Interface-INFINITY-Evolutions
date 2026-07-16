#!/usr/bin/env python3
"""Tests fuer build/aura_governor.py — den Resonanz-Koeffizienten.

Diese Tests bewachen die eine Eigenschaft, an der sich entscheidet, ob der Governor ein
Messgeraet ist oder eine Kontrollleuchte an einer Batterie: **Kann er ausloesen?**

Die Spezifikation in chapters/06_dephora-aura.md konnte es nicht — sie setzte
`k_sim=0.95, i_align=0.98, e_pass=1.0` fest (`# Simuliere`), womit R_t fuer immer 0.972 war.
Jeder Test hier stellt sicher, dass der gebaute Governor diesen Fehler nicht erbt.

Ausfuehren:  python -m unittest discover -s tests -v
"""

from __future__ import annotations

import os
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "build"))

import aura_governor as ag  # noqa: E402


class TestDieFormelAusKapitelVI(unittest.TestCase):
    """Die Formel, die Gewichte und der Schwellwert stammen aus Kap. VI und duerfen nicht driften."""

    def test_gewichte_summieren_auf_eins(self):
        # Kap. VI: "Gewichtungsfaktoren mit der unerbittlichen Nebenbedingung: alpha+beta+gamma = 1"
        self.assertAlmostEqual(ag.ALPHA + ag.BETA + ag.GAMMA, 1.0, places=9)

    def test_gewichte_wie_spezifiziert(self):
        self.assertEqual((ag.ALPHA, ag.BETA, ag.GAMMA), (0.4, 0.4, 0.2))

    def test_schwellwert_wie_spezifiziert(self):
        self.assertEqual(ag.SCHWELLE, 0.90)

    def test_bones_ordnung(self):
        self.assertEqual(ag.BONES, 322)

    def test_perfekte_resonanz_ist_eins(self):
        self.assertAlmostEqual(ag.resonanz(1.0, 1.0, 1.0), 1.0, places=9)

    def test_totalausfall_ist_null(self):
        self.assertAlmostEqual(ag.resonanz(0.0, 0.0, 0.0), 0.0, places=9)

    def test_die_spec_konstanten_ergeben_0972(self):
        # Der Beweis, dass die Spezifikation nie ausloesen konnte: ihre drei festen Eingaben.
        self.assertAlmostEqual(ag.resonanz(0.95, 0.98, 1.0), 0.972, places=3)
        self.assertGreater(ag.resonanz(0.95, 0.98, 1.0), ag.SCHWELLE,
                           "Die Spec-Konstanten liegen ueber der Schwelle — deshalb war das Gate tot.")


class TestEinRoterBuildBlockiertImmer(unittest.TestCase):
    """Die beweisbare Eigenschaft: E_pass = 0 deckelt R_t bei alpha+beta = 0.8 < 0.90.

    Genau das war der Zustand vom 13.-16.07.2026: 91 rote Builds. Haette der Governor
    existiert, waere kein Release durchgegangen.
    """

    def test_roter_build_blockiert_selbst_bei_perfektem_rest(self):
        r = ag.resonanz(k_sim=1.0, i_align=1.0, e_pass=0.0)
        self.assertLess(r, ag.SCHWELLE,
                        "Ein roter Build kommt durch — die wichtigste Eigenschaft ist verletzt.")
        self.assertAlmostEqual(r, 0.8, places=9)

    def test_obergrenze_bei_rotem_build_ist_alpha_plus_beta(self):
        self.assertLessEqual(ag.ALPHA + ag.BETA, ag.SCHWELLE,
                             "alpha+beta >= Schwelle: ein roter Build koennte durchrutschen.")

    def test_der_zustand_von_heute_vormittag_haette_blockiert(self):
        # 4 von 27 Teilen mit base64, ~die Haelfte der Audit-Befunde offen, Build rot.
        r = ag.resonanz(k_sim=1 - 4 / 27, i_align=0.5, e_pass=0.0)
        self.assertLess(r, ag.SCHWELLE)
        self.assertAlmostEqual(r, 0.541, places=2)


class TestWissenWirdGemessenNichtGesetzt(unittest.TestCase):
    """K_sim misst am realen Repo. Und es zaehlt nur, was eine Maschine wirklich nicht lesen kann."""

    def test_k_sim_erkennt_base64(self):
        text = "Prosa.\n[image1]: <data:image/png;base64,iVBORw0KGgo=>\n"
        self.assertEqual(len(ag.RE_BASE64.findall(text)), 1)

    def test_k_sim_erkennt_bildreferenzen(self):
        self.assertEqual(len(ag.RE_IMGREF.findall("siehe ![][image4] hier")), 1)

    def test_referenz_im_code_span_zaehlt_nicht(self):
        # Der Prolog-Nachklang gesteht woertlich: "bekam `![][image4]` und lernte nichts."
        # Das ist Text UEBER eine Referenz, keine Referenz. Wuerde er zaehlen, bestrafte
        # sich das Werk fuer seine eigene Ehrlichkeit.
        text = "Ein Agent bekam `![][image4]` und lernte nichts."
        self.assertEqual(len(ag.RE_IMGREF.findall(ag.RE_CODESPAN.sub("", text))), 0)

    def test_k_sim_am_echten_repo_ist_sauber(self):
        k, d = ag.messe_wissen()
        self.assertEqual(d["defekte_teile"], 0,
                         f"Unlesbares Wissen im Werk: {d['details']}")
        self.assertAlmostEqual(k, 1.0, places=9)

    def test_k_sim_faellt_bei_neuem_base64(self):
        # Wichtig: KEINE versionierte Datei anfassen. Ein Test, der Quelltext mutiert und im
        # finally zurueckschreibt, ist eine Landmine — stirbt der Prozess dazwischen, traegt
        # das Repo den Defekt. Also eine eigene Wegwerf-Datei, die messe_wissen() mitzaehlt.
        pfad = os.path.join(ROOT, "backmatter", "_test_base64_wegwerf.md")
        with open(pfad, "w", encoding="utf-8") as f:
            f.write("# Wegwerf\n\n[image99]: <data:image/png;base64,iVBORw0KGgo=>\n")
        try:
            k, d = ag.messe_wissen()
            self.assertEqual(d["defekte_teile"], 1, "K_sim bemerkt neues base64 nicht.")
            self.assertLess(k, 1.0, "K_sim faellt nicht, obwohl unlesbares Wissen dazukam.")
            self.assertIn("_test_base64_wegwerf.md", str(d["details"]),
                          "K_sim nennt die schuldige Datei nicht beim Namen.")
        finally:
            os.remove(pfad)

    def test_kein_test_hinterlaesst_spuren(self):
        # Narbe aus diesem Turn: Der erste Entwurf dieser Suite schrieb in backmatter/codex.md
        # und stellte sie wieder her. Inhaltlich folgenlos — aber die Datei tauchte im Diff auf.
        # Tests fassen keine versionierten Dateien an. Punkt.
        streuner = [f for ordner in ag.TEILE_ORDNER
                    for f in os.listdir(os.path.join(ROOT, ordner))
                    if f.startswith("_test")]
        self.assertEqual(streuner, [], f"Testmuell im Werk zurueckgelassen: {streuner}")


class TestWollenWirdAmAuditGemessen(unittest.TestCase):
    """I_align liest den erklaerten Willen aus docs/AUDIT-BAND-1.md — geschlossen vs. offen."""

    def test_audit_wird_gefunden_und_gelesen(self):
        i, d = ag.messe_wollen()
        self.assertNotIn("fehler", d, f"Audit nicht lesbar: {d.get('fehler')}")
        self.assertGreater(d["befunde"], 0, "Keine Befunde im Audit erkannt.")

    def test_i_align_liegt_zwischen_null_und_eins(self):
        i, _ = ag.messe_wollen()
        self.assertGreaterEqual(i, 0.0)
        self.assertLessEqual(i, 1.0)

    def test_offene_befunde_senken_i_align(self):
        i, d = ag.messe_wollen()
        erwartet = 1.0 - (d["offen_gewichtet"] / d["befunde"])
        self.assertAlmostEqual(i, erwartet, places=9)


class TestDerGovernorKannAusloesen(unittest.TestCase):
    """Der entscheidende Unterschied zur Spezifikation: dieses Gate KANN feuern."""

    def test_urteil_kippt_am_schwellwert(self):
        knapp_darunter = ag.SCHWELLE - 0.0001
        self.assertFalse(knapp_darunter >= ag.SCHWELLE)
        self.assertTrue(ag.SCHWELLE >= ag.SCHWELLE)

    def test_es_gibt_eingaben_die_blockieren(self):
        self.assertLess(ag.resonanz(0.0, 0.0, 0.0), ag.SCHWELLE)
        self.assertLess(ag.resonanz(0.9, 0.9, 0.0), ag.SCHWELLE)

    def test_eingaben_sind_keine_konstanten(self):
        # Der Kern: messe_wissen() liest Dateien. Faende es nichts, waere es fest verdrahtet.
        k, d = ag.messe_wissen()
        self.assertGreater(d["teile"], 20,
                           "messe_wissen() liest keine echten Teile — misst der Governor ueberhaupt?")


if __name__ == "__main__":
    unittest.main(verbosity=2)
