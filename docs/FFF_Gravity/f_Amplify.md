---
session_id: SES-20260813-AMPLIFY-001
file: docs/FFF_Gravity/f_Amplify.md
tag: "[FFF:GRAVITY:AMPLIFY]"
version: 1.0.0
status: canonical
wave: 3
node: F_fluid
role: Engineering primitive — increases binding coefficient β and effective pull P_eff
depends_on:
  - f_Capture.md
  - f_Field.md
  - f_Force.md
  - f_Frame.md
  - f_Emit.md
  - f_Dampen.md
new_operators:
  - F_amp
  - β_max
  - amp_cost
new_primitives:
  - PRIM:021 amplify_coupling
  - PRIM:022 check_runaway_risk
failure_modes_specified:
  - FM-010 (β domain)
invariants_enforced:
  - INV-001
  - INV-002
  - INV-003
  - INV-004
  - INV-005
  - INV-006
  - INV-007
  - INV-008
  - INV-009
  - INV-010
date: 2026-08-13
author: umaywant2
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- [FFF:GRAVITY:AMPLIFY] — CANONICAL SPECIFICATION                           -->
<!-- F_fluid Engineering Primitive — Binding Coefficient Amplification         -->
<!-- Wave 3, File 7 of 8                                                       -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# f_Amplify — Binding Coefficient Amplification

> **Module:** FFF_Gravity  
> **Tag:** `[FFF:GRAVITY:AMPLIFY]`  
> **Node:** F_fluid (Mass-Density Coupling)  
> **Wave:** 3 — Core Functions (7 of 8)  
> **Status:** 🟢 CANONICAL  
> **Session:** SES-20260813-AMPLIFY-001  

---

## §0 — Session Context

<!-- [AMPLIFY:§0] Session context block — do not edit -->

| Field | Value |
|---|---|
| Session ID | SES-20260813-AMPLIFY-001 |
| Founding Date | 2026-08-13 |
| Operator | umaywant2 |
| Preceding file | f_Dampen.md (PRIM:018–020 frozen) |
| Following file | f_Deflect.md (Wave 3, File 8 of 8) |
| Cumulative PRIMs after this file | PRIM:001–PRIM:022 (22 frozen) |
| All 10 FMs frozen? | ✅ Yes — FM-010 β-domain fully specified here |

**Purpose of this session:** Deliver the canonical specification of `f_Amplify.md` — the F_fluid engineering primitive that directly increases the binding coefficient β. f_Amplify is the complement of f_Emit (which deepens the coherence well ρ(Φ)) and f_Dampen (which suppresses ρ(Φ)). Where f_Emit widens the attractor field, f_Amplify tightens the grip: the same field density now binds harder.

---

## §1 — Module Identity

<!-- [AMPLIFY:§1] Module identity — frozen -->

### 1.1 Function Signature

```
f_Amplify(A, E, Φ, F_amp) → (β_new, amp_cost, state_flag)
```

| Parameter | Type | Description |
|---|---|---|
| A | Node | Anchor node (attractor; carries M_A, ρ(Φ), r_capture) |
| E | Node | Entrant node (bound object; carries M_E, β, d_bind) |
| Φ | Frame | Registry frame (carries capacity_MAX, registered captures) |
| F_amp | float ≥ 1.0 | Amplification factor applied to current β |

| Return field | Description |
|---|---|
| β_new | Updated binding coefficient post-amplification |
| amp_cost | Energy expended to achieve amplification |
| state_flag | One of: AMP_ACTIVE \| AMP_CEILING_APPROACHED \| AMP_RUNAWAY |

### 1.2 Triadic Position

```
         G = F_freq · F_fluid · F_force
                         │
              ┌──────────┘
              │   F_fluid  ◄── f_Amplify lives here
              │
         ┌────┴────┐
         │  M_A    │  Anchor mass
         │  M_E    │  Entrant mass
         │  β      │◄── f_Amplify modifies this directly
         └─────────┘
              │
         (cascade into d_bind, P_eff, capacity_MAX)
```

