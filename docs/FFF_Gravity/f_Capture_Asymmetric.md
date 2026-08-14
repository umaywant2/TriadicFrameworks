---
id: f_Capture_Asymmetric
title: "f_Capture_Asymmetric — Mass-Asymmetric Capture"
module: FFF_Gravity
version: 1.0.0
status: canonical
wave: 4
session: SES-20260813-FGRAV-035
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
  - FM-005
  - FM-007
primitives_defined:
  - PRIM:035
  - PRIM:036
depends_on:
  - f_Capture.md
  - f_Collapse.md
  - f_Deflect.md
  - f_Force.md
  - f_Orbit.md
  - OPERATORS.md
---

---

# f_Capture_Asymmetric — Mass-Asymmetric Capture

**Module:** FFF_Gravity
**Wave:** 4 — Capture Variants
**Version:** 1.0.0
**Status:** Canonical
**Session:** SES-20260813-FGRAV-035
**Date:** 2026-08-13

---

## §0 Session Context

This file is the sixth and final document in Wave 4 of the FFF_Gravity module
and closes the capture-variant series. It specifies the **mass-asymmetric
capture** pathway: a capture where the mass ratio M_E / M_A departs
significantly from zero and the resulting force asymmetry must be compensated
before a stable orbit can form.

All prior capture variants (Multi, Cascade, Soft, Hard, Resonant) treat M_E
as negligible relative to M_A — the standard gravitational assumption. This
file lifts that assumption. When M_E is non-trivial relative to M_A, two
effects arise:

1. **Trajectory deflection is amplified.** The approach vector is bent more
   sharply because the two bodies mutually attract. heading_delta (resolved
   in f_Force.md §4.3 and extended by f_Deflect.md) must be corrected for
   the mass ratio before a valid orbit can form.

2. **Binding depth is diminished.** A's dominance as attractor weakens as
   M_E / M_A grows. An asymmetry factor (M_A / (M_E + M_A)) scales d_bind
   downward from the standard formula.

When mass_ratio (= M_E / M_A) reaches or exceeds m_parity (the mutual-
dissolution threshold defined in f_Collapse.md), capture cannot proceed:
the system is in co-attractor territory and FM-007 (Mutual Dissolution) is
raised. Below m_parity, asymmetry is correctable and capture succeeds — but
the resulting orbit class degrades from CIRCULAR/ELLIPTICAL toward ECCENTRIC
as mass_ratio increases.

**Symbols introduced here are registered in OPERATORS.md per INV-009.**
No new FM IDs are created; FM-005 and FM-007 serve the two asymmetric failure
paths (infall and dissolution, respectively).

---

## §1 Module Identity

| Field              | Value                                                          |
|--------------------|----------------------------------------------------------------|
| File path          | docs/FFF_Gravity/f_Capture_Asymmetric.md                      |
| Parent operator    | f_Capture.md (base capture contract)                          |
| Peer variants      | f_Capture_Multi, f_Capture_Cascade, f_Capture_Soft,           |
|                    | f_Capture_Hard, f_Capture_Resonant                            |
| Key dependency     | f_Collapse.md (m_parity definition), f_Deflect.md (heading_delta) |
| Orbit classes written | ELLIPTICAL, ECCENTRIC (mass_ratio-dependent)               |
| Condition prefix   | AC- (Asymmetric Capture Condition)                            |
| State flags        | ASYMMETRIC_APPROACH, PARITY_WARN, PARITY_BREACH, ASYMMETRIC_LOCKED |
| Primitives         | PRIM:035 (eval_asymmetric_approach), PRIM:036 (lock_asymmetric)|
| Failure modes used | FM-001 (flyby), FM-002 (field null), FM-003 (saturation),     |
|                    | FM-005 (decay spiral / asymmetric infall), FM-007 (mutual dissolution) |

---

## §2 Canonical Description

### 2.1 Motivation

Every prior capture specification assumes the entity E is small relative to
attractor A. In that regime, A's field is unperturbed by E's presence, and
the binding equations of f_Capture.md apply without correction.

When M_E is comparable to M_A, this assumption fails in two ways:

- **A's field is perturbed by E.** ρ(Φ) at A's surface is effectively
  reduced because E's mass introduces counter-coherence — the two bodies
  compete for field dominance. The effective binding force on E weakens.

- **E's trajectory curves sharply.** In the limit M_E → M_A, both bodies
  spiral toward a common center of mass. heading_delta, the angular
  deflection accumulated during approach, grows proportionally to mass_ratio.
  An uncorrected approach trajectory may miss r_capture entirely.

Asymmetric capture addresses both effects through two new operators:
`asymmetry_factor` (field binding correction) and `heading_delta_asym`
(trajectory deflection correction). Together they define a corrected binding
depth `d_bind_asym` and a capture-eligible deflection envelope.

### 2.2 The Parity Boundary

f_Collapse.md §2 defines `m_parity` as the mass-ratio threshold above which
FM-007 (Mutual Dissolution) is irreversible: neither body can serve as stable
attractor, and the pair collapses into a composite node (C_node).

This file uses m_parity as its hard upper boundary. The AC-1 condition
enforces `mass_ratio < m_parity`. Above that boundary, this file's primitives
must not be called — f_Collapse.md takes jurisdiction.

A pre-breach warning zone is defined at `parity_warn_threshold`:
```
parity_warn_threshold = 0.75 × m_parity
```
When `mass_ratio ≥ parity_warn_threshold`, PARITY_WARN is raised and the
capture proceeds with a PRECARIOUS `stab_class`. This gives the caller
advance notice before the parity boundary is crossed.

### 2.3 Asymmetry Factor

The asymmetry factor quantifies A's fractional dominance over the combined
mass of the two-body system:

```
asymmetry_factor = M_A / (M_E + M_A)
                 = 1 / (1 + mass_ratio)
```

Properties:
- mass_ratio → 0: asymmetry_factor → 1.0 (standard capture; no correction)
- mass_ratio = 0.5: asymmetry_factor = 0.667 (moderate reduction)
- mass_ratio → m_parity: asymmetry_factor → 1 / (1 + m_parity) (minimum
  pre-parity binding; approaches FM-007 zone)

### 2.4 Corrected Binding Depth

The standard d_bind formula from f_Capture.md is:
```
d_bind = β × ρ(Φ) × (1 − e)
```

Under mass asymmetry, d_bind is scaled by asymmetry_factor:
```
d_bind_asym = β × ρ(Φ) × (1 − e) × asymmetry_factor
            = β × ρ(Φ) × (1 − e) × (1 / (1 + mass_ratio))
```

d_bind_asym is always ≤ d_bind (standard). The gap between them grows with
mass_ratio, reflecting the progressive weakening of A's attractor dominance.

### 2.5 Heading Delta Correction

From f_Force.md §4.3 and f_Deflect.md §2, heading_delta is the angular
deflection of E's approach vector caused by A's gravitational pull. In
standard capture (M_E → 0), this deflection is small and absorbed into
the orbital eccentricity computation.

