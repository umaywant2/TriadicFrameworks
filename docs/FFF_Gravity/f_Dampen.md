---
title: "f_Dampen — Field Suppression Primitive"
module: FFF_Gravity
version: 1.0.0
status: canonical
tag: "[FFF:GRAVITY:DAMPEN]"
session: SES-20260813-DAMPEN-001
wave: 3
wave_position: "6 of 8"
date: 2026-08-13
authors:
  - Nawder
  - Copilot
node: F_freq
inverse_of: f_Emit
depends_on:
  - f_Field.md        # ρ(Φ), r_capture, FM-002
  - f_Force.md        # M_A, β
  - f_Frame.md        # GravityGraph, registry
  - f_Emit.md         # shared ceiling/floor symmetry, FM-010 context
  - OPERATORS.md      # symbol authority
  - GLOSSARY.md       # term authority
operators_introduced:
  - F_damp
  - ρ(Φ)_floor
  - r_damp
  - δρ_damp
  - ρ(Φ)_delta_damp
  - E_damp
  - cascade_guard
  - k_damp
  - k_cost_damp
primitives_introduced:
  - "PRIM:018 suppress_field (impure)"
  - "PRIM:019 check_floor (pure)"
  - "PRIM:020 check_cascade_risk (pure/diagnostic)"
state_flags_introduced:
  - DAMPEN_ACTIVE
  - DAMPEN_FLOOR_APPROACHED
  - DAMPEN_CASCADE
failure_modes_introduced:
  - FM-009
provides_to:
  - f_Amplify.md
  - f_Capture_Resonant.md
  - f_Capture_Networked.md
invariants_active:
  - INV-001
  - INV-002
  - INV-003
  - INV-004
  - INV-005
  - INV-006
  - INV-008
  - INV-009
  - INV-010
changelog:
  - version: 1.0.0
    date: 2026-08-13
    session: SES-20260813-DAMPEN-001
    author: Nawder + Copilot
    note: >
      Initial canonical production. F_damp operator frozen. ρ(Φ)_floor,
      r_damp, cascade_guard, E_damp frozen. PRIM:018–020 frozen. FM-009
      (Dampen Cascade) fully specified. DAMP-C-1 through DAMP-C-4 conjunctive
      conditions. 4 canonical examples. Full INV compliance table.
---

# f_Dampen — Field Suppression Primitive
**Tag:** `[FFF:GRAVITY:DAMPEN]` · **Wave 3 · File 6 of 8** · **Canonical v1.0.0**

---

## §0 · Session Context

| Field | Value |
|---|---|
| Session ID | `SES-20260813-DAMPEN-001` |
| Date | 2026-08-13 |
| Authors | Nawder + Copilot |
| Wave | 3 — Core Functions |
| Position | File 6 of 8 |
| Preceding file | f_Emit.md (SES-20260813-EMIT-001) ✅ |
| Following file | f_Amplify.md |
| Status | ✅ canonical |

### §0.1 · What This Session Establishes

`f_Dampen` is the **field-suppression engineering primitive** of FFF_Gravity. It is the exact inverse of `f_Emit`: where `f_Emit` increases `ρ(Φ)` (the coherence well depth), `f_Dampen` decreases it. This file:

1. Freezes the `F_damp` operator and all subsidiary parameters.
2. Defines the four conjunctive Dampening Conditions (DAMP-C-1 through DAMP-C-4).
3. Fully specifies FM-009 (Dampen Cascade) — the fatal failure triggered by unguarded null propagation.
4. Introduces PRIM:018 (`suppress_field`), PRIM:019 (`check_floor`), PRIM:020 (`check_cascade_risk`).
5. Provides four worked examples covering drainage, orbit protection, cascade, and safe iteration.

### §0.2 · Invariants Active

| INV | Statement (abbreviated) |
|---|---|
| INV-001 | G = F_freq · F_fluid · F_force inseparable |
| INV-002 | f_Capture signature frozen |
| INV-003 | ρ(Φ) = 0 always triggers FM-002 |
| INV-004 | β < 1.0 always produces flyby |
| INV-005 | All Stability Conditions conjunctive |
| INV-006 | Terminal states irreversible |
| INV-008 | Operator evaluation order normative |
| INV-009 | OPERATORS.md is symbol authority |
| INV-010 | Frozen symbols unrenameable without major version bump |

---

## §1 · Module Identity

### §1.1 · Function Signature

```
f_Dampen(A, Φ, δρ, r_damp) → Φ_updated | FM-009
```

| Parameter | Type | Description |
|---|---|---|
| `A` | Attractor | The attractor whose field is being suppressed |
| `Φ` | FieldState | Current field state (contains ρ(Φ)_current, flags) |
| `δρ` | ℝ > 0 | Requested density decrement |
| `r_damp` | ℝ > 0 | Dampening radius (spatial bound of effect) |

| Return | Condition |
|---|---|
| `Φ_updated` | DAMP-C-1 through DAMP-C-4 all satisfied; ρ(Φ) decreased by ρ(Φ)_delta_damp |
| `FM-009` | Null propagation detected; cascade fired |

### §1.2 · Triadic Position

```
       ┌─────────────────────────────────────┐
       │           F_freq Node               │
       │                                     │
       │   ρ(Φ) ∈ [ρ_floor, 1.0]            │
       │          ↑            ↓             │
       │     f_Emit        f_Dampen          │
       │    (+δρ)          (−δρ)             │
       │                                     │
       │   Hard bounds:                      │
       │     Upper: ρ(Φ) = 1.0   (FM-010)   │
       │     Lower: ρ(Φ)_floor   (FM-009)   │
       └──────────────┬──────────────────────┘
                      │
          ┌───────────┴───────────┐
          │                       │
     F_fluid                  F_force
     (M_A, β)               (v_approach)
```

`f_Dampen` acts **exclusively on F_freq** via `ρ(Φ)`. The F_fluid and F_force nodes are unmodified. However, changes in `ρ(Φ)` cascade downstream:

