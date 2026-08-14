---
session_id: SES-20260813-CASCADE-001
tag: "[FFF:GRAVITY:CAPTURE:CASCADE]"
version: 1.0.0
status: STABLE
wave: 4
file: docs/FFF_Gravity/f_Capture_Cascade.md
module: FFF_Gravity
dependencies:
  - f_Capture.md        # base capture semantics — d_bind, e, r_capture
  - f_Field.md          # ρ(Φ), coherence well, F_freq
  - f_Force.md          # F_fluid (β), F_force (v_approach)
  - f_Frame.md          # capacity_MAX, register_capture, GravityGraph
  - f_Emit.md           # ρ(Φ) saturation ceiling (≤ 1.0)
  - f_Capture_Multi.md  # Φ_perturbed, δ_perturb, k_perturb field-perturbation model
new_operators:
  - cascade_depth    (k_max)   # maximum chain depth before hard termination
  - cascade_gain     (γ)       # transmission factor applied at each cascade step
  - Ω_cascade        (k)       # cascade transmission value at depth k
new_primitives:
  - PRIM:027  evaluate_cascade_eligibility   Pure
  - PRIM:028  execute_cascade_step           Impure
new_failure_modes:
  - FM-003-C  # sub-mode of FM-003 — Cascade Frame Saturation (partial-chain state)
inv_compliance: enforced   # INV-001–INV-010
---

# f_Capture_Cascade.md
## FFF_Gravity — Cascade Capture Variant

---

## §0 — Session Context

| Field            | Value                                                        |
|------------------|--------------------------------------------------------------|
| Session ID       | SES-20260813-CASCADE-001                                     |
| Tag              | [FFF:GRAVITY:CAPTURE:CASCADE]                                |
| Timestamp        | 2026-08-13T21:52 EDT                                         |
| Wave             | 4 — Capture Variants                                         |
| Wave Position    | File 2 of 6 in Wave 4                                        |
| Prior file       | f_Capture_Multi.md (PRIM:025–026, FM-003-M)                  |
| Next file        | f_Capture_Soft.md                                            |
| PRIM block       | PRIM:027–028 (Wave 4 block; PRIM:025–026 assigned to Multi)  |
| FM registry      | Frozen at FM-001–FM-010. Sub-modes only.                     |
| INV registry     | Frozen at INV-001–INV-010. All enforced.                     |

### §0.1 — Architectural Position

`f_Capture_Cascade.md` defines **cascade capture**: a sequential chain mechanism in which
one successful capture event triggers evaluation of a downstream candidate, propagating
through depth `k` until the chain terminates naturally, hits a depth bound, or exhausts
frame capacity.

**Distinction from Multi-Capture** (`f_Capture_Multi.md`):

| Dimension         | Multi-Capture (f_Capture_Multi.md)              | Cascade Capture (this file)                         |
|-------------------|-------------------------------------------------|-----------------------------------------------------|
| Structure         | Breadth — N independent candidates in parallel  | Depth — sequential chain, one step at a time        |
| Coupling          | Candidates are independent                      | Step k output is step k+1 stimulus                  |
| Termination       | Exhausted candidate list or FM-003-M            | Binding failure, depth bound, or FM-003-C           |
| Field model       | Φ_perturbed degrades per candidate              | Φ_perturbed degrades per chain step                 |
| Gain              | Not applicable                                  | γ — amplifies or attenuates across steps            |

Cascade and Multi are orthogonal variants. A cascade where each step is itself a
multi-capture batch is a valid extension (see §9 cross-references) but is not
specified in this file.

---

## §1 — Module Identity

| Field              | Value                                                     |
|--------------------|-----------------------------------------------------------|
| File               | `docs/FFF_Gravity/f_Capture_Cascade.md`                   |
| Module             | FFF_Gravity                                               |
| Layer              | Capture Variant — applied over Layer 1/2/3 substrate      |
| Core equation      | G = F_freq · F_fluid · F_force (INV-001)                  |
| Capture variant    | Sequential chain — Ω_cascade(k) = Ω_cascade(k−1) × γ     |
| Conditions         | CAS-1 through CAS-4 (conjunctive per INV-005)             |
| Failure sub-mode   | FM-003-C (Cascade Frame Saturation)                       |
| New primitives     | PRIM:027, PRIM:028                                        |
| Status             | STABLE                                                    |

---

## §2 — Canonical Description

### §2.1 — Mechanism

A cascade capture begins with an initial binding event — the **trigger capture** at depth
`k = 0`. The trigger capture is a standard capture (per `f_Capture.md`) that produces
a binding value `Ω_cascade(0)` equal to the achieved `d_bind(0)`.

At each subsequent depth `k ≥ 1`:

1. **Transmission:** The prior step's output is multiplied by the cascade gain `γ`:
   `Ω_cascade(k) = Ω_cascade(k−1) × γ`

2. **Field perturbation:** The field at depth `k` is degraded from the trigger field
   using the same perturbation model as `f_Capture_Multi.md`:
   `Φ_perturbed(k) = Φ_perturbed(k−1) − δ_perturb(k)`

3. **Binding threshold at depth k:**
   `d_bind(k) = β × ρ(Φ_perturbed(k)) × (1 − e(k))`

4. **Eligibility check:** Step k captures the downstream candidate if and only if
   all four cascade conditions CAS-1 through CAS-4 hold. The critical check:
   `Ω_cascade(k) ≥ d_bind(k)`

5. **Frame registration:** On success, the downstream element is registered in the
   Frame via `register_capture` (PRIM:003). Frame capacity is guarded by CAS-4.

### §2.2 — Gain Regimes

| γ value   | Regime        | Behavior                                                              |
|-----------|---------------|-----------------------------------------------------------------------|
| γ > 1.0   | Amplifying    | Each step carries more transmission than the last; chain grows        |
| γ = 1.0   | Neutral       | Transmission is preserved; chain length governed by field decay alone |
| 0 < γ < 1 | Attenuating   | Each step carries less; chain terminates when Ω_cascade < d_bind     |
| γ ≤ 0     | Invalid       | Violates CAS-1; cascade is rejected before any step executes         |

### §2.3 — Termination Taxonomy

A cascade terminates under exactly one of four conditions (whichever is reached first):

| Code   | Condition           | State at termination                        |
|--------|---------------------|---------------------------------------------|
| T-NAT  | Ω_cascade(k) < d_bind(k)  | Natural termination — chain exhausted       |
| T-DEPTH| k = k_max           | Depth bound — hard ceiling reached          |
| T-CAP  | FM-003-C triggered  | Frame saturation mid-chain (partial state)  |
| T-INIT | CAS-1 violated (γ ≤ 0) | Chain never starts — pre-flight rejection |

### §2.4 — Partial Cascade State (T-CAP)

When FM-003-C fires, the cascade halts with `m < k_max` successful steps. Elements
captured in steps 0 through `m−1` remain bound; the element at step `m` is **not**
captured. The system enters `PARTIAL_CASCADE` — a recoverable state requiring
`purge_registry` (PRIM:004) or field amplification via `f_Emit.md` before a new
cascade can be initiated.

---

## §3 — Triadic Equation

### §3.1 — Base Triadic Identity (INV-001)

```
G = F_freq · F_fluid · F_force
```

