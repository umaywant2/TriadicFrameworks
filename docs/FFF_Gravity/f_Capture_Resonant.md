# f_Capture_Resonant — Resonance-Locked Capture

```
id: f_Capture_Resonant
title: "f_Capture_Resonant — Resonance-Locked Capture"
module: FFF_Gravity
version: 1.0.0
status: canonical
wave: 4
session: SES-20260813-FGRAV-033
date: 2026-08-13
authors:
  - umaywant2
invariants_enforced:
  - INV-001
  - INV-002
  - INV-003
  - INV-004
  - INV-005
  - INV-006
  - INV-008
  - INV-009
failure_modes_referenced:
  - FM-001
  - FM-002
  - FM-003
  - FM-004
  - FM-006
primitives_defined:
  - PRIM:033
  - PRIM:034
depends_on:
  - f_Capture.md
  - f_Orbit.md
  - f_Field.md
  - f_Force.md
  - OPERATORS.md
```

---

**Module:** FFF_Gravity
**Wave:** 4 — Capture Variants
**Version:** 1.0.0
**Status:** Canonical
**Session:** SES-20260813-FGRAV-033
**Date:** 2026-08-13

---

## §0 Session Context

This file is the fifth of six capture-variant documents in Wave 4 of the
FFF_Gravity module. It specifies the **resonance-locked capture** pathway:
a capture that succeeds only when the entity E arrives within a narrow
orbital timing window defined by the attractor A's resonance frequency
ω_res.

Resonance-locked capture is the rarest canonical capture mode. Where soft
capture tolerates partial binding and hard capture demands threshold excess,
resonant capture demands *timing precision*: the approach vector must phase-
align with A's field oscillation cycle. An otherwise-qualified approach
(β ≥ 1.0, ρ(Φ) sufficient) is rejected as a flyby (FM-001) if it arrives
outside the resonance window.

Successful resonant capture writes `orbit_class = RESONANT` (defined in
f_Orbit.md §3) and produces the highest possible d_bind stability — resonant
orbits are deeply phase-locked and resist perturbation until field coherence
falls below a dedicated resonance-floor threshold.

**Symbols introduced here are registered in OPERATORS.md per INV-009.**
No new FM IDs are created per the FM freeze protocol; FM-004 (resonance drift)
serves as the recoverable warning for resonance degradation.

---

## §1 Module Identity

| Field               | Value                                                         |
|---------------------|---------------------------------------------------------------|
| File path           | docs/FFF_Gravity/f_Capture_Resonant.md                       |
| Parent operator     | f_Capture.md (base capture contract)                         |
| Peer variants       | f_Capture_Multi.md, f_Capture_Cascade.md, f_Capture_Soft.md, f_Capture_Hard.md |
| Successor           | f_Capture_Asymmetric.md                                       |
| Orbit class written | RESONANT                                                      |
| Condition prefix    | RLC- (Resonance Lock Condition)                               |
| State flags         | WINDOW_OPEN, WINDOW_CLOSED, RESONANCE_LOCKED, RESONANCE_LOST  |
| Primitives          | PRIM:033 (eval_resonance_window), PRIM:034 (lock_resonance)  |
| Failure modes used  | FM-001 (flyby), FM-002 (field null), FM-003 (saturation),    |
|                     | FM-004 (resonance drift), FM-006 (phantom capture)           |

---

## §2 Canonical Description

### 2.1 Motivation

Standard capture (f_Capture.md) requires β ≥ 1.0 and ρ(Φ) > 0 to bind E
to A. These conditions are necessary but not sufficient for resonant capture:
resonant capture additionally requires that E's arrival phase aligns with A's
oscillation cycle.

A's field coherence ρ(Φ) is not static — it oscillates at angular frequency
ω_res (radians per unit time). At resonance peaks, the binding force is
amplified; at troughs, it is suppressed. An entity arriving at a trough may
not achieve orbit even if all scalar conditions pass.

Resonance-locked capture exploits this oscillation: E must arrive within a
phase window [φ_open, φ_close] relative to ω_res. If it does, d_bind is
multiplied by a resonance gain factor (ρ_res_gain). If it does not, capture
is rejected and E continues on its approach trajectory — recorded as FM-001
with the sub-annotation `REASON: WINDOW_MISS`.

### 2.2 Physical Analogy

In orbital mechanics, resonance describes configurations where two bodies'
orbital periods form a small integer ratio (e.g., 2:1, 3:2). Here, resonance
describes the phase relationship between E's approach timing and A's field
cycle. The Laplace resonances of Jupiter's moons provide the canonical
physical analogue: only entities arriving in the correct phase slot achieve
stable co-orbiting configurations.

### 2.3 Relationship to orbit_class = RESONANT

f_Orbit.md §3 defines four orbit classes: CIRCULAR, ELLIPTICAL, ECCENTRIC,
RESONANT. The RESONANT class is only reachable via this file. No other
capture pathway writes `orbit_class = RESONANT`.

A RESONANT orbit has the following properties (inherited from f_Orbit.md):
- `stab_class` is forced to STABLE (resonant phase-lock implies stability)
- `T_orb` is pinned to a rational multiple of A's resonance period `T_res`
- Perturbations are dampened by the phase-lock force until ρ(Φ) < ρ_res_floor
- FM-004 (resonance drift) is the only non-fatal degradation mode

### 2.4 Resonance Window Geometry

The resonance window is defined in phase space, not time space:

```
φ_open  = 2π × n_window_start     (n_window_start ∈ [0, 1))
φ_close = 2π × n_window_end       (n_window_end ∈ (0, 1], n_window_end > n_window_start)
window_width = φ_close - φ_open
```

