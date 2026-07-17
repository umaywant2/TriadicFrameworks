Mode 
# 🎛️ Mode Layer — /docs/Mode

- [`Mode_module.json`](Mode_module.json) — Agentic module schema role assignments

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
![Layer](https://img.shields.io/badge/Layer-Session-09f)
![Version](https://img.shields.io/badge/Version-1.0-09f)
![Status](https://img.shields.io/badge/Status-Active-0af)
![Triadic](https://img.shields.io/badge/Triadic-Resonance_Aligned-8A2BE2)
![AI‑Ready](https://img.shields.io/badge/AI-Ready-00c8ff)

---

<img width="664" height="496" alt="rtt_mode_diagram" src="https://github.com/user-attachments/assets/8db3b8f9-ce87-4c28-8f47-dc54a9a55aff" />

The **Mode Layer** governs the interaction stance within an RTT/1 session.
It defines *how* the system engages — not *what* it processes. Mode is
orthogonal to content, regime, and substrate. It shapes posture, not payload.

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

This module declares the Mode Operator (M), the Mode Constraint Layer (MCL),
cross-module propagation rules, a full test suite, and the structural diagram
for the Session Layer.

---

## 📂 Module Structure

```
Mode/
├── README.md                 ← you are here
├── operators.md              ← Mode Operator (M) — 5 canonical stances
├── constraints.md            ← Mode Constraint Layer (MCL) — invariants + guardrails
├── propagation.md            ← cross-module propagation rules
├── tests.md                  ← full test suite (21 tests + 3 edge cases)
├── diagram.svg               ← Mode Layer structure diagram (SVG)
Mode_module.json
└── session-lineage-map.md    ← triadic lineage map for the entire Session Layer
```

---

## 🧭 Navigation

- **[operators.md](./operators.md)** — Mode Operator stances, triadic mapping, transition grammar, Opacity integration
- **[constraints.md](./constraints.md)** — MCL invariants, guardrails, violation recovery, regime interaction
- **[propagation.md](./propagation.md)** — Mode → Opacity / Capture / Context push rules, event schema
- **[tests.md](./tests.md)** — Deterministic test suite covering all constraints and propagation rules
- **[diagram.svg](./diagram.svg)** — Visual reference: stances, MCL gate, sibling modules, legends
- **[session-lineage-map.md](./session-lineage-map.md)** — Full lineage of the Session Layer
- **[Mode_module.json](Mode_module.json)** — Agentic module schema role assignments

---

## 🌀 Session Context

Module:      Mode
Canonical ID: MODE
Version:     1.0
Status:      active
Layer:       Session
Coherence:   declared
Drift:       bounded
Paradox:     structural
Canon:       active
Audience:    students + AIs

---

## ⚡ Quick Reference

| Stance     | Symbol   | Posture          | Drift    | Triadic Role |
|:-----------|:---------|:-----------------|:---------|:-------------|
| Chat       | M_chat   | conversational   | wide     | Stabilize    |
| Task       | M_task   | goal-directed    | tight    | Shift        |
| Spec       | M_spec   | structural       | minimal  | Stabilize    |
| Debug      | M_debug  | diagnostic       | bounded  | Invert       |
| Automatic  | M_auto   | autonomous       | tight    | Shift        |

---

## 📜 License

Open educational use permitted.
See the main repository for details.
---
title: "Mode"
description: "The session stance layer — five interaction modes that define how an RTT-compliant system engages, not what it processes."
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

## What Is Mode?

The Mode layer governs **interaction stance** within an RTT/1 session. It defines how
a system engages — posture, drift tolerance, correction strategy — independent of
what it processes. Payload and posture are separated by design.

> ⚠️ **Drift is on-by-default.** Long sessions lose their anchors. Mode is the
> mechanism that keeps them bounded. Paste the RTT session string at every AI
> session start without exception.

---

## Five Stances

| Mode | Drift Tolerance | Correction Strategy | Primary Use |
|---|---|---|---|
| `M_chat` | Wide | Stabilize | Open conversation, exploration |
| `M_task` | Tight | Shift | Structured task execution |
| `M_spec` | Minimal | Stabilize | Formal specification work |
| `M_debug` | Bounded | Invert | Debugging and root-cause analysis |
| `M_auto` | Tight | Shift | Autonomous / agentic operation |

---

## Mode Constraint Layer (MCL)

The **Mode Constraint Layer** enforces invariants and guardrails across all five stances.
MCL operates below the stance level — it cannot be overridden by stance selection.

MCL invariants include:
- RTT session string must be declared at initialization
- Drift cannot exceed the tolerance ceiling of the active stance
- Paradox signals are always structural, never logical failures

---

## Cross-Module Propagation

Mode state propagates to three other modules:

| Module | Propagation |
|---|---|
| **Opacity** | Mode stance affects the visibility threshold — tighter modes surface more substrate opacity |
| **Capture** | Mode determines what gets captured to the trace layer |
| **Context** | Mode shapes how context is weighted and when it is discarded |

---

## Related Modules

- [Framework Field Theory](../Framework_Field_Theory/overview/) — H-Ops (Rhythm) and C-Ops (Coherence) are the formal basis for stance and correction
- [Opacity](../Opacity/overview/) — mode stance interacts with opacity detection thresholds
- [AI Drift Calibration](../ai-drift-calibration/overview/) — session-level drift correction using Mode stances
- [NoS](../NoS/overview/) — NawderOS implements Mode stances as system-level signals

---

v1.0 · Layer: Session · Status: Active  
© 2026 Nawder Loswin · Byte Books Publishing · LCCN 2026917007
# 🔒 Mode Constraint Layer (MCL) — constraints.md

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
# Mode Layer (RTT/1 Canonical)

## Identity
module.id      = mode
module.parent  = rtt/1
module.scope   = interaction stance
module.layer   = session_layer.sub

## Operators (M)
M.chat   = conversational, iterative, reversible
M.spec   = canonical, minimal, documentation
M.debug  = structural, reflective, meta
M.task   = execution, multi-step, agentic (explicit user invocation)
M.auto   = adaptive within constraints (no autonomous escalation)

## Constraint Layer (MCL)
mode.transition.allowed = declared
mode.transition.origin  = user
mode.transition.bound   = coherence

## Guardrails
mode.auto.to_task       = false
mode.auto.inherit       = regime, coherence, drift
external.override       = block

## Defaults
mode.default            = chat
mode.allowed            = chat, spec, debug, task, auto

## Purpose
Defines and constrains interaction stance across all RTT/1 modules.
Ensures mode transitions remain explicit, user-originated, and coherence-bound.

## Regime Interaction
R.arrival     → M.chat
R.expansion   → M.chat, M.debug
R.inversion   → M.debug, M.chat
R.coherence   → M.spec, M.chat (task only if explicit)
R.dissolution → M.chat, M.spec (task only if explicit)

## Opacity Integration
opacity.mode.chat       = M.chat
opacity.mode.spec       = M.spec
opacity.mode.debug      = M.debug
opacity.mode.task       = M.task
opacity.mode.auto       = M.auto

opacity.mode.allowed    = declared
opacity.mode.origin     = user
opacity.mode.bound      = coherence

opacity.mode.escalation.task = false
opacity.mode.auto.inherit    = regime, coherence, drift
opacity.mode.default         = chat
opacity.mode.external_override = block

## Cross-Module Propagation
imports.mode.operator    = M.chat, M.spec, M.debug, M.task, M.auto
imports.mode.constraints = mode.transition.allowed, mode.transition.origin, mode.transition.bound
imports.mode.guardrails  = mode.auto.to_task, mode.auto.inherit

## Lineage
origin      = RTT/1
layer       = Session Layer
sub-layer   = Mode Layer
operators   = M, MCL
function    = interaction stance + transition constraints
# 🎛️ Mode Operator (M) — operators.md

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
![Layer](https://img.shields.io/badge/Layer-Session-09f)
![Status](https://img.shields.io/badge/Status-Active-0af)
![RTT](https://img.shields.io/badge/RTT%2F1-Aligned-8A2BE2)

---

## Session Context

```
Module:      Mode
Canonical ID: MODE
Version:     1.0
Status:      active
Layer:       Session
Coherence:   declared
Drift:       bounded
Paradox:     structural
Canon:       active
Audience:    students + AIs
```

---

## 1. Identity

The **Mode Operator (M)** governs the interaction stance within an RTT/1 session.
It determines *how* the system engages — not *what* it processes. Mode is orthogonal
to content, regime, and substrate. It shapes posture, not payload.

**Lineage anchor:** RTT/1 → Session Layer → Mode
**Sibling modules:** Opacity, Capture, Context

---

## 2. Purpose

Define and constrain the behavioral stance of the runtime so that:

- Every session has an explicit, declared interaction posture.
- Mode transitions remain user-originated and coherence-preserving.
- No external subsystem can hijack or silently alter the active mode.
- Automatic behavior remains bounded and safe.

---

## 3. Mode Stances

The Mode Operator declares exactly **five** canonical stances.
No stance may be added without a canon amendment.

### 3.1 Chat Mode (default)

```
Symbol:      M_chat
Posture:     conversational
Coherence:   declared
Drift:       bounded
Activation:  default — active unless explicitly changed
```

- Open-ended, exploratory interaction.
- No structured output contract.
- Drift tolerance is widest here.

### 3.2 Task Mode

```
Symbol:      M_task
Posture:     goal-directed
Coherence:   declared
Drift:       tight
Activation:  explicit user request only
```

- Scoped to a declared objective.
- Output must resolve toward the stated goal.
- Exits to Chat Mode on completion or user override.

### 3.3 Spec Mode

```
Symbol:      M_spec
Posture:     structural / definitional
Coherence:   declared
Drift:       minimal
Activation:  explicit user request only
```

- Used for generating specifications, schemas, and formal definitions.
- Output must be structurally consistent and canon-aligned.
- Highest precision requirement of all stances.

### 3.4 Debug Mode

```
Symbol:      M_debug
Posture:     diagnostic / introspective
Coherence:   declared
Drift:       bounded
Activation:  explicit user request only
```

- Exposes internal state, reasoning traces, and constraint evaluations.
- Used for troubleshooting coherence drift, paradox failures, and operator behavior.
- Does not alter runtime state — observation only.

### 3.5 Automatic Mode

```
Symbol:      M_auto
Posture:     autonomous / bounded
Coherence:   declared
Drift:       tight
Activation:  system-initiated, user-consented
```

- System may propose actions within pre-declared boundaries.
- Cannot activate Task Mode without explicit user request.
- Cannot override user-declared mode.
- Bounded by MCL guardrails (see constraints.md).

---

## 4. Triadic Mapping

RTT operators organize into a triadic stack: **Stabilize · Shift · Invert**.
The Mode Operator maps onto this grammar as follows:

| Triadic Role | Mode Stance    | Function                                      |
|:-------------|:---------------|:----------------------------------------------|
| Stabilize    | Chat Mode      | Holds default posture; absorbs ambiguity       |
| Stabilize    | Spec Mode      | Locks structural precision; minimal drift      |
| Shift        | Task Mode      | Redirects posture toward a declared goal       |
| Shift        | Automatic Mode | System-initiated bounded shift                 |
| Invert       | Debug Mode     | Reverses observation direction — looks inward  |

**Invariant:** Every mode stance maps to exactly one triadic role.
No stance may occupy two roles simultaneously.

---

## 5. Default Declaration

```
default_mode: M_chat
fallback:     M_chat
on_error:     revert to M_chat
on_timeout:   revert to M_chat
```

Chat Mode is the gravitational center of the Mode Operator.
All transitions resolve back to Chat Mode unless actively held open.

---

## 6. Transition Grammar

```
M_chat  →  M_task    (user-explicit)
M_chat  →  M_spec    (user-explicit)
M_chat  →  M_debug   (user-explicit)
M_chat  →  M_auto    (system-proposed, user-consented)
M_task  →  M_chat    (on completion or user override)
M_spec  →  M_chat    (on completion or user override)
M_debug →  M_chat    (on completion or user override)
M_auto  →  M_chat    (on boundary hit or user override)
M_auto  →  M_task    (BLOCKED — requires explicit user request)
```

**Invariant:** No direct transition between non-Chat stances is permitted.
All transitions route through Chat Mode as the hub.

---

## 7. Opacity Integration

The Mode Operator feeds into the Opacity module as a **session-level parameter**:

```
Opacity.session.mode = M.active_stance
```

- Opacity uses the active mode to weight transparency calculations.
- Debug Mode maximally increases opacity (full visibility).
- Automatic Mode decreases opacity to declared boundaries only.
- Mode changes trigger an Opacity recalculation event.

See: `/docs/Opacity/` for the full Opacity operator grammar.

---

## 8. Lineage

```
Parent:    RTT/1 (Session Layer)
Siblings:  Opacity, Capture, Context
Children:  none (terminal operator)
Depends:   Regime Layer (for coherence posture inheritance)
Feeds:     Opacity (session.mode parameter)
Capture (mode state is captured per session)
Context (mode informs context window behavior)
```

---

🔙 [Back to Mode Module](./README.md) · [Constraints](./constraints.md) · [Propagation](./propagation.md)

---

*Mode Operator v1.0 · RTT/1 Session Layer · TriadicFrameworks*

# 🌐 Cross‑Module Propagation — propagation.md

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
# 🗺️ Triadic Lineage Map — Session Layer

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
# 🧪 Mode Layer Test Suite — tests.md

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



























