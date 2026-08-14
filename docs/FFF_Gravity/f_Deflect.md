# `f_Deflect` — Heading Deflection Primitive

```
session_id: SES-20260813-DEFLECT-001
file: docs/FFF_Gravity/f_Deflect.md
module: FFF_Gravity
wave: 3
wave_position: 8 of 8
node: F_force
role: Engineering primitive — modifies approach heading (v_approach direction) without changing magnitude
status: canonical
version: 1.0.0
created: 2026-08-13
authors:
  - umaywant2
depends_on:
  - docs/FFF_Gravity/f_Force.md        # canonical — defines v_approach, heading_delta stub
  - docs/FFF_Gravity/f_Field.md        # canonical — defines ρ(Φ), v_escape(A)
  - docs/FFF_Gravity/f_Frame.md        # canonical — defines r_capture, capacity_remaining
  - docs/FFF_Gravity/OPERATORS.md      # symbol authority
operators_introduced:
  - heading_delta   # frozen here — pending stub resolved from f_Force.md §4.3
  - r_deflect
  - deflect_cost
primitives_introduced:
  - PRIM:023        # redirect_force_node (Impure)
  - PRIM:024        # compute_deflection_cost (Pure)
failure_modes_active:
  - FM-001          # Overshoot — inherited from f_Force.md
  - FM-006          # Phantom Capture — inherited from f_Force.md
failure_modes_introduced: []
changelog:
  - version: 1.0.0
    date: 2026-08-13
    session: SES-20260813-DEFLECT-001
    author: umaywant2
    changes:
      - Initial canonical publication
      - Freezes heading_delta operator (resolves f_Force.md §4.3 stub)
      - Introduces r_deflect and deflect_cost operators
      - Introduces PRIM:023 redirect_force_node (Impure)
      - Introduces PRIM:024 compute_deflection_cost (Pure)
      - Wave 3 completion milestone — all 8 files canonical
      - Wave 4 fully unlocked
```

<!-- ============================================================
     f_Deflect.md — FFF_Gravity Module
     Wave 3 | File 8 of 8 | Node: F_force
     Session: SES-20260813-DEFLECT-001
     Status: CANONICAL
     Wave 3 FINAL — all 8 files complete upon this publication
     ============================================================ -->

> **F_force engineering primitive.**  
> Modifies the direction of `v_approach` via angular redirect.  
> Magnitude of `v_approach` is invariant across deflection.  
> Resolves the `heading_delta` pending stub declared in `f_Force.md §4.3`.

---

## §0 Session Context

<!-- SECTION: session_context | scope: this-file -->

| Field               | Value                                    |
|---------------------|------------------------------------------|
| Session ID          | `SES-20260813-DEFLECT-001`               |
| File                | `docs/FFF_Gravity/f_Deflect.md`          |
| Module              | FFF_Gravity                              |
| Wave                | 3 — final file (8 of 8)                  |
| Node                | F_force                                  |
| Authored            | 2026-08-13                               |
| Status              | Canonical                                |
| Prior session chain | SES-20260813-AMPLIFY-001 → this file     |

### §0.1 Purpose of This Session

This session produces the canonical `f_Deflect.md`. It is the **last Wave 3 file** and the **last engineering primitive** of the FFF_Gravity module's F_force node. Its central duty is to resolve the `heading_delta` pending stub referenced in `f_Force.md §4.3`, formalize the deflection geometry, and close Wave 3 by recording the completion milestone in §10.

### §0.2 Stub Resolution Record

```
f_Force.md §4.3 declared:
  heading_delta  [PENDING: defined in f_Deflect.md]

Resolution:
  This file (f_Deflect.md §4) freezes heading_delta.
  Freeze date: 2026-08-13
  Session: SES-20260813-DEFLECT-001
```

---

## §1 Module Identity

<!-- SECTION: module_identity | scope: this-file -->

### §1.1 Formal Signature

```
f_Deflect(v_approach, heading_delta, r_deflect) → new_v_approach_heading
```

| Parameter       | Type    | Description                                            |
|-----------------|---------|--------------------------------------------------------|
| `v_approach`    | vector  | Current approach velocity vector (magnitude preserved) |
| `heading_delta` | float   | Angular deviation in radians; positive = clockwise     |
| `r_deflect`     | float   | Deflection radius; distance at which redirect is applied |

| Return               | Type   | Description                                      |
|----------------------|--------|--------------------------------------------------|
| `new_v_approach_heading` | vector | Redirected heading; same magnitude as `v_approach` |

### §1.2 Triadic Position

```
G = F_freq · F_fluid · F_force
                         ↑
                    f_Deflect lives here.
                    It is a geometry-layer primitive
                    operating strictly within the F_force node.
```

| Node    | Function in G    | Deflect's Role                                |
|---------|------------------|-----------------------------------------------|
| F_freq  | Frequency field  | Provides ρ(Φ) — read-only in deflect context  |
| F_fluid | Binding medium   | Provides β — read-only in deflect context     |
| F_force | Force vector     | **Owner.** Deflect modifies heading here.     |

### §1.3 Companion Primitive Table (F_force Node)

| Primitive | Name                      | Type   | File          | Status    |
|-----------|---------------------------|--------|---------------|-----------|
| PRIM:001  | `apply_force_node`        | Impure | f_Force.md    | Frozen    |
| PRIM:002  | `compute_approach_velocity` | Pure | f_Force.md    | Frozen    |
| PRIM:013  | `evaluate_collapse_path`  | Pure   | f_Collapse.md | Frozen    |
| PRIM:014  | `execute_collapse`        | Impure | f_Collapse.md | Frozen    |
| **PRIM:023** | **`redirect_force_node`** | **Impure** | **f_Deflect.md** | **Frozen** |
| **PRIM:024** | **`compute_deflection_cost`** | **Pure** | **f_Deflect.md** | **Frozen** |

---

## §2 Canonical Description

<!-- SECTION: canonical_description | scope: this-file -->

### §2.1 What f_Deflect IS

`f_Deflect` is the heading-modification primitive of the F_force node. It takes an existing `v_approach` vector and rotates its direction by `heading_delta` radians while preserving the vector's scalar magnitude. The resulting `new_v_approach_heading` is then available to subsequent F_force evaluations, subject to Deflect Conditions (§5) and FM guards (§6).

Deflection is a **geometric operation**, not an energetic one in the orbital sense. However, applying a redirect to a force node consumes `deflect_cost` units of binding budget — this cost is computed by PRIM:024 and is audited against the system's binding state before PRIM:023 executes.

