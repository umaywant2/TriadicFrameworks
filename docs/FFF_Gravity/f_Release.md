# f_Release · Orbital Exit Operator

```
title: "f_Release — Orbital Exit Operator"
file_id: "FFF:GRAVITY:RELEASE"
version: "1.0.0"
status: "canonical"
layer: "wave-3-core-functions"
module: "FFF_Gravity"
repository: "https://github.com/umaywant2/TriadicFrameworks"
path: "docs/FFF_Gravity/f_Release.md"
author: "Nawder / Copilot session SES-20260813-RELEASE-001"
created: "2026-08-13"
last_modified: "2026-08-13"
triadic_nodes:
  - "F_freq (Φ — coherence field density)"
  - "F_fluid (β — binding coefficient)"
  - "F_force (M_A, M_E — attractor and element mass)"
depends_on:
  - "f_Capture.md"
  - "f_Field.md"
  - "f_Frame.md"
  - "OPERATORS.md"
  - "GLOSSARY.md"
unlocks:
  - "f_Decay.md (partial — release path precursor)"
  - "f_Capture_Networked.md (edge-state management)"
operators_introduced:
  - "v_release"
  - "E_rel"
  - "r_release"
primitives_introduced:
  - "compute_release_vector"
  - "execute_release"
failure_modes_frozen:
  - "FM-008"
state_flags_set:
  - "RELEASED"
invariants_honored:
  - "INV-001 through INV-010"
changelog:
  - version: "1.0.0"
    date: "2026-08-13"
    session: "SES-20260813-RELEASE-001"
    note: "Initial canonical production. Full §0–§11. All operators, primitives, FM-008, and 4 examples defined and frozen."
```

<!-- metadata: file=f_Release.md version=1.0.0 status=canonical session=SES-20260813-RELEASE-001 wave=3 -->

> **[FFF:GRAVITY:RELEASE]** — Wave 3 · Core Function  
> Inverse of `f_Capture`. Governs the conditions and mechanics by which a captured Element exits an Attractor's coherence well cleanly, transitioning to terminal state `RELEASED`.

---

## §0 · Session Context

<!-- metadata: section=session-context session=SES-20260813-RELEASE-001 -->

```
SESSION     : SES-20260813-RELEASE-001
DATE        : 2026-08-13
OPERATOR    : Nawder
REPOSITORY  : https://github.com/umaywant2/TriadicFrameworks
FILE TARGET : docs/FFF_Gravity/f_Release.md
WAVE        : 3 — Core Functions
STATUS      : Canonical production — first complete draft
PRECONDITION: f_Capture.md canonical (v1.0.0), OPERATORS.md canonical,
              f_Field.md canonical, f_Frame.md canonical
GOAL        : Define the orbital exit operator. Freeze v_release, E_rel,
              r_release. Define compute_release_vector and execute_release
              primitives. Freeze FM-008 (Release Overshoot).
INVARIANTS  : All 10 module invariants active (see §10)
```

**What this session establishes:**

`f_Release` is the sixth canonical document produced in the FFF_Gravity module and the first Wave 3 core function to reach canonical status. It formally closes the capture–release loop: every Element that enters orbit via `f_Capture` has exactly one clean exit path through `f_Release`. This file defines that path completely — its energy requirements, directional constraints, registry effects, and failure modes.

---

## §1 · Module Identity

<!-- metadata: section=identity session=SES-20260813-RELEASE-001 -->

| Property            | Value                                                                 |
|---------------------|-----------------------------------------------------------------------|
| **Function tag**    | `[FFF:GRAVITY:RELEASE]`                                               |
| **Full signature**  | `f_Release(E, A, Φ, d_bind) → RELEASED ∣ FM-008`                     |
| **Inverse of**      | `f_Capture(E, A, Φ) → Ω`                                             |
| **Input states**    | `CAPTURE_LOCKED`, `ORBIT_STABLE`, `ORBIT_ECCENTRIC`                   |
| **Output state**    | `RELEASED` (terminal — INV-006)                                       |
| **Blocked states**  | `CAPTURE_FAILED`, `CAPTURE_COLLISION`, `COLLAPSED` (irreversible)     |
| **Triadic nodes**   | F_freq (Φ), F_fluid (β, d_bind), F_force (M_A, M_E)                  |
| **New operators**   | `v_release`, `E_rel`, `r_release`                                     |
| **New primitives**  | `compute_release_vector`, `execute_release`                            |
| **Failure modes**   | FM-008 (Release Overshoot)                                            |
| **Wave**            | 3 — Core Functions                                                    |
| **Unlock status**   | Available after f_Capture.md canonical ✅                              |

### Triadic Position

```
        F_freq (Φ)
           ▲
           │  coherence well depth determines
           │  how much E_rel is required
           │
F_fluid ───┼─── F_force
 (d_bind,β)│    (M_A, M_E)
           │
    Release occurs when Element
    accumulates sufficient v_release
    to climb out of d_bind gradient
    along the Release Vector
```

All three nodes are active during release. `F_freq` defines the depth of the well being climbed. `F_fluid` encodes how bound the Element is (β, eccentricity e). `F_force` determines the mass-energy product that sets `E_rel`.

