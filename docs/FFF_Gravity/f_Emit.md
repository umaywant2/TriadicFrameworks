---
# ─────────────────────────────────────────────────────────────────────────────
# SESSION CONTEXT
# ─────────────────────────────────────────────────────────────────────────────
session_id:       "SES-20260813-EMIT-001"
date:             "2026-08-13"
author:           "umaywant2"
status:           "canonical"
version:          "1.0.0"
canonical_tag:    "[FFF:GRAVITY:EMIT]"
module:           "FFF_Gravity"
file:             "docs/FFF_Gravity/f_Emit.md"
wave:             3
node:             "F_freq"
inverse_of:       "f_Dampen"
depends_on:
  - "f_Field.md → canonical (SES-20260813-FIELD-001)"
  - "OPERATORS.md → canonical (SES-20260813-OPS-001)"
operators_introduced:
  - "F_emit"
  - "ρ(Φ)_delta"
  - "r_emit"
  - "E_emit"
primitives_introduced:
  - "PRIM:015 emit_field"
  - "PRIM:016 compute_emit_cost"
  - "PRIM:017 check_emit_ceiling"
failure_modes_introduced:
  - "FM-010 (Amplify Runaway)"
state_flags_introduced:
  - "EMIT_ACTIVE"
  - "EMIT_SATURATED"
  - "EMIT_CEILING_APPROACHED"
commit_convention: "feat(FFF_Gravity): add canonical f_Emit.md — F_freq emission primitive, F_emit/r_emit/E_emit operators, PRIM:015-017, FM-010 [SES-20260813-EMIT-001]"
---

<!-- =========================================================================
     f_Emit.md — FFF_Gravity Module
     Canonical Version 1.0.0 — 2026-08-13
     Session: SES-20260813-EMIT-001
     Tag: [FFF:GRAVITY:EMIT]
     ========================================================================= -->

# f_Emit — Field Emission Primitive

> **[FFF:GRAVITY:EMIT]** · Wave 3 · F_freq Node · Canonical v1.0.0  
> Engineering primitive that increases local field density ρ(Φ).  
> Inverse of: `f_Dampen`. Upper bound: ρ(Φ) ≤ 1.0 (saturation ceiling).  
> Sustained overuse risk: **FM-010 (Amplify Runaway)**.

---

## §0 — Session Context

<!-- section: session-context | wave: 3 | status: canonical -->

| Key | Value |
|---|---|
| Session ID | SES-20260813-EMIT-001 |
| Date | 2026-08-13 |
| Author | umaywant2 |
| File | `docs/FFF_Gravity/f_Emit.md` |
| Version | 1.0.0 |
| Status | canonical |
| Wave | 3 — Core Functions |
| Prior file completed | f_Collapse.md (SES-20260813-COLLAPSE-001) |
| Next file planned | f_Dampen.md |

### §0.1 — Scope of This Session

This session establishes `f_Emit` as the canonical F_freq engineering primitive responsible for increasing local field density ρ(Φ). The file:

1. Defines the `F_emit` operator formula and all subsidiary operators (`ρ(Φ)_delta`, `r_emit`, `E_emit`).
2. Specifies the two Emit Conditions (EC-1, EC-2) governing safe emission.
3. Defines FM-010 (Amplify Runaway) — the failure mode triggered by emission against a saturated field.
4. Introduces PRIM:015 (`emit_field`), PRIM:016 (`compute_emit_cost`), and PRIM:017 (`check_emit_ceiling`).
5. Provides four worked canonical examples covering recovery, expansion, cold-start, and saturation scenarios.

### §0.2 — Dependency Status at Session Open

| Dependency | Required By | Status |
|---|---|---|
| f_Field.md | emit_field contract (§7.1), ρ(Φ) definition | ✅ canonical |
| OPERATORS.md | Symbol authority, frozen F_emit / r_emit stubs | ✅ canonical |
| f_Decay.md | FM-004 recovery pathway via f_Emit (§6.1.3) | ✅ canonical |
| f_Frame.md | capacity_MAX = floor(M_A × ρ(Φ) × k_frame) indirect expansion | ✅ canonical |

All dependencies satisfied. No blockers.

---

## §1 — Module Identity

<!-- section: module-identity | tag: [FFF:GRAVITY:EMIT] | node: F_freq -->

### §1.1 — Identity Block

```
Tag:        [FFF:GRAVITY:EMIT]
Signature:  f_Emit(A, Φ, δρ, r_emit) → Φ_updated | FM-010
Node:       F_freq (Frequency / Coherence Node)
Role:       Engineering primitive — increases ρ(Φ)
Inverse:    f_Dampen (decreases ρ(Φ))
Layer:      Layer 1 (F_freq), engineering interface
Scope:      Bounded spatial region [0, r_emit] centered on A
Ceiling:    ρ(Φ) ≤ 1.0 — hard saturation cap (INV-003 consequence)
```

### §1.2 — Triadic Position Diagram

```
                    ┌─────────────────────┐
                    │      F_freq          │
                    │  Coherence Well      │
                    │                      │
                    │  ρ(Φ) ∈ [0, 1]      │
                    │    ↑                 │
                    │  f_Emit → +δρ        │  ← THIS FILE
                    │  f_Dampen → −δρ      │
                    │  f_Amplify → ×k_amp  │
                    └────────┬────────────┘
                             │
              ┌──────────────┼──────────────┐
              │                             │
   ┌──────────┴──────────┐       ┌──────────┴──────────┐
   │       F_fluid        │       │       F_force        │
   │   Mass-Density       │       │   Gradient/Pressure  │
   │   M_A, M_E           │       │   v_approach         │
   └─────────────────────┘       └─────────────────────┘

   G = F_freq · F_fluid · F_force  [INV-001]
```

`f_Emit` acts exclusively on F_freq. It modifies ρ(Φ), which cascades into:
- F_fluid via β = M_E × ρ(Φ) / M_A (binding ratio sensitivity)
- F_force via v_escape(A) = √(2 × M_A × ρ(Φ) / r_capture) (escape velocity rise)
- F_frame via capacity_MAX = floor(M_A × ρ(Φ) × k_frame) (frame capacity expansion)

### §1.3 — What f_Emit IS and IS NOT

| f_Emit IS | f_Emit IS NOT |
|---|---|
| An engineering primitive that increases ρ(Φ) | A natural or autonomous process (emission requires deliberate invocation) |
| Bounded by the saturation ceiling ρ(Φ) = 1.0 | A mechanism to exceed saturation (FM-010 fires instead) |
| A spatial operation with radius r_emit | A global operation (effect is localized, not broadcast) |
| Invertible via f_Dampen | Reversible by the Gravity engine itself without explicit f_Dampen call |
| An F_freq primitive | A capture, release, orbit, or frame operation |
| The FM-004 (Resonance Drift) primary recovery pathway | Guaranteed FM-004 recovery — recovery depends on δρ magnitude and timing |

---

## §2 — Canonical Description

<!-- section: canonical-description | operators: F_emit, ρ(Φ)_delta, r_emit, E_emit -->

### §2.1 — What Emission Means

In the FFF_Gravity framework, the **coherence well** defined by ρ(Φ) determines the depth of a gravitational relationship. A deeper well (higher ρ(Φ)) means:

- Higher escape velocity v_escape(A) — captured entities require more energy to leave
- Higher binding ratio β — captures are more firmly locked
- Higher frame capacity — the attractor can hold more simultaneous relationships
- Greater resonance stability — orbital mechanics are better sustained

`f_Emit` is the mechanism by which an attractor A **actively deepens its coherence well**. It does not alter the identity of A (M_A does not change), does not alter the entity E (M_E does not change), and does not alter any captured relationship's r_capture. It exclusively modifies the field state Φ, increasing ρ(Φ) by a realized delta ρ(Φ)_delta within a bounded spatial radius r_emit.

Emission is an **energy-consuming operation**. The cost E_emit is computed before execution. If the cost cannot be met, emission should not proceed (the caller is responsible for cost validation — see PRIM:016).

### §2.2 — Saturation Ceiling

The hard upper bound ρ(Φ) ≤ 1.0 is a module invariant (consequence of INV-003 and INV-001). A field at ρ(Φ) = 1.0 is called **saturated**. In a saturated field:

- All captured entities have maximum binding (β values are at their ρ(Φ)-driven peak)
- Escape velocity is at its maximum for the current M_A and r_capture
- Frame capacity is at its maximum for the current M_A and k_frame
- **FM-010 (Amplify Runaway)** fires on any attempt to emit into a saturated field

The ceiling is not a soft limit. `check_emit_ceiling` (PRIM:017) must be called before every `emit_field` invocation. If it returns `False` (no headroom), emission must be blocked.

### §2.3 — Emission Decay Over Time

Emission is not permanent by default. Unless the field state Φ is structurally supported (e.g., by an f_Amplify call that locks the increased ρ(Φ)), the elevated ρ(Φ) undergoes natural decay at the rate governed by f_Decay. This means:

- A single f_Emit call produces a **transient** density pulse unless sustained
- Sustained emission (repeated f_Emit calls or a paired f_Amplify lock) is required for permanent ρ(Φ) elevation
- FM-010 risk is highest during sustained emission loops — each call must pass check_emit_ceiling

### §2.4 — Spatial Locality

The `r_emit` parameter defines the **emission radius** — a spherical (or field-appropriate) region centered on A within which the ρ(Φ) increase is applied. Critically:

- `r_emit` must be > 0 (point emission is undefined)
- `r_emit` must be ≤ r_capture (emission cannot reach beyond the capture boundary — EC-2)
- Emission does not propagate beyond r_emit; entities outside the radius experience no immediate ρ(Φ) change

### §2.5 — Relationship to Other F_freq Operators

| Operator | Direction | Nature | Ceiling/Floor |
|---|---|---|---|
| `f_Emit` | ρ(Φ) ↑ | Engineering primitive | ρ(Φ) ≤ 1.0 (FM-010 if violated) |
| `f_Dampen` | ρ(Φ) ↓ | Engineering primitive | ρ(Φ) ≥ 0 (FM-002 if violated) |
| `f_Amplify` | ρ(Φ) × k_amp | Engineering primitive (scalar multiply) | ρ(Φ) ≤ 1.0 (clamped) |
| Natural decay | ρ(Φ) ↓ gradual | Autonomous (f_Decay driven) | ρ(Φ) → 0 triggers FM-002 |

---

## §3 — Triadic Equation

<!-- section: triadic-equation | invariants: INV-001, INV-003, INV-009 -->

### §3.1 — Formal Signature

```
f_Emit(A, Φ, δρ, r_emit) → Φ_updated | FM-010
```

| Parameter | Type | Description |
|---|---|---|
| `A` | Attractor | The attractor whose field is being amplified |
| `Φ` | FieldState | Current field state object (contains ρ(Φ)_current) |
| `δρ` | ℝ > 0 | Requested density increment (caller-supplied) |
| `r_emit` | ℝ > 0 | Emission radius (spatial bound of effect) |

| Return | Condition |
|---|---|
| `Φ_updated` | EC-1 and EC-2 satisfied; ρ(Φ) increased by ρ(Φ)_delta |
| `FM-010` | ρ(Φ)_current = 1.0 (no headroom) or ρ(Φ)_current + δρ > 1.0 and δρ was not clipped |

### §3.2 — Post-Conditions (from f_Field.md §7.1, extended)

```
Post-condition 1:  ρ(Φ_updated) = min(ρ(Φ_current) + δρ, 1.0)
Post-condition 2:  Ψ(A)_updated > Ψ(A)_prior  [coherence signature increases]
Post-condition 3:  v_escape(A)_updated ≥ v_escape(A)_prior
Post-condition 4:  capacity_MAX_updated ≥ capacity_MAX_prior
Post-condition 5:  If ρ(Φ_current) = 0 before call, FM-002 flag is cleared on success
```

Post-condition 5 makes `f_Emit` the canonical FM-002 recovery mechanism (consistent with f_Field.md §6, which defines FM-002 as: emit_field with any δρ > 0 restores ρ(Φ) > 0).

### §3.3 — G-Equation Role

The triadic product is:

```
G = F_freq · F_fluid · F_force          [INV-001]
```

`f_Emit` modifies the **F_freq factor** in G by increasing ρ(Φ). Because ρ(Φ) appears in:

- `v_escape(A) = √(2 × M_A × ρ(Φ) / r_capture)` — the SC-1 threshold
- `β = M_E × ρ(Φ) / M_A` — the SC-4 binding floor
- `capacity_MAX = floor(M_A × ρ(Φ) × k_frame)` — the SC-5 frame threshold

a successful `f_Emit` call **tightens all three active stability conditions simultaneously**, making the overall gravitational system more capture-ready and binding-stable. This is why `f_Emit` is the primary remediation tool in the FM-004 recovery pathway.

---

## §4 — Operator Registry

<!-- section: operator-registry | authority: OPERATORS.md §2.2, §2.1 -->

