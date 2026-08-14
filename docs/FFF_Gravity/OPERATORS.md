# FFF_Gravity · Operators

```
# ┌─────────────────────────────────────────────────────────────┐
# │                  DOCUMENT FRONTMATTER                       │
# └─────────────────────────────────────────────────────────────┘
document:         OPERATORS
canonical_path:   docs/FFF_Gravity/OPERATORS.md
canonical_tag:    "[FFF:GRAVITY:OPERATORS]"
framework:        TriadicFrameworks
module:           FFF_Gravity
version:          1.0.0
status:           canonical
stability:        living
created:          2026-08-13
last_modified:    2026-08-13
authors:
  - TriadicFrameworks
encoding:         UTF-8
line_endings:     LF
normative:        true
description: >
  Single source of truth for every operator symbol defined in FFF_Gravity.
  Covers primary operators, derived operators, state flags, engineering
  primitives, failure modes, composition rules, evaluation order, and
  the symbol freeze registry. All function files must resolve symbol
  conflicts against this document before publishing.
tags:
  - FFF
  - gravity
  - operators
  - symbols
  - registry
  - normative

session_context:
  current_session:
    session_id:       SES-20260813-OPS-001
    opened_at:        2026-08-13T07:48:00-04:00
    closed_at:        ~
    editor:           Nawder
    branch:           main
    intent:           Create canonical OPERATORS.md — master symbol authority for FFF_Gravity
    status:           active
    dirty:            true
    sections_touched: [§0, §1, §2, §3, §4, §5, §6, §7, §8, §9, §10]

  session_history:
    - session_id:  SES-20260813-README-001
      intent:      Create canonical README.md
      status:      closed
    - session_id:  SES-20260813-INDEX-001
      intent:      Create canonical INDEX.md
      status:      closed

changelog:
  - version: 1.0.0
    date:    2026-08-13
    author:  TriadicFrameworks
    notes: >
      Initial canonical release. 9 primary operators, 10 derived operators,
      11 state flags, 15 primitives, 10 failure modes. All symbols from
      f_Capture.md v1.0.0 frozen. Wave 3+ symbols marked pending.
```

> **Canonical path:** `docs/FFF_Gravity/OPERATORS.md`
> **Authority:** This document is the single source of truth for all operator
> symbols in FFF_Gravity. In any conflict between this file and a function
> file, this file governs.
> **Normative:** Yes — all sections except §0 and §10 are normative.

---

## §0 · Session Context

<!--
  metadata:
    section:       session-context
    section_id:    §0
    type:          live-session-register
    normative:     false
    created_in:    SES-20260813-OPS-001
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

### Active Session

| Field | Value |
|---|---|
| Session ID | `SES-20260813-OPS-001` |
| Opened | `2026-08-13T07:48:00-04:00` |
| Closed | — (active) |
| Editor | Nawder |
| Branch | `main` |
| Intent | Create canonical OPERATORS.md — master symbol authority |
| Status | 🟡 Active |

### Update Policy

```
When to update this file:
  1. A new operator is introduced in any function file         → add to §1 or §2
  2. A new state flag is introduced                            → add to §3
  3. A new primitive is defined in any function file           → add to §4
  4. A new failure mode is defined                             → add to §5
  5. A composition rule is formalized                          → add to §6
  6. A scaffold file is promoted to canonical                  → update §8 freeze status
  7. A version bump occurs                                     → update §9 and CHANGELOG.md

Never:
  - Remove a frozen symbol (deprecate instead)
  - Rename a frozen symbol without a major version bump
  - Add a symbol that conflicts with FFF_Field, FFF_Momentum, or FFF_Resonance namespaces
```

---

## §1 · Primary Operators

<!--
  metadata:
    section:       primary-operators
    section_id:    §1
    type:          registry
    normative:     true
    operator_class: input
    operator_count: 9
    unit_system:   dimensionless-normalized
    frozen:        all 9 frozen at v1.0.0
    created_in:    SES-20260813-OPS-001
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

Primary operators are direct inputs to `f_Capture` and its sibling functions.
They are measured or externally provided — not computed from other operators.
All 9 are frozen at v1.0.0.

### §1.1 · Full Specification Table

| Symbol | Full Name | FFF Node | Type | Domain | Range | Unit | Frozen | Defined In |
|---|---|---|---|---|---|---|---|---|
| `v_approach` | Approach Vector | `F_force` | scalar | ℝ≥0 | [0, ∞) | normalized velocity | ✅ | `f_Capture.md §4.1` |
| `v_escape(A)` | Escape Velocity | `F_freq` | scalar | ℝ>0 | (0, ∞) | normalized velocity | ✅ | `f_Capture.md §4.1` |
| `ρ(Φ)` | Field Density | `F_freq` | scalar | ℝ≥0 | [0, 1] | dimensionless | ✅ | `f_Field.md §4.1` |
| `r_capture` | Capture Radius | Frame | scalar | ℝ>0 | (0, ∞) | normalized distance | ✅ | `f_Capture.md §4.1` |
| `β` | Binding Coefficient | derived | scalar | ℝ≥0 | [0, ∞) | dimensionless | ✅ | `f_Capture.md §4.1` |
| `ω_res` | Orbital Resonance | `F_freq` | ratio | ℚ ∪ ℝ | rational or irrational | dimensionless | ✅ | `f_Capture.md §4.1` |
| `M_A` | Attractor Mass | `F_fluid` | scalar | ℝ>0 | (0, ∞) | normalized mass | ✅ | `f_Field.md §4.1` |
| `M_E` | Element Mass | `F_fluid` | scalar | ℝ>0 | (0, ∞) | normalized mass | ✅ | `f_Capture.md §4.1` |
| `r` | Separation Distance | geometry | scalar | ℝ>0 | (0, ∞) | normalized distance | ✅ | `f_Capture.md §4.1` |

### §1.2 · Operator Constraints and Guards

| Symbol | Hard Constraints | Guard Violation Consequence |
|---|---|---|
| `v_approach` | Evaluated at `r_capture` crossing only; not at outer field boundary | Premature evaluation → invalid `C_thresh` |
| `v_escape(A)` | Must be recomputed if `ρ(Φ)` changes between entry and encounter | Stale value → FM-006 risk |
| `ρ(Φ)` | `0` = null field — triggers FM-002 immediately; `1` = saturated | Unguarded null → undefined `P_eff` |
| `r_capture` | Set by Attractor; cannot be modified by Element or engineering primitives | Modification → Frame integrity failure |
| `β` | Must be ≥ 1.0 for capture to proceed; `< 1.0` = flyby unconditionally | Below floor → `CAPTURE_FAILED` regardless of all other conditions |
| `ω_res` | Irrational value = FM-004 at any point — during approach or post-lock | Irrational → `CAPTURE_DECAYING` |
| `M_A` | Must be finite and positive; `M_A ≈ M_E` triggers FM-007 check | Mass parity → dissolution path |
| `M_E` | Must be finite and positive | Zero or infinite mass → undefined behavior |
| `r` | `r = 0` is undefined (singularity); `r > r_capture` → short-circuit in `evaluate_capture_threshold` | Zero → ⊥ |

### §1.3 · Node Assignment Summary

| FFF Node | Symbols |
|---|---|
| `F_freq` (Frequency) | `v_escape(A)`, `ρ(Φ)`, `ω_res` |
| `F_fluid` (Fluids) | `M_A`, `M_E` |
| `F_force` (Forces) | `v_approach` |
| Frame | `r_capture` |
| Geometry | `r` |
| Derived (no single node) | `β` |

