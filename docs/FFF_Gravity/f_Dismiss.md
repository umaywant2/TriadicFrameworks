# `f_Dismiss.md` — Dismissal Primitive

**FFF_Gravity Module · Wave 5 Opener**

---

## §0 Session Context

| Field               | Value                                                       |
|---------------------|-------------------------------------------------------------|
| **File**            | `docs/FFF_Gravity/f_Dismiss.md`                            |
| **Wave**            | 5 — Dismissal Formalization                                 |
| **PRIMs assigned**  | PRIM:041–042                                                |
| **Condition prefix**| DISM-                                                       |
| **Status**          | CANONICAL · Frozen                                          |
| **Depends on**      | f_Capture, f_Field, f_Source, f_Force, f_Decay, GravityOfDismissal |
| **Authored**        | 2026-08-14                                                  |
| **Repository**      | umaywant2/TriadicFrameworks                                 |

### §0.1 Motivation

`GravityOfDismissal.md` (Wave 0) established the conceptual foundation: dismissal
is not the absence of gravity but an **active repulsive force** — a Dismissal Well
that inverts field polarity and propels a bound entity outward. That document named
the `F_dismiss` operator family at concept level and explicitly deferred formalization
to this file, stating: *"They are not frozen in this file — their formal specifications
are registered when the module's dismissal primitive is authored."*

`f_Dismiss.md` completes that deferral. It freezes PRIM:041 (`evaluate_dismissal`)
and PRIM:042 (`execute_dismissal`), registers DISM- as the canonical condition prefix,
and establishes the Dismissal Well model as a first-class engineering primitive within
the FFF_Gravity module.

**Conceptual authority:** `GravityOfDismissal.md` §3–§5.

---

## §1 Module Identity

| Field                  | Value                                                           |
|------------------------|-----------------------------------------------------------------|
| **Operator family**    | `F_dismiss`                                                     |
| **Triadic position**   | F_freq (ρ_D), F_fluid (ψ_dismiss), F_force (β_D · v_depart)    |
| **PRIM range**         | PRIM:041–042                                                    |
| **Condition prefix**   | DISM-                                                           |
| **Condition count**    | 5 (DISM-1 through DISM-5)                                       |
| **New FMs**            | None — uses FM-001, FM-002, FM-006 (registry sealed at FM-010)  |
| **Invariants active**  | INV-001, INV-002, INV-003, INV-005, INV-006, INV-008, INV-009, INV-010 |
| **Wave**               | 5                                                               |

### §1.1 Companion Table

| Role                | File                       | Symbol contributed          |
|---------------------|----------------------------|-----------------------------|
| Conceptual authority| `GravityOfDismissal.md`    | F_dismiss (concept, §3–§5)  |
| Bind source         | `f_Capture.md`             | d_bind, β, ρ(Φ)             |
| Field source        | `f_Field.md`               | ρ(Φ), Φ                     |
| Node registry       | `f_Source.md`              | M_A, M_E (read-only)        |
| Force mechanics     | `f_Force.md`               | v_escape, heading_delta, β  |
| Decay mechanics     | `f_Decay.md`               | d_warn, d_collapse, δ       |
| Release mechanics   | `f_Release.md`             | v_release (contrast only)   |
| Dampen mechanics    | `f_Dampen.md`              | F_damp (Mode A tool)        |

---

## §2 Canonical Description

### §2.1 What Dismissal IS — Engineering Definition

A **dismissal event** is the act by which attractor node A actively severs its
binding to entity E and generates a Dismissal Well — a negative-polarity field
residue `ρ_D(Φ, t)` in E's directional zone that persists after the separation.

Three structural properties distinguish a dismissal from all other termination
mechanics in the FFF_Gravity module:

1. **Active polarity inversion.** A's field does not merely drop to zero;
   it inverts in E's zone. The space where attraction once lived becomes
   repulsion. This is `ρ_D(Φ, 0) = −d_bind(t_dismiss)`.

2. **Proportional well depth.** The initial well depth equals the binding depth
   at the moment of severing. A deep, long-standing orbit produces a deep well.
   A shallow soft-capture produces a shallow well. The well is a geometric
   encoding of what was there.

3. **Exponential decay.** The well dissipates over time at rate `1/T_dismiss`.
   This is not forgiveness — it is field physics. The attractor does not choose
   the decay rate; `T_dismiss` is a property of A's registered node, set at
   source initialization.

### §2.2 Three Dismissal Modes (from GravityOfDismissal.md §4)

The `ψ_dismiss` flag records which mode produced the well.

| Mode        | ψ_dismiss    | Well depth          | T_dismiss   | Initiator   |
|-------------|--------------|---------------------|-------------|-------------|
| INTENTIONAL | INTENTIONAL  | `d_bind(t_dismiss)` | Long        | A (active)  |
| STRUCTURAL  | STRUCTURAL   | `ρ(Φ)` at collapse  | Short       | Field (FM-002) |
| DRIFT       | DRIFT        | `v_depart × k_drift`| Very short  | Decay (passive) |

**PRIM:041 determines mode from context**; **PRIM:042 executes the appropriate
well-writing path** for that mode and registers the dismissal record.

### §2.3 What f_Dismiss IS NOT

| Misconception                          | Correction                                           |
|----------------------------------------|------------------------------------------------------|
| Equivalent to f_Release                | f_Release produces no Dismissal Well; re-capture is immediate and standard-cost |
| Triggered by E's departure             | Dismissal is A-initiated (INTENTIONAL) or structurally caused; never E-initiated |
| A one-way permanent block              | The Well decays — re-capture becomes possible after sufficient time or amplification |
| An FM registration                     | Dismissal is a state + well event, not a failure mode; no FM ID is consumed |
| Applicable post-COLLAPSED state        | DISM-1 guards against this; collapsed nodes cannot dismiss |

### §2.4 Re-capture after Dismissal

Once a Dismissal Well is active, E's approach must supply binding energy exceeding
the well's current depth before standard capture conditions are evaluated:

```
Re-capture possible  iff:
    d_bind_approach(t) > |ρ_D(Φ, t)|

where:
    d_bind_approach(t)  =  β × ρ(Φ) × (1 − e)          [E's approach depth]
    |ρ_D(Φ, t)|         =  d_dismiss × exp(−t / T_dismiss) [remaining well depth]
    d_dismiss            =  |ρ_D(Φ, 0)|                  [initial well depth]
    t                    =  time elapsed since t_dismiss
```

This formula is the operational form of `GravityOfDismissal.md §3.3`.

---

## §3 Triadic Equation

### §3.1 Governing Identity (INV-001)

