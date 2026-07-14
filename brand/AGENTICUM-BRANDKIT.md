# AGENTICUM — G5 Leadmachines · Brand Kit
## Faithful Extraction (kein Re-Design)

> **Das Design gehört dem Autor.** Diese Datei *extrahiert* nur die Original-Marke von Agenticum —
> Single Source liegt im `leadmachine`-Repo (`ops/config/identity.json`, `apps/leadmachines-site/src/app/globals.css`,
> `leadmachines_branding_kit.md`). Hier gespiegelt, damit der Buch-Band die Marke kennt. **Nichts erfunden.**

---

## 1. Visuelle Richtung (Original-Kit)
- **Dark premium Glassmorphism.** Deep Navy / Onyx-Basis, **Cyan-Teal**-Lichtakzente.
- Starke Tiefe, geschichtete Reflexe, weicher Blur. Slow ambient parallax, subtiler Glow-Puls, sanftes
  Scroll-Reveal — **keine lauten Übergänge**.
- Clean **Grotesk**-Typografie, überdimensionierte Hero-Headline, starke Asymmetrie & Negativraum.

## 2. Farbtoken — as built (`globals.css`, autoritativ für die Live-Sprache)
| Token | Hex/Wert | Rolle |
|---|---|---|
| `--bg` | **#020617** | Background (Slate-950) |
| `--bg-elevated` | **#0f172a** | Card-Background (Slate-900) |
| `--bg-surface` | **#16233f** | deckende Kartenfläche |
| `--fg` | **#f8fafc** | Text (Slate-50) |
| `--fg-dim` | rgba(248,250,252,0.72) | Text sekundär |
| `--fg-mute` | **#94a3b8** | Subtext (Slate-400, AA) |
| `--line` | **#1e293b** | Border (Slate-800) |
| `--signal` | **#06b6d4** | Primär (CTA-Fill, Ring, Links) — Cyan-500 |
| `--signal-bright` | **#22d3ee** | Accent (Highlight/Hover/Text auf Dunkel) — Cyan-400 |
| `--signal-deep` | **#0e7490** | Tiefe / Text auf Hell (AA) — Cyan-700 |
| `--glow` | #06b6d4 | Glow-Quelle (Lumineszenz, kein Text) |
| `--radius` | **14px** | premium-weich |

> **Hinweis (ehrlich):** Das Original-Kit-Briefing nannte `accent-cyan #4BD7E9 / accent-teal #1FA7B8`;
> `identity.json` führt vereinfacht `accent #1D4ED8`. **Live/as-built ist Cosmic-Cyan `#06b6d4` / `#22d3ee`**
> (globals.css) — das ist die maßgebliche Sprache. Kein Gold, nie.

## 3. Glas-System (as built)
```
backdrop-filter: blur(24px) saturate(1.4);
background: linear-gradient(155deg, rgba(12,22,35,0.35), rgba(20,34,52,0.48));
border: 1px solid rgba(180,220,255,0.12);
box-shadow: inset 0 1px 1px rgba(255,255,255,0.12), 0 24px 80px rgba(0,0,0,0.45);
glow (strong): 0 0 40px rgba(6,182,212,0.18);
```
Tokens & Utilities: siehe `brand/agenticum-tokens.css` (1:1 aus `globals.css`).

## 4. Typografie
- **Display / Hero:** Space Grotesk (Grotesk, 72–110px, bold, tight leading).
- **Body:** Inter (Subline 24–32px, light, zentriert; leichtes positives Tracking auf Labels).
- **Mono:** JetBrains Mono (Code / MACHINE-Modus).

## 5. Symbol & Modi
- **Logo:** animiertes **Radar** (Detektion/Präzision) — die Marke von Agenticum G5 Leadmachines.
- **HUMAN/MACHINE-Switch:** `data-mode="machine"` → reines Schwarz, Mono, Grafik aus (maschinenlesbare Ansicht).
- **A11y:** Fokus-Doppelring Cyan `#22d3ee`; reduced-motion respektiert.

## 6. Compliance (auf jedem Asset)
DSGVO · EU AI Act (Art. 50: KI gekennzeichnet, menschliche Freigabe) · EU Data Act (offene Formate) ·
EU-Hosting `europe-west3`.

*Marke = Enabler. Nie als Reseller von Google/Claude/Gemini auftreten. WIR SIND NOCH HIER.*
