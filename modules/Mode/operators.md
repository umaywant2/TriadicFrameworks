# 🎛️ Mode Operator (M) — operators.md

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