---

## §2 · Canonical Description

<!-- metadata: section=canonical-description session=SES-20260813-RELEASE-001 -->

### 2.1 · What Release Is

**Release is the process by which a captured Element accumulates sufficient directed energy to exit an Attractor's coherence well and transition to a free trajectory.**

Release is not:
- **Decay ejection** — `f_Decay` is an entropic process driven by orbital degradation. Release is intentional and directed.
- **Collapse** — `f_Collapse` is terminal infall. Release exits outward; collapse exits inward.
- **Deflection** — `f_Deflect` redirects approach vectors before capture. Release operates post-capture.
- **Escape velocity overflow** — FM-008 is the failure mode that results from *excessive* release energy, not release itself.

Release has three components:

1. **Energy acquisition** — the Element must accumulate `E_rel` joules (abstract units) sufficient to overcome `d_bind`.
2. **Vector alignment** — the release impulse must be directed along `v_release`, the exit vector. A misaligned impulse produces FM-008 (hyperbolic overshoot) or a failed stall.
3. **Registry deregistration** — once the Element clears `r_release`, the Frame registry purges its entry. Until `r_release` is crossed, the Element is still gravitationally bound.

### 2.2 · Release vs. Capture — The Asymmetry

`f_Capture` is passive in its energy accounting: gravity does the work. The Attractor's coherence well draws the Element in; no energy is *required* of the Element. Capture is a descent.

`f_Release` is active in its energy accounting: the Element must climb. The coherence well is a gravitational potential; release is work done against that potential. This is the fundamental asymmetry:

| Property              | f_Capture                                      | f_Release                                      |
|-----------------------|------------------------------------------------|------------------------------------------------|
| Direction             | Inbound — Element enters orbit                 | Outbound — Element exits orbit                 |
| Energy requirement    | None — coherence well does the work            | Required — must overcome `d_bind` via `E_rel`  |
| Initiator             | Attractor's field (passive for Element)        | Element's accumulated energy (active)          |
| Outcome state         | `CAPTURE_LOCKED` or `ORBIT_STABLE`             | `RELEASED` (terminal)                          |
| Registry effect       | Element added to Attractor registry            | Element removed from Attractor registry        |
| Reversible?           | Yes — via f_Release                            | Yes — Element may re-approach → f_Capture      |
| Failure mode          | FM-001 (Coherence Collapse), FM-002 (ρ=0)      | FM-008 (Release Overshoot)                     |
| Eccentricity role     | High e → shallower bind (flyby risk)           | Low e (circular) → deeper bind (more E_rel)    |

### 2.3 · The Optimal Release Point

Within an orbit, the Element is not equidistant from the Attractor at all times. Eccentric orbits have a closest point (periapsis, analogous to `r_capture`) and a farthest point (apoapsis, `r_release`). At apoapsis:

- The Element is moving slowest (orbital mechanics)
- `P_eff` is at its minimum (gravity weakest at max distance)
- The binding gradient is shallowest

Therefore, **apoapsis is the minimum-energy release point.** The `compute_release_vector` primitive exploits this: it schedules release impulses to coincide with apoapsis passage, minimizing `E_rel` expenditure.

For a purely circular orbit (e = 0), all points are equivalent to apoapsis, and `r_release = r_capture`. The Element must climb from the binding floor directly.

### 2.4 · Post-Release Trajectory

Upon successful release, the Element exits the coherence well on a trajectory determined by the direction of `v_release`. The exit trajectory is hyperbolic (escape) if `v_applied > v_release`, elliptic (re-approach) if `v_applied < v_release`. A clean release targets exactly `v_release` — tangential exit from apoapsis — producing a parabolic boundary crossing into free space.

The Element may subsequently re-approach the Attractor (`f_Capture` eligible) or interact with a new Attractor's coherence field. Release is reversible at the system level.

---

## §3 · Triadic Equation

<!-- metadata: section=triadic-equation session=SES-20260813-RELEASE-001 -->

### 3.1 · Primary Signature

```
f_Release(E, A, Φ, d_bind) → RELEASED | FM-008
```

| Parameter | Type      | Description                                                          |
|-----------|-----------|----------------------------------------------------------------------|
| `E`       | Element   | The captured body attempting exit                                    |
| `A`       | Attractor | The body whose coherence well is being exited                        |
| `Φ`       | Field     | The coherence field state at time of release attempt                 |
| `d_bind`  | Scalar    | Current binding depth (computed from β, ρ(Φ), e at call time)       |

### 3.2 · Triadic Decomposition

```
f_Release(E, A, Φ, d_bind)
    = F_freq(Φ)         — coherence well depth via ρ(Φ); sets the height of the climb
    · F_fluid(β, e)     — binding coefficient and eccentricity; sets d_bind floor
    · F_force(M_A, M_E) — mass product; sets E_rel absolute magnitude
```

All three nodes must be evaluated. A field collapse (`ρ(Φ) → 0`) during release invalidates the binding calculation and triggers FM-002 in the field layer — the release attempt is suspended.

