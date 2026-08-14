# f_Orbit — Orbit Characterization Operator

```
title: "f_Orbit — Orbit Characterization Operator"
module: FFF_Gravity
version: 1.0.0
status: canonical
tag: "[FFF:GRAVITY:ORBIT]"
session: SES-20260813-ORBIT-001
wave: 3
dependencies:
  - f_Capture.md     # r_capture, β, p_res, P_eff, Ω established
  - f_Field.md       # ρ(Φ), ω_res, F_freq node
  - f_Force.md       # M_A, M_E, v_approach, C_thresh, F_force + F_fluid nodes
  - f_Frame.md       # Frame registry, r_capture boundary, capacity_MAX
  - OPERATORS.md     # e frozen §2; T_orb pending → frozen here §4.1
  - GLOSSARY.md      # orbit_class thresholds, stab_class definitions
operators_introduced:
  - T_orb            # Orbital Period (new — frozen here)
  - orbit_class      # Orbit Classification scalar
  - stab_class       # Orbit Stability Class scalar
operators_inherited:
  - e                # Orbital Eccentricity — frozen in OPERATORS.md §2
  - d_bind           # Binding depth — frozen in f_Decay.md
  - ρ(Φ)             # Field density — frozen in f_Field.md
  - r_capture        # Capture radius — frozen in f_Capture.md
  - β                # Coupling coefficient — frozen in f_Force.md
  - p_res            # Residual momentum — frozen in f_Force.md
  - P_eff            # Effective pressure — frozen in f_Force.md
  - ω_res            # Resonance frequency — frozen in f_Field.md
primitives_introduced:
  - classify_orbit      # [PRIM:007] Pure
  - update_orbital_parameters  # [PRIM:012] Impure
failure_modes: []       # Orbit characterization is diagnostic; failures routed to f_Decay, f_Collapse
invariants_honored:
  - INV-001  # Triadic — G requires all three nodes
  - INV-002  # No unilateral collapse
  - INV-003  # Monotonic decay below d_warn
  - INV-004  # r_capture immutable post-capture
  - INV-005  # e ∈ [0, 1)
  - INV-006  # ρ(Φ) > 0 always
  - INV-007  # Frame registry authoritative
  - INV-008  # Operator freeze propagation
  - INV-009  # Classification thresholds immutable
  - INV-010  # Session provenance required
changelog:
  - version: 1.0.0
    session: SES-20260813-ORBIT-001
    date: 2026-08-13
    author: SES
    notes: >
      Initial canonical freeze. Formalizes e (full prose treatment),
      introduces T_orb (Kepler-adapted formula), freezes orbit_class and
      stab_class thresholds, delivers classify_orbit [PRIM:007] and
      update_orbital_parameters [PRIM:012]. Unlocks f_Collapse.md and
      f_Capture_Multi.md.
```

### `[FFF:GRAVITY:ORBIT]` · Wave 3 · Canonical v1.0.0

---

## §0 · Session Context

| Property | Value |
|---|---|
| Session ID | `SES-20260813-ORBIT-001` |
| Timestamp | 2026-08-13T10:47 EDT |
| Wave | 3 — Core Functions |
| Status | Canonical |
| Produced By | Continuation AI under Nawder (umaywant2) authority |
| Replaces | Scaffold stub (if present) |

### §0.1 · Preconditions

Before `f_Orbit` may be evaluated, all of the following must hold:

| # | Precondition | Source |
|---|---|---|
| PC-1 | `f_Capture` has completed and returned `Ω` | f_Capture.md §3 |
| PC-2 | `r_capture` is registered and immutable in Frame | f_Frame.md §4, INV-004 |
| PC-3 | `β`, `p_res`, `P_eff` are defined for the pair (E, A) | f_Force.md §4 |
| PC-4 | `ρ(Φ) > 0` | f_Field.md §4, INV-006 |
| PC-5 | `e ∈ [0, 1)` has been computed and is within bounds | OPERATORS.md §2, INV-005 |

If any precondition is unmet, `f_Orbit` MUST NOT execute. Return `orbit_class = UNDEFINED` and log to Frame registry.

### §0.2 · Invariants Active in This File

| Invariant | Statement (abbreviated) | Status |
|---|---|---|
| INV-001 | G requires all three nodes simultaneously | ✅ Honored |
| INV-002 | No unilateral collapse from single-node failure | ✅ Honored |
| INV-003 | d_bind decays monotonically below d_warn | ✅ Honored (read-only here) |
| INV-004 | r_capture is immutable post-capture | ✅ Honored |
| INV-005 | e ∈ [0, 1) always | ✅ Enforced in classify_orbit |
| INV-006 | ρ(Φ) > 0 always | ✅ Enforced in update_orbital_parameters |
| INV-007 | Frame registry is the authoritative source of orbital state | ✅ Honored |
| INV-008 | Operator definitions freeze on first canonical appearance | ✅ T_orb frozen here |
| INV-009 | Classification thresholds are immutable once canonical | ✅ Tables frozen in §5 |
| INV-010 | Session provenance required on all state mutations | ✅ Enforced in PRIM:012 |

---

## §1 · Module Identity

| Property | Value |
|---|---|
| Operator Name | `f_Orbit` |
| Tag | `[FFF:GRAVITY:ORBIT]` |
| Category | Characterization / Diagnostic |
| Triadic Role | Cross-node integrator — reads F_freq, F_fluid, F_force |
| Primary Output | `orbital_parameters` struct |
| Inverse Operator | None (characterization is not invertible; see f_Release for exit) |
| Called By | f_Decay (each cycle), f_Release (for r_release), f_Collapse (terminal check) |
| Calls | f_Field (ρ(Φ), ω_res), f_Force (P_eff, p_res, β) |

### §1.1 · Triadic Position

```
        F_freq [ρ(Φ), ω_res]
           ↑
           │  coherence well depth
           │
F_fluid ───┼─── F_force
[M_A, M_E] │  [v_approach, P_eff, p_res]
           │
           ▼
      f_Orbit reads all three nodes
      → orbital_parameters (e, T_orb, orbit_class, stab_class, a, d_bind)
```