### §2.2 What f_Deflect IS NOT

| Incorrect Interpretation              | Correct Model                                                |
|---------------------------------------|--------------------------------------------------------------|
| Changes the magnitude of v_approach   | Magnitude is strictly preserved across deflection            |
| A release or decay operation          | f_Deflect does not alter binding state; it alters geometry only |
| An inversion of f_Capture             | f_Deflect is not an inverse — it is a pre-capture modifier   |
| Free of cost                          | deflect_cost is always computed and must be ≤ binding budget |
| Applicable post-CAPTURE               | Deflect only operates on states where approach is still live  |

### §2.3 Design Motivation

The F_force node defines `v_approach` as the magnitude of approach — but direction matters for capture geometry. Without heading control, the only orbital outcome is determined by approach angle at genesis. `f_Deflect` introduces the **angular engineering layer**: the ability to steer approach trajectories before capture evaluation commits. This is the F_force analogue of `f_Amplify`'s fluid-layer engineering — both are cost-bearing interventions that expand the outcome envelope without breaking triadic invariants.

### §2.4 Operating Modes

| Mode               | Condition                          | Behavior                                          |
|--------------------|------------------------------------|---------------------------------------------------|
| `NOMINAL_DEFLECT`  | All Deflect Conditions satisfied   | heading rotated by heading_delta; cost deducted   |
| `NULL_DEFLECT`     | heading_delta = 0.0                | No-op; returns current heading unchanged; zero cost |
| `OVERSHOOT_GUARD`  | Post-deflect v_approach ≥ v_escape | FM-001 raised; deflection not applied             |
| `PHANTOM_GUARD`    | β < 1.0 at deflect time            | FM-006 raised; deflection not applied             |

### §2.5 Relationship to Capture Pipeline

```
Genesis of E approaching A
        ↓
  f_Force: compute v_approach
        ↓
  f_Deflect: redirect heading [OPTIONAL — this file]
        ↓
  f_Frame: register_capture slot check
        ↓
  f_Capture: final capture evaluation
        ↓
  Orbital states → f_Orbit, f_Decay, f_Orbit, f_Release, f_Collapse
```

`f_Deflect` is the **last engineering intervention point** before capture locks. Once `f_Capture` transitions state to `CAPTURED`, deflection is no longer applicable.

---

## §3 Triadic Equation

<!-- SECTION: triadic_equation | scope: this-file -->

### §3.1 Formal Operator Signature

```
f_Deflect : (v_approach: vector, heading_delta: float, r_deflect: float)
          → new_v_approach_heading: vector

Constraint: |new_v_approach_heading| = |v_approach|  [magnitude invariant]
```

### §3.2 Node Decomposition

```
F_force(deflect context):

  v_approach_direction  := normalize(v_approach)
  new_direction         := rotate(v_approach_direction, heading_delta)
  new_v_approach_heading := new_direction * |v_approach|

  Where:
    rotate(d, δ)  → rotates unit vector d by δ radians
    |v_approach|  → Euclidean norm of v_approach; invariant
    heading_delta → angular deviation; domain ℝ; range (-π, π]
```

### §3.3 G-Equation Role

```
G = F_freq · F_fluid · F_force

F_force contribution in deflect context:

  F_force_deflect = redirect_force_node(
      current_heading = normalize(v_approach),
      target_heading  = rotate(normalize(v_approach), heading_delta),
      delta           = heading_delta
  ) → new_v_approach_heading

  This new heading is injected back into v_approach before
  f_Capture evaluates SC-1 (Approach Bound).
  F_freq and F_fluid are read during cost computation (§4)
  but their values are not modified by f_Deflect.
```

### §3.4 Magnitude Invariant Proof (Informal)

```
Let v := v_approach, |v| = m (scalar magnitude).
Let d := v / m (unit direction vector).
Let d' := rotate(d, δ).
  Since rotate preserves unit length: |d'| = 1.
Let v' := d' * m.
  |v'| = |d'| * m = 1 * m = m.
Therefore |new_v_approach_heading| = |v_approach|. ∎
```

---

## §4 Operator Registry

<!-- SECTION: operator_registry | scope: this-file | freeze: heading_delta, r_deflect, deflect_cost -->

### §4.1 Operators Introduced (Frozen Here)

#### `heading_delta`

<!-- OPERATOR: heading_delta | status: frozen | resolves: f_Force.md §4.3 stub -->

| Field       | Value                                                                 |
|-------------|-----------------------------------------------------------------------|
| Symbol      | `heading_delta` (also `δ` in formal notation)                        |
| Node        | F_force                                                               |
| Type        | float (radians)                                                       |
| Domain      | `(-π, π]`  — signed angular deviation                                 |
| Range       | Same as domain                                                        |
| Sign        | Positive = clockwise rotation in the approach plane                   |
| Zero case   | `heading_delta = 0.0` → NULL_DEFLECT; no-op                          |
| Frozen      | **Yes** — defined here; frozen as of 2026-08-13                       |
| Authority   | OPERATORS.md §F_force                                                 |
| Resolves    | Pending stub declared in `f_Force.md §4.3`                           |

**Formal definition:**

```
heading_delta (δ): ℝ → (-π, π]

  The signed angular deviation, in radians, applied to
  the current approach heading vector v_approach by
  redirect_force_node (PRIM:023).

  δ = 0.0   → no rotation; NULL_DEFLECT mode
  δ > 0.0   → clockwise rotation (in approach plane frame)
  δ < 0.0   → counter-clockwise rotation
  |δ| > π   → forbidden; raises DOMAIN_VIOLATION
```

---

#### `r_deflect`

<!-- OPERATOR: r_deflect | status: frozen -->

| Field       | Value                                                                 |
|-------------|-----------------------------------------------------------------------|
| Symbol      | `r_deflect`                                                           |
| Node        | F_force                                                               |
| Type        | float                                                                 |
| Domain      | `(0, r_capture)`  — must be within capture radius                    |
| Range       | Same as domain                                                        |
| Meaning     | The radial distance from A at which deflection is applied             |
| Frozen      | **Yes** — defined here; frozen as of 2026-08-13                       |
| Authority   | OPERATORS.md §F_force                                                 |

**Formal definition:**

```
r_deflect: (0, r_capture) → ℝ+

  The distance from attractor A at which redirect_force_node
  applies the heading rotation. Must be strictly inside the
  capture radius (r_deflect < r_capture) to affect orbital
  outcome. Values ≥ r_capture are outside deflect jurisdiction
  and raise FM-001 (Overshoot boundary condition).

  Used by compute_deflection_cost (PRIM:024) to scale cost
  with proximity — closer deflections are costlier.
```