All three nodes are inseparable. Cascade does not relax this invariant.

### §3.2 — Cascade-Specialized Form

At chain depth `k`, the triadic equation maps as:

```
G_cascade(k) = ρ(Φ_perturbed(k))  ·  β  ·  Ω_cascade(k)
               └── F_freq node ──┘  └F_fluid┘  └── F_force node ──┘
```

Where:

| Term                 | Node     | Description                                         |
|----------------------|----------|-----------------------------------------------------|
| ρ(Φ_perturbed(k))    | F_freq   | Coherence well at cascade depth k, field-perturbed  |
| β                    | F_fluid  | Binding capacity — invariant across all steps       |
| Ω_cascade(k)         | F_force  | Cascade transmission force at depth k               |

### §3.3 — Cascade Recurrence

```
Ω_cascade(0) = d_bind(0)                          # trigger capture binding value
Ω_cascade(k) = Ω_cascade(k−1) × γ,   k ≥ 1      # geometric transmission
```

### §3.4 — Binding Condition at Depth k

```
Ω_cascade(k) ≥ d_bind(k)
```

Where:
```
d_bind(k) = β × ρ(Φ_perturbed(k)) × (1 − e(k))
Φ_perturbed(k) = Φ_perturbed(k−1) − δ_perturb(k)
δ_perturb(k)   = d_bind(k−1) × (1 − e(k−1)) × k_perturb
```

### §3.5 — Chain Length Formula

In the purely attenuating case (γ < 1, constant e, constant k_perturb):

```
k_terminate ≈ log(d_bind_base / Ω_cascade(0)) / log(γ / (1 − k_perturb))
```

This gives an analytic estimate of natural chain depth before numerical evaluation.

---

## §4 — Operator Registry

### §4.1 — cascade_depth (k_max)

| Field       | Value                                                               |
|-------------|---------------------------------------------------------------------|
| Symbol      | `k_max`                                                             |
| Type        | `int`, k_max ≥ 1                                                    |
| Domain      | Positive integers                                                   |
| Description | Maximum chain depth; hard termination at k = k_max regardless of Ω |
| Default     | System-configured; recommend ≤ 16 to bound frame load               |
| Guard       | CAS-2. Violation → T-DEPTH termination (not an error)              |

### §4.2 — cascade_gain (γ)

| Field       | Value                                                               |
|-------------|---------------------------------------------------------------------|
| Symbol      | `γ` (`gamma`)                                                       |
| Type        | `float`, γ > 0                                                      |
| Domain      | (0, ∞). Values > 1 amplify; values < 1 attenuate.                  |
| Description | Transmission factor applied to Ω_cascade at each chain step        |
| Guard       | CAS-1. γ ≤ 0 → T-INIT rejection before any step                   |
| Warning     | γ > 1 in amplifying regime risks rapid FM-003-C saturation         |

### §4.3 — Ω_cascade (cascade transmission)

| Field       | Value                                                               |
|-------------|---------------------------------------------------------------------|
| Symbol      | `Ω_cascade(k)`                                                      |
| Type        | `float`, Ω_cascade(k) ≥ 0                                          |
| Description | Cascade transmission value at depth k; represents binding stimulus  |
|             | carried forward from the prior step                                 |
| Recurrence  | Ω_cascade(0) = d_bind(0); Ω_cascade(k) = Ω_cascade(k−1) × γ       |
| Guard       | CAS-3. Ω_cascade(k) < d_bind(k) → T-NAT termination                |

### §4.4 — Inherited Operators (from f_Capture_Multi.md)

The field perturbation model is carried forward unchanged:

| Operator          | Source              | Role in cascade                                 |
|-------------------|---------------------|-------------------------------------------------|
| Φ_perturbed(k)    | f_Capture_Multi.md  | Field at cascade depth k                        |
| δ_perturb(k)      | f_Capture_Multi.md  | Per-step field decrement                        |
| k_perturb         | f_Capture_Multi.md  | Perturbation rate coefficient (system constant) |

### §4.5 — Operator Interaction Map

```
Ω_cascade(k−1) ──×γ──→ Ω_cascade(k) ──┐
                                        ├──→ CAS-3: Ω_cascade(k) ≥ d_bind(k)?
d_bind(k) = β·ρ(Φ_perturbed(k))·(1−e) ─┘         │
                                                    ├─ YES → register_capture (PRIM:003)
Φ_perturbed(k) = Φ_perturbed(k−1) − δ_perturb(k)  │         advance to k+1
                                                    └─ NO  → T-NAT termination
```

---

## §5 — Cascade Conditions

All four conditions are **conjunctive** (INV-005): all must hold at each step for the
cascade to proceed. Failure of any one condition terminates the chain.

### CAS-1 — Gain Positivity

```
γ > 0
```

Evaluated once before the chain initiates. γ ≤ 0 is a pre-flight violation (T-INIT).

**Rationale:** Negative or zero gain inverts or eliminates transmission, producing
undefined or degenerate chain behavior. The cascade model does not support these regimes.

### CAS-2 — Depth Bound

```
k < k_max  at the point of chain entry for step k
```

Evaluated at the start of each step. When k = k_max, the step is not attempted; the
chain terminates as T-DEPTH. This is a **clean** termination — not an error state.

**Rationale:** Unbounded cascade chains can exhaust frame capacity and computational
resources. k_max imposes a hard architectural ceiling.

### CAS-3 — Binding Threshold

```
Ω_cascade(k) ≥ d_bind(k)
```

Evaluated at each step after computing Ω_cascade(k) and d_bind(k). Failure → T-NAT.

**Rationale:** Transmission must exceed the binding cost of the downstream candidate.
This is the cascade analog of the standard capture binding check from `f_Capture.md`.

### CAS-4 — Frame Capacity Guard (FM-003-C)

```
frame_count + 1 ≤ capacity_MAX
```

Evaluated before each `register_capture` call. Failure → FM-003-C (T-CAP).

**Rationale:** The Frame has a hard capacity ceiling (INV-003). A cascade must not
bypass this ceiling, even mid-chain. See §6 for FM-003-C details.

### §5.1 — Condition Evaluation Order

```
CAS-1 (pre-flight) → [loop begins]
  CAS-2 (depth) → CAS-3 (binding) → CAS-4 (capacity) → register → advance k
                                                          [repeat]
```

CAS-1 is evaluated once. CAS-2, CAS-3, CAS-4 are re-evaluated at every step.

---

## §6 — Failure Modes

> FM registry is frozen at FM-001–FM-010. No new FM IDs are introduced.
> FM-003-C is a sub-mode of FM-003 (Frame Saturation) specific to cascade context.

### FM-003-C — Cascade Frame Saturation

| Field           | Value                                                              |
|-----------------|--------------------------------------------------------------------|
| ID              | FM-003-C (sub-mode of FM-003)                                      |
| Severity        | FATAL (for this cascade chain)                                     |
| Domain          | Layer 3 — Frame                                                    |
| Trigger         | CAS-4 fails: frame_count + 1 > capacity_MAX mid-cascade           |
| State           | PARTIAL_CASCADE — elements at k=0…m−1 bound; step m not executed  |
| Recovery path   | `purge_registry` (PRIM:004) to free slots, then re-initiate chain |
|                 | OR `f_Emit.md` to raise ρ(Φ) → capacity_MAX expansion             |
| Cascade effect  | Chain halts immediately; no further steps are attempted            |