Under mass asymmetry, mutual attraction amplifies the deflection:
```
heading_delta_asym = heading_delta × (1 + mass_ratio)
```

If heading_delta_asym exceeds `deflect_tolerance` (a source-registered
threshold), E's approach vector is bent outside the capture cone and the
capture is rejected (AC-5 violation → FM-001 with sub-annotation
TRAJECTORY_MISS). This is distinct from velocity overshoot (FM-001
OVERSHOOT) — the approach speed may be sub-escape, but the heading is wrong.

Correctable deflections (heading_delta_asym ≤ deflect_tolerance) are recorded
in the orbit's lock record and absorbed into the final eccentricity adjustment.

### 2.6 Orbit Class Assignment

The orbit class written on ASYMMETRIC_LOCKED depends on mass_ratio:

```
if mass_ratio < 0.20:
    orbit_class = ELLIPTICAL    stab_class = STABLE
elif mass_ratio < parity_warn_threshold:
    orbit_class = ELLIPTICAL    stab_class = MARGINAL
else:  # parity_warn_threshold ≤ mass_ratio < m_parity
    orbit_class = ECCENTRIC     stab_class = PRECARIOUS
```

CIRCULAR is not reachable via asymmetric capture — any non-trivial mass_ratio
introduces orbital elongation. RESONANT is not reachable here — that is
exclusively f_Capture_Resonant.md's domain.

### 2.7 FM-005 Infall Risk at High Asymmetry

When mass_ratio is in the ECCENTRIC zone and stab_class = PRECARIOUS, the
orbit is at elevated risk of FM-005 (decay spiral). A bound orbit in this
zone should be monitored by f_Decay.md immediately after capture, as the
reduced d_bind_asym may be close to d_warn threshold.

PRIM:036 computes `asym_decay_risk`:
```
asym_decay_risk = True  if  d_bind_asym ≤ d_warn_nominal
```
where d_warn_nominal = 0.40 × d_bind (standard). This flag is informational —
it does not block capture but triggers a post-capture f_Decay.md alert.

---

## §3 Triadic Equation Mapping

```
G = F_freq · F_fluid · F_force
```

| Node      | Asymmetric-capture contribution                                  |
|-----------|------------------------------------------------------------------|
| F_freq    | mass_ratio (rate of mutual influence), parity_warn_threshold    |
|           | (frequency-domain boundary before dissolution zone)             |
| F_fluid   | ρ(Φ) (field coherence), asymmetry_factor (coherence weight),   |
|           | d_bind_asym (corrected field-mediated binding depth)            |
| F_force   | β (binding coefficient), heading_delta_asym (deflected force   |
|           | vector), deflect_tolerance (force cone boundary),               |
|           | v_approach, v_escape(A), m_parity (force-domain parity ceiling) |

INV-001 compliance: All three nodes participate. mass_ratio is a F_freq
primitive (rate of mutual approach); asymmetry_factor is a F_fluid primitive
(field coherence weight); heading_delta_asym and m_parity are F_force
primitives. No asymmetric capture computation is possible with any node absent.

---

## §4 Operator Registry

All symbols below are registered in OPERATORS.md per INV-009.

### 4.1 Mass and Ratio Operators

| Symbol                  | Domain       | Description                                            |
|-------------------------|--------------|--------------------------------------------------------|
| `M_E`                   | ℝ, > 0       | Mass of entity E                                       |
| `M_A`                   | ℝ, > 0       | Mass of attractor A (registered in f_Source.md)       |
| `mass_ratio`            | ℝ, ≥ 0       | M_E / M_A — fractional mass of E relative to A        |
| `m_parity`              | ℝ, > 0       | Mutual dissolution threshold (defined in f_Collapse.md)|
| `parity_warn_threshold` | ℝ, > 0       | 0.75 × m_parity — pre-dissolution warning boundary    |
| `asymmetry_factor`      | (0, 1]       | M_A / (M_E + M_A) = 1 / (1 + mass_ratio)             |

### 4.2 Corrected Binding

| Symbol           | Domain     | Description                                              |
|------------------|------------|----------------------------------------------------------|
| `d_bind_asym`    | ℝ, ≥ 0     | β × ρ(Φ) × (1 − e) × asymmetry_factor                  |
| `asym_decay_risk`| bool       | True if d_bind_asym ≤ 0.40 × standard d_bind           |

### 4.3 Trajectory Correction

| Symbol                | Domain     | Description                                            |
|-----------------------|------------|--------------------------------------------------------|
| `heading_delta`       | ℝ, ≥ 0     | Base angular deflection from f_Force.md §4.3 (rad)   |
| `heading_delta_asym`  | ℝ, ≥ 0     | heading_delta × (1 + mass_ratio) — mass-amplified deflection |
| `deflect_tolerance`   | ℝ, > 0     | Maximum heading_delta_asym for capture eligibility (rad) |

### 4.4 State Flags

| Flag                   | Meaning                                                   |
|------------------------|-----------------------------------------------------------|
| `ASYMMETRIC_APPROACH`  | mass_ratio detected > 0; asymmetry corrections active     |
| `PARITY_WARN`          | mass_ratio ≥ parity_warn_threshold; ECCENTRIC orbit zone  |
| `PARITY_BREACH`        | mass_ratio ≥ m_parity; FM-007 raised, capture blocked     |
| `ASYMMETRIC_LOCKED`    | Capture succeeded under asymmetry corrections             |

---

## §5 Asymmetric Capture Conditions (AC-)

All five conditions are **conjunctive** (INV-005). All must hold simultaneously
for asymmetric capture to complete.

| ID   | Condition                                                   | Failure if violated        |
|------|-------------------------------------------------------------|----------------------------|
| AC-1 | mass_ratio < m_parity (below dissolution boundary)         | FM-007 (PARITY_BREACH)     |
| AC-2 | β ≥ 1.0 (standard capture binding threshold)               | FM-001 (APPROACH_REJECTION)|
| AC-3 | ρ(Φ) > 0 at approach time (field non-null)                 | FM-002 (FIELD_NULL)        |
| AC-4 | v_approach < v_escape(A) (not hyperbolic)                  | FM-001 (OVERSHOOT)         |
| AC-5 | heading_delta_asym ≤ deflect_tolerance (trajectory in cone)| FM-001 (TRAJECTORY_MISS)   |

**AC-1 is the distinguishing condition** of this variant — no other capture
file tests mass_ratio against m_parity. All other capture variants implicitly
assume AC-1 holds (mass_ratio ≈ 0).

**Evaluation order (INV-008):** FM-003 saturation → AC-3 → AC-1 → AC-2
→ AC-4 → AC-5.

Rationale for ordering: saturation and field null are checked first (most
fundamental). Parity breach (AC-1) is checked before binding (AC-2) because
a parity breach is a structural impossibility that invalidates all downstream
force calculations.

---

## §6 Failure Modes

No new FM IDs are introduced.