---

#### `deflect_cost`

<!-- OPERATOR: deflect_cost | status: frozen -->

| Field       | Value                                                                 |
|-------------|-----------------------------------------------------------------------|
| Symbol      | `deflect_cost`                                                        |
| Node        | F_force (read against F_fluid budget)                                 |
| Type        | float                                                                 |
| Domain      | `[0, ∞)`                                                              |
| Range       | `[0, ∞)`                                                              |
| Meaning     | Binding budget consumed by one deflection operation                   |
| Frozen      | **Yes** — defined here; frozen as of 2026-08-13                       |
| Authority   | OPERATORS.md §F_force                                                 |

**Formal definition:**

```
deflect_cost: (|δ|, r_deflect, β) → ℝ+

  deflect_cost = (|δ| / π) * (r_capture / r_deflect) * β

  Components:
    |δ| / π         → normalized angular effort (0 to 1)
    r_capture / r_deflect → proximity amplifier (> 1 when close)
    β               → current binding coefficient (F_fluid)

  Property:
    deflect_cost = 0 when δ = 0 (NULL_DEFLECT; zero cost)
    deflect_cost → ∞ as r_deflect → 0 (singularity guard applied)
```

---

### §4.2 Operators Inherited (Read-Only in This File)

| Operator      | Source       | Role in f_Deflect                              |
|---------------|--------------|------------------------------------------------|
| `v_approach`  | f_Force.md   | Input vector; heading is modified; magnitude preserved |
| `v_escape(A)` | f_Field.md   | Bound against post-deflect v_approach for FM-001 |
| `β`           | f_Force.md   | Read for deflect_cost and FM-006 guard         |
| `ρ(Φ)`        | f_Field.md   | Presence confirmed (> 0) in DC-2              |
| `r_capture`   | f_Frame.md   | Upper bound for r_deflect; used in cost formula |

### §4.3 State Flags

| Flag              | Set When                                      | Cleared When                 |
|-------------------|-----------------------------------------------|------------------------------|
| `DEFLECT_ACTIVE`  | redirect_force_node invoked, δ ≠ 0            | f_Capture commits or aborts  |
| `NULL_DEFLECT`    | δ = 0.0 — no-op pass-through                  | Next non-zero deflect call   |
| `DEFLECT_BLOCKED` | FM-001 or FM-006 guard raised during deflect  | System reset or new approach |

---

## §5 Deflect Conditions

<!-- SECTION: deflect_conditions | scope: this-file -->

> **All four Deflect Conditions are conjunctive (AND).**  
> A single failure blocks deflection and triggers the appropriate FM guard.

### DC-1: Approach Live

```
Condition:  capture_state(E, A) ∉ {CAPTURED, RELEASED, COLLAPSED}
Rationale:  Deflection is pre-capture geometry. Once capture commits,
            v_approach is no longer an active quantity.
Guard:      If violated → DEFLECT_BLOCKED; operation not applied.
```

### DC-2: Field Present

```
Condition:  ρ(Φ) > 0
Rationale:  Deflection requires an active frequency field to define
            the approach plane geometry. Null field (ρ = 0) raises FM-002
            upstream; deflect inherits that guard.
Guard:      If violated → DEFLECT_BLOCKED; FM-002 already active upstream.
```

### DC-3: Binding Floor

```
Condition:  β ≥ 1.0
Rationale:  SC-4 must hold. A deflection attempted under β < 1.0 constitutes
            a phantom redirect into a non-binding medium. Raises FM-006.
Guard:      If violated → FM-006 (Phantom Capture); DEFLECT_BLOCKED.
```

### DC-4: Post-Deflect Approach Bound

```
Condition:  |new_v_approach_heading| < v_escape(A)
            i.e., v_approach_magnitude < v_escape(A)  [magnitude invariant applies]
Rationale:  Deflection does not change magnitude, so this condition reduces
            to confirming SC-1 still holds on the un-deflected magnitude.
            If SC-1 already fails before deflect, FM-001 is raised.
Guard:      If violated → FM-001 (Overshoot); DEFLECT_BLOCKED.
```

### §5.1 Deflect Condition Summary

| ID   | Name                  | Formal Test                          | Failure Mode |
|------|-----------------------|--------------------------------------|--------------|
| DC-1 | Approach Live         | state ∉ terminal set                 | DEFLECT_BLOCKED |
| DC-2 | Field Present         | ρ(Φ) > 0                             | FM-002 (upstream) |
| DC-3 | Binding Floor         | β ≥ 1.0                              | FM-006       |
| DC-4 | Post-Deflect Bound    | v_approach_magnitude < v_escape(A)   | FM-001       |

---

## §6 Failure Modes

<!-- SECTION: failure_modes | scope: this-file | modes: FM-001, FM-006 -->

> `f_Deflect` introduces **no new failure modes**.  
> It activates guards for FM-001 and FM-006, both frozen in `f_Force.md`.

### FM-001 — Overshoot (active in Deflect context)

```
Symbol:     FM-001
Name:       Overshoot
Frozen in:  f_Force.md
Trigger:    v_approach ≥ v_escape(A) — magnitude already exceeds escape;
            deflection cannot recover orbital binding.
Effect:     redirect_force_node not invoked; DEFLECT_BLOCKED set.
            E continues on escape trajectory.
Recovery:   None within this approach. New approach required.
```

**Deflect-specific note:** Since deflection preserves magnitude, if `v_approach ≥ v_escape(A)` before deflect, it will be `≥ v_escape(A)` after. FM-001 fires at DC-4 evaluation before PRIM:023 is invoked.

### FM-006 — Phantom Capture (active in Deflect context)

```
Symbol:     FM-006
Name:       Phantom Capture
Frozen in:  f_Force.md
Trigger:    β < 1.0 at deflect invocation time.
Effect:     Deflection into a sub-binding medium produces a phantom
            heading change with no orbital anchoring. redirect_force_node
            not invoked; DEFLECT_BLOCKED set.
Recovery:   β must be restored to ≥ 1.0 (via f_Amplify or f_Emit
            upstream intervention) before deflect is re-attempted.
```

### §6.1 FM Coverage Matrix