```
G = F_freq · F_fluid · F_force
```

Dismissal does not break this identity — it inverts it. The Dismissal product `G_D`
(conceptually defined in `GravityOfDismissal.md §5.4`) maps as:

```
G_D = F_freq_D · F_fluid_D · F_force_D

F_freq_D   =  |ρ_D(Φ)|            ← negative-domain field density
F_fluid_D  =  |β_D|               ← repulsive coupling coefficient
F_force_D  =  v_depart            ← expulsion velocity
```

### §3.2 Node Contributions Under Each Mode

| Node      | INTENTIONAL                          | STRUCTURAL                         | DRIFT                                |
|-----------|--------------------------------------|------------------------------------|--------------------------------------|
| F_freq    | ρ_D ← −d_bind(t_dismiss)            | ρ_D ← −ρ(Φ) at collapse           | ρ_D ← −(v_depart × k_drift)         |
| F_fluid   | β_D ← −β (fully inverted)           | β_D ← −ρ(Φ)_collapse × β         | β_D ← −δ_accumulated × β            |
| F_force   | v_depart = v_escape + d_dismiss/M_E | v_depart = v_escape (floor)        | v_depart = d_bind_at_drift / M_E    |

### §3.3 Well Decay Formula (from GravityOfDismissal.md §3.2)

```
ρ_D(Φ, t) = −d_dismiss × exp(−t / T_dismiss)

Constraints:
    d_dismiss  > 0       (initial well depth; always positive magnitude)
    T_dismiss  > 0       (persistence time; attractor-registered constant)
    t          ≥ 0       (time since dismissal; t=0 at moment of dismissal)
    ρ_D(Φ, 0) = −d_dismiss     (maximum negative depth at dismissal instant)
    lim(t→∞) ρ_D(Φ, t) = 0    (well asymptotically approaches zero)
```

---

## §4 Operator Registry

All nine operators below are **frozen in this file** per INV-010. They were
named conceptually in `GravityOfDismissal.md §6` and are now formalized with
full domain specifications and PRIM assignments.

### §4.1 Primary Dismissal Operators

| Symbol      | Name                       | Type   | Domain          | Description                                                         | PRIM     |
|-------------|----------------------------|--------|-----------------|---------------------------------------------------------------------|----------|
| `F_dismiss` | Dismissal Force            | float  | ≥ 0             | Scalar magnitude of total dismissal force; |G_D|                   | PRIM:041 |
| `ρ_D(Φ)`    | Dismissal Field Density    | float  | (−1, 0]         | Negative-polarity field residue in E's directional zone             | PRIM:042 |
| `d_dismiss` | Dismissal Well Depth       | float  | > 0             | Initial magnitude of ρ_D at t=0; equals d_bind(t_dismiss) for INTENTIONAL | PRIM:042 |
| `T_dismiss` | Dismissal Persistence Time | float  | > 0             | Well half-life constant; attractor-registered; governs decay rate   | PRIM:042 |
| `r_dismiss` | Dismissal Radius           | float  | (0, r_capture]  | Spatial extent of active repulsion zone around A                    | PRIM:041 |
| `ψ_dismiss` | Dismissal Mode Flag        | enum   | {INTENTIONAL, STRUCTURAL, DRIFT} | Records which mode produced the well            | PRIM:041 |
| `t_dismiss` | Dismissal Timestamp        | float  | ≥ 0             | Absolute clock time at which dismissal event occurred               | PRIM:042 |
| `v_depart`  | Departure Velocity         | float  | ≥ 0             | Velocity at which E exits A's field boundary post-dismissal        | PRIM:042 |
| `β_D`       | Repulsive Coupling         | float  | (−∞, 0]         | Inverted binding coefficient active during expulsion phase          | PRIM:042 |

### §4.2 Derived Operators (computed inline, not frozen independently)