At any clock tick t, A's current phase is:

```
φ_A(t) = (ω_res × t) mod 2π
```

E's arrival phase is `φ_E = φ_A(t_arrive)`. Capture proceeds if and only if:

```
φ_open ≤ φ_E ≤ φ_close        ← RLC-1
```

Window width `window_width` is a property of A registered at f_Source.md
initialization. Narrower windows produce rarer but deeper captures.

### 2.5 Resonance Gain and d_bind Enhancement

When E arrives in-window, d_bind is computed with a resonance gain multiplier:

```
ρ_res_gain ∈ (1.0, ∞)          (registered in f_Source.md for A)
d_bind_res = β × (ρ(Φ) × ρ_res_gain) × (1 − e)
```

Note: ρ(Φ) × ρ_res_gain must be capped at 1.0 for the coherence product,
then d_bind_res is computed. The gain amplifies the effective field density
but does not violate the ρ(Φ) ∈ [0, 1] invariant on the base field.

```
ρ_eff = min(1.0, ρ(Φ) × ρ_res_gain)
d_bind_res = β × ρ_eff × (1 − e)
```

This is the governing d_bind for RESONANT orbits. It is always ≥ standard
d_bind when ρ_res_gain ≥ 1.0.

### 2.6 Resonance Lock vs. Resonance Drift

Once locked, a RESONANT orbit remains locked as long as:

```
ρ(Φ)(t) ≥ ρ_res_floor          ← RLC-4
```

where `ρ_res_floor` is a registered threshold (default 0.30, stricter than
the general field-null threshold of 0.0 in INV-003).

If ρ(Φ) drops below ρ_res_floor but remains above 0:
- FM-004 (resonance drift) is raised as a recoverable warning
- `orbit_class` degrades from RESONANT → ELLIPTICAL
- `stab_class` degrades from STABLE → MARGINAL
- Lock is not yet lost; recovery is possible if ρ(Φ) recovers above ρ_res_floor

If ρ(Φ) subsequently falls to 0: INV-003 triggers FM-002 (field null/collapse),
and the orbit is terminal regardless of prior resonance.

---

## §3 Triadic Equation Mapping

```
G = F_freq · F_fluid · F_force
```

| Node      | Resonant-capture contribution                                   |
|-----------|-----------------------------------------------------------------|
| F_freq    | ω_res (oscillation frequency), φ_A(t) (current phase),        |
|           | T_res (resonance period), window_width (phase gate width)      |
| F_fluid   | ρ(Φ) (field coherence), ρ_res_gain (amplification factor),     |
|           | ρ_eff (capped effective coherence), ρ_res_floor (lock floor)   |
| F_force   | β (binding coefficient), d_bind_res (resonance-enhanced depth), |
|           | v_approach, r_capture (base capture scalars inherited from      |
|           | f_Capture.md), heading_delta (from f_Force.md §4.3)            |

INV-001 compliance: All three nodes participate. ω_res is a F_freq primitive;
ρ_eff is a F_fluid primitive; d_bind_res is a F_force primitive. No resonant
capture computation is possible with any node absent.

---

## §4 Operator Registry

All symbols below are registered in OPERATORS.md per INV-009.

### 4.1 Resonance Frequency and Phase

| Symbol         | Domain         | Description                                      |
|----------------|----------------|--------------------------------------------------|
| `ω_res`        | ℝ, > 0         | Angular resonance frequency of attractor A (rad/unit time) |
| `T_res`        | ℝ, > 0         | Resonance period = 2π / ω_res                    |
| `φ_A(t)`       | [0, 2π)        | Current phase of A at time t = (ω_res × t) mod 2π |
| `φ_E`          | [0, 2π)        | Arrival phase of E = φ_A(t_arrive)               |
| `φ_open`       | [0, 2π)        | Window open phase boundary                       |
| `φ_close`      | (0, 2π]        | Window close phase boundary (> φ_open)           |
| `window_width` | (0, 2π]        | φ_close − φ_open                                 |
| `t_arrive`     | ℝ, ≥ 0         | Clock tick at which E reaches r_capture          |
| `t_next_open`  | ℝ, > t_arrive  | Earliest future t where WINDOW_OPEN holds        |

### 4.2 Field Enhancement

| Symbol         | Domain         | Description                                      |
|----------------|----------------|--------------------------------------------------|
| `ρ_res_gain`   | ℝ, > 1.0       | Field amplification factor during resonance window |
| `ρ_eff`        | [0, 1]         | min(1.0, ρ(Φ) × ρ_res_gain)                     |
| `ρ_res_floor`  | (0, 1)         | Minimum ρ(Φ) to maintain resonance lock (default 0.30) |

### 4.3 Enhanced Binding

| Symbol         | Domain         | Description                                      |
|----------------|----------------|--------------------------------------------------|
| `d_bind_res`   | ℝ, ≥ 0         | Resonance-enhanced binding depth = β × ρ_eff × (1 − e) |
| `orbit_class`  | enum           | Set to RESONANT on successful lock               |
| `stab_class`   | enum           | Forced STABLE on resonance lock                  |
| `T_orb_res`    | ℝ, > 0         | Orbital period under resonance lock = p/q × T_res (p, q ∈ ℤ⁺) |
| `p_ratio`      | ℤ⁺             | Numerator of orbital resonance ratio p:q         |
| `q_ratio`      | ℤ⁺             | Denominator of orbital resonance ratio p:q       |

### 4.4 Window State Flags