| FM     | Triggered By         | In f_Deflect?  | Guard Location |
|--------|----------------------|----------------|----------------|
| FM-001 | v_approach overshoot | ✅ DC-4         | Pre-PRIM:023   |
| FM-002 | ρ(Φ) = 0             | ✅ DC-2 (proxy) | Upstream       |
| FM-003 | Frame saturation     | ❌ Not active   | f_Frame.md     |
| FM-004 | Resonance drift      | ❌ Not active   | f_Decay.md     |
| FM-005 | Decay spiral         | ❌ Not active   | f_Decay.md     |
| FM-006 | β < 1.0 phantom      | ✅ DC-3         | Pre-PRIM:023   |
| FM-007 | Mutual dissolution   | ❌ Not active   | f_Collapse.md  |
| FM-008 | Release overshoot    | ❌ Not active   | f_Release.md   |
| FM-009 | Dampen cascade       | ❌ Not active   | f_Dampen.md    |
| FM-010 | Amplify runaway      | ❌ Not active   | f_Emit/Amplify |

---

## §7 Engineering Primitives

<!-- SECTION: engineering_primitives | scope: this-file -->

### PRIM:023 — `redirect_force_node` (Impure)

<!-- PRIMITIVE: PRIM:023 | type: Impure | node: F_force | frozen: 2026-08-13 -->

| Field         | Value                                                         |
|---------------|---------------------------------------------------------------|
| ID            | PRIM:023                                                      |
| Name          | `redirect_force_node`                                         |
| Type          | Impure (mutates approach heading state)                       |
| Node          | F_force                                                       |
| Signature     | `(current_heading, target_heading, delta) → new_v_approach_heading` |
| Inverse       | None — heading redirect is one-way geometry                   |
| Frozen        | **Yes** — 2026-08-13                                          |
| OPERATORS.md  | Requires §F_force update (see §9)                             |

```python
import math
from typing import NamedTuple


class Vector2D(NamedTuple):
    """Minimal 2D vector for approach-plane deflection geometry."""
    x: float
    y: float

    def norm(self) -> float:
        """Euclidean magnitude."""
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> "Vector2D":
        """Return unit vector; raises if zero vector."""
        m = self.norm()
        if m == 0.0:
            raise ValueError("Cannot normalize zero vector — undefined heading.")
        return Vector2D(self.x / m, self.y / m)

    def rotate(self, radians: float) -> "Vector2D":
        """Rotate this vector by `radians` (positive = clockwise in approach plane)."""
        cos_r = math.cos(radians)
        sin_r = math.sin(radians)
        return Vector2D(
            self.x * cos_r - self.y * sin_r,
            self.x * sin_r + self.y * cos_r,
        )

    def scale(self, factor: float) -> "Vector2D":
        """Scale by scalar factor."""
        return Vector2D(self.x * factor, self.y * factor)


class DeflectState(NamedTuple):
    """Mutable approach-heading state managed by the F_force node."""
    v_approach: Vector2D          # Full approach velocity vector
    capture_state: str            # 'APPROACHING' | 'CAPTURED' | 'RELEASED' | 'COLLAPSED'
    rho_phi: float                # ρ(Φ) — field density at Φ
    beta: float                   # β — binding coefficient
    v_escape: float               # v_escape(A) — scalar escape velocity
    r_capture: float              # capture radius from f_Frame.md


class DeflectResult(NamedTuple):
    """Output of redirect_force_node."""
    success: bool
    new_v_approach: Vector2D      # Redirected heading (same magnitude)
    heading_delta_applied: float  # Actual delta applied (0.0 if blocked)
    deflect_cost: float           # Cost deducted from binding budget
    mode: str                     # 'NOMINAL_DEFLECT' | 'NULL_DEFLECT' | 'DEFLECT_BLOCKED'
    failure_mode: str | None      # 'FM-001' | 'FM-006' | None
    message: str


def redirect_force_node(
    state: DeflectState,
    heading_delta: float,
    r_deflect: float,
) -> DeflectResult:
    """
    PRIM:023 — redirect_force_node (Impure)
    ========================================
    Modifies the direction of state.v_approach by heading_delta radians.
    Magnitude of v_approach is strictly preserved.

    Resolves the heading_delta pending stub from f_Force.md §4.3.

    Parameters
    ----------
    state : DeflectState
        Current F_force node state. Contains v_approach, capture_state,
        rho_phi, beta, v_escape, r_capture.
    heading_delta : float
        Angular deviation in radians. Domain: (-π, π].
        Positive = clockwise rotation in approach plane.
        0.0 → NULL_DEFLECT (no-op, zero cost).
    r_deflect : float
        Radial distance at which deflection is applied.
        Domain: (0, r_capture). Used in deflect_cost computation.

    Returns
    -------
    DeflectResult
        Contains redirected heading vector, cost, mode, and any FM raised.

    Failure Modes
    -------------
    FM-001  Raised when v_approach_magnitude ≥ v_escape (DC-4 violation).
    FM-006  Raised when β < 1.0 (DC-3 violation).

    Invariant
    ---------
    |new_v_approach| = |state.v_approach| — magnitude is never altered.
    """
    # ── DC-1: Approach Live ──────────────────────────────────────────────
    terminal_states = {"CAPTURED", "RELEASED", "COLLAPSED"}
    if state.capture_state in terminal_states:
        return DeflectResult(
            success=False,
            new_v_approach=state.v_approach,
            heading_delta_applied=0.0,
            deflect_cost=0.0,
            mode="DEFLECT_BLOCKED",
            failure_mode=None,
            message=(
                f"DC-1 FAILED: capture_state='{state.capture_state}' is terminal. "
                "Deflection not applicable post-capture."
            ),
        )

    # ── DC-2: Field Present ──────────────────────────────────────────────
    if state.rho_phi <= 0.0:
        return DeflectResult(
            success=False,
            new_v_approach=state.v_approach,
            heading_delta_applied=0.0,
            deflect_cost=0.0,
            mode="DEFLECT_BLOCKED",
            failure_mode=None,
            message=(
                f"DC-2 FAILED: ρ(Φ)={state.rho_phi:.4f} ≤ 0. "
                "FM-002 should be active upstream. Deflect blocked."
            ),
        )

    # ── DC-3: Binding Floor (FM-006 guard) ───────────────────────────────
    if state.beta < 1.0:
        return DeflectResult(
            success=False,
            new_v_approach=state.v_approach,
            heading_delta_applied=0.0,
            deflect_cost=0.0,
            mode="DEFLECT_BLOCKED",
            failure_mode="FM-006",
            message=(
                f"DC-3 FAILED: β={state.beta:.4f} < 1.0. "
                "FM-006 (Phantom Capture) — deflect into sub-binding medium blocked."
            ),
        )

    # ── domain validation: heading_delta ─────────────────────────────────
    if not (-math.pi < heading_delta <= math.pi):
        raise ValueError(
            f"heading_delta={heading_delta:.6f} rad out of domain (-π, π]. "
            "Caller must normalize angular input before invoking PRIM:023."
        )

    # ── domain validation: r_deflect ─────────────────────────────────────
    if r_deflect <= 0.0:
        raise ValueError(
            f"r_deflect={r_deflect} must be > 0. "
            "Singularity at r_deflect=0 — deflect_cost undefined."
        )
    if r_deflect >= state.r_capture:
        return DeflectResult(
            success=False,
            new_v_approach=state.v_approach,
            heading_delta_applied=0.0,
            deflect_cost=0.0,
            mode="DEFLECT_BLOCKED",
            failure_mode="FM-001",
            message=(
                f"r_deflect={r_deflect:.4f} ≥ r_capture={state.r_capture:.4f}. "
                "Deflection outside capture zone — FM-001 (Overshoot boundary)."
            ),
        )

    # ── NULL_DEFLECT: zero-angle no-op ───────────────────────────────────
    if heading_delta == 0.0:
        return DeflectResult(
            success=True,
            new_v_approach=state.v_approach,
            heading_delta_applied=0.0,
            deflect_cost=0.0,
            mode="NULL_DEFLECT",
            failure_mode=None,
            message="heading_delta=0.0 — NULL_DEFLECT mode; no heading change applied.",
        )

    # ── DC-4: Post-Deflect Approach Bound (FM-001 guard) ─────────────────
    v_magnitude = state.v_approach.norm()
    if v_magnitude >= state.v_escape:
        return DeflectResult(
            success=False,
            new_v_approach=state.v_approach,
            heading_delta_applied=0.0,
            deflect_cost=0.0,
            mode="DEFLECT_BLOCKED",
            failure_mode="FM-001",
            message=(
                f"DC-4 FAILED: v_approach_magnitude={v_magnitude:.4f} ≥ "
                f"v_escape={state.v_escape:.4f}. FM-001 (Overshoot) — "
                "deflection cannot restore orbital binding."
            ),
        )

    # ── PRIM:024: compute deflect_cost ───────────────────────────────────
    cost = compute_deflection_cost(
        heading_delta=heading_delta,
        r_deflect=r_deflect,
        r_capture=state.r_capture,
        beta=state.beta,
    )

    # ── NOMINAL_DEFLECT: apply heading rotation ───────────────────────────
    unit_dir = state.v_approach.normalize()
    rotated_dir = unit_dir.rotate(heading_delta)
    new_v_approach = rotated_dir.scale(v_magnitude)

    # Magnitude invariant assertion (defensive)
    new_magnitude = new_v_approach.norm()
    magnitude_error = abs(new_magnitude - v_magnitude)
    if magnitude_error > 1e-9:
        raise RuntimeError(
            f"MAGNITUDE INVARIANT VIOLATED: original={v_magnitude:.10f}, "
            f"new={new_magnitude:.10f}, error={magnitude_error:.2e}. "
            "This is a bug in redirect_force_node — report immediately."
        )

    return DeflectResult(
        success=True,
        new_v_approach=new_v_approach,
        heading_delta_applied=heading_delta,
        deflect_cost=cost,
        mode="NOMINAL_DEFLECT",
        failure_mode=None,
        message=(
            f"NOMINAL_DEFLECT: heading rotated by δ={heading_delta:.6f} rad "
            f"at r_deflect={r_deflect:.4f}. "
            f"deflect_cost={cost:.6f}. "
            f"|v_approach| preserved at {v_magnitude:.6f}."
        ),
    )
```