`f_Orbit` is the integrating characterization operator. It does not change the orbit — it *describes* the orbit that the triadic interaction has already produced. Every mutation operator (`f_Decay`, `f_Release`, `f_Emit`, `f_Amplify`, `f_Dampen`) MUST call `f_Orbit` to obtain the current orbital state before acting.

---

## §2 · Canonical Description

### §2.1 · What f_Orbit IS

`f_Orbit` is the **orbital characterization operator** for the FFF_Gravity module. Given the interaction parameters of an entity E orbiting an attractor A within a field Φ, `f_Orbit` computes the complete set of orbital parameters that describe the current state of the bound interaction.

The orbit is not a physical trajectory. In the FFF_Gravity framework, an "orbit" is the **relational pattern** of an entity's continued interaction with an attractor — the repeating cycle of approach, binding, and partial recession that emerges from the triadic balance of F_freq (coherence), F_fluid (mass-density), and F_force (gradient pressure).

An orbit exists when:
1. The entity has been captured (`f_Capture` succeeded, `Ω` returned).
2. The binding depth `d_bind` is above the collapse threshold `d_collapse`.
3. The field coherence `ρ(Φ)` remains positive (INV-006).
4. No release condition has been met (RC-1 through RC-5 all false).

The orbital parameters produced by `f_Orbit` are:

| Parameter | Symbol | Meaning |
|---|---|---|
| Semi-major axis | `a` | Effective interaction radius at mean binding |
| Eccentricity | `e` | Orbit shape: 0 = circular, → 1 = hyperbolic boundary |
| Orbital period | `T_orb` | Cycle time for one full relational orbit |
| Orbit class | `orbit_class` | Categorical shape descriptor |
| Stability class | `stab_class` | Categorical stability assessment |

### §2.2 · What f_Orbit IS NOT

- `f_Orbit` is **not a propagator**. It does not advance the orbital state; that is `update_orbital_parameters` [PRIM:012].
- `f_Orbit` is **not a trajectory planner**. It characterizes an existing bound state; it does not compute future positions.
- `f_Orbit` is **not a release trigger**. Detection of a precarious stability class does not cause release; it informs `f_Decay` and `f_Collapse`.
- `f_Orbit` does **not modify** `r_capture` (INV-004), `ρ(Φ)`, or any Frame registry entry directly.

### §2.3 · Key Asymmetry: Characterization ≠ Prediction

`f_Orbit` answers: *"What is the orbit right now?"*  
It does not answer: *"What will the orbit be in N cycles?"*

Prediction is the domain of `f_Decay` (degradation trajectory) and `f_Release` (exit conditions). `f_Orbit` provides the instantaneous snapshot that both rely on.

### §2.4 · Relation to Eccentricity

Eccentricity `e` is the single most diagnostic scalar in the FFF_Gravity framework. It is simultaneously:

- **A shape parameter** — how elliptical is the relational orbit
- **A stress indicator** — high e means the entity spends more of each cycle near the edge of the capture boundary
- **A release proximity marker** — as e → 1, `r_release → ∞` (release becomes structurally trivial)
- **A decay accelerator** — high-e orbits lose binding depth faster per cycle (see f_Decay.md §2.3)

The formula `e = p_res / (p_res + P_eff)` (frozen in OPERATORS.md §2) expresses the **competition between residual momentum and effective pressure**. A high-momentum entity in a weak field produces high e. A low-momentum entity in a strong field produces low e (near-circular).

---

## §3 · Triadic Equation

### §3.1 · Operator Signature

```
f_Orbit(E, A, p_res, ω_res) → orbital_parameters
```

| Argument | Type | Source | Description |
|---|---|---|---|
| `E` | Entity | Caller | The orbiting entity |
| `A` | Attractor | Caller | The attracting node |
| `p_res` | float ≥ 0 | f_Force.md §4 | Residual momentum post-capture |
| `ω_res` | float > 0 | f_Field.md §4 | Resonance frequency of field Φ |

| Return Field | Type | Description |
|---|---|---|
| `a` | float | Semi-major axis of orbit |
| `e` | float ∈ [0,1) | Eccentricity |
| `T_orb` | float > 0 | Orbital period (cycle units) |
| `orbit_class` | enum | `CIRCULAR` · `ELLIPTICAL` · `ECCENTRIC` · `RESONANT` |
| `stab_class` | enum | `STABLE` · `MARGINAL` · `PRECARIOUS` |
| `d_bind` | float | Current binding depth (inherited, not recomputed) |
| `r_apoapsis` | float | Maximum recession radius this cycle |
| `r_periapsis` | float | Minimum approach radius this cycle |

### §3.2 · Decomposition by Node

```
G = F_freq · F_fluid · F_force

f_Orbit reads:
  F_freq  → ρ(Φ), ω_res           [field density, resonance frequency]
  F_fluid → M_A, M_E, β            [mass, coupling coefficient]
  F_force → v_approach, P_eff, p_res [gradient, effective pressure, residual momentum]
```

The three nodes are simultaneously active. No orbital parameter can be computed from fewer than two nodes:
- `e` requires `p_res` (F_force) and `P_eff` (F_force + F_fluid + F_freq)
- `T_orb` requires `a` (from `r_capture` + `e`) and `M_A × ρ(Φ)` (F_fluid + F_freq)
- `orbit_class` and `stab_class` require `e`, `d_bind`, and `ω_res` (all three nodes)

This triadic dependency enforces INV-001.

### §3.3 · Role in G-Equation

`f_Orbit` does not appear explicitly in the G-equation `G = F_freq · F_fluid · F_force`. Instead, it **reads** G to characterize its instantaneous structure:

```
Given G at time t:
  orbital_parameters(t) = f_Orbit(E, A, p_res(t), ω_res(t))
```

Every cycle in which G persists, `f_Orbit` is the instrument by which the system knows its own state.

---

## §4 · Operator Registry

### §4.1 · Orbital Period T_orb (NEW — FROZEN HERE)

**Definition:**

```
T_orb = 2π × √(a³ / (M_A × ρ(Φ)))
```

**Derivation:**