| Downstream Effect | Mechanism |
|---|---|
| v_escape(A) decreases | `v_escape = √(2 × M_A × ρ(Φ) / r_capture)` |
| β decreases | `β = M_E × ρ(Φ) / M_A` (binding ratio drops) |
| d_bind decreases | `d_bind = β × ρ(Φ) × (1 − e)` (both β and ρ(Φ) fall) |
| capacity_MAX decreases | `floor(M_A × ρ(Φ) × k_frame)` |

These downstream consequences make `f_Dampen` a powerful but high-risk primitive. The cascade guard system (§5.4) exists precisely because of the non-local reach of even a small `ρ(Φ)` reduction.

### §1.3 · Symmetry with f_Emit

Every design decision in `f_Dampen` mirrors a corresponding decision in `f_Emit`. This symmetry is intentional — operators and automated systems should be able to pair calls bidirectionally.

| Property | f_Emit | f_Dampen |
|---|---|---|
| Direction | ρ(Φ) ↑ | ρ(Φ) ↓ |
| Blocking failure | FM-010 (ceiling) | FM-009 (floor/cascade) |
| Energy exchange | Consumes E_emit | Recovers/dissipates E_damp |
| Ceiling/floor check | `check_emit_ceiling` (PRIM:017) | `check_floor` (PRIM:019) |
| Risk profile | Runaway saturation | Cascade null propagation |
| Safe iteration helper | `sustained_emission_loop` | `iterative_dampen_loop` (§8.4) |
| Recovery from blockage | f_Dampen restores headroom for f_Emit | f_Emit restores headroom for f_Dampen |

---

## §2 · Canonical Description

### §2.1 · What f_Dampen IS

`f_Dampen` provides the only sanctioned mechanism for **decreasing** `ρ(Φ)` on a live attractor node. No other operator may write `ρ(Φ)` downward except `suppress_field` (PRIM:018). Its canonical use cases are:

1. **FM-010 recovery** — draining a saturated field (`ρ(Φ) = 1.0`) back below the ceiling so `f_Emit` can resume.
2. **Release assistance** — reducing `d_bind` by lowering `ρ(Φ)`, making `f_Release` cheaper (E_rel decreases as `ρ(Φ)` decreases).
3. **β management** — intentionally loosening an overly tight orbit (high β) by reducing the field density that feeds it.
4. **Selective unbinding** — driving a specific element's orbit toward FM-004/FM-005 by controlled field drainage (carefully, with cascade guard).
5. **Resonance tuning** — adjusting `ρ(Φ)` to hit a target `ω_res` for `f_Capture_Resonant` pre-positioning.

### §2.2 · What f_Dampen IS NOT

| Misconception | Correction |
|---|---|
| A way to destroy orbits instantly | Dampening does not purge registry entries; that is `f_Collapse` |
| Reversible by the engine itself | Only `f_Emit` can restore `ρ(Φ)` — no autonomous recovery |
| Safe with `cascade_guard = false` by default | Default is `cascade_guard = true`; disabling it requires deliberate opt-in |
| Bounded only by zero | Bounded by `ρ(Φ)_floor > 0` (default 0.05) to prevent FM-002 |
| F_force or F_fluid operation | Exclusively F_freq — modifies only `ρ(Φ)` |

### §2.3 · The Cascade Propagation Problem

When `ρ(Φ)` on node `A` is driven to `ρ(Φ)_floor` (the hard lower bound), the null signal can propagate across GravityGraph edges to adjacent attractor nodes. Each adjacent node that receives the null signal evaluates FM-002. If that node is also near its floor, its FM-002 fires and the cascade continues.

```
A → FM-002 → A₁(FM-002?) → A₂(FM-002?) → ... [cascade front]
```

`cascade_guard = true` prevents this by clamping `δρ_damp` such that `ρ(Φ)` on `A` never reaches `ρ(Φ)_floor`. With `cascade_guard = false`, the operator accepts cascade risk — FM-009 may fire.

**The cascade guard is on by default.** `cascade_guard = false` is an explicit operator override that should only be used in isolated single-node systems or controlled teardown sequences.

---

## §3 · Triadic Equation

### §3.1 · Core Formula

```
G = F_freq · F_fluid · F_force          [INV-001]

f_Dampen modifies F_freq exclusively:
  F_freq_new = F_freq(ρ(Φ) − ρ(Φ)_delta_damp)

Primary dampening operator:
  F_damp = (δρ_damp × k_damp) / (r_damp × ρ(Φ))

  where ρ(Φ) = current field density before suppression
        (denominator is non-zero: ρ(Φ) > ρ(Φ)_floor > 0 by DAMP-C-1)

Realized suppression magnitude:
  ρ(Φ)_delta_damp = min(δρ_damp, ρ(Φ) − ρ(Φ)_floor)

Post-suppression field density:
  ρ(Φ)_new = ρ(Φ) − ρ(Φ)_delta_damp  ≥  ρ(Φ)_floor  [guaranteed by DAMP-C-1]

Energy recovered (or thermally dissipated):
  E_damp = M_A × ρ(Φ)_delta_damp × r_damp² × k_cost_damp
```

**Note on energy sign.** E_damp is recovered energy (field coherence is released). When `k_cost_damp < 1.0`, the surplus is thermally dissipated. When `k_cost_damp > 1.0`, the suppression requires active energy input (pumping against field pressure — unusual but physically meaningful in high-coherence regimes).

### §3.2 · G-Product Consequence

After `f_Dampen`:
```
G_new = F_freq(ρ_new) · F_fluid · F_force
      < G_prior           (F_freq factor reduced)
```

The reduction in G weakens all binding relationships on `A`:
- All active orbits experience a reduction in `d_bind` (next `f_Decay` cycle)
- `v_escape(A)` falls — orbits become less stable
- `capacity_MAX` may fall — if ρ(Φ)_new × M_A × k_frame drops below an integer boundary, a capacity slot disappears

---

## §4 · Operator Registry

> **Authority:** OPERATORS.md governs all symbol definitions (INV-009). The definitions here are the first canonical statements of these symbols. All must be reflected in OPERATORS.md §2 and §4 after this file is committed.