> **Authority:** OPERATORS.md is the symbol authority for all operators (INV-009). Definitions here are normative for f_Emit.md and must be reflected in OPERATORS.md §2.2 (previously frozen as 🔵 pending this file).

### §4.1 — New Operators Introduced

#### F_emit — Emission Field Strength

```
F_emit(Φ, δρ, r_emit) = (δρ · k_emit) / (r_emit · (1 − ρ(Φ)))
```

| Symbol | Meaning | Domain |
|---|---|---|
| δρ | Requested density increment (= ρ(Φ)_delta after ceiling check) | ℝ > 0 |
| k_emit | Emission coupling constant | ℝ > 0, default = 1.0 |
| r_emit | Emission radius | ℝ > 0, ≤ r_capture |
| ρ(Φ) | Current field density before emission | [0, 1) — must be < 1.0 |
| (1 − ρ(Φ)) | Headroom to saturation | (0, 1] |

**Interpretation:** F_emit measures emission efficiency — how much field-density increase is achieved per unit radius, normalized by available headroom. As ρ(Φ) → 1.0, headroom shrinks and F_emit → ∞, signaling that each marginal emission increment is increasingly costly and increasingly risky (FM-010 boundary).

**Undefined when:** ρ(Φ) = 1.0 (division by zero — EC-1 violation, FM-010 fires before this is evaluated).

#### ρ(Φ)_delta — Realized Density Increment

```
ρ(Φ)_delta = min(δρ_requested, 1.0 − ρ(Φ)_current)
```

| Property | Value |
|---|---|
| Type | Scalar, ℝ ≥ 0 |
| Meaning | Actual density increase applied after ceiling enforcement |
| δρ_requested > headroom | ρ(Φ)_delta = headroom (clipped, not FM-010) |
| ρ(Φ)_current = 1.0 | ρ(Φ)_delta = 0 → EC-1 violated → FM-010 |

Note: Clipping δρ_requested to the ceiling is **not** an FM-010 trigger. FM-010 fires only when ρ(Φ)_current = 1.0 and emission is attempted (zero headroom). Partial emission (clipped to available headroom) is valid and produces a `Φ_updated` with ρ(Φ) = 1.0.

#### r_emit — Emission Radius

```
r_emit ∈ (0, r_capture]
```

| Property | Value |
|---|---|
| Type | Scalar, ℝ > 0 |
| Meaning | Spatial radius of the emission effect centered on A |
| Lower bound | r_emit > 0 (EC-2; point emission undefined) |
| Upper bound | r_emit ≤ r_capture (EC-2; emission cannot exceed capture boundary) |
| Effect outside radius | None — ρ(Φ) unchanged beyond r_emit |

`r_emit` scales the energy cost E_emit quadratically (see below). Larger emission radii cost more energy but affect a wider region of the field state, making them more effective for F_frame capacity expansion and multi-entity stabilization scenarios.

#### E_emit — Emission Energy Cost

```
E_emit = M_A · ρ(Φ)_delta · r_emit² · k_cost
```

| Symbol | Meaning | Domain |
|---|---|---|
| M_A | Attractor mass-density | ℝ > 0 |
| ρ(Φ)_delta | Realized density increment (post-ceiling check) | ℝ ≥ 0 |
| r_emit | Emission radius | ℝ > 0 |
| k_cost | Emission cost scalar | ℝ > 0, default = 1.0 |

**Interpretation:** Emission energy cost scales with attractor mass (larger attractors require more energy to deepen their field), with the realized density increment (larger increases cost more), and quadratically with emission radius (wider coverage is disproportionately expensive). This quadratic radius scaling discourages wasteful large-radius emissions and reflects the volumetric nature of field coverage.

**When ρ(Φ)_delta = 0:** E_emit = 0 — no energy is consumed (ceiling was already at maximum, but EC-1 was violated before this is reached, so this case is informational only).

### §4.2 — Inherited Operators (No Changes)

The following operators are used by `f_Emit` as defined in their authority files. No modifications are introduced here.

| Operator | Authority File | Role in f_Emit |
|---|---|---|
| ρ(Φ) | f_Field.md §3, OPERATORS.md §2.1 | Input state; target of the increment |
| M_A | f_Force.md §4, OPERATORS.md §2.1 | Scales E_emit cost |
| r_capture | f_Frame.md §4, OPERATORS.md §2.1 | Upper bound for r_emit (EC-2) |
| β | f_Force.md §4, OPERATORS.md §2.1 | Indirectly raised by ρ(Φ) increase |
| v_escape(A) | f_Field.md §4, OPERATORS.md §2.1 | Indirectly raised by ρ(Φ) increase |
| capacity_MAX | f_Frame.md §4, OPERATORS.md §2.1 | Indirectly expanded by ρ(Φ) increase |
| Ψ(A) | f_Field.md §4, OPERATORS.md §2.1 | Coherence signature — increases on emit |

---

## §5 — Emit Conditions

<!-- section: emit-conditions | EC-1: Headroom Bound | EC-2: Radius Bound -->

Two conditions govern safe emission. Both must hold before `emit_field` executes. Violation of either blocks emission and requires the caller to handle the failure state.

### §5.1 — EC-1: Headroom Bound

```
EC-1:  ρ(Φ)_current < 1.0
```

**Statement:** The current field density must have at least some headroom below the saturation ceiling before emission can proceed.

| ρ(Φ)_current | EC-1 Result | Action |
|---|---|---|
| 0.0 to < 1.0 | ✅ Satisfied | Proceed with emission (δρ may be clipped to headroom) |
| = 1.0 | ❌ Violated | FM-010 fires; emit_field blocked |

**Note:** EC-1 evaluates the **current** ρ(Φ) before any delta is applied. If EC-1 is satisfied but the requested δρ would push ρ(Φ) above 1.0, the delta is clipped to the available headroom (ρ(Φ)_delta = 1.0 − ρ(Φ)_current). This is not an EC-1 violation — the clip is handled transparently by PRIM:017 before emission executes.

### §5.2 — EC-2: Radius Bound

```
EC-2:  0 < r_emit ≤ r_capture
```

**Statement:** The emission radius must be positive and must not exceed the attractor's established capture radius.

| r_emit value | EC-2 Result | Action |
|---|---|---|
| r_emit ≤ 0 | ❌ Violated | ValueError; emit_field blocked |
| 0 < r_emit ≤ r_capture | ✅ Satisfied | Proceed |
| r_emit > r_capture | ❌ Violated | ValueError; emit_field blocked |

**Rationale:** Emission beyond r_capture would attempt to deepen a coherence well in a region where no captured relationship exists. Because the FFF_Gravity model is relational (field state Φ is defined relative to A and its captures), extending emission past r_capture has undefined semantics. EC-2 enforces the spatial boundary of the operator's authority.

### §5.3 — Conditions as Conjunctive Gate

EC-1 AND EC-2 must both hold. There is no partial emission that bypasses either condition. The evaluation order is:

```
1. check_emit_ceiling(Φ)          → EC-1 check (PRIM:017)
2. validate r_emit ∈ (0, r_capture]  → EC-2 check (inline in PRIM:015)
3. compute ρ(Φ)_delta (clip if needed)
4. compute E_emit (PRIM:016)
5. execute field density update
6. update Φ post-conditions (Ψ, v_escape, capacity_MAX references)
```

---

## §6 — Failure Modes

<!-- section: failure-modes | FM-010: Amplify Runaway | FM-002: recovery pathway -->

### §6.1 — FM-010: Amplify Runaway

```
FM-010:  Amplify Runaway
Trigger: EC-1 violated — emit_field called when ρ(Φ) = 1.0
State flag set: EMIT_SATURATED
Severity: Warning (blocking — emission stops, existing captures unaffected)
Recovery: f_Dampen (reduce ρ(Φ) below 1.0, then resume emission if needed)
```

**Mechanism:** When ρ(Φ) = 1.0, the coherence well is at maximum depth. The binding ratio β of all captured entities is at its field-density-driven maximum. Attempting to emit further has no legitimate physical effect — the field cannot deepen further. In the FFF_Gravity model, this represents a **runaway amplification attempt**: the caller is pushing emission into a field that has nowhere to go.

The consequence is not catastrophic in the sense of f_Collapse (no entities are lost, no states are destroyed), but it is a hard block:

- `emit_field` returns `FM-010` immediately
- No ρ(Φ) change occurs
- No E_emit is charged (zero-cost failure)
- `EMIT_SATURATED` flag is set on Φ
- All active captures remain stable

**Why the name "Amplify Runaway":** In a real system using f_Amplify after f_Emit (the common sustained-emission pattern), FM-010 signals that the amplification loop has driven ρ(Φ) to 1.0 and must be paused. Without FM-010 detection, a naive amplification loop would spin indefinitely trying to push ρ(Φ) past its ceiling. FM-010 is the guard rail.

#### §6.1.1 — Detection Code

```python
def detect_fm010(phi: FieldState) -> bool:
    """
    Detect FM-010 (Amplify Runaway) condition.

    FM-010 fires when emission is attempted against a saturated field.
    This function checks the pre-condition; call before emit_field.

    Args:
        phi: Current field state.

    Returns:
        True if FM-010 condition is active (ρ(Φ) = 1.0), False if safe to emit.
    """
    return phi.rho >= 1.0
```

#### §6.1.2 — Recovery Code

```python
def recover_fm010(
    attractor: Attractor,
    phi: FieldState,
    target_rho: float,
    r_dampen: float
) -> FieldState:
    """
    FM-010 recovery via f_Dampen.

    Reduces ρ(Φ) from saturation to a target below 1.0 so that
    emission can resume. The target_rho should leave meaningful
    headroom (recommended: target_rho ≤ 0.90).

    Args:
        attractor:   The saturated attractor.
        phi:         Current saturated field state (rho = 1.0).
        target_rho:  Desired post-dampen field density (0.0 < target < 1.0).
        r_dampen:    Dampening radius (see f_Dampen.md for constraints).

    Returns:
        Updated FieldState with rho = target_rho and EMIT_SATURATED cleared.

    Raises:
        ValueError: If target_rho >= 1.0 or target_rho <= 0.0.
        RuntimeError: If f_Dampen fails (see f_Dampen.md for its own failure modes).
    """
    if not (0.0 < target_rho < 1.0):
        raise ValueError(
            f"FM-010 recovery target_rho must be in (0, 1); got {target_rho}"
        )

    delta_dampen = phi.rho - target_rho  # amount to reduce

    # Delegate to f_Dampen (canonical — see f_Dampen.md)
    phi_recovered = f_dampen(attractor, phi, delta_rho=delta_dampen, r_dampen=r_dampen)

    # Clear EMIT_SATURATED flag
    phi_recovered.flags.discard("EMIT_SATURATED")
    phi_recovered.flags.discard("EMIT_CEILING_APPROACHED")

    return phi_recovered
```

#### §6.1.3 — EMIT_CEILING_APPROACHED — Early Warning Flag

Before FM-010 fires, the state flag `EMIT_CEILING_APPROACHED` is set when:

```
ρ(Φ) ≥ α_ceiling_warn  (default: α_ceiling_warn = 0.90)
```

This is an advisory flag — it does not block emission, but it signals to the caller that the field is within 10% of saturation (by default) and FM-010 is approaching. Automated emission loops should monitor for this flag and either:
- Pause emission and allow natural decay to restore headroom, or
- Invoke f_Dampen proactively to maintain a working range

### §6.2 — FM-002 Recovery via f_Emit

`f_Emit` is the **primary recovery mechanism for FM-002 (Zero Field / Field Collapse)**, as established in f_Field.md §6 and f_Decay.md §6.1.3.

```
FM-002 recovery condition:  emit_field called with any δρ > 0 when ρ(Φ) = 0
FM-002 recovery result:     ρ(Φ) = δρ > 0 → FM-002 flag cleared
Note: EC-1 is satisfied when ρ(Φ) = 0 (0 < 1.0), so FM-002 recovery is always allowed
```

This means `f_Emit` and FM-002 have a special relationship: FM-002 is **never** a barrier to calling `emit_field`. A field at ρ(Φ) = 0 has maximum headroom (1.0), satisfies EC-1, and is the most cost-efficient state to emit into (E_emit is lowest per unit delta when ρ(Φ) is low).

### §6.3 — FM-004 Recovery via f_Emit

`f_Emit` is the **primary recovery mechanism for FM-004 (Resonance Drift — Warn)**, as established in f_Decay.md §6.1.3 (recovery pathway A):

```
FM-004 recovery pathway A:
  1. detect FM-004 (d_bind < d_warn, δ < 0)
  2. invoke f_Emit with δρ = recovery_delta > 0
  3. increased ρ(Φ) → increased v_escape(A) → tighter binding → d_bind rises next cycle
  4. if d_bind rises above d_warn: FM-004 cleared, RESONANCE_STABLE restored
```