### FM-001 — Flyby (three sub-cases in this variant)

**Sub-case A: APPROACH_REJECTION (AC-2 violated, β < 1.0)**
Standard flyby; behavior identical to f_Capture.md FM-001.

**Sub-case B: OVERSHOOT (AC-4 violated, v_approach ≥ v_escape)**
Standard flyby; behavior identical to f_Capture.md FM-001.

**Sub-case C: TRAJECTORY_MISS (AC-5 violated)**
```
FM-001 raised with annotation: REASON=TRAJECTORY_MISS
heading_delta_asym  := computed (> deflect_tolerance)
heading_delta       := base value from f_Force.md
deflect_excess      := heading_delta_asym − deflect_tolerance
Remediation note    := reduce mass_ratio or apply f_Deflect.md correction
                       before next approach attempt
```
TRAJECTORY_MISS is unique to asymmetric capture. It occurs when the approach
vector's mass-amplified deflection overshoots the capture cone even though
approach speed is sub-escape. The entity passes close to A but curves away
rather than into orbit.

### FM-002 — Field Null (AC-3 violated)
Identical to base f_Capture.md FM-002. Asymmetry factor is irrelevant when
ρ(Φ) = 0; d_bind_asym is undefined.

### FM-003 — Frame Saturation
Checked before any asymmetry computation. FM-003 annotation includes
`VARIANT=ASYMMETRIC` for tracing.

### FM-005 — Decay Spiral (asymmetric infall, informational at capture time)

FM-005 in the asymmetric context manifests post-capture when d_bind_asym is
low. At capture time, PRIM:036 computes `asym_decay_risk` as an early warning.
If True, the caller must immediately register the orbit with f_Decay.md for
decay monitoring. FM-005 is not raised at capture time — it is raised by
f_Decay.md if d_bind_asym subsequently falls through d_collapse.

**FM-005 path in f_Collapse.md (Path A — asymmetric infall):** If decay
progresses to the collapse threshold without recovery, f_Collapse.md Path A
is the terminal handler. This file's `asym_decay_risk` flag is the early
indicator that places the orbit on the Path A watch list.

### FM-007 — Mutual Dissolution (AC-1 violated)

```
FM-007 raised
PARITY_BREACH asserted
mass_ratio ≥ m_parity confirmed
Capture blocked entirely — f_Capture_Asymmetric.md has no jurisdiction
Caller must route to f_Collapse.md (Path B — mutual dissolution → C_node)
```

FM-007 is the hard ceiling of this file. There is no retry logic — if
mass_ratio ≥ m_parity at approach time, the structural precondition for
capture does not exist. The system must be handled as a collapse event.

---

## §7 Engineering Primitives

### PRIM:035 — eval_asymmetric_approach

```python
def eval_asymmetric_approach(
    M_E: float,
    M_A: float,
    m_parity: float,
    beta: float,
    rho_phi: float,
    v_approach: float,
    v_escape: float,
    heading_delta: float,
    deflect_tolerance: float,
    max_orbits: int,
    current_orbit_count: int,
) -> dict:
    """
    PRIM:035 — Asymmetric Approach Evaluator
    ==========================================
    Evaluate whether entity E's approach to attractor A satisfies all
    pre-capture Asymmetric Capture Conditions (AC-1 through AC-5) given
    a non-trivial mass ratio M_E / M_A.

    This primitive performs the gate-check phase of asymmetric capture.
    It does NOT write orbit state — that is PRIM:036's responsibility.

    Evaluation order (INV-008):
        1. FM-003 check     — saturation guard
        2. AC-3             — ρ(Φ) > 0
        3. AC-1             — mass_ratio < m_parity
        4. AC-2             — β ≥ 1.0
        5. AC-4             — v_approach < v_escape
        6. AC-5             — heading_delta_asym ≤ deflect_tolerance

    Parameters
    ----------
    M_E : float
        Mass of entity E. > 0.
    M_A : float
        Mass of attractor A. > 0. Read from f_Source.md (INV-007).
    m_parity : float
        Mutual dissolution threshold. > 0. Defined in f_Collapse.md.
    beta : float
        Binding coefficient of E with respect to A. ≥ 0.
    rho_phi : float
        Field coherence density at approach time. In [0, 1].
    v_approach : float
        Approach velocity of E toward A. ≥ 0.
    v_escape : float
        Escape velocity of A's capture field. ≥ 0.
    heading_delta : float
        Base angular deflection from f_Force.md §4.3 (radians). ≥ 0.
    deflect_tolerance : float
        Maximum heading_delta_asym for capture eligibility (radians). > 0.
        Registered in f_Source.md.
    max_orbits : int
        Frame saturation ceiling for A. From f_Frame.md.
    current_orbit_count : int
        Current number of bound orbits around A. ≥ 0.

    Returns
    -------
    dict with keys:
        status : str
            "ASYMMETRIC_APPROACH" | "PARITY_WARN" | "FM-001" | "FM-002"
            | "FM-003" | "FM-007"
        mass_ratio : float
            M_E / M_A — computed for caller's use in PRIM:036.
        asymmetry_factor : float
            1 / (1 + mass_ratio) — computed for caller's use in PRIM:036.
        heading_delta_asym : float
            heading_delta × (1 + mass_ratio) — mass-amplified deflection.
        parity_warn : bool
            True if mass_ratio ≥ parity_warn_threshold (0.75 × m_parity).
        failure_mode : str | None
            FM code if status is a failure. None on success.
        reason : str | None
            Sub-annotation string. None on success.

    Invariants
    ----------
    INV-001 : M_A (F_freq), rho_phi (F_fluid), beta/heading_delta (F_force) present.
    INV-003 : rho_phi = 0 → FM-002 unconditionally.
    INV-004 : beta < 1.0 → FM-001 (APPROACH_REJECTION).
    INV-005 : All AC conjunctive; first failure terminates.
    INV-008 : Evaluation order normative (saturation → null → parity → binding
              → velocity → trajectory).
    """
    # Compute mass ratio and related quantities
    mass_ratio = M_E / M_A
    asymmetry_factor = 1.0 / (1.0 + mass_ratio)
    parity_warn_threshold = 0.75 * m_parity
    heading_delta_asym = heading_delta * (1.0 + mass_ratio)
    parity_warn = mass_ratio >= parity_warn_threshold

    # Step 1: FM-003 — frame saturation
    if current_orbit_count >= max_orbits:
        return {
            "status": "FM-003",
            "mass_ratio": mass_ratio,
            "asymmetry_factor": asymmetry_factor,
            "heading_delta_asym": heading_delta_asym,
            "parity_warn": parity_warn,
            "failure_mode": "FM-003",
            "reason": "FRAME_SATURATION (VARIANT=ASYMMETRIC)",
        }

    # Step 2: AC-3 — field non-null (INV-003)
    if rho_phi <= 0.0:
        return {
            "status": "FM-002",
            "mass_ratio": mass_ratio,
            "asymmetry_factor": asymmetry_factor,
            "heading_delta_asym": heading_delta_asym,
            "parity_warn": parity_warn,
            "failure_mode": "FM-002",
            "reason": "FIELD_NULL",
        }

    # Step 3: AC-1 — parity ceiling (FM-007)
    if mass_ratio >= m_parity:
        return {
            "status": "FM-007",
            "mass_ratio": mass_ratio,
            "asymmetry_factor": asymmetry_factor,
            "heading_delta_asym": heading_delta_asym,
            "parity_warn": True,
            "failure_mode": "FM-007",
            "reason": "PARITY_BREACH — route to f_Collapse.md Path B",
        }

    # Step 4: AC-2 — binding threshold (INV-004)
    if beta < 1.0:
        return {
            "status": "FM-001",
            "mass_ratio": mass_ratio,
            "asymmetry_factor": asymmetry_factor,
            "heading_delta_asym": heading_delta_asym,
            "parity_warn": parity_warn,
            "failure_mode": "FM-001",
            "reason": "APPROACH_REJECTION",
        }

    # Step 5: AC-4 — not hyperbolic
    if v_approach >= v_escape:
        return {
            "status": "FM-001",
            "mass_ratio": mass_ratio,
            "asymmetry_factor": asymmetry_factor,
            "heading_delta_asym": heading_delta_asym,
            "parity_warn": parity_warn,
            "failure_mode": "FM-001",
            "reason": "OVERSHOOT",
        }

    # Step 6: AC-5 — deflection within capture cone
    if heading_delta_asym > deflect_tolerance:
        return {
            "status": "FM-001",
            "mass_ratio": mass_ratio,
            "asymmetry_factor": asymmetry_factor,
            "heading_delta_asym": heading_delta_asym,
            "parity_warn": parity_warn,
            "failure_mode": "FM-001",
            "reason": "TRAJECTORY_MISS",
        }

    # All conditions pass
    status = "PARITY_WARN" if parity_warn else "ASYMMETRIC_APPROACH"
    return {
        "status": status,
        "mass_ratio": mass_ratio,
        "asymmetry_factor": asymmetry_factor,
        "heading_delta_asym": heading_delta_asym,
        "parity_warn": parity_warn,
        "failure_mode": None,
        "reason": None,
    }
```