| Flag               | Meaning                                                  |
|--------------------|----------------------------------------------------------|
| `WINDOW_OPEN`      | φ_E is within [φ_open, φ_close] — capture eligible      |
| `WINDOW_CLOSED`    | φ_E is outside window — capture rejected (FM-001)        |
| `RESONANCE_LOCKED` | Orbit is actively phase-locked; ρ(Φ) ≥ ρ_res_floor      |
| `RESONANCE_LOST`   | ρ(Φ) dropped below ρ_res_floor; FM-004 raised            |

---

## §5 Resonance Lock Conditions (RLC-)

All five conditions are **conjunctive** (INV-005). All must hold simultaneously
for resonance-locked capture to complete.

| ID    | Condition                                      | Failure if violated |
|-------|------------------------------------------------|---------------------|
| RLC-1 | φ_open ≤ φ_E ≤ φ_close (in-window arrival)    | FM-001 (WINDOW_MISS) |
| RLC-2 | β ≥ 1.0 (standard capture binding threshold)   | FM-001 (APPROACH_REJECTION) |
| RLC-3 | ρ(Φ) > 0 at t_arrive (field non-null)          | FM-002 (FIELD_NULL) |
| RLC-4 | ρ(Φ) ≥ ρ_res_floor post-capture (lock floor)  | FM-004 (RESONANCE_DRIFT) |
| RLC-5 | v_approach < v_escape(A) (not hyperbolic)      | FM-001 (OVERSHOOT) |

**RLC-1 is the distinguishing condition** of this variant. All other capture
variants ignore φ_E entirely. A WINDOW_MISS rejection is annotated distinctly
from standard FM-001 overshoot to aid diagnostics.

**RLC-4 is a post-capture maintenance condition**, not an entry gate. It is
evaluated on every subsequent tick after capture, not at t_arrive.

---

## §6 Failure Modes

No new FM IDs are introduced. The following FM entries apply:

### FM-001 — Flyby (two sub-cases in this variant)

**Sub-case A: WINDOW_MISS (RLC-1 violated)**
```
FM-001 raised with annotation: REASON=WINDOW_MISS
φ_E           := computed arrival phase
t_next_open   := next tick where WINDOW_OPEN will hold
                 = t_arrive + (φ_open − φ_E + 2π) mod 2π / ω_res
orbit_class   := not written (capture did not occur)
```
E continues on its pre-capture trajectory. The caller may retry by holding
E at a waiting state until t_next_open.

**Sub-case B: APPROACH_REJECTION or OVERSHOOT (RLC-2 or RLC-5 violated)**
Identical to base f_Capture.md FM-001 behavior; φ_E is irrelevant if scalar
conditions fail first.

Evaluation order per INV-008: RLC-3 → RLC-2 → RLC-5 → RLC-1.
(Field null checked first; window checked last to avoid phase calculation
on degenerate inputs.)

### FM-002 — Field Null (RLC-3 violated)
```
FM-002 raised
ρ(Φ) = 0 confirmed
d_bind_res is undefined (not computed)
orbit_class := not written
```
Behavior identical to base f_Capture.md FM-002.

### FM-003 — Frame Saturation
Evaluated against A's orbit count prior to resonant capture attempt. If A
has reached its max_orbits ceiling, the capture is refused pre-phase-check.
FM-003 annotation includes `VARIANT=RESONANT` for tracing.

### FM-004 — Resonance Drift (post-capture, recoverable)
```
Trigger: ρ(Φ)(t) < ρ_res_floor (RLC-4 violated post-capture)
State:   RESONANCE_LOCKED → RESONANCE_LOST
orbit_class: RESONANT → ELLIPTICAL
stab_class:  STABLE → MARGINAL
Action:  warning raised; orbit continues as ELLIPTICAL
Recovery: if ρ(Φ) recovers ≥ ρ_res_floor → RESONANCE_LOCKED re-asserted,
          orbit_class re-promoted to RESONANT
```
FM-004 is the only non-fatal degradation mode for a RESONANT orbit.

### FM-006 — Phantom Capture
If φ_E is in-window but ρ(Φ) is non-zero and β ≥ 1.0, yet the computed
d_bind_res resolves to 0.0 (due to eccentricity e = 1.0, i.e., p_res = 0
with P_eff = 0), FM-006 is raised: the phase alignment was real but the
binding force was phantom.

Phantom resonance is rare; the usual cause is a degenerate orbit where
the entity has zero effective momentum. The guard condition is:

```
if d_bind_res == 0.0 and all RLC pass:
    raise FM-006 (PHANTOM_RESONANCE)
```

---

## §7 Engineering Primitives

### PRIM:033 — eval_resonance_window

