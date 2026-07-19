---
title: "Incident Substrate Model"
description: "A grammar-driven substrate for calm, structured, deterministic incident ingestion, classification, and rectification."
stability: stable
date: 2026-07-14
section: core
rtt:
  coherence: declared
  drift: bounded
  paradox: structural
---

> ```
> rtt=1 | coherence=declared | drift=bounded | paradox=structural
> ```

## What Is the Incident Substrate Model?

The Incident Substrate Model (ISM) is a grammar-driven substrate for handling incidents
**calmly, structurally, and deterministically**. No drift. No improvisation. No panic.

ISM treats an incident not as an emergency but as a **substrate-level signal** — something
to ingest, classify, map, plan for, approve, and execute against in strict sequence.

---

## Seven Operators

| # | Operator | Function |
|---|----------|----------|
| 1 | `ingest` | Receive the raw incident signal |
| 2 | `classify` | Assign incident type and severity |
| 3 | `map_surface_area` | Identify the full affected substrate surface |
| 4 | `derive_rectification_steps` | Generate the ordered fix plan |
| 5 | `generate_readonly_plan` | Produce a read-only plan artifact for review |
| 6 | `request_operator_approval` | Gate on human approval before any action |
| 7 | `execute` | Apply the approved rectification steps |

---

## Three Fix Types

| Type | When Applied |
|------|-------------|
| **Remove** | Element is harmful and has no valid state |
| **Rotate** | Element is valid but in the wrong position or configuration |
| **Flag** | Element is ambiguous — mark for review without acting |

---

## Design Philosophy

ISM is built on three invariants:

- **Calm** — no urgency signals in the operator chain; urgency causes errors
- **Structured** — every action follows a declared grammar; no improvisation
- **Deterministic** — the same incident, ingested twice, produces the same plan

The `generate_readonly_plan` → `request_operator_approval` gate is non-negotiable.
No rectification step executes without explicit approval.

---

## Related Modules

- [Conditions Substrate Model](../Conditions_Substrate_Model/overview/) — maps the substrate conditions an incident disrupts
- [Governance Substrate Model](../Governance_Substrate_Model/overview/) — defines the approval authority structures ISM gates on
- [Structural Detection](../Structural_Detection/overview/) — detects the anomaly signals that become incident inputs
- [Opacity](../Opacity/overview/) — invisible substrate surfaces expand incident scope

---

v1.0 · Category: Safety / Operations · © 2026 Nawder Loswin · Byte Books Publishing