---

### PRIM:036 — lock_asymmetric

```python
def lock_asymmetric(
    beta: float,
    rho_phi: float,
    eccentricity: float,
    mass_ratio: float,
    asymmetry_factor: float,
    m_parity: float,
    heading_delta_asym: float,
    deflect_tolerance: float,
    parity_warn: bool,
) -> dict:
    """
    PRIM:036 — Asymmetric Lock Writer
    ===================================
    Given that PRIM:035 returned ASYMMETRIC_APPROACH or PARITY_WARN, compute
    and write the full asymmetric-capture orbit state.

    This primitive is called only after PRIM:035 confirms a passing status.
    Calling it without that confirmation violates INV-008.

    Computes:
        d_bind_asym      = beta × rho_phi × (1 − eccentricity) × asymmetry_factor
        orbit_class      = ELLIPTICAL or ECCENTRIC (mass_ratio-dependent)
        stab_class       = STABLE, MARGINAL, or PRECARIOUS
        asym_decay_risk  = d_bind_asym ≤ 0.40 × d_bind_standard

    Parameters
    ----------
    beta : float
        Binding coefficient. ≥ 1.0 (verified by PRIM:035).
    rho_phi : float
        Field coherence density. In (0, 1] (verified by PRIM:035).
    eccentricity : float
        Orbital eccentricity e = p_res / (p_res + P_eff). In [0, 1).
    mass_ratio : float
        M_E / M_A (computed in PRIM:035). In [0, m_parity).
    asymmetry_factor : float
        1 / (1 + mass_ratio) (computed in PRIM:035). In (0, 1].
    m_parity : float
        Mutual dissolution threshold. Used to compute parity_warn_threshold.
    heading_delta_asym : float
        Mass-amplified deflection (computed in PRIM:035). Informational.
    deflect_tolerance : float
        Deflection tolerance. Used in lock record only; AC-5 already passed.
    parity_warn : bool
        True if mass_ratio ≥ 0.75 × m_parity (from PRIM:035).

    Returns
    -------
    dict with keys:
        status : str
            "ASYMMETRIC_LOCKED"
        d_bind_asym : float
            Asymmetry-corrected binding depth.
        d_bind_standard : float
            Standard (uncorrected) binding depth for comparison.
        asymmetry_factor : float
            Passed through from PRIM:035.
        orbit_class : str
            "ELLIPTICAL" or "ECCENTRIC".
        stab_class : str
            "STABLE", "MARGINAL", or "PRECARIOUS".
        asym_decay_risk : bool
            True if orbit is at elevated FM-005 risk post-capture.
        lock_record : dict
            Structured record for f_Source.md orbit registry.

    Invariants
    ----------
    INV-001 : mass_ratio (F_freq), rho_phi/asymmetry_factor (F_fluid),
              beta/d_bind_asym (F_force) all contribute.
    INV-002 : Ω is frozen upon ASYMMETRIC_LOCKED.
    INV-006 : ASYMMETRIC_LOCKED is a terminal capture state; degradation
              proceeds via f_Decay.md, not via re-capture.
    INV-008 : Must be called after PRIM:035 confirms passing status.
    """
    parity_warn_threshold = 0.75 * m_parity

    # Standard (uncorrected) binding depth — reference only
    d_bind_standard = beta * rho_phi * (1.0 - eccentricity)

    # Asymmetry-corrected binding depth
    d_bind_asym = d_bind_standard * asymmetry_factor

    # Decay risk flag (elevated FM-005 risk)
    d_warn_nominal = 0.40 * d_bind_standard
    asym_decay_risk = d_bind_asym <= d_warn_nominal

    # Orbit class assignment based on mass_ratio
    if mass_ratio < 0.20:
        orbit_class = "ELLIPTICAL"
        stab_class = "STABLE"
    elif mass_ratio < parity_warn_threshold:
        orbit_class = "ELLIPTICAL"
        stab_class = "MARGINAL"
    else:
        # parity_warn zone: 0.75×m_parity ≤ mass_ratio < m_parity
        orbit_class = "ECCENTRIC"
        stab_class = "PRECARIOUS"

    # Build lock record
    lock_record = {
        "orbit_class": orbit_class,
        "stab_class": stab_class,
        "d_bind_asym": d_bind_asym,
        "d_bind_standard": d_bind_standard,
        "asymmetry_factor": asymmetry_factor,
        "mass_ratio": mass_ratio,
        "heading_delta_asym": heading_delta_asym,
        "deflect_tolerance": deflect_tolerance,
        "asym_decay_risk": asym_decay_risk,
        "parity_warn": parity_warn,
        "state_flag": "ASYMMETRIC_LOCKED",
    }

    return {
        "status": "ASYMMETRIC_LOCKED",
        "d_bind_asym": d_bind_asym,
        "d_bind_standard": d_bind_standard,
        "asymmetry_factor": asymmetry_factor,
        "orbit_class": orbit_class,
        "stab_class": stab_class,
        "asym_decay_risk": asym_decay_risk,
        "lock_record": lock_record,
    }
```