```python
def eval_resonance_window(
    omega_res: float,
    phi_open: float,
    phi_close: float,
    t_arrive: float,
    beta: float,
    rho_phi: float,
    v_approach: float,
    v_escape: float,
    max_orbits: int,
    current_orbit_count: int,
) -> dict:
    """
    PRIM:033 — Resonance Window Evaluator
    ======================================
    Evaluate whether entity E's arrival at attractor A satisfies all
    pre-capture Resonance Lock Conditions (RLC-1 through RLC-3, RLC-5)
    and compute the resonance arrival phase.

    This primitive performs the gate-check phase of resonant capture.
    It does NOT write orbit state — that is PRIM:034's responsibility.

    Evaluation order (INV-008):
        1. FM-003 check  — saturation guard
        2. RLC-3         — ρ(Φ) > 0
        3. RLC-2         — β ≥ 1.0
        4. RLC-5         — v_approach < v_escape
        5. RLC-1         — φ_E in [φ_open, φ_close]

    Parameters
    ----------
    omega_res : float
        Angular resonance frequency of attractor A (rad / unit time). > 0.
    phi_open : float
        Window open phase boundary. In [0, 2π).
    phi_close : float
        Window close phase boundary. In (0, 2π]. Must exceed phi_open.
    t_arrive : float
        Clock tick at which E reaches r_capture. ≥ 0.
    beta : float
        Binding coefficient of E with respect to A. ≥ 0.
    rho_phi : float
        Field coherence density at t_arrive. In [0, 1].
    v_approach : float
        Approach velocity of E toward A. ≥ 0.
    v_escape : float
        Escape velocity of A's capture field. ≥ 0. v_escape(A) from f_Force.md.
    max_orbits : int
        Frame saturation ceiling for A. From f_Frame.md.
    current_orbit_count : int
        Current number of bound orbits around A. ≥ 0.

    Returns
    -------
    dict with keys:
        status : str
            "WINDOW_OPEN" | "WINDOW_CLOSED" | "FM-001" | "FM-002" | "FM-003"
        phi_E : float
            Computed arrival phase = (omega_res × t_arrive) mod 2π.
        t_next_open : float | None
            If status == "WINDOW_CLOSED": earliest future tick where WINDOW_OPEN
            holds. None otherwise.
        failure_mode : str | None
            FM code if status is a failure. None on WINDOW_OPEN.
        reason : str | None
            Sub-annotation string (e.g., "WINDOW_MISS", "APPROACH_REJECTION").

    Invariants
    ----------
    INV-001 : F_freq (omega_res), F_fluid (rho_phi), F_force (beta) all present.
    INV-003 : rho_phi = 0 → FM-002 raised unconditionally.
    INV-004 : beta < 1.0 → FM-001 raised (flyby, approach rejection).
    INV-005 : All RLC evaluated conjunctively; first failure terminates.
    INV-008 : Evaluation order normative (saturation → null → binding → velocity → phase).
    """
    import math

    T_res = (2 * math.pi) / omega_res

    # Compute arrival phase unconditionally (used in all branches)
    phi_E = (omega_res * t_arrive) % (2 * math.pi)

    # Step 1: FM-003 — frame saturation
    if current_orbit_count >= max_orbits:
        return {
            "status": "FM-003",
            "phi_E": phi_E,
            "t_next_open": None,
            "failure_mode": "FM-003",
            "reason": "FRAME_SATURATION (VARIANT=RESONANT)",
        }

    # Step 2: RLC-3 — field non-null (INV-003)
    if rho_phi <= 0.0:
        return {
            "status": "FM-002",
            "phi_E": phi_E,
            "t_next_open": None,
            "failure_mode": "FM-002",
            "reason": "FIELD_NULL",
        }

    # Step 3: RLC-2 — binding threshold (INV-004)
    if beta < 1.0:
        return {
            "status": "FM-001",
            "phi_E": phi_E,
            "t_next_open": None,
            "failure_mode": "FM-001",
            "reason": "APPROACH_REJECTION",
        }

    # Step 4: RLC-5 — not hyperbolic
    if v_approach >= v_escape:
        return {
            "status": "FM-001",
            "phi_E": phi_E,
            "t_next_open": None,
            "failure_mode": "FM-001",
            "reason": "OVERSHOOT",
        }

    # Step 5: RLC-1 — phase window check
    if phi_open <= phi_E <= phi_close:
        return {
            "status": "WINDOW_OPEN",
            "phi_E": phi_E,
            "t_next_open": None,
            "failure_mode": None,
            "reason": None,
        }
    else:
        # Compute next open tick
        phase_gap = (phi_open - phi_E + 2 * math.pi) % (2 * math.pi)
        t_next_open = t_arrive + phase_gap / omega_res
        return {
            "status": "WINDOW_CLOSED",
            "phi_E": phi_E,
            "t_next_open": t_next_open,
            "failure_mode": "FM-001",
            "reason": "WINDOW_MISS",
        }
```

---

### PRIM:034 — lock_resonance