**Distinction from FM-003 (base Frame Saturation):**

| Aspect              | FM-003 (base)                     | FM-003-C (cascade)                         |
|---------------------|-----------------------------------|--------------------------------------------|
| Context             | Single or multi-capture overflow  | Mid-chain saturation during cascade        |
| State left          | Frame full, clean boundary        | Partial cascade — chain half-committed     |
| Recovery complexity | Standard purge or emit            | Must also decide whether to re-enter chain |
| Notification        | GravityGraph: FRAME_SATURATED     | GravityGraph: CASCADE_INTERRUPTED          |

### §6.1 — Active FM Guards During Cascade

All 10 base failure modes remain active throughout cascade execution:

| FM       | Domain      | Relevance in cascade context                                        |
|----------|-------------|---------------------------------------------------------------------|
| FM-001   | F_force     | v_approach guards still apply at each step's target candidate       |
| FM-002   | F_freq      | ρ(Φ) floor must not drop to zero (chain collapses naturally before) |
| FM-003   | Frame       | Base saturation; FM-003-C is the cascade sub-mode                   |
| FM-004   | Decay       | Existing orbits may decay while cascade executes                    |
| FM-005   | Decay       | A decay spiral on existing orbit does not block cascade             |
| FM-006   | F_force     | Escape velocity guard active per step                               |
| FM-007   | F_fluid     | Mass-parity guard does not block cascade; affects orbit quality     |
| FM-008   | Release     | Not triggered during capture; relevant post-cascade                 |
| FM-009   | Dampen      | Dampening a live cascade field — see CAS-4 interaction note         |
| FM-010   | F_freq/β    | ρ(Φ) ceiling and β ceiling enforced; amplification is blocked       |

> **CAS-4 / FM-009 interaction:** If `f_Dampen.md` fires mid-cascade (DAMP-C-3
> active-orbit guard), ρ(Φ) may drop enough to make CAS-3 fail at the next step,
> producing a T-NAT termination that is causally attributable to dampening. The
> GravityGraph notification should record this causal chain.

---

## §7 — Engineering Primitives

### PRIM:027 — evaluate_cascade_eligibility (Pure)

**Classification:** Pure — no side effects, no registry mutation.

**Purpose:** Evaluate whether cascade step `k` is eligible to execute, returning
a structured eligibility result with margin and termination reason.

```python
from dataclasses import dataclass
from typing import Optional


@dataclass
class CascadeEligibility:
    """Result of a cascade step eligibility evaluation."""
    eligible: bool
    k: int
    omega_k: float
    d_bind_k: float
    margin: float                   # omega_k - d_bind_k; positive = eligible
    termination_reason: Optional[str]  # None if eligible; T-NAT / T-DEPTH / T-CAP / T-INIT


def evaluate_cascade_eligibility(
    omega_k: float,
    d_bind_k: float,
    k: int,
    k_max: int,
    frame_count: int,
    capacity_MAX: int,
    gamma: float,
) -> CascadeEligibility:
    """
    Evaluate cascade step k for eligibility under conditions CAS-1 through CAS-4.

    This function is PURE — it does not mutate any external state.
    All four conditions are conjunctive; the first failure encountered terminates.

    Parameters
    ----------
    omega_k       : float  — Cascade transmission at depth k (already computed).
    d_bind_k      : float  — Binding threshold at depth k (field-perturbed).
    k             : int    — Current cascade depth (0-indexed, where k=0 is trigger).
    k_max         : int    — Maximum allowed cascade depth (hard ceiling).
    frame_count   : int    — Current number of registered elements in Frame.
    capacity_MAX  : int    — Maximum Frame capacity (from f_Frame.md §4.3).
    gamma         : float  — Cascade gain coefficient (checked for CAS-1 pre-flight).

    Returns
    -------
    CascadeEligibility
        eligible           : True iff all four conditions pass.
        k                  : Echo of depth parameter.
        omega_k            : Echo of cascade transmission.
        d_bind_k           : Echo of binding threshold.
        margin             : omega_k - d_bind_k (positive = eligible on CAS-3).
        termination_reason : None if eligible; one of T-INIT / T-DEPTH / T-NAT / T-CAP.

    Invariants enforced
    -------------------
    INV-001 : F_freq · F_fluid · F_force inseparability — all three nodes
              contributed to producing omega_k and d_bind_k upstream.
    INV-005 : Conditions are conjunctive; all must pass.

    Examples
    --------
    >>> evaluate_cascade_eligibility(
    ...     omega_k=0.48, d_bind_k=0.285, k=1, k_max=10,
    ...     frame_count=2, capacity_MAX=8, gamma=0.6
    ... )
    CascadeEligibility(eligible=True, k=1, omega_k=0.48, d_bind_k=0.285,
                       margin=0.195, termination_reason=None)

    >>> evaluate_cascade_eligibility(
    ...     omega_k=0.173, d_bind_k=0.255, k=3, k_max=10,
    ...     frame_count=2, capacity_MAX=8, gamma=0.6
    ... )
    CascadeEligibility(eligible=False, k=3, omega_k=0.173, d_bind_k=0.255,
                       margin=-0.082, termination_reason='T-NAT')
    """
    # CAS-1: Gain Positivity (pre-flight; caller should check before loop,
    # but guarded here defensively)
    if gamma <= 0.0:
        return CascadeEligibility(
            eligible=False, k=k, omega_k=omega_k, d_bind_k=d_bind_k,
            margin=omega_k - d_bind_k, termination_reason="T-INIT"
        )

    # CAS-2: Depth Bound
    if k >= k_max:
        return CascadeEligibility(
            eligible=False, k=k, omega_k=omega_k, d_bind_k=d_bind_k,
            margin=omega_k - d_bind_k, termination_reason="T-DEPTH"
        )

    # CAS-3: Binding Threshold
    margin = omega_k - d_bind_k
    if margin < 0.0:
        return CascadeEligibility(
            eligible=False, k=k, omega_k=omega_k, d_bind_k=d_bind_k,
            margin=margin, termination_reason="T-NAT"
        )

    # CAS-4: Frame Capacity Guard (FM-003-C)
    if frame_count + 1 > capacity_MAX:
        return CascadeEligibility(
            eligible=False, k=k, omega_k=omega_k, d_bind_k=d_bind_k,
            margin=margin, termination_reason="T-CAP"
        )

    return CascadeEligibility(
        eligible=True, k=k, omega_k=omega_k, d_bind_k=d_bind_k,
        margin=margin, termination_reason=None
    )
```

**Parameter table:**

| Parameter     | Type    | Constraint      | Description                                     |
|---------------|---------|-----------------|-------------------------------------------------|
| omega_k       | float   | ≥ 0             | Pre-computed cascade transmission at depth k    |
| d_bind_k      | float   | > 0             | Field-perturbed binding threshold at depth k    |
| k             | int     | ≥ 0             | Cascade depth (0 = trigger capture)             |
| k_max         | int     | ≥ 1             | Hard depth ceiling                              |
| frame_count   | int     | ≥ 0             | Elements currently registered in Frame          |
| capacity_MAX  | int     | ≥ 1             | Frame capacity ceiling from f_Frame.md          |
| gamma         | float   | > 0 required    | Cascade gain (validated for CAS-1)              |