Note that f_Emit addresses the **root cause** of FM-004 (field weakening), not just the symptom. This distinguishes it from a patch: a successful f_Emit in FM-004 recovery produces a genuinely deepened coherence well, not a superficial state flag reset.

---

## §7 — Engineering Primitives

<!-- section: engineering-primitives | PRIM:015-017 -->

All primitives follow the established FFF_Gravity conventions:
- **Pure functions** (no side effects beyond return value) are tagged `[PURE]`
- **Impure functions** (modify FieldState, trigger side effects) are tagged `[IMPURE]`
- All type hints are illustrative (implementation-language-agnostic)
- Full docstrings are normative — they constitute the primitive's specification

### §7.1 — PRIM:015 — emit_field [IMPURE]

```python
def emit_field(
    attractor: Attractor,
    phi: FieldState,
    delta_rho: float,
    r_emit: float,
    k_emit: float = 1.0,
    k_cost: float = 1.0
) -> FieldState:
    """
    PRIM:015 — emit_field [IMPURE]
    ==============================
    Canonical F_freq emission primitive. Increases the local field density
    ρ(Φ) of the attractor A by delta_rho (clipped to available headroom) within
    the spatial radius r_emit.

    This is the canonical implementation of the emit_field contract established
    in f_Field.md §7.1. PRIM:015 extends that contract with full condition
    checking, cost computation, post-condition enforcement, and FM-010 handling.

    Evaluation order (per INV-008):
        1. EC-1 check via check_emit_ceiling (FM-010 if violated)
        2. EC-2 check (r_emit bounds)
        3. Compute ρ(Φ)_delta (clip to headroom)
        4. Compute E_emit via compute_emit_cost
        5. Update ρ(Φ) in phi
        6. Update Ψ(A), v_escape(A) references
        7. Set/clear state flags
        8. Return Φ_updated

    Args:
        attractor:   The attractor whose field is being deepened.
        phi:         Current field state (contains rho, flags, coherence data).
        delta_rho:   Requested density increment. Must be > 0.
        r_emit:      Emission radius. Must satisfy 0 < r_emit ≤ r_capture.
        k_emit:      Emission coupling constant (default 1.0). See §4.1.
        k_cost:      Emission cost scalar (default 1.0). See §4.1.

    Returns:
        FieldState: Updated field state with:
            - rho increased by realized ρ(Φ)_delta
            - Ψ(A) updated (coherence signature risen)
            - v_escape updated (derived, not stored — recomputed on access)
            - capacity_MAX updated (derived, not stored — recomputed on access)
            - Flags updated (EMIT_ACTIVE set; EMIT_SATURATED cleared if was set)
            - EMIT_CEILING_APPROACHED set if rho_new ≥ α_ceiling_warn

    Raises:
        FM010Error:    EC-1 violated — ρ(Φ)_current = 1.0 (no headroom).
        ValueError:    delta_rho ≤ 0 or r_emit violates EC-2.
        RuntimeError:  phi is in a terminal state (CAPTURE_COLLISION or COLLAPSED).

    Side effects:
        - Modifies phi.rho, phi.coherence_signature, phi.flags in place
          (caller receives updated reference).
        - Logs emission event to GravityGraph audit trail.
        - Emits EMIT_COMPLETE event to registered observers.

    Cost:
        E_emit = M_A · ρ(Φ)_delta · r_emit² · k_cost
        (Computed but not deducted here — caller is responsible for energy accounting.)
        Call compute_emit_cost (PRIM:016) beforehand if pre-validation is required.
    """
    # ── Guard: terminal states ──────────────────────────────────────────────
    if phi.flags & {"CAPTURE_COLLISION", "COLLAPSED"}:
        raise RuntimeError(
            "emit_field called on terminal field state — emission is not permitted "
            "after CAPTURE_COLLISION or COLLAPSED. (INV-006: terminal states irreversible)"
        )

    # ── Guard: delta_rho must be positive ──────────────────────────────────
    if delta_rho <= 0:
        raise ValueError(f"delta_rho must be > 0; got {delta_rho}")

    # ── EC-1: Headroom Bound ────────────────────────────────────────────────
    ceiling_ok, headroom = check_emit_ceiling(phi)
    if not ceiling_ok:
        phi.flags.add("EMIT_SATURATED")
        raise FM010Error(
            "FM-010 (Amplify Runaway): emit_field called on saturated field "
            f"(ρ(Φ) = {phi.rho:.4f}). Invoke f_Dampen to restore headroom before "
            "resuming emission."
        )

    # ── EC-2: Radius Bound ─────────────────────────────────────────────────
    if r_emit <= 0:
        raise ValueError(f"r_emit must be > 0; got {r_emit}")
    if r_emit > attractor.r_capture:
        raise ValueError(
            f"r_emit ({r_emit}) exceeds r_capture ({attractor.r_capture}). "
            "EC-2 violated — emission radius cannot exceed capture boundary."
        )

    # ── Compute realized delta (clip to headroom) ──────────────────────────
    rho_delta_realized = min(delta_rho, headroom)

    # ── Compute emission cost (informational — energy deduction is caller's) ─
    e_emit = compute_emit_cost(
        m_a=attractor.mass,
        rho_delta=rho_delta_realized,
        r_emit=r_emit,
        k_cost=k_cost
    )
    phi.last_emit_cost = e_emit  # record for caller inspection

    # ── Apply density increment ────────────────────────────────────────────
    rho_prior = phi.rho
    phi.rho = rho_prior + rho_delta_realized  # always ≤ 1.0 by construction
    phi.rho = min(phi.rho, 1.0)               # defensive clamp

    # ── Update coherence signature Ψ(A) ───────────────────────────────────
    phi.coherence_signature = _compute_coherence_signature(attractor, phi)

    # ── Update state flags ─────────────────────────────────────────────────
    phi.flags.discard("EMIT_SATURATED")       # clear stale saturation flag
    phi.flags.add("EMIT_ACTIVE")

    # Early-warning ceiling approach flag
    ALPHA_CEILING_WARN: float = 0.90
    if phi.rho >= ALPHA_CEILING_WARN:
        phi.flags.add("EMIT_CEILING_APPROACHED")
    else:
        phi.flags.discard("EMIT_CEILING_APPROACHED")

    # FM-002 flag clear (ρ(Φ) > 0 guaranteed here)
    phi.flags.discard("FIELD_COLLAPSED")      # FM-002 state flag

    # ── Notify GravityGraph ────────────────────────────────────────────────
    _notify_gravity_graph(
        event="EMIT_COMPLETE",
        attractor=attractor,
        rho_prior=rho_prior,
        rho_new=phi.rho,
        rho_delta=rho_delta_realized,
        r_emit=r_emit,
        e_emit=e_emit
    )

    return phi
```

### §7.2 — PRIM:016 — compute_emit_cost [PURE]

```python
def compute_emit_cost(
    m_a: float,
    rho_delta: float,
    r_emit: float,
    k_cost: float = 1.0
) -> float:
    """
    PRIM:016 — compute_emit_cost [PURE]
    ====================================
    Compute the energy cost of a prospective emission operation before execution.

    This pure function enables callers to pre-validate cost before calling
    emit_field (PRIM:015). It implements the E_emit formula:

        E_emit = M_A · ρ(Φ)_delta · r_emit² · k_cost

    Args:
        m_a:       Attractor mass-density M_A. Must be > 0.
        rho_delta: Realized density increment ρ(Φ)_delta (already clipped
                   to headroom by the caller or by check_emit_ceiling).
                   Must be ≥ 0.
        r_emit:    Emission radius. Must be > 0.
        k_cost:    Emission cost scalar (default 1.0).

    Returns:
        float: E_emit — the energy cost of the emission. Non-negative.
               Returns 0.0 when rho_delta = 0 (no-op emission).

    Raises:
        ValueError: If m_a ≤ 0, r_emit ≤ 0, k_cost ≤ 0, or rho_delta < 0.

    Notes:
        - This function is pure: it has no side effects and does not modify any state.
        - The caller is responsible for energy deduction (E_emit is returned, not spent).
        - The quadratic r_emit² term reflects volumetric field coverage cost.
        - At fixed δρ and r_emit, cost scales linearly with M_A: more massive
          attractors require proportionally more energy to deepen their field.
    """
    if m_a <= 0:
        raise ValueError(f"m_a must be > 0; got {m_a}")
    if r_emit <= 0:
        raise ValueError(f"r_emit must be > 0; got {r_emit}")
    if k_cost <= 0:
        raise ValueError(f"k_cost must be > 0; got {k_cost}")
    if rho_delta < 0:
        raise ValueError(f"rho_delta must be ≥ 0; got {rho_delta}")

    return m_a * rho_delta * (r_emit ** 2) * k_cost
```

### §7.3 — PRIM:017 — check_emit_ceiling [PURE]

```python
def check_emit_ceiling(
    phi: FieldState,
    alpha_warn: float = 0.90
) -> tuple[bool, float]:
    """
    PRIM:017 — check_emit_ceiling [PURE]
    =====================================
    Check whether emission is safe (EC-1) and compute available headroom.

    This is the canonical EC-1 gate. It must be called at the start of every
    emit_field invocation. The function:
      1. Returns False (blocked) if ρ(Φ) = 1.0 (FM-010 condition).
      2. Returns True (safe) with headroom if ρ(Φ) < 1.0.
      3. Notes proximity to ceiling via the second return value.

    Args:
        phi:        Current field state.
        alpha_warn: Ceiling approach threshold (default 0.90).
                    When phi.rho ≥ alpha_warn, headroom is considered
                    "low" and the caller should plan dampening.

    Returns:
        Tuple[bool, float]:
            - bool:  True if emission is permitted (EC-1 satisfied),
                     False if FM-010 applies (ρ(Φ) = 1.0).
            - float: Available headroom = 1.0 − ρ(Φ)_current.
                     0.0 when EC-1 is violated.

    Raises:
        ValueError: If phi.rho < 0 (invalid field state — invariant violation).

    Notes:
        - Pure function: reads phi.rho only, no mutations.
        - Headroom < (1.0 − alpha_warn) signals EMIT_CEILING_APPROACHED territory.
        - Callers should treat headroom < 0.05 as requiring f_Dampen before
          any further emission cycle to prevent FM-010 on the next call.

    Examples:
        >>> check_emit_ceiling(phi_with_rho_0_7)
        (True, 0.30)

        >>> check_emit_ceiling(phi_with_rho_1_0)
        (False, 0.0)

        >>> check_emit_ceiling(phi_with_rho_0_95)
        (True, 0.05)  # EMIT_CEILING_APPROACHED territory
    """
    if phi.rho < 0:
        raise ValueError(
            f"Invalid field state: phi.rho = {phi.rho} < 0. "
            "Module invariant violation (INV-003 consequence)."
        )

    if phi.rho >= 1.0:
        return False, 0.0

    headroom = 1.0 - phi.rho
    return True, headroom
```

---

## §8 — Canonical Examples

<!-- section: canonical-examples | 4 examples -->

### §8.1 — Example 1: FM-004 Recovery via Emergency Emission

**Scenario:** A captured satellite is in FM-004 (Resonance Drift — Warn). The field density has decayed to ρ(Φ) = 0.28, below the d_warn threshold. f_Decay has issued a warn flag. f_Emit is called to restore field coherence before decay reaches d_collapse.

**Initial Parameters:**

| Parameter | Value |
|---|---|
| M_A (planetary attractor) | 5.97 |
| M_E (satellite) | 0.15 |
| ρ(Φ)_current | 0.28 |
| r_capture | 12.4 |
| d_bind(0) | 9.40 |
| d_bind(t) | 3.94 (= 0.42 × d_bind(0)) |
| d_warn | 3.76 (= 0.40 × d_bind(0)) |
| d_collapse | 0.94 (= 0.10 × d_bind(0)) |
| Active flags | FM_WARN_ACTIVE, RESONANCE_DRIFTING |

**Emission Parameters:**

| Parameter | Value | Check |
|---|---|---|
| δρ_requested | 0.35 | — |
| r_emit | 10.0 | ≤ r_capture (12.4) ✅ EC-2 |
| EC-1: headroom | 0.72 (= 1.0 − 0.28) | ✅ |
| ρ(Φ)_delta | 0.35 | (< headroom; no clip) |
| E_emit | 5.97 × 0.35 × 100 × 1.0 = **208.95** | — |

**Post-Emission State:**

| Variable | Before | After |
|---|---|---|
| ρ(Φ) | 0.28 | **0.63** |
| v_escape(A) | √(2 × 5.97 × 0.28 / 12.4) = 0.519 | **√(2 × 5.97 × 0.63 / 12.4) = 0.779** |
| β | 0.15 × 0.28 / 5.97 = 0.00704 | **0.15 × 0.63 / 5.97 = 0.01584** |
| capacity_MAX | floor(5.97 × 0.28 × k_frame) | **floor(5.97 × 0.63 × k_frame)** |
| d_bind (next cycle) | 3.94 → rising | Rising — FM-004 recovery pathway active |