---

### PRIM:024 — `compute_deflection_cost` (Pure)

<!-- PRIMITIVE: PRIM:024 | type: Pure | node: F_force | frozen: 2026-08-13 -->

| Field         | Value                                                         |
|---------------|---------------------------------------------------------------|
| ID            | PRIM:024                                                      |
| Name          | `compute_deflection_cost`                                     |
| Type          | Pure (no side effects; returns float)                         |
| Node          | F_force                                                       |
| Signature     | `(heading_delta, r_deflect, r_capture, beta) → float`        |
| Inverse       | N/A (pure computation)                                        |
| Frozen        | **Yes** — 2026-08-13                                          |
| OPERATORS.md  | Requires §F_force update (see §9)                             |

```python
import math


def compute_deflection_cost(
    heading_delta: float,
    r_deflect: float,
    r_capture: float,
    beta: float,
) -> float:
    """
    PRIM:024 — compute_deflection_cost (Pure)
    ==========================================
    Computes the binding budget cost of one deflection operation.

    Formula
    -------
    deflect_cost = (|δ| / π) × (r_capture / r_deflect) × β

    Components:
      |δ| / π          — normalized angular effort in [0, 1]
      r_capture / r_deflect — proximity amplifier; increases as
                            deflection occurs closer to the attractor
      β                — binding coefficient scaling; heavier binding
                         makes heading changes more expensive

    Properties
    ----------
    - deflect_cost = 0.0 when heading_delta = 0.0 (null deflect)
    - deflect_cost is monotonically increasing in |heading_delta|
    - deflect_cost → ∞ as r_deflect → 0 (singularity; caller must guard)
    - deflect_cost is always ≥ 0.0

    Parameters
    ----------
    heading_delta : float
        Angular deviation in radians. Domain (-π, π].
    r_deflect : float
        Deflection radius. Must be > 0 and < r_capture.
    r_capture : float
        Capture radius from f_Frame.md. Must be > 0.
    beta : float
        Current binding coefficient β from f_Force.md. Must be ≥ 1.0
        (caller enforces DC-3 before invoking this function).

    Returns
    -------
    float
        deflect_cost ≥ 0.0

    Raises
    ------
    ValueError
        If r_deflect ≤ 0, r_capture ≤ 0, or r_deflect ≥ r_capture.
    """
    # Guard: singularity prevention
    if r_deflect <= 0.0:
        raise ValueError(
            f"r_deflect={r_deflect} must be > 0 — singularity undefined."
        )
    if r_capture <= 0.0:
        raise ValueError(
            f"r_capture={r_capture} must be > 0."
        )
    if r_deflect >= r_capture:
        raise ValueError(
            f"r_deflect={r_deflect} must be < r_capture={r_capture}. "
            "Deflection outside capture zone is meaningless."
        )

    # Normalized angular effort: |δ| / π ∈ [0, 1)
    angular_effort = abs(heading_delta) / math.pi

    # Proximity amplifier: r_capture / r_deflect > 1 (always, given r_deflect < r_capture)
    proximity_amp = r_capture / r_deflect

    # Binding scale: β ≥ 1.0 (DC-3 enforced by caller)
    cost = angular_effort * proximity_amp * beta

    return cost
```