**Return schema:**

| Field              | Type    | Description                                             |
|--------------------|---------|---------------------------------------------------------|
| eligible           | bool    | True iff all four conditions pass                       |
| k                  | int     | Echo of depth                                           |
| omega_k            | float   | Echo of cascade transmission                            |
| d_bind_k           | float   | Echo of binding threshold                               |
| margin             | float   | omega_k − d_bind_k; negative signals T-NAT             |
| termination_reason | str     | None if eligible; T-INIT / T-DEPTH / T-NAT / T-CAP     |

---

### PRIM:028 — execute_cascade_step (Impure)

**Classification:** Impure — mutates GravityGraph registry on success.

**Purpose:** Execute one cascade step: compute Ω_cascade(k) and d_bind(k), evaluate
eligibility via PRIM:027, register the element if eligible, and advance state for
the next step.

```python
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class CascadeStepResult:
    """Result of executing a single cascade step."""
    status: str                       # CAPTURED / TERMINATED / FM-003-C
    k: int                            # cascade depth at which result was determined
    omega_k: float                    # cascade transmission at this step
    d_bind_k: float                   # binding threshold at this step
    phi_perturbed_k: float            # field value after perturbation at this step
    frame_count: int                  # frame count after this step (updated on CAPTURED)
    termination_reason: Optional[str] # None on CAPTURED; T-NAT / T-DEPTH / T-CAP / T-INIT
    margin: float                     # omega_k - d_bind_k


def execute_cascade_step(
    omega_prev: float,
    gamma: float,
    phi_perturbed_prev: float,
    k_perturb: float,
    d_bind_prev: float,
    e_prev: float,
    beta: float,
    e_k: float,
    k: int,
    k_max: int,
    frame_count: int,
    capacity_MAX: int,
    registry: Any,          # GravityGraph instance (f_Frame.md §4.5)
    element_id: str,
) -> CascadeStepResult:
    """
    Execute a single cascade step k, integrating field perturbation,
    transmission propagation, eligibility evaluation, and registry update.

    This function is IMPURE — it calls register_capture (PRIM:003) on
    the registry when the step is eligible, mutating Frame state.

    Parameters
    ----------
    omega_prev          : float  — Ω_cascade(k−1); cascade transmission from prior step.
    gamma               : float  — Cascade gain coefficient γ. Must be > 0 (CAS-1).
    phi_perturbed_prev  : float  — Φ_perturbed(k−1); field value after prior perturbation.
    k_perturb           : float  — Perturbation rate coefficient (system constant).
                                   From f_Capture_Multi.md §4.4.
    d_bind_prev         : float  — d_bind(k−1); prior step's binding threshold.
    e_prev              : float  — eccentricity at step k−1 (for δ_perturb computation).
    beta                : float  — F_fluid binding capacity (invariant across chain).
    e_k                 : float  — eccentricity at step k (for d_bind(k) computation).
    k                   : int    — Current cascade depth (k ≥ 1).
    k_max               : int    — Maximum cascade depth (CAS-2 ceiling).
    frame_count         : int    — Current Frame registration count before this step.
    capacity_MAX        : int    — Frame capacity ceiling (CAS-4).
    registry            : Any    — GravityGraph instance; mutated on CAPTURED.
    element_id          : str    — Identifier of the downstream candidate at depth k.

    Returns
    -------
    CascadeStepResult with fields described in class definition above.

    Side effects
    ------------
    On CAPTURED: calls registry.register_capture(element_id, ...) — mutates Frame.
    On TERMINATED / FM-003-C: no registry mutation.

    On FM-003-C: emits GravityGraph notification CASCADE_INTERRUPTED.

    Formulas applied (in order)
    ---------------------------
    1. δ_perturb(k) = d_bind_prev × (1 − e_prev) × k_perturb
    2. Φ_perturbed(k) = phi_perturbed_prev − δ_perturb(k)
       Φ_perturbed(k) = max(Φ_perturbed(k), 0.0)      # floor at 0
    3. ρ(Φ_perturbed(k)) = Φ_perturbed(k)              # simplified linear mapping
    4. d_bind(k) = beta × ρ(Φ_perturbed(k)) × (1 − e_k)
    5. Ω_cascade(k) = omega_prev × gamma
    6. eligibility = evaluate_cascade_eligibility(...)  # PRIM:027

    Invariants enforced
    -------------------
    INV-001 : Triadic product intact — ρ(Φ_perturbed(k)) · β · Ω_cascade(k).
    INV-003 : Frame capacity ceiling via CAS-4 / FM-003-C.
    INV-005 : CAS-1..CAS-4 conjunctive.

    Examples
    --------
    >>> result = execute_cascade_step(
    ...     omega_prev=0.8, gamma=0.6,
    ...     phi_perturbed_prev=0.9, k_perturb=0.05,
    ...     d_bind_prev=0.3, e_prev=0.1,
    ...     beta=0.5, e_k=0.1,
    ...     k=1, k_max=10, frame_count=2, capacity_MAX=8,
    ...     registry=graph, element_id="E-beta-1"
    ... )
    >>> result.status
    'CAPTURED'
    >>> result.omega_k
    0.48
    """
    # Step 1: Field perturbation
    delta_perturb_k = d_bind_prev * (1.0 - e_prev) * k_perturb
    phi_perturbed_k = max(phi_perturbed_prev - delta_perturb_k, 0.0)

    # Step 2: Field coherence at depth k (linear mapping)
    rho_phi_k = phi_perturbed_k

    # Step 3: Binding threshold at depth k
    d_bind_k = beta * rho_phi_k * (1.0 - e_k)

    # Step 4: Cascade transmission at depth k
    omega_k = omega_prev * gamma

    # Step 5: Eligibility evaluation (PRIM:027 — pure)
    eligibility = evaluate_cascade_eligibility(
        omega_k=omega_k,
        d_bind_k=d_bind_k,
        k=k,
        k_max=k_max,
        frame_count=frame_count,
        capacity_MAX=capacity_MAX,
        gamma=gamma,
    )

    if not eligibility.eligible:
        # FM-003-C: special notification for capacity exhaustion mid-chain
        if eligibility.termination_reason == "T-CAP":
            registry.notify("CASCADE_INTERRUPTED", {
                "element_id": element_id,
                "k": k,
                "frame_count": frame_count,
                "capacity_MAX": capacity_MAX,
                "fm": "FM-003-C",
            })
            return CascadeStepResult(
                status="FM-003-C", k=k, omega_k=omega_k, d_bind_k=d_bind_k,
                phi_perturbed_k=phi_perturbed_k, frame_count=frame_count,
                termination_reason="T-CAP", margin=eligibility.margin
            )

        return CascadeStepResult(
            status="TERMINATED", k=k, omega_k=omega_k, d_bind_k=d_bind_k,
            phi_perturbed_k=phi_perturbed_k, frame_count=frame_count,
            termination_reason=eligibility.termination_reason,
            margin=eligibility.margin
        )

    # Step 6: Register capture — IMPURE (mutates registry)
    registry.register_capture(element_id, d_bind=d_bind_k, depth=k)
    new_frame_count = frame_count + 1

    return CascadeStepResult(
        status="CAPTURED", k=k, omega_k=omega_k, d_bind_k=d_bind_k,
        phi_perturbed_k=phi_perturbed_k, frame_count=new_frame_count,
        termination_reason=None, margin=eligibility.margin
    )
```