---

## §2 · Derived Operators

<!--
  metadata:
    section:       derived-operators
    section_id:    §2
    type:          registry
    normative:     true
    operator_class: computed
    operator_count: 10
    depends_on:    [§1]
    freeze_status: mixed — see §8
    created_in:    SES-20260813-OPS-001
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

Derived operators are computed from primary operators via defined formulas.
Symbols marked ✅ frozen are defined in `f_Capture.md v1.0.0` and cannot change.
Symbols marked 🔵 pending have formulas in scaffold files awaiting canonicalization.

### §2.1 · Full Specification Table

| Symbol | Full Name | Formula | Depends On | Output Range | Sign Convention | Frozen | Defined In |
|---|---|---|---|---|---|---|---|
| `P_eff` | Effective Pull | `M_A × ρ(Φ) / r²` | `M_A`, `ρ(Φ)`, `r` | [0, ∞) | always positive | ✅ | `f_Capture.md §4.2` |
| `C_thresh` | Capture Threshold | `v_escape(A) − v_approach` | `v_escape(A)`, `v_approach` | (−∞, ∞) | positive = capture possible; negative = escape | ✅ | `f_Capture.md §4.2` |
| `d_bind` | Binding Depth | `β × ρ(Φ) × (1 − e)` | `β`, `ρ(Φ)`, `e` | [0, ∞) | higher = more stable | ✅ | `f_Capture.md §4.2` |
| `p_res` | Residual Momentum | `M_E × (v_approach − C_thresh)` | `M_E`, `v_approach`, `C_thresh` | [0, ∞) | always positive post-capture | ✅ | `f_Capture.md §4.2` |
| `e` | Orbital Eccentricity | `p_res / (p_res + P_eff)` | `p_res`, `P_eff` | [0, 1) | 0 = circular; approaching 1 = near-parabolic | ✅ | `f_Orbit.md §4.1` |
| `T_orb` | Orbital Period | 🔵 pending `f_Orbit.md §4.1` | `d_bind`, `ω_res` | (0, ∞) | always positive | 🔵 | `f_Orbit.md §4.1` |
| `δ` | Decay Rate | `Δd_bind / Δt` | `d_bind` series | (−∞, 0] in decay | negative = losing energy | 🔵 | `f_Decay.md §4.1` |
| `E_rel` | Release Energy | 🔵 pending `f_Release.md §4.1` | `d_bind`, `p_res`, `ρ(Φ)` | [0, ∞) | energy required to achieve release | 🔵 | `f_Release.md §4.1` |
| `F_emit` | Emit Field Strength | 🔵 pending `f_Emit.md §4.1` | `M_A`, emit energy input | [0, ∞) | higher = deeper coherence well | 🔵 | `f_Emit.md §4.1` |
| `F_damp` | Dampen Depth | 🔵 pending `f_Dampen.md §4.1` | `ρ(Φ)`, dampen energy input | [0, 1] | fraction of `ρ(Φ)` to suppress | 🔵 | `f_Dampen.md §4.1` |

### §2.2 · Supplementary Operators (Engineering Primitives Layer)

These operators are introduced by engineering primitive files.
They extend the derived operator set and are pending canonicalization.

| Symbol | Full Name | Formula | Defined In | Frozen |
|---|---|---|---|---|
| `F_amp` | Amplification Factor | scalar ≥ 1.0 | `f_Amplify.md §4.1` | 🔵 |
| `β_max` | Binding Coefficient Ceiling | 🔵 pending | `f_Amplify.md §4.1` | 🔵 |
| `heading_delta` | Heading Change | angular delta (radians) applied to `v_approach` | `f_Deflect.md §4.1` | 🔵 |
| `r_emit` | Emission Radius | bounded region of `emit_field` effect | `f_Emit.md §4.1` | 🔵 |
| `r_damp` | Dampening Radius | bounded region of `suppress_field` effect | `f_Dampen.md §4.1` | 🔵 |
| `d_warn` | Decay Warning Threshold | `d_bind` level at which FM-004 is raised | `f_Decay.md §4.1` | 🔵 |
| `d_collapse` | Collapse Threshold | `d_bind` level at which FM-005 fires; `f_Collapse` triggered | `f_Decay.md §4.1` | 🔵 |
| `m_parity` | Mass Parity Threshold | max `|M_E − M_A|` below which FM-007 fires | `f_Collapse.md §4.1` | 🔵 |

### §2.3 · Undefined Conditions

| Operator | Undefined When | Symbol for Undefined |
|---|---|---|
| `P_eff` | `r = 0` (singularity) or `ρ(Φ) = 0` (FM-002) | ⊥ |
| `C_thresh` | `v_escape(A)` undefined (ρ = 0) | ⊥ |
| `d_bind` | `e ≥ 1` (hyperbolic trajectory — not captured) | ⊥ |
| `p_res` | `C_thresh ≤ 0` (no capture) | ⊥ |
| `e` | `P_eff = 0` (FM-002) | ⊥ |
| `δ` | Pre-capture (no time series) | ⊥ |
| `E_rel` | `d_bind = 0` (collapse state; release not viable) | ⊥ |
| `F_amp` | `β > β_max` (runaway — FM-010) | ⊥ |

---

## §3 · State Flags

<!--
  metadata:
    section:       state-flags
    section_id:    §3
    type:          fsm-registry
    normative:     true
    flag_count:    11
    flag_type:     discrete
    model:         deterministic finite state machine
    frozen:        all 11 frozen at v1.0.0
    created_in:    SES-20260813-OPS-001
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

State flags represent the discrete relational state of an Element in the FFF_Gravity system.
The state machine is **deterministic** — every transition has a single defined trigger.
No state is revisitable once terminal.
All 11 flags are frozen at v1.0.0.

### §3.1 · Flag Specification Table

| Flag | Entry Condition | Set By | Exit Condition | Valid Next States | Terminal |
|---|---|---|---|---|---|
| `CAPTURE_PENDING` | E crosses `r_capture`; outcome unresolved | `compute_approach_vector` | `C_thresh` evaluated | `CAPTURE_LOCKED`, `CAPTURE_FAILED` | No |
| `CAPTURE_LOCKED` | `C_thresh > 0` ∧ `β ≥ 1.0` ∧ Frame ok ∧ `ω_res ∈ ℚ` | `register_capture` | `d_bind` falls below `d_warn`; or FM-007 | `CAPTURE_DECAYING`, `CAPTURE_COLLISION` | No |
| `CAPTURE_DECAYING` | FM-004 raised; `d_bind` decreasing | `flag_decay` | `d_bind ≤ d_collapse` | `CAPTURE_FAILED`, `CAPTURE_COLLISION` | No |
| `CAPTURE_FAILED` | FM-001/002/003/006 raised; or decay → ejection | `register_capture` | — | — | **Yes** |
| `CAPTURE_COLLISION` | FM-005 terminal infall; or FM-007 dissolution | `execute_collapse` | — | — | **Yes** |
| `ORBIT_STABLE` | `stab_class = stable` ∧ `e < 0.5` post `CAPTURE_LOCKED` | `classify_orbit` | `stab_class` drops below stable threshold | `ORBIT_ECCENTRIC`, `CAPTURE_DECAYING` | No |
| `ORBIT_ECCENTRIC` | `e ≥ 0.5` while orbit is still captured | `classify_orbit` | `e` drops below 0.5; or FM-004 | `ORBIT_STABLE`, `CAPTURE_DECAYING` | No |
| `RELEASED` | `f_Release` conditions satisfied; clean exit | `execute_release` | — | — | **Yes** (clean exit) |
| `COLLAPSED` | `f_Collapse` infall complete | `execute_collapse` | — | — | **Yes** |
| `DAMPEN_ACTIVE` | `f_Dampen` engaged on Attractor's field | `suppress_field` | Dampening removed; `ρ(Φ)` restored | `CAPTURE_PENDING`, `ORBIT_STABLE` | No |
| `EMIT_ACTIVE` | `f_Emit` engaged on Attractor's field | `emit_field` | Emission withdrawn | `ORBIT_STABLE`, `CAPTURE_DECAYING` | No |