```python
def lock_resonance(
    beta: float,
    rho_phi: float,
    rho_res_gain: float,
    rho_res_floor: float,
    eccentricity: float,
    p_ratio: int,
    q_ratio: int,
    T_res: float,
    phi_E: float,
    phi_open: float,
    phi_close: float,
) -> dict:
    """
    PRIM:034 — Resonance Lock Writer
    =================================
    Given that PRIM:033 returned WINDOW_OPEN, compute and write the full
    resonance-locked orbit state.

    This primitive is called only after PRIM:033 confirms WINDOW_OPEN.
    Calling it without that confirmation violates INV-008 (evaluation order).

    Computes:
        ρ_eff       = min(1.0, rho_phi × rho_res_gain)
        d_bind_res  = beta × ρ_eff × (1 − eccentricity)
        T_orb_res   = (p_ratio / q_ratio) × T_res
        orbit_class = RESONANT
        stab_class  = STABLE

    Raises FM-006 (phantom) if d_bind_res resolves to 0.0 despite all
    RLC passing — indicating degenerate eccentricity (e = 1.0).

    Parameters
    ----------
    beta : float
        Binding coefficient. ≥ 1.0 (already verified by PRIM:033).
    rho_phi : float
        Field coherence density. In (0, 1] (non-null verified by PRIM:033).
    rho_res_gain : float
        Field amplification factor during resonance window. > 1.0.
    rho_res_floor : float
        Minimum ρ(Φ) to maintain resonance lock post-capture. In (0, 1).
    eccentricity : float
        Orbital eccentricity e = p_res / (p_res + P_eff). In [0, 1).
        e must be < 1.0; e = 1.0 triggers FM-006.
    p_ratio : int
        Numerator of orbital period resonance ratio p:q. ≥ 1.
    q_ratio : int
        Denominator of orbital period resonance ratio p:q. ≥ 1.
    T_res : float
        Resonance period of A = 2π / omega_res. > 0.
    phi_E : float
        Arrival phase (from PRIM:033). In [phi_open, phi_close].
    phi_open : float
        Window open phase. Informational; used in output record only.
    phi_close : float
        Window close phase. Informational; used in output record only.

    Returns
    -------
    dict with keys:
        status : str
            "RESONANCE_LOCKED" | "FM-006"
        rho_eff : float
            Effective coherence used in binding computation.
        d_bind_res : float
            Resonance-enhanced binding depth.
        T_orb_res : float
            Pinned orbital period for this resonant orbit.
        orbit_class : str
            "RESONANT" on success; None on FM-006.
        stab_class : str
            "STABLE" on success; None on FM-006.
        failure_mode : str | None
            "FM-006" on phantom; None on success.
        lock_record : dict
            Structured record for appending to f_Source.md orbit registry.

    Invariants
    ----------
    INV-001 : All three nodes contribute to d_bind_res.
    INV-002 : Ω is frozen upon RESONANCE_LOCKED; orbit_class = RESONANT.
    INV-006 : RESONANCE_LOCKED is a terminal capture state (reversible only
              via FM-004 drift degradation, not arbitrary release).
    INV-008 : Must be called after PRIM:033 confirms WINDOW_OPEN.
    """
    # Compute effective coherence (ρ_eff capped at 1.0)
    rho_eff = min(1.0, rho_phi * rho_res_gain)

    # Compute resonance-enhanced binding depth
    d_bind_res = beta * rho_eff * (1.0 - eccentricity)

    # FM-006: phantom resonance guard
    if d_bind_res == 0.0:
        return {
            "status": "FM-006",
            "rho_eff": rho_eff,
            "d_bind_res": 0.0,
            "T_orb_res": None,
            "orbit_class": None,
            "stab_class": None,
            "failure_mode": "FM-006",
            "lock_record": None,
        }

    # Compute pinned orbital period (rational multiple of T_res)
    T_orb_res = (p_ratio / q_ratio) * T_res

    # Build lock record for f_Source.md orbit registry
    lock_record = {
        "orbit_class": "RESONANT",
        "stab_class": "STABLE",
        "d_bind_res": d_bind_res,
        "rho_eff": rho_eff,
        "T_orb_res": T_orb_res,
        "p_ratio": p_ratio,
        "q_ratio": q_ratio,
        "rho_res_floor": rho_res_floor,
        "phi_lock": phi_E,
        "phi_open": phi_open,
        "phi_close": phi_close,
        "state_flag": "RESONANCE_LOCKED",
    }

    return {
        "status": "RESONANCE_LOCKED",
        "rho_eff": rho_eff,
        "d_bind_res": d_bind_res,
        "T_orb_res": T_orb_res,
        "orbit_class": "RESONANT",
        "stab_class": "STABLE",
        "failure_mode": None,
        "lock_record": lock_record,
    }
```

---

## §8 Canonical Examples

### Example 1 — Clean In-Window Resonant Capture (2:1 Resonance)

**Scenario:** Entity E approaches attractor A at exactly the resonance peak.
A has a 2:1 orbital resonance configuration; E arrives perfectly centered
in the window.

**Given:**
```
omega_res       = π / 5          (T_res = 10 time units)
phi_open        = π / 3          (≈ 1.047 rad)
phi_close       = π              (≈ 3.142 rad)
window_width    = 2π / 3         (≈ 2.094 rad; wide window)

t_arrive        = 7.5
phi_A(7.5)      = (π/5 × 7.5) mod 2π
                = (1.5π) mod 2π
                = 3π/2           (≈ 4.712 rad)
```

Wait — φ_E = 4.712 > φ_close = 3.142. RLC-1 fails. Let us recalibrate:

```
t_arrive        = 3.5
phi_A(3.5)      = (π/5 × 3.5) mod 2π
                = 0.7π           (≈ 2.199 rad)
```

RLC-1: 1.047 ≤ 2.199 ≤ 3.142  ✓ — WINDOW_OPEN

**Scalar checks:**
```
rho_phi         = 0.75
beta            = 1.8
v_approach      = 3.2, v_escape = 5.0   ← RLC-5: 3.2 < 5.0  ✓
current_orbits  = 3, max_orbits = 10    ← FM-003: clear       ✓
```

**PRIM:033 result:**
```
status      = WINDOW_OPEN
phi_E       = 2.199 rad
failure_mode = None
```

**PRIM:034 inputs:**
```
rho_res_gain    = 1.4
rho_eff         = min(1.0, 0.75 × 1.4) = min(1.0, 1.05) = 1.0
eccentricity    = 0.15  (p_res=0.3, P_eff=1.7)
d_bind_res      = 1.8 × 1.0 × (1 − 0.15) = 1.8 × 0.85 = 1.530
p_ratio=2, q_ratio=1
T_orb_res       = (2/1) × 10 = 20.0 time units
```

**PRIM:034 result:**
```
status      = RESONANCE_LOCKED
orbit_class = RESONANT
stab_class  = STABLE
d_bind_res  = 1.530
rho_eff     = 1.000 (gain saturated — field fully coherent)
T_orb_res   = 20.0
```

**Observation:** ρ_res_gain of 1.4 on ρ(Φ) = 0.75 saturates the ρ_eff cap,
demonstrating that resonance gain does not produce super-unity coherence.
d_bind_res (1.530) exceeds standard d_bind (1.8 × 0.75 × 0.85 = 1.148) by
33% — the practical benefit of resonance capture.

---

### Example 2 — Window Miss: Arrival Out of Phase (FM-001, WINDOW_MISS)