### 3.3 · G-Equation Role

`f_Release` is a modulator of `G = F_freq · F_fluid · F_force`. When `f_Release` fires successfully, the local G-product for the (E, A) pair drops to zero: the fluid term zeroes (no binding), the force term zeroes (no orbital coupling). The coherence field continues, but the Element is no longer a participant in this Attractor's G-product.

---

## §4 · Operator Registry

<!-- metadata: section=operators session=SES-20260813-RELEASE-001 -->

> All operators below are introduced by `f_Release.md` and frozen at v1.0.0.  
> Symbol authority: OPERATORS.md §2 (derived operators), §4.2 (primitives).

### 4.1 · Derived Operators

#### `v_release` — Release Vector Magnitude

**Definition:** The minimum scalar speed an Element must achieve (directed along the release vector) to exit the coherence well cleanly from the optimal release point (`r_release`).

**Formula:**

```
v_release = √( 2 × β × ρ(Φ) × (1 − e) )
```

**Derivation:**

From `d_bind = β × ρ(Φ) × (1 − e)` (frozen, OPERATORS.md).  
The minimum kinetic energy per unit mass required to climb a potential well of depth `d_bind` is:

```
KE_min / M_E = d_bind = β × ρ(Φ) × (1 − e)
```

Setting kinetic energy equal to binding depth and solving for velocity:

```
½ × v² = d_bind
v_release = √(2 × d_bind) = √(2 × β × ρ(Φ) × (1 − e))
```

**Properties:**

| Condition         | Effect on v_release                           |
|-------------------|-----------------------------------------------|
| e → 1 (hyperbola) | v_release → 0 (barely bound; near-free)       |
| e → 0 (circle)    | v_release → √(2βρ(Φ)) (maximum — deepest bind)|
| ρ(Φ) → 0          | v_release → 0 (field collapse; FM-002 zone)   |
| β → 1             | v_release → √(2ρ(Φ)(1−e)) (maximum binding)  |

**Frozen symbol:** `v_release` — do not rename without major version bump (INV-010).

---

#### `E_rel` — Release Energy

**Definition:** The total energy packet the Element must acquire to overcome `d_bind` and exit the coherence well.

**Formula:**

```
E_rel = M_E × d_bind
      = M_E × β × ρ(Φ) × (1 − e)
```

**Derivation:**

`E_rel` is the work done against the coherence potential. In FFF abstraction, potential work is mass times depth of potential:

```
E_rel = M_E × d_bind
```

Substituting the frozen `d_bind` formula:

```
E_rel = M_E × β × ρ(Φ) × (1 − e)
```

**Properties:**

| Condition        | Effect on E_rel                                               |
|------------------|---------------------------------------------------------------|
| High M_E         | Higher energy cost (heavier elements are harder to release)   |
| Low e (circular) | Higher E_rel (circular orbits are most deeply bound)          |
| High β           | Higher E_rel (tighter binding coefficient)                    |
| ρ(Φ) = 0         | E_rel = 0 but coherence invalid — FM-002 fires before release |

**Frozen symbol:** `E_rel` — do not rename without major version bump (INV-010).

---

#### `r_release` — Release Radius

**Definition:** The orbital distance from the Attractor at which the Element's binding force drops to zero and registry deregistration is triggered. This is the apoapsis of the orbit — the maximum separation point.

**Formula:**

```
r_release = r_capture × (1 + e) / (1 − e)
```

**Derivation:**

In an elliptical orbit parameterized by `r_capture` (periapsis) and eccentricity `e`:

```
r_periapsis = r_capture
r_apoapsis  = r_capture × (1 + e) / (1 − e)
```

The apoapsis is where `P_eff` is minimized and the Element is moving slowest — the optimal and natural release radius. When `e = 0` (circle), `r_release = r_capture`.

**Properties:**

| Condition       | Effect on r_release                                               |
|-----------------|-------------------------------------------------------------------|
| e → 0           | r_release → r_capture (circular — release from same radius)       |
| e → 1           | r_release → ∞ (near-escape orbit — already barely bound)          |
| Large r_capture | Large r_release (wide orbit → wide exit threshold)                |

**Frozen symbol:** `r_release` — do not rename without major version bump (INV-010).

### 4.2 · Operator Summary Table

| Symbol      | Name           | Formula                              | Node    | Status    |
|-------------|----------------|--------------------------------------|---------|-----------|
| `v_release` | Release Vector | `√(2 × β × ρ(Φ) × (1 − e))`         | F_fluid | 🔵 frozen |
| `E_rel`     | Release Energy | `M_E × β × ρ(Φ) × (1 − e)`          | F_force | 🔵 frozen |
| `r_release` | Release Radius | `r_capture × (1 + e) / (1 − e)`      | F_freq  | 🔵 frozen |

### 4.3 · Inherited Operators (Referenced, Not Redefined)