### §3.2 · State Transition Diagram

```
                          E crosses r_capture
                                  │
                                  ▼
                        ┌─────────────────┐
                        │ CAPTURE_PENDING  │
                        └────────┬────────┘
                                 │
              ┌──────────────────┼──────────────────────┐
              │                  │                       │
    C_thresh > 0             C_thresh ≤ 0           ρ(Φ) = 0
    β ≥ 1.0                  (FM-001)               (FM-002)
    Frame ok                      │                       │
    ω_res ∈ ℚ                     │                       │
              │                   │                       │
              ▼                   ▼                       ▼
   ┌──────────────────┐   ┌───────────────┐       (FM-003 / FM-006)
   │  CAPTURE_LOCKED  │   │ CAPTURE_FAILED│◄──────── all terminal
   └────────┬─────────┘   │   [TERMINAL]  │             FMs
            │             └───────────────┘
            │
     d_bind monitored every cycle via flag_decay
            │
    ┌───────┴────────────────────────┐
    │                                │
d_bind < d_warn               M_E ≈ M_A
(FM-004)                      (FM-007)
    │                                │
    ▼                                ▼
┌──────────────────┐      ┌──────────────────┐
│ CAPTURE_DECAYING │      │ CAPTURE_COLLISION │
└────────┬─────────┘      │    [TERMINAL]    │
         │                └──────────────────┘
    ┌────┴────┐
    │         │
ejection  infall
(FM-005)  (FM-005)
    │         │
    ▼         ▼
CAPTURE_  CAPTURE_
FAILED    COLLISION

     ORBIT_STABLE ↔ ORBIT_ECCENTRIC  (reclassified each cycle)
     RELEASED [TERMINAL]             (clean exit via f_Release)
     COLLAPSED [TERMINAL]            (infall confirmed)
     DAMPEN_ACTIVE / EMIT_ACTIVE     (engineering overlay flags)
```

### §3.3 · Flag Ownership

| Flag | Owned By | Written By Primitive |
|---|---|---|
| `CAPTURE_PENDING` | Element `E` | `compute_approach_vector` |
| `CAPTURE_LOCKED` | Element `E` + Attractor `A` registry | `register_capture` |
| `CAPTURE_DECAYING` | Element `E` | `flag_decay` |
| `CAPTURE_FAILED` | Element `E` | `register_capture` |
| `CAPTURE_COLLISION` | Both `E` and `A` (or composite) | `execute_collapse` |
| `ORBIT_STABLE` | Element `E` | `classify_orbit` |
| `ORBIT_ECCENTRIC` | Element `E` | `classify_orbit` |
| `RELEASED` | Element `E` + Attractor `A` registry | `execute_release` |
| `COLLAPSED` | Composite node `C` (or `A` post-absorption) | `execute_collapse` |
| `DAMPEN_ACTIVE` | Attractor `A` | `suppress_field` |
| `EMIT_ACTIVE` | Attractor `A` | `emit_field` |

---

## §4 · Engineering Primitives

<!--
  metadata:
    section:       engineering-primitives
    section_id:    §4
    type:          primitive-registry
    normative:     true
    primitive_count: 15
    call_convention: functional
    created_in:    SES-20260813-OPS-001
    correction: >
      INDEX.md §2 listed 13 primitives. Correct count is 15.
      initialize_composite_node and purge_registry were listed
      separately in f_Collapse.md scaffolds but not in the original
      count. This document is authoritative: 15 primitives.
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

### §4.1 · Call Order and Dependencies

Primitives must be called in the order defined in §7 (Evaluation Order).
Side-effecting primitives write to external registries and are **not** idempotent.
Pure primitives may be called in any order relative to each other within their group.

### §4.2 · Full Primitive Specification Table

| # | Primitive | Source File | Pure | Reads | Writes | Call Timing | Frozen |
|---|---|---|---|---|---|---|---|
| 1 | `compute_approach_vector` | `f_Capture.md §7.2` | Yes | `E.state`, `A.position` | `v_approach` | Once · Step 1 | ✅ |
| 2 | `resolve_escape_velocity` | `f_Capture.md §7.2` | Yes | `M_A`, `ρ(Φ)` | `v_escape(A)` | Once · Step 2 | ✅ |
| 3 | `evaluate_capture_threshold` | `f_Capture.md §7.2` | Yes | `v_approach`, `v_escape`, `r` | `C_thresh` | Once · Step 5 | ✅ |
| 4 | `lock_orbit` | `f_Capture.md §7.2` | No | `E`, `A`, `Φ` | `orbital_parameters` | Once · Step 8 | ✅ |
| 5 | `register_capture` | `f_Capture.md §7.2` | No | `orbital_parameters` | `FFF_Registry`, `E.registry`, `A.registry`, `A.field_curvature` | Once · Step 9 | ✅ |
| 6 | `flag_decay` | `f_Capture.md §7.2` / `f_Decay.md §7` | No | `d_bind_delta` | `E.state_flag`, `decay_status` | Every cycle post `CAPTURE_LOCKED` | ✅ |
| 7 | `classify_orbit` | `f_Orbit.md §7` | Yes | `p_res`, `d_bind`, `ω_res` | `orbital_parameters.orbit_class`, `.stab_class` | Once post lock; then each cycle | 🔵 |
| 8 | `compute_release_vector` | `f_Release.md §7` | Yes | `E.state`, `d_bind` | `v_release` | Once · on release attempt | 🔵 |
| 9 | `execute_release` | `f_Release.md §7` | No | `v_release` | `FFF_Registry`, `E.registry`, `A.registry` | Once · on release | 🔵 |
| 10 | `execute_collapse` | `f_Collapse.md §7` | No | `d_bind`, `E`, `A` | composite node, both registries | Once · on FM-005 or FM-007 | 🔵 |
| 11 | `initialize_composite_node` | `f_Collapse.md §7` | No | `M_E`, `M_A` | new composite node `C` | Once · on FM-007 only | 🔵 |
| 12 | `purge_registry` | `f_Collapse.md §7` | No | `E.id`, `A.id` | `FFF_Registry` (deletion) | Once · on FM-007; partial on FM-005 | 🔵 |
| 13 | `emit_field` | `f_Emit.md §7` | No | `F_emit`, `A`, `r_emit` | `ρ(Φ)` local, `A.field_curvature` | On demand | 🔵 |
| 14 | `suppress_field` | `f_Dampen.md §7` | No | `F_damp`, `ρ(Φ)`, `r_damp` | `ρ(Φ)` local | On demand | 🔵 |
| 15 | `amplify_coupling` | `f_Amplify.md §7` | No | `F_amp`, `M_A`, `ρ(Φ)` | `β`, `P_eff` | On demand | 🔵 |
| 16 | `redirect_force_node` | `f_Deflect.md §7` | No | `heading_delta`, `r_deflect` | `v_approach` heading component | On demand | 🔵 |