### §4.1 · Primary Operator

#### `F_damp` — Dampening Field Strength

**Formula:**
```
F_damp = (δρ_damp × k_damp) / (r_damp × ρ(Φ))
```

**Properties:**

| Property | Value |
|---|---|
| Domain | ℝ > 0 (positive by definition — suppression magnitude) |
| Node | F_freq |
| Frozen in | f_Dampen.md §4.1 |
| Undefined when | ρ(Φ) = 0 (protected by INV-003 and DAMP-C-1 before this is reached) |

**Interpretation:** F_damp measures suppression intensity — how much field reduction is achieved per unit radius, normalized by current field density. As ρ(Φ) → ρ(Φ)_floor, F_damp → ∞: each marginal suppression increment is increasingly effective (the field is thin), but also increasingly close to FM-009. This is the mirror of F_emit's ceiling approach behavior.

### §4.2 · Derived Quantities

#### `ρ(Φ)_delta_damp` — Realized Suppression Magnitude

```
ρ(Φ)_delta_damp = min(δρ_damp, ρ(Φ) − ρ(Φ)_floor)
```

The actual density decrease applied after floor enforcement. May be smaller than `δρ_damp` when headroom is limited.

#### `ρ(Φ)_floor` — Field Floor Bound

```
ρ(Φ)_floor ∈ (0, ρ(Φ)_current)
```

| Property | Value |
|---|---|
| Default | 0.05 |
| Minimum | > 0 (must be strictly positive — INV-003) |
| Maximum | < ρ(Φ)_current (must leave some headroom to suppress at all) |
| Set by | Operator at initialization; may be raised for safety |
| Consequence of floor breach | FM-009 fires |

The floor is the **last engineering defense** before FM-002. Setting it too low (e.g., 0.001) creates a dangerously thin safety margin. Raising it (e.g., 0.20) provides more protection at the cost of reduced dampening range.

#### `r_damp` — Dampening Radius

```
r_damp ∈ (0, r_capture]
```

| Property | Value |
|---|---|
| Type | ℝ > 0 |
| Meaning | Spatial radius of suppression effect centered on A |
| Lower bound | r_damp > 0 (point suppression undefined — division by zero in F_damp) |
| Upper bound | r_damp ≤ r_capture (DAMP-C-2) |
| Effect outside radius | None — ρ(Φ) unchanged beyond r_damp |

#### `δρ_damp` — Requested Suppression Increment

Caller-supplied decrement. Must be > 0. Clipped by `check_floor` (PRIM:019) to available headroom before application.

#### `E_damp` — Dampening Energy

```
E_damp = M_A × ρ(Φ)_delta_damp × r_damp² × k_cost_damp
```

Energy released or dissipated during suppression. Scales quadratically with `r_damp` (volumetric coverage). The caller is responsible for energy accounting — `suppress_field` computes and records `E_damp` but does not deduct it from any reserve.

#### `cascade_guard` — Cascade Prevention Flag

| Value | Behavior |
|---|---|
| `True` (default) | Clamps δρ_damp to ensure ρ(Φ) ≥ ρ(Φ)_floor; FM-009 cannot fire |
| `False` | Operator accepts cascade risk; PRIM:020 evaluates FM-009 probability before proceeding |

### §4.3 · Constants

| Symbol | Default | Description |
|---|---|---|
| `k_damp` | 1.0 | Dampening gain constant (attractor-class-specific calibration) |
| `k_cost_damp` | 1.0 | Energy cost coefficient (< 1: passive dissipation; > 1: active pumping) |
| `ε_damp` | 0.02 | Floor proximity threshold for `DAMPEN_FLOOR_APPROACHED` flag |

---

## §5 · Dampening Conditions

All four conditions are conjunctive — all must hold before `suppress_field` executes. Missing any single condition blocks or modifies the operation.

### DAMP-C-1 — Floor Bound

```
ρ(Φ) − δρ_damp  ≥  ρ(Φ)_floor

If violated with cascade_guard = true:
    clamp: ρ(Φ)_delta_damp ← ρ(Φ) − ρ(Φ)_floor
    set: DAMPEN_FLOOR_APPROACHED
    proceed with clamped value

If violated with cascade_guard = false:
    evaluate cascade risk via PRIM:020
    if risk = HIGH → block and require operator override
    if risk = MEDIUM → set DAMPEN_FLOOR_APPROACHED, proceed
    if risk = LOW → proceed (floor clamp still applied)
```

**Rationale:** INV-003 (`ρ(Φ) = 0` → FM-002) means the floor is not optional. DAMP-C-1 ensures ρ(Φ) never reaches zero regardless of `δρ_damp`.

### DAMP-C-2 — Radius Bound

```
r_damp ∈ (0, r_capture]

If r_damp ≤ 0: reject with ValueError
If r_damp > r_capture: clamp to r_capture with warning
```

**Rationale:** Suppression cannot extend beyond the attractor's capture boundary. The field state Φ is defined relative to A and its relational scope — suppression outside `r_capture` has undefined semantics.

### DAMP-C-3 — Active Orbit Guard

```
For each element E with ORBIT_LOCKED on A:
    ρ_orbit_min(E) = minimum ρ(Φ) sustaining β(E) ≥ 1.0
    effective_floor = max(ρ(Φ)_floor, max over all E of ρ_orbit_min(E))
    clamp: ρ(Φ)_delta_damp ← min(ρ(Φ)_delta_damp, ρ(Φ) − effective_floor)
```

**Rationale:** INV-004 (β < 1.0 → flyby). Dampening below `ρ_orbit_min` would inadvertently trigger flyby on currently bound elements. DAMP-C-3 prevents inadvertent unbinding by raising the effective floor to protect all active orbits simultaneously.

### DAMP-C-4 — Cascade Guard Check