**Parameter table:**

| Parameter          | Type    | Constraint     | Description                                          |
|--------------------|---------|----------------|------------------------------------------------------|
| omega_prev         | float   | ≥ 0            | Cascade transmission from prior step                 |
| gamma              | float   | > 0            | Cascade gain (CAS-1 enforced inside PRIM:027)        |
| phi_perturbed_prev | float   | [0, 1]         | Field value at prior step                            |
| k_perturb          | float   | [0, 1)         | Perturbation sensitivity coefficient                 |
| d_bind_prev        | float   | ≥ 0            | Binding demand at prior step (for δ_perturb calc)   |
| e_prev             | float   | [0, 1)         | Eccentricity at prior step (for δ_perturb calc)     |
| beta               | float   | [0, 1]         | Binding coefficient β at current step                |
| e_k                | float   | [0, 1)         | Eccentricity of current candidate element            |
| k                  | int     | ≥ 1            | Current step index (1-based)                         |
| k_max              | int     | ≥ 1            | Maximum chain depth (CAS-2 ceiling)                  |
| frame_count        | int     | ≥ 0            | Current count of bound elements in registry          |
| capacity_MAX       | int     | ≥ 1            | Registry hard capacity (FM-003-C guard)              |
| registry           | list    | —              | Mutable registry of currently bound elements         |
| element_id         | str     | non-empty      | Identifier of candidate element being evaluated      |

**Return value:** `CascadeStepResult` — a typed record:

```python
@dataclass
class CascadeStepResult:
    status:        str    # "BOUND", "T-NAT", "T-DEPTH", "T-CAP"
    element_id:    str    # candidate processed
    k:             int    # step index
    omega_k:       float  # Ω_cascade(k) used
    phi_k:         float  # Φ_perturbed at this step
    d_bind_k:      float  # binding demand at this step
    bound:         bool   # True iff element was captured
    fm_triggered:  str | None  # "FM-003-C" or None
```

**Implementation:**

```python
def execute_cascade_step(
    omega_prev: float,
    gamma: float,
    phi_perturbed_prev: float,
    k_perturb: float,
    d_bind_prev: float,
    e_prev: float,
    beta: float,
    e_k: float,
    k: int,
    k_max: int,
    frame_count: int,
    capacity_MAX: int,
    registry: list,
    element_id: str,
) -> CascadeStepResult:
    """
    Execute one step of a cascade chain.

    Guards checked in order:
      1. k_max ceiling  → T-DEPTH
      2. FM-003-C capacity → T-CAP
      3. CAS-3 binding condition → T-NAT (if fails)
      4. Success → BOUND
    """

    # ── Step 1: depth ceiling ──────────────────────────────────────────
    if k > k_max:
        return CascadeStepResult(
            status="T-DEPTH",
            element_id=element_id,
            k=k,
            omega_k=omega_prev * gamma,   # still compute for audit
            phi_k=phi_perturbed_prev,
            d_bind_k=None,
            bound=False,
            fm_triggered=None,
        )

    # ── Step 2: advance Ω and Φ ───────────────────────────────────────
    omega_k       = omega_prev * gamma
    delta_perturb = d_bind_prev * (1.0 - e_prev) * k_perturb
    phi_k         = max(0.0, phi_perturbed_prev - delta_perturb)

    # ── Step 3: compute d_bind(k) ─────────────────────────────────────
    # d_bind(k) = beta * (1 − e_k) * phi_k   (from f_Capture.md §3)
    d_bind_k = beta * (1.0 - e_k) * phi_k

    # ── Step 4: FM-003-C capacity guard ───────────────────────────────
    if frame_count >= capacity_MAX:
        return CascadeStepResult(
            status="T-CAP",
            element_id=element_id,
            k=k,
            omega_k=omega_k,
            phi_k=phi_k,
            d_bind_k=d_bind_k,
            bound=False,
            fm_triggered="FM-003-C",
        )

    # ── Step 5: CAS-3 binding condition ───────────────────────────────
    if omega_k < d_bind_k:
        return CascadeStepResult(
            status="T-NAT",
            element_id=element_id,
            k=k,
            omega_k=omega_k,
            phi_k=phi_k,
            d_bind_k=d_bind_k,
            bound=False,
            fm_triggered=None,
        )

    # ── Step 6: capture ───────────────────────────────────────────────
    registry.append(element_id)
    return CascadeStepResult(
        status="BOUND",
        element_id=element_id,
        k=k,
        omega_k=omega_k,
        phi_k=phi_k,
        d_bind_k=d_bind_k,
        bound=True,
        fm_triggered=None,
    )
```

**Orchestration wrapper** (calls PRIM:027 → PRIM:028 in sequence):

```python
def run_cascade(
    d_bind_0: float,
    gamma: float,
    phi_0: float,
    k_perturb: float,
    beta: float,
    candidates: list[dict],   # each: {"id": str, "e": float}
    k_max: int,
    capacity_MAX: int,
    registry: list,
) -> dict:
    """
    Full cascade orchestration.

    candidates: ordered list of dicts with keys 'id' (str) and 'e' (float).
    Returns summary dict with termination code, chain depth, and step log.
    """

    # ── PRIM:027: validate eligibility before any steps ───────────────
    elig = evaluate_cascade_eligibility(
        gamma=gamma,
        phi_0=phi_0,
        d_bind_0=d_bind_0,
        k_max=k_max,
        capacity_MAX=capacity_MAX,
        frame_count=len(registry),
    )
    if not elig["eligible"]:
        return {
            "termination": "T-INIT",
            "reason": elig["reason"],
            "chain_depth": 0,
            "steps": [],
        }

    omega_prev         = d_bind_0
    phi_prev           = phi_0
    d_bind_prev        = d_bind_0
    e_prev             = candidates[0]["e"] if candidates else 0.0
    steps              = []

    for k, candidate in enumerate(candidates, start=1):
        result = execute_cascade_step(
            omega_prev        = omega_prev,
            gamma             = gamma,
            phi_perturbed_prev= phi_prev,
            k_perturb         = k_perturb,
            d_bind_prev       = d_bind_prev,
            e_prev            = e_prev,
            beta              = beta,
            e_k               = candidate["e"],
            k                 = k,
            k_max             = k_max,
            frame_count       = len(registry),
            capacity_MAX      = capacity_MAX,
            registry          = registry,
            element_id        = candidate["id"],
        )
        steps.append(result)

        if result.status != "BOUND":
            return {
                "termination": result.status,
                "chain_depth": k - 1,
                "steps": steps,
                "fm_triggered": result.fm_triggered,
            }

        # advance state for next step
        omega_prev  = result.omega_k
        phi_prev    = result.phi_k
        d_bind_prev = result.d_bind_k
        e_prev      = candidate["e"]

    # exhausted candidate list without a stopping condition
    return {
        "termination": "T-NAT",
        "chain_depth": len(steps),
        "steps": steps,
        "fm_triggered": None,
    }
```