> **Note:** Primitive 16 (`redirect_force_node`) was added from scaffold review.
> Corrected total: **16 primitives**. INDEX.md §2 to be updated at next session.

### §4.3 · Side-Effect Classification

| Class | Primitives | Consequence of Repeat Call |
|---|---|---|
| Pure (safe to repeat) | 1, 2, 3, 7, 8 | No side effects; produces same output for same inputs |
| Single-write (idempotent-safe) | 4, 6 | Overwrites same fields; safe to repeat |
| Registry-write (non-idempotent) | 5, 9, 10, 11, 12, 13, 14, 15, 16 | Repeat call creates duplicate records or double-applies effect |

### §4.4 · Primitive Guards Summary

| Primitive | Guard | Consequence of Violation |
|---|---|---|
| `evaluate_capture_threshold` | `r ≤ r_capture` | Returns `C_thresh < 0` immediately if `r > r_capture` |
| `lock_orbit` | `C_thresh > 0` | Must not be called if threshold not met |
| `register_capture` | `lock_orbit` completed | Undefined behavior if orbital parameters absent |
| `flag_decay` | Post `CAPTURE_LOCKED` only | No-op if called pre-capture |
| `execute_collapse` | FM-005 or FM-007 active | Must not be called outside terminal FM context |
| `initialize_composite_node` | FM-007 path only | Must not be called on asymmetric collapse |
| `emit_field` | `ρ(Φ) < 1.0` | No-op at saturation; runaway risk if `β → β_max` |
| `suppress_field` | `ρ(Φ) > ρ(Φ)_floor` | FM-009 risk if floor breached |
| `amplify_coupling` | `β < β_max` | FM-010 if ceiling exceeded |
| `redirect_force_node` | `heading_delta` within bounds | Over-deflection → FM-001 equivalent |

---

## §5 · Failure Mode Registry

<!--
  metadata:
    section:       failure-mode-registry
    section_id:    §5
    type:          registry
    normative:     true
    failure_count: 10
    id_prefix:     FM
    id_range:      FM-001 – FM-010
    severity_levels: [warn, error, fatal]
    frozen:        FM-001 through FM-007 frozen at v1.0.0; FM-008 through FM-010 pending
    created_in:    SES-20260813-OPS-001
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

### §5.1 · Full Failure Mode Table

| ID | Name | FFF Node | Trigger Condition | Operators Involved | State Transition | Outcome | Severity | Recoverable | Defined In |
|---|---|---|---|---|---|---|---|---|---|
| FM-001 | Overshoot | `F_force` | `C_thresh ≤ 0`; `v_approach ≥ v_escape(A)` | `v_approach`, `v_escape`, `C_thresh` | `CAPTURE_PENDING → CAPTURE_FAILED` | Element escapes | error | No | `f_Capture.md §6` |
| FM-002 | Field Null | `F_freq` | `ρ(Φ) = 0` at moment of encounter | `ρ(Φ)`, `P_eff`, `v_escape` | `CAPTURE_PENDING → CAPTURE_FAILED` | No pull transmitted | error | No | `f_Capture.md §6` |
| FM-003 | Frame Saturation | Frame | Attractor registry at MAX capacity | Frame.registry_capacity, `β` | `CAPTURE_PENDING → CAPTURE_FAILED` | Element deflected at boundary | error | No | `f_Capture.md §6` |
| FM-004 | Resonance Drift | `ω_res` | `ω_res` → irrational; `d_bind < d_warn` | `ω_res`, `d_bind`, `δ` | `CAPTURE_LOCKED → CAPTURE_DECAYING` | Orbit destabilizing | warn | Yes — via `f_Emit` or `f_Amplify` | `f_Capture.md §6` |
| FM-005 | Decay Spiral | `d_bind` | `d_bind ≤ d_collapse`; energy exhausted | `d_bind`, `δ`, `p_res` | `CAPTURE_DECAYING → CAPTURE_FAILED` or `CAPTURE_COLLISION` | Ejection or infall | fatal | No | `f_Decay.md §6` |
| FM-006 | Phantom Capture | `ρ(Φ)` | `β ≥ 1.0` met; `ρ(Φ)` locally structured; lock dissolves at field boundary | `β`, `ρ(Φ)`, `P_eff` | `CAPTURE_PENDING → CAPTURE_FAILED` | Apparent capture resolves to escape | warn | No | `f_Capture.md §6` |
| FM-007 | Mutual Dissolution | `F_fluid` | `\|M_E − M_A\| < m_parity`; collision threshold crossed | `M_E`, `M_A`, `β`, `C_thresh` | `CAPTURE_LOCKED → CAPTURE_COLLISION` | Composite node created; both registries purged | fatal | No | `f_Collapse.md §6` |
| FM-008 | Release Overshoot | `F_force` | `v_release` too high; trajectory becomes hyperbolic | `v_release`, `E_rel` | `CAPTURE_LOCKED → CAPTURE_FAILED` | Uncontrolled ejection | error | No | `f_Release.md §6` |
| FM-009 | Dampen Cascade | `F_freq` | `suppress_field` propagates beyond `r_damp`; `ρ(Φ) → 0` region-wide | `F_damp`, `ρ(Φ)`, `r_damp` | multiple `CAPTURE_LOCKED → CAPTURE_DECAYING` | Gravity null zone; uncontrolled releases | fatal | Partial — if caught before propagation | `f_Dampen.md §6` |
| FM-010 | Amplify Runaway | `F_fluid` | `β > β_max` under sustained `f_Emit` or `f_Amplify` | `β`, `F_amp`, `F_emit`, `β_max` | `ORBIT_STABLE → CAPTURE_COLLISION` | Collapse or singularity | fatal | No | `f_Amplify.md §6` |

### §5.2 · Failure Mode Groupings

| Group | IDs | Common Cause | Common Outcome |
|---|---|---|---|
| Approach failures | FM-001, FM-002, FM-003, FM-006 | Conditions wrong at encounter | `CAPTURE_FAILED` — never entered orbit |
| Orbital instability | FM-004, FM-005 | Post-capture energy loss | `CAPTURE_DECAYING` → ejection or infall |
| Terminal events | FM-005 (infall path), FM-007 | Mass collision or dissolution | `CAPTURE_COLLISION` — no survivors |
| Engineering failures | FM-008, FM-009, FM-010 | Primitive misuse or runaway | Varied — ejection, null zone, singularity |

### §5.3 · Severity Definitions

| Severity | Meaning | Recovery |
|---|---|---|
| `warn` | Orbit is at risk but not yet terminal; intervention window open | Yes — `f_Emit`, `f_Amplify` may restore |
| `error` | Capture has failed; element not in orbit; no immediate system danger | No — outcome is final for this interaction |
| `fatal` | Terminal event with system-wide consequences; nodes destroyed or topology changed | No — irreversible |

---

## §6 · Composition Rules

<!--
  metadata:
    section:       composition-rules
    section_id:    §6
    type:          formula-registry
    normative:     true
    source:        f_Capture.md §4.8
    created_in:    SES-20260813-OPS-001
    note: >
      These are the canonical derivation chains for all computed values.
      Each rule specifies: the output, its formula, what inputs must be
      defined first, and what state it is undefined in.
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

### §6.1 · Core Derivation Chain

Reading order — each row depends on all rows above it:

