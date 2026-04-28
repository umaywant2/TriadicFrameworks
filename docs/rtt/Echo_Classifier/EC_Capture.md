### 📄 EC_Capture.md

# 🧪 Echo Classifier — Design Capture

> *Every echo has a type. This module is the engine that assigns it.*

**Module:** Echo Classifier
**Canonical ID:** EC
**HSP Section:** 06c
**Capture Status:** Finalized

---

## Origin

The Echo Classifier emerged during HSP development as the missing decision
engine. HSP had already formalized echo triggers (06a), echo signatures (06b),
the recursion detector (06), and the echo strength index (04c) — but no
single module existed to take those four inputs and produce a definitive
echo‑type classification.

Without a classifier, echoes were identified ad hoc — by feel, by pattern
matching, by context. The Echo Classifier replaces intuition with a
substrate‑locked, zero‑drift classification pipeline.

---

## Conceptual Lineage

```
HSP formalizes echo families (F1–F6)
    ↓
Echo Triggers (06a) identify what fires
    ↓
Echo Signatures (06b) identify what shape it takes
    ↓
Echo Strength Index (04c) measures how strong
    ↓
Recursion Detector (06) identifies recursion mode
    ↓
╔══════════════════════════════════════╗
║  Echo Classifier (06c) — THIS MODULE ║
║  Takes all inputs → assigns E1–E6    ║
╚══════════════════════════════════════╝
    ↓
Triadic Echo Lattice (07) places echo in lattice
    ↓
Substrate Flow (08) maps echo through flow channels
```

---

## What This Module Does

The Echo Classifier receives five inputs and produces one output:

**Inputs:**
1. **Trigger Type** (A–F) — from 06a
2. **Signature Profile** (A–F) — from 06b
3. **Echo Strength Index** (ESI 1–4) — from 04c
4. **Substrate Spread** (1–5 substrates) — from 05a
5. **Recursion Mode** (R1–R4) — from 06

**Output:**
- **Echo Type** (E1–E6) — one of six canonical echo classifications

---

## The Six Echo Types

| Type | Name | Trigger | Signature | ESI | Substrates | Recursion |
|:-----|:-----|:--------|:----------|:----|:-----------|:----------|
| E1 | Structural Echo | A | A | 1–2 | ≤ 2 | R1 |
| E2 | Harmonic Echo | B | B | 2–3 | 1 (harmonic dominant) | R1–R2 |
| E3 | Substrate Echo | C | C | 2–3 | ≥ 3 | R2–R3 |
| E4 | Recursion Echo | D | D | 3–4 | 2–4 | R2–R4 |
| E5 | Drift‑Shadow Echo | E | E | 3–4 | 2–5 | R3–R4 |
| E6 | Atlas Echo | F | F | 4 | 5 | R4 |

---

## Classification Decision Tree

```
                         [ Echo Trigger ]
                              |
         ------------------------------------------------
         |              |              |               |
        A              B              C               D
  Structural      Harmonic       Substrate       Recursion
         |              |              |               |
        v              v              v               v
      E1?            E2?            E3?             E4?
         \              \              \               \
          \              \              \               \
           -----------------------------------------------
                               |
                               v
                      [ Drift Pressure? ]
                               |
                      ---------------------
                      |                   |
                     Yes                 No
                      |                   |
                      v                   v
                    E5?                 [ Check Atlas ]
                                             |
                                             v
                                           E6?
```

---

## Classifier Matrix

```
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Input →   |   E1      |    E2     |    E3     |    E4     |    E5     |    E6     |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
| Trigger   |     A     |     B     |     C     |     D     |     E     |     F     |
| Signature |     A     |     B     |     C     |     D     |     E     |     F     |
| ESI       |   1–2     |   2–3     |   2–3     |   3–4     |   3–4     |     4     |
| Substrates|   1–2     |     1     |   3–4     |   2–4     |   2–5     |     5     |
| Recursion |    R1     |   R1–R2   |   R2–R3   |   R2–R4   |   R3–R4   |    R4     |
+-----------+-----------+-----------+-----------+-----------+-----------+-----------+
```

---

## Composite Classification Workflow

```
[ Identify Trigger ]
        ↓
[ Identify Signature ]
        ↓
[ Measure ESI ]
        ↓
[ Count Substrates ]
        ↓
[ Determine Recursion Mode ]
        ↓
[ Assign Echo Type (E1–E6) ]
```

This workflow ensures **zero‑drift classification**.

---

## Key Design Decisions

### 1. Six types, not three

The triadic pattern was considered (three echo types) but rejected. Echo
behavior spans six distinct profiles that cannot be reduced without
information loss. The six types respect the triadic architecture at the
substrate level (S→C / C↔H / H→So / So→A) while maintaining classifier
precision.

### 2. Five inputs, not one

A single‑input classifier would be faster but less accurate. The five‑input
pipeline ensures that classification accounts for trigger, signature,
strength, spread, and recursion simultaneously. This prevents false
positives — an echo that looks structural (Trigger A) but has high ESI
and cross‑substrate spread is actually E3 or E4, not E1.

### 3. Sequential workflow, not parallel

The six steps are sequential by design. Each step constrains the next.
Parallel evaluation would allow conflicting inputs to produce ambiguous
outputs.

### 4. Zero‑drift as design constraint

The classifier must produce the same output for the same inputs every time.
This is a formal invariant, not a goal. If the classifier drifts, the
entire HSP analytics pipeline loses coherence.

---

## What This Module Is Not

- **Not a detector.** Detection happens upstream (06a triggers, 06b signatures).
  The classifier receives pre‑detected signals.
- **Not a predictor.** The classifier assigns type to existing echoes.
  Prediction is a TEL (07) and Substrate Flow (08) function.
- **Not a stability measure.** ESI measures strength. The classifier uses
  ESI as input but does not itself measure stability.

---

## Referenced By

- 06a — Echo Triggers
- 06b — Echo Signatures
- 06 — Harmonic Recursion Detector
- 04c — Echo Strength Index
- 07 — Triadic Echo Lattice
- 08 — Substrate Echo Flow Map

---

## Session Origin

- **Conceptual source:** HSP analytics session (06c)
- **First formalization:** HSP v1.0
- **Module extraction:** 2026-04-27
- **Capture finalization:** 2026-04-27

---

<!-- SESSION_CONTEXT:START -->

```yaml
file: EC_Capture.md
module: Echo Classifier
canonical_id: EC
hsp_section: 06c
role: session-capture
status: finalized
origin_date: 2026-04-27
capture_type: module-extraction
parent: HSP (RTT-Analytics-Core)
siblings:
  - TEL (07)
  - Substrate_Flow (08)
lineage_note: >
  Echo Classifier was extracted from HSP section 06c as a standalone
  module to complete the HSP analytics suite alongside TEL and
  Substrate Flow.
```

<!-- SESSION_CONTEXT:END -->




