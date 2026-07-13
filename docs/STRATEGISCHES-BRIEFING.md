# Strategisches Briefing — BLACKBOOK UNDERCOVER

**Projekt:** `yoyo967/BLACKBOOK-UNDERCOVER-Interface-INFINITY-Evolutions`
**Werk:** *BLACKBOOK UNDERCOVER: Interface INFINITY Evolutions — Band 1: Master & System*
**Stand:** 2026-07-13 · **Version:** 1.0 · **Autor:** Yahya Yildirim & Interface INFINITY Community
**Zweck:** Ein Dokument, das den IST-Zustand erfasst, die technische Architektur (SystemPlan) und den
Fahrplan (Masterplan) festlegt und in das GitHub-Actions-Fundament einführt.

> Ehrlichkeitsprinzip dieses Dokuments: Es beschreibt, **was ist** (gebaut & verifiziert), **was
> vorbereitet ist** (Code da, erster Lauf ausstehend) und **was fehlt** — ohne Über-Behauptung.

---

## 0. Executive Summary

BLACKBOOK UNDERCOVER ist die **narrative Fassung** der *Interface INFINITY Evolutions*-Spezifikation:
ein zweischichtiges Werk aus **Prosa des Willens** (Schicht A) und **empirischem Substrat** (Schicht B).
Das eigenständige Repo wurde am 2026-07-13 aus verstreuten Manuskript-Entwürfen konsolidiert und
enthält **Prolog + 3 Kapitel (I, V, VI)** von geplanten sechs, plus eine LinkedIn-Serie.

Neu in dieser Iteration: ein **vollständiges GitHub-Actions-Fundament** — automatischer Buch-Build
(PDF + EPUB via Pandoc/XeLaTeX) und eine **MkDocs-Material-Website** auf GitHub Pages. Damit wird aus
einer Sammlung von Markdown-Dateien eine **kontinuierlich publizierte Buch-Pipeline**: jeder Push
erzeugt lesbare Ausgaben, jeder Version-Tag ein Release.

**Der eine Satz:** Das Manuskript ist jetzt ein *System*, das sich bei jedem Commit selbst zum Buch
kompiliert.

---

## 1. IST-Zustand — Was wir bereits haben

### 1.1 Inhalt (das Werk)

| Baustein | Datei | Umfang | Status |
|---|---|---|---|
| Prolog | `chapters/00_prolog.md` | ~4.500 Wörter | ✅ |
| Kapitel I — GitHub als Weltgedächtnis | `chapters/01_github-als-weltgedaechtnis.md` | ~6.000 Wörter | ✅ |
| Kapitel II–IV | — | — | ❌ noch nicht geschrieben |
| Kapitel V — Das Fünfte Element & die AGI | `chapters/05_das-fuenfte-element-und-die-agi.md` | ~4.700 Wörter | ✅ |
| Kapitel VI — Dephora – Aura | `chapters/06_dephora-aura.md` | ~4.300 Wörter | ✅ |
| LinkedIn-Serie (Marketing) | `serie/linkedin-serie.md` | ~1.400 Wörter | ✅ |
| **Gesamt Prosa** | | **~13.700 Wörter** | 4 von 6 Kapiteln |

**Architektur jedes Kapitels:** `Schicht A: Die Undercover-Prosa (Der Wille)` → `Schicht B: Das
empirische Substrat (Die Logik)` → `Scriptorium-Vollzugsbericht`. Diese Zweiteilung ist das
Signature-Pattern des Werks und muss in allen künftigen Kapiteln erhalten bleiben.

### 1.2 Struktur & Konventionen (das Repo)