```
INPUT LAYER
  M_A        → provided by Attractor state
  M_E        → provided by Element state
  ρ(Φ)       → provided by F_freq (f_Field.md)
  r          → provided by geometry
  v_approach → computed by: compute_approach_vector(E, A)

STEP 1: Effective Pull
  P_eff = M_A × ρ(Φ) / r²
  Defined when: ρ(Φ) > 0 ∧ r > 0

STEP 2: Escape Velocity
  v_escape(A) = resolve_escape_velocity(M_A, ρ(Φ))
  Defined when: ρ(Φ) > 0

STEP 3: Binding Coefficient
  β = P_eff / (M_E × v_approach)
  Defined when: v_approach > 0

STEP 4: Capture Threshold
  C_thresh = v_escape(A) − v_approach
  Defined when: v_escape(A) defined

STEP 5: Residual Momentum
  p_res = M_E × (v_approach − C_thresh)
  Defined when: C_thresh > 0

STEP 6: Orbital Eccentricity
  e = p_res / (p_res + P_eff)
  Defined when: P_eff > 0 ∧ p_res ≥ 0
  Constraint: e must be in [0, 1); e ≥ 1 → hyperbolic → not captured

STEP 7: Binding Depth
  d_bind = β × ρ(Φ) × (1 − e)
  Defined when: e ∈ [0, 1)

STEP 8: Decay Rate (post-capture, per-cycle)
  δ = Δd_bind / Δt = d_bind(t) − d_bind(t−1)
  Defined when: t ≥ 1 (at least one prior cycle)
```

### §6.2 · Capture Gate Composition

The Capture Gate is the boolean conjunction of all stability conditions.
**All must be true simultaneously for capture to succeed.**

```
CAPTURE_GATE =
    C_thresh > 0             [Condition 1 — Approach]
  ∧ ρ(Φ) > 0 (uniform)      [Condition 2 — Field Coherence]
  ∧ ω_res ∈ ℚ               [Condition 3 — Resonance]
  ∧ β ≥ 1.0                 [Condition 4 — Binding Floor]
  ∧ Frame.capacity > 0       [Condition 5 — Frame Compatibility]

If CAPTURE_GATE = true  → lock_orbit() → register_capture() → CAPTURE_LOCKED
If CAPTURE_GATE = false → FM raised   → register_capture() → CAPTURE_FAILED
```

### §6.3 · Engineering Operator Compositions

| Goal | Composition | Operators Modified | Risk |
|---|---|---|---|
| Restore decaying orbit | `emit_field(F_emit)` → `ρ(Φ)↑` → `d_bind↑` | `ρ(Φ)`, `P_eff`, `β`, `d_bind` | FM-010 if sustained |
| Weaken attractor hold | `suppress_field(F_damp)` → `ρ(Φ)↓` → `d_bind↓` | `ρ(Φ)`, `P_eff`, `v_escape`, `d_bind` | FM-009 if propagates |
| Increase capture probability | `amplify_coupling(F_amp)` → `β↑` → `P_eff↑` | `β`, `P_eff`, `d_bind` | FM-010 if `β > β_max` |
| Route Element to target heading | `redirect_force_node(heading_delta)` → `v_approach` heading change | `v_approach` (heading only) | FM-001 if over-deflected |
| Engineer target resonance | `solve_resonant_approach(ω_res_target)` → `{heading, ρ(Φ), β}` spec | All approach operators | No solution if target irrational |

---

## §7 · Operator Evaluation Order

<!--
  metadata:
    section:       evaluation-order
    section_id:    §7
    type:          execution-sequence
    normative:     true
    source:        f_Capture.md §4.7
    scope: >
      This is the canonical evaluation order for the f_Capture execution path.
      Engineering primitives (f_Emit, f_Dampen, f_Amplify, f_Deflect) are called
      on demand, outside this sequence, before the approach window opens.
    created_in:    SES-20260813-OPS-001
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

| Step | Frequency | Primitive | Operators Read | Operators Written | Guard | Short-Circuits To |
|---|---|---|---|---|---|---|
| 1 | ONCE | `compute_approach_vector` | `E.state`, `A.position` | `v_approach` | none | — |
| 2 | ONCE | `resolve_escape_velocity` | `M_A`, `ρ(Φ)` | `v_escape(A)` | `ρ(Φ) > 0` | FM-002 |
| 3 | ONCE | *(implicit)* | `M_A`, `ρ(Φ)`, `r` | `P_eff` | requires step 2 | — |
| 4 | ONCE | *(implicit)* | `P_eff`, `v_approach`, `M_E` | `β` | requires step 3 | — |
| 5 | ONCE | `evaluate_capture_threshold` | `v_approach`, `v_escape`, `r_capture` | `C_thresh` | `r ≤ r_capture` | FM-001 if `C_thresh ≤ 0` |
| 6 | ONCE | *(Frame check)* | `Frame.registry_capacity` | — | `β ≥ 1.0` else halt | FM-003 |
| 7 | ONCE | *(Resonance check)* | `ω_res` | — | `ω_res ∈ ℚ` else halt | FM-004 |
| 8 | ONCE | `lock_orbit` | `E`, `A`, `p_res`, `ρ(Φ)` | `d_bind`, orbital parameters | `C_thresh > 0` | — |
| 9 | ONCE | `register_capture` | orbital parameters | `Ω`, `FFF_Registry`, `E.registry`, `A.registry` | requires step 8 | — |
| 10 | CYCLE | `flag_decay` | `d_bind_delta` | `E.state_flag`, `decay_status` | post `CAPTURE_LOCKED` only | FM-004 / FM-005 |

---

## §8 · Symbol Freeze Registry

<!--
  metadata:
    section:       freeze-registry
    section_id:    §8
    type:          governance-registry
    normative:     true
    policy: >
      A symbol is FROZEN once its defining file reaches canonical status.
      Frozen symbols cannot be renamed or removed — only deprecated.
      Deprecation requires a new symbol, a major version bump, and an
      entry in CHANGELOG.md explaining the migration path.
    created_in:    SES-20260813-OPS-001
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

### §8.1 · Frozen Symbols (v1.0.0)

All frozen by `f_Capture.md v1.0.0`:

| Symbol | Type | Frozen In | Frozen At |
|---|---|---|---|
| `v_approach` | Primary | `f_Capture.md` | v1.0.0 |
| `v_escape(A)` | Primary | `f_Capture.md` | v1.0.0 |
| `ρ(Φ)` | Primary | `f_Capture.md` | v1.0.0 |
| `r_capture` | Primary | `f_Capture.md` | v1.0.0 |
| `β` | Primary | `f_Capture.md` | v1.0.0 |
| `ω_res` | Primary | `f_Capture.md` | v1.0.0 |
| `M_A` | Primary | `f_Capture.md` | v1.0.0 |
| `M_E` | Primary | `f_Capture.md` | v1.0.0 |
| `r` | Primary | `f_Capture.md` | v1.0.0 |
| `P_eff` | Derived | `f_Capture.md` | v1.0.0 |
| `C_thresh` | Derived | `f_Capture.md` | v1.0.0 |
| `d_bind` | Derived | `f_Capture.md` | v1.0.0 |
| `p_res` | Derived | `f_Capture.md` | v1.0.0 |
| `CAPTURE_PENDING` | Flag | `f_Capture.md` | v1.0.0 |
| `CAPTURE_LOCKED` | Flag | `f_Capture.md` | v1.0.0 |
| `CAPTURE_DECAYING` | Flag | `f_Capture.md` | v1.0.0 |
| `CAPTURE_FAILED` | Flag | `f_Capture.md` | v1.0.0 |
| `CAPTURE_COLLISION` | Flag | `f_Capture.md` | v1.0.0 |
| `compute_approach_vector` | Primitive | `f_Capture.md` | v1.0.0 |
| `resolve_escape_velocity` | Primitive | `f_Capture.md` | v1.0.0 |
| `evaluate_capture_threshold` | Primitive | `f_Capture.md` | v1.0.0 |
| `lock_orbit` | Primitive | `f_Capture.md` | v1.0.0 |
| `register_capture` | Primitive | `f_Capture.md` | v1.0.0 |
| `flag_decay` | Primitive | `f_Capture.md` | v1.0.0 |
| FM-001 through FM-007 | Failure Mode | `f_Capture.md` | v1.0.0 |