**Scenario:** E has fully qualifying scalar properties but arrives between
resonance windows. FM-001 is raised; t_next_open is computed for retry.

**Given:**
```
omega_res       = π / 4          (T_res = 8 time units)
phi_open        = π/6            (≈ 0.524 rad)
phi_close       = π/2            (≈ 1.571 rad)
window_width    = π/3            (≈ 1.047 rad; narrow window)

t_arrive        = 6.0
phi_A(6.0)      = (π/4 × 6.0) mod 2π
                = 1.5π           (≈ 4.712 rad)
```

RLC-1: 0.524 ≤ 4.712 ≤ 1.571  ✗ — WINDOW_CLOSED

**Scalar checks (all pass):**
```
rho_phi         = 0.80   ← RLC-3 ✓
beta            = 1.5    ← RLC-2 ✓
v_approach      = 2.0, v_escape = 4.5  ← RLC-5 ✓
current_orbits  = 0, max_orbits = 5    ← FM-003 clear ✓
```

**PRIM:033 result:**
```
status          = WINDOW_CLOSED
phi_E           = 4.712 rad
failure_mode    = FM-001
reason          = WINDOW_MISS

phase_gap       = (0.524 − 4.712 + 2π) mod 2π
                = (0.524 − 4.712 + 6.283) mod 2π
                = 2.095 mod 2π
                = 2.095 rad

t_next_open     = 6.0 + 2.095 / (π/4)
                = 6.0 + 2.095 / 0.785
                = 6.0 + 2.668
                = 8.668 time units
```

**Retry guidance:**
```
Hold E on approach trajectory.
Re-attempt PRIM:033 at t_arrive = 8.668.
phi_A(8.668) = (π/4 × 8.668) mod 2π ≈ 0.524 rad = φ_open  ← window just opens
```

**Observation:** The WINDOW_MISS path provides a concrete retry timestamp —
this is the key operational difference between resonant and standard capture.
A caller that treats FM-001 as terminal (rather than retry-able) would
incorrectly abandon a qualifying entity. The t_next_open return value exists
specifically to support retry scheduling.

---

### Example 3 — Resonance Drift Mid-Orbit (FM-004 Triggered, Recovery Succeeds)

**Scenario:** E is already in a RESONANCE_LOCKED orbit. A field perturbation
drops ρ(Φ) below ρ_res_floor. FM-004 triggers. Field recovers; lock is
re-asserted.

**Initial locked state:**
```
orbit_class     = RESONANT
stab_class      = STABLE
d_bind_res      = 1.200
rho_res_floor   = 0.30
```

**Tick-by-tick ρ(Φ) sequence:**
```
t=10: ρ(Φ) = 0.72  ← RESONANCE_LOCKED  ✓ (0.72 ≥ 0.30)
t=11: ρ(Φ) = 0.48  ← RESONANCE_LOCKED  ✓ (0.48 ≥ 0.30)
t=12: ρ(Φ) = 0.26  ← RLC-4 violated!   ✗ (0.26 < 0.30)
```

**FM-004 trigger at t=12:**
```
state:        RESONANCE_LOCKED → RESONANCE_LOST
orbit_class:  RESONANT         → ELLIPTICAL
stab_class:   STABLE           → MARGINAL
FM-004 raised (recoverable warning)
d_bind_res    retained (binding depth does not vanish — orbit continues as ELLIPTICAL)
```

**Recovery sequence:**
```
t=13: ρ(Φ) = 0.28  ← still below floor  (RESONANCE_LOST, MARGINAL)
t=14: ρ(Φ) = 0.35  ← above floor        ← RLC-4 re-satisfied
```

**Re-lock at t=14:**
```
state:        RESONANCE_LOST → RESONANCE_LOCKED
orbit_class:  ELLIPTICAL     → RESONANT
stab_class:   MARGINAL       → STABLE
FM-004 cleared
```

**Observation:** FM-004 (resonance drift) is the sole recoverable degradation
for RESONANT orbits. Unlike FM-005 (decay spiral, fatal) or FM-007 (mutual
dissolution, fatal), FM-004 preserves the orbit as ELLIPTICAL during drift
and allows full restoration. The orbit never enters a terminal state unless
ρ(Φ) drops to 0, which escalates to FM-002.

---

### Example 4 — Phantom Resonance (FM-006) on Degenerate Eccentricity

**Scenario:** E arrives in-window with β = 1.2 and ρ(Φ) = 0.6, but has
reached maximum eccentricity (e = 1.0) due to a prior failed capture that
left it in a radial fall trajectory. PRIM:033 passes; PRIM:034 raises FM-006.

**PRIM:033 evaluation:**
```
omega_res       = π/3
phi_open        = π/4    (≈ 0.785 rad)
phi_close       = 3π/4   (≈ 2.356 rad)
t_arrive        = 4.5
phi_E           = (π/3 × 4.5) mod 2π = 1.5π mod 2π = (4.712) — MISS?
```

Let us use t_arrive = 1.5:
```
phi_E           = (π/3 × 1.5) mod 2π = π/2 ≈ 1.571 rad
RLC-1: 0.785 ≤ 1.571 ≤ 2.356  ✓  — WINDOW_OPEN
rho_phi = 0.60   ✓  (RLC-3)
beta    = 1.20   ✓  (RLC-2)
v_approach = 2.0 < v_escape = 3.5  ✓  (RLC-5)
PRIM:033 → status = WINDOW_OPEN
```

**PRIM:034 evaluation:**
```
eccentricity    = 1.0    ← degenerate radial trajectory
rho_res_gain    = 1.3
rho_eff         = min(1.0, 0.60 × 1.3) = 0.78
d_bind_res      = 1.2 × 0.78 × (1 − 1.0)
                = 1.2 × 0.78 × 0.0
                = 0.000
```

