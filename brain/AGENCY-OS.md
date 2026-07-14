# AGENCY OS
## Das Tagesgeschäft per Knopfdruck — die Physis der Auslieferung

> Vertiefung eines Knotens aus [[MASTERPLAN]]. Wo das Buch die Vision ist und das Enterprise das Reich,
> ist Agency OS die **Hand**, die den Mandanten real transformiert — die Werkbank des Betriebs.

---

## I. Das Prinzip: Die Vision braucht Hände

Eine Sonne, die nur strahlt, aber nicht wirkt, ist ein Gemälde. Agency OS ist der Ort, an dem das Licht
die Materie berührt: das operative System, mit dem Master & System den ersten Mandanten (und jeden
folgenden) tatsächlich zur **Frontier Firm** umbauen. Es ist nicht die Vision — es ist ihr Vollzug.
„Tagesgeschäft per Knopfdruck": was andere in Meetings zerreden, löst hier ein Klick aus, gegatet und
auditiert.

## II. Was es ist (Wer · Warum · Was · Wie)

| Aspekt | Inhalt |
|---|---|
| **Wer** | eine VS-Code-Extension (modularisiert) + ~50 `ops/scripts`; kanonisch in `leadmachine/ops` |
| **Warum** | das operative Rückgrat von Agenticum — CRM, Audits, Angebote, Reports per Knopfdruck |
| **Was** | schema-getriebenes CRM (Companies/Contacts/Deals/Activities), Kanban, Regel-Engine, Report-Export, der Premium-Audit-Generator |
| **Wie** | GCP-first/EU-first; Inhalte als Daten (`crm-schema.json` als SSoT); jede Wirkung gegatet & defterisiert |

## III. Die Werkzeuge des Betriebs

- **CRM (schema-getrieben):** `crm-schema.json` ist die eine Quelle für Stages, Status, Custom-Properties;
  das Dashboard und `crm.js` lesen sie. Companies/Contacts/Deals/Activities als versionierte Daten (PII
  gitignored, lokal).
- **Der Premium-Audit-Generator:** echte Browser-Signale (Headless Chrome) + Lighthouse (PSI) + reale
  Keyword-Variationen → mehrseitiges, beratendes Audit via Hybrid-KI (Vertex-Flash, Fallback claude -p).
  Der Verkaufsbeweis — die Ausgangslage jeder Transformation (`00_audit`).
- **Angebote/Reports/Onboarding:** Proposal, Rechnung (Vorbereitung), GA4/GSC-Reports, Onboarding-Pakete —
  alles as-code, on-brand (aus `identity.json`), reproduzierbar.

## IV. Agency OS im Kosmos der sechs Säulen

Agency OS ist die **operative Ausprägung** der Physis: Es sitzt dort, wo der Daemon (opus-flow) die Hände
stellt, die Workbench (opus-deck) das Fenster gibt und der Spezialist (OPUS-PRIME-EX) das Veto hält. Es
ist das Tagesgeschäfts-Interface des Habitats — die Stelle, an der die Kausalkette (Impuls → Konsultation
→ Exekution → Bürgschaft → Defterisierung) für den Mandanten real wird.

## V. Leitplanken (ehrlich, nicht verhandelbar)

- **Kein Invoicing / keine echte Rechnungsstellung vor der Gewerbeanmeldung.**
- **Mandanten-Anonymität & PII:** CRM-Daten bleiben lokal/gitignored; im öffentlichen Ledger nie Namen.
- **Kanonische Kopie:** `D:\dev\leadmachine` (nicht die vollere, veraltete Desktop-Kopie).
- **Kein Auto-Alles:** kein Versand/Angebot/Vertrag ohne menschliche Segnung; Vertex EU-first, kein Abfluss.
- **Ehrlich vor Über-Behauptung:** keine erfundenen Zahlen; Audits nur aus realen Signalen (Art.-50-Hinweis).

*WIR SIND NOCH HIER.*