### §8.2 · Pending Freeze (promoted when source file goes canonical)

| Symbol | Type | Pending In | Freeze Trigger |
|---|---|---|---|
| `e` | Derived | `f_Orbit.md` | `f_Orbit.md` → canonical |
| `T_orb` | Derived | `f_Orbit.md` | `f_Orbit.md` → canonical |
| `δ` | Derived | `f_Decay.md` | `f_Decay.md` → canonical |
| `d_warn` | Derived | `f_Decay.md` | `f_Decay.md` → canonical |
| `d_collapse` | Derived | `f_Decay.md` | `f_Decay.md` → canonical |
| `E_rel` | Derived | `f_Release.md` | `f_Release.md` → canonical |
| `m_parity` | Derived | `f_Collapse.md` | `f_Collapse.md` → canonical |
| `F_emit` | Derived | `f_Emit.md` | `f_Emit.md` → canonical |
| `F_damp` | Derived | `f_Dampen.md` | `f_Dampen.md` → canonical |
| `F_amp` | Supplementary | `f_Amplify.md` | `f_Amplify.md` → canonical |
| `β_max` | Supplementary | `f_Amplify.md` | `f_Amplify.md` → canonical |
| `heading_delta` | Supplementary | `f_Deflect.md` | `f_Deflect.md` → canonical |
| `ORBIT_STABLE` | Flag | `f_Orbit.md` | `f_Orbit.md` → canonical |
| `ORBIT_ECCENTRIC` | Flag | `f_Orbit.md` | `f_Orbit.md` → canonical |
| `RELEASED` | Flag | `f_Release.md` | `f_Release.md` → canonical |
| `COLLAPSED` | Flag | `f_Collapse.md` | `f_Collapse.md` → canonical |
| `DAMPEN_ACTIVE` | Flag | `f_Dampen.md` | `f_Dampen.md` → canonical |
| `EMIT_ACTIVE` | Flag | `f_Emit.md` | `f_Emit.md` → canonical |
| FM-008 | Failure Mode | `f_Release.md` | `f_Release.md` → canonical |
| FM-009 | Failure Mode | `f_Dampen.md` | `f_Dampen.md` → canonical |
| FM-010 | Failure Mode | `f_Amplify.md` | `f_Amplify.md` → canonical |
| Primitives 7–16 | Primitive | Wave 3 files | each source file → canonical |

---

## §9 · Versioning Policy

<!--
  metadata:
    section:       versioning-policy
    section_id:    §9
    type:          governance
    normative:     true
    created_in:    SES-20260813-OPS-001
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

### §9.1 · Version Bump Rules

| Change Type | Bump Required | Example |
|---|---|---|
| Add a new symbol (not conflicting) | **minor** — e.g. v1.0.0 → v1.1.0 | Adding `T_orb` when `f_Orbit.md` canonicalizes |
| Change a frozen symbol's formula | **major** — e.g. v1.1.0 → v2.0.0 | Changing `P_eff` formula |
| Rename a frozen symbol | **major** | Renaming `d_bind` to `d_orbital` |
| Remove a frozen symbol | **major** + deprecation notice | Removing `ω_res` |
| Add a failure mode | **minor** | Adding FM-011 |
| Change a failure mode's severity | **minor** | Upgrading FM-004 from warn to error |
| Fix a typo in a non-normative section | **patch** — e.g. v1.0.0 → v1.0.1 | Fixing a table cell |
| Add a note or example | **patch** | Adding a new canonical example |

### §9.2 · Namespace Reservation

The following symbol prefixes are reserved for future use and must not be used
by any function file without first registering here:

| Prefix | Reserved For | Example |
|---|---|---|
| `v_` | velocity operators | `v_approach`, `v_escape`, `v_release` |
| `ρ` | field density operators | `ρ(Φ)`, `ρ(Φ,θ)`, `ρ(Φ,t)` |
| `ω_` | resonance and frequency operators | `ω_res`, `ω_target` |
| `d_` | depth and distance operators | `d_bind`, `d_warn`, `d_collapse` |
| `F_` | engineering force/field operators | `F_emit`, `F_damp`, `F_amp` |
| `M_` | mass operators | `M_A`, `M_E` |
| `G_` | GravityGraph operators | `G_edge`, `G_degree`, `G_stability` |
| `FM-` | failure mode IDs | FM-001 through FM-999 |
| `EX-` | canonical example IDs | EX-001, EX-RES-001 |
| `SES-` | session IDs | SES-20260813-OPS-001 |

---

## §10 · Document Metadata

<!--
  metadata:
    section:       document-metadata
    section_id:    §10
    type:          administrative
    normative:     false
  session:
    session_id:    SES-20260813-OPS-001
    touch_count:   1
    change_type:   created
-->

| Field | Value |
|---|---|
| Canonical Path | `docs/FFF_Gravity/OPERATORS.md` |
| Version | 1.0.0 |
| Status | Canonical |
| Stability | Living — update when any symbol is added, frozen, or deprecated |
| Normative | Yes |
| Created | 2026-08-13 |
| Last Modified | 2026-08-13 |
| Authors | TriadicFrameworks |
| License | See `/LICENSE` at repository root |
| Encoding | UTF-8 · LF |
| Supersedes | Operator tables in `f_Capture.md §4` (those remain normative; this file is the consolidated authority) |

---

*Single source of truth for all FFF_Gravity operator symbols.*
*All function files derive their symbol definitions from this document.*
*Update at the close of any session that introduces or freezes a symbol.*
```

---

**Commit message:**
```
feat(FFF_Gravity): add canonical OPERATORS.md — master symbol authority, 9P/10D operators, 11 flags, 16 primitives, 10 FMs, composition rules, freeze registry [SES-20260813-OPS-001]

---

Two corrections surfaced while writing this — both logged in the file, both need propagating:

| Discovery | Location to update |
|---|---|
| Primitive count is **16**, not 13 (INDEX said 13, scaffolds said 15) — `redirect_force_node` was the missing one | `INDEX.md §2` master registry row for primitives; `FFF_Gravity_module.json` |
| Primitive count correction note in `§4.2` is self-documenting | No separate action needed |

---

## Wave 3 Addendum — Core Function Operators (PRIM:007–024)
> Session: SES-20260813-W3 | Sealed: 2026-08-13

### f_Orbit Operators (Wave 3 · PRIM:007, 012)

