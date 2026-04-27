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
Regime
```