```
If cascade_guard = true:
    → proceed (DAMP-C-1 already enforces floor)

If cascade_guard = false:
    require graph argument
    invoke check_cascade_risk(A, ρ(Φ)_delta_damp, graph)  [PRIM:020]
    if risk.level = HIGH:
        block and emit FM-009 HIGH warning
        return error unless operator passes override = true
    if risk.level = MEDIUM:
        set DAMPEN_FLOOR_APPROACHED
        proceed with warning
    if risk.level = LOW:
        proceed
```

**Rationale:** The cascade guard is the primary systemic safety mechanism. `cascade_guard = false` is not an error; it is a deliberate choice that must be paired with explicit cascade risk assessment.

---

## §6 · Failure Modes

### FM-009 — Dampen Cascade

| Property | Value |
|---|---|
| ID | FM-009 |
| Name | Dampen Cascade |
| Severity | **fatal** |
| Frozen in | f_Dampen.md §6 |
| Node | F_freq |
| Trigger | `ρ(Φ)` on A reaches or breaches `ρ(Φ)_floor` while `cascade_guard = false`, AND null signal propagates to ≥ 1 adjacent node |
| State flag | `DAMPEN_CASCADE` |
| Recoverable | No — FM-009 is terminal for each affected node (INV-006) |
| Prevention | `cascade_guard = true` (default) |

**Mechanism:** When A's `ρ(Φ)` hits the floor under unguarded conditions, the field null signal propagates across GravityGraph edges. Each adjacent node `Aᵢ` with `cascade_guard = false` evaluates FM-002. If FM-002 fires on `Aᵢ`, its null signal propagates further. The cascade front expands until it encounters a node with `cascade_guard = true` or a node with no unprotected neighbors.

**Cascade propagation algorithm:**

```python
def propagate_cascade(origin, graph):
    queue, visited = [origin], set()
    while queue:
        node = queue.pop(0)
        if node in visited: continue
        visited.add(node)
        trigger_FM002(node)           # Field Null — terminal for this node
        node.state = "DAMPEN_CASCADE" # INV-006: irreversible
        for neighbor in graph.neighbors(node):
            if neighbor.cascade_guard:
                log(f"CASCADE_HALTED at {neighbor.id} — guard active")
            else:
                queue.append(neighbor)
    return visited  # set of all affected nodes
```

**Detection code:**

```python
def detect_fm009(
    rho_current: float,
    rho_floor:   float,
    delta_damp:  float
) -> bool:
    """
    Returns True if FM-009 cascade condition is met.
    Caller (suppress_field) uses this before applying any suppression.
    """
    rho_after = rho_current - delta_damp
    return rho_after < rho_floor   # strict: floor breach triggers FM-009
```

**Key distinction from FM-002:** FM-002 fires on a single node when `ρ(Φ)` = 0. FM-009 is the systemic event when A's field null *propagates to adjacent nodes*. FM-009 always includes FM-002 on the origin node, but adds multi-node cascade semantics.

**GravityGraph events emitted:**

| Event | Trigger |
|---|---|
| `FM_009_TRIGGERED` | Cascade fires; payload: `{origin, cascade_depth, affected_nodes}` |
| `FM_002_FROM_CASCADE` | Per-node FM-002 during propagation |
| `CASCADE_HALTED` | Guard-protected node stops the front |

---

## §7 · Engineering Primitives

### PRIM:018 — `suppress_field` (impure)

**Purpose:** Master dampening executor. Validates all Dampening Conditions, applies `ρ(Φ)_delta_damp`, updates field state, emits events, triggers FM-009 if cascade guard is off and floor is breached.

**Tag:** `[FFF:GRAVITY:PRIM:018]`
**Frozen in:** f_Dampen.md §7 (SES-20260813-DAMPEN-001)