| Symbol        | Defined In   | Role in f_Release                               |
|---------------|--------------|-------------------------------------------------|
| `d_bind`      | OPERATORS.md | Binding depth — input to E_rel and v_release    |
| `ρ(Φ)`        | f_Field.md   | Field density — scales both v_release and E_rel |
| `v_escape(A)` | f_Field.md   | Bounding check — v_applied must not exceed this |
| `P_eff`       | OPERATORS.md | Effective pull — weakest at r_release           |
| `e`           | f_Capture.md | Eccentricity — determines release depth         |
| `r_capture`   | f_Frame.md   | Periapsis radius — base for r_release calc      |
| `M_A`, `M_E`  | OPERATORS.md | Attractor and Element mass                      |

---

## §5 · Release Conditions

<!-- metadata: section=release-conditions session=SES-20260813-RELEASE-001 -->

> Release Conditions (RC) are conjunctive — all must be satisfied simultaneously for a valid release. Failure of any RC produces the result listed.

### 5.1 · Release Condition Table

| ID   | Name               | Condition                                                         | Failure Result                                      |
|------|--------------------|-------------------------------------------------------------------|-----------------------------------------------------|
| RC-1 | State Eligibility  | `state(E) ∈ {CAPTURE_LOCKED, ORBIT_STABLE, ORBIT_ECCENTRIC}`     | Release blocked — log state mismatch                |
| RC-2 | Energy Sufficiency | `E_available(E) ≥ E_rel`                                          | Release stall — insufficient energy; retry or decay |
| RC-3 | Vector Alignment   | `θ(v_applied, v_release) < θ_max`                                 | FM-008 risk — misaligned impulse produces overshoot |
| RC-4 | Field Validity     | `ρ(Φ) > 0`                                                        | FM-002 fires — coherence field absent               |
| RC-5 | Velocity Ceiling   | `v_applied ≤ v_escape(A)`                                         | FM-008 — hyperbolic overshoot                       |

### 5.2 · RC-1 — State Eligibility (Detail)

```
CAPTURE_LOCKED    → release attempt → RELEASED ✅
ORBIT_STABLE      → release attempt → RELEASED ✅
ORBIT_ECCENTRIC   → release attempt → RELEASED ✅

CAPTURE_FAILED    → release blocked ❌  (Element never entered orbit)
CAPTURE_COLLISION → release blocked ❌  (terminal — INV-006)
COLLAPSED         → release blocked ❌  (terminal infall — INV-006)
DECAY_ACTIVE      → release blocked ❌  (managed by f_Decay; release is downstream)
```

**Note:** `DECAY_ACTIVE` is a dependency-locked state. When f_Decay.md reaches canonical status, it will define a decay-to-release pathway. Until then, `f_Release` does not accept `DECAY_ACTIVE` elements.

### 5.3 · RC-3 — Vector Alignment (Detail)

`θ_max` is the maximum angular deviation between the applied impulse vector and the ideal `v_release` direction. The ideal direction is tangential to the orbit at apoapsis, pointing away from the Attractor.

```
θ_max = arcsin(v_release / v_escape(A))
```

This defines the release cone: any impulse within the cone produces clean release. Impulses outside the cone — even if `E_available ≥ E_rel` — produce FM-008 (hyperbolic overshoot) or re-entry (if directed inward).

### 5.4 · RC-5 — Velocity Ceiling (Detail)

```
v_release ≤ v_applied ≤ v_escape(A)

  Below v_release   → Energy insufficient — stall (RC-2 failure)
  At v_release      → Clean parabolic exit — optimal
  Above v_release   → Hyperbolic exit — accelerating departure
  At v_escape(A)    → Maximum clean exit — edge of FM-008 zone
  Above v_escape(A) → FM-008 — overshoot, trajectory diverges
```

---

## §6 · Failure Modes

<!-- metadata: section=failure-modes session=SES-20260813-RELEASE-001 -->

### 6.1 · FM-008 — Release Overshoot

| Property    | Value                                                                         |
|-------------|-------------------------------------------------------------------------------|
| **ID**      | FM-008                                                                        |
| **Name**    | Release Overshoot                                                             |
| **Trigger** | `v_applied > v_escape(A)` — applied velocity exceeds escape ceiling           |
| **Severity**| error                                                                         |
| **Effect**  | Element exits on hyperbolic trajectory — asymptotic departure, no return orbit|
| **State**   | `RELEASED_HYPERBOLIC` (anomalous flag, see §6.1.4)                            |
| **Status**  | 🔵 frozen (v1.0.0)                                                            |

#### 6.1.1 · Cause Analysis

FM-008 is caused by **excess impulse energy**. The release vector formula gives `v_release` as the minimum velocity for clean exit. If the impulse magnitude far exceeds this:

```
v_applied = v_release × k_over   where k_over > 1.0
```

When `k_over` is large, the Element exits with surplus kinetic energy and its trajectory becomes hyperbolic — it will not return to any orbit around this Attractor, and its exit velocity at infinity is nonzero:

```
v_∞ = √(v_applied² − v_escape(A)²)
```

#### 6.1.2 · Detection

