# 🧪 Mode Layer Test Suite — tests.md

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
![Component](https://img.shields.io/badge/Component-Tests-00c8ff)
![Status](https://img.shields.io/badge/Status-Active-0af)
![RTT](https://img.shields.io/badge/RTT%2F1-Aligned-8A2BE2)

---

## Session Context

```
Module:      Mode
Component:   Test Suite
Version:     1.0
Status:      active
Layer:       Session
Coherence:   declared
Drift:       bounded
Canon:       active
```

---

## 1. Purpose

This test suite validates the Mode Operator (M), Mode Constraint Layer (MCL),
and cross-module propagation rules. Each test is minimal, deterministic, and
maps to a specific invariant, guardrail, or propagation rule.

**Test philosophy:** A test that cannot name the constraint it validates
does not belong in this suite.

---

## 2. Test Index

| ID       | Component   | Tests                          | Constraint     |
|:---------|:------------|:-------------------------------|:---------------|
| T-M-001  | Operator    | Default stance is Chat Mode    | INV-3          |
| T-M-002  | Operator    | Valid transition Chat → Task   | Transition     |
| T-M-003  | Operator    | Valid transition Chat → Spec   | Transition     |
| T-M-004  | Operator    | Valid transition Chat → Debug  | Transition     |
| T-M-005  | Operator    | Valid transition Chat → Auto   | Transition     |
| T-M-006  | Operator    | Revert on completion           | INV-3          |
| T-M-007  | Operator    | Revert on error                | INV-3          |
| T-M-008  | Operator    | Revert on timeout              | INV-3          |
| T-MCL-001| MCL         | User origin required           | INV-1          |
| T-MCL-002| MCL         | Coherence preserved            | INV-2          |
| T-MCL-003| MCL         | Chat Mode gravity              | INV-3          |
| T-MCL-004| MCL         | No silent mode changes         | GRD-1          |
| T-MCL-005| MCL         | Auto cannot escalate to Task   | GRD-2          |
| T-MCL-006| MCL         | No external hijacking          | GRD-3          |
| T-MCL-007| MCL         | Drift bound enforcement        | GRD-4          |
| T-MCL-008| MCL         | Hub-and-spoke routing          | GRD-5          |
| T-P-001  | Propagation | Mode → Opacity event fires     | PROP-1         |
| T-P-002  | Propagation | Mode → Capture event logged    | PROP-2         |
| T-P-003  | Propagation | Mode → Context window adjusts  | PROP-1         |
| T-P-004  | Propagation | Regime → Mode posture change   | PROP-2         |
| T-P-005  | Propagation | Idempotent duplicate handling  | PROP-3         |

---

## 3. Operator Tests

### T-M-001 · Default Stance

```
Given:   A new session starts with no mode declaration.
When:    The session initializes.
Then:    Active stance = M_chat.
Validates: INV-3 (Chat Mode gravity)
```

### T-M-002 · Chat → Task Transition

```
Given:   Active stance = M_chat.
When:    User explicitly requests Task Mode.
Then:    Active stance = M_task.
Transition event is logged.
Opacity recalculates.
Validates: Transition grammar, GRD-1
```

### T-M-003 · Chat → Spec Transition

```
Given:   Active stance = M_chat.
When:    User explicitly requests Spec Mode.
Then:    Active stance = M_spec.
Drift tolerance = minimal.
Validates: Transition grammar, GRD-4
```

### T-M-004 · Chat → Debug Transition

```
Given:   Active stance = M_chat.
When:    User explicitly requests Debug Mode.
Then:    Active stance = M_debug.
Opacity = maximum transparency.
Validates: Transition grammar, Opacity integration
```

### T-M-005 · Chat → Auto Transition

```
Given:   Active stance = M_chat.
When:    System proposes Automatic Mode and user consents.
Then:    Active stance = M_auto.
Drift tolerance = tight.
Validates: Transition grammar, INV-1
```

### T-M-006 · Revert on Completion

```
Given:   Active stance = M_task.
When:    Task completes successfully.
Then:    Active stance = M_chat.
Validates: INV-3 (Chat Mode gravity)
```

### T-M-007 · Revert on Error

```
Given:   Active stance = M_spec.
When:    An unrecoverable error occurs.
Then:    Active stance = M_chat.
Error is surfaced to the user.
Validates: INV-3, default_mode fallback
```

### T-M-008 · Revert on Timeout

```
Given:   Active stance = M_debug.
When:    Session timeout threshold is reached.
Then:    Active stance = M_chat.
Validates: INV-3, on_timeout behavior
```

---

## 4. MCL Tests

### T-MCL-001 · User Origin Required

```
Given:   Active stance = M_chat.
When:    A system process attempts to transition to M_task
without user request.
Then:    Transition is REJECTED.
Violation logged: INV-1.
Active stance remains M_chat.
Validates: INV-1 (user origin)
```

### T-MCL-002 · Coherence Preserved

```
Given:   Coherence posture = declared.
When:    A transition would create an ambiguous coherence state.
Then:    Transition is REJECTED.
Violation logged: INV-2.
Validates: INV-2 (coherence preservation)
```

### T-MCL-003 · Chat Mode Gravity

```
Given:   Active stance = M_auto.
When:    Automatic Mode hits its boundary.
Then:    Active stance = M_chat (not M_task or any other stance).
Validates: INV-3 (Chat Mode gravity)
```

### T-MCL-004 · No Silent Mode Changes

```
Given:   Active stance = M_chat.
When:    User requests transition to M_task.
Then:    A mode_transition event is generated with:
previous = M_chat, current = M_task,
timestamp, origin = user.
Event is visible in Capture log.
Validates: GRD-1 (no silent changes)
```

### T-MCL-005 · Auto Cannot Escalate

```
Given:   Active stance = M_auto.
When:    Automatic Mode attempts to activate M_task.
Then:    Transition is REJECTED.
Violation logged: GRD-2.
M_auto may propose but not escalate.
Validates: GRD-2 (auto cannot escalate)
```

### T-MCL-006 · No External Hijacking

```
Given:   Active stance = M_chat.
When:    An external workflow attempts to set mode to M_spec.
Then:    Transition is REJECTED.
Violation logged: GRD-3.
External system may surface a proposal in Chat Mode.
Validates: GRD-3 (no external hijacking)
```

### T-MCL-007 · Drift Bound Enforcement

```
Given:   Active stance = M_chat (drift = bounded/wide).
When:    User requests transition to M_spec (drift = minimal).
Then:    Transition succeeds only if current state does not
exceed M_spec's drift bounds.
If drift exceeds bounds: transition REJECTED, GRD-4.
Validates: GRD-4 (drift bound enforcement)
```

### T-MCL-008 · Hub-and-Spoke Routing

```
Given:   Active stance = M_task.
When:    User requests transition to M_spec (direct).
Then:    Transition is REJECTED.
System routes: M_task → M_chat → M_spec.
Two events are logged.
Validates: GRD-5 (hub-and-spoke routing)
```

---

## 5. Propagation Tests

### T-P-001 · Mode → Opacity Event

```
Given:   Active stance = M_chat.
When:    User transitions to M_debug.
Then:    Opacity receives mode_transition event.
Opacity recalculates: transparency = maximum.
No stale mode state persists in Opacity.
Validates: PROP-1 (no stale state)
```

### T-P-002 · Mode → Capture Logging

```
Given:   Active stance = M_chat.
When:    User transitions to M_task.
Then:    Capture records the event BEFORE the transition completes.
Log entry includes: M_chat → M_task, timestamp, user origin.
Events are in timestamp order.
Validates: PROP-2 (order preservation)
```

### T-P-003 · Mode → Context Adjustment

```
Given:   Active stance = M_chat (wide context).
When:    User transitions to M_task.
Then:    Context window narrows to goal-scoped behavior.
Adjustment completes before next user input is processed.
Validates: PROP-1 (no stale state)
```

### T-P-004 · Regime → Mode Posture Change

```
Given:   Regime posture = declared.
Active stance = M_task.
When:    Regime Layer changes posture to suspended.
Then:    MCL re-evaluates constraints.
M_task exits gracefully to M_chat.
Non-Chat modes are locked.
Validates: Regime interaction, PROP-2
```

### T-P-005 · Idempotent Duplicate Handling

```
Given:   Opacity received mode_transition (M_chat → M_task, T=100).
When:    A duplicate event arrives (M_chat → M_task, T=100).
Then:    Opacity treats it as a no-op.
No recalculation occurs.
Validates: PROP-3 (idempotent consumption)
```

---

## 6. Edge Cases

### T-EDGE-001 · Rapid Sequential Transitions

```
Given:   Active stance = M_chat.
When:    User requests M_task, then immediately requests M_chat.
Then:    Both transitions complete in order.
Two events logged. Final stance = M_chat.
No intermediate state is lost.
```

### T-EDGE-002 · Session Start with Explicit Mode

```
Given:   User declares M_spec at session start.
When:    Session initializes.
Then:    Active stance = M_spec (not M_chat).
Chat Mode gravity applies on exit, not on override at start.
```

### T-EDGE-003 · Violation During Auto Mode

```
Given:   Active stance = M_auto.
When:    M_auto attempts an action that violates INV-1.
Then:    Violation logged.
M_auto reverts to M_chat.
Violation is surfaced to user.
```

---

## 7. Coverage Matrix

```
Invariants:   INV-1 ✓  INV-2 ✓  INV-3 ✓
Guardrails:   GRD-1 ✓  GRD-2 ✓  GRD-3 ✓  GRD-4 ✓  GRD-5 ✓
Propagation:  PROP-1 ✓ PROP-2 ✓ PROP-3 ✓
Stances:      Chat ✓  Task ✓  Spec ✓  Debug ✓  Auto ✓
Edge cases:   3/3 ✓
```

**Full coverage achieved.** Every constraint, guardrail, propagation rule,
and stance is tested at least once.

---

🔙 [Back to Mode Module](./README.md) · [Operators](./operators.md) · [Constraints](./constraints.md) · [Propagation](./propagation.md)

---

*Mode Layer Test Suite v1.0 · RTT/1 Session Layer · TriadicFrameworks*



