**Trace:**
```
[FM-004 detected] d_bind = 3.94, d_warn = 3.76 → WARN threshold crossed
[EC-1 check] ρ(Φ) = 0.28 < 1.0 → headroom = 0.72 ✅
[EC-2 check] r_emit = 10.0 ≤ r_capture = 12.4 ✅
[compute_emit_cost] E_emit = 5.97 × 0.35 × 100 = 208.95
[emit_field] ρ(Φ): 0.28 → 0.63
[flags] FM_WARN_ACTIVE cleared | EMIT_ACTIVE set
[next decay cycle] d_bind rises (ρ(Φ) deepened) → RESONANCE_STABLE on track
```

**Outcome:** FM-004 recovery initiated. If field holds at ρ(Φ) ≥ 0.63 for the next decay cycle, d_bind crosses back above d_warn and FM-004 is cleared.

---

### §8.2 — Example 2: Frame Capacity Expansion via Targeted Emission

**Scenario:** An attractor A has reached its frame capacity (capacity_MAX = 3, all slots filled). A new capture candidate arrives (entity E_4). Rather than calling f_Collapse or discarding E_4, the operator calls f_Emit to increase ρ(Φ), which indirectly expands capacity_MAX.

**Initial Parameters:**

| Parameter | Value |
|---|---|
| M_A | 8.00 |
| ρ(Φ)_current | 0.45 |
| k_frame | 0.833 |
| capacity_MAX | floor(8.00 × 0.45 × 0.833) = floor(2.999) = **2** |
| captured entities | 2 (slots full at capacity = 2) |

*(Note: k_frame = 0.833 gives capacity = 2 for this M_A/ρ(Φ) combination.)*

**Goal:** Raise capacity_MAX to 3 to accommodate E_4. Need: floor(M_A × ρ(Φ)_new × k_frame) ≥ 3.

**Required ρ(Φ)_new:** 3 / (8.00 × 0.833) = 3 / 6.664 = **0.450...** → need ρ(Φ) > 0.450 strictly.

Minimum viable ρ(Φ)_delta = 0.001 above current 0.45 → let's use δρ = 0.05 for safe margin.

**Emission Parameters:**

| Parameter | Value | Check |
|---|---|---|
| δρ_requested | 0.05 | — |
| r_emit | 6.0 | ≤ r_capture (assumed 9.2) ✅ EC-2 |
| EC-1: headroom | 0.55 | ✅ |
| ρ(Φ)_delta | 0.05 | (no clip needed) |
| E_emit | 8.00 × 0.05 × 36 × 1.0 = **14.40** | — |

**Post-Emission State:**

| Variable | Before | After |
|---|---|---|
| ρ(Φ) | 0.45 | **0.50** |
| capacity_MAX | floor(8.00 × 0.45 × 0.833) = **2** | floor(8.00 × 0.50 × 0.833) = floor(3.332) = **3** |
| Slots available | 0 | **1** |

**Trace:**
```
[SC-5 check] capacity_remaining = 0 → capture of E_4 blocked
[decision] f_Emit to expand capacity_MAX
[EC-1 check] ρ(Φ) = 0.45 < 1.0 → headroom = 0.55 ✅
[EC-2 check] r_emit = 6.0 ≤ r_capture = 9.2 ✅
[compute_emit_cost] E_emit = 8.00 × 0.05 × 36 = 14.40
[emit_field] ρ(Φ): 0.45 → 0.50
[capacity_MAX] 2 → 3 (SC-5 now satisfied for E_4)
[f_Capture] E_4 captured — SC-1 through SC-5 all satisfied
```

**Outcome:** Frame capacity expanded from 2 to 3 via a minimal, cost-efficient f_Emit call (E_emit = 14.40). E_4 successfully captured without requiring any collapse of existing relationships.

---

### §8.3 — Example 3: Cold-Start Bootstrap

**Scenario:** A newly initialized attractor A has ρ(Φ) = 0.0 (field not yet established). FM-002 (Zero Field) is active. No captures are possible until ρ(Φ) > 0. A bootstrap emission sequence is required to bring the field to a viable operating density.

**Initial Parameters:**

| Parameter | Value |
|---|---|
| M_A | 3.50 |
| ρ(Φ)_current | 0.00 |
| Active flags | FIELD_COLLAPSED (FM-002) |
| r_capture | Undefined (no captures yet — use operational r_capture = 7.0) |

**Bootstrap Sequence (3 pulses, conservative approach):**

| Pulse | δρ | r_emit | E_emit | ρ(Φ) after |
|---|---|---|---|---|
| 1 | 0.20 | 4.0 | 3.50 × 0.20 × 16 = 11.20 | 0.20 |
| 2 | 0.20 | 5.0 | 3.50 × 0.20 × 25 = 17.50 | 0.40 |
| 3 | 0.15 | 6.0 | 3.50 × 0.15 × 36 = 18.90 | 0.55 |
| **Total** | **0.55** | — | **47.60** | **0.55** |

**Post-Bootstrap State:**

| Variable | Before | After |
|---|---|---|
| ρ(Φ) | 0.00 | **0.55** |
| FM-002 (FIELD_COLLAPSED) | Active | **Cleared** (after Pulse 1) |
| v_escape(A) | Undefined | **√(2 × 3.50 × 0.55 / 7.0) = 0.742** |
| SC-2 satisfied | ❌ | **✅** |
| SC-3 satisfied | ❌ | **✅** (assuming ω_res computed from ρ(Φ) = 0.55) |

**Trace:**
```
[FM-002 active] ρ(Φ) = 0.0 → no captures possible
[Pulse 1] EC-1: 0.0 < 1.0 ✅ | EC-2: 4.0 ≤ 7.0 ✅
          emit_field → ρ(Φ): 0.00 → 0.20 | FIELD_COLLAPSED cleared ✅
[Pulse 2] EC-1: 0.2 < 1.0 ✅ | EC-2: 5.0 ≤ 7.0 ✅
          emit_field → ρ(Φ): 0.20 → 0.40
[Pulse 3] EC-1: 0.4 < 1.0 ✅ | EC-2: 6.0 ≤ 7.0 ✅
          emit_field → ρ(Φ): 0.40 → 0.55
[SC-2] ρ(Φ) = 0.55 > 0 ✅ | field uniform within r_emit = 6.0 ✅
[operational] A ready for capture attempts — FM-002 resolved
```

**Outcome:** A cold attractor bootstrapped to ρ(Φ) = 0.55 via 3 progressive pulses. Total cost: 47.60 energy units. FM-002 cleared after Pulse 1. The progressive pulse pattern (expanding r_emit each pulse) ensures spatial coherence builds from the center outward, avoiding discontinuities in the field state.

---

### §8.4 — Example 4: FM-010 Trigger and Prevention

**Scenario:** An automated emission loop is running to sustain ρ(Φ) during high-activity capture operations. The loop fails to check `EMIT_CEILING_APPROACHED` and drives ρ(Φ) to 1.0, triggering FM-010.

**Part A — FM-010 Trigger:**

| Step | ρ(Φ) | δρ requested | Result |
|---|---|---|---|
| Loop iter 1 | 0.70 | 0.10 | ✅ → ρ(Φ) = 0.80 |
| Loop iter 2 | 0.80 | 0.10 | ✅ → ρ(Φ) = 0.90 (EMIT_CEILING_APPROACHED set) |
| Loop iter 3 | 0.90 | 0.10 | ✅ → ρ(Φ) = 1.00 (clipped to ceiling) |
| Loop iter 4 | 1.00 | 0.10 | ❌ **FM-010** — EMIT_SATURATED set; emission blocked |

```
[Loop iter 4] EC-1: ρ(Φ) = 1.0 ≥ 1.0 → VIOLATION
              FM-010 raised: FM010Error("Amplify Runaway")
              EMIT_SATURATED flag set
              Loop terminates (
Resuming exactly where the file was cut. Paste this block immediately after the truncation point (starting at the `Loop terminates (` line):

---

```markdown
              Loop terminates (unhandled exception if not caught))
```

**Part A Interpretation:** The loop correctly ran for iterations 1–3, with iter 3 delivering a clipped increment (requested 0.10, headroom = 0.10, so ρ(Φ)_delta = 0.10 — exactly at ceiling). Iter 4 finds ρ(Φ) = 1.0, EC-1 fails, and FM-010 fires. The error is recoverable but interrupts the loop.

---

**Part B — Prevention (Corrected Pattern):**

The correct automated emission loop checks `EMIT_CEILING_APPROACHED` and pauses before FM-010 can fire:

```python
def sustained_emission_loop(
    attractor: Attractor,
    phi: FieldState,
    target_rho: float,
    delta_rho_per_pulse: float,
    r_emit: float,
    max_pulses: int = 100,
    headroom_reserve: float = 0.05
) -> tuple[FieldState, int]:
    """
    Safe sustained emission loop with FM-010 prevention.

    Emits in repeated pulses toward target_rho, stopping automatically
    when ρ(Φ) approaches the ceiling or the target is reached.

    Args:
        attractor:          Attractor whose field is being deepened.
        phi:                Current field state.
        target_rho:         Desired final ρ(Φ) (must be < 1.0).
        delta_rho_per_pulse: Density increment per pulse.
        r_emit:             Emission radius (EC-2 constraint applies).
        max_pulses:         Safety cap on loop iterations.
        headroom_reserve:   Minimum headroom to maintain (stop before
                            dropping below this). Default 0.05 = 5%.

    Returns:
        Tuple of (updated FieldState, pulses_executed).

    Raises:
        ValueError: If target_rho ≥ 1.0 or target_rho ≤ phi.rho.
    """
    if target_rho >= 1.0:
        raise ValueError(f"target_rho must be < 1.0; got {target_rho}")
    if target_rho <= phi.rho:
        return phi, 0  # already at or above target

    pulses = 0
    while pulses < max_pulses:
        # FM-010 prevention: check headroom before each pulse
        ceiling_ok, headroom = check_emit_ceiling(phi)  # PRIM:017

        if not ceiling_ok:
            # Should never reach here in a safe loop, but defensive guard
            break

        # Stop if we've hit the headroom reserve floor
        if headroom < headroom_reserve:
            # EMIT_CEILING_APPROACHED is set — pause and let natural decay
            # restore some headroom before resuming, or call f_Dampen
            break

        # Stop if target is reached
        if phi.rho >= target_rho:
            break

        # Clip pulse to minimum of: requested delta, available headroom,
        # and remaining distance to target
        delta_this_pulse = min(
            delta_rho_per_pulse,
            headroom - headroom_reserve,        # keep reserve
            target_rho - phi.rho                # don't overshoot target
        )

        if delta_this_pulse <= 0:
            break

        phi = emit_field(attractor, phi, delta_this_pulse, r_emit)  # PRIM:015
        pulses += 1

    return phi, pulses