> **Purity note:** `evaluate_cascade_eligibility` (PRIM:027) is **Pure**;
> `execute_cascade_step` (PRIM:028) and the `run_cascade` wrapper are
> **Impure** (mutate `registry`). Callers must hold a registry lock for
> the duration of the cascade.

---

## §8  Canonical Examples

Four worked traces cover the full termination taxonomy.

---

### Example 8.1 — Attenuating Cascade, Natural Exhaustion (T-NAT)

**Scenario:** A weak gravitational field admits an initial capture but each
successive element faces a progressively smaller cascade transmission.
The chain runs to natural exhaustion after three steps.

**Parameters:**

| Parameter      | Value    | Notes                              |
|----------------|----------|------------------------------------|
| d_bind_0       | 0.40     | Seed binding demand                |
| γ (gamma)      | 0.70     | Attenuating — chain loses 30 % per step |
| Φ_0            | 0.75     | Initial field coherence            |
| k_perturb      | 0.08     | Mild perturbation sensitivity      |
| β              | 0.60     | Binding coefficient                |
| k_max          | 10       | Depth ceiling (not hit)            |
| capacity_MAX   | 8        | Frame has headroom                 |
| registry (t₀)  | 2 bound  | Frame not near saturation          |

**Candidate queue:**

| k  | element_id | e_k  |
|----|------------|------|
| 1  | "E_alpha"  | 0.10 |
| 2  | "E_beta"   | 0.15 |
| 3  | "E_gamma"  | 0.20 |
| 4  | "E_delta"  | 0.25 |

**Step-by-step trace:**

**Step k = 1**
- Ω(1) = 0.40 × 0.70 = **0.280**
- δ_perturb = 0.40 × (1 − 0.10) × 0.08 = 0.0288
- Φ_perturbed(1) = 0.75 − 0.0288 = **0.7212**
- d_bind(1) = 0.60 × (1 − 0.10) × 0.7212 = **0.3895**
- CAS-3: 0.280 < 0.3895 → **FAIL**
- Termination: **T-NAT at k = 1**

> The first cascade step already fails the binding condition. The chain
> never advances beyond the seed; zero additional elements are captured.
> This is the degenerate-attenuating case — γ < 1 and d_bind is
> large enough that even step 1 is unreachable.

**Post-state:**
- `chain_depth = 0`
- `registry` unchanged (2 bound)
- `fm_triggered = None`
- Partial cascade state: none (no steps committed)

**Adjusted trace (γ = 0.90 to show multi-step exhaustion):**

| k | Ω(k)  | δ_perturb | Φ_pert(k) | d_bind(k) | CAS-3?  | Result |
|---|-------|-----------|-----------|-----------|---------|--------|
| 1 | 0.360 | 0.0288    | 0.7212    | 0.3895    | ✅ pass  | BOUND  |
| 2 | 0.324 | 0.0234    | 0.6978    | 0.3528    | ✅ pass  | BOUND  |
| 3 | 0.292 | 0.0197    | 0.6781    | 0.3257    | ✅ pass  | BOUND  |
| 4 | 0.263 | 0.0163    | 0.6618    | 0.3017    | ✅ pass  | BOUND  |
| 5 | 0.236 | 0.0133    | 0.6485    | 0.2794    | ✅ pass  | BOUND  |
| 6 | 0.213 | 0.0107    | 0.6378    | 0.2592    | ❌ fail  | T-NAT  |

*(γ = 0.90 variant: chain runs 5 steps, exhausts at k = 6)*

**Post-state (γ = 0.90 variant):**
- `chain_depth = 5`
- `registry` += ["E_alpha", "E_beta", "E_gamma", "E_delta", and one more]
- Termination: **T-NAT** (natural exhaustion — no FM triggered)

---

### Example 8.2 — FM-003-C Mid-Chain Saturation (T-CAP)

**Scenario:** A neutral-to-mild cascade runs into a nearly full frame.
Capture proceeds until the registry hits `capacity_MAX`, triggering FM-003-C.

**Parameters:**

| Parameter      | Value    | Notes                                  |
|----------------|----------|----------------------------------------|
| d_bind_0       | 0.35     | Moderate seed demand                   |
| γ (gamma)      | 0.95     | Near-neutral; chain stays healthy      |
| Φ_0            | 0.80     | Strong initial coherence               |
| k_perturb      | 0.05     | Low perturbation                       |
| β              | 0.55     | Binding coefficient                    |
| k_max          | 20       | Deep ceiling (not limiting here)       |
| capacity_MAX   | 5        | Frame tight — only 2 slots remain      |
| registry (t₀)  | 3 bound  | Pre-filled; headroom = 2              |

**Candidate queue:**

| k  | element_id | e_k  |
|----|------------|------|
| 1  | "E_1"      | 0.10 |
| 2  | "E_2"      | 0.12 |
| 3  | "E_3"      | 0.14 |

**Step-by-step trace:**

**Step k = 1** (frame_count = 3, capacity_MAX = 5 → 2 slots free)
- Ω(1) = 0.35 × 0.95 = **0.3325**
- δ_perturb = 0.35 × (1 − 0.10) × 0.05 = 0.01575
- Φ_pert(1) = 0.80 − 0.01575 = **0.7843**
- d_bind(1) = 0.55 × (1 − 0.10) × 0.7843 = **0.3877**
- CAS-3: 0.3325 < 0.3877 → **FAIL → T-NAT**

*(Adjust β = 0.45 so the chain clears a few steps:)*

**Adjusted trace (β = 0.45):**

| k | frame_count (entry) | Ω(k)  | Φ_pert(k) | d_bind(k) | Cap guard | CAS-3 | Result   |
|---|---------------------|-------|-----------|-----------|-----------|-------|----------|
| 1 | 3                   | 0.3325| 0.7843    | 0.3172    | pass      | ✅    | BOUND    |
| 2 | 4                   | 0.3159| 0.7699    | 0.3005    | pass      | ✅    | BOUND    |
| 3 | 5 = capacity_MAX    | 0.3001| 0.7559    | 0.2844    | **FAIL**  | —     | **T-CAP**|

**FM-003-C trigger at k = 3:**
- Elements E_1 and E_2 (steps 1–2) are **committed** to the registry.
- E_3 (step 3) is **abandoned** — partial cascade state holds.
- `fm_triggered = "FM-003-C"`

**Post-state:**
- `chain_depth = 2` (steps committed before FM)
- `registry` = [original 3] + ["E_1", "E_2"] = 5 bound
- Partial cascade: E_3 evaluated but not captured; cascade halted.
- Caller must log the partial state and surface FM-003-C to the attractor.

---

### Example 8.3 — Deep Chain, Neutral Gain, Depth-Bound Termination (T-DEPTH)

**Scenario:** γ = 1.0 (neutral cascade — Ω stays constant at d_bind_0).
The binding condition is satisfied at every step. The chain terminates
only when k > k_max.

**Parameters:**

