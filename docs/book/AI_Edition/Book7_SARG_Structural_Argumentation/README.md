# Book 7 — SARG Structural Argumentation
### AI Edition · Book 7 of 9

> **Draft** — content scaffold, 2026-10-10

---

## Purpose

**SARG (Structural Argumentation)** reframes argumentation as a structural phenomenon. Rather than evaluating arguments through propositional logic or rhetorical force, SARG treats arguments as structured objects — with nodes (claims, evidence, warrants), relations (support, contradiction, qualification), and constraints (validity conditions). An argument is sound if and only if it satisfies its declared structural constraints and preserves governing invariants.

This framework enables rigorous, domain-neutral argument evaluation tractable for both human analysts and AI reasoning systems.

---

## What This Book Covers

| Chapter Area | Description |
|---|---|
| Argument as Structure | Defining claims, evidence, and warrants as structural nodes |
| Relation Types | Support, contradiction, qualification, and auxiliary relations |
| Validity Conditions | Structural constraints that determine argument soundness |
| Defeat Conditions | How to structurally defeat an argument vs. merely contest it |
| Argument Construction | Step-by-step procedure for building SARG-compliant arguments |
| Evaluation Procedures | Systematic walkthrough for assessing argument structural integrity |
| TEL Integration | Encoding SARG arguments in TEL (Book 5) |
| Governance Arguments | Applying SARG to regime legitimacy claims (Book 6) |

---

## Core Invariants

- **INV-SARG-001** — Argument Integrity: every argument node must be reachable from the argument's root claim via declared relations
- **INV-SARG-002** — Warrant Necessity: every claim-evidence pair requires at least one explicit warrant relation
- **INV-SARG-003** — Defeat Completeness: a defeat of an argument must target at least one structural component, not merely a surface-level assertion
- **INV-SARG-004** — Reflexive Prohibition: an argument cannot provide structural support for its own root claim without passing through an independent evidentiary node

---

## Reading Order

```
Book 1 (FFT)
Book 3 (Structural Detection)
Book 5 (TEL Expression & Representation)
Book 6 (Governance & Regime Logic)
    └──► Book 7 (SARG Structural Argumentation)  ← YOU ARE HERE
              ├── Book 8 (Nature of Structure)
              └── Book 9 (Pattern Dynamics)
```

**Prerequisites:** Books 1, 3, 5, 6  
**Unlocks:** Books 8, 9

---

## AI Module Metadata

| Field | Value |
|---|---|
| Module ID | `book7_sarg` |
| Folder | `Book7_SARG_Structural_Argumentation/` |
| Edition | AI Edition v1.0.0 |
| Domain | Argumentation & Logic |
| Tier | Applied |
| Status | Active |
| Invariants file | `invariants/book7_invariants.json` |

---

## Live Site

[https://umaywant2.github.io/TriadicFrameworks/docs/book/AI_Edition/Book7_SARG_Structural_Argumentation](https://umaywant2.github.io/TriadicFrameworks/docs/book/AI_Edition/Book7_SARG_Structural_Argumentation)

---

*Draft · Last updated: 2026-10-10 · AI Edition*