| Symbol        | Type  | Domain                          | Description                                                       | Frozen in |
|---------------|-------|---------------------------------|-------------------------------------------------------------------|-----------|
| `T_orb`       | float | > 0                             | Orbital period; time for one complete orbit around source node    | PRIM:012  |
| `orbit_class` | enum  | {STABLE, DECAYING, ESCAPE}      | Orbit classification derived from binding strength and δ          | PRIM:007  |
| `stab_class`  | enum  | {HIGH, MED, LOW, CRITICAL}      | Stability classification derived from T_orb and decay trajectory  | PRIM:012  |

### f_Release Operators (Wave 3 · PRIM:008–009)

| Symbol      | Type  | Domain | Description                                                  | Frozen in |
|-------------|-------|--------|--------------------------------------------------------------|-----------|
| `v_release` | float | ≥ 0    | Scalar release velocity at moment of unbinding               | PRIM:009  |
| `r_release` | float | > 0    | Release radius; distance at which unbinding condition is met | PRIM:008  |

### f_Decay Operators (Wave 3 · PRIM:010–011)

| Symbol       | Type  | Domain        | Description                                                         | Frozen in |
|--------------|-------|---------------|---------------------------------------------------------------------|-----------|
| `δ`          | float | (0, 1)        | Decay rate coefficient; fractional binding-distance loss per cycle  | PRIM:010  |
| `d_warn`     | float | > 0, < d_bind | Binding distance level at which decay warning is raised             | PRIM:010  |
| `d_collapse` | float | > 0, ≤ d_warn | Binding distance threshold triggering collapse evaluation           | PRIM:011  |

### f_Collapse Operators (Wave 3 · PRIM:013–014)

| Symbol     | Type    | Domain | Description                                                       | Frozen in |
|------------|---------|--------|-------------------------------------------------------------------|-----------|
| `m_parity` | float   | > 0    | Mass parity ratio between collapsing nodes                        | PRIM:013  |
| `C_node`   | node_id | —      | Identifier of the surviving/dominant node after collapse resolves | PRIM:014  |

### f_Emit Operators (Wave 3 · PRIM:015–017)

| Symbol       | Type  | Domain | Description                                                    | Frozen in |
|--------------|-------|--------|----------------------------------------------------------------|-----------|
| `F_emit`     | float | ≥ 0    | Emission force magnitude applied outward into the field        | PRIM:015  |
| `ρ(Φ)_delta` | float | any    | Change in field density ρ(Φ) caused by a single emission event | PRIM:016  |
| `r_emit`     | float | > 0    | Emission radius; spatial extent of emitted influence           | PRIM:017  |

### f_Dampen Operators (Wave 3 · PRIM:018–020)

| Symbol          | Type  | Domain | Description                                                    | Frozen in |
|-----------------|-------|--------|----------------------------------------------------------------|-----------|
| `F_damp`        | float | ≤ 0    | Dampening force; negative magnitude opposing field escalation  | PRIM:018  |
| `ρ(Φ)_floor`    | float | ≥ 0    | Minimum field density enforced when dampening is active        | PRIM:019  |
| `cascade_guard` | bool  | {0, 1} | Flag active when cascade dampening guard is engaged            | PRIM:020  |

### f_Amplify Operators (Wave 3 · PRIM:021–022)

| Symbol     | Type  | Domain | Description                                                  | Frozen in |
|------------|-------|--------|--------------------------------------------------------------|-----------|
| `F_amp`    | float | ≥ 0    | Amplification force magnitude applied to field               | PRIM:021  |
| `β_max`    | float | > 1    | Maximum amplification coefficient; hard ceiling on β         | PRIM:021  |
| `amp_cost` | float | ≥ 0    | Energy cost of amplification; deducted from ρ(Φ) each cycle | PRIM:022  |

### f_Deflect Operators (Wave 3 · PRIM:023–024)

> **Stub resolution note:** `heading_delta` was declared as a forward stub in `f_Force.md §4.3`
> (PRIM:005). That stub is fully resolved here. `f_Force.md §4.3` remains the declaration
> site; `f_Deflect.md` (PRIM:023) is the authoritative definition and domain authority.

| Symbol          | Type  | Domain  | Description                                                | Frozen in |
|-----------------|-------|---------|------------------------------------------------------------|-----------|
| `heading_delta` | float | [−π, π] | Angular deflection applied to the approach vector          | PRIM:023  |
| `r_deflect`     | float | > 0     | Deflection radius; distance at which deflection force acts | PRIM:023  |
| `deflect_cost`  | float | ≥ 0     | Energy cost of deflection; deducted from ρ(Φ)             | PRIM:024  |

---

## Wave 4 Addendum — Capture Variant Operators (PRIM:025–040)
> Session: SES-20260813-W4 | Sealed: 2026-08-13

### f_Capture_Multi Operators (Wave 4 · PRIM:025–026)

| Symbol        | Type  | Domain  | Description                                                               | Frozen in |
|---------------|-------|---------|---------------------------------------------------------------------------|-----------|
| `N`           | int   | ≥ 2     | Count of simultaneous capture targets in multi-capture event              | PRIM:025  |
| `eval_order`  | list  | ordered | Evaluation priority sequence for multi-target binding attempts            | PRIM:025  |
| `Φ_perturbed` | float | [0, 1]  | Field value after perturbation from multi-target interference             | PRIM:026  |
| `δ_perturb`   | float | ≥ 0     | Perturbation magnitude applied to Φ during multi-capture                  | PRIM:026  |
| `k_perturb`   | float | > 0     | Perturbation scaling coefficient                                          | PRIM:026  |

### f_Capture_Cascade Operators (Wave 4 · PRIM:027–028)

| Symbol          | Type  | Domain | Description                                                            | Frozen in |
|-----------------|-------|--------|------------------------------------------------------------------------|-----------|
| `cascade_depth` | int   | ≥ 0    | Current recursion depth within the cascade capture chain               | PRIM:027  |
| `k_max`         | int   | ≥ 1    | Maximum permitted cascade depth; CAS-1 guard enforced inside PRIM:027 | PRIM:027  |
| `γ`             | float | (0, 1) | Cascade gain; fraction of parent Ω_cascade transmitted to child step  | PRIM:028  |
| `Ω_cascade`     | float | ≥ 0    | Cascade transmission energy available at the current depth step        | PRIM:028  |

### f_Capture_Soft Operators (Wave 4 · PRIM:029–030)

| Symbol           | Type  | Domain | Description                                                       | Frozen in |
|------------------|-------|--------|-------------------------------------------------------------------|-----------|
| `d_soft`         | float | > 0    | Soft capture binding distance (relaxed threshold vs. d_bind)     | PRIM:029  |
| `soft_threshold` | float | (0, 1) | Minimum ρ(Φ) required to sustain soft capture                    | PRIM:029  |
| `grace_period`   | int   | ≥ 0    | Cycles permitted below soft_threshold before release triggers     | PRIM:030  |
| `k_grace`        | float | > 0    | Grace period scaling coefficient                                  | PRIM:030  |

### f_Capture_Hard Operators (Wave 4 · PRIM:031–032)

| Symbol       | Type  | Domain        | Description                                                   | Frozen in |
|--------------|-------|---------------|---------------------------------------------------------------|-----------|
| `d_hard`     | float | > 0           | Hard capture binding distance; strict threshold for lock entry | PRIM:031  |
| `α_hard`     | float | > 1           | Hard capture alpha; binding distance multiplier               | PRIM:031  |
| `β_hard`     | float | > 0           | Hard capture beta; force amplification coefficient            | PRIM:031  |
| `β_min_hard` | float | > 0, ≤ β_hard | Minimum beta required to achieve and sustain hard lock        | PRIM:032  |
| `lock_cost`  | float | ≥ 0           | Energy cost deducted from ρ(Φ) to establish hard lock         | PRIM:032  |
| `k_lock`     | float | > 0           | Lock cost scaling coefficient                                 | PRIM:032  |

