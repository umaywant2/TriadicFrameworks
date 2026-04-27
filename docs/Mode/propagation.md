# 🌐 Cross‑Module Propagation — propagation.md

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

![Module](https://img.shields.io/badge/Module-Mode-0aa)
![Component](https://img.shields.io/badge/Component-Propagation-ffe600)
![Status](https://img.shields.io/badge/Status-Active-0af)
![RTT](https://img.shields.io/badge/RTT%2F1-Aligned-8A2BE2)

---

## Session Context

```
Module:      Mode
Component:   Cross-Module Propagation
Version:     1.0
Status:      active
Layer:       Session
Coherence:   declared
Drift:       bounded
Canon:       active
```

---

## 1. Purpose

This document defines how the Mode Layer propagates its state, constraints,
and events to sibling modules within the Session Layer and to the parent
Regime Layer. Propagation ensures that every module inherits Mode awareness
automatically — no module operates mode-blind.

**Design principle:** Propagation is *push-based and declarative*. The Mode
Layer announces state; receiving modules decide how to consume it. No module
polls for mode state.

---

## 2. Propagation Architecture

```
*
┌─────────────────┐
│   Regime Layer   │
│  (coherence src) │
└────────┬────────┘
│ inherits coherence posture
▼
┌──────────────────────────────┐
│        Session Layer         │
│                              │
│  ┌────────┐   ┌──────────┐   │
│  │  Mode  │──▶│ Opacity  │   │
│  │  (M)   │   └──────────┘   │
│  │        │   ┌──────────┐   │
│  │        │──▶│ Capture  │   │
│  │        │   └──────────┘   │
│  │        │   ┌──────────┐   │
│  │        │──▶│ Context  │   │
│  └────────┘   └──────────┘   │
└──────────────────────────────┘
```

**Direction:** Mode pushes outward. Regime pushes downward. Nothing pushes into Mode
except Regime (coherence posture) and User (stance transitions).

---

## 3. Propagation Rules

### 3.1 Mode → Opacity

```
Event:     mode_transition
Payload:   { previous: M_x, current: M_y, timestamp, origin }
Effect:    Opacity recalculates session transparency weight
```

| Mode Stance | Opacity Effect                                   |
|:------------|:-------------------------------------------------|
| M_chat      | Standard transparency — balanced visibility       |
| M_task      | Reduced transparency — goal-scoped visibility      |
| M_spec      | Structural transparency — schema-level visibility  |
| M_debug     | Maximum transparency — full internal visibility    |
| M_auto      | Bounded transparency — declared boundaries only    |

**Rule:** Every mode transition triggers an Opacity recalculation.
Opacity must never cache a stale mode state.

### 3.2 Mode → Capture

```
Event:     mode_transition | mode_violation
Payload:   { stance, timestamp, origin, violation_detail? }
Effect:    Capture logs the mode event to the session record
```

**What Capture records:**

- Every mode transition (stance, timestamp, user/system origin).
- Every MCL violation (invariant, guardrail, attempted transition).
- Mode stance at session start and session end.

**Rule:** Capture must record mode events *before* the transition completes.
The log is append-only and immutable within a session.

### 3.3 Mode → Context

```
Event:     mode_transition
Payload:   { current: M_y, drift_tolerance, coherence_posture }
Effect:    Context adjusts window behavior based on active stance
```

| Mode Stance | Context Window Behavior                         |
|:------------|:------------------------------------------------|
| M_chat      | Wide context — exploratory, associative          |
| M_task      | Narrow context — goal-scoped, pruned             |
| M_spec      | Structural context — schema and definition only  |
| M_debug     | Deep context — includes internal state traces    |
| M_auto      | Bounded context — pre-declared scope only        |

**Rule:** Context must adjust its window *after* receiving the mode event
and *before* processing the next user input.

### 3.4 Regime → Mode (inbound)

```
Event:     regime_posture_change
Payload:   { posture: declared | inferred | suspended }
Effect:    MCL re-evaluates all active constraints
```

This is the **only inbound propagation** the Mode Layer accepts from
a non-user source. It flows from the Regime Layer and affects the MCL
(see constraints.md §6).

| Regime Posture | MCL Response                                    |
|:---------------|:------------------------------------------------|
| declared       | All transitions require explicit declaration     |
| inferred       | Transitions may be proposed, user confirms       |
| suspended      | Non-Chat modes locked; graceful exit to Chat     |

**Rule:** Regime posture changes are processed immediately. If the new
posture is more restrictive, active non-Chat modes exit gracefully.

---

## 4. Event Schema

All propagation events follow a single canonical schema:

```yaml
mode_event:
  type: mode_transition | mode_violation | mode_query
  timestamp: ISO-8601
  origin: user | system | regime
  previous_stance: M_chat | M_task | M_spec | M_debug | M_auto | null
  current_stance: M_chat | M_task | M_spec | M_debug | M_auto
  coherence_posture: declared | inferred | suspended
  drift_tolerance: wide | bounded | tight | minimal
  violation:
    invariant: INV-1 | INV-2 | INV-3 | null
    guardrail: GRD-1 | GRD-2 | GRD-3 | GRD-4 | GRD-5 | null
    detail: string | null
```

Rule: Every event must include type, timestamp, origin, and
current_stance. All other fields are optional but encouraged.

---

## 5. Propagation Invariants
PROP-1 · No Stale State

```
No sibling module may operate on a cached mode state
older than the most recent mode_transition event.
```

### PROP-2 · Order Preservation

```
Propagation events are delivered in timestamp order.
Out-of-order delivery is a constraint violation.
```

### PROP-3 · Idempotent Consumption

```
Receiving modules must handle duplicate events gracefully.
A repeated mode_transition with the same timestamp is a no-op.
```

---

## 6. Module Inheritance Block
Any module can inherit Mode Layer awareness by including this block
in its session-context:

```yaml
# Mode Propagation — Inherited
mode_propagation:
  version: 1.0
  listens_to:
    - mode_transition
    - mode_violation
  receives_from: Mode (Session Layer)
  coherence_source: Regime Layer
  default_stance: M_chat
  on_missing_event: assume M_chat
```

Paste this into any module's session-context to make it Mode-aware.
The module will automatically receive mode events and adjust its behavior.

---

## 7. Lineage

```
Source:     Mode Operator (M) + MCL
Targets:   Opacity, Capture, Context
Inbound:   Regime Layer (coherence posture only)
Layer:     Session
Pattern:   push-based, event-driven, declarative
```


🔙 Back to Mode Module · Operators · Constraints · Tests

Cross-Module Propagation v1.0 · RTT/1 Session Layer · TriadicFrameworks