**FM-006 raised:**
```
status          = FM-006
reason          = PHANTOM_RESONANCE
d_bind_res      = 0.000
orbit_class     = not written
stab_class      = not written
```

**Diagnosis and remediation:**
```
Root cause: eccentricity = 1.0 (p_res = 0, P_eff = 0 — radial infall)
            Phase alignment was genuine but force was absent.
Remediation: f_Force.md heading_delta adjustment to give E non-zero
             transverse momentum before next approach attempt.
             Until e < 1.0, resonant capture is structurally impossible.
```

**Observation:** FM-006 is the rarest failure mode in this file. It requires
the improbable combination of correct phase alignment AND degenerate orbital
geometry. It is not a retry-able condition without structural correction —
the caller must address e before re-attempting.

---

## §9 Cross-Module References

| Reference              | Symbol used                    | Direction  |
|------------------------|--------------------------------|------------|
| f_Capture.md           | β, ρ(Φ), v_approach, v_escape, r_capture, d_bind base formula | Parent |
| f_Orbit.md             | orbit_class = RESONANT, T_orb, stab_class, classify_orbit (PRIM:007) | Peer |
| f_Field.md             | ρ(Φ) oscillation model, field source | Parent |
| f_Force.md             | v_escape(A), heading_delta     | Parent     |
| f_Source.md            | ω_res, T_res, φ_open, φ_close, ρ_res_gain, ρ_res_floor, max_orbits | Read-only (INV-007) |
| f_Decay.md             | d_warn, d_collapse monitoring for RESONANT orbits post-lock | Downstream |
| f_Dampen.md            | ρ(Φ) floor enforcement; cascade guard relevant if resonance chain | Downstream |
| f_Capture_Cascade.md   | Ω_cascade — resonant capture can be a cascade step | Peer |
| OPERATORS.md           | Symbol authority for all operators in §4 | Authority (INV-009) |

---

## §10 Operator Integration Notes

### 10.1 OPERATORS.md Registration Block

The following symbols are added to OPERATORS.md upon this file's ratification:

```
| ω_res          | Angular resonance frequency       | ℝ, > 0       | f_Capture_Resonant.md §4.1 |
| T_res          | Resonance period (2π / ω_res)    | ℝ, > 0       | f_Capture_Resonant.md §4.1 |
| φ_A(t)         | Current phase of A at time t     | [0, 2π)      | f_Capture_Resonant.md §4.1 |
| φ_E            | Arrival phase of E               | [0, 2π)      | f_Capture_Resonant.md §4.1 |
| φ_open         | Window open phase boundary       | [0, 2π)      | f_Capture_Resonant.md §4.1 |
| φ_close        | Window close phase boundary      | (0, 2π]      | f_Capture_Resonant.md §4.1 |
| window_width   | φ_close − φ_open                 | (0, 2π]      | f_Capture_Resonant.md §4.1 |
| t_arrive       | Clock tick at E reaching r_cap   | ℝ, ≥ 0       | f_Capture_Resonant.md §4.1 |
| t_next_open    | Earliest future WINDOW_OPEN tick | ℝ, > t_arrive| f_Capture_Resonant.md §4.1 |
| ρ_res_gain     | Field amplification in window    | ℝ, > 1.0     | f_Capture_Resonant.md §4.2 |
| ρ_eff          | min(1.0, ρ(Φ) × ρ_res_gain)     | [0, 1]       | f_Capture_Resonant.md §4.2 |
| ρ_res_floor    | Minimum ρ(Φ) for lock maintenance| (0, 1)       | f_Capture_Resonant.md §4.2 |
| d_bind_res     | Resonance-enhanced binding depth | ℝ, ≥ 0       | f_Capture_Resonant.md §4.3 |
| T_orb_res      | Pinned orbital period (p/q×T_res)| ℝ, > 0       | f_Capture_Resonant.md §4.3 |
| p_ratio        | Numerator of resonance ratio p:q | ℤ⁺           | f_Capture_Resonant.md §4.3 |
| q_ratio        | Denominator of resonance ratio   | ℤ⁺           | f_Capture_Resonant.md §4.3 |
```

### 10.2 f_Source.md Fields Required

Per INV-007 (f_Source.md read-only), the following fields must be set at
source initialization and never modified by this file:

```
omega_res       : float    — registered by source author at A creation
phi_open        : float    — window geometry, source-specific
phi_close       : float    — window geometry, source-specific
rho_res_gain    : float    — amplification factor, source-specific
rho_res_floor   : float    — lock maintenance floor, default 0.30
p_ratio         : int      — resonance ratio numerator
q_ratio         : int      — resonance ratio denominator
```

### 10.3 Condition Prefix Uniqueness

`RLC-` (Resonance Lock Condition) is unique to this file. No other Wave 4
file uses this prefix. Full prefix registry across Wave 4:

```
MC-    f_Capture_Multi.md
CAS-   f_Capture_Cascade.md
SCS-   f_Capture_Soft.md
HLC-   f_Capture_Hard.md
RLC-   f_Capture_Resonant.md    ← this file
       f_Capture_Asymmetric.md  (prefix: AC-, to be assigned)
```

---

## §11 Document Metadata

### 11.1 INV Compliance Table