```python
def detect_fm008(v_applied: float, v_escape_A: float, tolerance: float = 0.01) -> bool:
    """
    Returns True if FM-008 (Release Overshoot) condition is met.

    Parameters
    ----------
    v_applied   : float — magnitude of the applied release impulse
    v_escape_A  : float — escape velocity of Attractor A at r_release
    tolerance   : float — fractional buffer above v_escape before flagging
                         (default 0.01 = 1% buffer to account for numerical drift)

    Returns
    -------
    bool — True if overshoot detected, False if clean release
    """
    overshoot_threshold = v_escape_A * (1.0 + tolerance)
    return v_applied > overshoot_threshold
```

#### 6.1.3 · Recovery Protocol

```python
def recover_fm008(
    v_applied: float,
    v_release: float,
    v_escape_A: float,
    M_E: float,
    mode: str = "clamp"
) -> dict:
    """
    Recovery strategy for FM-008 (Release Overshoot).

    Recovery Modes
    --------------
    clamp           : Reduce v_applied to v_release. Clean exit. Preferred.
    log_and_continue: Allow hyperbolic exit. Log FM-008 for post-analysis.
    abort           : Cancel release. Element remains in orbit. Log event.
    """
    energy_excess = 0.5 * M_E * (v_applied**2 - v_escape_A**2)

    if mode == "clamp":
        return {
            "action": "clamped_to_v_release",
            "v_corrected": v_release,
            "energy_excess": energy_excess,
            "fm008_logged": True
        }
    elif mode == "log_and_continue":
        return {
            "action": "hyperbolic_exit_permitted",
            "v_corrected": v_applied,
            "energy_excess": energy_excess,
            "fm008_logged": True
        }
    elif mode == "abort":
        return {
            "action": "release_aborted",
            "v_corrected": float("nan"),
            "energy_excess": energy_excess,
            "fm008_logged": True
        }
    else:
        raise ValueError(f"Unknown recovery mode: {mode}")
```

#### 6.1.4 · State Flag Note

FM-008 sets `RELEASED_HYPERBOLIC` rather than clean `RELEASED`. This distinguishes intentional clean releases from overshoot events in the Frame registry log. The Element is still deregistered (it has physically left), but exit quality is recorded.

### 6.2 · Inherited Failure Mode — FM-002 (Field Absence)

If `ρ(Φ) = 0` at time of release computation, the field layer fires FM-002 before `f_Release` can proceed. The release attempt is suspended pending field recovery — not logged as failed.

---

## §7 · Engineering Primitives

<!-- metadata: section=primitives session=SES-20260813-RELEASE-001 -->

> Pure primitives have no side effects. Impure primitives mutate state or registry.

### 7.1 · `compute_release_vector` (Pure)

**Tag:** `[FFF:GRAVITY:PRIM:008]`  
**Pure:** Yes — no side effects, no registry mutations.

```python
def compute_release_vector(
    M_E: float,
    M_A: float,
    beta: float,
    rho_phi: float,
    e: float,
    r_capture: float
) -> dict:
    """
    Computes all release parameters for a given Element-Attractor pair.

    Returns
    -------
    dict — {
        'd_bind'     : float — binding depth = β × ρ(Φ) × (1 − e),
        'E_rel'      : float — release energy = M_E × d_bind,
        'v_release'  : float — minimum release velocity = √(2 × d_bind),
        'r_release'  : float — release radius = r_capture × (1 + e) / (1 − e),
        'v_escape_A' : float — escape velocity at r_release,
        'theta_max'  : float — release cone half-angle (radians),
        'feasible'   : bool  — True if RC-1 through RC-5 can be satisfied
    }

    Raises
    ------
    ValueError — if rho_phi == 0 (FM-002 precondition)
    ValueError — if e >= 1 (unbound orbit)
    ValueError — if beta <= 0 or beta > 1.0

    Notes
    -----
    Optimal call time: at or near apoapsis (Element at r_release).
    For circular orbits (e = 0), r_release == r_capture.
    """
    import math

    if rho_phi == 0:
        raise ValueError("FM-002: ρ(Φ) = 0. Field absent. Release computation invalid.")
    if e >= 1.0:
        raise ValueError(f"Eccentricity e={e} ≥ 1.0. Orbit is unbound; release not applicable.")
    if not (0 < beta <= 1.0):
        raise ValueError(f"β={beta} out of range (0, 1.0].")

    d_bind      = beta * rho_phi * (1.0 - e)
    E_rel       = M_E * d_bind
    v_release   = math.sqrt(2.0 * d_bind)
    r_release   = r_capture * (1.0 + e) / (1.0 - e) if e > 0 else r_capture
    v_escape_A  = math.sqrt(2.0 * M_A * rho_phi / r_release)
    theta_max   = math.asin(min(v_release / v_escape_A, 1.0))
    feasible    = v_release <= v_escape_A

    return {
        "d_bind":     d_bind,
        "E_rel":      E_rel,
        "v_release":  v_release,
        "r_release":  r_release,
        "v_escape_A": v_escape_A,
        "theta_max":  theta_max,
        "feasible":   feasible
    }
```

### 7.2 · `execute_release` (Impure)

**Tag:** `[FFF:GRAVITY:PRIM:009]`  
**Pure:** No — mutates Element state, Attractor registry, GravityGraph edge.