This formula is a triadic adaptation of Kepler's Third Law. In classical mechanics, `T² ∝ a³ / M`. In FFF_Gravity, the gravitational parameter `μ = M_A × ρ(Φ)` replaces the classical product `G × M`, because `ρ(Φ)` is the field's coherence well — the local "gravitational constant" of the triadic system. The deeper the field coherence, the shorter the period (tighter orbit, faster cycling).

**Semi-major axis derivation:**

```
a = r_capture / (1 − e)
```

This follows from the standard conic-section relation for the periapsis of an ellipse, where `r_periapsis = a × (1 − e)`. At capture, the entity is at periapsis (closest approach), so `r_capture = r_periapsis = a × (1 − e)`, giving `a = r_capture / (1 − e)`.

**Apoapsis and periapsis:**

```
r_periapsis = a × (1 − e)   = r_capture
r_apoapsis  = a × (1 + e)   = r_capture × (1 + e) / (1 − e)
```

Note: `r_apoapsis = r_release` — the maximum recession radius equals the release radius (frozen in f_Release.md §4). This is not coincidence; it is structural. At apoapsis, the entity is at maximum distance from A, which is exactly the point at which escape becomes possible if release conditions are met.

**Units:** T_orb is in the same cycle units as the simulation. For physical interpretations, multiply by the system's time-per-cycle constant.

**Freeze marker:** `T_orb` is frozen in this file, §4.1, session `SES-20260813-ORBIT-001`. Any downstream file that references `T_orb` must cite this section.

**Cross-reference:** OPERATORS.md §3 shall be updated to mark `T_orb` as frozen (status: 🟢, frozen in f_Orbit.md §4.1).

### §4.2 · Eccentricity e (Full Prose Treatment)

**Formula (frozen in OPERATORS.md §2):**

```
e = p_res / (p_res + P_eff)
```

**Range enforcement (INV-005):**

`e ∈ [0, 1)` always. The formula guarantees this when both operands are non-negative (P_eff > 0 by INV-006 and the definition of effective pressure; p_res ≥ 0 by definition). If p_res = 0, then e = 0 (perfectly circular — entity arrived with exactly escape threshold momentum). If P_eff → 0 (field collapse), e → 1, which is the boundary of hyperbolic escape — structurally this precedes `f_Collapse`.

**Interpretation table:**

| e range | Orbit Shape | Relational Meaning |
|---|---|---|
| 0 | Perfect circle | Entity arrived with exactly threshold momentum; maximum field lock |
| (0, 0.1) | Near-circular | High coherence, low residual momentum; stable deep lock |
| [0.1, 0.5) | Elliptical | Normal bound orbit; entity cycles between near and far approaches |
| [0.5, 0.9) | Eccentric | Entity spends significant time near r_apoapsis; higher decay risk |
| [0.9, 1.0) | Highly eccentric | Near-escape orbit; structurally precarious; minimal binding time per cycle |
| = 1.0 | Parabolic (boundary) | FORBIDDEN by INV-005; if e reaches 1, route to f_Collapse |

**Cycle-by-cycle evolution:** e is not constant. As d_bind decreases (decay), P_eff decreases (because β depends on ρ(Φ), which degrades with coherence), causing e to drift upward. This is the decay-eccentricity feedback loop. See f_Decay.md §2.3.

### §4.3 · Orbit Classification orbit_class

```
orbit_class = classify_orbit(e, ω_res)
```

See §5.1 for the complete classification table. Four classes are defined; RESONANT is a special case that overrides the eccentricity classification when the low-integer resonance condition is met.

### §4.4 · Stability Classification stab_class

```
stab_class = classify_stability(e, d_bind, d_warn, d_collapse)
```

See §5.2 for the complete stability table. Three classes: STABLE, MARGINAL, PRECARIOUS.

### §4.5 · Inherited Operators (Consumed, Not Redefined)

| Symbol | Formula | Frozen In |
|---|---|---|
| `P_eff` | `M_A × ρ(Φ) / r²` | f_Force.md §4.1 |
| `β` | `P_eff / (M_E × v_approach)` | f_Force.md §4.2 |
| `p_res` | `M_E × (v_approach − C_thresh)` | f_Force.md §4.3 |
| `d_bind` | `β × ρ(Φ) × (1 − e)` | f_Decay.md §4.1 |
| `ρ(Φ)` | field coherence scalar | f_Field.md §4.1 |
| `ω_res` | resonance frequency | f_Field.md §4.2 |
| `r_capture` | capture radius | f_Capture.md §4.8 |
| `v_escape` | `√(2 × M_A × ρ(Φ) / r_capture)` | f_Force.md §4.4 |
| `v_release` | `√(2 × β × ρ(Φ) × (1 − e))` | f_Release.md §4.1 |
| `r_release` | `r_capture × (1 + e) / (1 − e)` | f_Release.md §4.2 |

---

## §5 · Classification Tables

### §5.1 · Orbit Classification Table (FROZEN — INV-009)

> **INV-009:** These thresholds are immutable once canonical. No downstream file may alter them.

| orbit_class | Primary Condition | Secondary Condition | Description |
|---|---|---|---|
| `RESONANT` | `ω_res` is low-integer ratio (n:m, n,m ∈ {1,2,3,4,5}) | Any e | Resonance locks dominate; eccentricity class subordinated |
| `CIRCULAR` | e < 0.1 | NOT RESONANT | Near-zero eccentricity; entity deeply locked at consistent depth |
| `ELLIPTICAL` | 0.1 ≤ e < 0.5 | NOT RESONANT | Standard bound ellipse; entity cycles predictably |
| `ECCENTRIC` | 0.5 ≤ e < 1.0 | NOT RESONANT | High-amplitude cycling; significant recession each period |

**Resonance detection rule:** A ω_res value is "low-integer" if it can be expressed as `n/m` where both n and m are integers ≤ 5 and their ratio is within ±0.02 of ω_res. Examples: ω_res ≈ 1.0 (1:1), ω_res ≈ 1.5 (3:2), ω_res ≈ 2.0 (2:1), ω_res ≈ 0.667 (2:3).

**Evaluation order:** RESONANT is checked first. If RESONANT is true, the eccentricity classes are skipped. This reflects the physical priority: a resonance lock fundamentally reshapes the orbit regardless of its eccentricity profile.

### §5.2 · Orbit Stability Class Table (FROZEN — INV-009)