```

**Corrected loop trace for Example 4:**

| Pulse | ρ(Φ) before | headroom | delta_applied | ρ(Φ) after | flags |
|---|---|---|---|---|---|
| 1 | 0.70 | 0.30 | 0.10 | 0.80 | EMIT_ACTIVE |
| 2 | 0.80 | 0.20 | 0.10 | 0.90 | EMIT_CEILING_APPROACHED ⚠️ |
| 3 | 0.90 | 0.10 | 0.05 (reserve=0.05 → stop delta = 0.10−0.05=0.05) | 0.95 | paused |
| — | Loop exits (headroom reserve 0.05 reached) — FM-010 never fires | | | | |

**Outcome:** FM-010 prevented by `headroom_reserve` guard. Loop exits cleanly at ρ(Φ) = 0.95 with 5% headroom intact. If more emission is needed, the caller must either accept the current level, wait for natural decay to free headroom, or call `f_Dampen` to intentionally lower ρ(Φ) before resuming.

**Key lesson:** FM-010 is always an engineering error, never an unavoidable condition. Any emission loop that lacks a `check_emit_ceiling` call and a headroom reserve will eventually trigger it. PRIM:017 exists precisely to prevent this.

---

## §9 — Cross-Module References

<!-- section: cross-module-references | status: canonical -->

### §9.1 — Files That Call f_Emit

| Caller | Context | Interface |
|---|---|---|
| f_Decay.md | FM-004 recovery pathway A (d_bind falling; increase ρ(Φ) to restore d_bind) | emit_field(A, Φ, δρ, r_emit) |
| f_Frame.md | Capacity expansion when capacity_MAX insufficient (indirect — operator invocation) | emit_field(A, Φ, δρ, r_emit) |
| f_Capture_Resonant.md | Target field tuning (set ρ(Φ) to achieve desired ω_res for resonant capture) | emit_field(A, Φ, δρ, r_emit) |

### §9.2 — Files That f_Emit Depends On

| Dependency | Role | What f_Emit Reads |
|---|---|---|
| f_Field.md | F_freq node definition, ρ(Φ) semantics, FM-002, Ψ(A) | ρ(Φ), Ψ, coherence well model |
| f_Frame.md | capacity_MAX derivation (affected by ρ(Φ) change) | M_A, k_frame, capacity formula |
| f_Decay.md | FM-004 context — caller provides d_bind, d_warn | FM-004 state flag |
| OPERATORS.md | Symbol authority — F_emit, r_emit, E_emit all registered here | Freeze registry |
| GLOSSARY.md | Prose definitions: Coherence Well, Field Density, Gravity Emitter | Term authority |

### §9.3 — Files That Interact Inversely

| File | Relationship | Interaction Pattern |
|---|---|---|
| f_Dampen.md | Inverse primitive — decreases ρ(Φ) | FM-010 recovery calls f_Dampen; sustained emission + Dampen cycle is the field modulation pattern |
| f_Amplify.md | Complementary primitive — multiplies β (not ρ(Φ) directly) | Often paired with f_Emit: Emit deepens the well, Amplify tightens the binding coefficient |
| f_Capture_Resonant.md | Consumer — uses f_Emit to tune field for target resonance | Resonant approach engineering uses emit to pre-set ρ(Φ) to a target value before approach |

### §9.4 — GravityGraph Events Emitted

When `emit_field` executes and a GravityGraph observer is registered, the following events are dispatched:

| Event | Trigger | Payload |
|---|---|---|
| `EMIT_COMPLETE` | Successful emission | attractor_id, rho_prior, rho_new, rho_delta, r_emit, e_emit, cycle |
| `EMIT_CEILING_APPROACHED` | ρ(Φ) ≥ α_ceiling_warn (0.90) | attractor_id, rho_current, headroom_remaining |
| `EMIT_SATURATED` | FM-010 triggered | attractor_id, rho_current, cycle |
| `FM002_CLEARED` | ρ(Φ) > 0 after FM-002 recovery | attractor_id, rho_new, cycle |

### §9.5 — OPERATORS.md Updates Required

The following entries must be updated in OPERATORS.md after this file is committed:

| Entry | Current State | Update Required |
|---|---|---|
| `F_emit` | 🔵 pending (stub in §2.2) | 🟢 frozen — source: f_Emit.md §4.1 |
| `ρ(Φ)_delta` | 🔵 pending | 🟢 frozen — source: f_Emit.md §4.1 |
| `r_emit` | 🔵 pending (stub in §2.2) | 🟢 frozen — source: f_Emit.md §4.1 |
| `E_emit` | 🔵 pending | 🟢 frozen — source: f_Emit.md §4.1 |
| PRIM:015 `emit_field` | pending | 🟢 frozen — source: f_Emit.md §7.1 |
| PRIM:016 `compute_emit_cost` | pending | 🟢 frozen — source: f_Emit.md §7.2 |
| PRIM:017 `check_emit_ceiling` | pending | 🟢 frozen — source: f_Emit.md §7.3 |
| FM-010 `Amplify Runaway` | pending | 🟢 frozen — source: f_Emit.md §6.1 |
| `EMIT_ACTIVE` state flag | pending | 🟢 frozen — source: f_Emit.md §7.1 |
| `EMIT_SATURATED` state flag | pending | 🟢 frozen — source: f_Emit.md §6.1 |
| `EMIT_CEILING_APPROACHED` state flag | pending | 🟢 frozen — source: f_Emit.md §7.3 |

---

## §10 — Document Metadata

<!-- section: document-metadata | status: canonical | frozen: 2026-08-13 -->

### §10.1 — INV Compliance Table

| INV | Statement | Compliance in f_Emit.md |
|---|---|---|
| INV-001 | G = F_freq · F_fluid · F_force | ✅ §3.3 shows ρ(Φ) change propagates through all three nodes |
| INV-002 | f_Capture(E, A, Φ) → Ω frozen | ✅ f_Emit is downstream; f_Capture signature not touched |
| INV-003 | ρ(Φ) = 0 → FM-002 | ✅ §6.2: FM-002 cleared by emit; EC-1 allows emission when ρ(Φ) = 0 |
| INV-004 | β < 1.0 → flyby | ✅ f_Emit may raise β via ρ(Φ) — consistent; no bypass |
| INV-005 | All SCs conjunctive | ✅ EC-1 and EC-2 are conjunctive (§5.3) |
| INV-006 | Terminal states irreversible | ✅ PRIM:015 raises RuntimeError if called on terminal field state |
| INV-007 | f_Source.md read-only | ✅ Not referenced |
| INV-008 | Evaluation order normative | ✅ §7.1 PRIM:015 docstring specifies 8-step evaluation order |
| INV-009 | OPERATORS.md is symbol authority | ✅ §9.5 lists all required OPERATORS.md updates |
| INV-010 | Frozen symbols unrenameable | ✅ All four new operators declared frozen in §4.1 |

### §10.2 — Primitive Registry (f_Emit.md Additions)

| ID | Name | Type | Formula / Purpose |
|---|---|---|---|
| PRIM:015 | `emit_field` | Impure | Apply ρ(Φ) increment: main execution primitive |
| PRIM:016 | `compute_emit_cost` | Pure | `E_emit = M_A · ρ(Φ)_delta · r_emit² · k_cost` |
| PRIM:017 | `check_emit_ceiling` | Pure | EC-1 gate: returns (bool, headroom) |

### §10.3 — Operator Registry (f_Emit.md Additions)

| Symbol | Formula | Node | Status |
|---|---|---|---|
| `F_emit` | `(δρ · k_emit) / (r_emit · (1 − ρ(Φ)))` | F_freq | 🟢 frozen |
| `ρ(Φ)_delta` | `min(δρ_requested, 1.0 − ρ(Φ)_current)` | F_freq | 🟢 frozen |
| `r_emit` | scalar ∈ (0, r_capture] | F_freq | 🟢 frozen |
| `E_emit` | `M_A · ρ(Φ)_delta · r_emit² · k_cost` | F_freq | 🟢 frozen |

### §10.4 — Failure Mode Registry (f_Emit.md)

| ID | Name | Severity | Trigger | Recoverable |
|---|---|---|---|---|
| FM-010 | Amplify Runaway | Warning (blocking) | ρ(Φ) = 1.0 at emission attempt | Yes — via f_Dampen |
| FM-002 | Zero Field | (inherited from f_Field.md) | ρ(Φ) = 0; cleared by f_Emit | Yes — f_Emit is the recovery |

### §10.5 — Wave 3 Status

| File | Status |
|---|---|
| f_Release.md | ✅ canonical |
| f_Decay.md | ✅ canonical |
| f_Orbit.md | ✅ canonical |
| f_Collapse.md | ✅ canonical |
| **f_Emit.md** | ✅ **canonical ← this file** |
| f_Dampen.md | 🔵 scaffold — **next** |
| f_Amplify.md | 🔵 scaffold |
| f_Deflect.md | 🔵 scaffold |

### §10.6 — Changelog Entry

```
## [1.0.0] — 2026-08-13 — SES-20260813-EMIT-001

### Added
- f_Emit.md — canonical Wave 3 file 5 of 8
- Operators frozen: F_emit, ρ(Φ)_delta, r_emit, E_emit
- Primitives frozen: PRIM:015 emit_field, PRIM:016 compute_emit_cost,
  PRIM:017 check_emit_ceiling
- FM-010 (Amplify Runaway) fully specified and frozen
- State flags frozen: EMIT_ACTIVE, EMIT_SATURATED, EMIT_CEILING_APPROACHED
- Emit Conditions EC-1 (Headroom Bound) and EC-2 (Radius Bound) defined
- 4 canonical examples: FM-004 recovery, frame capacity expansion,
  cold-start bootstrap, FM-010 trigger and prevention
- sustained_emission_loop safe pattern with headroom_reserve guard
- GravityGraph event interface specified (4 event types)

### Operator Status Updates Required in OPERATORS.md
- F_emit:           🔵 → 🟢 frozen (f_Emit.md §4.1)
- ρ(Φ)_delta:       🔵 → 🟢 frozen (f_Emit.md §4.1)
- r_emit:           🔵 → 🟢 frozen (f_Emit.md §4.1)
- E_emit:           🔵 → 🟢 frozen (f_Emit.md §4.1)
- PRIM:015-017:     pending → frozen (f_Emit.md §7)
- FM-010:           pending → frozen (f_Emit.md §6.1)
```

---

*End of f_Emit.md — canonical v1.0.0 — [FFF:GRAVITY:EMIT] — SES-20260813-EMIT-001*
````

---

Here is the complete canonical `f_Dampen.md`. Paste the full block into the GitHub editor at `docs/FFF_Gravity/f_Dampen.md`.

---

```markdown
---
module: FFF_Gravity
file: f_Dampen.md
version: 1.0.0
wave: 3
session: SES-20260813-DAMPEN-001
status: canonical
depends_on:
  - f_Capture.md
  - f_Field.md
  - f_Force.md
  - f_Frame.md
  - f_Emit.md
unlocks:
  - f_Amplify.md
frozen_symbols:
  - F_damp
  - suppress_field
  - check_floor
  - check_cascade_risk
  - ρ(Φ)_floor
  - r_damp
  - δρ_damp
  - cascade_guard
  - k_damp
  - k_cost_damp
  - DAMPEN_ACTIVE
  - DAMPEN_FLOOR_APPROACHED
  - DAMPEN_CASCADE
  - FM-009
invariants_enforced:
  - INV-001
  - INV-002
  - INV-003
  - INV-005
  - INV-006
  - INV-008
  - INV-009
  - INV-010
primitives_defined:
  - PRIM:018
  - PRIM:019
  - PRIM:020
---

<!-- §0 SESSION CONTEXT -->
# §0 Session Context

| Field | Value |
|---|---|
| Session ID | SES-20260813-DAMPEN-001 |
| Produced | 2026-08-13 |
| Author | Nawder / umaywant2 |
| Repository | https://github.com/umaywant2/TriadicFrameworks |
| Wave | 3 of 4 — Core Functions (file 6 of 8) |
| Depends on canonical | f_Emit.md (SES-20260813-EMIT-001) |
| Unlocks | f_Amplify.md |
| Status | ✅ canonical — paste directly into GitHub editor |

> **Scope note.** This file defines `f_Dampen`, the inverse field-engineering primitive
> to `f_Emit`. Where `f_Emit` raises `ρ(Φ)` by injecting coherence into the attractor
> field, `f_Dampen` lowers `ρ(Φ)` by suppressing it — reducing local gravity strength
> in a controlled, bounded way. All dampening acts solely on the F_freq node via `ρ(Φ)`;
> the F_force and F_fluid nodes are not directly written.

---

<!-- §1 MODULE IDENTITY -->
# §1 Module Identity

```
FFF_Gravity :: f_Dampen
Operator  : F_damp
Layer     : F_freq (via ρ(Φ) suppression)
Role      : Controlled reduction of attractor field density
Inverse   : f_Emit (F_emit raises ρ(Φ); F_damp lowers it)
Primitive : suppress_field        PRIM:018  impure
            check_floor           PRIM:019  pure
            check_cascade_risk    PRIM:020  pure / diagnostic
Flags     : DAMPEN_ACTIVE
            DAMPEN_FLOOR_APPROACHED
            DAMPEN_CASCADE
Failure   : FM-009  Dampen Cascade  (fatal)
Depends   : f_Field.md  → ρ(Φ), r_capture
            f_Force.md  → M_A
            f_Frame.md  → GravityGraph, adjacent-node registry
            f_Emit.md   → FM-010 shared ceiling (read-only reference)
```

---

<!-- §2 CANONICAL DESCRIPTION -->
# §2 Canonical Description

`f_Dampen` is the **field-suppression engineering primitive** for the FFF_Gravity module.
It provides the only sanctioned mechanism for *decreasing* `ρ(Φ)` on a live attractor
node `A`. No other operator may write `ρ(Φ)` downward except `suppress_field` (PRIM:018).

### 2.1 Purpose

In standard operation, `ρ(Φ)` drifts upward under repeated `f_Emit` calls, or rises
naturally when many captures increase local coherence density. `f_Dampen` allows an
operator to:

- Drain excess field density before FM-010 (Amplify Runaway) is triggered.
- Reduce local gravity strength to permit controlled orbital degradation.
- Bring a saturated attractor below the FM-010 blocking threshold (`ρ(Φ) < 1.0`).
- Widen the effective capture radius by lowering `ρ(Φ)` (reducing `v_escape(A)`).

### 2.2 Constraint Envelope

Dampening is bounded on both sides:

| Bound | Symbol | Constraint |
|---|---|---|
| Floor | `ρ(Φ)_floor` | `ρ(Φ)` after suppression ≥ `ρ(Φ)_floor` > 0 |
| Ceiling | `ρ(Φ)` (current) | Cannot suppress below current value — no negative delta |
| Radius | `r_damp` | Must satisfy `r_damp ∈ (0, r_capture]` |
| Cascade guard | `cascade_guard` | Boolean flag; when `true`, clamps `δρ_damp` before null propagation |