```python
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class DampenResult:
    success:           bool
    rho_before:        float
    rho_after:         float
    delta_applied:     float   # actual ρ(Φ)_delta_damp after clamping
    E_damp:            float
    flags:             list[str]
    fm_triggered:      list[str]
    cascade_affected:  list[str]  # node IDs reached by cascade
    abort_reason:      Optional[str]


def suppress_field(
    attractor,
    phi,
    delta_rho:     float,
    r_damp:        float,
    rho_floor:     float = 0.05,
    cascade_guard: bool  = True,
    k_damp:        float = 1.0,
    k_cost_damp:   float = 1.0,
    graph          = None
) -> DampenResult:
    """
    PRIM:018 — suppress_field (impure)

    Canonical field-suppression primitive. The only sanctioned mechanism for
    decreasing ρ(Φ) on a live attractor node.

    Evaluation order (INV-008):
        1. Terminal state guard
        2. DAMP-C-2: radius bound
        3. DAMP-C-3: active orbit guard → effective_floor
        4. DAMP-C-1: floor bound → compute ρ(Φ)_delta_damp via check_floor (PRIM:019)
        5. DAMP-C-4: cascade guard check → PRIM:020 if cascade_guard=False
        6. Apply ρ(Φ) decrement
        7. Compute E_damp
        8. Update flags and emit GravityGraph events

    Args:
        attractor:     Mutable attractor node (A.rho_phi is written in-place).
        phi:           Field state object (mutable).
        delta_rho:     Requested suppression magnitude (must be > 0).
        r_damp:        Dampening radius (DAMP-C-2: must be ∈ (0, r_capture]).
        rho_floor:     Floor bound below which ρ(Φ) must not fall (default 0.05).
        cascade_guard: If True (default), clamp δρ to prevent floor breach.
                       If False, accept cascade risk — PRIM:020 is invoked.
        k_damp:        Dampening gain constant.
        k_cost_damp:   Energy cost coefficient.
        graph:         GravityGraph reference (required when cascade_guard=False).

    Returns:
        DampenResult with full audit trail.

    Raises:
        ValueError:   delta_rho ≤ 0, r_damp violates DAMP-C-2, or
                      cascade_guard=False with no graph provided.
        RuntimeError: phi is in a terminal state (CAPTURE_COLLISION, COLLAPSED).
        FM009Error:   FM-009 triggered (cascade propagated; nodes terminal).

    Side effects:
        - Writes attractor.rho_phi (decremented by delta_applied).
        - Sets/clears phi.flags.
        - Calls propagate_cascade() if FM-009 fires.
        - Emits DAMPEN_COMPLETE / DAMPEN_FLOOR_APPROACHED / FM_009_TRIGGERED
          events to GravityGraph event bus.
    """
    result = DampenResult(
        success=False, rho_before=phi.rho, rho_after=phi.rho,
        delta_applied=0.0, E_damp=0.0, flags=["DAMPEN_ACTIVE"],
        fm_triggered=[], cascade_affected=[], abort_reason=None
    )

    # ── Terminal state guard ────────────────────────────────────────────────
    if any(f in phi.flags for f in ("CAPTURE_COLLISION", "COLLAPSED", "FIELD_NULL")):
        result.abort_reason = "suppress_field called on terminal field state (INV-006)"
        return result

    # ── delta_rho must be positive ──────────────────────────────────────────
    if delta_rho <= 0:
        raise ValueError(f"delta_rho must be > 0; got {delta_rho}")

    # ── DAMP-C-2: Radius Bound ──────────────────────────────────────────────
    if r_damp <= 0:
        raise ValueError(f"r_damp must be > 0; got {r_damp}")
    if r_damp > attractor.r_capture:
        r_damp = attractor.r_capture
        result.flags.append("RADIUS_CLAMPED_TO_R_CAPTURE")

    # ── DAMP-C-3: Active Orbit Guard ─────────────────────────────────────────
    rho_orbit_min = compute_orbit_floor(attractor)   # max β≥1.0 requirement over all E
    effective_floor = max(rho_floor, rho_orbit_min)

    # ── DAMP-C-1: Floor Bound → via check_floor ──────────────────────────────
    floor_result = check_floor(phi.rho, delta_rho, effective_floor)   # PRIM:019
    rho_delta = floor_result.clamped_delta

    if floor_result.floor_approached:
        result.flags.append("DAMPEN_FLOOR_APPROACHED")

    # If no headroom at all, block
    if rho_delta <= 0:
        result.abort_reason = (
            f"No suppression headroom: ρ(Φ)={phi.rho:.4f} is already at "
            f"effective_floor={effective_floor:.4f}"
        )
        result.flags.remove("DAMPEN_ACTIVE")
        return result

    # ── DAMP-C-4: Cascade Guard Check ────────────────────────────────────────
    if not cascade_guard:
        if graph is None:
            raise ValueError(
                "cascade_guard=False requires a GravityGraph argument. "
                "Provide graph= or set cascade_guard=True."
            )
        risk = check_cascade_risk(attractor, rho_delta, graph)   # PRIM:020
        if risk.level == "HIGH":
            result.abort_reason = (
                f"FM-009 HIGH CASCADE RISK: estimated depth {risk.cascade_depth_est}, "
                f"vulnerable neighbors: {risk.vulnerable_neighbors}. "
                f"Set cascade_guard=True or pass override=True explicitly."
            )
            result.flags.remove("DAMPEN_ACTIVE")
            return result
        elif risk.level == "MEDIUM":
            result.flags.append("DAMPEN_FLOOR_APPROACHED")

    # ── Apply suppression ────────────────────────────────────────────────────
    rho_prior = phi.rho
    phi.rho = rho_prior - rho_delta

    # Defensive floor clamp (should already be guaranteed, but belt-and-suspenders)
    if phi.rho < 0:
        phi.rho = 0.0
        _trigger_fm009(attractor, graph, result)
        result.flags.remove("DAMPEN_ACTIVE")
        return result

    # ── Compute E_damp ───────────────────────────────────────────────────────
    E_damp = attractor.M_A * rho_delta * (r_damp ** 2) * k_cost_damp

    # ── Update flags ─────────────────────────────────────────────────────────
    result.flags.remove("DAMPEN_ACTIVE")   # operation complete

    EPS_DAMP = 0.02
    if (phi.rho - effective_floor) < EPS_DAMP:
        result.flags.append("DAMPEN_FLOOR_APPROACHED")

    # Clear FM-010 saturation flag (suppress_field restores emit headroom)
    phi.flags.discard("EMIT_SATURATED")
    phi.flags.discard("EMIT_CEILING_APPROACHED")

    # ── Emit GravityGraph event ───────────────────────────────────────────────
    _emit_event("DAMPEN_COMPLETE", {
        "node":      attractor.id,
        "rho_before": rho_prior,
        "rho_after":  phi.rho,
        "rho_delta":  rho_delta,
        "r_damp":     r_damp,
        "E_damp":     E_damp,
    })

    # ── Build result ─────────────────────────────────────────────────────────
    result.success       = True
    result.rho_before    = rho_prior
    result.rho_after     = phi.rho
    result.delta_applied = rho_delta
    result.E_damp        = E_damp

    return result
```

---

### PRIM:019 — `check_floor` (pure)

**Purpose:** EC-1 mirror for dampening. Returns available headroom above `ρ(Φ)_floor` and clips the requested delta if needed.

**Tag:** `[FFF:GRAVITY:PRIM:019]`
**Frozen in:** f_Dampen.md §7 (SES-20260813-DAMPEN-001)