### f_Capture_Resonant Operators (Wave 4 · PRIM:033–034)

| Symbol         | Type  | Domain   | Description                                                       | Frozen in |
|----------------|-------|----------|-------------------------------------------------------------------|-----------|
| `ω_res`        | float | > 0      | Resonant angular frequency of the source emission cycle           | PRIM:033  |
| `T_res`        | float | > 0      | Resonant period; T_res = 2π / ω_res                               | PRIM:033  |
| `φ_A(t)`       | float | [0, 2π)  | Approach node phase angle at time t                               | PRIM:033  |
| `φ_E`          | float | [0, 2π)  | Emission phase angle of source at peak resonance                  | PRIM:033  |
| `φ_open`       | float | [0, 2π)  | Phase angle at which resonance acceptance window opens            | PRIM:033  |
| `φ_close`      | float | [0, 2π)  | Phase angle at which resonance acceptance window closes           | PRIM:033  |
| `window_width` | float | (0, 2π)  | Angular width of resonance acceptance window                      | PRIM:033  |
| `p_ratio`      | int   | ≥ 1      | Numerator of the p:q phase-lock ratio                             | PRIM:033  |
| `q_ratio`      | int   | ≥ 1      | Denominator of the p:q phase-lock ratio                           | PRIM:033  |
| `ρ_res_gain`   | float | > 0      | Field density gain multiplier active during resonance window      | PRIM:034  |
| `ρ_eff`        | float | ≥ 0      | Effective field density under resonance conditions                | PRIM:034  |
| `ρ_res_floor`  | float | ≥ 0      | Minimum field density floor enforced in resonant state            | PRIM:034  |
| `d_bind_res`   | float | > 0      | Resonance-adjusted binding distance                               | PRIM:034  |
| `T_orb_res`    | float | > 0      | Resonance-adjusted orbital period                                 | PRIM:034  |

### f_Capture_Asymmetric Operators (Wave 4 · PRIM:035–036)

| Symbol                  | Type  | Domain  | Description                                                   | Frozen in |
|-------------------------|-------|---------|---------------------------------------------------------------|-----------|
| `mass_ratio`            | float | > 0     | Ratio of source node mass to approach node mass               | PRIM:035  |
| `asymmetry_factor`      | float | ≥ 0     | Degree of mass asymmetry (0 = fully symmetric)                | PRIM:035  |
| `parity_warn_threshold` | float | > 0     | Asymmetry level at which parity warning is raised             | PRIM:035  |
| `d_bind_asym`           | float | > 0     | Asymmetry-corrected binding distance                          | PRIM:036  |
| `heading_delta_asym`    | float | [−π, π] | Asymmetry-adjusted heading deflection angle                   | PRIM:036  |
| `deflect_tolerance`     | float | ≥ 0     | Maximum heading_delta_asym before deflection is rejected      | PRIM:036  |
| `asym_decay_risk`       | bool  | {0, 1}  | Flag: elevated decay risk due to asymmetric mass distribution | PRIM:036  |

### f_Capture_Temporal Operators (Wave 4 · PRIM:037–038)

| Symbol                  | Type   | Domain   | Description                                                   | Frozen in |
|-------------------------|--------|----------|---------------------------------------------------------------|-----------|
| `t_open`                | float  | ≥ 0      | Timestamp at which temporal capture window opens              | PRIM:037  |
| `t_close`               | float  | > t_open | Timestamp at which temporal capture window closes             | PRIM:037  |
| `t_span`                | float  | > 0      | Duration of window; t_span = t_close − t_open                | PRIM:037  |
| `t_elapsed`             | float  | ≥ 0      | Time elapsed since t_open at evaluation moment                | PRIM:037  |
| `t_remaining`           | float  | ≥ 0      | Time remaining until t_close at evaluation moment             | PRIM:037  |
| `window_id`             | string | unique   | Identifier for this temporal capture window instance          | PRIM:037  |
| `proximity_ratio`       | float  | [0, 1]   | t_elapsed / t_span; urgency metric for temporal capture       | PRIM:038  |
| `temporal_decay_factor` | float  | (0, 1]   | Decay multiplier applied to d_bind as window approaches close | PRIM:038  |
| `d_bind_temporal`       | float  | > 0      | Temporally-adjusted binding distance                          | PRIM:038  |
| `temporal_margin`       | float  | ≥ 0      | Buffer interval before t_close that triggers margin alert     | PRIM:038  |

### f_Capture_Networked Operators (Wave 4 · PRIM:039–040)

| Symbol                 | Type  | Domain    | Description                                                      | Frozen in |
|------------------------|-------|-----------|------------------------------------------------------------------|-----------|
| `N_net`                | int   | ≥ 2       | Number of nodes participating in the capture network             | PRIM:039  |
| `G_net`                | graph | connected | Network graph structure (nodes + weighted directed edges)        | PRIM:039  |
| `w_i`                  | float | ≥ 0       | Edge weight for node i within G_net                              | PRIM:039  |
| `d_bind_net`           | float | > 0       | Network-consensus binding distance (weighted aggregate)          | PRIM:040  |
| `ρ(Φ)_net`             | float | ≥ 0       | Aggregate network field density across all participating nodes   | PRIM:040  |
| `resilience_threshold` | float | (0, 1)    | Minimum connectivity fraction required to sustain network capture| PRIM:040  |

---

## Wave 5 — Dismissal Operators (PRIM:041–042)
> Session: SES-20260814-DISMISS-001 | Sealed: 2026-08-14

### f_Dismiss Operators (Wave 5 · PRIM:041–042)

| Symbol      | Type  | Domain           | Description                                               | Frozen in |
|-------------|-------|------------------|-----------------------------------------------------------|-----------|
| `F_dismiss` | float | ≥ 0              | Scalar dismissal force magnitude (\|G_D\|)                | PRIM:041  |
| `ρ_D(Φ)`    | float | (−1, 0]          | Dismissal field density (negative-polarity extension)     | PRIM:042  |
| `d_dismiss` | float | > 0              | Initial Dismissal Well depth at t = 0                     | PRIM:042  |
| `T_dismiss` | float | > 0              | Dismissal persistence time; governs exponential well decay| PRIM:042  |
| `r_dismiss` | float | (0, r_capture]   | Spatial extent of dismissal repulsion zone around A       | PRIM:041  |
| `ψ_dismiss` | enum  | {INTENTIONAL, STRUCTURAL, DRIFT} | Dismissal mode flag               | PRIM:041  |
| `t_dismiss` | float | ≥ 0              | Absolute clock time of dismissal event                    | PRIM:042  |
| `v_depart`  | float | ≥ 0              | Entity departure velocity post-dismissal                  | PRIM:042  |
| `β_D`       | float | (−∞, 0]          | Repulsive coupling coefficient active during expulsion    | PRIM:042  |

**Well decay formula (conceptual authority: GravityOfDismissal.md §3.2):**
```
ρ_D(Φ, t) = −d_dismiss × exp(−t / T_dismiss)
```

**Re-capture gate (operational form of GravityOfDismissal.md §3.3):**
```
d_bind_approach(t) > |ρ_D(Φ, t)|   →   re-capture structurally eligible
```