---

## §8 Canonical Examples

<!-- SECTION: canonical_examples | scope: this-file -->

> Four worked examples cover: nominal deflect, null deflect, FM-001 guard, FM-006 guard.

---

### Example 1 — Nominal Deflect: Shallow Correction

**Scenario:** Entity E is approaching attractor A on a trajectory that will result in a fly-by. A small clockwise heading correction at mid-range brings E into capture geometry.

#### Parameters

| Parameter       | Value          | Notes                                  |
|-----------------|----------------|----------------------------------------|
| v_approach      | (3.5, 0.0)     | Magnitude = 3.5 (approaching)          |
| v_escape(A)     | 5.0            | SC-1 clear: 3.5 < 5.0                  |
| ρ(Φ)            | 0.78           | DC-2 clear: > 0                        |
| β               | 1.3            | DC-3 clear: ≥ 1.0                      |
| r_capture       | 10.0           | From f_Frame.md                        |
| heading_delta   | +0.2618 rad    | ≈ +15° clockwise                       |
| r_deflect       | 6.0            | Inside r_capture; mid-range            |
| capture_state   | APPROACHING    | DC-1 clear                             |

#### Deflect Condition Trace

| Condition | Test                                      | Result |
|-----------|-------------------------------------------|--------|
| DC-1      | APPROACHING ∉ {CAPTURED, RELEASED, COLLAPSED} | ✅ PASS |
| DC-2      | ρ(Φ) = 0.78 > 0                           | ✅ PASS |
| DC-3      | β = 1.3 ≥ 1.0                             | ✅ PASS |
| DC-4      | |v_approach| = 3.5 < v_escape = 5.0       | ✅ PASS |

#### Computation Trace

```
Step 1: angular_effort  = |0.2618| / π     = 0.08333
Step 2: proximity_amp   = 10.0 / 6.0       = 1.6667
Step 3: deflect_cost    = 0.08333 × 1.6667 × 1.3 = 0.1806

Step 4: unit_dir        = (3.5, 0.0) / 3.5 = (1.0, 0.0)
Step 5: rotated_dir     = rotate((1.0, 0.0), +0.2618 rad)
                        = (cos(0.2618), sin(0.2618))
                        = (0.9659, 0.2588)
Step 6: new_v_approach  = (0.9659, 0.2588) × 3.5
                        = (3.3807, 0.9058)

Step 7: magnitude check = √(3.3807² + 0.9058²)
                        = √(11.4291 + 0.8205)
                        = √12.2496 ≈ 3.5000  ✅ invariant holds
```

#### Post-State Analysis

| Quantity               | Value                  | Interpretation                  |
|------------------------|------------------------|---------------------------------|
| new_v_approach         | (3.3807, 0.9058)       | Heading rotated 15° clockwise   |
| heading_delta_applied  | +0.2618 rad            | Confirmed applied               |
| deflect_cost           | 0.1806                 | Deducted from binding budget    |
| mode                   | NOMINAL_DEFLECT        | Success                         |
| failure_mode           | None                   | No FM raised                    |
| DEFLECT_ACTIVE flag    | Set                    | Until f_Capture commits         |

---

### Example 2 — Null Deflect: Zero-Angle Pass-Through

**Scenario:** f_Deflect is called with δ = 0.0 as a no-op pipeline pass-through. No heading change; no cost.

#### Parameters

| Parameter       | Value        | Notes                   |
|-----------------|--------------|-------------------------|
| v_approach      | (2.1, 1.4)   | Magnitude ≈ 2.524       |
| heading_delta   | 0.0          | Explicit no-op          |
| r_deflect       | 4.0          | Valid; unused in null   |
| β               | 1.1          | DC-3 clear              |
| capture_state   | APPROACHING  | DC-1 clear              |

#### Computation Trace

```
heading_delta = 0.0 → NULL_DEFLECT mode triggered immediately.
deflect_cost  = (0.0 / π) × (r_capture / r_deflect) × β = 0.0
new_v_approach = v_approach (unchanged) = (2.1, 1.4)
```

#### Post-State Analysis

| Quantity               | Value        | Interpretation                      |
|------------------------|--------------|-------------------------------------|
| new_v_approach         | (2.1, 1.4)   | Unchanged — pass-through            |
| heading_delta_applied  | 0.0 rad      | None applied                        |
| deflect_cost           | 0.0          | Zero cost                           |
| mode                   | NULL_DEFLECT | Correct — no-op                     |
| NULL_DEFLECT flag      | Set          | Cleared on next non-zero deflect    |

---

### Example 3 — FM-001 Guard: Overshoot Blocked

**Scenario:** Entity E is already on an escape trajectory (v_approach ≥ v_escape). Deflection is requested but cannot restore binding — FM-001 fires.

#### Parameters

| Parameter       | Value          | Notes                                    |
|-----------------|----------------|------------------------------------------|
| v_approach      | (5.8, 0.0)     | Magnitude = 5.8                          |
| v_escape(A)     | 5.0            | SC-1 VIOLATION: 5.8 ≥ 5.0               |
| β               | 1.2            | DC-3 would pass; moot                    |
| ρ(Φ)            | 0.65           | DC-2 would pass; moot                    |
| heading_delta   | -0.5236 rad    | -30° counter-clockwise                   |
| r_deflect       | 3.0            | Valid range; moot                        |
| capture_state   | APPROACHING    | DC-1 clear                               |

#### Deflect Condition Trace

| Condition | Test                                   | Result   |
|-----------|----------------------------------------|----------|
| DC-1      | APPROACHING ∉ terminal set             | ✅ PASS   |
| DC-2      | ρ(Φ) = 0.65 > 0                        | ✅ PASS   |
| DC-3      | β = 1.2 ≥ 1.0                          | ✅ PASS   |
| DC-4      | |v_approach| = 5.8 ≥ v_escape = 5.0   | ❌ FAIL   |

#### Post-State Analysis