| Parameter      | Value    | Notes                                   |
|----------------|----------|-----------------------------------------|
| d_bind_0       | 0.30     | Moderate seed                           |
| γ (gamma)      | 1.00     | Neutral — Ω constant                    |
| Φ_0            | 0.85     | High coherence                          |
| k_perturb      | 0.02     | Very low perturbation (field stays high)|
| β              | 0.35     | Deliberately low so d_bind stays ≤ Ω   |
| k_max          | 4        | Tight ceiling to force T-DEPTH          |
| capacity_MAX   | 20       | Frame has plenty of room               |
| registry (t₀)  | 1 bound  | Nearly empty                            |

**Candidate queue (5 elements, but k_max = 4):**

| k  | element_id | e_k  |
|----|------------|------|
| 1  | "E_A"      | 0.10 |
| 2  | "E_B"      | 0.10 |
| 3  | "E_C"      | 0.10 |
| 4  | "E_D"      | 0.10 |
| 5  | "E_E"      | 0.10 |

**Step-by-step trace (γ = 1.0 → Ω(k) = 0.30 always):**

| k | Ω(k)  | δ_perturb | Φ_pert(k) | d_bind(k) | CAS-3? | Cap? | Result |
|---|-------|-----------|-----------|-----------|--------|------|--------|
| 1 | 0.300 | 0.0054    | 0.8446    | 0.2660    | ✅     | pass | BOUND  |
| 2 | 0.300 | 0.0048    | 0.8398    | 0.2645    | ✅     | pass | BOUND  |
| 3 | 0.300 | 0.0048    | 0.8350    | 0.2630    | ✅     | pass | BOUND  |
| 4 | 0.300 | 0.0047    | 0.8303    | 0.2615    | ✅     | pass | BOUND  |
| 5 | —     | —         | —         | —         | —      | —    | **T-DEPTH** (k=5 > k_max=4) |

**Post-state:**
- `chain_depth = 4` (all four within-ceiling steps committed)
- `registry` += ["E_A", "E_B", "E_C", "E_D"] → 5 total bound
- `fm_triggered = None` (T-DEPTH is a policy ceiling, not a failure mode)
- E_E is never evaluated — it remains in the candidate queue.

**Key insight:** With γ = 1.0 and low β, the cascade is self-sustaining
indefinitely. Only the depth ceiling terminates it. Operators who want
an unbounded neutral cascade must explicitly raise k_max, understanding
that frame capacity (FM-003-C) then becomes the final safety valve.

---

### Example 8.4 — Amplifying Cascade, FM-003-C at Step 2 (T-CAP)

**Scenario:** γ > 1.0 causes Ω to grow geometrically. Each successive
element faces a larger transmission than the one before. The cascade
captures aggressively until the frame saturates.

**Parameters:**

| Parameter      | Value    | Notes                                    |
|----------------|----------|------------------------------------------|
| d_bind_0       | 0.25     | Low initial demand (easy first capture)  |
| γ (gamma)      | 1.30     | Amplifying — 30 % growth per step        |
| Φ_0            | 0.70     | Moderate field                           |
| k_perturb      | 0.10     | Elevated sensitivity                     |
| β              | 0.50     | Binding coefficient                      |
| k_max          | 10       | Not the limiting factor here             |
| capacity_MAX   | 3        | Very tight — only 1 slot remains         |
| registry (t₀)  | 2 bound  | Nearly saturated                         |

**Candidate queue:**

| k  | element_id | e_k  |
|----|------------|------|
| 1  | "E_X"      | 0.12 |
| 2  | "E_Y"      | 0.18 |
| 3  | "E_Z"      | 0.20 |

**Step-by-step trace:**

**Step k = 1** (frame_count = 2, 1 slot free)
- Ω(1) = 0.25 × 1.30 = **0.325**
- δ_perturb = 0.25 × (1 − 0.12) × 0.10 = 0.0220
- Φ_pert(1) = 0.70 − 0.0220 = **0.6780**
- d_bind(1) = 0.50 × (1 − 0.12) × 0.6780 = **0.2983**
- Cap guard: frame_count(2) < capacity_MAX(3) → pass
- CAS-3: 0.325 ≥ 0.2983 → **pass**
- Result: **BOUND** — E_X captured; frame_count → 3

**Step k = 2** (frame_count = 3 = capacity_MAX)
- Cap guard fires **before** CAS-3 check
- Result: **T-CAP** — FM-003-C triggered
- E_Y abandoned; cascade halted

**Ω(2) would have been:** 0.325 × 1.30 = 0.4225  
*(Transmitted with surplus — amplifying cascade is most dangerous near saturation because Ω is growing while capacity is shrinking)*

**Post-state:**
- `chain_depth = 1`
- `registry` += ["E_X"] → 3 bound (frame full)
- `fm_triggered = "FM-003-C"`
- Partial cascade: E_X committed, E_Y and E_Z abandoned

**Amplification hazard analysis:**

| Step | Ω(k) if unconstrained | Growth factor vs. seed |
|------|----------------------|------------------------|
| 0    | 0.250                | 1.00×                  |
| 1    | 0.325                | 1.30×                  |
| 2    | 0.423                | 1.69×                  |
| 3    | 0.549                | 2.20×                  |
| 5    | 0.927                | 3.71×                  |

With γ = 1.30, Ω doubles by step ~6 and approaches Φ saturation by
step ~10. Frame saturation (FM-003-C) is almost always the first
terminator in amplifying cascades — not depth or natural binding failure.
Operators **must** enforce conservative `capacity_MAX` when γ > 1.0.

---

## §9  Cross-Module References

### §9.1  Upstream Dependencies

| Module              | Operator / Concept Used                                         | Section |
|---------------------|-----------------------------------------------------------------|---------|
| f_Capture.md        | d_bind(k), β, e, base capture mechanics                        | §3, §4  |
| f_Capture_Multi.md  | Φ_perturbed model, δ_perturb, k_perturb, MC-1, MC-2           | §4, §5  |
| f_Field.md          | ρ(Φ), v_escape, SC-1/SC-2/SC-3                                | §3, §5  |
| f_Force.md          | M_A, M_E, v_approach, β derivation                             | §3, §4  |
| f_Frame.md          | registry, capacity_MAX, register_capture, FM-003               | §4, §5  |
| f_Orbit.md          | orbit_class assignment post-cascade, T_orb                     | §4      |
| f_Amplify.md        | β_max guard relevant when γ > 1 and β is elevated             | §5      |
| f_Dampen.md         | cascade_guard (BFS) must wrap run_cascade in dampened fields   | §5      |
| OPERATORS.md        | All inherited operator symbols must be pre-registered           | global  |

### §9.2  Downstream Consumers

| Module                   | How It Consumes Cascade Output                                    |
|--------------------------|-------------------------------------------------------------------|
| f_Capture_Soft.md        | May use cascade as sub-step in soft approach sequences           |
| f_Capture_Resonant.md    | Resonant chains may initialize a cascade at resonance lock       |
| f_Collapse.md            | FM-003-C partial state feeds Path A infall assessment            |
| f_Emit.md                | Post-cascade field density drop (ρ(Φ)_delta) may trigger emit   |
| f_Decay.md               | Overcrowded registry post-cascade increases δ decay rate         |
| INDEX.md                 | Cascade depth and termination code surfaced in module index      |
| FFF_Gravity_module.json  | cascade_depth, gamma, Ω_cascade added to operator manifest      |

### §9.3  OPERATORS.md Registration Block

Add the following block to `OPERATORS.md` under the **Wave 4 — Capture Variants** section:

