# Agenticum Design System

Design system for **Agenticum — G5 Leadmachines**, extracted for the book-cover production of
**BLACKBOOK UNDERCOVER: Interface INFINITY Evolutions** (Band 1 — *Die finale Konvergenz*), by Yahya
Yildirim. Agenticum is the author's own build studio and the book's founding sponsor/imprint — its
"Dark premium Glassmorphism" digital brand (Slate-950 base, Cosmic-Cyan signal) is the **only** visual
language used across this system: book covers, chapter openers, and any companion collateral.

## Sources
- **yoyo967/BLACKBOOK-UNDERCOVER-Interface-INFINITY-Evolutions** (GitHub, `main`) — the book's content repo.
  Brand tokens were mirrored faithfully from `brand/AGENTICUM-BRANDKIT.md` and `brand/agenticum-tokens.css`
  in that repo (itself a mirror of Agenticum's own `leadmachine` codebase, not directly accessible here).
  Explore further: `chapters/`, `frontmatter/`, `brain/` (worldbuilding canon), `backmatter/`.
- Companion technical spec: `github.com/yoyo967/DIE-LOGIK-UND-DIE-MATRIX` (Swarm Governance Specification).
- Readers with access to the `leadmachine` repo itself (`ops/config/identity.json`,
  `apps/leadmachines-site/src/app/globals.css`) can cross-check these tokens against the live site for
  even greater fidelity — this system currently mirrors the brandkit's documented "as-built" values.

No logo file was found in the source repo — **no mark was invented**. Wherever a logo would sit, the
brand name is set in type (see `guidelines/brand-wordmark.html`); the "all-seeing eye / radar" motif
(concentric rings) stands in as the one recurring graphic device, per the brand brief.

## Font substitution note
Space Grotesk, Inter and JetBrains Mono are the brand's declared fonts and are all standard Google
Fonts — loaded here via `@font-face` against Google's font CDN (no local binaries were provided). If you
have the exact licensed font files, drop them into an `assets/fonts/` folder and repoint the `src: url()`
in `tokens/typography.css`.

## Components
- **Core** (`components/core/`) — `Button`, `Badge`, `GlassCard`, `Divider`, `DualLayerBlock`
- **Book** (`components/book/`) — `RadarMotif`, `ChapterKicker`, `QRPanel`

No component library existed in the source (it's a book/content repo, not an app codebase), so this is
an intentionally small, from-scratch set sized to what the brand and the book-cover deliverable actually
need — not a generic UI kit.

### Intentional additions
- `DualLayerBlock` — added to embody the book's recurring "Schicht A (Wille) / Schicht B (Logik)"
  two-layer device (light pane vs. dark pane), which is core to this brand's content structure but has
  no generic UI-kit equivalent.
- `RadarMotif`, `ChapterKicker`, `QRPanel` — book-cover-specific primitives (leitmotif, kicker line,
  back-cover repo pointer) drawn straight from the cover brief in the book's own repo.

## Content fundamentals
- **Voice:** German, literary and declarative — long, cadenced sentences with heavy em-dashes and
  colons; register swings from "narrative prosa" (mythic, second-person "du") to "empirisches Substrat"
  (terse, technical, first-person-plural "wir"). The book's own device: *"Schicht A: die narrative Prosa
  des Willens · Schicht B: das empirische Substrat der Logik."*
- **Back-cover copy is direct and non-hyperbolic:** short paragraphs, a plain claim, then an honesty
  caveat immediately after — e.g. *"Ein Grundstein, ehrlich benannt — keine behauptete Reichweite, kein
  fertiges Weltreich."* Never invents reviews, awards, or numbers; placeholders are marked, not guessed.
- **Casing:** ALL-CAPS for the main title and kicker lines (mono, tracked-out); sentence case for body
  prose; no exclamation points.
- **No emoji** anywhere in the brand voice or on covers. The source book's own README does use emoji
  sparingly (⭐ 💛 🐇) in its GitHub-facing sections — that's the *repo's* community-facing register, not
  the print/cover register, and is not carried into this design system.
- **Compliance is stated plainly, not hidden:** EU AI Act Art. 50 co-authorship disclosure, CC BY-NC-ND 4.0,
  and the "Agenticum is the author's own studio, not independent validation" disclaimer are treated as
  first-class copy, not fine print.

## Visual foundations
- **Palette:** one dark base (`#020617` Slate-950) with a single cyan signal family
  (`#06b6d4` / `#22d3ee` / `#0e7490`). No gold, no warm metals, no second accent hue — this is a hard
  brand rule (§3 of the brief: *"KEIN Gold, keine warmen Metalltöne"*).
  Neutrals are Slate 950→50 for backgrounds, cards, borders and text.
- **Type:** Space Grotesk (display/titles, bold, tight leading, often with a soft cyan text-glow via
  `text-shadow`), Inter (body/back-cover copy, light weight, generous line-height), JetBrains Mono
  (labels, kickers, ledger/repo lines, always uppercase + wide tracking when used as a label).
- **Backgrounds:** flat Slate-950, occasionally with a very subtle radial glow (`#0a2233 → transparent`)
  behind the title block — never a busy gradient, never a stock photo. A faint 40px grid overlay
  (`rgba(6,182,212,.05)` lines) is acceptable behind cover title panels for a "HUD/ledger" texture.
- **Glassmorphism:** the signature surface (`.glass` / `.glass-strong` in `tokens/effects.css`) —
  24px backdrop blur + 1.4–1.5 saturation, a 155° two-stop gradient fill, a barely-there cyan-tinted
  border (`rgba(180,220,255,.12)`), inset top highlight, and an outer soft shadow. `.glass-strong` adds
  an ambient `0 0 40px rgba(6,182,212,.18)` glow — use once per composition, never on every panel.
- **Corner radius:** 14px is the brand default (`--radius`); 8px for small chips, 20px for large hero
  panels, full/pill for buttons and tags.
- **Animation:** slow and ambient only — a soft pulse on the radar motif's center point (~2.4s
  ease-in-out), gentle parallax/scroll-reveal per the original brandkit. No bounces, no fast easings,
  reduced-motion is respected.
- **Hover/press states:** hover brightens (signal → signal-bright fill, or border brightens to signal);
  press states are not elaborated in the source brand kit — treat as a further-brightened, slightly
  scaled-down state consistent with the hover direction, nothing jarring.
- **Borders & shadows:** hairline 1px borders in `--line` (`#1e293b`) throughout; shadows are soft and
  large-radius (`0 24px 80px rgba(0,0,0,.45)`), never a hard drop shadow.
- **Layout:** asymmetric, generous negative space, one dominant focal element (the radar motif or the
  title) per composition — never a dense, evenly-weighted grid.
- **Imagery:** none in the source brand kit — no photography, no stock imagery, no illustrations. The
  book's own placeholder cover render (skull-and-crossbones over a rock texture, `blackbook_undercover_cover.png`
  in the source repo) is an early AI-generated draft, not part of the Agenticum brand kit, and is
  intentionally **not** carried into this system — it conflicts with the "no stock-photo optics, no
  literal skull/robot iconography" don'ts in the brief. This system instead builds the specified
  concentric-ring "all-seeing eye" leitmotif.