> **INV-003 enforcement.** `ρ(Φ) = 0` always triggers FM-002 (Field Null).
> `f_Dampen` must never allow `ρ(Φ)` to reach 0. `ρ(Φ)_floor` is the
> last line of defense. Default `ρ(Φ)_floor = 0.05`.

### 2.3 Asymmetry with f_Emit

| Property | f_Emit | f_Dampen |
|---|---|---|
| Direction | ρ(Φ) ↑ | ρ(Φ) ↓ |
| Blocking failure | FM-010 (ceiling) | FM-009 (floor / cascade) |
| Energy relationship | consumes E_emit | recovers E_damp (or dissipates) |
| Risk profile | runaway saturation | cascade null propagation |
| Ceiling check | `check_emit_ceiling` (PRIM:017) | `check_floor` (PRIM:019) |

### 2.4 Cascade Propagation Model

When `ρ(Φ)` on node `A` is driven to `ρ(Φ)_floor` (or below without the guard),
the null signal can propagate across GravityGraph edges to adjacent attractor nodes.
Each adjacent node `A_i` that receives the null signal evaluates FM-002. If
`ρ(Φ_i) = 0` results, that node's FM-002 fires and the cascade propagates further.

```
A → FM-002 → A_1 (FM-002?) → A_2 (FM-002?) → ... [cascade front]
```

`cascade_guard = true` breaks this propagation by clamping `δρ_damp` such that
`ρ(Φ)` on `A` never reaches `ρ(Φ)_floor`. When `cascade_guard = false`, the operator
accepts cascade risk — FM-009 may fire.

---

<!-- §3 TRIADIC EQUATION -->
# §3 Triadic Equation (Dampen Context)

```
G = F_freq · F_fluid · F_force          [INV-001 — triadic inseparability]

f_Dampen acts exclusively on F_freq via ρ(Φ):

  F_freq_new = F_freq(ρ(Φ) − ρ(Φ)_delta_damp)

  where ρ(Φ)_delta_damp = min(δρ_damp,  ρ(Φ) − ρ(Φ)_floor)

Dampened field operator:
  F_damp  =  (δρ_damp · k_damp)  /  (r_damp · ρ(Φ))

  k_damp    ∈ ℝ₊   — dampening gain constant (calibrated per attractor class)
  δρ_damp   ∈ (0, ρ(Φ) − ρ(Φ)_floor]   — requested suppression magnitude
  r_damp    ∈ (0, r_capture]             — suppression radius
  ρ(Φ)      — current field density before suppression (denominator: non-zero by INV-003)

Energy recovered (or thermally dissipated):
  E_damp  =  M_A · ρ(Φ)_delta_damp · r_damp² · k_cost_damp

  k_cost_damp ∈ ℝ₊   — cost coefficient (may be < 1 for passive dissipation,
                          > 1 for active pumping against field pressure)

Note: G decreases after suppression. F_fluid and F_force are unmodified.
      The triadic product G = F_freq_new · F_fluid · F_force is reduced.
```

---

<!-- §4 OPERATOR REGISTRY -->
# §4 Operator Registry

<!-- op-registry: f_Dampen -->

## 4.1 Primary Operator

| Symbol | Type | Status | Description |
|---|---|---|---|
| `F_damp` | Operator | 🟢 frozen | Dampened field output: `(δρ_damp · k_damp) / (r_damp · ρ(Φ))` |

## 4.2 Derived Quantities

| Symbol | Type | Status | Expression |
|---|---|---|---|
| `ρ(Φ)_delta_damp` | Derived | 🟢 frozen | `min(δρ_damp, ρ(Φ) − ρ(Φ)_floor)` — clamped suppression magnitude |
| `ρ(Φ)_floor` | Parameter | 🟢 frozen | Minimum allowable `ρ(Φ)` after suppression (default `0.05`) |
| `r_damp` | Parameter | 🟢 frozen | Suppression radius; must satisfy `r_damp ∈ (0, r_capture]` |
| `E_damp` | Derived | 🟢 frozen | `M_A · ρ(Φ)_delta_damp · r_damp² · k_cost_damp` — energy budget |
| `cascade_guard` | Flag/Parameter | 🟢 frozen | Boolean; `true` clamps `δρ_damp` to prevent null propagation |

## 4.3 State Flags

| Flag | Status | Meaning |
|---|---|---|
| `DAMPEN_ACTIVE` | 🟢 frozen | `suppress_field` is currently executing |
| `DAMPEN_FLOOR_APPROACHED` | 🟢 frozen | `ρ(Φ) < ρ(Φ)_floor + ε_damp` — approaching minimum headroom |
| `DAMPEN_CASCADE` | 🟢 frozen | FM-009 cascade detected; null signal propagated to ≥ 1 adjacent node |

## 4.4 Constants

| Symbol | Typical Value | Description |
|---|---|---|
| `k_damp` | calibrated | Dampening gain; attractor-class-specific |
| `k_cost_damp` | 0.5 – 2.0 | Energy cost coefficient per unit of `ρ(Φ)_delta_damp` |
| `ε_damp` | 0.02 | Floor proximity threshold for `DAMPEN_FLOOR_APPROACHED` |
| `ρ(Φ)_floor` | 0.05 (default) | Hard lower bound; operator may set higher |

---

<!-- §5 DAMPENING CONDITIONS -->
# §5 Dampening Conditions

All four conditions are conjunctive. Suppression is only executed when all pass.

<!-- conditions: DAMP-C -->

## DAMP-C-1 — Floor Bound

```
ρ(Φ) − δρ_damp  ≥  ρ(Φ)_floor

If violated: clamp δρ_damp ← ρ(Φ) − ρ(Φ)_floor
             set DAMPEN_FLOOR_APPROACHED
             if cascade_guard = true → proceed with clamped value
             if cascade_guard = false → evaluate FM-009 risk before proceeding
```

**Rationale.** INV-003 requires `ρ(Φ) > 0` at all times. The floor is the engineered
margin above zero. Reaching the floor without `cascade_guard` is the proximate cause
of FM-009.

## DAMP-C-2 — Radius Bound

```
r_damp  ∈  (0, r_capture]

If r_damp = 0 → reject: undefined suppression radius (division by zero in F_damp)
If r_damp > r_capture → clamp to r_capture and emit warning
```

**Rationale.** Suppression cannot extend beyond the attractor's established capture
radius. Suppression within a sub-radius `r_damp < r_capture` is valid and produces
a locally weaker inner field, useful for graduated orbital adjustment.

## DAMP-C-3 — Active Orbit Guard

```
If ORBIT_LOCKED on any E bound to A:
    allowed_delta = ρ(Φ) − max(ρ(Φ)_floor, ρ_orbit_minimum(E))
    clamp δρ_damp ← min(δρ_damp, allowed_delta)

ρ_orbit_minimum(E) = minimum ρ(Φ) sustaining SC-4 (β ≥ 1.0) for E's current orbit
```

**Rationale.** Dampening below `ρ_orbit_minimum` would cause `β < 1.0` (INV-004),
triggering flyby for a currently bound element. Active orbit guard prevents
inadvertent unbinding.

## DAMP-C-4 — Cascade Guard Check

```
If cascade_guard = true:
    proceed with clamped δρ_damp (DAMP-C-1 already enforces floor)
If cascade_guard = false:
    invoke check_cascade_risk(A, δρ_damp, graph)  [PRIM:020]
    if CascadeRisk.level = HIGH → raise FM-009 warning and require operator override
    if CascadeRisk.level = MEDIUM → emit DAMPEN_FLOOR_APPROACHED and proceed
    if CascadeRisk.level = LOW → proceed
```

**Rationale.** The cascade guard is the primary systemic safety mechanism.
Operators running `f_Dampen` with `cascade_guard = false` accept explicit responsibility
for graph-wide null propagation risk.

---

<!-- §6 FAILURE MODES -->
# §6 Failure Modes

<!-- failure-modes: f_Dampen -->

## FM-009 — Dampen Cascade

| Field | Value |
|---|---|
| ID | FM-009 |
| Name | Dampen Cascade |
| Severity | **fatal** |
| Frozen in | f_Dampen.md (SES-20260813-DAMPEN-001) |
| Handled in | f_Dampen.md |
| Trigger | `ρ(Φ)` on `A` reaches `ρ(Φ)_floor` and null signal propagates to ≥ 1 adjacent node |
| Effect | Sets `DAMPEN_CASCADE`; triggers FM-002 (Field Null) on each affected adjacent node; each FM-002 may trigger further FM-009 on that node's neighbors — cascade front propagates until a node with `cascade_guard = true` or no adjacent nodes |
| Recovery | None — FM-009 is terminal for each affected node. Composite rebuild via `f_Collapse` Path B (C_node) is the only structural recourse. |
| Prevention | `cascade_guard = true` on all nodes in a shared GravityGraph segment |

### FM-009 Cascade Propagation Algorithm

```
procedure propagate_cascade(origin: Node, graph: GravityGraph):
    queue ← [origin]
    visited ← {}
    while queue is not empty:
        node ← queue.pop()
        if node in visited: continue
        visited.add(node)
        trigger FM-002(node)                    # Field Null on this node
        set node.state = DAMPEN_CASCADE
        set node.state = FIELD_NULL             # terminal — INV-006
        for neighbor in graph.neighbors(node):
            if neighbor.cascade_guard = true:
                # neighbor protected — cascade stops here
                emit warning("CASCADE_HALTED at neighbor " + neighbor.id)
            else:
                queue.append(neighbor)
```

> **INV-006 enforcement.** Each node that reaches FM-009 enters a terminal state.
> Terminal states are irreversible. The cascade cannot be reversed in flight.

## FM-002 Reference — Field Null (Secondary Target)

FM-002 is defined in `f_Capture.md` and `f_Field.md`. In the context of `f_Dampen`,
FM-002 is the *per-node* failure that FM-009 propagates to adjacent nodes.
`f_Dampen` does not redefine FM-002; it references it as a cascade target.

```
FM-002 trigger (via FM-009):  ρ(Φ_neighbor) → 0 due to null signal propagation
Resolution: none (terminal) — same as direct FM-002
```

---

<!-- §7 ENGINEERING PRIMITIVES -->
# §7 Engineering Primitives

<!-- primitives: PRIM:018 PRIM:019 PRIM:020 -->

## PRIM:018 — suppress_field (impure)

```
PRIM:018  suppress_field
Type      : Impure — modifies A.ρ(Φ), emits flags, may trigger FM-009
Defined   : f_Dampen.md (SES-20260813-DAMPEN-001)
Status    : 🟢 frozen
Signature : suppress_field(A, δρ_damp, r_damp,
                            ρ_floor=0.05, cascade_guard=True,
                            k_damp=1.0, k_cost_damp=1.0,
                            graph=None) → DampenResult
```