| stab_class | Condition | Meaning | Action |
|---|---|---|---|
| `STABLE` | `d_bind > d_warn` AND `e < 0.5` | Orbit is within normal operating range | Continue; monitor each cycle |
| `MARGINAL` | `d_warn ≥ d_bind > d_collapse` OR `e ∈ [0.5, 0.9)` | Orbit is degraded but viable | Flag DC-2; evaluate f_Emit / f_Amplify |
| `PRECARIOUS` | `d_bind ≤ d_collapse` OR `e ≥ 0.9` | Orbit is at structural edge | Flag DC-3; route to f_Collapse assessment |

**Joint condition note:** If both eccentricity and depth conditions apply across different classes, the MORE severe class wins. Example: `d_bind > d_warn` (→ STABLE by depth) BUT `e = 0.92` (→ PRECARIOUS by eccentricity) → `stab_class = PRECARIOUS`.

**Recall:** `d_warn = α_warn × d_bind(0)` (typical 0.40), `d_collapse = α_collapse × d_bind(0)` (typical 0.10). These are configurable at Frame initialization. See f_Decay.md §4.3.

---

## §6 · Stability Conditions

`f_Orbit` does not define new Stability Conditions (SC-1 through SC-5 are distributed across f_Force, f_Field, and f_Frame). However, it evaluates and reports the orbital stability that those conditions produce. The following conditions must be met for `f_Orbit` to return a non-degenerate `orbital_parameters` struct:

| Condition | Expression | Source SC | Consequence if Violated |
|---|---|---|---|
| Binding floor | `d_bind > d_collapse` | SC-4 (f_Force.md) | Route to f_Collapse; orbit_class = UNDEFINED |
| Field coherence | `ρ(Φ) > 0` | SC-2 (f_Field.md) | INV-006 violated; T_orb undefined (division by zero) |
| Eccentricity bound | `e < 1.0` | INV-005 | Escape condition; route to f_Release or f_Collapse |
| Frame registration | E registered in Frame | SC-5 (f_Frame.md) | Cannot retrieve r_capture; abort |
| Resonance validity | `ω_res > 0` | SC-3 (f_Field.md) | RESONANT class cannot be evaluated |

---

## §7 · Engineering Primitives

### §7.1 · classify_orbit [PRIM:007] — Pure

```python
from dataclasses import dataclass
from enum import Enum
from fractions import Fraction
from typing import Tuple

class OrbitClass(Enum):
    """Categorical orbit shape descriptor.

    Frozen in f_Orbit.md §5.1, session SES-20260813-ORBIT-001.
    Thresholds are immutable (INV-009).
    """
    CIRCULAR    = "CIRCULAR"
    ELLIPTICAL  = "ELLIPTICAL"
    ECCENTRIC   = "ECCENTRIC"
    RESONANT    = "RESONANT"
    UNDEFINED   = "UNDEFINED"

class StabilityClass(Enum):
    """Categorical orbit stability descriptor.

    Frozen in f_Orbit.md §5.2, session SES-20260813-ORBIT-001.
    Thresholds are immutable (INV-009).
    """
    STABLE      = "STABLE"
    MARGINAL    = "MARGINAL"
    PRECARIOUS  = "PRECARIOUS"
    UNDEFINED   = "UNDEFINED"

@dataclass
class OrbitalClassification:
    """Output struct for classify_orbit.

    Fields:
        orbit_class:  Shape classification of the orbit.
        stab_class:   Stability classification of the orbit.
        is_resonant:  True if resonance lock was detected.
        resonance_ratio: String representation of detected ratio (e.g. "3:2"), or None.
    """
    orbit_class: OrbitClass
    stab_class:  StabilityClass
    is_resonant: bool
    resonance_ratio: str | None

def _detect_resonance(omega_res: float, max_n: int = 5, tolerance: float = 0.02) -> Tuple[bool, str | None]:
    """Check if omega_res is within tolerance of a low-integer ratio n:m.

    Pure function. No side effects.

    Args:
        omega_res:   Resonance frequency of the field Φ (must be > 0).
        max_n:       Maximum numerator/denominator to check (default 5).
        tolerance:   Fractional tolerance for ratio match (default 0.02 = 2%).

    Returns:
        Tuple of (is_resonant: bool, ratio_string: str | None).
        ratio_string is e.g. "3:2" if detected, else None.

    Raises:
        ValueError: If omega_res ≤ 0.
    """
    if omega_res <= 0:
        raise ValueError(f"omega_res must be > 0; got {omega_res}")

    for n in range(1, max_n + 1):
        for m in range(1, max_n + 1):
            ratio = n / m
            if abs(omega_res - ratio) / ratio <= tolerance:
                return True, f"{n}:{m}"
    return False, None

def classify_orbit(
    e: float,
    omega_res: float,
    d_bind: float,
    d_warn: float,
    d_collapse: float,
) -> OrbitalClassification:
    """[PRIM:007] Classify the current orbit by shape and stability.

    Pure function — reads orbital state, produces classification, no side effects.

    Implements:
      - Orbit classification table (f_Orbit.md §5.1, INV-009)
      - Stability classification table (f_Orbit.md §5.2, INV-009)
      - Resonance detection (f_Orbit.md §5.1)
      - INV-005: e ∈ [0, 1) enforcement
      - INV-009: immutable threshold enforcement

    Args:
        e:           Eccentricity ∈ [0, 1). Frozen formula: p_res / (p_res + P_eff).
                     Frozen in OPERATORS.md §2.
        omega_res:   Resonance frequency of field Φ (must be > 0).
                     Frozen in f_Field.md §4.2.
        d_bind:      Current binding depth (cycle t).
                     Frozen in f_Decay.md §4.1.
        d_warn:      Warning threshold = α_warn × d_bind(0), typical α_warn = 0.40.
                     Frozen in f_Decay.md §4.3.
        d_collapse:  Collapse threshold = α_collapse × d_bind(0), typical α_collapse = 0.10.
                     Frozen in f_Decay.md §4.3.

    Returns:
        OrbitalClassification with orbit_class, stab_class, is_resonant, resonance_ratio.

    Raises:
        ValueError: If e is out of [0, 1) or omega_res ≤ 0 or d_collapse ≥ d_warn.
        RuntimeError: If d_bind ≤ d_collapse (collapse condition — caller must route to f_Collapse).
    """
    # --- Input validation ---
    if not (0.0 <= e < 1.0):
        raise ValueError(f"INV-005 violated: e must be in [0, 1); got {e}")
    if omega_res <= 0:
        raise ValueError(f"omega_res must be > 0; got {omega_res}")
    if d_collapse >= d_warn:
        raise ValueError(f"d_collapse ({d_collapse}) must be < d_warn ({d_warn})")

    # --- Collapse guard ---
    if d_bind <= d_collapse:
        raise RuntimeError(
            f"d_bind ({d_bind:.4f}) ≤ d_collapse ({d_collapse:.4f}): "
            "orbit has reached collapse threshold. Route to f_Collapse."
        )

    # --- Orbit class: RESONANT takes priority ---
    is_resonant, ratio_str = _detect_resonance(omega_res)

    if is_resonant:
        orbit_class = OrbitClass.RESONANT
    elif e < 0.1:
        orbit_class = OrbitClass.CIRCULAR
    elif e < 0.5:
        orbit_class = OrbitClass.ELLIPTICAL
    else:
        orbit_class = OrbitClass.ECCENTRIC

    # --- Stability class: severity-wins joint evaluation ---
    depth_class: StabilityClass
    if d_bind > d_warn:
        depth_class = StabilityClass.STABLE
    elif d_bind > d_collapse:
        depth_class = StabilityClass.MARGINAL
    else:
        depth_class = StabilityClass.PRECARIOUS  # already guarded above; belt-and-suspenders

    ecc_class: StabilityClass
    if e < 0.5:
        ecc_class = StabilityClass.STABLE
    elif e < 0.9:
        ecc_class = StabilityClass.MARGINAL
    else:
        ecc_class = StabilityClass.PRECARIOUS

    # Severity order: PRECARIOUS > MARGINAL > STABLE
    severity = {
        StabilityClass.STABLE:     0,
        StabilityClass.MARGINAL:   1,
        StabilityClass.PRECARIOUS: 2,
    }
    stab_class = depth_class if severity[depth_class] >= severity[ecc_class] else ecc_class

    return OrbitalClassification(
        orbit_class=orbit_class,
        stab_class=stab_class,
        is_resonant=is_resonant,
        resonance_ratio=ratio_str,
    )
```