- **Transparency/blur:** reserved for the glass panel system described above — not used for arbitrary
  translucent overlays elsewhere.

## Iconography
No icon font, sprite sheet, or SVG icon set exists in the source. The brand's only graphic device is the
concentric-ring "radar/all-seeing eye" leitmotif (`components/book/RadarMotif.jsx`), used once per
composition. No emoji are used on covers or in brand-voice copy (see Content Fundamentals). If a project
built on this system needs a general icon set later, pick a thin-stroke geometric CDN set (e.g. Lucide)
to match the brand's precise, ungimmicky register — flag any such addition as a substitution when made.

## Index
- `styles.css` — root stylesheet, imports everything below
- `tokens/` — `colors.css`, `typography.css` (+ `@font-face`), `spacing.css`, `effects.css` (glass system)
- `components/core/` — `Button`, `Badge`, `GlassCard`, `Divider`, `DualLayerBlock`
- `components/book/` — `RadarMotif`, `ChapterKicker`, `QRPanel`
- `guidelines/` — foundation specimen cards (colors, type, spacing, radius, glass, wordmark, radar motif)
- `ui_kits/book-cover/` — interactive front/spine/back + e-book cover recreation (the book's actual
  deliverable), built from the exact strings in the cover brief
- `thumbnail.html` — project homepage tile
- `SKILL.md` — Claude Code-compatible skill wrapper for this design system