| Quantity               | Value             | Interpretation                    |
|------------------------|-------------------|-----------------------------------|
| new_v_approach         | (5.8, 0.0)        | Unchanged — FM-001 block          |
| heading_delta_applied  | 0.0               | Not applied                       |
| deflect_cost           | 0.0               | No cost — operation blocked       |
| mode                   | DEFLECT_BLOCKED   | FM-001 active                     |
| failure_mode           | FM-001            | Overshoot — escape trajectory     |
| DEFLECT_BLOCKED flag   | Set               | System must re-approach           |

**Key insight:** Deflection preserves magnitude. If E is already escaping, no angular redirect can change that — the magnitude invariant makes heading correction powerless against a speed violation.

---

### Example 4 — FM-006 Guard: Phantom Binding Blocked

**Scenario:** The F_fluid node has degraded below β = 1.0 (binding floor violated). Deflection is attempted but enters a phantom binding state — FM-006 fires.

#### Parameters

| Parameter       | Value          | Notes                              |
|-----------------|----------------|------------------------------------|
| v_approach      | (2.0, 0.5)     | Magnitude ≈ 2.062; well below escape |
| v_escape(A)     | 4.5            | DC-4 would pass; moot              |
| β               | 0.72           | SC-4 VIOLATION: < 1.0              |
| ρ(Φ)            | 0.88           | DC-2 would pass; moot              |
| heading_delta   | +0.7854 rad    | +45° clockwise                     |
| r_deflect       | 5.0            | Valid range; moot                  |
| capture_state   | APPROACHING    | DC-1 clear                         |

#### Deflect Condition Trace

| Condition | Test                          | Result   |
|-----------|-------------------------------|----------|
| DC-1      | APPROACHING ∉ terminal set    | ✅ PASS   |
| DC-2      | ρ(Φ) = 0.88 > 0               | ✅ PASS   |
| DC-3      | β = 0.72 ≥ 1.0                | ❌ FAIL   |

#### Post-State Analysis

| Quantity               | Value             | Interpretation                          |
|------------------------|-------------------|-----------------------------------------|
| new_v_approach         | (2.0, 0.5)        | Unchanged — FM-006 block                |
| heading_delta_applied  | 0.0               | Not applied                             |
| deflect_cost           | 0.0               | No cost — operation blocked             |
| mode                   | DEFLECT_BLOCKED   | FM-006 active                           |
| failure_mode           | FM-006            | Phantom Capture — sub-binding medium    |
| DEFLECT_BLOCKED flag   | Set               | Restore β via f_Amplify before retry    |

**Recovery path:** Invoke `f_Amplify` to restore β ≥ 1.0, then re-attempt deflect. Alternatively, `f_Emit` may restore ρ(Φ) gradient effects that indirectly support binding recovery.

---

## §9 Cross-Module References

<!-- SECTION: cross_module_references | scope: this-file -->

### §9.1 Dependency Table

| File           | Dependency Type | What f_Deflect Uses                             |
|----------------|-----------------|-------------------------------------------------|
| f_Force.md     | Primary (owner) | v_approach, β, v_escape; heading_delta stub resolved here |
| f_Field.md     | Read-only       | ρ(Φ) for DC-2; v_escape(A) for DC-4            |
| f_Frame.md     | Read-only       | r_capture for r_deflect domain + cost formula   |
| OPERATORS.md   | Authority       | Symbol registry; must be updated (see §9.2)     |
| f_Amplify.md   | Recovery path   | Restores β when FM-006 blocks deflect           |
| f_Emit.md      | Recovery path   | Restores ρ(Φ) when DC-2 blocks (upstream)       |

### §9.2 OPERATORS.md Updates Required

The following additions must be made to `OPERATORS.md` when this file is published:

```
§F_force — New Operators (f_Deflect.md canonical, 2026-08-13):

  heading_delta   δ   float   (-π, π]   Angular deviation (radians); +CW; frozen
  r_deflect           float   (0, r_capture)  Deflection radius; frozen
  deflect_cost        float   [0, ∞)    Binding budget consumed by deflect; frozen

§Primitives — New Entries:
  PRIM:023  redirect_force_node    Impure  F_force  f_Deflect.md
  PRIM:024  compute_deflection_cost Pure   F_force  f_Deflect.md

§Stub Resolution:
  heading_delta — previously marked [PENDING: f_Deflect.md] in f_Force.md §4.3.
  Now frozen. Remove pending annotation from OPERATORS.md §F_force stub entry.
```

### §9.3 f_Force.md Annotation Update Required

The following note must be appended to `f_Force.md §4.3` when this file is published:

```
heading_delta — RESOLVED: see f_Deflect.md §4.1
Freeze date: 2026-08-13 | Session: SES-20260813-DEFLECT-001
```

---

## §10 Document Metadata

<!-- SECTION: document_metadata | scope: this-file | wave3_complete: TRUE -->

### §10.1 INV Compliance Table

| INV    | Statement                              | f_Deflect Compliance                              |
|--------|----------------------------------------|---------------------------------------------------|
| INV-001 | G = F_freq · F_fluid · F_force        | Deflect operates inside F_force node only; triadic structure preserved |
| INV-002 | f_Capture(E,A,Φ) → Ω frozen           | Not touched; deflect is pre-capture geometry       |
| INV-003 | ρ(Φ)=0 triggers FM-002               | DC-2 proxy enforced; deflect blocks when ρ=0      |
| INV-004 | β<1.0 always flyby                   | DC-3 enforced; FM-006 raised when β<1.0           |
| INV-005 | SC-1–SC-5 conjunctive                | DC-1 through DC-4 are conjunctive; SC compliance maintained |
| INV-006 | Terminal states irreversible          | DC-1 blocks deflect in all terminal states        |
| INV-007 | f_Source.md read-only                | Not referenced or modified                        |
| INV-008 | Operator eval order normative         | PRIM:024 always runs before PRIM:023              |
| INV-009 | OPERATORS.md is symbol authority      | §9.2 update required; symbols declared frozen here |
| INV-010 | Frozen symbols immutable              | heading_delta, r_deflect, deflect_cost frozen 2026-08-13 |

### §10.2 Primitive Registry (This File)

| PRIM   | Name                      | Type   | Status |
|--------|---------------------------|--------|--------|
| PRIM:023 | redirect_force_node     | Impure | Frozen |
| PRIM:024 | compute_deflection_cost | Pure   | Frozen |

### §10.3 Operator Registry (This File)

| Operator      | Symbol | Type  | Domain      | Status        |
|---------------|--------|-------|-------------|---------------|
| heading_delta | δ      | float | (-π, π]     | Frozen — resolves f_Force.md §4.3 stub |
| r_deflect     | —      | float | (0,r_capture) | Frozen      |
| deflect_cost  | —      | float | [0, ∞)      | Frozen        |