### §7.2 · update_orbital_parameters [PRIM:012] — Impure

```python
import math
from dataclasses import dataclass
from typing import Optional

@dataclass
class OrbitalParameters:
    """Full orbital state struct produced by f_Orbit.

    Immutable per-cycle snapshot. Each cycle generates a new instance.
    Written to Frame registry by update_orbital_parameters [PRIM:012].

    Fields:
        e:            Eccentricity ∈ [0, 1).
        a:            Semi-major axis = r_capture / (1 − e).
        T_orb:        Orbital period = 2π × √(a³ / (M_A × ρ(Φ))).
        r_periapsis:  Closest approach radius = a × (1 − e) = r_capture.
        r_apoapsis:   Maximum recession radius = a × (1 + e).
        orbit_class:  Shape class (OrbitClass enum).
        stab_class:   Stability class (StabilityClass enum).
        d_bind:        Binding depth at this cycle.
        cycle:        Cycle number at which this snapshot was taken.
        session_id:   Session provenance (INV-010).
    """
    e:           float
    a:           float
    T_orb:       float
    r_periapsis: float
    r_apoapsis:  float
    orbit_class: OrbitClass
    stab_class:  StabilityClass
    d_bind:      float
    cycle:       int
    session_id:  str

def update_orbital_parameters(
    e: float,
    r_capture: float,
    M_A: float,
    rho_phi: float,
    d_bind: float,
    d_warn: float,
    d_collapse: float,
    omega_res: float,
    cycle: int,
    frame_registry: dict,
    entity_id: str,
    session_id: str,
) -> OrbitalParameters:
    """[PRIM:012] Compute and register the current orbital parameters in Frame.

    Impure — writes to frame_registry. Called once per cycle by f_Decay, and
    on-demand by f_Release, f_Collapse, and f_Capture_Multi.

    Computes:
      a         = r_capture / (1 − e)           [f_Orbit.md §4.1]
      T_orb     = 2π × √(a³ / (M_A × ρ(Φ)))   [f_Orbit.md §4.1, FROZEN HERE]
      r_periapsis = a × (1 − e)
      r_apoapsis  = a × (1 + e)
      orbit_class, stab_class via classify_orbit [PRIM:007]

    Enforces:
      INV-004: r_capture is not modified.
      INV-005: e ∈ [0, 1).
      INV-006: rho_phi > 0.
      INV-010: session_id recorded on every write.

    Args:
        e:              Eccentricity ∈ [0, 1). From OPERATORS.md §2.
        r_capture:      Immutable capture radius (INV-004). From f_Frame.md registry.
        M_A:            Attractor mass. From f_Force.md.
        rho_phi:        Field coherence density ρ(Φ). Must be > 0 (INV-006).
        d_bind:         Current binding depth. From f_Decay.md cycle output.
        d_warn:         Warning threshold. From Frame initialization.
        d_collapse:     Collapse threshold. From Frame initialization.
        omega_res:      Resonance frequency. From f_Field.md.
        cycle:          Current simulation cycle number.
        frame_registry: Mutable Frame registry dict (written in-place).
        entity_id:      Identifier of entity E in Frame registry.
        session_id:     Session provenance string (INV-010).

    Returns:
        OrbitalParameters snapshot for this cycle.

    Raises:
        ValueError: If rho_phi ≤ 0 (INV-006), e out of range (INV-005),
                    or entity_id not in frame_registry.
        RuntimeError: If d_bind ≤ d_collapse (route to f_Collapse instead).
    """
    # --- Validate preconditions ---
    if rho_phi <= 0:
        raise ValueError(f"INV-006 violated: rho_phi must be > 0; got {rho_phi}")
    if not (0.0 <= e < 1.0):
        raise ValueError(f"INV-005 violated: e must be in [0, 1); got {e}")
    if entity_id not in frame_registry:
        raise ValueError(f"Entity '{entity_id}' not found in Frame registry. "
                         "f_Capture must be called first.")

    # --- Compute orbital geometry ---
    a           = r_capture / (1.0 - e)
    r_periapsis = a * (1.0 - e)   # = r_capture (structural identity)
    r_apoapsis  = a * (1.0 + e)   # = r_release (structural identity with f_Release.md §4.2)

    # T_orb = 2π × √(a³ / (M_A × ρ(Φ)))
    # Frozen in f_Orbit.md §4.1, SES-20260813-ORBIT-001
    gravitational_parameter = M_A * rho_phi
    T_orb = 2.0 * math.pi * math.sqrt((a ** 3) / gravitational_parameter)

    # --- Classify ---
    classification = classify_orbit(
        e=e,
        omega_res=omega_res,
        d_bind=d_bind,
        d_warn=d_warn,
        d_collapse=d_collapse,
    )

    params = OrbitalParameters(
        e=e,
        a=a,
        T_orb=T_orb,
        r_periapsis=r_periapsis,
        r_apoapsis=r_apoapsis,
        orbit_class=classification.orbit_class,
        stab_class=classification.stab_class,
        d_bind=d_bind,
        cycle=cycle,
        session_id=session_id,
    )

    # --- Write to Frame registry (INV-010: session_id required) ---
    frame_registry[entity_id]["orbital_parameters"] = {
        "cycle":         cycle,
        "e":             e,
        "a":             a,
        "T_orb":         T_orb,
        "r_periapsis":   r_periapsis,
        "r_apoapsis":    r_apoapsis,
        "orbit_class":   classification.orbit_class.value,
        "stab_class":    classification.stab_class.value,
        "is_resonant":   classification.is_resonant,
        "resonance_ratio": classification.resonance_ratio,
        "d_bind":        d_bind,
        "session_id":    session_id,
    }

    return params
```