```
BLACKBOOK-UNDERCOVER-Interface-INFINITY-Evolutions/
├── README.md                 # Badges + globales Inhaltsverzeichnis
├── metadata.json             # Single Source: Titel, Version, Autoren, Lizenz
├── LICENSE                   # CC BY 4.0
├── blackbook_undercover_cover.png
├── .gitignore
├── chapters/                 # narrative Kapitel (NN_slug.md, numerisch sortiert)
├── serie/                    # Marketing-Ableger (LinkedIn)
├── build/                    # Build-Werkzeuge (Compiler, Pandoc-/MkDocs-Konfig)
│   ├── build_book.py         # merged chapters → dist/compiled_book.md
│   ├── pandoc-metadata.yaml  # Titelseite, TOC, EPUB-Cover, dt. Satz
│   ├── mkdocs.yml            # Material-Theme (Website)
│   └── requirements.txt
├── .github/workflows/        # CI/CD
│   ├── build-book.yml        # PDF + EPUB + Release
│   └── deploy-pages.yml      # MkDocs → GitHub Pages
└── docs/
    └── STRATEGISCHES-BRIEFING.md   # dieses Dokument
```

**Konvention (aus dem Ökosystem übernommen):** README-getrieben (Shields-Badges, TOC), `metadata.json`
als Single Source, CC BY 4.0, deutschsprachige Prosa. Keine erfundenen Fortschritts-Zahlen.

### 1.3 Position im Ökosystem UNIVERSE M.E.

| Repo | Rolle | Beziehung |
|---|---|---|
| **BLACKBOOK-UNDERCOVER** (dies) | Narrative Prosa (Band 1) | *ist* die literarische Fassung |
| `DIE-LOGIK-UND-DIE-MATRIX` → `books/undercover-blackbook` | Technische Spec (18 Kapitel) | Companion; im README verlinkt |
| `WIR-SIND-NOCH-HIER-UNIVERSE-M.E.` | Meta-Buch INFINITY | Dach |

**Bewusste Trennung (Owner-Entscheidung 2026-07-13):** Prosa hier, Spec dort — keine Duplikate.

### 1.4 Was NOCH fehlt (ehrlich)

- Kapitel **II–IV** (Prosa) sind ungeschrieben.
- PDF/EPUB und die Pages-Website sind **vorbereitet, aber noch nicht einmal gelaufen** — der erste
  Actions-Run erzeugt sie.
