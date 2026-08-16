## Lineage‑Integrity Matrix

The lineage‑integrity matrix is a promptable checklist for testing whether a concept, model, or operator
has a **traceable, honest, and non‑laundered ancestry** inside and across frameworks.

| Axis                      | Question / Prompt                                                                 | Expected Evidence                                      | Integrity Risk If Weak                          |
|---------------------------|------------------------------------------------------------------------------------|--------------------------------------------------------|-------------------------------------------------|
| Origin traceability       | Can we name the earliest *canonical* source(s) for this concept or operator?      | Citations, dates, authors, module paths                | Ancestry blur, “came from nowhere” narratives   |
| Cross‑canon mapping       | Is this concept mapped to at least one external canon or prior art?               | Cross‑canon matrix entries, external references        | Local reinvention, novelty inflation            |
| Inheritance rules         | Are the inheritance rules (what was kept, changed, dropped) explicitly stated?    | Change logs, deltas, rationale notes                   | Silent mutation, regime drift                    |
| Drift accounting          | Is drift (semantic, operational, ethical) tracked across versions and forks?      | Version history, drift tags, deprecation notes         | Unacknowledged drift, misaligned reuse          |
| Operator genealogy        | Are operators linked to parent operators or patterns in other modules?            | Genealogy diagrams, operator trees                     | Orphan operators, opaque behavior               |
| Regime context            | Is the regime (domain, constraints, stakes) of origin clearly documented?         | Domain tags, risk level, deployment context            | Context loss, mis‑deployment in new regimes     |
| Attribution & credit      | Are all major ancestors credited (people, labs, communities, frameworks)?         | Attribution section, contributor list                  | Credit laundering, exploitative reuse           |
| Licensing & obligations   | Are licensing terms and obligations attached to the lineage, not just the artifact? | License tags, obligations checklist                  | Rights laundering, compliance gaps              |
| Defensive publication     | Is there a defensive publication or prior‑art record for key claims?             | DOI, timestamped repo, public archive link             | Patent risk, enclosure of shared knowledge      |
| AI‑parsable structure     | Is the lineage represented in a machine‑readable format (JSON, YAML, graph)?      | JSON/YAML lineage file, graph schema                   | Non‑scannable ancestry, weak automated checks   |

### Usage

- **For each new artifact** (model, operator, pattern, module), walk the matrix row by row.  
- Mark each axis as: `strong`, `partial`, or `weak`.  
- Any axis marked `weak` should trigger:
  - a **lineage repair task** (add citations, cross‑canon mapping, genealogy), or  
  - a **deployment constraint** (do not deploy in high‑stakes regimes until repaired).