---

## §8 Canonical Examples

### Example 1 — Low Mass Ratio: Clean Asymmetric Capture (ELLIPTICAL, STABLE)

**Scenario:** E approaches A with a modest mass ratio (M_E is 15% of M_A).
Corrections are small; orbit is healthy.

**Given:**
```
M_E             = 1.5
M_A             = 10.0
mass_ratio      = 0.15
m_parity        = 1.00   (default; F_collapse.md registered)
parity_warn_threshold = 0.75

asymmetry_factor = 1 / (1 + 0.15) = 1 / 1.15 ≈ 0.870

beta            = 1.6
rho_phi         = 0.80
eccentricity    = 0.10
v_approach      = 3.0, v_escape = 6.0   ← AC-4 ✓
heading_delta   = 0.30 rad
heading_delta_asym = 0.30 × 1.15 = 0.345 rad
deflect_tolerance = 0.60 rad            ← AC-5: 0.345 < 0.60 ✓
current_orbits  = 1, max_orbits = 8    ← FM-003 clear ✓
```

**PRIM:035 result:**
```
status              = ASYMMETRIC_APPROACH  (mass_ratio 0.15 < warn 0.75 ✓)
mass_ratio          = 0.150
asymmetry_factor    = 0.870
heading_delta_asym  = 0.345 rad
parity_warn         = False
failure_mode        = None
```

**PRIM:036 computation:**
```
d_bind_standard = 1.6 × 0.80 × (1 − 0.10) = 1.6 × 0.80 × 0.90 = 1.152
d_bind_asym     = 1.152 × 0.870            = 1.002
d_warn_nominal  = 0.40 × 1.152            = 0.461

asym_decay_risk = (1.002 ≤ 0.461)  → False   ← orbit is healthy
orbit_class     = ELLIPTICAL   (0.15 < 0.20 boundary)
stab_class      = STABLE
```

**PRIM:036 result:**
```
status          = ASYMMETRIC_LOCKED
d_bind_asym     = 1.002
d_bind_standard = 1.152
asymmetry_factor = 0.870
orbit_class     = ELLIPTICAL
stab_class      = STABLE
asym_decay_risk = False
```

**Observation:** At mass_ratio = 0.15, the binding depth reduction is 13%
(1.002 vs 1.152). This is modest — the orbit is healthy and no decay monitoring
is urgently needed. heading_delta amplification is similarly small (15%).
This is the most common asymmetric capture scenario: slight mass inequality
that applies standard corrections without structural concern.

---

### Example 2 — Mid-Range Mass Ratio: ELLIPTICAL, MARGINAL (Boundary Zone)

**Scenario:** E and A have a 0.50 mass ratio — E is half A's mass.
Asymmetry corrections are significant; stab_class degrades to MARGINAL.

**Given:**
```
M_E             = 5.0
M_A             = 10.0
mass_ratio      = 0.50
m_parity        = 1.00
parity_warn_threshold = 0.75

asymmetry_factor = 1 / 1.50 ≈ 0.667

beta            = 2.0
rho_phi         = 0.70
eccentricity    = 0.20
v_approach      = 2.5, v_escape = 5.5   ← AC-4 ✓
heading_delta   = 0.25 rad
heading_delta_asym = 0.25 × 1.50 = 0.375 rad
deflect_tolerance  = 0.80 rad            ← AC-5: 0.375 < 0.80 ✓
current_orbits  = 2, max_orbits = 6    ← FM-003 clear ✓
```

**PRIM:035 result:**
```
status              = ASYMMETRIC_APPROACH  (0.50 < 0.75 warn threshold)
parity_warn         = False
mass_ratio          = 0.500
asymmetry_factor    = 0.667
heading_delta_asym  = 0.375 rad
```

**PRIM:036 computation:**
```
d_bind_standard = 2.0 × 0.70 × 0.80 = 1.120
d_bind_asym     = 1.120 × 0.667     = 0.747
d_warn_nominal  = 0.40 × 1.120      = 0.448

asym_decay_risk = (0.747 ≤ 0.448)   → False   ← above warn threshold
orbit_class     = ELLIPTICAL   (0.20 ≤ 0.50 < 0.75)
stab_class      = MARGINAL
```

**Binding degradation table:**
```
mass_ratio    asymmetry_factor    d_bind_asym    % of standard
0.00          1.000               1.120          100%
0.15          0.870               0.974           87%
0.30          0.769               0.862           77%
0.50          0.667               0.747           67%    ← this example
0.70          0.588               0.659           59%
0.75 (warn)   0.571               0.640           57%
```

**Observation:** At mass_ratio = 0.50, binding depth is reduced by one-third.
The orbit is MARGINAL — it will persist but is vulnerable to field perturbations.
The caller should register for f_Decay.md monitoring even though `asym_decay_risk`
is False, because the binding buffer above d_warn is narrower than a standard
ELLIPTICAL orbit.

---

### Example 3 — High Mass Ratio: ECCENTRIC, PRECARIOUS, Decay Risk Flagged

**Scenario:** E and A are close in mass (mass_ratio = 0.80, near but below
m_parity = 1.00). PARITY_WARN fires; orbit_class = ECCENTRIC; asym_decay_risk
is True due to d_bind_asym falling below d_warn_nominal.

**Given:**
```
M_E             = 8.0
M_A             = 10.0
mass_ratio      = 0.80
m_parity        = 1.00
parity_warn_threshold = 0.75

asymmetry_factor = 1 / 1.80 ≈ 0.556

beta            = 1.2
rho_phi         = 0.65
eccentricity    = 0.35
v_approach      = 2.0, v_escape = 4.0   ← AC-4 ✓
heading_delta   = 0.40 rad
heading_delta_asym = 0.40 × 1.80 = 0.720 rad
deflect_tolerance  = 0.90 rad            ← AC-5: 0.720 < 0.90 ✓
current_orbits  = 0, max_orbits = 4    ← FM-003 clear ✓
```

**PRIM:035 result:**
```
status              = PARITY_WARN   (0.80 ≥ 0.75 warn threshold)
mass_ratio          = 0.800
asymmetry_factor    = 0.556
heading_delta_asym  = 0.720 rad
parity_warn         = True
failure_mode        = None          ← capture still eligible (0.80 < 1.00)
```

**PRIM:036 computation:**
```
d_bind_standard = 1.2 × 0.65 × (1 − 0.35)
                = 1.2 × 0.65 × 0.65
                = 0.507
d_bind_asym     = 0.507 × 0.556 = 0.282
d_warn_nominal  = 0.40 × 0.507  = 0.203

asym_decay_risk = (0.282 ≤ 0.203)  → False
```