```python
@dataclass
class FloorResult:
    clamped_delta:    float   # actual δρ to apply (≤ δρ_requested)
    floor_approached: bool    # True if remaining headroom < ε_damp after clamp
    headroom:         float   # ρ_current − ρ_floor (before any clamp)
    was_clamped:      bool    # True if δρ_requested was reduced

EPS_DAMP: float = 0.02       # module constant — floor proximity threshold

def check_floor(
    rho_current:   float,
    delta_requested: float,
    rho_floor:     float
) -> FloorResult:
    """
    PRIM:019 — check_floor (pure)

    Symmetric counterpart to check_emit_ceiling (PRIM:017).
    Where PRIM:017 tests headroom below ρ(Φ)=1.0,
    PRIM:019 tests headroom above ρ(Φ)_floor.

    Returns the clamped delta and approach flag. No side effects.

    Args:
        rho_current:     Current ρ(Φ) before suppression.
        delta_requested: Requested suppression magnitude.
        rho_floor:       Minimum allowable ρ(Φ) after suppression.

    Returns:
        FloorResult with clamped_delta, headroom, flags.

    Raises:
        ValueError: rho_floor >= rho_current (no headroom at all — caller must handle).
        ValueError: rho_floor < 0 (INV-003: floor must be > 0).
    """
    if rho_floor < 0:
        raise ValueError(f"rho_floor must be ≥ 0; got {rho_floor}. (INV-003)")
    if rho_floor > 0 and rho_current <= rho_floor:
        raise ValueError(
            f"rho_current ({rho_current:.4f}) ≤ rho_floor ({rho_floor:.4f}). "
            "No headroom available. caller must handle."
        )

    headroom = rho_current - rho_floor
    clamped  = min(delta_requested, headroom)
    was_clamped = clamped < delta_requested

    remaining     = rho_current - clamped - rho_floor
    floor_approached = remaining < EPS_DAMP

    return FloorResult(
        clamped_delta    = clamped,
        floor_approached = floor_approached,
        headroom         = headroom,
        was_clamped      = was_clamped
    )
```

---

### PRIM:020 — `check_cascade_risk` (pure / diagnostic)

**Purpose:** Pre-flight cascade risk assessment when `cascade_guard = false`. Reads graph topology to estimate FM-009 propagation scope.

**Tag:** `[FFF:GRAVITY:PRIM:020]`
**Frozen in:** f_Dampen.md §7 (SES-20260813-DAMPEN-001)

```python
@dataclass
class CascadeRisk:
    level:               str        # "LOW" | "MEDIUM" | "HIGH"
    at_floor_after:      bool       # True if A itself hits rho_floor after delta
    vulnerable_neighbors: list[str] # neighbor IDs with cascade_guard=False and low ρ(Φ)
    cascade_depth_est:   int        # estimated BFS depth before first guarded node
    notes:               list[str]  # diagnostic messages

def check_cascade_risk(attractor, delta_damp: float, graph) -> CascadeRisk:
    """
    PRIM:020 — check_cascade_risk (pure / diagnostic)

    Evaluates the cascade propagation risk of a proposed suppression operation.
    Called by suppress_field (PRIM:018) when cascade_guard=False.
    Safe to call independently for pre-flight assessment.

    Pure function: reads graph topology; no mutations.

    Args:
        attractor:  Attractor node (read-only).
        delta_damp: Proposed ρ(Φ)_delta_damp (already clamped by DAMP-C-1).
        graph:      GravityGraph instance (read-only).

    Returns:
        CascadeRisk with level, vulnerable neighbors, estimated depth.

    Risk levels:
        LOW    → A does not reach rho_floor after delta, or no unguarded neighbors.
        MEDIUM → A approaches floor or ≥1 neighbor is vulnerable but depth is shallow.
        HIGH   → A hits floor after delta AND ≥1 unguarded neighbor is also near floor;
                 estimated cascade depth ≥ 3.
    """
    notes     = []
    vulnerable = []
    EPS_DAMP   = 0.02

    rho_after_A = attractor.rho_phi - delta_damp
    at_floor    = rho_after_A <= attractor.rho_floor

    # Assess immediate neighbors
    for neighbor in graph.neighbors(attractor):
        if neighbor.cascade_guard:
            continue  # protected — not vulnerable
        proximity = neighbor.rho_phi - neighbor.rho_floor
        if proximity < EPS_DAMP:
            vulnerable.append(neighbor.id)
            notes.append(
                f"Neighbor {neighbor.id}: ρ(Φ)={neighbor.rho_phi:.3f} "
                f"within {EPS_DAMP} of floor {neighbor.rho_floor:.3f}"
            )

    # Estimate cascade depth (BFS stopping at guarded nodes)
    depth = 0
    if at_floor and len(vulnerable) > 0:
        depth = _bfs_cascade_depth(attractor, graph)

    # Classify
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

---

## §8 · Canonical Examples

### EX-D-001 — Saturation Drain (FM-010 Recovery)

**Scenario:** Attractor `A_hub` has `ρ(Φ) = 0.97` after sustained `f_Emit` calls. FM-010 (`EMIT_CEILING_APPROACHED`) is set — further emission is blocked. The operator calls `f_Dampen` to drain headroom to 0.75.

**Parameters:**

| Symbol | Value |
|---|---|
| M_A | 8.0 |
| ρ(Φ)_current | 0.97 |
| r_capture | 12.0 |
| ρ(Φ)_floor | 0.05 |
| cascade_guard | True |
| δρ_requested | 0.22 |
| r_damp | 12.0 |
| k_cost_damp | 0.7 |

**Condition evaluation:**
```
DAMP-C-2: r_damp = 12.0 = r_capture  ✅
DAMP-C-3: No ORBIT_LOCKED elements → rho_orbit_min = 0.0
           effective_floor = max(0.05, 0.0) = 0.05
DAMP-C-1: headroom = 0.97 − 0.05 = 0.92
           clamped_delta = min(0.22, 0.92) = 0.22  (no clip)
           remaining = 0.97 − 0.22 − 0.05 = 0.70  >> ε_damp → no floor approach