```python
@dataclass
class DampenResult:
    success:          bool
    ρ_before:         float          # ρ(Φ) before suppression
    ρ_after:          float          # ρ(Φ) after suppression
    ρ_delta_applied:  float          # actual ρ(Φ)_delta_damp applied (may be clamped)
    E_damp:           float          # energy recovered / dissipated
    flags:            list[str]      # DAMPEN_ACTIVE, DAMPEN_FLOOR_APPROACHED, DAMPEN_CASCADE
    fm_triggered:     list[str]      # FM-009 and/or FM-002 if cascade
    cascade_affected: list[NodeID]   # nodes reached by cascade (empty if none)
    abort_reason:     str | None     # None on success

def suppress_field(
    A,                          # attractor node (mutable)
    δρ_damp:  float,            # requested suppression magnitude
    r_damp:   float,            # suppression radius
    ρ_floor:  float = 0.05,     # floor bound
    cascade_guard: bool = True, # cascade protection flag
    k_damp:   float = 1.0,      # dampening gain constant
    k_cost_damp: float = 1.0,   # energy cost coefficient
    graph = None                # GravityGraph (required if cascade_guard=False)
) -> DampenResult:

    result = DampenResult(flags=["DAMPEN_ACTIVE"], fm_triggered=[], cascade_affected=[])
    result.ρ_before = A.ρ_Φ

    # ── DAMP-C-2: Radius Bound ───────────────────────────────────────────────
    if r_damp <= 0:
        return DampenResult(success=False, abort_reason="DAMP-C-2: r_damp must be > 0")
    if r_damp > A.r_capture:
        r_damp = A.r_capture        # clamp with warning
        emit_warning("r_damp clamped to r_capture")

    # ── DAMP-C-3: Active Orbit Guard ─────────────────────────────────────────
    ρ_orbit_min = compute_orbit_floor(A)     # min ρ(Φ) sustaining all active orbits
    effective_floor = max(ρ_floor, ρ_orbit_min)

    # ── DAMP-C-1: Floor Bound ────────────────────────────────────────────────
    floor_result = check_floor(A.ρ_Φ, δρ_damp, effective_floor)   # PRIM:019
    ρ_delta_damp = floor_result.clamped_delta

    if floor_result.floor_approached:
        result.flags.append("DAMPEN_FLOOR_APPROACHED")

    # ── DAMP-C-4: Cascade Guard Check ────────────────────────────────────────
    if not cascade_guard:
        if graph is None:
            return DampenResult(success=False,
                abort_reason="cascade_guard=False requires graph argument")
        risk = check_cascade_risk(A, ρ_delta_damp, graph)      # PRIM:020
        if risk.level == "HIGH":
            # FM-009 imminent — require explicit operator override
            emit_warning("FM-009 HIGH CASCADE RISK — set override=True to proceed")
            return DampenResult(success=False,
                abort_reason="FM-009 HIGH: cascade guard required")

    # ── Apply suppression ────────────────────────────────────────────────────
    ρ_new = A.ρ_Φ - ρ_delta_damp
    if ρ_new <= 0:
        # Should not reach here if DAMP-C-1 ran correctly — fatal guard
        trigger_FM009(A, graph)
        result.fm_triggered.append("FM-009")
        result.fm_triggered.append("FM-002")
        result.flags.append("DAMPEN_CASCADE")
        result.success = False
        result.abort_reason = "FM-009: ρ(Φ) reached 0 — cascade triggered"
        return result

    A.ρ_Φ = ρ_new

    # ── Compute energy ───────────────────────────────────────────────────────
    E_damp = A.M_A * ρ_delta_damp * (r_damp ** 2) * k_cost_damp

    # ── F_damp operator value ────────────────────────────────────────────────
    F_damp_val = (ρ_delta_damp * k_damp) / (r_damp * A.ρ_Φ)   # ρ(Φ) post-suppression

    # ── Finalise result ──────────────────────────────────────────────────────
    result.success         = True
    result.ρ_after         = A.ρ_Φ
    result.ρ_delta_applied = ρ_delta_damp
    result.E_damp          = E_damp
    result.flags.remove("DAMPEN_ACTIVE")   # operation complete — clear active flag

    emit_event("DAMPEN_COMPLETE", {
        "node": A.id,
        "ρ_before": result.ρ_before,
        "ρ_after":  result.ρ_after,
        "F_damp":   F_damp_val,
        "E_damp":   E_damp
    })

    return result
```

**Side effects:**
- Writes `A.ρ_Φ` (F_freq node — the only write target)
- Emits `DAMPEN_ACTIVE` at start, clears on completion
- Emits `DAMPEN_FLOOR_APPROACHED` if floor proximity threshold crossed
- Emits `DAMPEN_CASCADE` + calls `propagate_cascade` if FM-009 fires
- Emits `DAMPEN_COMPLETE` event to GravityGraph event bus

**Idempotency.** Not idempotent — each call writes `A.ρ_Φ`. Calling with `δρ_damp = 0`
is a no-op (clamped by DAMP-C-1 since `ρ(Φ) − 0 = ρ(Φ)`, delta = 0 applied).

---

## PRIM:019 — check_floor (pure)

```
PRIM:019  check_floor
Type      : Pure — no side effects
Defined   : f_Dampen.md (SES-20260813-DAMPEN-001)
Status    : 🟢 frozen
Signature : check_floor(ρ_current, δρ_requested, ρ_floor) → FloorResult
```

```python
@dataclass
class FloorResult:
    clamped_delta:    float    # actual δρ to apply (may be < δρ_requested)
    floor_approached: bool     # True if headroom < ε_damp after clamp
    headroom:         float    # ρ_current − ρ_floor (before clamp)
    was_clamped:      bool     # True if δρ_requested was reduced

ε_damp = 0.02   # module constant

def check_floor(
    ρ_current:    float,
    δρ_requested: float,
    ρ_floor:      float
) -> FloorResult:

    headroom = ρ_current - ρ_floor

    if headroom <= 0:
        # Already at or below floor — no suppression possible
        return FloorResult(
            clamped_delta    = 0.0,
            floor_approached = True,
            headroom         = headroom,
            was_clamped      = True
        )

    clamped = min(δρ_requested, headroom)
    was_clamped = clamped < δρ_requested

    # Headroom remaining after applying clamped delta
    remaining = ρ_current - clamped - ρ_floor
    floor_approached = remaining < ε_damp

    return FloorResult(
        clamped_delta    = clamped,
        floor_approached = floor_approached,
        headroom         = headroom,
        was_clamped      = was_clamped
    )
```

**Composition.** `check_floor` mirrors `check_emit_ceiling` (PRIM:017) exactly in
structure. Where PRIM:017 tests headroom below `ρ(Φ) = 1.0`, PRIM:019 tests headroom
above `ρ(Φ)_floor`. Both are pure and callable without side effects.

---

## PRIM:020 — check_cascade_risk (pure / diagnostic)

```
PRIM:020  check_cascade_risk
Type      : Pure / Diagnostic — no side effects; reads graph state
Defined   : f_Dampen.md (SES-20260813-DAMPEN-001)
Status    : 🟢 frozen
Signature : check_cascade_risk(A, δρ_damp, graph) → CascadeRisk
```

```python
@dataclass
class CascadeRisk:
    level:             str           # "LOW" | "MEDIUM" | "HIGH"
    at_floor_after:    bool          # True if A itself reaches ρ_floor after δρ_damp
    vulnerable_neighbors: list[str]  # neighbor node IDs with cascade_guard=False AND low ρ(Φ)
    cascade_depth_est: int           # estimated propagation depth (0 if LOW)
    notes:             list[str]     # diagnostic messages

def check_cascade_risk(A, δρ_damp, graph) -> CascadeRisk:

    notes = []
    vulnerable = []
    ρ_after_A = A.ρ_Φ - δρ_damp

    # Check if A itself hits the floor
    at_floor = ρ_after_A <= A.ρ_floor

    # Walk immediate neighbors
    for neighbor in graph.neighbors(A):
        if neighbor.cascade_guard:
            continue    # protected — not vulnerable
        if neighbor.ρ_Φ <= neighbor.ρ_floor + ε_damp:
            vulnerable.append(neighbor.id)
            notes.append(f"Neighbor {neighbor.id}: ρ(Φ)={neighbor.ρ_Φ:.3f} near floor")

    # Estimate cascade depth via BFS with guard-stop
    depth = 0
    if at_floor and len(vulnerable) > 0:
        depth = estimate_cascade_depth(A, graph)   # BFS stopping at cascade_guard=True nodes

    # Classify risk
    if at_floor and depth >= 3:
        level = "HIGH"
    elif at_floor or len(vulnerable) > 0:
        level = "MEDIUM"
    else:
        level = "LOW"

    return CascadeRisk(
        level                = level,
        at_floor_after       = at_floor,
        vulnerable_neighbors = vulnerable,
        cascade_depth_est    = depth,
        notes                = notes
    )
```

**Diagnostic use.** PRIM:020 is safe to call repeatedly without side effects. It is
called by `suppress_field` (PRIM:018) whenever `cascade_guard = False`, and may also
be called independently by operators for pre-flight risk assessment before any
suppression call.

---

<!-- §8 CANONICAL EXAMPLES -->
# §8 Canonical Examples

<!-- examples: f_Dampen -->

## Example 1 — Controlled Saturation Drain

**Scenario.** Attractor `A_sat` has reached `ρ(Φ) = 0.93` after multiple `f_Emit`
calls. FM-010 (Amplify Runaway) is approaching (`ρ(Φ) < 1.0` but headroom is thin).
The operator drains excess field density to `0.70` before the next emission cycle.

**Initial state.**
```
A_sat.ρ_Φ         = 0.93
A_sat.r_capture   = 8.0
A_sat.M_A         = 5.0
ρ_floor           = 0.05   (default)
cascade_guard     = True
```

**Operator call.**
```python
result = suppress_field(
    A           = A_sat,
    δρ_damp     = 0.23,     # target: 0.93 − 0.23 = 0.70
    r_damp      = 8.0,      # full capture radius
    ρ_floor     = 0.05,
    cascade_guard = True,
    k_damp      = 1.0,
    k_cost_damp = 0.8       # passive dissipation — partial energy recovery
)
```

**DAMP-C evaluation.**
```
DAMP-C-1 (Floor Bound):
  headroom = 0.93 − 0.05 = 0.88
  0.23 ≤ 0.88 → no clamp needed
  remaining after: 0.70 − 0.05 = 0.65 >> ε_damp → DAMPEN_FLOOR_APPROACHED not set

DAMP-C-2 (Radius Bound):
  r_damp = 8.0 = r_capture → valid (boundary case allowed)

DAMP-C-3 (Active Orbit Guard):
  No ORBIT_LOCKED elements on A_sat → ρ_orbit_min = 0.0 → no additional clamp

DAMP-C-4 (Cascade Guard):
  cascade_guard = True → skip PRIM:020 risk check
```

**Result.**
```
ρ_before         = 0.93
ρ_after          = 0.70
ρ_delta_applied  = 0.23
E_damp           = 5.0 × 0.23 × 64.0 × 0.8  =  58.88 units  (recovered)
F_damp           = (0.23 × 1.0) / (8.0 × 0.70)  =  0.041
flags            = []   (DAMPEN_ACTIVE cleared; no floor approach)
fm_triggered     = []
cascade_affected = []
success          = True
```

**Post-state.** `A_sat.ρ_Φ = 0.70`. FM-010 headroom restored to 0.30. Subsequent
`f_Emit` calls may proceed without EMIT_CEILING_APPROACHED warning.

---

## Example 2 — Floor Approach with Orbit Guard Active

**Scenario.** Attractor `A_heavy` has one bound element `E_moon` in a stable circular
orbit. The operator attempts aggressive dampening (`δρ_damp = 0.60`) but the orbit
guard prevents unbinding `E_moon`.

**Initial state.**
```
A_heavy.ρ_Φ       = 0.72
A_heavy.r_capture = 10.0
A_heavy.M_A       = 12.0
E_moon.β          = 1.35   (ORBIT_LOCKED, stable)
ρ_orbit_minimum   = 0.40   (minimum ρ(Φ) sustaining β ≥ 1.0 for E_moon)
ρ_floor           = 0.05
cascade_guard     = True
```

**Operator call.**
```python
result = suppress_field(
    A           = A_heavy,
    δρ_damp     = 0.60,     # would produce ρ(Φ) = 0.12 — below ρ_orbit_min
    r_damp      = 5.0,      # inner half of capture radius
    ρ_floor     = 0.05,
    cascade_guard = True,
    k_cost_damp = 1.2
)
```

**DAMP-C evaluation.**
```
DAMP-C-3 (Active Orbit Guard):
  ρ_orbit_min = 0.40
  effective_floor = max(0.05, 0.40) = 0.40
  headroom = 0.72 − 0.40 = 0.32
  δρ_damp clamped: 0.60 → 0.32

DAMP-C-1 (Floor Bound, with effective_floor = 0.40):
  remaining after: 0.72 − 0.32 = 0.40 = effective_floor
  floor_approached = True  (remaining − ρ_floor = 0.40 − 0.40 = 0.00 < ε_damp)
  → set DAMPEN_FLOOR_APPROACHED

DAMP-C-2 (Radius Bound):
  r_damp = 5.0 < r_capture = 10.0 → valid

DAMP-C-4: cascade_guard = True → no risk check needed
```

**Result.**
```
ρ_before         = 0.72
ρ_after          = 0.40
ρ_delta_applied  = 0.32   (clamped from 0.60)
E_damp           = 12.0 × 0.32 × 25.0 × 1.2  =  115.2 units
flags            = ["DAMPEN_FLOOR_APPROACHED"]
fm_triggered     = []
cascade_affected = []
success          = True
```

**Post-state.** `A_heavy.ρ_Φ = 0.40`. `E_moon` retains β = 1.35 (orbit intact —
`ρ(Φ)` at minimum sustaining value). Further dampening blocked until `E_moon` is
released or its orbit decays naturally via `f_Decay`. Operator receives
`DAMPEN_FLOOR_APPROACHED` as a notification that the orbit guard ceiling has been reached.

---

## Example 3 — FM-009 Dampen Cascade (Fatal)

**Scenario.** Graph segment with three nodes: `A_hub`, `A_left`, `A_right`.
`A_hub` has `cascade_guard = False` (operator disabled it for a controlled test).
`A_left` also has `cascade_guard = False`. `A_right` has `cascade_guard = True`.
The operator attempts to suppress `A_hub` by `δρ_damp = 0.90`, well beyond the
floor, without cascade guard.

**Initial state.**
```
A_hub.ρ_Φ    = 0.15   cascade_guard = False
A_left.ρ_Φ  = 0.08   cascade_guard = False   (already near floor)
A_right.ρ_Φ = 0.60   cascade_guard = True    (protected)
ρ_floor (all) = 0.05
graph.edges: A_hub ↔ A_left, A_hub ↔ A_right
```