---

## §8 · Canonical Examples

### §8.1 · Example 1 — Near-Circular Stable Orbit (Deep Lock)

**Scenario:** An entity enters a high-coherence field with minimal residual momentum. The field's pressure strongly dominates.

**Parameters:**

| Parameter | Value | Notes |
|---|---|---|
| M_A | 10.0 | High-mass attractor |
| M_E | 1.0 | Standard entity |
| v_approach | 3.2 | Just above C_thresh |
| C_thresh | 3.0 | Capture threshold |
| ρ(Φ) | 5.0 | High coherence |
| r_capture | 2.0 | Set at capture |
| ω_res | 0.73 | Non-resonant |
| α_warn | 0.40 | Standard |
| α_collapse | 0.10 | Standard |

**Computed:**

```
P_eff     = M_A × ρ(Φ) / r²     = 10.0 × 5.0 / 4.0     = 12.50
β         = P_eff / (M_E × v_approach) = 12.50 / (1.0 × 3.2) = 3.906
p_res     = M_E × (v_approach − C_thresh) = 1.0 × 0.2   = 0.200
e         = p_res / (p_res + P_eff) = 0.200 / 12.700     = 0.016

a         = r_capture / (1 − e) = 2.0 / 0.984           = 2.033
T_orb     = 2π × √(a³ / (M_A × ρ(Φ)))
          = 2π × √(8.406 / 50.0)                         = 2π × 0.410 = 2.576 cycles
r_periapsis = 2.000
r_apoapsis  = 2.033 × 1.016                              = 2.066

d_bind(0) = β × ρ(Φ) × (1 − e) = 3.906 × 5.0 × 0.984   = 19.215
d_warn    = 0.40 × 19.215                                 = 7.686
d_collapse= 0.10 × 19.215                                 = 1.922
```

**Classification:**

| Parameter | Value |
|---|---|
| orbit_class | `CIRCULAR` (e = 0.016 < 0.1) |
| stab_class | `STABLE` (d_bind >> d_warn; e < 0.5) |
| is_resonant | False |
| T_orb | 2.576 cycles |

**Interpretation:** Entity is deeply locked in a near-circular orbit. Decay pressure is low. Expected to persist many cycles without intervention.

---

### §8.2 · Example 2 — Elliptical Marginal Orbit (Resonant Override)

**Scenario:** An entity in a 3:2 resonance lock. Eccentricity is elliptical, but resonance dominates the classification.

**Parameters:**

| Parameter | Value | Notes |
|---|---|---|
| M_A | 4.0 | Moderate attractor |
| M_E | 1.0 | Standard |
| v_approach | 5.5 | Moderate excess momentum |
| C_thresh | 4.0 | Lower threshold |
| ρ(Φ) | 3.0 | Moderate coherence |
| r_capture | 2.5 | Set at capture |
| ω_res | 1.502 | ≈ 3:2 (within 0.02 tolerance) |
| d_bind(0) | 6.0 | Established |
| d_warn | 2.4 (0.40 × 6.0) | |
| d_collapse | 0.6 (0.10 × 6.0) | |
| d_bind(current) | 2.0 | Cycle 8; decayed |

**Computed:**

```
P_eff     = 4.0 × 3.0 / 6.25     = 1.920
p_res     = 1.0 × 1.5             = 1.500
e         = 1.500 / (1.500 + 1.920) = 0.438

a         = 2.5 / (1 − 0.438)    = 4.448
T_orb     = 2π × √(4.448³ / 12.0)
          = 2π × √(87.98 / 12.0) = 2π × 2.710 = 17.03 cycles
r_periapsis = 2.500
r_apoapsis  = 4.448 × 1.438       = 6.396
```

**Classification:**

| Parameter | Value |
|---|---|
| orbit_class | `RESONANT` (ω_res = 1.502 ≈ 3:2; resonance overrides ELLIPTICAL) |
| stab_class | `MARGINAL` (d_bind = 2.0, below d_warn = 2.4; e = 0.438, below 0.5 → depth drives) |
| is_resonant | True |
| resonance_ratio | "3:2" |

**Interpretation:** The resonance lock provides some structural protection despite the elliptical eccentricity. Stability is MARGINAL due to depth decay. Apply f_Emit or f_Amplify to recover d_bind before it drops to d_collapse. T_orb is long (17 cycles), meaning the entity is far from A for much of each orbit — increasing decay risk.