DAMP-C-4: cascade_guard = True → skip risk check
```

**Result:**
```
ρ_before        = 0.97
ρ_after         = 0.75
delta_applied   = 0.22
E_damp          = 8.0 × 0.22 × 144 × 0.7  =  176.5 units  (recovered)
F_damp          = (0.22 × 1.0) / (12.0 × 0.75)  =  0.024
flags           = []
fm_triggered    = []
```

**Post-state:** `ρ(Φ) = 0.75`. Emit headroom = 0.25. `EMIT_SATURATED` and `EMIT_CEILING_APPROACHED` cleared. `f_Emit` may resume immediately.

---

### EX-D-002 — Floor Clamp with Active Orbit Protection

**Scenario:** Attractor `A_planet` has one bound element `E_moon` in stable orbit (β = 1.60). Operator attempts aggressive dampening (`δρ = 0.50`) but DAMP-C-3 limits suppression to protect `E_moon`'s binding floor.

**Parameters:**

| Symbol | Value |
|---|---|
| ρ(Φ)_current | 0.65 |
| ρ(Φ)_floor | 0.05 |
| ρ_orbit_min(E_moon) | 0.30 |
| effective_floor | max(0.05, 0.30) = 0.30 |
| δρ_requested | 0.50 |
| r_damp | 8.0 (< r_capture = 15.0) |

**Condition evaluation:**
```
DAMP-C-3: effective_floor raised to 0.30 (orbit guard)
DAMP-C-1: headroom = 0.65 − 0.30 = 0.35
           clamped_delta = min(0.50, 0.35) = 0.35  (was_clamped = True)
           remaining = 0.65 − 0.35 − 0.30 = 0.00  < ε_damp
           → DAMPEN_FLOOR_APPROACHED set
```

**Result:**
```
ρ_before        = 0.65
ρ_after         = 0.30
delta_applied   = 0.35  (clamped from 0.50)
E_damp          = M_A × 0.35 × 64 × k_cost_damp
flags           = ["DAMPEN_FLOOR_APPROACHED"]
fm_triggered    = []
```

**Post-state:** `ρ(Φ) = 0.30`. `E_moon` orbit intact: β remains ≥ 1.0 at the floor. Further dampening blocked until `E_moon` is released or its orbit self-decays. Operator receives `DAMPEN_FLOOR_APPROACHED` advisory.

---

### EX-D-003 — FM-009 Cascade Triggered (Fatal)

**Scenario:** Graph segment with three nodes, `cascade_guard = False` on two of them. Operator suppresses `A_hub` beyond its floor.

**Graph topology:**
```
A_hub   ρ(Φ)=0.12   cascade_guard=False   rho_floor=0.10
A_left  ρ(Φ)=0.11   cascade_guard=False   rho_floor=0.10
A_right ρ(Φ)=0.60   cascade_guard=True    (protected)
Edges: A_hub ↔ A_left, A_hub ↔ A_right
```

**Operator call:**
```python
result = suppress_field(
    attractor=A_hub, phi=phi, delta_rho=0.20, r_damp=A_hub.r_capture,
    rho_floor=0.10, cascade_guard=False, graph=gravity_graph
)
```

**PRIM:020 pre-flight:**
```
rho_after_A_hub = 0.12 − 0.20 = −0.08  → at_floor = True
A_left: cascade_guard=False, rho_phi=0.11, proximity=0.01 < ε_damp → VULNERABLE
A_right: cascade_guard=True → PROTECTED
cascade_depth_est = 2  (A_hub → A_left; A_left has no further unprotected neighbors)
level = HIGH  → suppress_field blocks and returns abort_reason
```

*[Operator passes `override=True` — acknowledges HIGH risk explicitly.]*

**Cascade execution:**
```
propagate_cascade(A_hub, graph):
  trigger FM-002(A_hub) → FIELD_NULL [terminal]
  neighbors:
    A_left: cascade_guard=False → queue
    A_right: cascade_guard=True → CASCADE_HALTED logged ✅
  trigger FM-002(A_left) → FIELD_NULL [terminal]
  A_left neighbors: [A_hub (visited)] → stop
```

**Result:**
```
success         = False
fm_triggered    = ["FM-009", "FM-002"]
cascade_affected = ["A_hub", "A_left"]
flags           = ["DAMPEN_CASCADE"]
abort_reason    = "FM-009: cascade propagated to 1 adjacent node"
```

**Post-state:** `A_hub` → FIELD_NULL (terminal). `A_left` → FIELD_NULL (terminal). `A_right` → unaffected (guard held). All orbits on `A_hub` and `A_left` unbound. This is irreversible — INV-006 applies.

---

### EX-D-004 — Iterative β-Targeting with Safe Dampening Pattern

**Scenario:** Attractor `A_giant` has `ρ(Φ) = 0.90` after aggressive emission. Bound element `E_probe` has β = 3.8 — excessively tight orbit accelerating decay. Operator wants β ≈ 1.8 without triggering orbit loss.

**Initial state:**
```
ρ(Φ)_current  = 0.90
ρ_orbit_min   = 0.25  (floor for E_probe β ≥ 1.0)
target_rho    = 0.43  (computed to yield β ≈ 1.8)
δρ_total      = 0.90 − 0.43 = 0.47
```

**Safe iterative dampening pattern:**

```python
def iterative_dampen_loop(
    attractor, phi, target_rho, step_size, r_damp,
    rho_floor, max_steps=10
):
    """
    Safe dampening toward target_rho in small steps.
    Runs one f_Decay cycle between each step to allow orbital
    parameters to stabilize before the next suppression.
    """
    steps_taken = 0
    for step in range(max_steps):
        if phi.rho <= target_rho + 0.01:
            break  # close enough
        delta_step = min(step_size, phi.rho - target_rho)
        result = suppress_field(
            attractor, phi, delta_step, r_damp,
            rho_floor=rho_floor, cascade_guard=True
        )
        if not result.success:
            break
        run_decay_cycle(attractor)   # allow f_Decay to re-evaluate β
        steps_taken += 1
    return phi, steps_taken