| Invariant | Description (abbreviated)              | Status in this file               |
|-----------|----------------------------------------|-----------------------------------|
| INV-001   | G = F_freq · F_fluid · F_force         | ✅ All three nodes in §3          |
| INV-002   | f_Capture → Ω frozen                   | ✅ RESONANCE_LOCKED freezes Ω     |
| INV-003   | ρ(Φ) = 0 → FM-002                      | ✅ RLC-3 + PRIM:033 step 2        |
| INV-004   | β < 1.0 → flyby                        | ✅ RLC-2 + PRIM:033 step 3        |
| INV-005   | Conditions conjunctive                 | ✅ RLC-1–5 all required           |
| INV-006   | Terminal states irreversible           | ✅ FM-006 terminal; LOCKED→LOST reversible only via FM-004 |
| INV-007   | f_Source.md read-only                  | ✅ §10.2 lists read-only fields   |
| INV-008   | Evaluation order normative             | ✅ PRIM:033 docstring + §5 table  |
| INV-009   | OPERATORS.md is symbol authority       | ✅ §10.1 registration block       |
| INV-010   | Frozen symbols unrenameable            | ✅ No renames; new symbols only   |

### 11.2 Primitive Registry (this file)

| PRIM  | Name                    | Type   | Pure? | Description                              |
|-------|-------------------------|--------|-------|------------------------------------------|
| 033   | eval_resonance_window   | Guard  | Yes   | Phase-gate check; returns WINDOW_OPEN/CLOSED or FM code |
| 034   | lock_resonance          | Writer | No    | Computes ρ_eff, d_bind_res, T_orb_res; writes RESONANCE_LOCKED state |

Running total after this file: **PRIM:034**

### 11.3 Failure Mode Summary (this file)

| FM    | Trigger in this file              | Fatal? | Sub-annotation             |
|-------|-----------------------------------|--------|----------------------------|
| FM-001| RLC-1, RLC-2, or RLC-5 violated  | No     | WINDOW_MISS / APPROACH_REJECTION / OVERSHOOT |
| FM-002| RLC-3 violated (ρ(Φ) = 0)        | Yes    | FIELD_NULL                 |
| FM-003| max_orbits ceiling reached        | Yes    | FRAME_SATURATION (VARIANT=RESONANT) |
| FM-004| RLC-4 violated post-capture       | No     | RESONANCE_DRIFT (recoverable) |
| FM-006| d_bind_res = 0 despite RLC pass  | Yes    | PHANTOM_RESONANCE          |

### 11.4 State Flag Registry

| Flag               | Set by      | Cleared by         | Meaning                             |
|--------------------|-------------|--------------------|-------------------------------------|
| WINDOW_OPEN        | PRIM:033    | next tick          | E's arrival phase is in window      |
| WINDOW_CLOSED      | PRIM:033    | next tick          | E's arrival phase is out of window  |
| RESONANCE_LOCKED   | PRIM:034    | FM-004 trigger     | Orbit is actively phase-locked      |
| RESONANCE_LOST     | FM-004      | ρ(Φ) recovery      | Lock broken; orbit downgraded       |

### 11.5 Wave 4 Status Tracker

| File                    | Status     | PRIM range |
|-------------------------|------------|------------|
| f_Capture_Multi.md      | ✅ Complete | 025–026   |
| f_Capture_Cascade.md    | ✅ Complete | 027–028   |
| f_Capture_Soft.md       | ✅ Complete | 029–030   |
| f_Capture_Hard.md       | ✅ Complete | 031–032   |
| f_Capture_Resonant.md   | ✅ Complete | 033–034   |
| f_Capture_Asymmetric.md | ⏳ Pending  | 035–036   |

Wave 4 is **5/6 complete.**

### 11.6 Changelog

```
## [1.0.0] — 2026-08-13
### Added
- Initial canonical release of f_Capture_Resonant.md
- PRIM:033 (eval_resonance_window): phase-gate guard with FM-001/002/003 routing
- PRIM:034 (lock_resonance): resonance-enhanced d_bind_res writer
- RLC-1 through RLC-5 conditions (conjunctive, INV-005 compliant)
- ω_res, T_res, φ_open, φ_close, φ_E, t_next_open operator family
- ρ_res_gain, ρ_eff, ρ_res_floor field enhancement family
- d_bind_res, T_orb_res, p_ratio, q_ratio binding/period family
- WINDOW_OPEN/WINDOW_CLOSED/RESONANCE_LOCKED/RESONANCE_LOST state flags
- FM-004 drift/recovery cycle for post-capture maintenance (RLC-4)
- FM-006 phantom resonance guard on degenerate eccentricity
- Four canonical examples: clean lock (2:1), window miss with retry,
  FM-004 drift + recovery, FM-006 phantom resonance
- Full INV-001–010 compliance table
- OPERATORS.md registration block for all 14 new symbols
```

### 11.7 Suggested Commit Message

```
feat(FFF_Gravity): add f_Capture_Resonant.md — PRIM:033–034, Wave 4 file 5/6

Introduces resonance-locked capture variant for orbit_class=RESONANT.
Defines ω_res-gated capture windows (RLC-1), resonance gain (ρ_res_gain,
ρ_eff), enhanced binding depth (d_bind_res), and orbital period pinning
(T_orb_res = p/q × T_res). PRIM:033 evaluates phase gate with FM-001/002/003
routing and t_next_open retry computation. PRIM:034 writes RESONANCE_LOCKED
state with stab_class=STABLE forcing. FM-004 drift/recovery cycle defined
for post-capture ρ(Φ) maintenance (RLC-4). FM-006 phantom resonance guard
added for degenerate eccentricity case. Wave 4 now 5/6 complete; running
primitive total: PRIM:034.
```

---

*f_Capture_Resonant.md — FFF_Gravity v1.0.0 — Session SES-20260813-FGRAV-033*
*Wave 4 file 5/6 — PRIM:033–034 — 2026-08-13*