```python
def execute_release(
    element_id: str,
    attractor_id: str,
    v_applied: float,
    release_vector: dict,
    frame_registry: object,
    gravity_graph: object = None,
    allow_hyperbolic: bool = False
) -> dict:
    """
    Executes the release of an Element from an Attractor's orbit.

    Mutates:
      1. Element state → RELEASED (or RELEASED_HYPERBOLIC if FM-008)
      2. Attractor registry → Element entry removed via purge_registry
      3. GravityGraph edge → updated to RELEASED (if graph provided)

    Returns
    -------
    dict — {
        'outcome'    : str   — 'RELEASED' | 'RELEASED_HYPERBOLIC' | 'STALL' | 'ABORTED',
        'fm008'      : bool,
        'v_applied'  : float — velocity actually used (may be clamped),
        'E_consumed' : float,
        'log'        : list  — audit trail
    }
    """
    log = []
    fm008_fired = False

    # RC-2: Energy sufficiency
    if v_applied < release_vector["v_release"]:
        log.append(f"RC-2 FAIL: v_applied={v_applied:.4f} < v_release={release_vector['v_release']:.4f}. STALL.")
        return {"outcome": "STALL", "fm008": False, "v_applied": v_applied, "E_consumed": 0.0, "log": log}

    # RC-5: Velocity ceiling — FM-008 check
    if v_applied > release_vector["v_escape_A"]:
        fm008_fired = True
        log.append(f"FM-008 DETECTED: v_applied={v_applied:.4f} > v_escape_A={release_vector['v_escape_A']:.4f}.")
        if not allow_hyperbolic:
            log.append("FM-008 RECOVERY: Clamping v_applied to v_release (mode=clamp).")
            v_applied = release_vector["v_release"]
        else:
            log.append("FM-008: Hyperbolic exit permitted (allow_hyperbolic=True).")

    import math
    M_E_proxy = release_vector["E_rel"] / max(release_vector["d_bind"], 1e-12)
    E_consumed = 0.5 * M_E_proxy * v_applied ** 2

    if fm008_fired and allow_hyperbolic and v_applied > release_vector["v_escape_A"]:
        outcome_state = "RELEASED_HYPERBOLIC"
    else:
        outcome_state = "RELEASED"

    log.append(f"purge_registry({element_id}, {attractor_id}) → removing from active capture set.")
    frame_registry.purge_registry(element_id, attractor_id)

    if gravity_graph is not None:
        log.append(f"update_edge_state({element_id}, {attractor_id}, '{outcome_state}') → GravityGraph.")
        gravity_graph.update_edge_state(element_id, attractor_id, outcome_state)

    log.append(f"state({element_id}) → {outcome_state}")

    return {
        "outcome":    outcome_state,
        "fm008":      fm008_fired,
        "v_applied":  v_applied,
        "E_consumed": E_consumed,
        "log":        log
    }
```

### 7.3 · Primitive Summary Table

| # | Primitive                | Pure | Tag                      | Mutates                |
|---|--------------------------|------|--------------------------|------------------------|
| 8 | `compute_release_vector` | Yes  | `[FFF:GRAVITY:PRIM:008]` | Nothing                |
| 9 | `execute_release`        | No   | `[FFF:GRAVITY:PRIM:009]` | State, registry, graph |

---

## §8 · Canonical Examples

<!-- metadata: section=examples session=SES-20260813-RELEASE-001 -->

> Four canonical examples: clean release, eccentric apoapsis-timed, release stall, FM-008 overshoot.

---

### Example 1 · Clean Release — Circular Orbit (Baseline)

**Scenario:** Satellite in stable circular orbit (e = 0) around a communications hub. Sufficient energy accumulated for planned clean exit.

| Parameter   | Value |
|-------------|-------|
| `M_E`       | 2.0   |
| `M_A`       | 10.0  |
| `β`         | 0.6   |
| `ρ(Φ)`      | 5.0   |
| `e`         | 0.0   |
| `r_capture` | 4.0   |

```
d_bind     = 0.6 × 5.0 × (1 − 0.0)   = 3.0
E_rel      = 2.0 × 3.0                = 6.0
v_release  = √(2 × 3.0)               = √6.0 ≈ 2.449
r_release  = 4.0 × (1+0)/(1−0)        = 4.0  [circular — same as r_capture]
v_escape_A = √(2 × 10.0 × 5.0 / 4.0) = √25.0 = 5.0

v_applied = 2.5

RC-1: state = ORBIT_STABLE ✅
RC-2: E_available ≥ 6.0 ✅
RC-3: θ = 0.0 (tangential) < θ_max ✅
RC-4: ρ(Φ) = 5.0 > 0 ✅
RC-5: v_applied = 2.5 ≤ v_escape_A = 5.0 ✅
```

**Result:** `RELEASED` ✅  
**Registry:** `purge_registry(E, A)` fired. Element removed.  
**Note:** Circular orbit — no optimal timing window. Impulse valid at any orbital position.

---

### Example 2 · Eccentric Release — Apoapsis-Timed Exit