```

**Execution trace (step_size = 0.10):**

| Step | ρ(Φ) before | δρ applied | ρ(Φ) after | β estimate |
|---|---|---|---|---|
| 0 | 0.90 | 0.10 | 0.80 | 3.37 |
| 1 | 0.80 | 0.10 | 0.70 | 2.95 |
| 2 | 0.70 | 0.10 | 0.60 | 2.53 |
| 3 | 0.60 | 0.10 | 0.50 | 2.11 |
| 4 | 0.50 | 0.07 | **0.43** | **1.81** |

**Outcome:** β = 1.81 ≈ target 1.80. `E_probe` orbit stabilized. DAMP-C-3 guarded throughout (effective_floor = 0.25). No FM triggered. `f_Decay` re-evaluation after each step confirmed orbit health.

---

## §9 · Cross-Module References

### §9.1 · Files That Call f_Dampen

| Caller | Context | When |
|---|---|---|
| f_Emit.md | FM-010 recovery (§6.1.2) — restores headroom after saturation | Post FM-010 trigger |
| f_Release.md | Release assistance — lowers d_bind to reduce E_rel | Before release attempt |
| f_Capture_Resonant.md | ω_res pre-positioning — fine-tunes ρ(Φ) toward resonance target | Before resonant approach |

### §9.2 · Files That f_Dampen Depends On

| File | What f_Dampen Reads | Purpose |
|---|---|---|
| f_Field.md | ρ(Φ), r_capture, FM-002 semantics | Primary write target, radius bound |
| f_Force.md | M_A, β | E_damp computation, orbit floor |
| f_Frame.md | GravityGraph, registry, capacity_MAX | Cascade propagation, downstream effects |
| f_Emit.md | FM-010 flag (cleared by dampening) | Recovery context |
| OPERATORS.md | All frozen symbols | Symbol authority (INV-009) |

### §9.3 · OPERATORS.md Updates Required

| Symbol / Primitive | Current Status | Required Update |
|---|---|---|
| `F_damp` | 🔵 pending | 🟢 frozen — f_Dampen.md §4.1 |
| `ρ(Φ)_floor` | 🔵 pending | 🟢 frozen — f_Dampen.md §4.2 |
| `r_damp` | 🔵 pending | 🟢 frozen — f_Dampen.md §4.2 |
| `δρ_damp` | 🔵 pending | 🟢 frozen — f_Dampen.md §4.2 |
| `ρ(Φ)_delta_damp` | 🔵 pending | 🟢 frozen — f_Dampen.md §4.2 |
| `E_damp` | 🔵 pending | 🟢 frozen — f_Dampen.md §4.2 |
| `cascade_guard` | 🔵 pending | 🟢 frozen — f_Dampen.md §4.2 |
| `k_damp` | 🔵 pending | 🟢 frozen — f_Dampen.md §4.3 |
| `k_cost_damp` | 🔵 pending | 🟢 frozen — f_Dampen.md §4.3 |
| `DAMPEN_ACTIVE` | 🔵 pending | 🟢 frozen — f_Dampen.md §4 |
| `DAMPEN_FLOOR_APPROACHED` | 🔵 pending | 🟢 frozen — f_Dampen.md §4 |
| `DAMPEN_CASCADE` | 🔵 pending | 🟢 frozen — f_Dampen.md §4 |
| `FM-009` | 🔵 pending | 🟢 frozen — f_Dampen.md §6 |
| PRIM:018 `suppress_field` | pending | 🟢 frozen — f_Dampen.md §7 |
| PRIM:019 `check_floor` | pending | 🟢 frozen — f_Dampen.md §7 |
| PRIM:020 `check_cascade_risk` | pending | 🟢 frozen — f_Dampen.md §7 |

---

## §10 · Document Metadata

### §10.1 · INV Compliance Table

| INV | Statement | Compliance | How Honored |
|---|---|---|---|
| INV-001 | G = F_freq · F_fluid · F_force | ✅ | §3.1 shows F_freq modified; F_fluid and F_force unmodified; G-product reduced accordingly |
| INV-002 | f_Capture(E,A,Φ)→Ω frozen | ✅ | f_Dampen does not modify f_Capture or its signature |
| INV-003 | ρ(Φ)=0 → FM-002 | ✅ | ρ(Φ)_floor (default 0.05) enforced by DAMP-C-1; FM-009 fires if floor breached; FM-002 triggers on cascade nodes |
| INV-004 | β < 1.0 → flyby | ✅ | DAMP-C-3 (orbit guard) prevents dampening below ρ_orbit_min(E) for all ORBIT_LOCKED elements |
| INV-005 | All SCs conjunctive | ✅ | DAMP-C-1 through DAMP-C-4 are conjunctive (§5) |
| INV-006 | Terminal states irreversible | ✅ | FM-009 cascade nodes enter FIELD_NULL terminal state; no recovery path |
| INV-007 | f_Source.md read-only | ✅ | Not referenced |
| INV-008 | Evaluation order normative | ✅ | PRIM:018 §7.1 docstring specifies 8-step evaluation order matching INV-008 |
| INV-009 | OPERATORS.md symbol authority | ✅ | §9.3 lists all 16 required OPERATORS.md updates |
| INV-010 | Frozen symbols unrenameable | ✅ | 9 operators + 3 flags + FM-009 + 3 primitives all declared frozen in §4 |

### §10.2 · Primitive Registry (This File)

| ID | Name | Type | Purpose |
|---|---|---|---|
| PRIM:018 | `suppress_field` | Impure | Master dampening executor — only sanctioned ρ(Φ) downward write |
| PRIM:019 | `check_floor` | Pure | Headroom check and delta clamp (symmetric to PRIM:017 check_emit_ceiling) |
| PRIM:020 | `check_cascade_risk` | Pure/Diagnostic | Pre-flight cascade risk assessment (BFS on GravityGraph) |

**Cumulative primitive count after this file:** PRIM:001 – PRIM:020 (20 primitives frozen across the module)

### §10.3 · Operator Registry (This File)

| Symbol | Formula | Node |
|---|---|---|
| `F_damp` | `(δρ_damp × k_damp) / (r_damp × ρ(Φ))` | F_freq |
| `ρ(Φ)_delta_damp` | `min(δρ_damp, ρ(Φ) − ρ(Φ)_floor)` | F_freq |
| `E_damp` | `M_A × ρ(Φ)_delta_damp × r_damp² × k_cost_damp` | F_freq |

### §10.4 · Failure Mode Registry (This File)

| ID | Name | Severity | Trigger | Recoverable |
|---|---|---|---|---|
| FM-009 | Dampen Cascade | fatal | ρ(Φ) reaches floor; null propagates to adjacent node | No (INV-006) |

**With FM-009 frozen here, all 10 module failure modes (FM-001 through FM-010) are now canonical.**