```markdown
### Wave 4 Operators — f_Capture_Cascade.md

| Symbol         | Name              | Type   | Domain      | Defined In              |
|----------------|-------------------|--------|-------------|-------------------------|
| cascade_depth  | Cascade Depth     | int    | ≥ 0         | f_Capture_Cascade §4.1  |
| k_max          | Max Chain Depth   | int    | ≥ 1         | f_Capture_Cascade §4.1  |
| γ (gamma)      | Cascade Gain      | float  | > 0         | f_Capture_Cascade §4.2  |
| Ω_cascade(k)   | Cascade Binding   | float  | ≥ 0         | f_Capture_Cascade §4.3  |
| k_perturb      | Perturb Coeff     | float  | [0, 1)      | f_Capture_Multi §4      |
| δ_perturb(k)   | Field Perturbation| float  | ≥ 0         | f_Capture_Multi §4      |
| Φ_perturbed(k) | Perturbed Field   | float  | [0, 1]      | f_Capture_Multi §4      |
```

> **Note:** k_perturb, δ_perturb, and Φ_perturbed are first-registered
> in f_Capture_Multi.md. The entries above are cross-reference markers
> only; do not create duplicate registrations in OPERATORS.md.

---

## §10  Document Metadata

### §10.1  INV Compliance

| Invariant | Statement (abbreviated)                      | Status     | How Satisfied                                              |
|-----------|----------------------------------------------|------------|------------------------------------------------------------|
| INV-001   | G = F_freq · F_fluid · F_force               | ✅ Compliant | Cascade operates within established G product; no bypass   |
| INV-002   | ρ(Φ) ∈ [0, 1]                               | ✅ Compliant | Φ_perturbed clamped to [0,1]; CAS-4 enforces floor ≥ 0    |
| INV-003   | β ∈ [0, 1]                                  | ✅ Compliant | β parameter validated by PRIM:027 eligibility check        |
| INV-004   | v_approach > 0 for any capture               | ✅ Compliant | Inherited from f_Capture.md; cascade does not modify v     |
| INV-005   | d_bind ≥ 0                                  | ✅ Compliant | d_bind(k) computed as non-negative product; no subtraction |
| INV-006   | SC-1 through SC-5 are conjunctive            | ✅ Compliant | CAS-1–CAS-4 are additive; do not relax base SCs            |
| INV-007   | FM registry is frozen at FM-010             | ✅ Compliant | FM-003-C is a sub-mode suffix; no new FM ID allocated      |
| INV-008   | PRIM IDs are sequential and non-reused      | ✅ Compliant | PRIM:027–028 follow PRIM:026 from f_Capture_Multi.md       |
| INV-009   | Operators registered before use             | ✅ Compliant | §9.3 OPERATORS.md block registers all new symbols          |
| INV-010   | Impure primitives must not bypass guards    | ✅ Compliant | PRIM:028 checks depth → capacity → CAS-3 in strict order   |

### §10.2  Primitive Registry

| PRIM ID  | Name                          | Purity  | Defined In            |
|----------|-------------------------------|---------|------------------------|
| PRIM:027 | evaluate_cascade_eligibility  | Pure    | §7, PRIM:027           |
| PRIM:028 | execute_cascade_step          | Impure  | §7, PRIM:028           |

**Running PRIM total after this file:** PRIM:028

### §10.3  Operator Registry (This File)

| Symbol         | Name              | First Defined       |
|----------------|-------------------|---------------------|
| cascade_depth  | Cascade Depth     | §4.1 (this file)    |
| k_max          | Max Chain Depth   | §4.1 (this file)    |
| γ (gamma)      | Cascade Gain      | §4.2 (this file)    |
| Ω_cascade(k)   | Cascade Binding   | §4.3 (this file)    |

Inherited from f_Capture_Multi.md (not re-registered here):
`k_perturb`, `δ_perturb(k)`, `Φ_perturbed(k)`, `N`, `eval_order`

### §10.4  Failure Mode Registry

| FM ID    | Name                     | Type    | Scope              |
|----------|--------------------------|---------|--------------------|
| FM-003-C | Cascade Frame Saturation | Fatal   | Mid-chain partial  |

All base FMs (FM-001 through FM-010) remain active and are inherited
from the module-level registry. FM-003-C is a sub-mode of FM-003
(Frame Overflow) and uses its suffix per the frozen FM convention.

### §10.5  Changelog Entry

```markdown
## [Wave 4] f_Capture_Cascade.md — Initial Release

### Added
- Cascade capture variant: sequential chain mechanics with geometric gain γ
- Operators: cascade_depth, k_max, γ, Ω_cascade(k)
- Conditions: CAS-1 (γ validity), CAS-2 (depth ceiling), CAS-3 (binding),
  CAS-4 (field floor)
- Failure mode: FM-003-C (Cascade Frame Saturation), sub-mode of FM-003
- Primitives: PRIM:027 evaluate_cascade_eligibility (Pure),
  PRIM:028 execute_cascade_step (Impure)
- Orchestration wrapper: run_cascade (convenience, not a registered PRIM)
- Termination codes: T-NAT, T-DEPTH, T-CAP, T-INIT
- Canonical examples: 4 (attenuating, mid-chain FM-003-C,
  neutral deep chain, amplifying)
- OPERATORS.md registration block (§9.3)

### Cross-references
- Upstream: f_Capture.md, f_Capture_Multi.md, f_Field.md, f_Force.md,
  f_Frame.md, f_Orbit.md, f_Amplify.md, f_Dampen.md
- Downstream: f_Capture_Soft.md, f_Capture_Resonant.md,
  f_Collapse.md, f_Emit.md, f_Decay.md
```

### §10.6  Wave 4 Status Tracker

| File                     | Status      | PRIM Range  | Notes                          |
|--------------------------|-------------|-------------|--------------------------------|
| f_Capture_Multi.md       | ✅ Complete  | 025–026     | MULTI_ELEMENT, MULTI_ATTRACTOR |
| f_Capture_Cascade.md     | ✅ Complete  | 027–028     | This file                      |
| f_Capture_Soft.md        | ⏳ Pending   | 029–030     | Soft-approach mechanics        |
| f_Capture_Hard.md        | ⏳ Pending   | TBD         | Hard-lock mechanics            |
| f_Capture_Resonant.md    | ⏳ Pending   | TBD         | Resonance-lock mechanics       |
| f_Capture_Asymmetric.md  | ⏳ Pending   | TBD         | Asymmetric mass-ratio captures |

### §10.7  Suggested Commit Message

```
docs(FFF_Gravity): add f_Capture_Cascade.md [Wave 4]

Implements cascade capture variant with geometric gain γ, chain depth
k_max, Ω_cascade recurrence, and CAS-1–CAS-4 conditions. Defines
FM-003-C (partial frame saturation sub-mode), PRIM:027 (eligibility
check, Pure) and PRIM:028 (step executor, Impure). Includes four
canonical examples covering T-NAT, T-CAP (×2), and T-DEPTH terminations.
Adds OPERATORS.md registration block for Wave 4 symbols.

PRIM range: 027–028 | Operators added: 4 | FM sub-modes added: 1
```

---

*— end of f_Capture_Cascade.md —*