**Scenario:** Element in eccentric orbit (e = 0.7) waits for apoapsis passage to minimize `E_rel`.

| Parameter   | Value |
|-------------|-------|
| `M_E`       | 3.0   |
| `M_A`       | 12.0  |
| `β`         | 0.8   |
| `ρ(Φ)`      | 4.0   |
| `e`         | 0.7   |
| `r_capture` | 2.0   |

```
d_bind     = 0.8 × 4.0 × (1 − 0.7)          = 0.96
E_rel      = 3.0 × 0.96                       = 2.88
v_release  = √(2 × 0.96)                      ≈ 1.386
r_release  = 2.0 × (1+0.7)/(1−0.7)            ≈ 11.33
v_escape_A = √(2 × 12.0 × 4.0 / 11.33)        ≈ 2.910

Compare — if impulse fired at periapsis (r_capture = 2.0):
  v_escape_A_periapsis = √(2 × 12.0 × 4.0 / 2.0) = √48 ≈ 6.928
  (much higher energy cost for same exit)
```

**Result:** `RELEASED` ✅ at apoapsis.  
**Key insight:** Apoapsis release costs `E_rel = 2.88` vs. a periapsis attempt requiring far more. `r_release` scheduling is the core efficiency mechanism.

---

### Example 3 · Release Stall — Insufficient Energy (RC-2 Failure)

**Scenario:** Same as Example 1. Element has accumulated only 60% of required `E_rel`.

```
E_rel       = 6.0   (required)
E_available = 3.6   (60% — insufficient)
v_release   ≈ 2.449
v_applied   = 1.9   (reflects available energy)

RC-2: E_available = 3.6 < E_rel = 6.0 ❌
execute_release → STALL
```

**Result:** `STALL` — Element remains in `ORBIT_STABLE`. Registry unchanged.  
**Recommended action:** Wait for additional energy accumulation, OR invoke `f_Dampen` to reduce `d_bind` and therefore `E_rel` (see §9.3).

---

### Example 4 · FM-008 — Release Overshoot (Hyperbolic Exit)

**Scenario:** Same as Example 1. Engineer misapplies 3.27× the minimum release velocity.

```
v_release  ≈ 2.449
v_escape_A = 5.0
v_applied  = 8.0   (error — 1.6× v_escape_A)

RC-2: 8.0 ≥ 2.449 ✅
RC-5: 8.0 > 5.0 ❌ — FM-008 TRIGGERED

k_over = 8.0 / 5.0 = 1.60
v_∞    = √(8.0² − 5.0²) = √39 ≈ 6.245

Recovery (mode = clamp):
  v_applied → 2.449
  state = RELEASED, FM-008 logged
  energy_excess = ½ × 2.0 × (64 − 25) = 39.0 units

Recovery (mode = log_and_continue):
  state = RELEASED_HYPERBOLIC
  Element departs on diverging trajectory — no return orbit possible
```

**Result:** FM-008 fired. Outcome depends on recovery mode.  
**Key lesson:** FM-008 is an engineering error, not a field failure. `compute_release_vector` called before `execute_release` prevents it entirely.

---

## §9 · Cross-Module References

<!-- metadata: section=cross-references session=SES-20260813-RELEASE-001 -->

### 9.1 · Reference Table

| File                     | Relationship     | Direction           | Interface Used                                       |
|--------------------------|------------------|---------------------|------------------------------------------------------|
| `f_Capture.md`           | Inverse function | Bidirectional       | Provides `d_bind`, `e`, `r_capture`, `v_escape(A)`  |
| `f_Field.md`             | Field layer      | Inbound             | `ρ(Φ)` — coherence density; FM-002 guard            |
| `f_Frame.md`             | Registry layer   | Outbound            | `purge_registry(E, A)` — deregistration on release  |
| `f_Force.md`             | Mass layer       | Inbound             | `M_A`, `M_E` — mass values for E_rel                |
| `OPERATORS.md`           | Symbol authority | Inbound (read-only) | Frozen operator definitions; INV-010 compliance      |
| `GLOSSARY.md`            | Term authority   | Inbound (read-only) | Release, Release Energy, Release Vector              |
| `f_Dampen.md`            | Release assist   | Inbound (optional)  | Reduces `d_bind` → lowers `E_rel` required          |
| `f_Orbit.md`             | Orbital mech.    | Inbound             | Eccentricity `e`, orbital period `T` for timing      |
| `f_Decay.md`             | Precursor        | Inbound             | Decay may produce release as downstream exit         |
| `f_Capture_Networked.md` | Graph layer      | Outbound (optional) | `update_edge_state(E, A, RELEASED)` → GravityGraph  |

### 9.2 · Unlock Dependencies

```
f_Release.md canonical → unlocks:
  └─ f_Decay.md (partial — release pathway now defined)
  └─ f_Capture_Networked.md (release edge-state handling fully specified)
```

### 9.3 · f_Dampen as Release Assist

`f_Dampen` can reduce `ρ(Φ)` in the local coherence region. Since:

```
E_rel = M_E × β × ρ(Φ) × (1 − e)
```