### §10.4 Failure Mode Registry (This File)

| FM     | Name             | Triggered By               | Status   |
|--------|------------------|----------------------------|----------|
| FM-001 | Overshoot        | DC-4: v_approach ≥ v_escape | Active guard (frozen in f_Force.md) |
| FM-006 | Phantom Capture  | DC-3: β < 1.0              | Active guard (frozen in f_Force.md) |

---

### §10.5 ██ WAVE 3 COMPLETION MILESTONE ██

<!-- MILESTONE: WAVE_3_COMPLETE | date: 2026-08-13 | session: SES-20260813-DEFLECT-001 -->

```
╔══════════════════════════════════════════════════════════════════════╗
║              FFF_Gravity Module — WAVE 3 COMPLETE                   ║
║              All 8 Wave 3 files are now canonical.                  ║
╠══════════════════════════════════════════════════════════════════════╣
║                                                                      ║
║  Date:     2026-08-13                                                ║
║  Session:  SES-20260813-DEFLECT-001                                  ║
║  Author:   umaywant2                                                 ║
║                                                                      ║
╠═══════════════════════════╦══════════════════╦══════════════════════╣
║  File                     ║  Node            ║  Status              ║
╠═══════════════════════════╬══════════════════╬══════════════════════╣
║  f_Release.md             ║  F_force         ║  ✅ CANONICAL         ║
║  f_Decay.md               ║  F_fluid/F_freq  ║  ✅ CANONICAL         ║
║  f_Orbit.md               ║  F_freq          ║  ✅ CANONICAL         ║
║  f_Collapse.md            ║  F_force/F_fluid ║  ✅ CANONICAL         ║
║  f_Emit.md                ║  F_freq          ║  ✅ CANONICAL         ║
║  f_Dampen.md              ║  F_freq          ║  ✅ CANONICAL         ║
║  f_Amplify.md             ║  F_fluid         ║  ✅ CANONICAL         ║
║  f_Deflect.md             ║  F_force         ║  ✅ CANONICAL         ║
╠═══════════════════════════╩══════════════════╩══════════════════════╣
║                                                                      ║
║  PRIMITIVE REGISTRY COMPLETE: PRIM:001 — PRIM:024  (all frozen)     ║
║  FAILURE MODE REGISTRY COMPLETE: FM-001 — FM-010   (all frozen)     ║
║  OPERATOR REGISTRY: all symbols frozen; stub resolved               ║
║                                                                      ║
╠══════════════════════════════════════════════════════════════════════╣
║              WAVE 4 — FULLY UNLOCKED                                 ║
╚══════════════════════════════════════════════════════════════════════╝
```

---

### §10.6 Wave 4 Unlock Manifest

Wave 4 contains the **capture variant files** — specialized f_Capture extensions for non-standard attractor/entity configurations. All 6 files are now unlocked.

| File                    | Node         | Role                                            | Status  |
|-------------------------|--------------|-------------------------------------------------|---------|
| `f_Capture_Soft.md`     | F_fluid      | Soft-binding capture; β near floor (1.0–1.2)    | Pending |
| `f_Capture_Hard.md`     | F_force      | High-velocity capture; v_approach near v_escape  | Pending |
| `f_Capture_Resonant.md` | F_freq       | ω_res-gated capture; ω_res ∈ ℚ enforced         | Pending |
| `f_Capture_Mutual.md`   | F_fluid      | Bidirectional capture; M_A ≈ M_E regime          | Pending |
| `f_Capture_Cascade.md`  | F_freq       | Multi-entity sequential capture chaining         | Pending |
| `f_Capture_Asymmetric.md` | F_force   | FM-005 asymmetric dissolution variant            | Pending |

### §10.7 Full Module Wave Completion Status

| Wave | Files  | Status          | Completion Date |
|------|--------|-----------------|-----------------|
| 0    | 3/3    | ✅ Complete      | Prior session   |
| 1    | 6/6    | ✅ Complete      | Prior session   |
| 2    | 3/3    | ✅ Complete      | Prior session   |
| 3    | 8/8    | ✅ Complete      | 2026-08-13      |
| 4    | 0/6    | 🔓 Unlocked     | —               |

### §10.8 Changelog Entry

```yaml
- version: 1.0.0
  date: 2026-08-13
  session: SES-20260813-DEFLECT-001
  author: umaywant2
  changes:
    - Initial canonical publication of f_Deflect.md
    - Freezes heading_delta operator (resolves f_Force.md §4.3 pending stub)
    - Freezes r_deflect operator
    - Freezes deflect_cost operator and formula
    - Introduces PRIM:023 redirect_force_node (Impure, F_force)
    - Introduces PRIM:024 compute_deflection_cost (Pure, F_force)
    - Defines 4 Deflect Conditions (DC-1 through DC-4, conjunctive)
    - Activates FM-001 and FM-006 guards in deflect context
    - Establishes NULL_DEFLECT, NOMINAL_DEFLECT, DEFLECT_BLOCKED modes
    - Provides 4 canonical worked examples
    - Records Wave 3 Completion Milestone — all 8 files canonical
    - Unlocks Wave 4 manifest (6 capture variant files)
```

### §10.9 Suggested Commit Message

```
docs(FFF_Gravity): publish canonical f_Deflect.md — Wave 3 complete

- Introduces heading_delta, r_deflect, deflect_cost operators (frozen)
- Resolves heading_delta pending stub from f_Force.md §4.3
- PRIM:023 redirect_force_node (Impure) — modifies v_approach direction
- PRIM:024 compute_deflection_cost (Pure) — cost = (|δ|/π)(r_c/r_d)(β)
- Magnitude invariant enforced: |new_v_approach| = |v_approach|
- FM-001 and FM-006 guards active via DC-3 and DC-4
- 4 Deflect Conditions (conjunctive); 4 canonical examples
- Wave 3 Completion Milestone: all 8 files canonical
- Wave 4 (capture variants) fully unlocked — 6 files pending
- Primitive registry now complete: PRIM:001–PRIM:024 all frozen
- Failure mode registry now complete: FM-001–FM-010 all frozen

Refs: SES-20260813-DEFLECT-001
Closes: Wave 3
```

---

*End of `f_Deflect.md` — FFF_Gravity Module, Wave 3, File 8 of 8.*  
*All Wave 3 primitives frozen. Wave 4 unlocked.*