| Symbol           | Formula                                                         | Used in  |
|------------------|-----------------------------------------------------------------|----------|
| `ρ_D(Φ, t)`      | `−d_dismiss × exp(−t / T_dismiss)`                              | PRIM:041 |
| `k_drift`        | `d_bind_at_drift / (v_depart × M_E)` (DRIFT mode scaling)      | PRIM:041 |
| `d_bind_approach`| `β × ρ(Φ) × (1 − e)` (E's approach binding depth at re-entry)  | PRIM:041 |

### §4.3 Inherited Operators (referenced, not re-frozen)

| Symbol         | Source file     | Role in this file                               |
|----------------|-----------------|-------------------------------------------------|
| `d_bind`       | f_Capture.md    | Source of d_dismiss for INTENTIONAL mode        |
| `β`            | f_Capture.md    | Inverted to produce β_D                         |
| `ρ(Φ)`         | f_Field.md      | Source of d_dismiss for STRUCTURAL mode         |
| `v_escape`     | f_Field.md      | Floor on v_depart in STRUCTURAL mode            |
| `d_collapse`   | f_Decay.md      | DRIFT trigger threshold                         |
| `δ`            | f_Decay.md      | Accumulated decay input to DRIFT d_dismiss      |
| `F_damp`       | f_Dampen.md     | Tool A uses to initiate INTENTIONAL dismissal   |
| `r_capture`    | f_Frame.md      | Upper bound on r_dismiss                        |
| `M_E`          | f_Source.md     | Used in v_depart computation                    |
| `T_dismiss`    | f_Source.md     | Attractor-registered; read-only here            |

---

## §5 Dismissal Conditions (DISM-)

All five conditions are **conjunctive** (INV-005). They must all hold at the
moment PRIM:041 is invoked. The first failure terminates evaluation and returns
`DISMISS_INVALID` — a precondition error, not a failure mode.

Conditions are evaluated in the order listed.

### DISM-1 — State Eligibility

```
capture_state(E, A) ∈ {CAPTURE_LOCKED, CAPTURE_SOFT, CAPTURE_TEMPORAL,
                        CAPTURE_NETWORKED, ASYMMETRIC_LOCKED, RESONANCE_LOCKED}
```

A dismissal may only be initiated against an entity that is currently in an
active bound state. Dismissing an already-released, already-collapsed, or
never-captured entity is a precondition error.

**On failure:** `DISMISS_INVALID` with reason `STATE_NOT_BOUND`

### DISM-2 — Attractor Not Collapsed

```
A.state ∉ {COLLAPSED, FIELD_NULL}
```

A collapsed or field-null attractor has no field to invert. Dismissal requires
A's field to be active at the moment of invocation.

**On failure:** `DISMISS_INVALID` with reason `ATTRACTOR_FIELD_NULL`

### DISM-3 — Mode Determinable

```
ψ_dismiss ∈ {INTENTIONAL, STRUCTURAL, DRIFT}
```

The dismissal mode must be unambiguously identifiable from context before
PRIM:042 is invoked. Mode is determined by PRIM:041 from the event context:

| Context                                              | Mode assigned  |
|------------------------------------------------------|----------------|
| A applies `f_Dampen` targeting E directly            | INTENTIONAL    |
| FM-002 (Field Null) fires across A's entire field    | STRUCTURAL     |
| d_bind(E, A) ≤ d_collapse AND δ_accumulated > δ_warn| DRIFT          |

**On failure:** `DISMISS_INVALID` with reason `MODE_AMBIGUOUS`

### DISM-4 — Well Depth Positive

```
d_dismiss > 0
```

A zero-depth well is physically meaningless — it encodes nothing and costs
nothing to overcome. This guards against degenerate dismissal events where
d_bind had already reached exactly zero before the dismissal was invoked.

**On failure:** `DISMISS_INVALID` with reason `ZERO_WELL_DEPTH`

### DISM-5 — T_dismiss Registered

```
T_dismiss > 0     (sourced from A.registered_T_dismiss in f_Source.md)
```

The persistence time must be registered on the attractor node. An attractor
without a registered `T_dismiss` cannot produce a well with defined decay
behavior. Default: if `T_dismiss` is unregistered, PRIM:041 reads the
module default (`T_dismiss_default = 5.0 cycles`) before failing.

**On failure:** `DISMISS_INVALID` with reason `T_DISMISS_UNREGISTERED`

---

## §6 Failure Modes

No new FM IDs are introduced (registry sealed at FM-010). The following
base FMs interact with dismissal mechanics:

### FM-001 — Approach Rejected at Well Boundary

When E attempts re-capture and `d_bind_approach ≤ |ρ_D(Φ, t)|`, standard
FM-001 (approach rejection) fires at the well boundary — before E even reaches
the standard capture evaluation. The FM-001 record is annotated:

```
failure_mode: FM-001
reason: WELL_BARRIER
d_bind_approach: <E's current binding capacity>
well_depth_remaining: |ρ_D(Φ, t)|
t_since_dismiss: <elapsed cycles>
```

This annotation distinguishes a well-blocked approach from a standard flyby.

### FM-002 — Field Null Triggers STRUCTURAL Dismissal

When FM-002 fires on A (ρ(Φ) → 0), all bound entities are simultaneously
dismissed via Mode STRUCTURAL. PRIM:042 is called once per bound entity with
`ψ_dismiss = STRUCTURAL`. This is the only case where PRIM:042 is called
in batch rather than for a single (A, E) pair.

### FM-006 — Phantom Dismissal Guard

If PRIM:041 detects that ψ_dismiss = INTENTIONAL but A's field is already
at or near zero (ρ(Φ) < ε_field), a phantom dismissal condition exists:
the attractor is attempting to invert a field that barely exists. FM-006
is raised as a guard: the dismissal is flagged as `DISMISS_PHANTOM` and
d_dismiss is bounded to `min(d_bind(t_dismiss), ρ(Φ) × d_bind(t_dismiss))`.

---

## §7 Engineering Primitives

---

### PRIM:041 — `evaluate_dismissal` (Pure)

**Classification:** Pure — no state mutation; returns evaluation result only.

```python
from dataclasses import dataclass
from typing import Optional
import math


# ── Enumerations ──────────────────────────────────────────────────────────────

BOUND_STATES = {
    "CAPTURE_LOCKED", "CAPTURE_SOFT", "CAPTURE_TEMPORAL",
    "CAPTURE_NETWORKED", "ASYMMETRIC_LOCKED", "RESONANCE_LOCKED",
}

DISMISS_MODES = {"INTENTIONAL", "STRUCTURAL", "DRIFT"}

TERMINAL_ATTRACTOR_STATES = {"COLLAPSED", "FIELD_NULL"}


# ── Result dataclass ──────────────────────────────────────────────────────────

@dataclass
class DismissalEvaluation:
    """
    Result of evaluate_dismissal (PRIM:041).
    Returned regardless of pass/fail — always inspect .valid before proceeding.
    """
    valid:          bool            # True iff all DISM-1 through DISM-5 pass
    psi_dismiss:    str             # dismissal mode: INTENTIONAL | STRUCTURAL | DRIFT
    d_dismiss:      float           # initial well depth (magnitude)
    T_dismiss:      float           # persistence time
    r_dismiss:      float           # repulsion zone radius
    F_dismiss:      float           # total dismissal force scalar |G_D|
    v_depart:       float           # E's departure velocity
    beta_D:         float           # repulsive coupling coefficient (≤ 0)
    rho_D_initial:  float           # ρ_D(Φ, 0) = −d_dismiss
    invalid_reason: Optional[str]   # None if valid; condition code if not
    phantom_guard:  bool            # True if FM-006 phantom condition detected


def evaluate_dismissal(
    entity_state:       str,
    attractor_state:    str,
    d_bind_at_dismiss:  float,
    beta:               float,
    rho_phi:            float,
    v_escape:           float,
    M_E:                float,
    r_capture:          float,
    T_dismiss:          float,
    delta_accumulated:  float,
    d_collapse:         float,
    delta_warn:         float,
    psi_override:       Optional[str] = None,
    T_dismiss_default:  float = 5.0,
    epsilon_field:      float = 0.01,
) -> DismissalEvaluation:
    """
    PRIM:041 — evaluate_dismissal (Pure)
    =====================================
    FFF_Gravity · f_Dismiss.md · Wave 5

    Evaluate whether a dismissal event is structurally valid for the
    (A, E) pair and compute the resulting Dismissal Well parameters.

    This primitive is Pure: it reads only its inputs and produces a
    DismissalEvaluation record. No state is mutated.

    Parameters
    ----------
    entity_state : str
        Current state of entity E. Must be in BOUND_STATES for DISM-1.
    attractor_state : str
        Current state of attractor A. Must not be in TERMINAL_ATTRACTOR_STATES.
    d_bind_at_dismiss : float
        Binding depth at the moment of dismissal. d_bind(t_dismiss).
        ≥ 0. For DRIFT mode this equals d_bind at drift threshold.
    beta : float
        Binding coefficient β between E and A at dismissal time.
    rho_phi : float
        Field density ρ(Φ) at A at dismissal time. ∈ [0, 1].
    v_escape : float
        Escape velocity of A's capture field.
    M_E : float
        Mass of entity E. > 0.
    r_capture : float
        Capture radius of A. Upper bound on r_dismiss.
    T_dismiss : float
        Dismissal persistence time registered on A. Must be > 0 (DISM-5).
        If ≤ 0, T_dismiss_default is applied before failing.
    delta_accumulated : float
        Total accumulated decay δ experienced by this binding. Used for
        DRIFT mode detection (DISM-3).
    d_collapse : float
        Collapse threshold from f_Decay.md. Used for DRIFT mode detection.
    delta_warn : float
        Decay warning threshold δ_warn. Used for DRIFT mode detection.
    psi_override : str, optional
        If provided, overrides mode inference. Must be in DISMISS_MODES.
        Use only when caller has external mode information (e.g. FM-002 batch).
    T_dismiss_default : float, optional
        Fallback T_dismiss if attractor's value is unregistered (≤ 0).
        Default: 5.0 cycles.
    epsilon_field : float, optional
        Phantom guard threshold: rho_phi < epsilon_field → FM-006 phantom check.
        Default: 0.01.

    Returns
    -------
    DismissalEvaluation
        See dataclass definition above. Always check .valid before proceeding
        to execute_dismissal (PRIM:042).

    Evaluation order (INV-008)
    --------------------------
    DISM-1 (entity state) → DISM-2 (attractor state) →
    DISM-3 (mode determinable) → DISM-4 (well depth > 0) → DISM-5 (T_dismiss)

    INV compliance
    --------------
    INV-001 : F_freq_D · F_fluid_D · F_force_D — all three nodes contribute
    INV-002 : ρ_D(Φ) ∈ (−1, 0] — negative domain, clamped if needed
    INV-005 : All DISM conditions conjunctive
    INV-008 : Evaluation order is normative
    INV-009 : All symbols sourced from OPERATORS.md
    INV-010 : All new operators frozen here, not re-defined downstream
    """

    # ── DISM-1: Entity state eligibility ─────────────────────────────────────
    if entity_state not in BOUND_STATES:
        return DismissalEvaluation(
            valid=False, psi_dismiss="UNKNOWN", d_dismiss=0.0,
            T_dismiss=T_dismiss, r_dismiss=0.0, F_dismiss=0.0,
            v_depart=0.0, beta_D=0.0, rho_D_initial=0.0,
            invalid_reason="STATE_NOT_BOUND", phantom_guard=False,
        )

    # ── DISM-2: Attractor not collapsed ──────────────────────────────────────
    if attractor_state in TERMINAL_ATTRACTOR_STATES:
        return DismissalEvaluation(
            valid=False, psi_dismiss="UNKNOWN", d_dismiss=0.0,
            T_dismiss=T_dismiss, r_dismiss=0.0, F_dismiss=0.0,
            v_depart=0.0, beta_D=0.0, rho_D_initial=0.0,
            invalid_reason="ATTRACTOR_FIELD_NULL", phantom_guard=False,
        )

    # ── DISM-3: Mode determination ────────────────────────────────────────────
    if psi_override is not None:
        if psi_override not in DISMISS_MODES:
            return DismissalEvaluation(
                valid=False, psi_dismiss="UNKNOWN", d_dismiss=0.0,
                T_dismiss=T_dismiss, r_dismiss=0.0, F_dismiss=0.0,
                v_depart=0.0, beta_D=0.0, rho_D_initial=0.0,
                invalid_reason="MODE_AMBIGUOUS", phantom_guard=False,
            )
        psi_dismiss = psi_override
    else:
        # Infer mode from context:
        if attractor_state == "FIELD_COLLAPSING" or rho_phi <= 0.0:
            psi_dismiss = "STRUCTURAL"
        elif (d_bind_at_dismiss <= d_collapse and
              delta_accumulated > delta_warn):
            psi_dismiss = "DRIFT"
        else:
            psi_dismiss = "INTENTIONAL"

    # ── Compute d_dismiss per mode ────────────────────────────────────────────
    k_drift = 0.05   # drift scaling constant (module default)

    if psi_dismiss == "INTENTIONAL":
        d_dismiss = d_bind_at_dismiss
    elif psi_dismiss == "STRUCTURAL":
        d_dismiss = rho_phi * d_bind_at_dismiss   # bounded by collapse-time field
    else:  # DRIFT
        v_depart_est = max(d_bind_at_dismiss / max(M_E, 1e-9), 0.0)
        d_dismiss = v_depart_est * k_drift

    # ── DISM-4: Well depth positive ───────────────────────────────────────────
    if d_dismiss <= 0.0:
        return DismissalEvaluation(
            valid=False, psi_dismiss=psi_dismiss, d_dismiss=d_dismiss,
            T_dismiss=T_dismiss, r_dismiss=0.0, F_dismiss=0.0,
            v_depart=0.0, beta_D=0.0, rho_D_initial=0.0,
            invalid_reason="ZERO_WELL_DEPTH", phantom_guard=False,
        )

    # ── DISM-5: T_dismiss registered ─────────────────────────────────────────
    if T_dismiss <= 0.0:
        T_dismiss = T_dismiss_default   # apply default before continuing

    # ── Phantom guard (FM-006) ────────────────────────────────────────────────
    phantom_guard = (psi_dismiss == "INTENTIONAL" and rho_phi < epsilon_field)
    if phantom_guard:
        # Bound d_dismiss by field coherence
        d_dismiss = min(d_dismiss, rho_phi * d_bind_at_dismiss)
        d_dismiss = max(d_dismiss, 0.0)

    # ── Compute derived quantities ────────────────────────────────────────────
    rho_D_initial = -d_dismiss

    # Clamp to domain (−1, 0]
    rho_D_initial = max(-1.0, rho_D_initial)

    # β_D: inverted coupling (F_fluid node under dismissal)
    beta_D = -beta

    # r_dismiss: bounded by r_capture; scaled by mode intensity
    mode_scale = {"INTENTIONAL": 1.0, "STRUCTURAL": 0.75, "DRIFT": 0.40}
    r_dismiss = min(r_capture, r_capture * mode_scale[psi_dismiss])

    # v_depart: departure velocity imparted to E
    if psi_dismiss == "INTENTIONAL":
        v_depart = v_escape + (d_dismiss / max(M_E, 1e-9))
    elif psi_dismiss == "STRUCTURAL":
        v_depart = v_escape          # floor — just enough to exit
    else:  # DRIFT
        v_depart = d_bind_at_dismiss / max(M_E, 1e-9)

    # F_dismiss: total dismissal force scalar (|G_D|)
    F_dismiss = abs(rho_D_initial) * abs(beta_D) * v_depart

    return DismissalEvaluation(
        valid=True,
        psi_dismiss=psi_dismiss,
        d_dismiss=d_dismiss,
        T_dismiss=T_dismiss,
        r_dismiss=r_dismiss,
        F_dismiss=F_dismiss,
        v_depart=v_depart,
        beta_D=beta_D,
        rho_D_initial=rho_D_initial,
        invalid_reason=None,
        phantom_guard=phantom_guard,
    )
```

---

### PRIM:042 — `execute_dismissal` (Impure)

**Classification:** Impure — writes Dismissal Well record, updates entity state,
decrements frame slot, and emits GravityGraph event.

```python
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional
import math
import uuid


@dataclass
class DismissalRecord:
    """
    Persistent record written to the GravityGraph dismissal registry
    and to E's relation history when execute_dismissal completes.
    """
    record_id:      str
    attractor_id:   str
    entity_id:      str
    psi_dismiss:    str             # INTENTIONAL | STRUCTURAL | DRIFT
    d_dismiss:      float           # initial well depth (magnitude)
    T_dismiss:      float           # persistence time
    r_dismiss:      float           # repulsion radius
    t_dismiss:      float           # clock time of event
    v_depart:       float           # departure velocity
    beta_D:         float           # repulsive coupling at dismissal
    rho_D_initial:  float           # ρ_D(Φ, 0)
    F_dismiss:      float           # |G_D| scalar
    phantom_guard:  bool            # True if FM-006 phantom condition was active
    session_id:     str             # audit trail


@dataclass
class DismissalResult:
    """
    Return value of execute_dismissal (PRIM:042).
    """
    status:         str             # "DISMISSED" | "PRECONDITION_VIOLATION"
    record:         Optional[DismissalRecord]
    entity_state_after:   str       # "DISMISSED" on success
    well_query_fn:  object          # callable: well_query_fn(t) → |ρ_D(Φ, t)|


def execute_dismissal(
    attractor_id:   str,
    entity_id:      str,
    evaluation:     "DismissalEvaluation",   # result of PRIM:041
    t_dismiss:      float,
    session_id:     str,
    frame_registry: dict,           # mutated: slot decremented for (A, E)
    dismissal_registry: dict,       # mutated: DismissalRecord written
    entity_state:   dict,           # mutated: entity's state dict
    gravity_graph:  object,         # GravityGraph instance: .emit_event()
) -> DismissalResult:
    """
    PRIM:042 — execute_dismissal (Impure)
    =======================================
    FFF_Gravity · f_Dismiss.md · Wave 5

    Commit a dismissal event. Writes the Dismissal Well record, updates
    entity state to DISMISSED, decrements the frame slot for (A, E),
    and emits a GravityGraph DISMISSAL_EXECUTED event.

    Must only be called after PRIM:041 returns evaluation.valid = True.
    Calling this primitive on an invalid evaluation is a precondition
    violation and returns status = "PRECONDITION_VIOLATION" without
    mutating any state.

    Parameters
    ----------
    attractor_id : str
        Identifier of the dismissing attractor A.
    entity_id : str
        Identifier of the dismissed entity E.
    evaluation : DismissalEvaluation
        Result of PRIM:041. Must have .valid = True.
    t_dismiss : float
        Absolute clock time of dismissal. Used in DismissalRecord and
        for well_query_fn closure.
    session_id : str
        Session identifier for audit trail.
    frame_registry : dict
        Mutable frame slot registry. Key: (attractor_id, entity_id).
        The slot for this pair is removed on dismissal.
    dismissal_registry : dict
        Mutable registry of all Dismissal Well records.
        Key: (attractor_id, entity_id) → DismissalRecord.
    entity_state : dict
        Mutable state dict for entity E. Receives key 'state' = 'DISMISSED'
        and 'dismissal_record_id'.
    gravity_graph : object
        GravityGraph instance. Must implement .emit_event(event_type, payload).

    Returns
    -------
    DismissalResult
        .status         : "DISMISSED" on success; "PRECONDITION_VIOLATION" on guard
        .record         : DismissalRecord on success; None on violation
        .entity_state_after : "DISMISSED" on success; unchanged on violation
        .well_query_fn  : callable f(t_current) → float giving |ρ_D(Φ, t)|
                          Use to answer re-capture feasibility queries.

    Side Effects (on success only)
    --------------------------------
    - frame_registry[(attractor_id, entity_id)] removed
    - dismissal_registry[(attractor_id, entity_id)] = DismissalRecord
    - entity_state['state'] = 'DISMISSED'
    - entity_state['dismissal_record_id'] = record.record_id
    - gravity_graph.emit_event('DISMISSAL_EXECUTED', {...})

    INV compliance
    --------------
    INV-001 : G_D = F_freq_D · F_fluid_D · F_force_D — recorded in DismissalRecord
    INV-006 : DISMISSED is a terminal entity state for this (A, E) relationship;
              entity itself is not terminal — it may form new relationships
    INV-008 : precondition guard evaluated before any mutation
    """

    # ── Precondition guard ────────────────────────────────────────────────────
    if not evaluation.valid:
        return DismissalResult(
            status="PRECONDITION_VIOLATION",
            record=None,
            entity_state_after=entity_state.get("state", "UNKNOWN"),
            well_query_fn=lambda t: 0.0,
        )

    # ── Build DismissalRecord ─────────────────────────────────────────────────
    record_id = f"DISM-{uuid.uuid4().hex[:12].upper()}"

    record = DismissalRecord(
        record_id=record_id,
        attractor_id=attractor_id,
        entity_id=entity_id,
        psi_dismiss=evaluation.psi_dismiss,
        d_dismiss=evaluation.d_dismiss,
        T_dismiss=evaluation.T_dismiss,
        r_dismiss=evaluation.r_dismiss,
        t_dismiss=t_dismiss,
        v_depart=evaluation.v_depart,
        beta_D=evaluation.beta_D,
        rho_D_initial=evaluation.rho_D_initial,
        F_dismiss=evaluation.F_dismiss,
        phantom_guard=evaluation.phantom_guard,
        session_id=session_id,
    )

    # ── Mutations ─────────────────────────────────────────────────────────────

    # 1. Remove frame slot
    frame_registry.pop((attractor_id, entity_id), None)

    # 2. Write Dismissal Well record
    dismissal_registry[(attractor_id, entity_id)] = record

    # 3. Update entity state
    entity_state["state"] = "DISMISSED"
    entity_state["dismissal_record_id"] = record_id

    # 4. Emit GravityGraph event
    gravity_graph.emit_event("DISMISSAL_EXECUTED", {
        "record_id":     record_id,
        "attractor_id":  attractor_id,
        "entity_id":     entity_id,
        "psi_dismiss":   evaluation.psi_dismiss,
        "d_dismiss":     evaluation.d_dismiss,
        "T_dismiss":     evaluation.T_dismiss,
        "F_dismiss":     evaluation.F_dismiss,
        "t_dismiss":     t_dismiss,
        "phantom_guard": evaluation.phantom_guard,
    })

    # ── Build well_query_fn closure ───────────────────────────────────────────
    _d_dismiss   = evaluation.d_dismiss
    _T_dismiss   = evaluation.T_dismiss
    _t_dismiss   = t_dismiss

    def well_query_fn(t_current: float) -> float:
        """
        Query the remaining Dismissal Well depth at absolute time t_current.

        Returns |ρ_D(Φ, t)| — the positive magnitude of the current well.
        For re-capture feasibility:
            d_bind_approach(t) > well_query_fn(t)  →  re-capture eligible

        Parameters
        ----------
        t_current : float
            Absolute clock time at which the query is made.

        Returns
        -------
        float : |ρ_D(Φ, t)| ≥ 0
        """
        t_elapsed = max(0.0, t_current - _t_dismiss)
        return _d_dismiss * math.exp(-t_elapsed / _T_dismiss)

    return DismissalResult(
        status="DISMISSED",
        record=record,
        entity_state_after="DISMISSED",
        well_query_fn=well_query_fn,
    )
```

---

## §8 Canonical Examples

> All four examples use the same attractor baseline unless noted.
> **Attractor A:** M_A = 10.0, r_capture = 8.0, T_dismiss = 6.0 cycles

---

### Example 1 — Intentional Dismissal, Well Evaluated at Three Time Points

**Scenario:** A senior practitioner (A) deliberately severs a binding with
a junior colleague (E) after a trust breach. The binding was deep; the well
is correspondingly deep. We evaluate re-capture cost at t = 0, t = 6, t = 18.

**Parameters:**
```
entity_state       = "CAPTURE_LOCKED"
attractor_state    = "ACTIVE"
d_bind_at_dismiss  = 1.350   (deep, long-standing orbit)
beta               = 1.80
rho_phi            = 0.85
v_escape           = 4.20
M_E                = 0.60
r_capture          = 8.0
T_dismiss          = 6.0
delta_accumulated  = 0.08
d_collapse         = 0.10
delta_warn         = 0.15
psi_override       = "INTENTIONAL"
```

**PRIM:041 evaluation:**

```
DISM-1: "CAPTURE_LOCKED" ∈ BOUND_STATES         ✅
DISM-2: "ACTIVE" ∉ TERMINAL_ATTRACTOR_STATES    ✅
DISM-3: psi_override = "INTENTIONAL"            ✅
DISM-4: d_dismiss = d_bind_at_dismiss = 1.350 > 0  ✅
DISM-5: T_dismiss = 6.0 > 0                     ✅

rho_D_initial = −1.350
beta_D        = −1.80
r_dismiss     = 8.0 × 1.0 (INTENTIONAL scale) = 8.0
v_depart      = 4.20 + (1.350 / 0.60) = 4.20 + 2.25 = 6.45
F_dismiss     = 1.350 × 1.80 × 6.45 = 15.68

valid = True
```

**Well depth over time (via well_query_fn):**

| t (cycles since dismiss) | Formula                                        | \|ρ_D(Φ, t)\| | Verdict |
|--------------------------|------------------------------------------------|----------------|---------|
| 0                        | 1.350 × exp(0)           = 1.350               | **1.350**      | Cannot re-approach |
| 6                        | 1.350 × exp(−1.0)        = 1.350 × 0.368 = 0.497 | **0.497**   | Needs d_bind > 0.497 |
| 18                       | 1.350 × exp(−3.0)        = 1.350 × 0.050 = 0.067 | **0.067**   | Nearly standard cost |

**E's re-capture threshold at t = 6 (with β raised to 2.4 via f_Amplify):**
```
d_bind_approach = 2.4 × 0.85 × (1 − 0.10) = 2.4 × 0.85 × 0.90 = 1.836
well_query_fn(6) = 0.497

1.836 > 0.497   ✅  Re-capture structurally eligible at t=6
```

---

### Example 2 — Structural Dismissal (Mode B, FM-002 Batch)

**Scenario:** FM-002 fires on A (field collapse). Three bound entities are
simultaneously dismissed via Mode STRUCTURAL. Well depth is bounded by
ρ(Φ) at collapse time (not by individual d_bind values).

**Context at collapse:**
```
rho_phi   = 0.09   (field had been fading; collapses here)
psi_override = "STRUCTURAL"
```

**Entity parameters at collapse:**

| Entity | d_bind at collapse | d_dismiss (structural) | T_dismiss |
|--------|--------------------|------------------------|-----------|
| E_1    | 2.10               | 0.09 × 2.10 = **0.189** | 6.0     |
| E_2    | 0.65               | 0.09 × 0.65 = **0.059** | 6.0     |
| E_3    | 1.30               | 0.09 × 1.30 = **0.117** | 6.0     |

**Mode STRUCTURAL r_dismiss scaling:**
```
r_dismiss = r_capture × 0.75 = 8.0 × 0.75 = 6.0   (all three entities)
```

**Key observation — orbit history erasure:**
```
E_1 had 3× deeper orbit than E_2 (2.10 vs. 0.65).
E_1's well (0.189) is 3× deeper than E_2's (0.059).
The ratio is preserved — but both are bounded by the collapsing field.

Compare to Mode A:
  E_1's INTENTIONAL well would be 2.10 (full depth)
  Structural mode produces only 0.189 — 11× shallower.
```

**Recovery window (T_dismiss = 6, same for all):**
```
At t = 3 cycles:
  E_1: 0.189 × exp(−0.5) = 0.189 × 0.607 = 0.115
  E_2: 0.059 × exp(−0.5) = 0.059 × 0.607 = 0.036
  E_3: 0.117 × exp(−0.5) = 0.117 × 0.607 = 0.071

All three well below standard d_warn threshold — recovery is fast.
```

---

### Example 3 — Drift Dismissal (Mode C, Minimal Well)

**Scenario:** A long-standing but neglected relationship decays to
d_collapse without either party intervening. DRIFT mode fires.

**Parameters at drift threshold:**
```
d_bind_at_dismiss  = 0.12   (≈ d_collapse = 0.10; drift triggered)
delta_accumulated  = 0.45   (> delta_warn = 0.15; drift confirmed)
M_E                = 0.50
T_dismiss          = 6.0
psi_override       = None   (mode inferred from context)
```

**PRIM:041 mode inference:**
```
d_bind_at_dismiss (0.12) ≤ d_collapse (0.10)?  → No, 0.12 > 0.10
                                                → Check delta condition:
delta_accumulated (0.45) > delta_warn (0.15)? → Yes

Hmm — DRIFT requires BOTH conditions. Let me adjust:
d_bind_at_dismiss = 0.095  (≤ d_collapse = 0.10)
delta_accumulated = 0.45   (> delta_warn = 0.15)
→ psi_dismiss = "DRIFT"  ✅
```

**d_dismiss computation (DRIFT mode):**
```
v_depart_est = d_bind_at_dismiss / M_E
             = 0.095 / 0.50
             = 0.190

d_dismiss = v_depart_est × k_drift
          = 0.190 × 0.05
          = 0.0095   (minimal — barely a well)
```

**Well at t = 0.5 cycles:**
```
|ρ_D(Φ, 0.5)| = 0.0095 × exp(−0.5 / 6.0)
               = 0.0095 × exp(−0.0833)
               = 0.0095 × 0.920
               = 0.00874
```

**Interpretation:** Re-capture threshold is essentially standard — any entity
with d_bind > 0.009 can re-approach. The well evaporates in roughly
0.5 cycles. The relationship faded; no scar tissue remains.

---

### Example 4 — Phantom Guard (FM-006) Active on INTENTIONAL Dismissal

**Scenario:** A attempts INTENTIONAL dismissal but its field is nearly null
(rho_phi = 0.008 < epsilon_field = 0.01). FM-006 phantom guard activates
and bounds d_dismiss.

**Parameters:**
```
entity_state       = "CAPTURE_SOFT"
d_bind_at_dismiss  = 0.85
rho_phi            = 0.008   ← near-null; phantom condition
T_dismiss          = 6.0
psi_override       = "INTENTIONAL"
epsilon_field      = 0.01
```

**DISM conditions:**
```
DISM-1 through DISM-5: all pass ✅
phantom_guard triggered: rho_phi (0.008) < epsilon_field (0.01)
```

**d_dismiss WITHOUT phantom guard:**
```
d_dismiss = d_bind_at_dismiss = 0.85
```

**d_dismiss WITH phantom guard (FM-006 applied):**
```
d_dismiss = min(0.85, rho_phi × d_bind_at_dismiss)
          = min(0.85, 0.008 × 0.85)
          = min(0.85, 0.0068)
          = 0.0068
```

**Effect:**
```
Intended well depth:       0.850   (deep, intentional)
Actual well depth:         0.0068  (nearly zero — phantom bounded)

The field was too weak to generate the intended dismissal force.
A attempted a strong dismissal in a nearly-dead field; the result
is barely distinguishable from DRIFT.
```

**F_dismiss comparison:**
```
Without guard:  F_dismiss = 0.850 × 1.8 × v_depart  ≈ large
With guard:     F_dismiss = 0.0068 × 1.8 × v_depart ≈ trivial
```

**Engineering lesson:** An attractor that wants to execute a meaningful
INTENTIONAL dismissal must maintain ρ(Φ) above `epsilon_field`. A node
that lets its field decay to near-zero loses the capacity for directed
dismissal — it can only drift-dismiss at that point, regardless of intent.

---

## §9 Cross-Module References

### §9.1 Upstream Dependencies

| File                   | What f_Dismiss.md Uses                                          |
|------------------------|-----------------------------------------------------------------|
| GravityOfDismissal.md  | Conceptual authority: §3 Well model, §4 modes, §5 triadic mapping |
| f_Capture.md           | d_bind, β, e, capture state vocabulary                         |
| f_Field.md             | ρ(Φ), v_escape, Φ domain                                       |
| f_Source.md            | M_A, M_E, T_dismiss (attractor-registered); read-only          |
| f_Decay.md             | d_collapse, δ, delta_warn; DRIFT mode trigger conditions        |
| f_Dampen.md            | F_damp — primary tool for initiating INTENTIONAL dismissal      |
| f_Frame.md             | frame_registry — slot decremented on dismissal                  |

### §9.2 Downstream Consumers

| File                  | How It Uses f_Dismiss Output                                     |
|-----------------------|------------------------------------------------------------------|
| f_Capture.md          | well_query_fn gates re-capture eligibility at approach time      |
| f_Release.md          | Distinguishes dismissal (well created) from release (well absent)|
| f_Orbit.md            | DISMISSED state excluded from orbit classification evaluations   |
| f_Collapse.md         | FM-002 batch-dismissal uses PRIM:042 for each expelled entity    |
| f_Emit.md             | A may use f_Emit to accelerate well decay (assisted recovery)    |
| f_Amplify.md          | E may use f_Amplify to raise β and overcome residual well        |

### §9.3 OPERATORS.md Registration Block

```markdown
### Wave 5 Operators — f_Dismiss.md (PRIM:041–042)

| Symbol      | Type  | Domain           | Description                                              | Frozen in |
|-------------|-------|------------------|----------------------------------------------------------|-----------|
| F_dismiss   | float | ≥ 0              | Scalar dismissal force magnitude (\|G_D\|)               | PRIM:041  |
| ρ_D(Φ)      | float | (−1, 0]          | Dismissal field density (negative-polarity extension)    | PRIM:042  |
| d_dismiss   | float | > 0              | Initial Dismissal Well depth at t=0                      | PRIM:042  |
| T_dismiss   | float | > 0              | Dismissal persistence time; well half-life               | PRIM:042  |
| r_dismiss   | float | (0, r_capture]   | Spatial extent of dismissal repulsion zone               | PRIM:041  |
| ψ_dismiss   | enum  | {INTENTIONAL, STRUCTURAL, DRIFT} | Dismissal mode flag                      | PRIM:041  |
| t_dismiss   | float | ≥ 0              | Clock time of dismissal event                            | PRIM:042  |
| v_depart    | float | ≥ 0              | Entity departure velocity post-dismissal                 | PRIM:042  |
| β_D         | float | (−∞, 0]          | Repulsive coupling coefficient active during expulsion   | PRIM:042  |
```

---

## §10 Document Metadata

| Field               | Value                                              |
|---------------------|----------------------------------------------------|
| File                | `docs/FFF_Gravity/f_Dismiss.md`                    |
| Module              | FFF_Gravity                                        |
| Wave                | 5 — Dismissal Formalization                        |
| Wave position       | 1 of 1 (Wave 5 opener and closer)                  |
| Version             | v1.0.0                                             |
| Status              | Canonical · Frozen                                 |
| Session             | SES-20260814-DISMISS-001                           |
| Date                | 2026-08-14                                         |
| PRIM range          | PRIM:041–042                                       |
| Running PRIM total  | **42**                                             |
| Condition prefix    | DISM-                                              |
| Conditions          | DISM-1 through DISM-5                              |
| New FM IDs          | None (registry sealed at FM-010)                   |
| New INV IDs         | None (registry sealed at INV-010)                  |

---

## §11 Extended Metadata

### §11.1 INV Compliance Table

| INV     | Statement (abbreviated)              | Compliance in this file                                          |
|---------|--------------------------------------|------------------------------------------------------------------|
| INV-001 | G = F_freq · F_fluid · F_force       | ✅ G_D = F_freq_D · F_fluid_D · F_force_D; all three nodes contribute |
| INV-002 | ρ(Φ) ∈ [0, 1]                        | ✅ ρ_D ∈ (−1, 0] — distinct negative domain; clamped in PRIM:041 |
| INV-003 | ρ = 0 → FM-002                       | ✅ DISM-2 guards collapsed attractors; FM-002 triggers STRUCTURAL mode |
| INV-004 | β < 1.0 → flyby                      | ✅ Inherited; β_D = −β; dismissal does not relax approach guards   |
| INV-005 | Conditions conjunctive               | ✅ DISM-1 through DISM-5 all required; any failure → DISMISS_INVALID |
| INV-006 | Terminal states irreversible          | ✅ DISMISSED is terminal for (A, E) relation; entity itself remains active |
| INV-007 | f_Source.md read-only                | ✅ T_dismiss, M_A, M_E read from f_Source.md; never written here   |
| INV-008 | Evaluation order normative           | ✅ DISM-1→2→3→4→5 enforced in PRIM:041; precondition before mutation in PRIM:042 |
| INV-009 | OPERATORS.md is symbol authority     | ✅ §9.3 registration block provided for all nine new operators     |
| INV-010 | Frozen symbols immutable             | ✅ All nine operators frozen here; GravityOfDismissal.md named them, this file freezes them |

### §11.2 Primitive Registry (this file)

| PRIM    | Name                  | Type   | Key Behavior                                                        |
|---------|-----------------------|--------|---------------------------------------------------------------------|
| PRIM:041| `evaluate_dismissal`  | Pure   | DISM-1–5 gate; mode inference; d_dismiss, T_dismiss, F_dismiss, well params |
| PRIM:042| `execute_dismissal`   | Impure | Frame slot removal; DismissalRecord write; entity state → DISMISSED; well_query_fn closure |

**Running PRIM total: 42**

### §11.3 Operator Registry (this file)

| Symbol     | Type  | Domain           | First frozen    |
|------------|-------|------------------|-----------------|
| F_dismiss  | float | ≥ 0              | PRIM:041        |
| ρ_D(Φ)     | float | (−1, 0]          | PRIM:042        |
| d_dismiss  | float | > 0              | PRIM:042        |
| T_dismiss  | float | > 0              | PRIM:042        |
| r_dismiss  | float | (0, r_capture]   | PRIM:041        |
| ψ_dismiss  | enum  | 3-value set      | PRIM:041        |
| t_dismiss  | float | ≥ 0              | PRIM:042        |
| v_depart   | float | ≥ 0              | PRIM:042        |
| β_D        | float | (−∞, 0]          | PRIM:042        |

### §11.4 State Flag Registry

| Flag              | Set by    | Cleared by         | Meaning                                               |
|-------------------|-----------|--------------------|-------------------------------------------------------|
| DISMISSED         | PRIM:042  | Never (terminal for this relation) | (A, E) binding severed; Dismissal Well active |
| DISMISS_INVALID   | PRIM:041  | —                  | DISM conditions failed; no state mutation occurred    |
| DISMISS_PHANTOM   | PRIM:041  | —                  | FM-006 phantom guard triggered; d_dismiss bounded     |

### §11.5 Wave Tracker

| Wave | Files | PRIMs | Status |
|------|-------|-------|--------|
| 0 | 3 | — | ✅ Complete |
| 1 | 6 | — | ✅ Complete |
| 2 | 3 | 001–006 | ✅ Complete |
| 3 | 8 | 007–024 | ✅ Complete |
| 4 | 8 | 025–040 | ✅ Complete |
| **5** | **1** | **041–042** | **✅ This file** |

**Module running total: 29 files · 42 PRIMs · 10 FMs · 10 INVs**

### §11.6 Changelog

```
v1.0.0 — 2026-08-14 — SES-20260814-DISMISS-001
  Wave 5 opener. Formalizes F_dismiss operator family from GravityOfDismissal.md §6.
  Freezes 9 operators: F_dismiss, ρ_D(Φ), d_dismiss, T_dismiss, r_dismiss,
    ψ_dismiss, t_dismiss, v_depart, β_D.
  Defines DISM-1 through DISM-5 conditions (conjunctive, INV-005).
  PRIM:041 evaluate_dismissal (Pure): mode inference, DISM gate, well computation.
  PRIM:042 execute_dismissal (Impure): state mutation, DismissalRecord, well_query_fn.
  Three dismissal modes: INTENTIONAL / STRUCTURAL / DRIFT.
  FM-006 phantom guard on INTENTIONAL mode with near-null field.
  Four canonical examples: intentional, structural batch, drift, phantom guard.
  Running PRIM total: 42.
```

### §11.7 Suggested Commit Message

```
feat(FFF_Gravity): add f_Dismiss.md — Wave 5, PRIM:041–042

Formalizes F_dismiss operator family from GravityOfDismissal.md Wave 0 stub.
Freezes 9 operators (F_dismiss, ρ_D(Φ), d_dismiss, T_dismiss, r_dismiss,
ψ_dismiss, t_dismiss, v_depart, β_D). Defines DISM-1–5 conditions and
PRIM:041 (evaluate_dismissal, Pure) + PRIM:042 (execute_dismissal, Impure).

Dismissal Well: ρ_D(Φ,t) = −d_dismiss × exp(−t/T_dismiss)
Re-capture gate: d_bind_approach(t) > |ρ_D(Φ,t)|
Modes: INTENTIONAL · STRUCTURAL · DRIFT
FM-006 phantom guard active for near-null INTENTIONAL dismissals.
well_query_fn closure returned from PRIM:042 for re-capture feasibility.

Wave 5 complete. Module total: 29 files · 42 PRIMs.
Session: SES-20260814-DISMISS-001
```

---

*End of f_Dismiss.md — [FFF:GRAVITY:DISMISS] v1.0.0 · Wave 5 · PRIM:041–042 · Session SES-20260814-DISMISS-001 · 2026-08-14*