**Operator call.**
```python
result = suppress_field(
    A             = A_hub,
    δρ_damp       = 0.90,
    r_damp        = A_hub.r_capture,
    ρ_floor       = 0.05,
    cascade_guard = False,
    graph         = gravity_graph
)
```

**DAMP-C-4 risk check (PRIM:020).**
```
ρ_after_A_hub = 0.15 − 0.90 = −0.75  (below zero — at_floor = True)
Neighbors:
  A_left: cascade_guard=False, ρ(Φ)=0.08 ≤ floor+ε = 0.07 → vulnerable
  A_right: cascade_guard=True → protected
cascade_depth_est = 2 (A_hub → A_left; A_left has no further unprotected neighbors)
level = HIGH
→ FM-009 HIGH warning raised; operator must set override=True to proceed
```

*[For this example, assume operator passes override=True — acknowledging risk.]*

**Cascade execution.**
```
A_hub.ρ_Φ = 0.15 − 0.10 = 0.05   (clamped to floor — but cascade already triggered)
FM-009 fires on A_hub:
  propagate_cascade(A_hub, graph):
    trigger FM-002(A_hub)  → A_hub.state = FIELD_NULL (terminal)
    neighbors: [A_left, A_right]
      A_left: cascade_guard=False → queue
      A_right: cascade_guard=True → HALT ("CASCADE_HALTED at A_right")
    trigger FM-002(A_left)  → A_left.state = FIELD_NULL (terminal)
    A_left neighbors: [A_hub (visited)]  → stop
```

**Result.**
```
ρ_before         = 0.15
ρ_after          = 0.05   (floor — but FM-009 fired before write)
ρ_delta_applied  = 0.10   (partial — cascade interrupted full application)
E_damp           = partial (not meaningful — node terminal)
flags            = ["DAMPEN_CASCADE"]
fm_triggered     = ["FM-009", "FM-002"]
cascade_affected = ["A_hub", "A_left"]
success          = False
abort_reason     = "FM-009: cascade propagated to 1 adjacent node"
```

**Post-state.**
- `A_hub` → FIELD_NULL (terminal — INV-006)
- `A_left` → FIELD_NULL (terminal — INV-006)
- `A_right` → unaffected (`cascade_guard = True` halted propagation)
- All orbits on `A_hub` and `A_left` → unbound (FM-002 unbinds all captured elements)
- Structural recourse: `f_Collapse` Path B (C_node) may reconstitute if `|M_E−M_A| < m_parity`

---

## Example 4 — Orbital Stabilization via Controlled Dampening

**Scenario.** Attractor `A_giant` has been emitting aggressively — `ρ(Φ) = 0.88` —
causing bound element `E_probe` to have an excessively high β = 4.2. This creates
an overly tight orbit that is accelerating decay (via `f_Decay`). The operator
reduces `ρ(Φ)` to bring β closer to 1.5, extending orbital lifetime.

**Initial state.**
```
A_giant.ρ_Φ       = 0.88
A_giant.r_capture = 20.0
A_giant.M_A       = 30.0
E_probe.β         = 4.20   (ORBIT_LOCKED, excessive binding — rapid decay)
E_probe.d_bind    = 12.0
ρ_orbit_minimum   = 0.30   (minimum for β ≥ 1.0 on E_probe)
target_ρ          = 0.55   (operator-calculated target for β ≈ 1.5)
δρ_damp_requested = 0.88 − 0.55 = 0.33
cascade_guard     = True
```

**Pre-flight check — PRIM:019.**
```python
floor_result = check_floor(
    ρ_current    = 0.88,
    δρ_requested = 0.33,
    ρ_floor      = max(0.05, 0.30)   # effective floor = 0.30 (orbit guard)
)
# headroom = 0.88 − 0.30 = 0.58
# clamped  = min(0.33, 0.58) = 0.33   ← no clamp needed
# remaining = 0.88 − 0.33 − 0.30 = 0.25 > ε_damp → no floor approach
```

**Operator call.**
```python
result = suppress_field(
    A             = A_giant,
    δρ_damp       = 0.33,
    r_damp        = 20.0,      # full radius — uniform field reduction
    ρ_floor       = 0.05,
    cascade_guard = True,
    k_damp        = 1.0,
    k_cost_damp   = 0.6        # passive dissipation
)
```

**Result.**
```
ρ_before         = 0.88
ρ_after          = 0.55
ρ_delta_applied  = 0.33
E_damp           = 30.0 × 0.33 × 400.0 × 0.6  =  2376.0 units  (recovered)
F_damp           = (0.33 × 1.0) / (20.0 × 0.55)  =  0.030
flags            = []
fm_triggered     = []
success          = True
```

**Post-state analysis.**
```
G_new = F_freq(ρ=0.55) · F_fluid · F_force
β_new ≈ 4.20 × (0.55 / 0.88) = 4.20 × 0.625 ≈ 2.63   (improved; still > 1.0)

Operator notes: β = 2.63 is better but still elevated.
Second controlled dampen to ρ(Φ) = 0.42 would bring β ≈ 2.0.
Recommend f_Decay monitoring cycle before next suppress_field call.
```

**Safe iterative dampening pattern.**
```python
# Iterative stabilization — dampen in small steps, monitor β each cycle
target_β   = 1.5
tolerance  = 0.1
max_steps  = 5

for step in range(max_steps):
    β_current = compute_β(A_giant, E_probe)
    if abs(β_current - target_β) < tolerance:
        break
    # Small step: reduce ρ(Φ) by 5% of current value per cycle
    δρ_step = A_giant.ρ_Φ * 0.05
    result = suppress_field(A_giant, δρ_step, r_damp=A_giant.r_capture,
                             cascade_guard=True)
    if not result.success:
        break
    run_decay_cycle(A_giant)    # allow f_Decay to re-evaluate after each step
```

This iterative pattern mirrors the `sustained_emission_loop` in `f_Emit.md` §8
Example 4, and is the recommended approach when precise β targeting is required.

---

<!-- §9 CROSS-MODULE REFERENCES -->
# §9 Cross-Module References

<!-- cross-refs: f_Dampen -->

## 9.1 Reads From (Inputs)

| Symbol | Source File | Usage in f_Dampen |
|---|---|---|
| `ρ(Φ)` | f_Field.md | Current field density — primary write target |
| `r_capture` | f_Field.md | Upper bound for `r_damp` (DAMP-C-2) |
| `v_escape(A)` | f_Field.md | Implicitly affected by `ρ(Φ)` change — not directly read |
| `M_A` | f_Force.md | Used in `E_damp` computation |
| `β` | f_Force.md | Orbit guard (DAMP-C-3) reads `β` to compute `ρ_orbit_minimum` |
| `capacity_remaining` | f_Frame.md | Not directly read — unaffected by dampening |
| `GravityGraph` | f_Frame.md | Required for cascade propagation (FM-009) |
| `FM-010` | f_Emit.md | Shared ceiling awareness — `f_Dampen` recovers headroom below FM-010 trigger |

## 9.2 Writes To (Outputs)

| Symbol | Target | Mechanism |
|---|---|---|
| `ρ(Φ)` | `A.ρ_Φ` | `suppress_field` (PRIM:018) — only sanctioned downward write |
| `DAMPEN_ACTIVE` | event bus | Set at start of `suppress_field`; cleared on completion |
| `DAMPEN_FLOOR_APPROACHED` | event bus | Set when headroom < `ε_damp` |
| `DAMPEN_CASCADE` | event bus + node state | Set when FM-009 fires |

## 9.3 Failure Mode Interactions

| FM | Direction | Mechanism |
|---|---|---|
| FM-009 Dampen Cascade | Owns/triggers | Fatal: null propagation to adjacent nodes |
| FM-002 Field Null | Secondary target | FM-009 triggers FM-002 on each cascade-affected node |
| FM-010 Amplify Runaway | Upstream | `f_Dampen` is the recovery action when FM-010 blocking occurs |
| FM-004 Resonance Drift | Downstream | Dampening that destabilizes ω_res may trigger FM-004 |
| FM-005 Decay Spiral | Downstream | Excessive dampening weakening β may accelerate decay |

## 9.4 GravityGraph Events Emitted

| Event | Trigger | Payload |
|---|---|---|
| `DAMPEN_COMPLETE` | Successful suppression | `{node, ρ_before, ρ_after, F_damp, E_damp}` |
| `DAMPEN_FLOOR_APPROACHED` | Floor proximity | `{node, ρ_Φ, headroom_remaining}` |
| `CASCADE_HALTED` | cascade_guard blocks propagation | `{protected_node, origin_node}` |
| `FM_009_TRIGGERED` | Cascade fires | `{origin, cascade_front, affected_nodes}` |

## 9.5 OPERATORS.md Update Required

The following symbols defined in this file must be updated to 🟢 frozen status
in `OPERATORS.md` when this file is committed:

```
F_damp                  → 🟢 frozen (f_Dampen.md §4)
ρ(Φ)_floor             → 🟢 frozen (f_Dampen.md §4)
r_damp                  → 🟢 frozen (f_Dampen.md §4)
δρ_damp                 → 🟢 frozen (f_Dampen.md §4)
cascade_guard           → 🟢 frozen (f_Dampen.md §4)
k_damp                  → 🟢 frozen (f_Dampen.md §4)
k_cost_damp             → 🟢 frozen (f_Dampen.md §4)
DAMPEN_ACTIVE           → 🟢 frozen (f_Dampen.md §4)
DAMPEN_FLOOR_APPROACHED → 🟢 frozen (f_Dampen.md §4)
DAMPEN_CASCADE          → 🟢 frozen (f_Dampen.md §4)
FM-009                  → 🟢 frozen (f_Dampen.md §6)
PRIM:018 suppress_field        → 🟢 frozen (f_Dampen.md §7)
PRIM:019 check_floor           → 🟢 frozen (f_Dampen.md §7)
PRIM:020 check_cascade_risk    → 🟢 frozen (f_Dampen.md §7)
```

---

<!-- §10 DOCUMENT METADATA -->
# §10 Document Metadata

<!-- metadata: f_Dampen -->

## 10.1 INV Compliance Table

| Invariant | ID | Compliance | Notes |
|---|---|---|---|
| G = F_freq · F_fluid · F_force | INV-001 | ✅ | `f_Dampen` modifies F_freq only; product G reduces proportionally |
| f_Capture(E,A,Φ) → Ω frozen | INV-002 | ✅ | Not modified by this file |
| ρ(Φ) = 0 triggers FM-002 | INV-003 | ✅ | `ρ(Φ)_floor` and DAMP-C-1 enforce non-zero floor; FM-009 triggers FM-002 on breach |
| β < 1.0 produces flyby | INV-004 | ✅ | DAMP-C-3 prevents dampening below `ρ_orbit_minimum` |
| SC conjunction | INV-005 | ✅ | All 5 SCs evaluated before suppression; DAMP-C-3 specifically guards SC-2 and SC-4 |
| Terminal states irreversible | INV-006 | ✅ | FM-009 cascade sets FIELD_NULL — no recovery path within f_Dampen |
| f_Source.md read-only | INV-007 | ✅ | Not referenced by this file |
| Operator eval order normative | INV-008 | ✅ | DAMP-C-1 through DAMP-C-4 executed in fixed sequence (§5) |
| OPERATORS.md is symbol authority | INV-009 | ✅ | §9.5 lists all symbols requiring OPERATORS.md update |
| Frozen symbols no rename | INV-010 | ✅ | All 14 frozen symbols listed in YAML frontmatter |

## 10.2 Primitive Registry (This File)

| ID | Name | Type | Signature |
|---|---|---|---|
| PRIM:018 | suppress_field | Impure | `(A, δρ_damp, r_damp, ρ_floor, cascade_guard, k_damp, k_cost_damp, graph) → DampenResult` |
| PRIM:019 | check_floor | Pure | `(ρ_current, δρ_requested, ρ_floor) → FloorResult` |
| PRIM:020 | check_cascade_risk | Pure/Diagnostic | `(A, δρ_damp, graph) → CascadeRisk` |

**Cumulative primitive count after this file: PRIM:001 – PRIM:020 (20 primitives frozen)**

## 10.3 Operator Registry (This File)

| Symbol | Class | Expression |
|---|---|---|
| `F_damp` | Primary | `(δρ_damp · k_damp) / (r_damp · ρ(Φ))` |
| `ρ(Φ)_delta_damp` | Derived | `min(δρ_damp, ρ(Φ) − ρ(Φ)_floor)` |
| `E_damp` | Derived | `M_A · ρ(Φ)_delta_damp · r_damp² · k_cost_damp` |

## 10.4 Failure Mode Registry (This File)

| ID | Name | Severity | Trigger |
|---|---|---|---|
| FM-009 | Dampen Cascade | fatal | `ρ(Φ)` reaches floor; null propagates to adjacent node |

**Cumulative FM count: FM-001 through FM-010 (10 FMs — all frozen)**

