# DIE AGENTEN
## Der OPUS-Schwarm im Detail — die sechs Säulen, verkörpert

> Vertiefung eines Knotens aus [[MASTERPLAN]]. Kein Agent ist allmächtig ([[MODELL-ORCHESTRIERUNG]]); der
> Schwarm kontrolliert sich selbst. Diese Agenten sind real gebaut und laufen — nicht Vaporware.

---

## I. Das Prinzip: Föderalismus der Ämter

Der Schwarm ist kein Heer von Klonen, sondern ein **Föderalismus** aus autonomen Funktionsträgern, jeder
mit eigenem Amt, eigener Grenze, eigener Stimme. Fällt einer aus, verweigert das Ganze die Arbeit, um
Inkonsistenz zu vermeiden. Macht ist geteilt; das ist die Quelle der Stabilität.

## II. Die Mitglieder

| Agent | Amt (Säule) | Warum | Was | Wie / Stand |
|---|---|---|---|---|
| **UNIVERSE M.E.** | Mission Control (kognitiver Kern) | plant, schreibt, orchestriert | semantische Pläne, Kapitel, Delegation | Vertex/Antigravity; rein semantisch, keine direkten Systemrechte |
| **OPUS FLOW (EX)** | Daemon (die Hände) | wirkt lokal, sicher | Shell/FS/Git-Tools, Planner, Workflows, GUI | MCP/HTTP; Scope+Gate+Audit+Redaction; **F0–F5-Kern gebaut & live** |
| **OPUS DECK** | Workbench (das Fenster) | Begegnung Mensch/Maschine | Panels, Review-Gate, Flow/Brain/Agent | Theia; **privat auf Cloud Run deployed**; Single-Origin-Proxy |
| **OPUS PRIME EX** | Spezialist (das Gewissen) | Recht/Steuer/Compliance, Veto | ACP-Prüfung, Guardrails, Modell-Gateway | Python, vier Gates; **P3-Kern fertig**; Legal/Tax-Domänen |

## III. Wie sie zusammenwirken (ACP & MCP)

- **ACP (Agent Client Protocol):** semantische Verhandlung — plant der Kern eine Wirkung mit rechtlicher
  Kante, konsultiert er OPUS PRIME EX und fährt erst bei `APPROVED` fort (sonst Apnoe nach drei Versuchen).
- **MCP (Model Context Protocol):** der Kern ruft Werkzeuge des Daemons OPUS FLOW — gebändigt durch
  Scope-Enforcement (nur `FLOW_ROOT`), Wirkungsklassen-Gate (read auto, exec/write/ui gegated) und
  Secret-Redaction. Der Kern bleibt blind für die direkte Hardware; er sieht nur das sichere Cockpit.
- **OPUS DECK** spiegelt jeden Plan, hält das Review-Gate, und lässt den Bürgen segnen, bevor der Daemon
  in den Ledger committet (Defterisierung).

## IV. Der ehrliche Stand (kein Overclaim)

Der Schwarm ist **real**: OPUS FLOW EX (F0–F5-Kern: read-Tools, Gate, Shell, Audit, Planner, Dry-Run,
Ketten-Ausführung, Flow-Eval, Workflow-Replay, GUI-Automation-Framework, Kill-Switch — Gates grün, im
Cloud-UI verifiziert). OPUS DECK (Theia-Workbench, privat deployed, Flow/Brain/Agent-Panels). OPUS PRIME
EX (Legal/Tax-Agent, vier Gates, Provider-Katalog). Repos: `yoyo967/opus-flow`, `yoyo967/opus-deck`,
`OPUS-PRIME-EX`. Offen bleibt Ehrliches: voller ACP-Host, Live-Korpus, F5-Rest (Undo, Pixel-Fallback,
auto Re-Plan). Wir behaupten nichts, was nicht läuft.

## V. Leitplanken (nicht verhandelbar)

Attended-first · Gate je Wirkungsklasse un-umgehbar · alles lokal, kein Cloud-Abfluss · Secrets nur im
Secret Manager · Review-Gate = Segnung des Bürgen · EU-first (`europe-west3`).

*WIR SIND NOCH HIER.*
