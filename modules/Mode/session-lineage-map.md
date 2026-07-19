# 🗺️ Triadic Lineage Map — Session Layer

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

![Layer](https://img.shields.io/badge/Layer-Session-09f)
![Scope](https://img.shields.io/badge/Scope-Full_Lineage-ffe600)
![Status](https://img.shields.io/badge/Status-Active-0af)
![RTT](https://img.shields.io/badge/RTT%2F1-Aligned-8A2BE2)

---

## Session Context

```
Document:    Triadic Lineage Map — Session Layer
Version:     1.0
Status:      active
Layer:       Session
Coherence:   declared
Drift:       bounded
Canon:       active
Audience:    students + AIs
```

---

## 1. Purpose

This document maps the **complete lineage** of the RTT/1 Session Layer —
every module, every dependency, every propagation path. It is the structural
spine that prevents drift, preserves module identity, and ensures no
component operates orphaned from its ancestry.

**Design principle:** Every module must know where it came from, what it
feeds, and what constrains it. Lineage is not documentation — it is
load-bearing structure.

---

## 2. Layer Architecture

```
RTT/1 Stack (simplified)
═══════════════════════════════════════════════

  ┌─────────────────────────────────────────┐
  │            REGIME LAYER                 │
  │  coherence · drift · paradox · posture  │
  └──────────────────┬──────────────────────┘
                     │ inherits
                     ▼
  ┌─────────────────────────────────────────┐
  │            SESSION LAYER                │
  │                                         │
  │   ┌────────┐  ┌─────────┐  ┌────────┐   │
  │   │  Mode  │  │ Opacity │  │Capture │   │
  │   │  (M)   │  │  (O)    │  │  (C)   │   │
  │   └───┬────┘  └────┬────┘  └───┬────┘   │
  │       │            │           │        │
  │       │    ┌───────┴───────┐   │        │
  │       └───▶│   Context    │◀──┘        │
  │            │    (Cx)      │             │
  │            └──────────────┘             │
  └─────────────────────────────────────────┘
```

---

## 3. Module Lineage Cards

### 3.1 Mode (M)

```
Canonical ID:   MODE
Layer:          Session
Triadic Role:   Stabilize · Shift · Invert (maps all three)
Parent:         Regime Layer (coherence posture inheritance)
Siblings:       Opacity, Capture, Context
Children:       none (terminal operator)
Feeds:          Opacity (session.mode parameter)
                Capture (mode events)
                Context (stance → window behavior)
Constraints:    MCL (3 invariants, 5 guardrails)
Propagation:    push-based, event-driven
Default State:  M_chat
Files:          operators.md, constraints.md, propagation.md,
                tests.md, diagram.svg
```

**Identity statement:** Mode governs *how* the system engages — posture,
not payload. It is orthogonal to content and substrate.

### 3.2 Opacity (O)

```
Canonical ID:   OPACITY
Layer:          Session
Triadic Role:   Stabilize (transparency calibration)
Parent:         Regime Layer
Siblings:       Mode, Capture, Context
Children:       none (terminal operator)
Receives:       Mode (session.mode → transparency weight)
                Regime (opacity posture inheritance)
Feeds:          Context (visibility parameters)
                Capture (opacity state logged)
Constraints:    Opacity Constraint Layer (OCL)
Propagation:    recalculates on Mode transition events
Default State:  balanced transparency
```

**Identity statement:** Opacity governs *how much* is visible — the
transparency dial of the session. It weights visibility based on mode,
regime, and user preference.

### 3.3 Capture (C)

```
Canonical ID:   CAPTURE
Layer:          Session
Triadic Role:   Stabilize (immutable record)
Parent:         Regime Layer
Siblings:       Mode, Opacity, Context
Children:       none (terminal operator)
Receives:       Mode (mode_transition, mode_violation events)
                Opacity (opacity state changes)
                Context (context window snapshots)
Feeds:          external consumers (session logs, audit)
Constraints:    append-only within session; immutable after close
Propagation:    receives from all siblings; pushes to none
Default State:  empty log, recording active
```

**Identity statement:** Capture is the session's memory — the append-only,
immutable log of everything that happened. It does not interpret; it records.

### 3.4 Context (Cx)

```
Canonical ID:   CONTEXT
Layer:          Session
Triadic Role:   Shift (adaptive window)
Parent:         Regime Layer
Siblings:       Mode, Opacity, Capture
Children:       none (terminal operator)
Receives:       Mode (stance → window behavior)
                Opacity (visibility parameters)
                Regime (context scope inheritance)
Feeds:          runtime processing (active context window)
Constraints:    window must adjust before next input processed
Propagation:    receives from Mode and Opacity; feeds runtime
Default State:  wide context (Chat Mode aligned)
```

**Identity statement:** Context governs *what* is in scope — the active
window of attention. It adapts its shape based on the current mode and
opacity state.

---

## 4. Dependency Matrix

This matrix shows every directed dependency in the Session Layer.
Read as: **row depends on column**.

|            | Regime | Mode | Opacity | Capture | Context |
|:-----------|:------:|:----:|:-------:|:-------:|:-------:|
| **Mode**   |   ✓    |  —   |         |         |         |
| **Opacity**|   ✓    |  ✓   |    —    |         |         |
| **Capture**|        |  ✓   |    ✓    |    —    |    ✓    |
| **Context**|   ✓    |  ✓   |    ✓    |         |    —    |

**Key observations:**

- **Mode** depends only on the Regime Layer (upward inheritance).
- **Opacity** depends on both Regime and Mode.
- **Capture** receives from all siblings but depends on none for its own operation.
- **Context** is the most dependent — it synthesizes Mode, Opacity, and Regime.
- **No circular dependencies exist.** The graph is a directed acyclic graph (DAG).

---

## 5. Propagation Flow Map

```
Regime Layer
    │
    ├──▶ Mode ──push──▶ Opacity
    │      │                │
    │      ├──push──▶ Capture ◀── Opacity (state)
    │      │                │
    │      └──push──▶ Context ◀── Opacity (visibility)
    │                   │
    └───────────────────┘ (Regime → Context direct)
```

**Event flow sequence for a mode transition:**

```
1. User requests mode change          (origin: user)
2. MCL validates transition            (constraints check)
3. Mode Operator executes transition   (stance changes)
4. Mode pushes event → Capture         (logged before completion)
5. Mode pushes event → Opacity         (recalculates transparency)
6. Mode pushes event → Context         (adjusts window)
7. Opacity pushes state → Context      (visibility updated)
8. Context ready for next input        (window stabilized)
```

**Invariant:** Steps 4–6 happen in parallel. Step 7 follows Opacity
recalculation. Step 8 is the final gate before the next user input
is processed.

---

## 6. Triadic Role Summary

| Module   | Primary Role | Secondary Role | Triadic Function                    |
|:---------|:-------------|:---------------|:------------------------------------|
| Mode     | all three    | —              | Maps stances to Stabilize/Shift/Invert |
| Opacity  | Stabilize    | —              | Calibrates; holds steady visibility  |
| Capture  | Stabilize    | —              | Records; preserves immutable state   |
| Context  | Shift        | —              | Adapts; reshapes the active window   |

**Session Layer triadic profile:**

- **Stabilize-heavy:** 3 of 4 modules have Stabilize as primary.
  This is by design — the Session Layer's job is to hold steady.
- **Shift present:** Context provides adaptive capacity.
- **Invert absent at layer level:** Inversion lives *inside* Mode
  (Debug Mode) rather than as a separate Session module. This keeps
  the layer structurally minimal.

---

## 7. Regime Interaction Map

The Session Layer inherits its operating constraints from the Regime Layer.
This table shows how each regime posture affects each Session module.

| Regime Posture | Mode                          | Opacity                      | Capture                   | Context                    |
|:---------------|:------------------------------|:-----------------------------|:--------------------------|:---------------------------|
| declared       | All transitions explicit       | Full transparency range      | Normal logging            | Wide context available     |
| inferred       | Transitions may be proposed    | Weighted transparency        | Normal logging            | Adaptive context           |
| suspended      | Chat Mode only; others locked  | Minimal transparency         | Violation logging active  | Narrow context; read-only  |

---

## 8. Ancestry Chain

The full ancestry chain from root to terminal:

```
RTT (root theory)
 └── RTT/1 (runtime specification)
      └── Regime Layer (coherence governance)
           └── Session Layer
                ├── Mode (M)
                │    └── MCL (constraint sub-layer)
                ├── Opacity (O)
                │    └── OCL (constraint sub-layer)
                ├── Capture (C)
                └── Context (Cx)
```

**Every module in this chain can trace its lineage to RTT.**
No orphan modules exist. No module operates without a declared parent.

---

## 9. Canon Rules

1. **No module may be added to the Session Layer** without a lineage
   card, dependency entry, and propagation path.
2. **No module may be removed** without verifying that no sibling
   depends on it.
3. **All propagation paths must remain acyclic.** Introducing a cycle
   is a canon violation.
4. **The Regime Layer is the sole source of coherence posture.**
   No Session module may self-declare coherence.
5. **Mode is the sole source of interaction stance.**
   No sibling module may independently set mode state.

---

🔙 [Back to Mode Module](./README.md) · [Operators](./operators.md) · [Constraints](./constraints.md) · [Propagation](./propagation.md)

---

*Session Layer Triadic Lineage Map v1.0 · RTT/1 · TriadicFrameworks*