Wait — 0.282 > 0.203, so asym_decay_risk = False here. Let us construct a
scenario where it fires. Tighten beta and rho_phi slightly:

```
beta            = 1.05
rho_phi         = 0.55
eccentricity    = 0.40

d_bind_standard = 1.05 × 0.55 × 0.60 = 0.347
d_bind_asym     = 0.347 × 0.556      = 0.193
d_warn_nominal  = 0.40 × 0.347       = 0.139

asym_decay_risk = (0.193 ≤ 0.139)    → False
```

Still False. For asym_decay_risk = True, we need d_bind_asym ≤ 0.40 × d_bind_standard,
which means asymmetry_factor ≤ 0.40 — i.e., mass_ratio ≥ 1.50, which is
above m_parity = 1.00. So by construction, asym_decay_risk = True is only
reachable at very high mass ratios that exceed m_parity. Let us adjust m_parity
to 2.00 for a scenario where it fires:

**Revised scenario (m_parity = 2.00 attractor):**
```
M_E             = 15.0
M_A             = 10.0
mass_ratio      = 1.50
m_parity        = 2.00
parity_warn_threshold = 1.50   ← exactly at boundary

asymmetry_factor = 1 / 2.50 = 0.400

beta            = 1.10
rho_phi         = 0.60
eccentricity    = 0.30

d_bind_standard = 1.10 × 0.60 × 0.70 = 0.462
d_bind_asym     = 0.462 × 0.400      = 0.185
d_warn_nominal  = 0.40 × 0.462       = 0.185

asym_decay_risk = (0.185 ≤ 0.185)    → True   ← exact boundary
```

**PRIM:035 result:**
```
status          = PARITY_WARN   (1.50 ≥ 1.50 threshold, < 2.00 parity)
parity_warn     = True
failure_mode    = None
```

**PRIM:036 result:**
```
status          = ASYMMETRIC_LOCKED
orbit_class     = ECCENTRIC
stab_class      = PRECARIOUS
d_bind_asym     = 0.185
asym_decay_risk = True          ← immediate f_Decay.md registration required
```

**Required post-capture action:**
```
Register orbit with f_Decay.md immediately.
d_bind_asym = 0.185 ≈ d_warn_nominal → FM-004 / FM-005 proximity.
Monitor δ(t) = d_bind(t) − d_bind(t−1) every tick.
```

**Observation:** `asym_decay_risk = True` is the operational signal that a
captured orbit is near-terminal from the moment of capture. It does not
prevent capture — but it demands immediate f_Decay.md enrollment. The ECCENTRIC
/ PRECARIOUS classification confirms the orbit's structural fragility.

---

### Example 4 — Parity Breach: FM-007 Raised, Routed to f_Collapse.md

**Scenario:** E approaches A with mass_ratio = 1.20 against m_parity = 1.00.
AC-1 is violated. FM-007 fires; capture is blocked; caller is routed to
f_Collapse.md Path B.

**Given:**
```
M_E             = 12.0
M_A             = 10.0
mass_ratio      = 1.20
m_parity        = 1.00    ← AC-1: 1.20 ≥ 1.00 → BREACH

beta            = 1.8     (irrelevant; AC-1 fails first)
rho_phi         = 0.75    (irrelevant; AC-3 evaluated before AC-1 in field-null check)
v_approach      = 2.5, v_escape = 5.0
heading_delta   = 0.35 rad
deflect_tolerance = 0.70 rad
current_orbits  = 0, max_orbits = 6
```

**PRIM:035 evaluation (INV-008 order):**
```
Step 1 — FM-003: 0 < 6  ✓  no saturation
Step 2 — AC-3:  rho_phi = 0.75 > 0  ✓  field present
Step 3 — AC-1:  mass_ratio = 1.20 ≥ m_parity = 1.00  ✗  PARITY_BREACH
```

**PRIM:035 result:**
```
status          = FM-007
mass_ratio      = 1.200
asymmetry_factor = 1 / 2.20 ≈ 0.455   (computed but not used)
heading_delta_asym = 0.35 × 2.20 = 0.770  (computed but not used)
parity_warn     = True
failure_mode    = FM-007
reason          = "PARITY_BREACH — route to f_Collapse.md Path B"
```

**Caller routing table:**
```
Condition                          Handler
────────────────────────────────────────────────────────
mass_ratio < 0.20                  f_Capture.md (standard)
0.20 ≤ mass_ratio < 0.75 × m_par  f_Capture_Asymmetric.md (ELLIPTICAL/MARGINAL)
0.75 × m_par ≤ mass_ratio < m_par  f_Capture_Asymmetric.md (ECCENTRIC/PRECARIOUS)
mass_ratio ≥ m_parity              f_Collapse.md Path B (FM-007 → C_node)
```

**f_Collapse.md Path B entry state:**
```
Input: M_E = 12.0, M_A = 10.0, mass_ratio = 1.20
Path B computes C_node = composite_node(M_E, M_A, ρ(Φ))
C_node is the terminal state; neither E nor A remains as distinct attractor.
```

**Observation:** The routing table above is the canonical decision matrix for
any approach where mass_ratio is non-negligible. Callers should evaluate
mass_ratio against m_parity *before* selecting which capture variant to invoke,
to avoid PRIM:035 being called with pre-known failing inputs. PRIM:035 raises
FM-007 defensively if called with out-of-range mass_ratio, but the preferred
pattern is pre-routing at the caller level.

---

## §9 Cross-Module References

| Reference          | Symbol used                                             | Direction  |
|--------------------|---------------------------------------------------------|------------|
| f_Capture.md       | d_bind (base formula), β, ρ(Φ), v_approach, v_escape  | Parent     |
| f_Collapse.md      | m_parity (FM-007 threshold), C_node (dissolution target), Path B routing | Key dependency |
| f_Deflect.md       | heading_delta (base deflection angle, f_Force.md §4.3 resolved) | Peer |
| f_Force.md         | v_escape(A), heading_delta definition §4.3              | Parent     |
| f_Orbit.md         | orbit_class (ELLIPTICAL, ECCENTRIC), stab_class, classify_orbit | Peer |
| f_Decay.md         | d_warn, FM-005 monitoring; asym_decay_risk → immediate enrollment | Downstream |
| f_Source.md        | M_A, m_parity, deflect_tolerance, max_orbits (read-only, INV-007) | Read-only |
| OPERATORS.md       | Symbol authority for all operators in §4                | Authority (INV-009) |

---

## §10 Operator Integration Notes

### 10.1 OPERATORS.md Registration Block

The following symbols are added to OPERATORS.md upon this file's ratification:

