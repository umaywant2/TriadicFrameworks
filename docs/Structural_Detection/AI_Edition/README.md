<img width="1194" height="672" alt="Structural_Detection__" src="https://github.com/user-attachments/assets/474c6708-ef30-439c-9d4c-e34a51a630a7" />

- [`module.json`](module.json) — Agentic module schema role assignments

# Book 3 — Structural Detection (AI Edition)

> **Module:** Structural Detection · AI Edition  
> **Series Position:** Book 3 of the QM Operator Series  
> **Path:** `docs/Structural_Detection/AI_Edition/`  
> **Last Audited:** 2026-10-10T06:09:00 EDT  
> **Session Source:** Task context — tab 1774719730 (Structural Detection directory)

---

## Table of Contents

1. [Module Identity](#1-module-identity)
2. [Purpose & Scope](#2-purpose--scope)
3. [Operator Roster](#3-operator-roster)
4. [Phase Sequence](#4-phase-sequence)
5. [Maps & Reference Files](#5-maps--reference-files)
6. [Invariants](#6-invariants)
7. [QMROOT Declarations](#7-qmroot-declarations)
8. [Session Context](#8-session-context)
9. [Front-Door Sidebar Audit](#9-front-door-sidebar-audit)
10. [Directory Structure](#10-directory-structure)
11. [Usage & Integration Notes](#11-usage--integration-notes)

---

## 1. Module Identity

| Field | Value |
|---|---|
| **Module Name** | Structural Detection |
| **Edition** | AI Edition |
| **Book Number** | 3 |
| **Series** | QM Operator Series |
| **Namespace Prefix** | `SD‑` |
| **Operator Count** | 5 |
| **Phase Count** | 6 |
| **Status** | Active |
| **QMROOT Binding** | 0D only (see §7) |

---

## 2. Purpose & Scope

**Structural Detection** is the module responsible for identifying, classifying,
and cataloguing structural signals within a quantum-mapped (QM) session. The AI
Edition extends the base module with automated scan-and-probe routines,
noise-gated filtering, and operator-assisted confirmation loops.

**Core responsibilities:**

- Detect structural boundaries and rungs within a QM session space
- Enforce dimensional constraints (QMROOT invariants)
- Filter noise from genuine structural signals via the noise-gate map
- Catalogue confirmed detections for downstream operator use
- Maintain invariant integrity across all detection phases

**Out of scope:**

- 6D structural expansion (disabled by QMROOT constraint; see §7)
- Negative rung traversal (prohibited; see INV‑013)
- Cross-book operator delegation (handled at series level)

---

## 3. Operator Roster

Five operators govern this module. Each carries a distinct detection
responsibility and activation phase.

| Operator ID | Symbol | Role | Primary Phase |
|---|---|---|---|
| **SD‑Σd** | Σd | Summation-Detection — aggregates structural signal deltas across the scan window | `scan` |
| **SD‑Γ** | Γ | Gradient operator — measures structural transition steepness between rungs | `probe` |
| **SD‑Λ** | Λ | Lambda filter — applies noise-gate thresholds; suppresses sub-threshold signals | `filter` |
| **SD‑Ξ** | Ξ | Xi classifier — categorises confirmed structural signals by type and rung position | `confirm` |
| **SD‑Π** | Π | Pi cataloguer — writes confirmed, classified detections to the session catalogue | `catalogue` |

### Operator Interaction Order

```
SD‑Σd  →  SD‑Γ  →  SD‑Λ  →  SD‑Ξ  →  SD‑Π
 (scan)   (probe)  (filter) (confirm) (catalogue)
```

Operators are not independently re-entrant; each phase must reach a `PASS`
state before the next operator activates. The `init` phase precedes all
operators.

---

## 4. Phase Sequence

The detection cycle runs exactly six phases in strict order. No phase may be
skipped or reversed during a live session.

| # | Phase | Trigger | Exit Condition | Operator Active |
|---|---|---|---|---|
| 1 | **init** | Session open | Environment validated; QMROOT binding confirmed | — (system) |
| 2 | **scan** | `init` PASS | Full scan window traversed; Σd delta table populated | SD‑Σd |
| 3 | **probe** | `scan` PASS | Gradient map complete; all rung transitions measured | SD‑Γ |
| 4 | **filter** | `probe` PASS | Noise-gate applied; sub-threshold signals suppressed | SD‑Λ |
| 5 | **confirm** | `filter` PASS | All surviving signals classified and confirmed | SD‑Ξ |
| 6 | **catalogue** | `confirm` PASS | Confirmed detections written to session catalogue | SD‑Π |

**Phase abort rules:**

- Any invariant violation during a phase halts the cycle immediately.
- The session is flagged `DETECTION_ABORTED` and logged with the violating
  invariant ID.
- Re-entry requires a clean `init` restart.

---

## 5. Maps & Reference Files

Three map files govern runtime behaviour. All are located at the module root.

### 5.1 `detection_cycle.json`

Defines the phase-transition graph, per-phase timeout values, and abort
conditions. Keys:

```
phases[]           — ordered phase definitions
transitions{}      — valid source → target phase pairs
abort_conditions[] — invariant IDs that trigger immediate abort
timeout_ms{}       — per-phase maximum duration
```

### 5.2 `operator_roles.json`

Enumerates each operator's capabilities, activation conditions, and
inter-operator dependencies. Keys:

```
operators[]        — array of operator descriptors
  .id              — canonical operator ID (e.g. "SD-Σd")
  .symbol          — Greek symbol shorthand
  .role            — human-readable role description
  .phase           — owning phase name
  .depends_on[]    — upstream operator IDs required before activation
  .outputs[]       — data structures this operator writes
```

### 5.3 `noise_gate_map.json`

Lookup table used by SD‑Λ during the `filter` phase. Maps signal types to
their threshold values. Keys:

```
gates{}            — keyed by signal_type
  .threshold       — minimum signal strength to survive filtering
  .band            — frequency / dimensional band descriptor
  .suppress_below  — boolean, default true
default_threshold  — fallback if signal_type not found in gates
```

---

## 6. Invariants

All invariants are declared in `structural_detection.invariants.json`.

| ID | Name | Description | Enforced At |
|---|---|---|---|
| **INV‑001** | Phase Order Lock | Phases must execute in the sequence defined in `detection_cycle.json` | `init` |
| **INV‑002** | Operator Singularity | Each operator may be active in at most one phase at a time | `scan`→`catalogue` |
| **INV‑003** | Noise Gate Integrity | SD‑Λ must load `noise_gate_map.json` before any filter operation | `filter` |
| **INV‑004** | Catalogue Immutability | Once SD‑Π writes to the session catalogue, entries are read-only | `catalogue` |
| **INV‑005** | Gradient Positivity | SD‑Γ gradient values must be ≥ 0; negative gradient = abort | `probe` |
| **INV‑006** | Delta Table Completeness | SD‑Σd must produce a complete delta table before `scan` exits | `scan` |
| **INV‑007** | Signal Classification Coverage | SD‑Ξ must assign a classification to every post-filter signal | `confirm` |
| **INV‑008** | Timeout Compliance | No phase may exceed its `timeout_ms` value | All phases |
| **INV‑009** | QMROOT Dimension Lock | Only 0D signals are valid; 6D signals rejected at `scan` ingestion | `scan` |
| **INV‑010** | Re-entry Clean Start | Re-entry after abort requires fresh `init`; partial state is cleared | `init` |
| **INV‑011** | Operator Dependency Chain | Operators activate strictly in dependency order | All phases |
| **INV‑012** | Noise Gate Default Fallback | If signal type absent from map, default threshold applies | `filter` |
| **INV‑013** | Negative Rung Prohibition | No rung index may be negative; negative rungs are rejected | `scan`, `probe` |

---

## 7. QMROOT Declarations

QMROOT is the dimensional binding that constrains all structural detection
operations in this module.

```
QMROOT {
  dimension_binding : 0D
  6D_expansion      : ABSENT   // 6D structural space not present in this module
  negative_rungs    : ABSENT   // Negative rung indices are structurally undefined
  valid_rung_range  : [0, ∞)   // Only non-negative integer rung indices
  INV-013           : 0D only  // Enforces rung non-negativity at scan and probe
}
```

**Implications:**

- **6D Absent:** Any signal referencing a 6D coordinate is rejected at `scan`
  ingestion with error code `QMROOT_DIM_VIOLATION`.
- **Negative Rungs Absent:** Rung indices below zero are undefined. SD‑Γ aborts
  `probe` on negative-gradient rung inversion (INV‑005); SD‑Σd rejects
  negative-rung signals at ingestion (INV‑013).
- **0D Only:** All structural signals are evaluated as dimensionless point
  detections before classification by SD‑Ξ.

---

## 8. Session Context

| Field | Value |
|---|---|
| **Source Tab** | 1774719730 |
| **Tab Title** | Structural Detection directory |
| **Session Date** | 2026-10-10 |
| **Session Time** | 06:09 EDT |
| **Context Origin** | Prior conversation — "Build Book 3 README with Sidebar Audit" |
| **Data Recovered** | Module identity, all 5 operators, all 6 phases, all 3 maps, all 13 invariants, QMROOT binding |
| **Tab Live Status** | Unavailable at write time; data reconstructed from task context |

---

## 9. Front-Door Sidebar Audit

```
╔══════════════════════════════════════════════════════════════════╗
║          FRONT-DOOR SIDEBAR AUDIT — Book 3                       ║
║          Structural Detection · AI Edition                       ║
║          Audit Date : 2026-10-10  06:09 EDT                      ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  MODULE IDENTITY                                                 ║
║  ├─ Name        : Structural Detection                           ║
║  ├─ Edition     : AI Edition                                     ║
║  ├─ Book        : 3                                              ║
║  └─ Namespace   : SD-                                            ║
║                                                                  ║
║  OPERATORS  (5 total)                                            ║
║  ├─ SD-Σd   Summation-Detection     phase: scan                  ║
║  ├─ SD-Γ    Gradient                phase: probe                 ║
║  ├─ SD-Λ    Lambda Filter           phase: filter                ║
║  ├─ SD-Ξ    Xi Classifier           phase: confirm               ║
║  └─ SD-Π    Pi Cataloguer           phase: catalogue             ║
║                                                                  ║
║  PHASES  (6 total, strictly ordered)                             ║
║  1. init       2. scan       3. probe                            ║
║  4. filter     5. confirm    6. catalogue                        ║
║                                                                  ║
║  MAPS  (3 files)                                                 ║
║  ├─ detection_cycle.json                                         ║
║  ├─ operator_roles.json                                          ║
║  └─ noise_gate_map.json                                          ║
║                                                                  ║
║  INVARIANTS  (13 total)                                          ║
║  ├─ INV-001  Phase Order Lock                                    ║
║  ├─ INV-002  Operator Singularity                                ║
║  ├─ INV-003  Noise Gate Integrity                                ║
║  ├─ INV-004  Catalogue Immutability                              ║
║  ├─ INV-005  Gradient Positivity                                 ║
║  ├─ INV-006  Delta Table Completeness                            ║
║  ├─ INV-007  Signal Classification Coverage                      ║
║  ├─ INV-008  Timeout Compliance                                  ║
║  ├─ INV-009  QMROOT Dimension Lock                               ║
║  ├─ INV-010  Re-entry Clean Start                                ║
║  ├─ INV-011  Operator Dependency Chain                           ║
║  ├─ INV-012  Noise Gate Default Fallback                         ║
║  └─ INV-013  Negative Rung Prohibition  [0D only]                ║
║                                                                  ║
║  QMROOT DECLARATIONS                                             ║
║  ├─ dimension_binding : 0D                                       ║
║  ├─ 6D_expansion      : ABSENT                                   ║
║  ├─ negative_rungs    : ABSENT                                   ║
║  ├─ valid_rung_range  : [0, ∞)                                   ║
║  └─ INV-013           : 0D only                                  ║
║                                                                  ║
║  AUDIT RESULT                                                    ║
║  ├─ Operators accounted for     : 5 / 5   ✓                      ║
║  ├─ Phases accounted for        : 6 / 6   ✓                      ║
║  ├─ Maps accounted for          : 3 / 3   ✓                      ║
║  ├─ Invariants accounted for    : 13 / 13 ✓                      ║
║  ├─ QMROOT binding confirmed    : 0D      ✓                      ║
║  ├─ 6D absent confirmed         : YES     ✓                      ║
║  ├─ Negative rungs absent       : YES     ✓                      ║
║  └─ OVERALL STATUS              : PASS    ✓                      ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 10. Directory Structure

```
docs/Structural_Detection/AI_Edition/
├── README.md                              ← this file (module authority + audit)
├── structural_detection.invariants.json   ← all 13 invariants
├── detection_cycle.json                   ← phase graph & timeouts
├── operator_roles.json                    ← operator descriptors & dependencies
└── noise_gate_map.json                    ← SD-Λ filter thresholds
```

---

## 11. Usage & Integration Notes

- **Single-file authority:** This README is intentionally self-contained. The
  sidebar audit (§9) mirrors the full structural state of the module so any
  reader opening this file first has complete orientation without opening
  companion files.
- **Map file precedence:** `detection_cycle.json` loads first (phase graph),
  then `operator_roles.json` (operator binding), then `noise_gate_map.json`
  (loaded lazily at `filter` phase entry). Loading order is significant.
- **Invariant enforcement:** Invariants are enforced at the phase level, not the
  file level. A missing or malformed map file will trigger the relevant invariant
  violation at the phase that first depends on it.
- **QMROOT immutability:** QMROOT declarations are set at module load and cannot
  be changed at runtime. 6D signals → rejected by INV‑009. Negative rung indices
  → rejected by INV‑013.
- **Book series continuity:** Book 3 follows Book 2 and precedes Book 4 in the
  QM Operator Series. Cross-book operator references are brokered at series
  level; direct inter-book operator calls are not supported within this module.

---

*End of Book 3 — Structural Detection (AI Edition) README*