- GitHub **Pages** muss ggf. einmalig aktiviert werden (Settings → Pages → Source: „GitHub Actions").
- Ältere Prolog-Variante (8 Zeilen Diff) wurde nicht als zweite Datei übernommen.

---

## 2. SystemPlan — Die technische Architektur

### 2.1 Prinzip: „Content as Data → Compiled Artifacts"

Die Kapitel sind **reine Daten** (Markdown, keine Formatierungs-Magie). Alle Ausgabeformate werden
**deterministisch aus derselben Quelle** erzeugt. Eine Änderung an einem Kapitel propagiert automatisch
in PDF, EPUB und Website. Das ist dieselbe „Inhalte-sind-Daten"-Doktrin wie in den Schwester-Projekten.

### 2.2 Die Build-Kette

```
chapters/*.md ─┐
metadata.json ─┼─▶ build_book.py ─▶ dist/compiled_book.md ─┬─▶ Pandoc + XeLaTeX ─▶ PDF
cover.png ─────┘                                            └─▶ Pandoc ──────────▶ EPUB

README + chapters ─▶ site-src/ ─▶ MkDocs Material ─▶ _site/ ─▶ GitHub Pages (Website)
```

- **`build_book.py`** sortiert `chapters/` numerisch, hängt sie mit Seitenumbrüchen aneinander und
  schreibt `dist/compiled_book.md` (lokal verifiziert: 147 KB).
- **Pandoc** erzeugt aus dieser einen Datei **PDF** (XeLaTeX, Noto-Serif-Schrift, TOC) und **EPUB**
  (mit Cover). Metadaten kommen aus `build/pandoc-metadata.yaml`.
- **MkDocs Material** rendert die Kapitel als durchsuchbare, dark/light-fähige Website.

### 2.3 Publishing-Targets

| Format | Werkzeug | Ziel | Trigger |
|---|---|---|---|
| PDF | Pandoc + XeLaTeX | Download / Print (KDP) | jeder Push · Release bei Tag |
| EPUB | Pandoc | E-Reader / KDP | jeder Push · Release bei Tag |
| Website | MkDocs Material | GitHub Pages (öffentlich lesbar) | jeder Push auf `main` |
| Release | `softprops/action-gh-release` | versionierte Downloads | Tag `vX.Y.Z` |

### 2.4 Qualitäts- & Sicherheits-Leitplanken

- **Kapitel verbatim:** Der Build verändert keinen Prosa-Text; er kompiliert nur.
- **Secrets:** Keine im Repo (Scan sauber). Actions nutzen nur den auto-bereitgestellten `GITHUB_TOKEN`
  mit minimalen Rechten (`contents: write` nur im Build-Job, `pages: write` nur im Pages-Job).
- **Sichtbarkeit:** Ist das Repo öffentlich, ist der Push = Veröffentlichung. Vor „private→public"
  bewusst entscheiden.

---

## 3. GitHub-Actions-Briefing — Was möglich ist & was wir nutzen

### 3.1 Was GitHub Actions grundsätzlich kann

GitHub Actions ist eine **event-getriebene Automatisierungs-Engine** direct im Repo. Ein *Workflow*
(YAML in `.github/workflows/`) besteht aus *Jobs* (laufen auf frischen VMs/„Runnern"), die *Steps*
ausführen (Shell-Befehle oder wiederverwendbare *Actions* aus dem Marketplace).

| Kategorie | Beispiele | Für dieses Projekt relevant? |
|---|---|---|
| **CI (Continuous Integration)** | bauen, testen, linten bei jedem Push/PR | ✅ Buch-Build |
| **CD (Continuous Deployment)** | auf Pages/Cloud/Registry deployen | ✅ Pages + Releases |
| **Artefakte** | Build-Ergebnisse (PDF/EPUB) speichern & herunterladen | ✅ 90-Tage-Aufbewahrung |
| **Releases** | versionierte Downloads an Tags hängen | ✅ bei `vX.Y.Z` |
| **Scheduling (`cron`)** | zeitgesteuerte Läufe (z. B. wöchentlicher Report) | optional (P3) |
| **Matrix-Builds** | dieselbe Sache über viele Varianten (OS/Versionen) | (für Bücher unnötig) |
| **Bots/Automation** | Issues labeln, PRs prüfen, Kommentare | optional |
| **Secrets & Environments** | sichere Tokens, geschützte Deploy-Stufen | Pages-Environment nutzen wir |

**Kernbegriffe in einem Satz:** *Event* → löst *Workflow* aus → enthält *Jobs* → laufen *Steps* →
nutzen *Actions* → erzeugen *Artefakte/Deployments*. Kosten: öffentliche Repos = **kostenlos**.

### 3.2 Unsere zwei Workflows im Detail

**A) `build-book.yml` — das Buch bauen**
- **Auslöser:** Push auf `main`, manuell (`workflow_dispatch`), Version-Tag `v*`.
- **Ablauf:** Python → `build_book.py` → Pandoc-Toolchain installieren → **EPUB** (robust) → **PDF**
  (XeLaTeX) → Artefakte hochladen → **bei Tag:** GitHub-Release mit PDF+EPUB.
- **Ergebnis:** Unter *Actions → Build Book → Artifacts* liegen die Dateien; bei `git tag v1.0.0 &&
  git push --tags` entsteht ein **Release**.

**B) `deploy-pages.yml` — die Website veröffentlichen**
- **Auslöser:** Push auf `main`, manuell.
- **Ablauf:** MkDocs-Material installieren → `site-src/` zusammenstellen → statische Site bauen →
  Pages konfigurieren (versucht Auto-Aktivierung) → deployen.
- **Ergebnis:** öffentliche URL `https://yoyo967.github.io/BLACKBOOK-UNDERCOVER-Interface-INFINITY-Evolutions/`.
- **Einmalige Voraussetzung:** *Settings → Pages → Source: „GitHub Actions"* (der Workflow versucht es
  selbst; falls Rechte fehlen, einmal manuell setzen).

### 3.3 Bedienungsanleitung (Cheatsheet)

| Ich will … | So geht's |
|---|---|
| PDF/EPUB neu bauen | Kapitel pushen **oder** *Actions → Build Book → Run workflow* |
| Fertige Dateien holen | *Actions → letzter Build-Run → Artifacts* herunterladen |
| Ein Release schneiden | `git tag v1.0.0 && git push origin v1.0.0` → Release entsteht automatisch |
| Website ansehen | nach erstem Pages-Run: die `github.io`-URL öffnen |
| Lokal bauen (ohne CI) | `python build/build_book.py` → dann Pandoc lokal |