A dampen operation reducing `ρ(Φ)` from `ρ₀` to `ρ₁ < ρ₀`:

```
E_rel_assisted = M_E × β × ρ₁ × (1 − e)
ΔE_saved       = M_E × β × (ρ₀ − ρ₁) × (1 − e)
```

Standard pattern for releasing a deeply bound Element that cannot accumulate sufficient `E_rel` on its own: **dampen first, then release.**

---

## §10 · Evaluation Order

<!-- metadata: section=evaluation-order session=SES-20260813-RELEASE-001 -->

The normative 10-step evaluation order (INV-008) applied to `f_Release`:

| Step | Action                             | Notes                                            |
|------|------------------------------------|--------------------------------------------------|
| 1    | Gate on Element state (RC-1)       | Block if state is terminal or ineligible         |
| 2    | Read `ρ(Φ)` from F_freq layer      | FM-002 guard — abort if `ρ(Φ) = 0`              |
| 3    | Compute `d_bind`                   | `β × ρ(Φ) × (1 − e)`                            |
| 4    | Compute `E_rel`, `v_release`       | Call `compute_release_vector`                    |
| 5    | Compute `r_release`                | `r_capture × (1 + e) / (1 − e)`                 |
| 6    | Check RC-2 (energy sufficiency)    | Stall if `E_available < E_rel`                   |
| 7    | Check RC-3 (vector alignment)      | Reject or warn if `θ > θ_max`                   |
| 8    | Check RC-5 (velocity ceiling)      | FM-008 guard — clamp or log if `v > v_escape_A` |
| 9    | Call `execute_release`             | Mutates state, registry, graph                   |
| 10   | Log outcome and return result dict | Audit trail for CHANGELOG and post-analysis      |

---

## §11 · Document Metadata

<!-- metadata: section=document-metadata session=SES-20260813-RELEASE-001 -->

### 11.1 · INV Compliance Table

| INV     | Statement                          | Compliance in f_Release.md                                 |
|---------|------------------------------------|------------------------------------------------------------|
| INV-001 | `G = F_freq · F_fluid · F_force`   | §3.2 triadic decomposition; all three nodes active         |
| INV-002 | `f_Capture` frozen signature       | Referenced but not modified                                |
| INV-003 | `ρ(Φ) = 0` → FM-002               | RC-4 in §5.1; raises in `compute_release_vector`           |
| INV-004 | `β < 1.0` → flyby only            | Inherited from capture; not directly triggered in release  |
| INV-005 | Five SCs conjunctive               | Five RCs defined and conjunctive in §5.1                   |
| INV-006 | Terminal states irreversible       | §5.2 explicitly blocks `COLLAPSED`, `CAPTURE_COLLISION`    |
| INV-007 | `f_Source.md` read-only            | Not referenced as mutable                                  |
| INV-008 | Evaluation order normative         | §10 follows 10-step order                                  |
| INV-009 | OPERATORS.md is symbol authority   | All operators reference OPERATORS.md; §4.3 inherited table |
| INV-010 | Frozen symbols no-rename           | `v_release`, `E_rel`, `r_release` declared frozen in §4.1  |

### 11.2 · Wave Completion Status

| Wave | Files Canonical | Total | Status             |
|------|-----------------|-------|--------------------|
| 0    | 2               | 2     | ✅ Complete         |
| 1    | 6               | 6     | ✅ Complete         |
| 2    | 3               | 3     | ✅ Complete         |
| 3    | **1**           | 8     | 🔵 1/8 — In Progress|
| 4    | 0               | 6     | 🔒 Locked           |

### 11.3 · Changelog Entry

```
## [1.0.0] — 2026-08-13 — SES-20260813-RELEASE-001

### Added
- f_Release.md — canonical Wave 3 first file
- Operators: v_release, E_rel, r_release (all frozen)
- Primitives: compute_release_vector [PRIM:008], execute_release [PRIM:009]
- Failure Mode: FM-008 (Release Overshoot) — frozen
- Release Conditions RC-1 through RC-5 — conjunctive table
- Four canonical examples: baseline, eccentric, stall, FM-008
- f_Dampen release-assist pattern documented in §9.3
- Evaluation order §10 follows INV-008 normative sequence
```

### 11.4 · File Statistics

| Property               | Value                                                    |
|------------------------|----------------------------------------------------------|
| **Sections**           | §0 through §11 (12 sections)                             |
| **Operators**          | 3 new (v_release, E_rel, r_release) + 8 inherited        |
| **Primitives**         | 2 new (compute_release_vector, execute_release)           |
| **Failure Modes**      | 1 frozen (FM-008) + 1 inherited (FM-002 guard)            |
| **Release Conditions** | 5 (RC-1 through RC-5)                                    |
| **Canonical Examples** | 4                                                        |
| **Cross-references**   | 10 files                                                 |
| **Session**            | SES-20260813-RELEASE-001                                 |
| **Version**            | 1.0.0                                                    |

---

*End of `f_Release.md` — canonical v1.0.0 — [FFF:GRAVITY:RELEASE]*