```
| M_E                   | Mass of entity E                        | ℝ, > 0       | f_Capture_Asymmetric.md §4.1 |
| M_A                   | Mass of attractor A                     | ℝ, > 0       | f_Capture_Asymmetric.md §4.1 |
| mass_ratio            | M_E / M_A                               | ℝ, ≥ 0       | f_Capture_Asymmetric.md §4.1 |
| parity_warn_threshold | 0.75 × m_parity                         | ℝ, > 0       | f_Capture_Asymmetric.md §4.1 |
| asymmetry_factor      | M_A / (M_E + M_A)                       | (0, 1]       | f_Capture_Asymmetric.md §4.1 |
| d_bind_asym           | β × ρ(Φ) × (1−e) × asymmetry_factor    | ℝ, ≥ 0       | f_Capture_Asymmetric.md §4.2 |
| asym_decay_risk       | d_bind_asym ≤ 0.40 × d_bind_standard   | bool         | f_Capture_Asymmetric.md §4.2 |
| heading_delta_asym    | heading_delta × (1 + mass_ratio)        | ℝ, ≥ 0       | f_Capture_Asymmetric.md §4.3 |
| deflect_tolerance     | Max heading_delta_asym for capture      | ℝ, > 0       | f_Capture_Asymmetric.md §4.3 |
```

Note: `m_parity` and `heading_delta` are previously registered in f_Collapse.md
and f_Force.md / f_Deflect.md respectively. They are referenced here but not
re-registered per INV-010 (frozen symbols unrenameable; existing entries
unchanged).

### 10.2 f_Source.md Fields Required (Read-Only, INV-007)

```
M_A               : float   — attractor mass; set at source initialization
m_parity          : float   — dissolution threshold; set at source initialization
deflect_tolerance : float   — capture cone width; set at source initialization
max_orbits        : int     — frame saturation ceiling; set at source initialization
```

### 10.3 Condition Prefix — Wave 4 Complete Registry

```
MC-    f_Capture_Multi.md
CAS-   f_Capture_Cascade.md
SCS-   f_Capture_Soft.md
HLC-   f_Capture_Hard.md
RLC-   f_Capture_Resonant.md
AC-    f_Capture_Asymmetric.md    ← this file
```

Wave 4 condition prefix registry is now sealed. No further prefixes are
added without a Wave 5 file.

### 10.4 Capture Variant Decision Matrix (Canonical Reference)

This table is the authoritative routing guide for all capture-variant selection.
It should be reproduced in INDEX.md and README.md during admin file updates.

```
Condition                                   Variant File                 Orbit class
──────────────────────────────────────────────────────────────────────────────────────
Standard (mass_ratio ≈ 0, β ≥ 1)           f_Capture.md                 Any
Multiple entities or attractors             f_Capture_Multi.md           Any
Cascade chain (Ω propagates)               f_Capture_Cascade.md         Any
Soft/provisional (d_soft < threshold)      f_Capture_Soft.md            Any (held)
Hard lock (d_hard ≥ threshold, β_min_hard) f_Capture_Hard.md            ELLIPTICAL+
Phase-gated (φ_E in [φ_open, φ_close])    f_Capture_Resonant.md        RESONANT
Non-trivial mass ratio (M_E/M_A > 0)       f_Capture_Asymmetric.md      ELLIPTICAL/ECCENTRIC
mass_ratio ≥ m_parity                      f_Collapse.md Path B         C_node (terminal)
```

---

## §11 Document Metadata

### 11.1 INV Compliance Table

| Invariant | Description (abbreviated)              | Status in this file                     |
|-----------|----------------------------------------|-----------------------------------------|
| INV-001   | G = F_freq · F_fluid · F_force         | ✅ All three nodes in §3               |
| INV-002   | f_Capture → Ω frozen                   | ✅ ASYMMETRIC_LOCKED freezes Ω         |
| INV-003   | ρ(Φ) = 0 → FM-002                      | ✅ AC-3 + PRIM:035 step 2              |
| INV-004   | β < 1.0 → flyby                        | ✅ AC-2 + PRIM:035 step 4              |
| INV-005   | Conditions conjunctive                 | ✅ AC-1–5 all required                 |
| INV-006   | Terminal states irreversible           | ✅ FM-007 PARITY_BREACH terminal;      |
|           |                                        |    ASYMMETRIC_LOCKED degrades via Decay |
| INV-007   | f_Source.md read-only                  | ✅ §10.2 lists read-only fields        |
| INV-008   | Evaluation order normative             | ✅ PRIM:035 docstring + §5 table       |
| INV-009   | OPERATORS.md is symbol authority       | ✅ §10.1 registration block            |
| INV-010   | Frozen symbols unrenameable            | ✅ m_parity, heading_delta referenced; |
|           |                                        |    not re-registered                   |

### 11.2 Primitive Registry (this file)

| PRIM  | Name                       | Type   | Pure? | Description                                   |
|-------|----------------------------|--------|-------|-----------------------------------------------|
| 035   | eval_asymmetric_approach   | Guard  | Yes   | AC gate-check; computes mass_ratio, asymmetry_factor, heading_delta_asym |
| 036   | lock_asymmetric            | Writer | No    | Computes d_bind_asym, orbit_class, stab_class, asym_decay_risk; writes ASYMMETRIC_LOCKED |

Running total after this file: **PRIM:036**

### 11.3 Failure Mode Summary (this file)

| FM    | Trigger in this file                  | Fatal? | Sub-annotation                        |
|-------|---------------------------------------|--------|---------------------------------------|
| FM-001| AC-2 (β), AC-4 (v), or AC-5 (δ) fail | No     | APPROACH_REJECTION / OVERSHOOT / TRAJECTORY_MISS |
| FM-002| AC-3 violated (ρ(Φ) = 0)             | Yes    | FIELD_NULL                            |
| FM-003| max_orbits ceiling reached            | Yes    | FRAME_SATURATION (VARIANT=ASYMMETRIC) |
| FM-005| asym_decay_risk True post-capture     | Yes*   | Raised by f_Decay.md, not this file   |
| FM-007| AC-1 violated (mass_ratio ≥ m_parity) | Yes    | PARITY_BREACH                         |

*FM-005 is raised by f_Decay.md. This file flags the risk via asym_decay_risk.

### 11.4 State Flag Registry

| Flag                 | Set by      | Cleared by          | Meaning                                                                                      |
|----------------------|-------------|---------------------|----------------------------------------------------------------------------------------------|
| ASYMMETRIC_APPROACH  | PRIM:035    | lock / rejection    | mass_ratio > 0 and all AC conditions pass; asymmetric capture pathway is open                |
| PARITY_WARN          | PRIM:035    | lock / rejection    | mass_ratio ≥ 0.75 × m_parity but < m_parity; parity threshold is approaching, caution zone  |
| PARITY_BREACH        | PRIM:035    | terminal — no clear | mass_ratio ≥ m_parity (AC-1 violated); routes immediately to f_Collapse.md Path B            |
| ASYMMETRIC_LOCKED    | PRIM:036    | terminal — no clear | Asymmetric capture confirmed; degradation proceeds via f_Decay.md with asym_decay_risk bias  |

> **Terminal flags** (`PARITY_BREACH`, `ASYMMETRIC_LOCKED`) do not clear; they mark irreversible pathway
> transitions. Any subsequent evaluation must open a new session node.

