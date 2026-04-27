# 🔒 Mode Constraint Layer (MCL) — constraints.md

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
![Component](https://img.shields.io/badge/Component-MCL-ff00d4)
![Status](https://img.shields.io/badge/Status-Active-0af)
![RTT](https://img.shields.io/badge/RTT%2F1-Aligned-8A2BE2)

---

## Session Context

```
Module:      Mode
Component:   Mode Constraint Layer (MCL)
Version:     1.0
Status:      active
Layer:       Session
Coherence:   declared
Drift:       bounded
Canon:       active
```

---

## 1. Purpose

The **Mode Constraint Layer (MCL)** binds all Mode Operators to RTT/1's declared
coherence, drift bounds, and user-origin constraints. It enforces that mode
transitions remain **explicit**, **user-originated**, and **coherence-preserving**.

The MCL is not a policy layer — it is a structural constraint. It cannot be
overridden by configuration, preference, or external workflow. It is load-bearing.

---

## 2. Invariants

The MCL declares exactly **three** structural invariants.
These hold across all sessions, all stances, and all regimes.

### INV-1 · User Origin

```
All mode transitions must originate from the user.
```

- No system process, external workflow, or automated routine may change
  the active mode without explicit user declaration.
- Automatic Mode may *propose* actions but cannot *transition* modes.
- This invariant is unconditional — no framing, context, or urgency
  overrides it.

### INV-2 · Coherence Preservation

```
No mode transition may violate the declared coherence posture.
```

- If the current session declares `coherence: declared`, every mode
  transition must preserve that declaration.
- A transition that would create an undeclared or ambiguous coherence
  state is rejected.
- Coherence posture is inherited from the Regime Layer (see propagation.md).

### INV-3 · Chat Mode Gravity

```
Chat Mode is the default, fallback, and recovery state.
```


- Every session begins in Chat Mode unless the user explicitly declares
  otherwise at session start.
- Every error, timeout, or unresolved transition reverts to Chat Mode.
- Chat Mode cannot be removed, disabled, or deprioritized.

---

## 3. Guardrails

Guardrails are operational rules that enforce the invariants at runtime.
The MCL declares exactly **five** guardrails.

### GRD-1 · No Silent Mode Changes

```
Rule:    Mode changes must be announced and logged.
Scope:   all stances
Enforces: INV-1
```


- Every mode transition generates a session event.
- The event includes: previous stance, new stance, timestamp, origin (user/system).
- Silent transitions are a constraint violation.

### GRD-2 · Automatic Mode Cannot Escalate

```
Rule:    Automatic Mode cannot activate Task Mode.
Scope:   M_auto only
Enforces: INV-1
```

- Automatic Mode may propose actions within its declared boundaries.
- It may **not** activate Task Mode, Spec Mode, or Debug Mode.
- Escalation requires an explicit user request routed through Chat Mode.

### GRD-3 · No External Mode Hijacking

```
Rule:    No external workflow may override user-declared mode.
Scope:   all stances
Enforces: INV-1, INV-2
```

- External systems, plugins, or integrations cannot set or change the
  active mode.
- They may *request* a mode change by surfacing a proposal in Chat Mode.
- The user must explicitly accept the proposal for the transition to occur.

### GRD-4 · Drift Bound Enforcement

```
Rule:    Mode transitions must respect the stance's drift tolerance.
Scope:   all stances
Enforces: INV-2
```


- Each stance declares a drift tolerance (see operators.md §3).
- A transition is rejected if the resulting state would exceed the
  target stance's drift bounds.
- Drift is evaluated at transition time, not retrospectively.

| Stance    | Drift Tolerance |
|:----------|:----------------|
| Chat      | bounded (wide)  |
| Task      | tight           |
| Spec      | minimal         |
| Debug     | bounded         |
| Automatic | tight           |

### GRD-5 · Hub-and-Spoke Routing

```
Rule:    All mode transitions route through Chat Mode.
Scope:   non-Chat stances
Enforces: INV-3
```

- No direct transition between non-Chat stances is permitted.
- Task → Spec requires: Task → Chat → Spec.
- This ensures Chat Mode remains the observable, stable center.

---

## 4. Constraint Violations

When a constraint is violated, the MCL enforces a deterministic recovery:

```
on_violation:

1. Log the violation (stance, invariant, guardrail, timestamp).

2. Reject the attempted transition.

3. Revert to Chat Mode (INV-3).

4. Surface the violation to the user in Chat Mode.
```

Violations are **not silent**. The user always sees what happened and why.

---

## 5. Session-Context Override Block

This block can be pasted into any module's session-context to inherit Mode
constraints. It is minimal, non-intrusive, and cross-module compatible.

```yaml
# Mode Constraint Layer — Session Override
mode_constraint_layer:
  version: 1.0
  invariants:
    - user_origin
    - coherence_preservation
    - chat_mode_gravity
  guardrails:
    - no_silent_mode_changes
    - automatic_mode_cannot_escalate
    - no_external_mode_hijacking
    - drift_bound_enforcement
    - hub_and_spoke_routing
  default_mode: M_chat
  fallback: M_chat
  on_error: revert_to_M_chat
  on_violation: log_reject_revert_surface
```

### Operational consequences of pasting this block:

- No module can be forced into Task Mode.
- No external subsystem can hijack mode.
- Automatic Mode remains bounded and safe.
- Chat Mode stays the stable default.
- Coherence posture remains the governing constraint.

---

## 6. Regime Layer Interaction
The MCL inherits its coherence posture from the Regime Layer:

```
Regime Layer → declares coherence posture
  ↓
Mode Constraint Layer → enforces coherence during transitions
  ↓
Mode Operator → executes transitions within constraints
```

| Regime Posture | MCL Effect |
| --- | --- |
| declared | All transitions must be explicitly declared |
| inferred | Transitions may be proposed, user confirms |
| suspended | All non-Chat modes locked; Chat Mode only |

When the Regime Layer changes its coherence posture, the MCL re-evaluates
all active constraints. If the new posture is more restrictive, non-Chat
modes are gracefully exited.

## 7. Lineage

```
Parent:    Mode Operator (M)
Layer:     Session → Mode → MCL
Depends:   Regime Layer (coherence posture)
Feeds:     Mode Operator (transition gating)
           Opacity (constraint state visibility)
           Capture (constraint violations logged)
```


🔙 Back to Mode Module · Operators · Propagation

Mode Constraint Layer v1.0 · RTT/1 Session Layer · TriadicFrameworks