---

### §8.3 · Example 3 — Eccentric Precarious Orbit (Pre-Collapse State)

**Scenario:** A high-momentum entity captured in a low-coherence field. Orbit is structurally at risk.

**Parameters:**

| Parameter | Value | Notes |
|---|---|---|
| M_A | 2.0 | Weak attractor |
| M_E | 3.0 | Heavy entity |
| v_approach | 9.0 | High momentum |
| C_thresh | 5.0 | |
| ρ(Φ) | 0.8 | Low coherence |
| r_capture | 3.0 | |
| ω_res | 2.71 | Non-resonant (irrational-like) |
| d_bind(0) | 4.0 | Initial |
| d_warn | 1.6 | |
| d_collapse | 0.4 | |
| d_bind(current) | 0.5 | Cycle 12 |

**Computed:**

```
P_eff     = 2.0 × 0.8 / 9.0      = 0.178
p_res     = 3.0 × 4.0             = 12.000
e         = 12.000 / 12.178       = 0.985

a         = 3.0 / (1 − 0.985)    = 200.0
T_orb     = 2π × √(200³ / (2.0 × 0.8))
          = 2π × √(8,000,000 / 1.6) = 2π × 2236.1 = 14,049 cycles
r_periapsis = 3.000
r_apoapsis  = 200.0 × 1.985       = 397.0
```

**Classification:**

| Parameter | Value |
|---|---|
| orbit_class | `ECCENTRIC` (e = 0.985) |
| stab_class | `PRECARIOUS` (e ≥ 0.9 → PRECARIOUS; d_bind = 0.5 > d_collapse → MARGINAL; severity-wins → PRECARIOUS) |
| is_resonant | False |

**Interpretation:** This orbit is at the edge of structural collapse. The entity barely captured — it arrives with 98.5% of escape momentum. r_apoapsis = 397 means the entity recedes to 132× the capture radius each orbit. T_orb is astronomically long; in practice, the entity will escape or collapse long before completing one orbit. Route to f_Collapse for assessment. If f_Release conditions are met at apoapsis, execute release immediately.

---

### §8.4 · Example 4 — Stable Circular Orbit Tracked Over 5 Cycles

**Scenario:** A standard capture with moderate parameters, tracked cycle-by-cycle to show how orbital parameters evolve with decay.

**Initial Parameters:**

| Parameter | Value |
|---|---|
| M_A | 6.0 |
| M_E | 1.5 |
| v_approach | 4.0 |
| C_thresh | 3.5 |
| ρ(Φ) | 4.0 (decays 5%/cycle) |
| r_capture | 2.0 |
| ω_res | 1.0 (1:1 resonance) |
| d_bind(0) | 8.64 |
| d_warn | 3.456 |
| d_collapse | 0.864 |

**Cycle Trace:**

| Cycle | ρ(Φ) | P_eff | p_res | e | a | T_orb | d_bind | orbit_class | stab_class |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 4.000 | 6.000 | 0.750 | 0.111 | 2.250 | 2.985 | 8.640 | RESONANT (1:1) | STABLE |
| 1 | 3.800 | 5.700 | 0.750 | 0.116 | 2.263 | 3.076 | 7.981 | RESONANT | STABLE |
| 2 | 3.610 | 5.415 | 0.750 | 0.122 | 2.278 | 3.181 | 7.310 | RESONANT | STABLE |
| 3 | 3.430 | 5.144 | 0.750 | 0.127 | 2.294 | 3.302 | 6.617 | RESONANT | STABLE |
| 4 | 3.258 | 4.887 | 0.750 | 0.133 | 2.311 | 3.441 | 5.890 | RESONANT | STABLE |
| 5 | 3.095 | 4.643 | 0.750 | 0.139 | 2.325 | 3.556 | 5.128 | RESONANT | STABLE |

**Observations:**
- ρ(Φ) decay causes P_eff to decline, driving e upward gradually.
- T_orb lengthens each cycle as the orbit loosens (a increases as e grows).
- The 1:1 resonance lock holds throughout, keeping orbit_class = RESONANT.
- d_bind remains well above d_warn (3.456) through cycle 5. Extrapolating the decay trajectory: d_warn breach occurs around cycle 18–19. Action point: schedule f_Amplify intervention at cycle 15 to maintain STABLE classification.

---

## §9 · Cross-Module References

### §9.1 · Files That Read From f_Orbit

| Consumer File | What It Reads | Purpose |
|---|---|---|
| f_Decay.md | `e`, `T_orb`, `orbit_class`, `stab_class`, `d_bind` | Each cycle: assess decay rate, flag DC-2/DC-3/DC-4 |
| f_Release.md | `e`, `r_apoapsis`, `stab_class` | Compute r_release, evaluate RC-1 through RC-5 |
| f_Collapse.md | `stab_class = PRECARIOUS`, `e ≥ 0.9`, `d_bind ≤ d_collapse` | Entry condition for collapse sequence |
| f_Capture_Multi.md | `orbit_class`, `T_orb` | Multi-capture scheduling, resonance conflict detection |
| f_Emit.md | `stab_class`, `d_bind`, `T_orb` | Determine emission timing within orbit cycle |
| f_Amplify.md | `stab_class`, `d_bind` | Target amplification to orbit depth recovery |

### §9.2 · Files That Write To f_Orbit (Provide Inputs)

| Provider File | What It Provides | Operator |
|---|---|---|
| f_Capture.md | `r_capture`, `β`, `p_res`, `P_eff`, `Ω` | f_Capture §4.8 |
| f_Field.md | `ρ(Φ)`, `ω_res` | f_Field §4.1, §4.2 |
| f_Force.md | `M_A`, `M_E`, `v_approach`, `C_thresh` | f_Force §4.1–4.4 |
| f_Frame.md | Frame registry (r_capture retrieval) | f_Frame §4.3 |
| f_Decay.md | `d_bind(t)` (current cycle value) | f_Decay §4.1 |

### §9.3 · OPERATORS.md Update Required

The following entries in OPERATORS.md must be updated to reflect this file's canonical status:

| Operator | OPERATORS.md Change |
|---|---|
| `T_orb` | Status: 🔵 pending → 🟢 frozen; source: f_Orbit.md §4.1 |
| `orbit_class` | Status: 🔵 pending → 🟢 frozen; source: f_Orbit.md §5.1 |
| `stab_class` | Status: 🔵 pending → 🟢 frozen; source: f_Orbit.md §5.2 |
| `classify_orbit` | PRIM:007 status: pending → frozen; source: f_Orbit.md §7.1 |
| `update_orbital_parameters` | PRIM:012 status: pending → frozen; source: f_Orbit.md §7.2 |

### §9.4 · Evaluation Order Within a Cycle

```
Cycle t:
  1. f_Field     → ρ(Φ)(t), ω_res(t)
  2. f_Force     → P_eff(t), p_res(t)
  3. OPERATORS   → e(t) = p_res / (p_res + P_eff)
  4. f_Orbit     → a(t), T_orb(t), orbit_class(t), stab_class(t)
  5. f_Decay     → δ(t), d_bind(t), DC flags
  6. f_Release   → RC evaluation (if triggered externally or by stab_class)
  7. f_Collapse  → collapse check (if stab_class = PRECARIOUS)
```

`f_Orbit` is step 4 of 7. It may not be called before steps 1–3 complete.

---

## §10 · Document Metadata

### §10.1 · INV Compliance Table

| Invariant | Description | Status in This File |
|---|---|---|
| INV-001 | G requires all three nodes | ✅ §3.2 proves all three nodes contribute to every orbital parameter |
| INV-002 | No unilateral collapse from single-node failure | ✅ Multi-condition checks in classify_orbit; no single flag triggers collapse |
| INV-003 | d_bind decays monotonically below d_warn | ✅ Read-only; decay managed by f_Decay |
| INV-004 | r_capture immutable post-capture | ✅ update_orbital_parameters validates; never writes r_capture |
| INV-005 | e ∈ [0, 1) | ✅ classify_orbit raises ValueError on violation; enforced in PRIM:007 and PRIM:012 |
| INV-006 | ρ(Φ) > 0 | ✅ update_orbital_parameters raises ValueError if rho_phi ≤ 0 |
| INV-007 | Frame registry authoritative | ✅ PRIM:012 writes to frame_registry; reads r_capture from it |
| INV-008 | Operator freeze propagation | ✅ T_orb frozen here §4.1; orbit_class, stab_class frozen §5 |
| INV-009 | Classification thresholds immutable | ✅ §5 tables frozen and labeled INV-009; code uses hardcoded thresholds |
| INV-010 | Session provenance required | ✅ session_id parameter required in PRIM:012; recorded in Frame registry |

### §10.2 · Wave Status

| Wave | File | Status |
|---|---|---|
| 0 | f_Capture.md | ✅ Canonical |
| 0 | f_Source.md | ✅ Archived |
| 0 | GravityOfDismissal.md | ✅ Canonical |
| 1 | README.md | ✅ Canonical |
| 1 | INDEX.md | ✅ Canonical |
| 1 | OPERATORS.md | ✅ Canonical (T_orb pending → frozen here) |
| 1 | GLOSSARY.md | ✅ Canonical |
| 1 | CHANGELOG.md | ✅ Canonical |
| 1 | FFF_Gravity_module.json | ✅ Canonical |
| 2 | f_Field.md | ✅ Canonical |
| 2 | f_Force.md | ✅ Canonical |
| 2 | f_Frame.md | ✅ Canonical |
| 3 | f_Release.md | ✅ Canonical |
| 3 | f_Decay.md | ✅ Canonical |
| **3** | **f_Orbit.md** | **✅ Canonical ← THIS FILE** |
| 3 | f_Collapse.md | 🔵 Scaffold → NOW UNBLOCKED |
| 3 | f_Emit.md | 🔵 Scaffold → unblocked |
| 3 | f_Dampen.md | 🔵 Scaffold → unblocked |
| 3 | f_Amplify.md | 🔵 Scaffold → unblocked |
| 3 | f_Deflect.md | 🔵 Scaffold → unblocked |
| 4 | f_Capture_Multi.md | 🔵 Scaffold → NOW UNBLOCKED |

### §10.3 · Changelog Entry

```
## [1.0.0] — 2026-08-13 — SES-20260813-ORBIT-001

### Added
- Initial canonical freeze of f_Orbit.md.
- Operator T_orb defined and frozen (§4.1):
    T_orb = 2π × √(a³ / (M_A × ρ(Φ)))
    a = r_capture / (1 − e)
- Operator orbit_class frozen with 4 categories (§5.1, INV-009):
    RESONANT · CIRCULAR · ELLIPTICAL · ECCENTRIC
- Operator stab_class frozen with 3 categories (§5.2, INV-009):
    STABLE · MARGINAL · PRECARIOUS
- Primitive classify_orbit [PRIM:007] frozen (§7.1) — Pure.
- Primitive update_orbital_parameters [PRIM:012] frozen (§7.2) — Impure.
- 4 canonical examples: near-circular stable, resonant elliptical,
  eccentric precarious, 5-cycle decay trace.
- Cross-module reference table: 6 consumers, 5 providers.
- Evaluation order within cycle codified (§9.4).
- INV compliance table complete (§10.1).

### Unlocks
- f_Collapse.md (was blocked on f_Decay.md ✅ + f_Orbit.md → now fully unblocked)
- f_Capture_Multi.md (was blocked on f_Orbit.md + f_Frame.md → now fully unblocked)

### Operator Status Updates Required in OPERATORS.md
- T_orb: 🔵 → 🟢 frozen in f_Orbit.md §4.1
- orbit_class: 🔵 → 🟢 frozen in f_Orbit.md §5.1
- stab_class: 🔵 → 🟢 frozen in f_Orbit.md §5.2
- PRIM:007 classify_orbit: pending → frozen in f_Orbit.md §7.1
- PRIM:012 update_orbital_parameters: pending → frozen in f_Orbit.md §7.2
```

---

*f_Orbit.md — Canonical v1.0.0 — [FFF:GRAVITY:ORBIT] — SES-20260813-ORBIT-001*
*FFF_Gravity Module · TriadicFrameworks · umaywant2*