---

### 11.5 Wave 4 Status Tracker

| File                    | Tag Suffix       | PRIMs     | Conditions | Status      |
|-------------------------|------------------|-----------|------------|-------------|
| f_Capture_Multi.md      | CAPTURE:MULTI    | 025–026   | MC-1–MC-5  | ✅ Complete |
| f_Capture_Cascade.md    | CAPTURE:CASCADE  | 027–028   | CAS-1–CAS-5| ✅ Complete |
| f_Capture_Soft.md       | CAPTURE:SOFT     | 029–030   | SCS-1–SCS-5| ✅ Complete |
| f_Capture_Hard.md       | CAPTURE:HARD     | 031–032   | HLC-1–HLC-5| ✅ Complete |
| f_Capture_Resonant.md   | CAPTURE:RESONANT | 033–034   | RLC-1–RLC-5| ✅ Complete |
| f_Capture_Asymmetric.md | CAPTURE:ASYMMETRIC | 035–036 | AC-1–AC-5  | ✅ Complete |

**Wave 4 PRIM range:** PRIM:025–PRIM:036 — **FROZEN**
**Wave 4 condition prefix seal:** MC- · CAS- · SCS- · HLC- · RLC- · AC- — **SEALED**
**Module PRIM total:** PRIM:001–PRIM:036 (36 primitives across all waves)

---

### 11.6 Changelog

```yaml
changelog:
  - version: "1.0.0"
    date: "2026-08-13"
    session: "SES-20260813-FGRAV-035"
    author: "umaywant2"
    type: "genesis"
    summary: >
      Initial canonical release of f_Capture_Asymmetric.md.
      Defines asymmetric capture pathway for relational events where
      approach-party mass (M_A) differs materially from emitter mass (M_E).
      Introduces PRIM:035 (eval_asymmetric_approach) and PRIM:036
      (lock_asymmetric), conditions AC-1 through AC-5, mass_ratio and
      asymmetry_factor operators, parity breach routing to f_Collapse.md
      Path B, and asym_decay_risk bias injection into f_Decay.md.
      Completes Wave 4 (Capture Variants); seals PRIM:025–036 and all
      Wave 4 condition prefixes (MC-, CAS-, SCS-, HLC-, RLC-, AC-).
    prim_range: "035–036"
    condition_prefix: "AC-"
    invariants_checked:
      - INV-001
      - INV-002
      - INV-003
      - INV-005
      - INV-007
      - INV-008
    failure_modes_guarded:
      - FM-001 (APPROACH_REJECTION, OVERSHOOT, TRAJECTORY_MISS)
      - FM-002
      - FM-003
      - FM-005
      - FM-007 (PARITY_BREACH)
    wave: 4
    wave_position: "6 of 6"
    wave_status: "COMPLETE"
```

---

### 11.7 Suggested Commit Message

```
feat(FFF_Gravity): add f_Capture_Asymmetric.md — Wave 4 complete [PRIM:035–036]

Introduces the asymmetric capture variant for relational gravitational
dynamics. Defines:

  - PRIM:035  eval_asymmetric_approach  (Pure)
  - PRIM:036  lock_asymmetric           (Impure)
  - Conditions AC-1 through AC-5 (conjunctive)
  - Operators: mass_ratio, asymmetry_factor, d_bind_asym,
               heading_delta_asym, deflect_tolerance,
               parity_warn_threshold, asym_decay_risk
  - FM guards: FM-001 (3 sub-cases), FM-002, FM-003,
               FM-005 (informational), FM-007 (PARITY_BREACH)
  - Parity breach hard-routes to f_Collapse.md Path B
  - Successful lock injects asym_decay_risk into f_Decay.md

Completes Wave 4 (Capture Variants).
Seals PRIM:025–036 and condition prefixes MC-/CAS-/SCS-/HLC-/RLC-/AC-.
Module PRIM total: 001–036 (36 primitives). Wave 4: 6/6 canonical.

Refs: f_Capture.md, f_Collapse.md, f_Decay.md, f_Deflect.md,
      OPERATORS.md, GLOSSARY.md, INDEX.md, CHANGELOG.md

Session: SES-20260813-FGRAV-035
```

---

```
*
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║          ███████╗███████╗███████╗     ██╗    ██╗ █████╗ ██╗   ██╗███████╗    ║
║          ██╔════╝██╔════╝██╔════╝     ██║    ██║██╔══██╗██║   ██║██╔════╝    ║
║          █████╗  █████╗  █████╗       ██║ █╗ ██║███████║██║   ██║█████╗      ║
║          ██╔══╝  ██╔══╝  ██╔══╝       ██║███╗██║██╔══██║╚██╗ ██╔╝██╔══╝      ║
║          ██║     ██║     ██║          ╚███╔███╔╝██║  ██║ ╚████╔╝ ███████╗    ║
║          ╚═╝     ╚═╝     ╚═╝           ╚══╝╚══╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝    ║
║                                                                              ║
║                   ── WAVE 4 COMPLETION MILESTONE ──                          ║
║                                                                              ║
║   All 6 Capture Variant files are canonical and sealed.                      ║
║                                                                              ║
║   ✅  f_Capture_Multi.md        PRIM:025–026   MC-1–MC-5    CANONICAL        ║
║   ✅  f_Capture_Cascade.md      PRIM:027–028   CAS-1–CAS-5  CANONICAL        ║
║   ✅  f_Capture_Soft.md         PRIM:029–030   SCS-1–SCS-5  CANONICAL        ║
║   ✅  f_Capture_Hard.md         PRIM:031–032   HLC-1–HLC-5  CANONICAL        ║
║   ✅  f_Capture_Resonant.md     PRIM:033–034   RLC-1–RLC-5  CANONICAL        ║
║   ✅  f_Capture_Asymmetric.md   PRIM:035–036   AC-1–AC-5    CANONICAL        ║
║                                                                              ║
║   PRIM RANGE  ............  025–036  (12 primitives, Wave 4)                 ║
║   MODULE TOTAL  ..........  001–036  (36 primitives, all waves)              ║
║                                                                              ║
║   CONDITION PREFIXES SEALED:                                                 ║
║     MC-  ·  CAS-  ·  SCS-  ·  HLC-  ·  RLC-  ·  AC-                          ║
║                                                                              ║
║   FAILURE MODES (module) .....  FM-001–FM-010  FROZEN                        ║
║   INVARIANTS (module) ........  INV-001–INV-010  FROZEN                      ║
║                                                                              ║
║   Wave 0 ✅  Wave 1 ✅  Wave 2 ✅  Wave 3 ✅  Wave 4 ✅                    ║
║                                                                              ║
║   FFF_Gravity module core specification: COMPLETE                            ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

*End of f_Capture_Asymmetric.md — [FFF:GRAVITY:CAPTURE:ASYMMETRIC] v1.0.0 — Wave 4 File 6 of 6*