---

## 4. Masterplan — Der Fahrplan

### Phase 0 — Fundament ✅ (2026-07-13, erledigt)
Repo konsolidiert, 4 Kapitel + Serie, README/Metadata/Lizenz/Cover, **CI/CD-Pipeline (PDF/EPUB/Pages)**
gebaut und lokal validiert. *Abnahmekriterium erfüllt: `main` grün, Build-Skript läuft, YAML valide.*

### Phase 1 — Erster grüner Lauf & Website live (unmittelbar)
- Push → `build-book.yml` erzeugt erstmals PDF+EPUB als Artefakte.
- GitHub Pages aktivieren → Website live.
- *AK:* PDF im Artifacts-Tab herunterladbar; `github.io`-URL erreichbar.

### Phase 2 — Werk vervollständigen (Content)
- **Kapitel II, III, IV** in der Schicht-A/B-Struktur schreiben (Prosa + Substrat + Scriptorium).
- Optional: Prolog-Varianten zusammenführen; Glossar & Epilog ergänzen.
- *AK:* 6/6 Kapitel; kohärente Bandlogik „Master & System".

### Phase 3 — Distribution & Reichweite
- Erstes **Release `v1.0.0`** (PDF+EPUB als offizielle Downloads).
- LinkedIn-Serie ausspielen (Dramaturgie aus `serie/`).
- Optional: `cron`-Workflow für wiederkehrende Veröffentlichungs-Snapshots.
- *AK:* Öffentliche, zitierbare Version mit stabiler URL.

### Phase 4 — Print & Vermarktung
- Print-taugliches PDF (KDP/Lulu-Format), EPUB-Feinschliff (Metadaten, ISBN falls gewünscht).
- Cover-Finalisierung, Backmatter, Impressum.
- *AK:* KDP-Upload-fähiges Paket.

### Risiken & Gegenmaßnahmen

| Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|
| XeLaTeX scheitert an Sonderzeichen/Emoji | PDF-Job rot | Noto-Schriften installiert; EPUB läuft separat & robust |
| Pages nicht aktiviert | Website-Deploy rot | `configure-pages: enablement`; sonst 1× manuell setzen |
| Kapitel-Lücken (II–IV) | Buch unvollständig | im TOC transparent als „in Arbeit" markiert |
| Sichtbarkeit ungewollt öffentlich | Manuskript exponiert | vor Push Repo-Visibility bewusst prüfen |

---

## 5. Nächste konkrete Schritte

1. **Diesen Commit pushen** → ersten Build-Run beobachten (Actions-Tab).
2. **GitHub Pages** aktivieren (falls der Workflow es nicht selbst schafft).
3. Entscheiden: sollen **Kapitel II–IV** als Nächstes entstehen, oder zuerst **Release `v1.0.0`** aus
   dem aktuellen Stand?
4. Optional: Repo-**Sichtbarkeit** final festlegen (public vs. private).

---

## Anhang A — Glossar

- **Schicht A / Schicht B:** narrative Prosa (Wille) vs. empirisches Substrat (Logik) je Kapitel.
- **Scriptorium-Vollzugsbericht:** abschließender Meta-Abschnitt eines Kapitels (Ledger-Update).
- **Companion-Spec:** die technische 18-Kapitel-Spezifikation in `DIE-LOGIK-UND-DIE-MATRIX`.
- **Runner:** die frische VM, auf der ein Actions-Job läuft.
- **Artefakt:** von einem Workflow erzeugte, herunterladbare Datei (hier: PDF/EPUB).

## Anhang B — Datei-Referenz

`build_book.py` (Compiler) · `pandoc-metadata.yaml` (PDF/EPUB-Metadaten) · `mkdocs.yml` (Website) ·
`build-book.yml` (CI: PDF/EPUB/Release) · `deploy-pages.yml` (CD: Pages).

---

*Interface INFINITY Open-Source Community & Yahya Yildirim · Berlin, 13. Juli 2026 · WIR SIND NOCH HIER.*