**Triadic role:** f_Amplify is a targeted intervention on the F_fluid node. It does not alter ρ(Φ) (that is f_Emit's and f_Dampen's domain) nor v_approach (f_Force's domain). It acts exclusively on β — the binding coefficient that mediates how much of the field's coherence density actually translates into sustained gravitational grip.

### 1.3 Relationship to Companion Primitives

| Primitive | Node | Action | Direction |
|---|---|---|---|
| f_Emit (PRIM:015) | F_freq | Increases ρ(Φ) | Deepens coherence well |
| f_Dampen (PRIM:018) | F_freq | Decreases ρ(Φ) | Suppresses coherence well |
| **f_Amplify (PRIM:021)** | **F_fluid** | **Increases β** | **Tightens binding grip** |
| f_Deflect (PRIM:023) | F_force | Modifies v_approach | Redirects approach vector |

> **Canonical principle:** f_Emit deepens the well; f_Amplify tightens the grip. Both must be evaluated together when engineering a high-stability capture.

---

## §2 — Canonical Description

<!-- [AMPLIFY:§2] Canonical description — frozen -->

### 2.1 What f_Amplify Does

`f_Amplify` increases the binding coefficient β for a given (A, E) pair. β expresses how tightly the entrant E is coupled to the anchor A per unit of field density — it is the F_fluid node's primary tunable scalar. Amplification multiplies β by F_amp (≥ 1.0), subject to the ceiling constraint β_max.

The immediate effects cascade through the model:

1. **d_bind rises** — because `d_bind = β × ρ(Φ) × (1 − e)`, a higher β produces a larger binding depth at identical field density.
2. **P_eff rises (indirectly)** — effective pull `P_eff = M_A × ρ(Φ) / r²` is frozen as a field property, but higher β means P_eff translates more efficiently into sustained binding (fewer escape attempts succeed).
3. **capacity_MAX is unchanged** — `capacity_MAX = floor(M_A × ρ(Φ) × k_frame)` does not depend on β; f_Amplify does not expand the frame registry (that requires f_Emit).
4. **FM-004 recovery becomes possible** — if β has drifted below d_warn threshold, f_Amplify can restore d_bind without touching ρ(Φ).

### 2.2 What f_Amplify Does NOT Do

- Does **not** alter ρ(Φ) — field density is strictly f_Emit/f_Dampen territory.
- Does **not** alter M_A, M_E, or r_capture — those are node properties, not coupling scalars.
- Does **not** modify the frame registry — capacity_MAX, registered_count, and r_capture are untouched.
- Does **not** alter orbital eccentricity e — orbital geometry is computed post-capture by f_Orbit.
- Does **not** trigger f_Capture — amplification can only strengthen an **existing** binding, not create a new one. If no prior capture exists, f_Amplify is a null operation.

### 2.3 Design Motivation

The separation of β-amplification from ρ(Φ)-emission reflects the triadic inseparability principle (INV-001) while preserving engineering orthogonality. In practice:

- A relationship can have high coherence (ρ(Φ) near 1.0) but low coupling efficiency (β near its post-capture minimum) — for example, a mentor relationship with abundant field density but low behavioral commitment. f_Amplify addresses this without wasting energy on field deepening.
- A relationship can have moderate ρ(Φ) but tightly amplified β — for example, a professional contract relationship where behavioral coupling is enforced rather than emergent. Here f_Amplify is the primary instrument; f_Emit is supplementary.

### 2.4 Interaction with f_Frame

`f_Frame.md §2.4` noted that capacity expansion via f_Amplify raises ρ(Φ) indirectly. That note refers to a **second-order** effect: when β increases, bound nodes exhibit tighter orbits, reducing the effective r² load on the frame, which in turn means the same M_A × ρ(Φ) budget supports more registered captures. This is **not** a direct capacity_MAX change — it is a tighter packing effect within the existing capacity.

---

## §3 — Triadic Equation in the Amplify Context

<!-- [AMPLIFY:§3] Equation context — frozen -->

### 3.1 Gravity Identity (INV-001)

```
G = F_freq · F_fluid · F_force
```

f_Amplify modifies **F_fluid exclusively** via β:

```
F_fluid = f(M_A, M_E, β)
```

After amplification:

```
β_new = β_old × F_amp          where F_amp ≥ 1.0
β_new ≤ β_max                  ceiling constraint
```

### 3.2 Cascade into d_bind

```
d_bind_new = β_new × ρ(Φ) × (1 − e)
```

Because β_new > β_old and ρ(Φ), e are unchanged:

```
d_bind_new > d_bind_old        (amplification always increases binding depth)
```

### 3.3 Amplification Cost

```
amp_cost = M_E × (β_new − β_old) × r_capture² × k_cost_amp
```

where:
- `M_E` — entrant mass (the object being more tightly bound incurs proportional cost)
- `(β_new − β_old)` — net β gain; zero gain = zero cost
- `r_capture²` — orbital radius scaling (tighter orbits cost less to amplify; wider orbits cost more)
- `k_cost_amp` — system amplification cost constant (default: 1.0)

### 3.4 β_max Ceiling

```
β_new = min(β_old × F_amp, β_max)
```

β_max is the maximum safe binding coefficient. Exceeding β_max in the β domain triggers **FM-010 (Amplify Runaway)** — the β-domain expression of the same failure mode that ρ(Φ) = 1.0 triggers in the ρ domain.

---

## §4 — Operator Registry

<!-- [AMPLIFY:§4] Operator registry — frozen upon commit -->

### 4.1 New Operators (Introduced in f_Amplify.md)

| Symbol | Name | Domain | Definition | Default |
|---|---|---|---|---|
| `F_amp` | Amplification Factor | F_fluid | Scalar multiplier applied to β; must be ≥ 1.0 | 1.0 (identity, no-op) |
| `β_max` | Binding Coefficient Ceiling | F_fluid | Maximum safe β; exceeding triggers FM-010 (β domain) | System-defined; default 1.0 |
| `amp_cost` | Amplification Energy Cost | F_fluid | Energy consumed by amplify operation | Computed per §3.3 |

> **Freeze notice:** `F_amp`, `β_max`, and `amp_cost` are frozen as of SES-20260813-AMPLIFY-001. Renaming or redefining any of these symbols requires a major version bump per INV-010.

### 4.2 Inherited Operators (Active in f_Amplify Context)

| Symbol | Defined in | Role here |
|---|---|---|
| `β` | OPERATORS.md, f_Force.md | Binding coefficient — the primary target of amplification |
| `P_eff` | OPERATORS.md, f_Force.md | Effective pull = M_A × ρ(Φ) / r²; unchanged by f_Amplify directly |
| `ρ(Φ)` | OPERATORS.md, f_Field.md | Field density; read here, not modified |
| `d_bind` | OPERATORS.md, f_Decay.md | Binding depth; recalculated after β_new is set |
| `M_A` | OPERATORS.md, f_Force.md | Anchor mass; read-only in f_Amplify |
| `M_E` | OPERATORS.md, f_Force.md | Entrant mass; used in amp_cost formula |
| `r_capture` | OPERATORS.md, f_Frame.md | Orbital radius at capture; used in amp_cost formula |
| `e` | OPERATORS.md, f_Orbit.md | Orbital eccentricity; read-only in f_Amplify |
| `k_cost_amp` | (new constant, frozen here) | Amplification cost constant; default 1.0 |

### 4.3 State Flags (Introduced in f_Amplify.md)

| Flag | Meaning |
|---|---|
| `AMP_ACTIVE` | Amplification completed successfully; β updated |
| `AMP_CEILING_APPROACHED` | β_new ≥ 0.90 × β_max; warn operator; next amplification risks runaway |
| `AMP_RUNAWAY` | FM-010 triggered; β would exceed β_max; amplification aborted |

---

## §5 — Amplify Conditions

<!-- [AMPLIFY:§5] Amplify conditions — conjunctive; all must hold -->

All four Amplify Conditions are **conjunctive**. Failure of any single condition aborts amplification and returns the appropriate state flag or error.

### AMP-C-1 — Prior Capture Required

```
∃ capture_record(A, E) in Φ.registry
```

A binding must already exist. f_Amplify cannot create a capture — it can only deepen an existing one. If no capture record exists for (A, E), amplification is a null operation and returns immediately.

### AMP-C-2 — Headroom Available

```
β_old < β_max
```

β must be strictly below the ceiling. If β_old = β_max, no headroom exists and FM-010 is triggered immediately (regardless of F_amp value).

### AMP-C-3 — Field Alive

```
ρ(Φ) > 0.0
```

The coherence field must be active. Amplifying β in a null field (ρ(Φ) = 0.0) has no effect on d_bind (since d_bind = β × 0 × (1−e) = 0 regardless of β), and amplification cost would be wasted. Per INV-003, ρ(Φ) = 0 always triggers FM-002 in f_Field; f_Amplify simply refuses to proceed as a guard.

### AMP-C-4 — F_amp in Range

```
F_amp ≥ 1.0
```

The amplification factor must be at least 1.0 (identity). Values below 1.0 would decrease β — that is the domain of f_Deflect (for v_approach) or a future β-suppression primitive. f_Amplify strictly increases or holds β.

---

## §6 — Failure Modes

<!-- [AMPLIFY:§6] Failure modes — FM-010 β-domain canonical specification -->

### 6.1 FM-010 — Amplify Runaway (β Domain)

> **FM-010** is frozen across two domains:
> - **ρ(Φ) domain** — specified in `f_Emit.md §6.1` (triggered when ρ(Φ) → 1.0)
> - **β domain** — specified HERE (triggered when β → β_max)

#### 6.1.1 Trigger Condition

FM-010 (β domain) fires when:

```
β_old × F_amp > β_max
```

i.e., the requested amplification would push β beyond the ceiling.

#### 6.1.2 Behavior on Trigger

1. **Amplification is aborted.** β is not updated. β_old is preserved.
2. `state_flag` returns `AMP_RUNAWAY`.
3. amp_cost is **not** charged — no energy is consumed for an aborted operation.
4. The capture record in Φ.registry is **not modified**.
5. A diagnostic record is written to Φ's error log: `{node_pair: (A.id, E.id), fm: "FM-010-BETA", beta_old: β_old, f_amp_requested: F_amp, beta_max: β_max}`.

#### 6.1.3 Recovery

FM-010 (β domain) is **not** fatal by itself — unlike FM-005 or the terminal path of FM-009. The capture remains intact. The operator may:

- Reduce F_amp to a value where `β_old × F_amp ≤ β_max`, then retry.
- Accept current β and shift strategy to f_Emit (deepen ρ(Φ) instead).
- Invoke f_Release and re-capture at different parameters if a fundamentally different binding is desired.

> **Warning:** Repeated near-runaway amplification (β approaching β_max over many cycles) is a precursor to frame instability. Monitor via `check_runaway_risk` (PRIM:022).

#### 6.1.4 Dual-Domain FM-010 Summary

| Domain | Ceiling | Trigger | Handler |
|---|---|---|---|
| ρ(Φ) domain | ρ(Φ) = 1.0 | ρ(Φ)_new would exceed 1.0 | f_Emit.md §6.1, PRIM:017 |
| β domain | β = β_max | β_new would exceed β_max | f_Amplify.md §6.1, PRIM:022 |

Both domains share the FM-010 label because they represent the same class of failure: runaway amplification of a coupling coefficient past its physical ceiling.

### 6.2 Other Failure Modes (Referenced, Not Triggered Directly)

| FM | Condition | How f_Amplify Interacts |
|---|---|---|
| FM-002 Field Null | ρ(Φ) = 0 | AMP-C-3 guard prevents amplification; FM-002 is f_Field's responsibility |
| FM-004 Resonance Drift | d_bind drifting below d_warn | f_Amplify is the primary recovery instrument (see f_Decay.md §6.1.3 Path B) |
| FM-005 Decay Spiral | d_bind below d_collapse | If FM-005 is already active, amplification may be too late; check d_bind first |
| FM-007 Mutual Dissolution | mass parity collapse | β amplification cannot prevent f_Collapse when |M_E − M_A| < m_parity |
| FM-009 Dampen Cascade | cascade_guard failure | Unrelated to f_Amplify unless dampen and amplify are called in the same cycle |

---

## §7 — Engineering Primitives

<!-- [AMPLIFY:§7] Primitive specifications — PRIM:021 and PRIM:022 frozen -->

### PRIM:021 — amplify_coupling (Impure)

> **Tag:** PRIM:021  
> **Name:** amplify_coupling  
> **Type:** IMPURE — modifies node state (β) and writes to Φ.registry  
> **Defined in:** f_Amplify.md  
> **Wave:** 3  

#### Signature

```python
def amplify_coupling(
    A: Node,
    E: Node,
    Phi: Frame,
    F_amp: float,
    beta_max: float = 1.0,
    k_cost_amp: float = 1.0
) -> dict:
```

#### Full Specification

```python
def amplify_coupling(
    A: Node,
    E: Node,
    Phi: Frame,
    F_amp: float,
    beta_max: float = 1.0,
    k_cost_amp: float = 1.0
) -> dict:
    """
    PRIM:021 — amplify_coupling (IMPURE)
    =====================================
    Engineering primitive: increases the binding coefficient β for the (A, E) pair.

    Implements the F_fluid amplification operator for f_Amplify.md.
    Modifies E.beta in-place and updates the capture record in Phi.registry.

    Parameters
    ----------
    A : Node
        Anchor node. Required attributes:
          - A.id         : str   — unique node identifier
          - A.M_A        : float — anchor mass (> 0)
          - A.rho_phi    : float — current field density ρ(Φ) ∈ [0, 1]
          - A.r_capture  : float — orbital radius at capture (> 0)
    E : Node
        Entrant node. Required attributes:
          - E.id         : str   — unique node identifier
          - E.M_E        : float — entrant mass (> 0)
          - E.beta       : float — current binding coefficient (> 0)
          - E.d_bind     : float — current binding depth (will be recalculated)
          - E.ecc        : float — orbital eccentricity e ∈ [0, 1)
    Phi : Frame
        Registry frame. Required attributes:
          - Phi.registry : dict  — maps (A.id, E.id) → capture_record
          - Phi.error_log: list  — diagnostic records appended on FM-010
    F_amp : float
        Amplification factor. Must be ≥ 1.0.
    beta_max : float, optional
        Binding coefficient ceiling. Default 1.0.
    k_cost_amp : float, optional
        Amplification cost constant. Default 1.0.

    Returns
    -------
    dict with keys:
        beta_old      : float  — β before amplification
        beta_new      : float  — β after amplification (same as beta_old on failure)
        d_bind_new    : float  — recalculated binding depth (same as old on failure)
        amp_cost      : float  — energy cost of amplification (0.0 on failure)
        state_flag    : str    — AMP_ACTIVE | AMP_CEILING_APPROACHED | AMP_RUNAWAY
        fm_triggered  : str    — "FM-010-BETA" if runaway, else None
        conditions    : dict   — evaluation results for AMP-C-1 through AMP-C-4

    Raises
    ------
    ValueError
        If F_amp < 1.0 (violates AMP-C-4).
    LookupError
        If no capture record exists in Phi.registry for (A.id, E.id) — AMP-C-1 failure.

    Side Effects (IMPURE)
    ---------------------
    On success:
      - E.beta is updated to beta_new.
      - E.d_bind is updated to d_bind_new.
      - Phi.registry[(A.id, E.id)]['beta'] is updated to beta_new.
      - Phi.registry[(A.id, E.id)]['d_bind'] is updated to d_bind_new.
      - Phi.registry[(A.id, E.id)]['amp_history'] is appended with this call's record.
    On FM-010:
      - No state is modified.
      - Phi.error_log is appended with FM-010-BETA diagnostic record.
    """
    from math import isclose

    beta_old  = E.beta
    rho_phi   = A.rho_phi
    r_capture = A.r_capture
    M_E       = E.M_E
    e         = E.ecc

    # ── Condition Evaluation ─────────────────────────────────────────────────

    conditions = {}

    # AMP-C-1: Prior capture required
    pair_key = (A.id, E.id)
    amp_c1 = pair_key in Phi.registry
    conditions["AMP-C-1"] = amp_c1
    if not amp_c1:
        raise LookupError(
            f"AMP-C-1 FAIL: No capture record for ({A.id}, {E.id}). "
            f"f_Amplify cannot create a capture — run f_Capture first."
        )

    # AMP-C-2: Headroom available
    amp_c2 = beta_old < beta_max
    conditions["AMP-C-2"] = amp_c2

    # AMP-C-3: Field alive
    amp_c3 = rho_phi > 0.0
    conditions["AMP-C-3"] = amp_c3

    # AMP-C-4: F_amp in range
    amp_c4 = F_amp >= 1.0
    conditions["AMP-C-4"] = amp_c4
    if not amp_c4:
        raise ValueError(
            f"AMP-C-4 FAIL: F_amp={F_amp} < 1.0. "
            f"Amplification factor must be ≥ 1.0. Use f_Deflect for v_approach adjustment."
        )

    # ── FM-010 (β domain) check ──────────────────────────────────────────────

    if not amp_c2:
        # β is already at ceiling — immediate FM-010
        fm_record = {
            "node_pair":          pair_key,
            "fm":                 "FM-010-BETA",
            "beta_old":           beta_old,
            "f_amp_requested":    F_amp,
            "beta_max":           beta_max,
            "reason":             "AMP-C-2: beta_old already equals beta_max"
        }
        Phi.error_log.append(fm_record)
        return {
            "beta_old":     beta_old,
            "beta_new":     beta_old,          # unchanged
            "d_bind_new":   E.d_bind,          # unchanged
            "amp_cost":     0.0,               # no charge on abort
            "state_flag":   "AMP_RUNAWAY",
            "fm_triggered": "FM-010-BETA",
            "conditions":   conditions
        }

    beta_proposed = beta_old * F_amp

    if beta_proposed > beta_max:
        # Requested F_amp would exceed ceiling — FM-010
        fm_record = {
            "node_pair":          pair_key,
            "fm":                 "FM-010-BETA",
            "beta_old":           beta_old,
            "f_amp_requested":    F_amp,
            "beta_proposed":      beta_proposed,
            "beta_max":           beta_max,
            "reason":             "beta_old × F_amp > beta_max"
        }
        Phi.error_log.append(fm_record)
        return {
            "beta_old":     beta_old,
            "beta_new":     beta_old,          # unchanged
            "d_bind_new":   E.d_bind,          # unchanged
            "amp_cost":     0.0,               # no charge on abort
            "state_flag":   "AMP_RUNAWAY",
            "fm_triggered": "FM-010-BETA",
            "conditions":   conditions
        }

    # ── AMP-C-3 guard (null field) ───────────────────────────────────────────

    if not amp_c3:
        # Field is null — amplification would be meaningless; refuse
        return {
            "beta_old":     beta_old,
            "beta_new":     beta_old,
            "d_bind_new":   0.0,
            "amp_cost":     0.0,
            "state_flag":   "AMP_RUNAWAY",
            "fm_triggered": "FM-002-GUARD",    # not FM-010; FM-002 is f_Field's responsibility
            "conditions":   conditions
        }

    # ── Amplification proceeds ───────────────────────────────────────────────

    beta_new   = beta_proposed   # already verified ≤ beta_max
    d_bind_new = beta_new * rho_phi * (1.0 - e)
    amp_cost   = M_E * (beta_new - beta_old) * (r_capture ** 2) * k_cost_amp

    # Determine ceiling proximity flag
    ceiling_threshold = 0.90 * beta_max
    if beta_new >= ceiling_threshold:
        state_flag = "AMP_CEILING_APPROACHED"
    else:
        state_flag = "AMP_ACTIVE"

    # ── Impure side effects ──────────────────────────────────────────────────

    # Update entrant node
    E.beta   = beta_new
    E.d_bind = d_bind_new

    # Update frame registry record
    record = Phi.registry[pair_key]
    record["beta"]   = beta_new
    record["d_bind"] = d_bind_new
    if "amp_history" not in record:
        record["amp_history"] = []
    record["amp_history"].append({
        "beta_old":    beta_old,
        "f_amp":       F_amp,
        "beta_new":    beta_new,
        "d_bind_new":  d_bind_new,
        "amp_cost":    amp_cost,
        "state_flag":  state_flag
    })

    return {
        "beta_old":     beta_old,
        "beta_new":     beta_new,
        "d_bind_new":   d_bind_new,
        "amp_cost":     amp_cost,
        "state_flag":   state_flag,
        "fm_triggered": None,
        "conditions":   conditions
    }
```

---

### PRIM:022 — check_runaway_risk (Pure)

> **Tag:** PRIM:022  
> **Name:** check_runaway_risk  
> **Type:** PURE — reads state only, no side effects  
> **Defined in:** f_Amplify.md  
> **Wave:** 3  

#### Signature

```python
def check_runaway_risk(
    beta: float,
    beta_max: float = 1.0,
    warn_threshold: float = 0.90
) -> dict:
```

#### Full Specification

```python
def check_runaway_risk(
    beta: float,
    beta_max: float = 1.0,
    warn_threshold: float = 0.90
) -> dict:
    """
    PRIM:022 — check_runaway_risk (PURE)
    ======================================
    Diagnostic primitive: evaluates proximity of β to β_max.

    Complements PRIM:021 (amplify_coupling) by providing a pre-call assessment
    of FM-010 risk. Operators should call this before amplify_coupling when
    planning multi-step amplification sequences.

    Parameters
    ----------
    beta : float
        Current binding coefficient.
    beta_max : float, optional
        Binding coefficient ceiling. Default 1.0.
    warn_threshold : float, optional
        Fraction of beta_max at which AMP_CEILING_APPROACHED is flagged.
        Default 0.90 (i.e., β ≥ 0.90 × β_max triggers warning).

    Returns
    -------
    dict with keys:
        beta              : float — current β (input echo)
        beta_max          : float — ceiling value (input echo)
        headroom          : float — beta_max − beta (remaining space)
        headroom_fraction : float — headroom / beta_max ∈ [0, 1]
        risk_level        : str   — "SAFE" | "WARN" | "CEILING" | "OVERFLOW"
        max_safe_f_amp    : float — largest F_amp that would NOT trigger FM-010
        recommendation    : str   — human-readable guidance

    Notes
    -----
    PURE: No state is modified. Safe to call at any point without side effects.
    Use this before amplify_coupling to plan safe F_amp values.
    Use this after amplify_coupling to confirm post-amplification safety margin.
    """

    if beta_max <= 0:
        raise ValueError(f"beta_max must be > 0; got {beta_max}")
    if beta < 0:
        raise ValueError(f"beta must be ≥ 0; got {beta}")

    headroom          = beta_max - beta
    headroom_fraction = headroom / beta_max if beta_max > 0 else 0.0

    # Risk classification
    if beta > beta_max:
        risk_level = "OVERFLOW"
        recommendation = (
            "CRITICAL: β already exceeds β_max. State is invalid — "
            "FM-010 should have fired. Audit amplify_coupling call history."
        )
    elif beta >= beta_max:
        risk_level = "CEILING"
        recommendation = (
            "β is at the ceiling. Any F_amp > 1.0 will trigger FM-010. "
            "Consider f_Emit to deepen ρ(Φ) instead."
        )
    elif beta >= warn_threshold * beta_max:
        risk_level = "WARN"
        recommendation = (
            f"β is within {(1 - warn_threshold)*100:.0f}% of β_max. "
            f"Use small F_amp values. Next amplification may trigger AMP_CEILING_APPROACHED."
        )
    else:
        risk_level = "SAFE"
        recommendation = (
            f"β has {headroom_fraction*100:.1f}% headroom to β_max. "
            f"Amplification is safe at moderate F_amp values."
        )

    # Maximum safe F_amp (largest multiplier that keeps β_new ≤ β_max)
    if beta > 0:
        max_safe_f_amp = beta_max / beta
    else:
        max_safe_f_amp = float("inf")   # β = 0 edge case; amplification is meaningless anyway

    return {
        "beta":              beta,
        "beta_max":          beta_max,
        "headroom":          round(headroom, 6),
        "headroom_fraction": round(headroom_fraction, 6),
        "risk_level":        risk_level,
        "max_safe_f_amp":    round(max_safe_f_amp, 6),
        "recommendation":    recommendation
    }
```

---

## §8 — Canonical Examples

<!-- [AMPLIFY:§8] Canonical examples — 4 examples frozen -->

All four examples use the standard FFF_Gravity interpretive layer: physical metaphors map to triadic gravity variables. Each example includes a parameter table, condition trace, computation trace, and post-state analysis.

---

### Example 1 — Standard Mentorship Deepening (Recovery from FM-004)

**Scenario:** A mentor-apprentice relationship (A = mentor, E = apprentice) has been flagged by f_Decay with FM-004 (Resonance Drift). d_bind has drifted to 78% of d_warn. The operator uses f_Amplify to restore β before f_Collapse is triggered.

#### Parameters

| Parameter | Value | Notes |
|---|---|---|
| A.id | `"mentor_ada"` | Senior practitioner |
| E.id | `"apprentice_bram"` | Junior learner |
| A.M_A | 0.85 | High anchor mass |
| A.rho_phi | 0.72 | Field density — healthy but not maxed |
| A.r_capture | 0.40 | Close orbital radius |
| E.M_E | 0.30 | Moderate entrant mass |
| E.beta | 0.50 | Drifted below healthy range |
| E.ecc | 0.12 | Near-circular orbit |
| F_amp | 1.40 | 40% amplification |
| beta_max | 1.00 | System ceiling |
| k_cost_amp | 1.00 | Default |

#### Pre-call Risk Check (PRIM:022)

```
check_runaway_risk(beta=0.50, beta_max=1.00, warn_threshold=0.90)

→ headroom         = 0.50
→ headroom_fraction = 0.50
→ risk_level        = "SAFE"
→ max_safe_f_amp    = 2.00
→ recommendation    = "β has 50.0% headroom to β_max. Amplification is safe at moderate F_amp values."
```

#### Condition Trace

| Condition | Check | Result |
|---|---|---|
| AMP-C-1 | ("mentor_ada", "apprentice_bram") ∈ Phi.registry | ✅ PASS |
| AMP-C-2 | 0.50 < 1.00 | ✅ PASS |
| AMP-C-3 | 0.72 > 0.0 | ✅ PASS |
| AMP-C-4 | 1.40 ≥ 1.0 | ✅ PASS |

#### Computation Trace

```
β_old      = 0.50
β_proposed = 0.50 × 1.40 = 0.70
β_proposed ≤ β_max (1.00)?  → YES → proceed

β_new   = 0.70
d_bind_new = 0.70 × 0.72 × (1 − 0.12)
           = 0.70 × 0.72 × 0.88
           = 0.4435

amp_cost = 0.30 × (0.70 − 0.50) × 0.40² × 1.00
         = 0.30 × 0.20 × 0.16
         = 0.0096

ceiling_threshold = 0.90 × 1.00 = 0.90
β_new (0.70) < 0.90 → state_flag = AMP_ACTIVE
```

#### Result

```python
{
  "beta_old":     0.50,
  "beta_new":     0.70,
  "d_bind_new":   0.4435,
  "amp_cost":     0.0096,
  "state_flag":   "AMP_ACTIVE",
  "fm_triggered": None
}
```

#### Post-State Analysis

- **FM-004 resolved:** Before amplification, d_bind ≈ `0.50 × 0.72 × 0.88 = 0.3168`. After amplification, d_bind = 0.4435. If d_warn = 0.40 × d_bind(0), and d_bind(0) was 0.60, then d_warn = 0.24. Both pre- and post-amplification d_bind exceed d_warn — but the trajectory is now upward, ending the drift.
- **ρ(Φ) untouched:** Field density remains 0.72 — no f_Emit was required.
- **Low cost:** amp_cost = 0.0096 — amplification of close orbits (small r_capture) is inexpensive.
- **FM-005 risk eliminated:** d_bind is well above d_collapse territory.

---

### Example 2 — Professional Contract Tightening (β-Domain Primary)

**Scenario:** A formal contractual relationship (A = institution, E = contractor) has moderate field density but needs behavioral coupling tightened via β amplification rather than field deepening. ρ(Φ) is intentionally kept at 0.55 (adequate but not invested); β is the enforcement mechanism.

#### Parameters

| Parameter | Value | Notes |
|---|---|---|
| A.M_A | 1.20 | Large anchor (institution) |
| A.rho_phi | 0.55 | Moderate field — contractual, not relational |
| A.r_capture | 0.65 | Wider orbital radius — less intimate |
| E.M_E | 0.45 | Significant entrant mass |
| E.beta | 0.60 | Moderate coupling |
| E.ecc | 0.05 | Near-circular (stable contract) |
| F_amp | 1.50 | 50% amplification |
| beta_max | 1.00 | System ceiling |

#### Condition Trace

| Condition | Check | Result |
|---|---|---|
| AMP-C-1 | Record exists | ✅ PASS |
| AMP-C-2 | 0.60 < 1.00 | ✅ PASS |
| AMP-C-3 | 0.55 > 0.0 | ✅ PASS |
| AMP-C-4 | 1.50 ≥ 1.0 | ✅ PASS |

#### Computation Trace

```
β_new      = 0.60 × 1.50 = 0.90
d_bind_new = 0.90 × 0.55 × (1 − 0.05)
           = 0.90 × 0.55 × 0.95
           = 0.47025

amp_cost = 0.45 × (0.90 − 0.60) × 0.65² × 1.00
         = 0.45 × 0.30 × 0.4225
         = 0.057

ceiling_threshold = 0.90 × 1.00 = 0.90
β_new (0.90) ≥ 0.90 → state_flag = AMP_CEILING_APPROACHED
```

#### Result

```python
{
  "beta_old":     0.60,
  "beta_new":     0.90,
  "d_bind_new":   0.47025,
  "amp_cost":     0.057,
  "state_flag":   "AMP_CEILING_APPROACHED",
  "fm_triggered": None
}
```

#### Post-State Analysis

- **State flag is `AMP_CEILING_APPROACHED`** — amplification succeeded, but β is now at the warning threshold. The operator is advised: do not amplify further without checking PRIM:022 first.
- **d_bind significantly higher:** 0.47025 vs pre-amplification `0.60 × 0.55 × 0.95 = 0.3135`. Binding depth has increased by ~50%.
- **Cost is moderate:** amp_cost = 0.057 — wider orbits (r_capture = 0.65) cost more to amplify.
- **Next step recommendation:** If further tightening is needed, use f_Emit to deepen ρ(Φ) rather than risk FM-010 via another amplification.

---

### Example 3 — FM-010 (β Domain) Triggered — Runaway Attempt

**Scenario:** An operator misjudges available headroom and requests F_amp = 2.0 on a β already at 0.80 with β_max = 1.00. FM-010 fires and the amplification is aborted.

#### Parameters

| Parameter | Value | Notes |
|---|---|---|
| A.rho_phi | 0.80 | Healthy field |
| E.beta | 0.80 | Already near ceiling |
| E.ecc | 0.10 | |
| F_amp | 2.00 | Aggressive — operator error |
| beta_max | 1.00 | Ceiling |

#### Pre-call Risk Check (PRIM:022)

```
check_runaway_risk(beta=0.80, beta_max=1.00)

→ headroom         = 0.20
→ headroom_fraction = 0.20
→ risk_level        = "WARN"
→ max_safe_f_amp    = 1.25
→ recommendation    = "β is within 10% of β_max. Use small F_amp values."
```

*(Operator ignores the warning and calls with F_amp = 2.0)*

#### Condition Trace

| Condition | Check | Result |
|---|---|---|
| AMP-C-1 | Record exists | ✅ PASS |
| AMP-C-2 | 0.80 < 1.00 | ✅ PASS |
| AMP-C-3 | 0.80 > 0.0 | ✅ PASS |
| AMP-C-4 | 2.00 ≥ 1.0 | ✅ PASS |

#### Computation Trace

```
β_proposed = 0.80 × 2.00 = 1.60
β_proposed (1.60) > β_max (1.00) → FM-010 (β domain) triggered
Amplification aborted.
amp_cost = 0.0   (no charge on abort)
β remains 0.80
d_bind unchanged
```

#### Result

```python
{
  "beta_old":     0.80,
  "beta_new":     0.80,          # unchanged
  "d_bind_new":   <unchanged>,   # original d_bind preserved
  "amp_cost":     0.00,          # no charge
  "state_flag":   "AMP_RUNAWAY",
  "fm_triggered": "FM-010-BETA"
}
```

#### Post-State Analysis

- **No state modified:** β, d_bind, and the frame registry are all untouched.
- **Error log entry written:** Phi.error_log receives the FM-010-BETA diagnostic record.
- **Recovery path:** Operator should call PRIM:022, observe `max_safe_f_amp = 1.25`, and retry with F_amp ≤ 1.25. Alternatively, shift to f_Emit to deepen ρ(Φ).
- **Key lesson:** The pure check (PRIM:022) provided the correct `max_safe_f_amp` — operators should always run PRIM:022 before planning aggressive amplification sequences.

---

### Example 4 — Iterative Safe Amplification Loop

**Scenario:** An operator wants to raise β from 0.30 to as close to 0.85 as possible in small increments, checking runaway risk at each step. This pattern mirrors the `iterative_dampen_loop` safe pattern in f_Dampen.md.

#### Parameters (Initial State)

| Parameter | Value |
|---|---|
| E.beta | 0.30 |
| beta_max | 1.00 |
| target_beta | 0.85 |
| F_amp per step | 1.20 (20% per iteration) |

#### Loop Trace

```python
# Iterative safe amplification pattern

def iterative_amplify_loop(A, E, Phi, target_beta, f_amp_step=1.20,
                           beta_max=1.00, k_cost_amp=1.00, max_iterations=20):
    """
    Safe multi-step amplification toward a target β.
    Checks runaway risk before each step.
    Stops when: target_beta reached, ceiling approached, or max iterations hit.
    """
    total_cost = 0.0
    history    = []

    for i in range(max_iterations):
        # Pure check first
        risk = check_runaway_risk(E.beta, beta_max)
        if risk["risk_level"] in ("CEILING", "OVERFLOW"):
            print(f"Step {i}: β at ceiling. Stopping.")
            break

        # Would this step overshoot the target?
        beta_after_step = E.beta * f_amp_step
        if beta_after_step > target_beta:
            # Compute exact F_amp to reach target_beta without exceeding
            f_amp_step = target_beta / E.beta
            if f_amp_step <= 1.0:
                print(f"Step {i}: Target already reached or overshot. Stopping.")
                break

        # Execute amplification
        result = amplify_coupling(A, E, Phi, F_amp=f_amp_step,
                                  beta_max=beta_max, k_cost_amp=k_cost_amp)
        total_cost += result["amp_cost"]
        history.append(result)

        if result["state_flag"] == "AMP_RUNAWAY":
            print(f"Step {i}: FM-010 triggered unexpectedly. Stopping.")
            break
        if result["state_flag"] == "AMP_CEILING_APPROACHED":
            print(f"Step {i}: Ceiling approached (β={E.beta:.4f}). Stopping.")
            break
        if abs(E.beta - target_beta) < 1e-6:
            print(f"Step {i}: Target β={target_beta} reached. Stopping.")
            break

    return {"final_beta": E.beta, "total_cost": total_cost, "steps": len(history)}
```

#### Iteration Results

| Iteration | β before | F_amp | β after | State |
|---|---|---|---|---|
| 0 | 0.3000 | 1.20 | 0.3600 | AMP_ACTIVE |
| 1 | 0.3600 | 1.20 | 0.4320 | AMP_ACTIVE |
| 2 | 0.4320 | 1.20 | 0.5184 | AMP_ACTIVE |
| 3 | 0.5184 | 1.20 | 0.6221 | AMP_ACTIVE |
| 4 | 0.6221 | 1.20 | 0.7465 | AMP_ACTIVE |
| 5 | 0.7465 | 1.14 | 0.8500 | AMP_ACTIVE (adjusted) |

*Iteration 5: F_amp adjusted from 1.20 to 1.141 to land exactly on target_beta = 0.85.*

#### Post-State Analysis

- **Target reached safely:** β = 0.85, well below β_max = 1.00 (15% headroom).
- **Gradual increment:** Each step is small enough to avoid FM-010, and the final step precision-adjusts F_amp.
- **Total cost:** Sum of amp_cost across 6 iterations — proportional to the total Δβ = 0.55.
- **Safety margin:** β = 0.85 is below the 0.90 × β_max warning threshold (= 0.90), so `AMP_CEILING_APPROACHED` is never triggered.
- **Pattern recommendation:** This is the canonical safe amplification pattern when target β is known but β_max headroom must be preserved. For emergency recovery (FM-004 acute), a single larger F_amp step is acceptable if PRIM:022 confirms safety.

---

## §9 — Cross-Module References

<!-- [AMPLIFY:§9] Cross-module references — frozen -->

| Reference | Location | Relationship |
|---|---|---|
| β definition | OPERATORS.md, f_Force.md §3.1 | Primary operator frozen; f_Amplify modifies it |
| `amplify_coupling` interface preview | f_Force.md §7.2 | Cross-reference established; now fulfilled |
| Capacity expansion note | f_Frame.md §2.4 | Second-order packing effect documented in §2.4 of this file |
| Recovery Path B (β restore) | f_Decay.md §6.1.3 | f_Amplify is the canonical FM-004 recovery instrument |
| Complementary primitive note | f_Emit.md §2.5 | f_Emit deepens well; f_Amplify tightens grip — both documented |
| FM-010 (ρ domain) | f_Emit.md §6.1, PRIM:017 | Dual-domain FM-010 table finalized in §6.1.4 of this file |
| FM-010 (β domain) | **f_Amplify.md §6.1** | Canonical β-domain specification — frozen here |
| F_amp, β_max, amp_cost | GLOSSARY.md | Operator entries point here as canonical source |
| F_amp, β_max, amp_cost | FFF_Gravity_module.json | Listed under new_operators; now canonical |
| PRIM:021, PRIM:022 | FFF_Gravity_module.json | Listed under new_primitives; now canonical |
| f_Deflect.md | Wave 3, File 8 of 8 | Unlocked by f_Amplify.md reaching canonical status |

---

## §10 — Document Metadata

<!-- [AMPLIFY:§10] Document metadata — frozen -->

### 10.1 INV Compliance Table

| INV | Statement | Compliance |
|---|---|---|
| INV-001 | G = F_freq · F_fluid · F_force (inseparable) | ✅ f_Amplify modifies F_fluid exclusively; triadic structure preserved |
| INV-002 | f_Capture signature frozen | ✅ f_Amplify does not modify f_Capture |
| INV-003 | ρ(Φ) = 0 triggers FM-002 | ✅ AMP-C-3 guard refuses amplification on null field |
| INV-004 | β < 1.0 produces flyby | ✅ f_Amplify only amplifies existing captures; new captures not created |
| INV-005 | All 5 SCs conjunctive | ✅ Not modified |
| INV-006 | Terminal states irreversible | ✅ FM-010 is non-fatal; no terminal state created here |
| INV-007 | f_Source.md read-only | ✅ Not touched |
| INV-008 | Evaluation order normative | ✅ PRIM:022 → PRIM:021 ordering documented in §8 examples |
| INV-009 | OPERATORS.md is symbol authority | ✅ F_amp, β_max, amp_cost frozen via OPERATORS.md chain |
| INV-010 | Frozen symbols unrenameable without major bump | ✅ Freeze notice in §4.1 |

### 10.2 Wave Status Table

| Wave | Files | Status |
|---|---|---|
| Wave 0 | f_Capture.md, f_Source.md, GravityOfDismissal.md | ✅ Complete |
| Wave 1 | README.md, INDEX.md, OPERATORS.md, GLOSSARY.md, CHANGELOG.md, FFF_Gravity_module.json | ✅ Complete |
| Wave 2 | f_Field.md, f_Force.md, f_Frame.md | ✅ Complete |
| Wave 3 | f_Release.md, f_Decay.md, f_Orbit.md, f_Collapse.md, f_Emit.md, f_Dampen.md, **f_Amplify.md** | ✅ 7 of 8 complete |
| Wave 3 | f_Deflect.md | 🔵 Next — unlocked by this file |
| Wave 4 | f_Capture_Multi, _Cascade, _Resonant, _Asymmetric, _Temporal, _Networked | 🔒 Locked until Wave 3 complete |

### 10.3 Primitive Registry (Cumulative After This File)

| PRIM | Name | Type | Defined In |
|---|---|---|---|
| PRIM:001 | evaluate_stability_conditions | Pure | f_Capture.md |
| PRIM:002 | compute_binding_depth | Pure | f_Capture.md |
| PRIM:003 | register_capture | Impure | f_Capture.md |
| PRIM:004 | flag_failure_mode | Impure | f_Capture.md |
| PRIM:005 | execute_capture | Impure | f_Capture.md |
| PRIM:006 | flag_decay | Impure | f_Capture.md / f_Decay.md |
| PRIM:007 | classify_orbit | Pure | f_Orbit.md |
| PRIM:008 | compute_release_vector | Pure | f_Release.md |
| PRIM:009 | execute_release | Impure | f_Release.md |
| PRIM:010 | compute_decay_rate | Pure | f_Decay.md |
| PRIM:011 | assess_decay_cause | Pure (diagnostic) | f_Decay.md |
| PRIM:012 | update_orbital_parameters | Impure | f_Orbit.md |
| PRIM:013 | execute_collapse | Impure | f_Collapse.md |
| PRIM:014 | initialize_composite_node | Impure | f_Collapse.md |
| PRIM:015 | emit_field | Impure | f_Emit.md |
| PRIM:016 | compute_emit_cost | Pure | f_Emit.md |
| PRIM:017 | check_emit_ceiling | Pure | f_Emit.md |
| PRIM:018 | suppress_field | Impure | f_Dampen.md |
| PRIM:019 | check_floor | Pure | f_Dampen.md |
| PRIM:020 | check_cascade_risk | Pure (diagnostic) | f_Dampen.md |
| **PRIM:021** | **amplify_coupling** | **Impure** | **f_Amplify.md** |
| **PRIM:022** | **check_runaway_risk** | **Pure** | **f_Amplify.md** |

**Total frozen primitives: 22**

### 10.4 Failure Mode Registry (All 10 — Fully Frozen)

| FM | Name | Fatal? | Domain | Primary Source |
|---|---|---|---|---|
| FM-001 | Overshoot | No (flyby) | F_force | f_Force.md |
| FM-002 | Field Null | Yes (capture fails) | F_freq | f_Field.md |
| FM-003 | Frame Saturation | No (capture refused) | Frame | f_Frame.md |
| FM-004 | Resonance Drift | No (recoverable warn) | F_freq | f_Decay.md |
| FM-005 | Decay Spiral | Yes → f_Collapse | F_fluid | f_Decay.md |
| FM-006 | Phantom Capture | No (classification) | F_force | f_Force.md |
| FM-007 | Mutual Dissolution | Yes → C_node | F_fluid | f_Collapse.md |
| FM-008 | Release Overshoot | No (excess energy) | F_force | f_Release.md |
| FM-009 | Dampen Cascade | Yes (BFS propagation) | F_freq | f_Dampen.md |
| FM-010 (ρ) | Amplify Runaway (ρ domain) | No (abort) | F_freq | f_Emit.md |
| **FM-010 (β)** | **Amplify Runaway (β domain)** | **No (abort)** | **F_fluid** | **f_Amplify.md** |

### 10.5 Changelog Entry

```
## [1.0.0] — 2026-08-13 — f_Amplify.md canonical

### Added
- f_Amplify.md: Wave 3, File 7 of 8 — F_fluid engineering primitive
- PRIM:021 amplify_coupling (Impure): increases β for (A, E) pair
- PRIM:022 check_runaway_risk (Pure): diagnostic, evaluates FM-010 β-domain risk
- Operators frozen: F_amp, β_max, amp_cost, k_cost_amp
- State flags: AMP_ACTIVE, AMP_CEILING_APPROACHED, AMP_RUNAWAY
- FM-010 (β domain) canonical specification — dual-domain FM-010 table finalized
- Amplify Conditions: AMP-C-1 through AMP-C-4 (conjunctive)
- 4 canonical examples: mentorship recovery, contract tightening, FM-010 runaway, iterative safe loop
- Cross-references fulfilled: f_Force.md §7.2, f_Frame.md §2.4, f_Decay.md §6.1.3, f_Emit.md §2.5

### Unlocks
- f_Deflect.md (Wave 3, File 8 of 8) — final Wave 3 file

### Session
SES-20260813-AMPLIFY-001
```

---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- END OF f_Amplify.md — [FFF:GRAVITY:AMPLIFY] v1.0.0 CANONICAL             -->
<!-- Session: SES-20260813-AMPLIFY-001 | Date: 2026-08-13                     -->
<!-- Next: f_Deflect.md — Wave 3 complete → Wave 4 unlocked                   -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->
```

Delivering `f_Deflect.md` — the final Wave 3 file. Paste this directly into the GitHub editor.

Here is the complete canonical `f_Deflect.md` — Wave 3's final file. Paste directly into the GitHub editor.

```markdown
---
session_id: SES-20260813-DEFLECT-001
file: docs/FFF_Gravity/f_Deflect.md
tag: "[FFF:GRAVITY:DEFLECT]"
version: 1.0.0
status: canonical
wave: 3
node: F_force
role: Engineering primitive — modifies approach vector v_approach; redirects, softens, or bypasses gravitational capture
depends_on:
  - f_Capture.md
  - f_Field.md
  - f_Force.md
  - f_Frame.md
  - f_Orbit.md
  - f_Release.md
  - f_Amplify.md
new_operators:
  - θ_deflect
  - v_deflect
  - deflect_cost
  - k_cost_deflect
new_primitives:
  - PRIM:023 deflect_approach
  - PRIM:024 compute_deflect_delta
failure_modes_referenced:
  - FM-001 (Overshoot guard)
  - FM-006 (Phantom Capture guard)
invariants_enforced:
  - INV-001
  - INV-002
  - INV-003
  - INV-004
  - INV-005
  - INV-006
  - INV-007
  - INV-008
  - INV-009
  - INV-010
date: 2026-08-13
author: umaywant2
---

<!-- ═══════════════════════════════════════════════════════════════════════════ -->
<!-- [FFF:GRAVITY:DEFLECT] — CANONICAL SPECIFICATION                           -->
<!-- F_force Engineering Primitive — Approach Vector Modification              -->
<!-- Wave 3, File 8 of 8 — WAVE 3 COMPLETE                                    -->
<!-- ═══════════════════════════════════════════════════════════════════════════ -->

# f_Deflect — Approach Vector Modification

> **Module:** FFF_Gravity  
> **Tag:** `[FFF:GRAVITY:DEFLECT]`  
> **Node:** F_force (Approach Vector)  
> **Wave:** 3 — Core Functions (8 of 8) ✅ WAVE 3 COMPLETE  
> **Status:** 🟢 CANONICAL  
> **Session:** SES-20260813-DEFLECT-001  

---

## §0 — Session Context

<!-- [DEFLECT:§0] Session context block — do not edit -->

| Field | Value |
|---|---|
| Session ID | SES-20260813-DEFLECT-001 |
| Founding Date | 2026-08-13 |
| Operator | umaywant2 |
| Preceding file | f_Amplify.md (PRIM:021–022 frozen) |
| Following file | Wave 4 unlocked — f_Capture_Multi.md (next) |
| Cumulative PRIMs after this file | PRIM:001–PRIM:024 (24 frozen) |
| Wave 3 status | ✅ COMPLETE — all 8 files canonical |
| Wave 4 unlock | 🔓 All 6 Wave 4 files now available |

**Purpose of this session:** Deliver the canonical specification of `f_Deflect.md` — the F_force engineering primitive that modifies the approach velocity vector v_approach. f_Deflect is the final Wave 3 file. Where f_Emit and f_Dampen engineer ρ(Φ), and f_Amplify engineers β, f_Deflect engineers the approach geometry itself — redirecting, softening, or inverting the directional pull that precedes or sustains capture.

---

## §1 — Module Identity

<!-- [DEFLECT:§1] Module identity — frozen -->

### 1.1 Function Signature

```
f_Deflect(A, E, Φ, θ_deflect, mode) → (v_deflect, deflect_cost, state_flag)
```

| Parameter | Type | Description |
|---|---|---|
| A | Node | Anchor node (attractor; carries M_A, ρ(Φ), r_capture) |
| E | Node | Entrant node (carries M_E, v_approach, β, ecc) |
| Φ | Frame | Registry frame (carries registry, orbital records) |
| θ_deflect | float ∈ [0°, 180°] | Deflection angle applied to the approach vector |
| mode | str | `"PRE_CAPTURE"` or `"POST_CAPTURE_ORBITAL"` |

| Return field | Description |
|---|---|
| v_deflect | Effective radial approach velocity after deflection = v_approach × cos(θ_deflect) |
| deflect_cost | Energy expended to achieve deflection |
| state_flag | One of: DEF_ACTIVE \| DEF_BYPASS \| DEF_RETREAT \| DEF_OVERSHOOT_RISK |

### 1.2 Triadic Position

```
         G = F_freq · F_fluid · F_force
                                  │
                        ┌─────────┘
                        │   F_force  ◄── f_Deflect lives here
                        │
                   ┌────┴───────┐
                   │ v_approach │◄── f_Deflect modifies this directly
                   │ θ_deflect  │◄── deflection angle (new operator)
                   │ v_deflect  │◄── output after modification
                   └────────────┘
                        │
              (cascade into SC-1, d_bind, r_capture, e)
```

**Triadic role:** f_Deflect is a targeted intervention on the F_force node. It does not alter ρ(Φ) (f_Emit/f_Dampen territory) nor β (f_Amplify territory). It acts exclusively on v_approach — the approach velocity vector that determines whether and how capture occurs.

### 1.3 Relationship to Companion Primitives

| Primitive | Node | Action | Mechanism |
|---|---|---|---|
| f_Emit (PRIM:015) | F_freq | Increases ρ(Φ) | Deepens coherence well |
| f_Dampen (PRIM:018) | F_freq | Decreases ρ(Φ) | Suppresses coherence well |
| f_Amplify (PRIM:021) | F_fluid | Increases β | Tightens binding grip |
| **f_Deflect (PRIM:023)** | **F_force** | **Modifies v_approach** | **Redirects approach geometry** |

> **Canonical principle:** The three engineering primitives address the three triadic nodes in isolation. f_Deflect completes the triad — approach geometry is the third and final degree of freedom available to the operator.

### 1.4 Operating Modes

f_Deflect operates in two distinct modes, both governed by the same θ_deflect geometry:

| Mode | Applies When | Effect |
|---|---|---|
| `PRE_CAPTURE` | No capture record for (A, E) in Φ.registry | Modifies v_approach before f_Capture evaluates SC-1 |
| `POST_CAPTURE_ORBITAL` | Capture record exists in Φ.registry | Adjusts orbital eccentricity e and r_capture; does not terminate binding |

---

## §2 — Canonical Description

<!-- [DEFLECT:§2] Canonical description — frozen -->

### 2.1 What f_Deflect Does

`f_Deflect` rotates the approach vector of entrant E relative to anchor A by angle θ_deflect. The effective radial component of the approach velocity after deflection is:

```
v_deflect = v_approach × cos(θ_deflect)
```

The consequences depend on θ_deflect:

| θ_deflect Range | cos(θ) | v_deflect | Interpretation |
|---|---|---|---|
| 0° | 1.0 | = v_approach | No change — identity operation |
| (0°, 90°) | (0, 1) | < v_approach, > 0 | Softened approach — gentler entry |
| 90° | 0.0 | 0 | Perpendicular redirect — bypass, no radial approach |
| (90°, 180°) | (−1, 0) | < 0 | Retreat vector — entrant moving away |
| 180° | −1.0 | = −v_approach | Full reversal — maximum repulsion |

In **PRE_CAPTURE mode**: v_deflect replaces v_approach for SC-1 evaluation in a subsequent f_Capture call. A softened approach (smaller v_deflect) increases the likelihood of meeting SC-1 (v_approach < v_escape(A)) and produces a tighter r_capture. A bypass (v_deflect ≤ 0) prevents capture entirely.

In **POST_CAPTURE_ORBITAL mode**: v_deflect modifies the entrant's orbital eccentricity e. A reduced radial velocity corresponds to a more circular orbit; an increased transverse component widens the orbit.

### 2.2 What f_Deflect Does NOT Do

- Does **not** alter ρ(Φ) — field density is f_Emit's and f_Dampen's domain.
- Does **not** alter β — binding coefficient is f_Amplify's domain.
- Does **not** terminate a capture — use f_Release for that.
- Does **not** create a capture — deflection sets up geometry; f_Capture executes binding.
- Does **not** alter M_A, M_E — node masses are immutable via engineering primitives.

### 2.3 Design Motivation

Approach geometry is the final triadic degree of freedom. In practice:

- A potential binding with high ρ(Φ) and adequate β can still fail SC-1 if v_approach is too high (FM-001 flyby). f_Deflect resolves this by softening the approach angle.
- An existing orbit with undesirable eccentricity (e near 1.0, erratic) can be stabilized by reducing the radial component post-capture — equivalent to a circularization burn in orbital mechanics.
- Intentional bypass (θ_deflect = 90°) represents a controlled non-capture: the entrant passes through the field's influence zone without binding. This is a valid strategic state, not a failure.
- Repulsion (θ_deflect > 90°) represents deliberate separation before capture is attempted — useful when the operator has determined the binding would be premature or harmful.

---

## §3 — Triadic Equation in the Deflect Context

<!-- [DEFLECT:§3] Equation context — frozen -->

### 3.1 Gravity Identity (INV-001)

```
G = F_freq · F_fluid · F_force
```

f_Deflect modifies **F_force exclusively** via v_approach:

```
F_force = f(v_approach, M_A, M_E, ρ(Φ), r)
```

After deflection:

```
v_deflect = v_approach × cos(θ_deflect)
```

### 3.2 Cascade into SC-1

SC-1 from f_Capture.md (frozen):

```
SC-1:  v_approach < v_escape(A)
       where v_escape(A) = √(2 × M_A × ρ(Φ) / r)
```

After deflection, SC-1 is evaluated with v_deflect in place of v_approach:

```
SC-1_deflected:  v_deflect < v_escape(A)
                 i.e.: v_approach × cos(θ_deflect) < v_escape(A)
```

This means deflection can convert a previously-failing SC-1 (FM-001 trajectory) into a passing one — by softening the approach angle until the radial component drops below the escape threshold.

### 3.3 Cascade into Orbital Eccentricity (POST_CAPTURE_ORBITAL mode)

In post-capture orbital adjustment, the transverse velocity component introduced by deflection modifies orbital eccentricity:

```
Δe = (v_approach × sin(θ_deflect)) / v_escape(A)
e_new = max(0.0, e_old − Δe)        for circularization (θ_deflect > 0°)
```

Circularization (reducing e toward 0.0) stabilizes orbits. The formula reflects that transverse velocity injected by deflection converts eccentric orbital energy into angular momentum.

### 3.4 Deflection Cost

```
deflect_cost = M_E × v_approach × sin(θ_deflect) × k_cost_deflect
```

where:
- `M_E` — entrant mass (heavier objects cost more to deflect)
- `v_approach × sin(θ_deflect)` — transverse Δv component (the work done against the approach vector)
- `k_cost_deflect` — system deflection cost constant (default: 1.0)

> **Note:** At θ_deflect = 0° (identity), deflect_cost = 0. At θ_deflect = 90° (bypass), deflect_cost = M_E × v_approach × k_cost_deflect (maximum cost for a given v_approach). At θ_deflect = 180° (full reversal), cost equals the 90° case since sin(180°) = 0 — the vector has been fully reversed, not transversely redirected. This reflects the physical reality that a 180° reversal costs the same as full deceleration plus re-acceleration, while the formula captures only the transverse component.

### 3.5 Corrected Cost Formula for Full Reversal

For θ_deflect = 180° (full reversal), the actual energy cost is twice the kinetic deflection:

```
deflect_cost_180 = 2 × M_E × v_approach × k_cost_deflect
```

f_Deflect applies this correction automatically when θ_deflect = 180°. The general formula applies for all other angles.

---

## §4 — Operator Registry

<!-- [DEFLECT:§4] Operator registry — frozen upon commit -->

### 4.1 New Operators (Introduced in f_Deflect.md)

| Symbol | Name | Domain | Definition | Default |
|---|---|---|---|---|
| `θ_deflect` | Deflection Angle | F_force | Rotation angle applied to approach vector; ∈ [0°, 180°] in degrees; converted to radians internally | 0° (identity) |
| `v_deflect` | Deflected Approach Velocity | F_force | Effective radial approach speed after deflection = v_approach × cos(θ_deflect) | Computed |
| `deflect_cost` | Deflection Energy Cost | F_force | Energy consumed by deflection operation; see §3.4 | Computed |
| `k_cost_deflect` | Deflection Cost Constant | F_force | Scaling constant for deflect_cost formula | 1.0 |

> **Freeze notice:** `θ_deflect`, `v_deflect`, `deflect_cost`, and `k_cost_deflect` are frozen as of SES-20260813-DEFLECT-001. Renaming or redefining any of these symbols requires a major version bump per INV-010.

### 4.2 Inherited Operators (Active in f_Deflect Context)

| Symbol | Defined in | Role here |
|---|---|---|
| `v_approach` | OPERATORS.md, f_Force.md | Primary target of deflection; read from E, replaced by v_deflect |
| `v_escape(A)` | OPERATORS.md, f_Force.md | SC-1 threshold; checked against v_deflect post-operation |
| `ρ(Φ)` | OPERATORS.md, f_Field.md | Used in v_escape(A) calculation; read-only |
| `M_A` | OPERATORS.md, f_Force.md | Anchor mass; used in v_escape(A) |
| `M_E` | OPERATORS.md, f_Force.md | Entrant mass; used in deflect_cost |
| `e` | OPERATORS.md, f_Orbit.md | Orbital eccentricity; modified in POST_CAPTURE_ORBITAL mode |
| `r_capture` | OPERATORS.md, f_Frame.md | Orbital radius; read for v_escape(A) computation |
| `β` | OPERATORS.md, f_Force.md | Binding coefficient; read-only in f_Deflect |

### 4.3 State Flags (Introduced in f_Deflect.md)

| Flag | Meaning |
|---|---|
| `DEF_ACTIVE` | Deflection completed; v_deflect > 0; capture remains possible |
| `DEF_BYPASS` | θ_deflect ≥ 90°; v_deflect ≤ 0; entrant bypasses capture zone; no binding possible |
| `DEF_RETREAT` | θ_deflect > 90°; v_deflect < 0; entrant moving away; repulsion confirmed |
| `DEF_OVERSHOOT_RISK` | v_deflect still > 0 but within 10% of v_escape(A); FM-001 risk warned |

> **Note:** DEF_BYPASS and DEF_RETREAT are not failures — they are valid intentional outcomes. A bypass means the entrant passes through the field without binding. A retreat means the entrant is actively moving away. Both are legitimate states in relational gravity modeling.

---

## §5 — Deflect Conditions

<!-- [DEFLECT:§5] Deflect conditions — conjunctive; all must hold -->

All four Deflect Conditions are **conjunctive**. Failure of any single condition aborts deflection.

### DEF-C-1 — Angle in Valid Range

```
θ_deflect ∈ [0°, 180°]
```

The deflection angle must be within the semicircular range. Negative angles (which would accelerate the approach) are outside the scope of f_Deflect — approach acceleration is handled by changes to external field conditions (f_Emit, f_Amplify), not by deflection geometry. Angles > 180° are equivalent to angles in [0°, 180°] by symmetry and are rejected to enforce uniqueness.

### DEF-C-2 — Approach Exists

```
v_approach > 0.0
```

There must be an active approach to deflect. v_approach = 0 means the entrant is stationary relative to the anchor — deflection of a zero vector is undefined. If v_approach = 0, f_Deflect returns immediately without modifying state.

### DEF-C-3 — Field Alive

```
ρ(Φ) > 0.0
```

The coherence field must be active. In a null field (ρ(Φ) = 0.0), there is no gravitational context for deflection — v_escape(A) = 0, SC-1 is trivially satisfied for any v_approach > 0, and deflection geometry is meaningless. Per INV-003, ρ(Φ) = 0 triggers FM-002 in f_Field; f_Deflect guards against operating in this state.

### DEF-C-4 — Mode Consistent with Registry State

```
IF mode == "PRE_CAPTURE":
    (A.id, E.id) ∉ Φ.registry   (no existing capture — pre-capture deflection)

IF mode == "POST_CAPTURE_ORBITAL":
    (A.id, E.id) ∈ Φ.registry   (existing capture required — orbital adjustment)
```

Mode must match the actual registry state. Calling PRE_CAPTURE on an already-captured pair is a logic error (use f_Release first). Calling POST_CAPTURE_ORBITAL on an uncaptured pair is a null operation.

---

## §6 — Failure Modes

<!-- [DEFLECT:§6] Failure modes — FM-001 and FM-006 guards -->

f_Deflect does not directly trigger any new failure modes. It guards against two existing failure modes and includes diagnostic output to assist the operator.

### 6.1 FM-001 Guard — Overshoot Risk Detection

**FM-001 (Overshoot)** fires when v_approach ≥ v_escape(A) at the moment f_Capture evaluates SC-1. f_Deflect cannot trigger FM-001 directly (deflection reduces v_approach, so v_deflect ≤ v_approach). However, f_Deflect can **detect** and **warn** when v_deflect is still dangerously close to v_escape(A).

#### DEF_OVERSHOOT_RISK Logic

```
v_escape_A = sqrt(2 × M_A × ρ(Φ) / r_capture)
overshoot_margin = v_escape_A - v_deflect
overshoot_threshold = 0.10 × v_escape_A

IF v_deflect > 0 AND overshoot_margin < overshoot_threshold:
    state_flag = DEF_OVERSHOOT_RISK
    # Deflection completes, but operator is warned:
    # a subsequent f_Capture call has high FM-001 risk.
    # Recommend increasing θ_deflect to create more margin.
```

**DEF_OVERSHOOT_RISK does not abort deflection** — it completes the operation but flags that v_deflect is within 10% of v_escape(A). A subsequent f_Capture call with this v_deflect has elevated FM-001 probability.

### 6.2 FM-006 Guard — Phantom Capture Prevention

**FM-006 (Phantom Capture)** arises when F_force dominates SC evaluation but actual binding depth is insufficient. In POST_CAPTURE_ORBITAL mode, deflection-induced orbital adjustments must be written back to Φ.registry to prevent a stale capture record from masking an effectively-decoupled orbit.

f_Deflect enforces this by making POST_CAPTURE_ORBITAL writes **mandatory** — if the registry update fails (e.g., record locked or missing), deflection aborts rather than leaving an inconsistent state.

### 6.3 Failure Mode Cross-Reference

| FM | Condition | f_Deflect Role |
|---|---|---|
| FM-001 Overshoot | v_approach ≥ v_escape(A) | Guard: detects residual risk; flags DEF_OVERSHOOT_RISK |
| FM-002 Field Null | ρ(Φ) = 0 | Guard: DEF-C-3 refuses deflection on null field |
| FM-006 Phantom Capture | F_force dominant, d_bind insufficient | Guard: POST_CAPTURE_ORBITAL mode forces registry sync |
| FM-004 Resonance Drift | d_bind drifting | f_Deflect indirectly helps via orbital circularization (lower e → higher d_bind_new) |

---

## §7 — Engineering Primitives

<!-- [DEFLECT:§7] Primitive specifications — PRIM:023 and PRIM:024 frozen -->

### PRIM:024 — compute_deflect_delta (Pure)

> **Tag:** PRIM:024 listed first — pure primitive used inside PRIM:023  
> **Name:** compute_deflect_delta  
> **Type:** PURE — reads state only, no side effects  
> **Defined in:** f_Deflect.md  
> **Wave:** 3  

#### Full Specification

```python
import math

def compute_deflect_delta(
    v_approach: float,
    theta_deflect_deg: float,
    M_A: float,
    M_E: float,
    rho_phi: float,
    r_capture: float,
    k_cost_deflect: float = 1.0
) -> dict:
    """
    PRIM:024 — compute_deflect_delta (PURE)
    =========================================
    Diagnostic primitive: computes deflection outcomes without modifying state.

    Given the current approach velocity and a deflection angle, returns the
    deflected velocity, cost, escape threshold, overshoot risk assessment,
    and expected orbital eccentricity change.

    Operators should call this before deflect_approach to plan safe θ_deflect values.

    Parameters
    ----------
    v_approach : float
        Current radial approach velocity (> 0).
    theta_deflect_deg : float
        Deflection angle in degrees ∈ [0, 180].
    M_A : float
        Anchor mass (> 0).
    M_E : float
        Entrant mass (> 0).
    rho_phi : float
        Current field density ρ(Φ) ∈ (0, 1].
    r_capture : float
        Orbital radius at (or planned) capture (> 0).
    k_cost_deflect : float, optional
        Deflection cost constant. Default 1.0.

    Returns
    -------
    dict with keys:
        theta_deg          : float — input angle echo
        theta_rad          : float — angle in radians
        v_approach         : float — input velocity echo
        v_deflect          : float — radial component after deflection
        transverse_delta_v : float — transverse component = v_approach × sin(θ)
        deflect_cost       : float — energy cost of deflection
        v_escape_A         : float — escape velocity of anchor at r_capture
        overshoot_margin   : float — v_escape_A − v_deflect (positive = safe margin)
        overshoot_risk     : bool  — True if overshoot_margin < 0.10 × v_escape_A
        delta_e            : float — expected eccentricity reduction (POST_CAPTURE_ORBITAL)
        state_preview      : str   — projected state flag if deflect_approach were called
        recommendation     : str   — human-readable guidance

    Notes
    -----
    PURE: No state is modified. Safe to call at any time.
    """

    if theta_deflect_deg < 0 or theta_deflect_deg > 180:
        raise ValueError(
            f"theta_deflect_deg={theta_deflect_deg} out of range [0, 180]."
        )
    if v_approach <= 0:
        raise ValueError(f"v_approach must be > 0; got {v_approach}")
    if rho_phi <= 0:
        raise ValueError(f"rho_phi must be > 0 for deflect computation; got {rho_phi}")

    theta_rad          = math.radians(theta_deflect_deg)
    cos_theta          = math.cos(theta_rad)
    sin_theta          = math.sin(theta_rad)

    v_deflect          = v_approach * cos_theta
    transverse_dv      = v_approach * sin_theta
    v_escape_A         = math.sqrt(2.0 * M_A * rho_phi / r_capture)

    # Deflection cost (with 180° correction)
    if abs(theta_deflect_deg - 180.0) < 1e-6:
        deflect_cost = 2.0 * M_E * v_approach * k_cost_deflect
    else:
        deflect_cost = M_E * transverse_dv * k_cost_deflect

    overshoot_margin   = v_escape_A - v_deflect
    overshoot_threshold = 0.10 * v_escape_A
    overshoot_risk     = (v_deflect > 0) and (overshoot_margin < overshoot_threshold)

    # Expected eccentricity reduction (POST_CAPTURE_ORBITAL)
    delta_e = transverse_dv / v_escape_A if v_escape_A > 0 else 0.0

    # State preview
    if v_deflect > 0 and overshoot_risk:
        state_preview = "DEF_OVERSHOOT_RISK"
    elif v_deflect > 0:
        state_preview = "DEF_ACTIVE"
    elif v_deflect == 0:
        state_preview = "DEF_BYPASS"
    else:
        state_preview = "DEF_RETREAT"

    # Recommendation
    if state_preview == "DEF_ACTIVE":
        recommendation = (
            f"Deflection safe. v_deflect={v_deflect:.4f}, "
            f"{overshoot_margin/v_escape_A*100:.1f}% margin below escape threshold."
        )
    elif state_preview == "DEF_OVERSHOOT_RISK":
        recommendation = (
            f"WARNING: v_deflect={v_deflect:.4f} is within 10% of v_escape_A={v_escape_A:.4f}. "
            f"Increase θ_deflect to create safer margin before calling f_Capture."
        )
    elif state_preview == "DEF_BYPASS":
        recommendation = (
            f"θ=90°: entrant bypasses capture zone. No radial approach component. "
            f"Capture impossible at this angle."
        )
    else:  # DEF_RETREAT
        recommendation = (
            f"θ={theta_deflect_deg}°: entrant retreating. v_deflect={v_deflect:.4f} < 0. "
            f"Deliberate repulsion confirmed."
        )

    return {
        "theta_deg":          theta_deflect_deg,
        "theta_rad":          round(theta_rad, 6),
        "v_approach":         v_approach,
        "v_deflect":          round(v_deflect, 6),
        "transverse_delta_v": round(transverse_dv, 6),
        "deflect_cost":       round(deflect_cost, 6),
        "v_escape_A":         round(v_escape_A, 6),
        "overshoot_margin":   round(overshoot_margin, 6),
        "overshoot_risk":     overshoot_risk,
        "delta_e":            round(delta_e, 6),
        "state_preview":      state_preview,
        "recommendation":     recommendation
    }
```

---

### PRIM:023 — deflect_approach (Impure)

> **Tag:** PRIM:023  
> **Name:** deflect_approach  
> **Type:** IMPURE — modifies node state (v_approach or e) and writes to Φ.registry  
> **Defined in:** f_Deflect.md  
> **Wave:** 3  

#### Full Specification

```python
import math

def deflect_approach(
    A: Node,
    E: Node,
    Phi: Frame,
    theta_deflect_deg: float,
    mode: str = "PRE_CAPTURE",
    k_cost_deflect: float = 1.0
) -> dict:
    """
    PRIM:023 — deflect_approach (IMPURE)
    ======================================
    Engineering primitive: modifies the approach vector of entrant E relative to anchor A.

    In PRE_CAPTURE mode: replaces E.v_approach with v_deflect for a subsequent f_Capture call.
    In POST_CAPTURE_ORBITAL mode: adjusts E.ecc (eccentricity) using deflection geometry.

    Parameters
    ----------
    A : Node
        Anchor node. Required attributes:
          - A.id         : str   — unique node identifier
          - A.M_A        : float — anchor mass (> 0)
          - A.rho_phi    : float — current field density ρ(Φ) ∈ (0, 1]
          - A.r_capture  : float — orbital radius at capture (> 0)
    E : Node
        Entrant node. Required attributes:
          - E.id         : str   — unique node identifier
          - E.M_E        : float — entrant mass (> 0)
          - E.v_approach : float — current approach velocity (> 0)
          - E.ecc        : float — orbital eccentricity (POST_CAPTURE_ORBITAL mode)
    Phi : Frame
        Registry frame. Required attributes:
          - Phi.registry     : dict — maps (A.id, E.id) → capture_record
          - Phi.deflect_log  : list — deflection history records
          - Phi.error_log    : list — diagnostic error records
    theta_deflect_deg : float
        Deflection angle in degrees ∈ [0, 180].
    mode : str, optional
        "PRE_CAPTURE" (default) or "POST_CAPTURE_ORBITAL".
    k_cost_deflect : float, optional
        Deflection cost constant. Default 1.0.

    Returns
    -------
    dict with keys:
        v_approach_old : float — original approach velocity
        v_deflect      : float — effective radial velocity after deflection
        deflect_cost   : float — energy expended
        state_flag     : str   — DEF_ACTIVE | DEF_BYPASS | DEF_RETREAT | DEF_OVERSHOOT_RISK
        mode           : str   — mode used
        delta_e        : float — eccentricity change (POST_CAPTURE_ORBITAL only; else 0.0)
        e_new          : float — updated eccentricity (POST_CAPTURE_ORBITAL only; else E.ecc)
        fm_warning     : str   — "FM-001-RISK" if DEF_OVERSHOOT_RISK; else None
        conditions     : dict  — DEF-C-1 through DEF-C-4 results

    Raises
    ------
    ValueError
        If theta_deflect_deg ∉ [0, 180] (DEF-C-1 violation).
        If v_approach ≤ 0 (DEF-C-2 violation).
        If rho_phi ≤ 0 (DEF-C-3 violation).
        If mode is unrecognized.
    RuntimeError
        If mode is "PRE_CAPTURE" but (A.id, E.id) already in Phi.registry (DEF-C-4 violation).
        If mode is "POST_CAPTURE_ORBITAL" but (A.id, E.id) not in Phi.registry (DEF-C-4 violation).

    Side Effects (IMPURE)
    ---------------------
    PRE_CAPTURE mode (on success):
      - E.v_approach is updated to v_deflect.
      - Phi.deflect_log is appended with this call's record.
    POST_CAPTURE_ORBITAL mode (on success):
      - E.ecc is updated to e_new.
      - Phi.registry[(A.id, E.id)]['ecc'] is updated to e_new.
      - Phi.registry[(A.id, E.id)]['deflect_history'] is appended.
      - Phi.deflect_log is appended with this call's record.
    On DEF_BYPASS or DEF_RETREAT (PRE_CAPTURE):
      - E.v_approach is set to v_deflect (may be 0 or negative).
      - Phi.deflect_log is appended.
      - No capture record is created.
    """

    pair_key     = (A.id, E.id)
    v_approach   = E.v_approach
    rho_phi      = A.rho_phi
    r_capture    = A.r_capture
    M_A          = A.M_A
    M_E          = E.M_E

    # ── Condition Evaluation ─────────────────────────────────────────────────

    conditions = {}

    # DEF-C-1: Angle in range
    def_c1 = 0.0 <= theta_deflect_deg <= 180.0
    conditions["DEF-C-1"] = def_c1
    if not def_c1:
        raise ValueError(
            f"DEF-C-1 FAIL: theta_deflect_deg={theta_deflect_deg} ∉ [0, 180]."
        )

    # DEF-C-2: Approach exists
    def_c2 = v_approach > 0.0
    conditions["DEF-C-2"] = def_c2
    if not def_c2:
        raise ValueError(
            f"DEF-C-2 FAIL: v_approach={v_approach} ≤ 0. No approach to deflect."
        )

    # DEF-C-3: Field alive
    def_c3 = rho_phi > 0.0
    conditions["DEF-C-3"] = def_c3
    if not def_c3:
        raise ValueError(
            f"DEF-C-3 FAIL: rho_phi={rho_phi} = 0. Field null — FM-002 applies."
        )

    # DEF-C-4: Mode consistent with registry
    if mode == "PRE_CAPTURE":
        def_c4 = pair_key not in Phi.registry
        conditions["DEF-C-4"] = def_c4
        if not def_c4:
            raise RuntimeError(
                f"DEF-C-4 FAIL: mode=PRE_CAPTURE but capture record already exists "
                f"for ({A.id}, {E.id}). Use mode='POST_CAPTURE_ORBITAL' or call f_Release first."
            )
    elif mode == "POST_CAPTURE_ORBITAL":
        def_c4 = pair_key in Phi.registry
        conditions["DEF-C-4"] = def_c4
        if not def_c4:
            raise RuntimeError(
                f"DEF-C-4 FAIL: mode=POST_CAPTURE_ORBITAL but no capture record "
                f"for ({A.id}, {E.id}). Use mode='PRE_CAPTURE' instead."
            )
    else:
        raise ValueError(f"Unrecognized mode='{mode}'. Use 'PRE_CAPTURE' or 'POST_CAPTURE_ORBITAL'.")

    # ── Core Computation (delegate to PRIM:024) ──────────────────────────────

    delta = compute_deflect_delta(
        v_approach        = v_approach,
        theta_deflect_deg = theta_deflect_deg,
        M_A               = M_A,
        M_E               = M_E,
        rho_phi           = rho_phi,
        r_capture         = r_capture,
        k_cost_deflect    = k_cost_deflect
    )

    v_deflect    = delta["v_deflect"]
    deflect_cost = delta["deflect_cost"]
    state_flag   = delta["state_preview"]
    delta_e      = delta["delta_e"]
    fm_warning   = "FM-001-RISK" if state_flag == "DEF_OVERSHOOT_RISK" else None

    # ── Impure Side Effects ──────────────────────────────────────────────────

    e_new = E.ecc  # default — unchanged unless POST_CAPTURE_ORBITAL

    if mode == "PRE_CAPTURE":
        # Update entrant approach velocity
        E.v_approach = v_deflect

    elif mode == "POST_CAPTURE_ORBITAL":
        # Reduce eccentricity by delta_e (circularization)
        e_old = E.ecc
        e_new = max(0.0, e_old - delta_e)
        E.ecc = e_new

        # Update frame registry
        record = Phi.registry[pair_key]
        record["ecc"] = e_new
        if "deflect_history" not in record:
            record["deflect_history"] = []
        record["deflect_history"].append({
            "theta_deg":   theta_deflect_deg,
            "v_deflect":   v_deflect,
            "e_old":       e_old,
            "e_new":       e_new,
            "deflect_cost": deflect_cost,
            "state_flag":  state_flag
        })

    # Append to deflect log
    Phi.deflect_log.append({
        "pair":          pair_key,
        "mode":          mode,
        "theta_deg":     theta_deflect_deg,
        "v_approach_old": v_approach,
        "v_deflect":     v_deflect,
        "deflect_cost":  deflect_cost,
        "state_flag":    state_flag,
        "fm_warning":    fm_warning
    })

    return {
        "v_approach_old": v_approach,
        "v_deflect":      v_deflect,
        "deflect_cost":   deflect_cost,
        "state_flag":     state_flag,
        "mode":           mode,
        "delta_e":        delta_e,
        "e_new":          e_new,
        "fm_warning":     fm_warning,
        "conditions":     conditions
    }
```

---

## §8 — Canonical Examples

<!-- [DEFLECT:§8] Canonical examples — 4 examples frozen -->

All four examples use the standard FFF_Gravity interpretive layer. Each includes a parameter table, condition trace, computation trace, and post-state analysis.

---

### Example 1 — Approach Softening (PRE_CAPTURE, FM-001 Prevention)

**Scenario:** A potential mentorship binding (A = established practitioner, E = eager newcomer) is approaching too fast — E is enthusiastic but overwhelming. v_approach exceeds the threshold for stable capture. The operator applies a 45° deflection to soften the approach before calling f_Capture.

#### Parameters

| Parameter | Value | Notes |
|---|---|---|
| A.M_A | 0.80 | Anchor mass |
| A.rho_phi | 0.70 | Field density |
| A.r_capture | 0.50 | Orbital radius |
| E.M_E | 0.35 | Entrant mass |
| E.v_approach | 0.80 | Too fast — near escape threshold |
| θ_deflect | 45° | Moderate softening |
| mode | PRE_CAPTURE | No capture exists yet |

#### Pre-call PRIM:024 Check

```
compute_deflect_delta(v_approach=0.80, theta=45°, M_A=0.80, M_E=0.35,
                      rho_phi=0.70, r_capture=0.50)

v_escape_A = √(2 × 0.80 × 0.70 / 0.50) = √(2.240) = 1.497
→ Original v_approach (0.80) < v_escape_A (1.497) — SC-1 would pass originally.
→ v_deflect = 0.80 × cos(45°) = 0.80 × 0.7071 = 0.566
→ overshoot_margin = 1.497 − 0.566 = 0.931  (62% margin)
→ overshoot_risk = False
→ deflect_cost = 0.35 × (0.80 × sin(45°)) × 1.0 = 0.35 × 0.566 = 0.198
→ state_preview = "DEF_ACTIVE"
→ delta_e = 0.566 / 1.497 = 0.378 (for orbital mode; not used here)
```

#### Condition Trace

| Condition | Check | Result |
|---|---|---|
| DEF-C-1 | 45° ∈ [0°, 180°] | ✅ PASS |
| DEF-C-2 | 0.80 > 0 | ✅ PASS |
| DEF-C-3 | 0.70 > 0 | ✅ PASS |
| DEF-C-4 | No capture record for (A, E) | ✅ PASS |

#### Result

```python
{
  "v_approach_old": 0.80,
  "v_deflect":      0.5657,
  "deflect_cost":   0.1980,
  "state_flag":     "DEF_ACTIVE",
  "mode":           "PRE_CAPTURE",
  "delta_e":        0.3781,
  "fm_warning":     None
}
```

#### Post-State Analysis

- **E.v_approach updated to 0.5657** — softened approach; 62% margin below v_escape_A.
- **SC-1 headroom improved substantially** — next f_Capture call operates well within stable range.
- **deflect_cost = 0.198** — moderate cost; reflects the energy of redirecting the transverse component.
- **Next step:** Call f_Capture with updated E.v_approach = 0.5657. Capture should produce a tighter r_capture and lower e than the original approach would have achieved.

---

### Example 2 — Intentional Bypass (PRE_CAPTURE, θ = 90°)

**Scenario:** A potential business partnership (A = large firm, E = solo consultant) is in the field, but the operator determines that a binding at this time would be premature — the consultant needs more development before committing. The operator applies a 90° deflection to route E past the capture zone without binding.

#### Parameters

| Parameter | Value | Notes |
|---|---|---|
| A.M_A | 1.20 | Large anchor mass |
| A.rho_phi | 0.85 | Strong field |
| E.v_approach | 0.60 | Moderate approach |
| θ_deflect | 90° | Full bypass |
| mode | PRE_CAPTURE | |

#### PRIM:024 Check

```
v_deflect = 0.60 × cos(90°) = 0.60 × 0.0 = 0.000
state_preview = "DEF_BYPASS"
deflect_cost = 0.M_E × (0.60 × sin(90°)) × 1.0 = M_E × 0.60
```

#### Condition Trace

| Condition | Check | Result |
|---|---|---|
| DEF-C-1 | 90° ∈ [0°, 180°] | ✅ PASS |
| DEF-C-2 | 0.60 > 0 | ✅ PASS |
| DEF-C-3 | 0.85 > 0 | ✅ PASS |
| DEF-C-4 | No prior capture | ✅ PASS |

#### Result

```python
{
  "v_approach_old": 0.60,
  "v_deflect":      0.0,
  "state_flag":     "DEF_BYPASS",
  "mode":           "PRE_CAPTURE",
  "fm_warning":     None
}
```

#### Post-State Analysis

- **E.v_approach = 0.0** — the entrant has zero radial approach. SC-1 would still pass (0 < v_escape_A), but a subsequent f_Capture call would produce d_bind = 0 (since v_approach = 0 → no binding depth). The bypass is effective.
- **DEF_BYPASS is not a failure** — it is a deliberate strategic outcome. The entrant remains in the field's proximity but is not bound. Future interactions can re-initiate approach when conditions improve.
- **No capture record created** — Φ.registry is untouched.

---

### Example 3 — Orbital Circularization (POST_CAPTURE_ORBITAL)

**Scenario:** An existing binding (A = senior researcher, E = PhD student) has an eccentric orbit (e = 0.55) — the relationship is productive but irregular, with large fluctuations in engagement. The operator applies a 40° deflection post-capture to circularize the orbit and stabilize d_bind.

#### Parameters

| Parameter | Value | Notes |
|---|---|---|
| A.M_A | 0.90 | |
| A.rho_phi | 0.75 | |
| A.r_capture | 0.45 | |
| E.M_E | 0.40 | |
| E.v_approach | 0.55 | Current orbital velocity component |
| E.ecc | 0.55 | Highly eccentric — target: reduce toward 0.30 |
| θ_deflect | 40° | Partial circularization |
| mode | POST_CAPTURE_ORBITAL | Capture already registered |

#### PRIM:024 Check

```
v_escape_A = √(2 × 0.90 × 0.75 / 0.45) = √(3.000) = 1.732
v_deflect  = 0.55 × cos(40°) = 0.55 × 0.766 = 0.421
transverse_dv = 0.55 × sin(40°) = 0.55 × 0.643 = 0.354
deflect_cost  = 0.40 × 0.354 × 1.0 = 0.141
delta_e       = 0.354 / 1.732 = 0.204
e_new         = max(0.0, 0.55 − 0.204) = 0.346
```

#### Condition Trace

| Condition | Check | Result |
|---|---|---|
| DEF-C-1 | 40° ∈ [0°, 180°] | ✅ PASS |
| DEF-C-2 | 0.55 > 0 | ✅ PASS |
| DEF-C-3 | 0.75 > 0 | ✅ PASS |
| DEF-C-4 | Capture record exists | ✅ PASS |

#### Result

```python
{
  "v_approach_old": 0.55,
  "v_deflect":      0.4212,
  "deflect_cost":   0.1412,
  "state_flag":     "DEF_ACTIVE",
  "mode":           "POST_CAPTURE_ORBITAL",
  "delta_e":        0.2044,
  "e_new":          0.3456,
  "fm_warning":     None
}
```

#### Post-State Analysis

- **Eccentricity reduced from 0.55 → 0.346** — significantly more circular orbit. Engagement irregularity decreases substantially.
- **d_bind_new recalculates:** `d_bind = β × ρ(Φ) × (1 − e_new) = β × 0.75 × (1 − 0.346)` — binding depth improves due to lower e.
- **Registry updated:** Φ.registry now carries e = 0.346 — f_Orbit can re-classify the orbit as ELLIPTICAL or approaching CIRCULAR.
- **Further circularization:** If e = 0.346 is still too high, the operator can apply additional deflection in subsequent cycles.

---

### Example 4 — FM-001 Risk Detection and Correction Sequence

**Scenario:** A high-velocity approach (A = company, E = high-profile hire) is flagged by PRIM:024 as DEF_OVERSHOOT_RISK after a 20° softening deflection. The operator checks the warning, increases θ, and achieves a safe approach.

#### Phase 1 — Initial Attempt (θ = 20°, Insufficient)

```
v_approach = 0.92, v_escape_A = 1.00

compute_deflect_delta(v_approach=0.92, theta=20°, ...)
→ v_deflect = 0.92 × cos(20°) = 0.92 × 0.940 = 0.864
→ overshoot_margin = 1.00 − 0.864 = 0.136
→ overshoot_threshold = 0.10 × 1.00 = 0.10
→ overshoot_risk = True  (0.136 > 0.10, BUT margin < 0.136... wait)
```

Actually let me recalculate:
```
overshoot_threshold = 0.10 × v_escape_A = 0.10 × 1.00 = 0.10
overshoot_margin = 1.00 − 0.864 = 0.136
overshoot_risk: 0.136 > 0.10 → False (margin is ABOVE threshold)
```

Let me use v_approach = 0.95 instead, which gives v_deflect closer to escape:

```
v_approach = 0.95
v_escape_A = 1.00

Phase 1 — θ = 10° (too small):
  v_deflect = 0.95 × cos(10°) = 0.95 × 0.985 = 0.935
  overshoot_margin = 1.00 − 0.935 = 0.065
  overshoot_threshold = 0.10
  overshoot_risk = True  (margin 0.065 < threshold 0.10)
  → state_flag = DEF_OVERSHOOT_RISK
  → fm_warning = "FM-001-RISK"

Phase 2 — θ = 25° (adequate):
  v_deflect = 0.95 × cos(25°) = 0.95 × 0.906 = 0.861
  overshoot_margin = 1.00 − 0.861 = 0.139
  overshoot_risk = False  (margin 0.139 > threshold 0
```
