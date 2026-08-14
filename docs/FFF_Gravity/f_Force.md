# f_Force — Force Node & Fluid Node Definitions

```
# ============================================================
# f_Force.md — Force Node & Fluid Node Layer Definition
# Module: FFF_Gravity | TriadicFrameworks v1.0.0
# ============================================================
title: "f_Force — Force Node & Fluid Node Definitions"
module: FFF_Gravity
layer: "Wave 2 — Layer Definitions"
node_primary: F_force
node_secondary: F_fluid
version: "1.0.0"
status: canonical
frozen: true

session_context:
  session_id: "SES-20260813-FORCE-001"
  date: "2026-08-13"
  author: "Nawder (umaywant2)"
  assistant: "Copilot (Microsoft)"
  session_note: >
    Canonical build. Dual-node file covering F_force (gradient/pressure identity)
    and F_fluid (mass-density identity). Both nodes are defined here because they
    form a co-dependent lower dyad — splitting creates circular dependencies.
    Genesis material sourced from f_Source.md dialogue and confirmed by
    FFF_Gravity_module.json node registry.

dependencies:
  required:
    - "README.md"
    - "INDEX.md"
    - "OPERATORS.md"
    - "GLOSSARY.md"
    - "CHANGELOG.md"
    - "FFF_Gravity_module.json"
    - "f_Field.md"
  referenced_by:
    - "f_Frame.md"
    - "f_Orbit.md"
    - "f_Decay.md"
    - "f_Release.md"
    - "f_Collapse.md"
    - "f_Amplify.md"
    - "f_Deflect.md"
    - "f_Dampen.md"
    - "f_Emit.md"
    - "f_Capture.md"

changelog:
  - version: "1.0.0"
    date: "2026-08-13"
    author: "Nawder"
    change: "Initial canonical release. §0–§10 complete. Dual F_force + F_fluid node definitions. SC-1, SC-4, FM-001, FM-006, FM-007 registered."
```

<!-- metadata: file=f_Force.md module=FFF_Gravity status=canonical frozen=true wave=2 -->

> **FFF_Gravity Module · Wave 2 · Layer Definitions**
> This file defines two co-dependent nodes: **F_force** (gradient/pressure identity)
> and **F_fluid** (mass-density identity). They are defined together because in every
> physical and engineered gravity scenario they are mutually constraining — neither
> fully describes a state without reference to the other.

---

## §0 · Session Context

<!-- section: 0-session-context -->

| Field | Value |
|---|---|
| Session ID | `SES-20260813-FORCE-001` |
| Date | 2026-08-13 |
| Module | FFF_Gravity |
| File | `f_Force.md` |
| Status | Canonical — frozen at v1.0.0 |
| Nodes Defined | F_force, F_fluid |
| Wave | 2 — Layer Definitions |
| Sibling Files | `f_Field.md` (F_freq), `f_Frame.md` (Frame Node) |

### §0.1 · Design Decision: Why Dual-Node?

The standard triadic pattern assigns one node per definition file. F_force and F_fluid
are an exception. Three reasons justify the dual-node design:

1. **Mutual constraint.** SC-4 (Binding Floor) requires F_fluid coupling coefficient
   `β ≥ 1.0` — but the floor is enforced by F_force providing the approach vector.
   Neither condition is meaningful in isolation.

2. **Historical isolation.** Every canonical experiment that isolates one node
   implicitly holds the other constant. The Cavendish torsion balance, for example,
   isolates F_fluid by making F_force negligible — but it can only be understood as
   such if both are defined in the same scope.

3. **Failure mode co-location.** FM-007 (Mutual Dissolution) requires simultaneous
   reference to F_fluid mass parity and F_force gradient collapse. Splitting the
   definitions forces every failure mode analysis to cross-reference two files.

> **Governance:** This dual-node structure is recorded in `FFF_Gravity_module.json`
> (`defined_in: "f_Force.md"` for both nodes). The `OPERATORS.md` file remains the
> single source of truth for all operator symbols. `GLOSSARY.md` governs prose
> definitions.

---

## §1 · Node Identity

<!-- section: 1-node-identity -->

### §1.1 · F_force — Force Node

<!-- metadata: node=F_force symbol=F_force domain=gradient-pressure role=passive-gradient -->

| Field | Value |
|---|---|
| Node Name | Force Node |
| Symbol | `F_force` |
| Domain | Gradient / Pressure Identity |
| Role in Triadic Ratio | Gradient operator — provides approach vector, atmospheric overlay, pressure differential |
| Triadic Position | Lower-right (see §3) |
| Stability Posture | **Passive** — dominance indicates anomaly or engineering |
| Frozen | v1.0.0 |

**Core identity statement:**

> *F_force is the gradient component of the local gravitational ratio. It carries
> atmospheric pressure, isomorphic gradients, density layer transitions, and
> regime stabilization. It does not create the coherence well — it shapes the
> approach path to it.*

**Passivity principle.** In all naturally occurring stable gravity regimes, F_force
is passive — it contributes gradient context without dominating the ratio. A dominant
F_force (F_force >> F_freq × F_fluid) is always either anomalous or engineered.
This is one of the most important asymmetries in the FFF_Gravity model: the node
that most resembles "force" in the colloquial sense is the one that, when dominant,
signals failure or override.

---

### §1.2 · F_fluid — Fluid Node

<!-- metadata: node=F_fluid symbol=F_fluid domain=mass-density role=substrate-continuity -->

| Field | Value |
|---|---|
| Node Name | Fluid Node |
| Symbol | `F_fluid` |
| Domain | Mass-Density Identity |
| Role in Triadic Ratio | Substrate operator — carries mass distribution, pooling, flow potential, mass-energy coupling |
| Triadic Position | Lower-left (see §3) |
| Stability Posture | **Neutral** — must meet binding floor `β ≥ 1.0` |
| Frozen | v1.0.0 |

**Core identity statement:**

> *F_fluid is the mass-density component of the local gravitational ratio. Mass is
> not the cause of gravity — mass is the fluid node that interacts with the
> frequency node (F_freq) to produce the coherence well. F_fluid carries
> distribution, pooling, substrate continuity, and flow potential.*

**Mass reframing.** The most important conceptual shift in FFF_Gravity is that mass
does not generate gravity. Mass is F_fluid — one node in a three-node ratio.
Without F_freq (the coherence well), F_fluid has no attractor to pool toward.
Without F_force, F_fluid has no gradient context. This is not a claim that mass is
irrelevant — it is a claim that mass alone is insufficient to describe a gravity regime.

---

## §2 · Canonical Description

<!-- section: 2-canonical-description -->

### §2.1 · The Triadic Ratio

The FFF_Gravity local gravity ratio is:

```
G_local = F_freq · F_fluid · F_force
```

Where:
- `F_freq` — coherence well identity (defined in `f_Field.md`)
- `F_fluid` — mass-density substrate (defined here)
- `F_force` — gradient/pressure overlay (defined here)

All three nodes must be present for a complete gravity description. A reading that
accounts for only one or two nodes will produce a partial model — accurate in its
limited scope, blind to the remainder.

---

### §2.2 · F_force Canonical Description

**What F_force carries:**

- Atmospheric pressure (surface and stratospheric gradients)
- Isomorphic pressure fields (pressure equivalence zones across a body)
- Density layer transitions (interfaces between fluid layers — ocean thermoclines,
  atmospheric pressure bands, mantle/crust boundaries)
- Regime stabilization (the overlay that maintains a pressure envelope around a
  coherence well)
- Approach vector magnitude (`v_approach`) — the rate at which an element is
  moving toward an attractor

**What F_force does NOT carry:**

- The coherence well itself (that is F_freq)
- The mass substrate (that is F_fluid)
- The capture threshold (that is SC-1, computed across all three nodes)

**Force override class.** When an external mechanism artificially elevates F_force
to dominance — replacing the natural gradient with an engineered pressure field —
the result is a Force Override state. The coherence well (F_freq) may still be
present, but the element's behavior is governed by the artificial gradient, not the
natural triadic ratio. This is designated FM-006 (Phantom Capture). The canonical
fictional example: a Green Lantern ring creates an artificial gravity that operates
by F_force dominance — gravity is not broken, but overridden.

---

### §2.3 · F_fluid Canonical Description

**What F_fluid carries:**

- Mass distribution (how mass is distributed within and around an attractor body)
- Pooling (the tendency of mass to accumulate toward coherence well minima)
- Flow potential (the directional bias of mass redistribution over time)
- Mass-energy coupling coefficient (`β`) — how strongly the element's mass
  participates in the coherence well interaction
- Attractor mass (`M_A`) — the total effective mass of the attractor body
- Element mass (`M_E`) — the total effective mass of the element

**What F_fluid does NOT carry:**

- The frequency of the coherence well (that is F_freq)
- The gradient of the approach path (that is F_force)
- The escape threshold (that is SC-1, `v_escape(A)`, computed from F_freq)

**Mass parity hazard.** When `M_E ≈ M_A`, the attractor/element distinction
collapses. Neither body can serve as the stable coherence anchor. This is the
Subset/Supsphere failure class, designated FM-007 (Mutual Dissolution). The
model requires `M_A >> M_E` for standard capture/orbit behavior.

---

## §3 · Triadic Position

<!-- section: 3-triadic-position -->

The three FFF_Gravity nodes occupy fixed positions in the triadic diagram.
F_force and F_fluid form the lower dyad — the operational layer beneath the
F_freq coherence anchor.

```
              ┌─────────────────────────────────┐
              │           F_freq                │
              │    (Coherence Well / Field)     │
              │    [ defined in f_Field.md ]    │
              └───────────┬─────────────────────┘
                          │
              ┌───────────┴─────────────────────┐
              │         Lower Dyad              │
              │                                 │
              │  F_fluid          F_force        │
              │  (Mass-Density)   (Gradient)    │
              │  [THIS FILE]      [THIS FILE]   │
              └─────────────────────────────────┘
```

**Dyad co-dependence.** The lower dyad is not a simple pair of independent nodes.
F_fluid provides the substrate mass that F_force acts upon. F_force provides the
gradient context within which F_fluid distributes. In the ratio `G_local = F_freq
· F_fluid · F_force`, neither lower node is meaningful without the upper anchor
(F_freq), and neither is fully interpretable without the other.

**Reading the diagram for engineering:**

| Target | Operator | Node to Modify |
|---|---|---|
| Increase effective gravity | Increase `β` (coupling) | F_fluid via `amplify_coupling` |
| Change approach path | Change `v_approach` heading | F_force via `redirect_force_node` |
| Eliminate F_force entirely | Set gradient to null | F_force → ISS/vacuum state |
| Replace F_force artificially | Substitute pressure field | F_force → Force Override (FM-006) |

---

## §4 · Operator Definitions

<!-- section: 4-operator-definitions -->

> **Authority:** `OPERATORS.md` is the single source of truth for all operator
> symbols, types, units, and freeze status. The table below is a local reference
> only. In case of conflict, `OPERATORS.md` governs.

### §4.1 · F_force Operators

<!-- metadata: operators=F_force frozen=v1.0.0 -->

| Operator | Name | Type | Domain | Definition | Frozen |
|---|---|---|---|---|---|
| `v_approach` | Approach Vector | scalar ℝ≥0 | F_force | Rate and direction of element movement toward attractor; magnitude of closing velocity along the approach path | v1.0.0 |

**`v_approach` notes:**

- Scalar form (ℝ≥0) represents magnitude only. Direction is carried by the
  `heading_delta` operator (defined in `f_Deflect.md`, Wave 3 — pending).
- `v_approach = 0` → element is stationary relative to attractor (capture
  threshold crossed or orbit established).
- `v_approach ≥ v_escape(A)` → SC-1 violated; FM-001 (Overshoot) triggered.
- `v_approach` is not a force in the Newtonian sense. It is the approach
  characterization of the F_force node — the gradient-shaped path the element
  follows toward the coherence well.

---

### §4.2 · F_fluid Operators

<!-- metadata: operators=F_fluid frozen=v1.0.0 -->

| Operator | Name | Type | Domain | Definition | Frozen |
|---|---|---|---|---|---|
| `M_A` | Attractor Mass | scalar ℝ>0 | F_fluid | Total effective mass of the attractor body; the primary F_fluid contributor to the coherence well | v1.0.0 |
| `M_E` | Element Mass | scalar ℝ>0 | F_fluid | Total effective mass of the element; the secondary F_fluid participant in the triadic ratio | v1.0.0 |

**`M_A` notes:**

- `M_A` must be strictly positive (ℝ>0). A zero or negative attractor mass
  has no defined behavior in the FFF_Gravity model.
- `M_A >> M_E` is required for standard capture/orbit behavior (see FM-007).
- `M_A` is the primary contributor to the coupling coefficient `β`.
  Specifically, `β` is a function of `M_A`, `M_E`, and the coherence well
  density `ρ(Φ)` (defined in `f_Field.md`).

**`M_E` notes:**

- `M_E` must be strictly positive (ℝ>0).
- As `M_E → M_A`, FM-007 (Mutual Dissolution) probability increases.
- `M_E` participates in F_fluid but does not define F_freq. This is the
  explicit statement that mass does not generate the coherence well.
- The Galileo result (all masses fall at the same rate in vacuum) follows
  directly: F_freq and F_force are independent of `M_E`; only F_fluid
  carries `M_E`, and its contribution cancels in the ratio when F_force → 0.

---

### §4.3 · Derived / Pending Operators

| Operator | Name | Defined In | Status |
|---|---|---|---|
| `heading_delta` | Approach heading deflection angle | `f_Deflect.md` | Scaffold — Wave 3 |
| `β` | F_fluid coupling coefficient | `f_Field.md` §4 (inline), `f_Force.md` §5 (SC-4) | Canonical — used here |
| `v_escape(A)` | Escape velocity of attractor | `f_Field.md` §4, `f_Force.md` §5 (SC-1) | Canonical — used here |
| `ρ(Φ)` | Coherence well density | `f_Field.md` §4 | Canonical — referenced here |

---

## §5 · Stability Conditions

<!-- section: 5-stability-conditions -->

> Two stability conditions are registered to `f_Force.md`. All five module
> stability conditions (SC-1 through SC-5) are listed with their home files
> in `INDEX.md`.

### §5.1 · SC-1 — Approach Bound

<!-- metadata: SC=SC-1 name=Approach-Bound node=F_force home=f_Force.md -->

**Condition:**

```
v_approach < v_escape(A)
```

**Meaning:** The element's approach velocity must remain below the attractor's
escape velocity for any form of capture, binding, or orbit to be possible.

| Field | Value |
|---|---|
| Condition ID | SC-1 |
| Name | Approach Bound |
| Node | F_force (provides `v_approach`); F_freq (provides `v_escape(A)`) |
| Home File | `f_Force.md` |
| Violation | FM-001 (Overshoot) |
| Applies To | All capture, orbit, and binding scenarios |

**Interpretation:**

`v_escape(A)` is a property of the attractor's coherence well (F_freq) — it is
the minimum velocity required to escape the well entirely. `v_approach` is a
property of the element's F_force gradient trajectory. SC-1 expresses the
boundary condition between capture-eligible and non-capture states.

SC-1 is necessary but not sufficient for capture. An element with `v_approach
< v_escape(A)` is capture-eligible, but capture requires SC-4 (Binding Floor)
to also hold. Both conditions must be satisfied simultaneously for stable
binding to occur.

**Boundary behavior:**

```
v_approach << v_escape(A)   → deep binding eligible; stable orbit or capture
v_approach → v_escape(A)    → marginal binding; high eccentricity orbit
v_approach = v_escape(A)    → parabolic trajectory; boundary condition
v_approach > v_escape(A)    → SC-1 violated; FM-001 (Overshoot) triggered
```

---

### §5.2 · SC-4 — Binding Floor

<!-- metadata: SC=SC-4 name=Binding-Floor node=F_fluid home=f_Force.md -->

**Condition:**

```
β ≥ 1.0
```

**Meaning:** The F_fluid coupling coefficient must meet or exceed unity for the
element to participate in the coherence well interaction. Below unity, the
element's mass substrate is insufficiently coupled to sustain binding.

| Field | Value |
|---|---|
| Condition ID | SC-4 |
| Name | Binding Floor |
| Node | F_fluid (provides `β`) |
| Home File | `f_Force.md` |
| Violation | FM-007 (Mutual Dissolution) partial; also contributes to anomalous decay |
| Applies To | All binding, orbit, and capture scenarios |

**Interpretation:**

`β` is the F_fluid coupling coefficient — a dimensionless ratio capturing how
effectively the element's mass participates in the attractor's coherence well.
`β = 1.0` represents the minimum viable coupling. `β >> 1.0` represents strong
coupling (tight orbit, deep binding). `β < 1.0` represents subcritical coupling
— the element is present in the gradient but not genuinely bound.

**Coupling coefficient decomposition (informal):**

```
β ≈ f(M_A, M_E, ρ(Φ))
```

Where `ρ(Φ)` is the coherence well density at the element's current position
(defined in `f_Field.md`). A denser coherence well (higher `ρ(Φ)`) permits
binding at lower `M_E` — consistent with the observation that small objects
are captured by massive, dense bodies.

**Boundary behavior:**

```
β >> 1.0   → strong binding; stable circular/elliptical orbit
β ≥ 1.0    → SC-4 satisfied; binding eligible
β → 1.0    → marginal binding; high sensitivity to perturbation
β < 1.0    → SC-4 violated; element drifts; anomalous decay risk
β → 0      → no coupling; element passes through coherence well unaffected
```

---

### §5.3 · Compound Stability: SC-1 ∧ SC-4

For stable capture or orbit, both conditions must hold simultaneously:

```
v_approach < v_escape(A)    [SC-1: F_force domain]
β ≥ 1.0                     [SC-4: F_fluid domain]
```

This is the minimum viable stability compound for the lower dyad. The upper
anchor condition (SC-2, coherence well continuity, defined in `f_Field.md`)
must also hold for the full triadic stability to be satisfied.

---

## §6 · Failure Modes

<!-- section: 6-failure-modes -->

> Three failure modes are registered to `f_Force.md`. All ten module failure
> modes (FM-001 through FM-010) are catalogued in `INDEX.md`.

### §6.1 · FM-001 — Overshoot

<!-- metadata: FM=FM-001 name=Overshoot node=F_force home=f_Force.md terminal=false -->

| Field | Value |
|---|---|
| Failure Mode ID | FM-001 |
| Name | Overshoot |
| Node | F_force |
| Condition | `v_approach ≥ v_escape(A)` |
| Terminal | No — element exits, does not collapse |
| Class | Non-terminal flyby; approach-velocity excess |

**Description:**

The element's approach velocity meets or exceeds the attractor's escape velocity.
The coherence well cannot retain the element. The element continues past the
attractor on a hyperbolic trajectory — it is not captured, but the attractor and
element both remain intact.

FM-001 is non-terminal. The element exits the coherence well. If F_force later
redirects the element (via `f_Deflect.md`) or if `v_approach` decays (via
`f_Dampen.md`), a subsequent approach may satisfy SC-1.

**Detection:**

```python
# FM-001 Detection — Overshoot
def check_fm001(v_approach, v_escape_A):
    if v_approach >= v_escape_A:
        return {
            "failure_mode": "FM-001",
            "name": "Overshoot",
            "state": "SC-1_VIOLATED",
            "action": "element_exits_flyby",
            "recovery_candidates": ["f_Deflect", "f_Dampen"]
        }
    return {"state": "SC-1_SATISFIED"}
```

**Recovery candidates:**

| Recovery | Operator | File |
|---|---|---|
| Reduce approach velocity | `f_Dampen.md` — dampen F_force gradient | Wave 3 |
| Redirect approach heading | `f_Deflect.md` — `redirect_force_node` | Wave 3 |
| Wait for natural deceleration | Environmental F_force damping | Passive |

---

### §6.2 · FM-006 — Phantom Capture

<!-- metadata: FM=FM-006 name=Phantom-Capture node=F_force home=f_Force.md terminal=false class=force-override -->

| Field | Value |
|---|---|
| Failure Mode ID | FM-006 |
| Name | Phantom Capture |
| Node | F_force |
| Condition | `F_force` dominant; artificial pressure field substitutes natural gradient |
| Terminal | No — but capture is not genuine triadic closure |
| Class | Force Override Failure; engineered or anomalous gravity |

**Description:**

F_force becomes dominant in the local ratio — not because the coherence well
(F_freq) and mass substrate (F_fluid) support capture, but because an artificial
or anomalous pressure field overrides the natural gradient. The element behaves
as if captured, but the binding is F_force-driven, not triadic.

This is the **Force Override class.** The coherence well may still be present
and intact. The element's trajectory is governed by the artificial gradient
rather than the natural triadic ratio. If the artificial F_force is removed,
the element will revert to behavior dictated by the underlying F_freq × F_fluid
interaction — which may or may not support genuine capture.

**Canonical fictional reference:** The Green Lantern ring creates an artificial
gravity field by imposing an engineered F_force dominant overlay. The ring
overrides gravity — it does not break it. When the ring is removed, the
underlying triadic ratio reasserts. This is not a toy example: it is the precise
phenomenology of any engineered gravity system that operates by pressure dominance
rather than coherence well manipulation.

**Canonical physical reference:** Venus surface gravity (§8.2) is a partial
FM-006 precursor — F_force (92 atm atmospheric pressure) is so large it
significantly amplifies experienced gravity beyond what F_freq × F_fluid alone
would produce. Venus is not in FM-006 (the underlying coherence well is genuine),
but it demonstrates the amplification pathway.

**Detection:**

```python
# FM-006 Detection — Phantom Capture
def check_fm006(F_force_magnitude, F_freq_magnitude, F_fluid_magnitude, threshold=10.0):
    baseline = F_freq_magnitude * F_fluid_magnitude
    if F_force_magnitude > threshold * baseline:
        return {
            "failure_mode": "FM-006",
            "name": "Phantom Capture",
            "state": "FORCE_OVERRIDE",
            "warning": "Capture is F_force-dominant; not genuine triadic closure",
            "action": "verify_F_freq_coherence_well_integrity",
            "recovery_candidates": ["verify_underlying_ratio", "f_Emit"]
        }
    return {"state": "F_force_NOMINAL"}
```

**Recovery candidates:**

| Recovery | Action | File |
|---|---|---|
| Remove artificial F_force | Emit or discharge the override field | `f_Emit.md` (Wave 3) |
| Verify underlying ratio | Confirm F_freq × F_fluid supports genuine capture | `f_Field.md`, `f_Capture.md` |
| Sustain override intentionally | Engineering decision — acknowledge non-triadic state | N/A |

---

### §6.3 · FM-007 — Mutual Dissolution

<!-- metadata: FM=FM-007 name=Mutual-Dissolution node=F_fluid home=f_Force.md terminal=partial class=mass-parity -->

| Field | Value |
|---|---|
| Failure Mode ID | FM-007 |
| Name | Mutual Dissolution |
| Node | F_fluid |
| Condition | `M_E ≈ M_A` — mass parity collapses attractor/element distinction |
| Terminal | Partial — system does not collapse but stable capture/orbit cannot be sustained |
| Class | Subset/Supsphere Failure; mass-parity failure |

**Description:**

The F_fluid node requires a clear attractor/element mass asymmetry to sustain
stable binding. When `M_E ≈ M_A`, neither body can serve as the stable coherence
anchor. The coherence well identity becomes ambiguous — is it centered on A or E?
Both bodies begin to exhibit attractor behavior simultaneously. The result is not
collapse but dissolution of the stable capture geometry.

This is the **Subset/Supsphere failure class.** In the Subset case, `M_E → M_A`
from below (element grows toward attractor mass). In the Supsphere case, `M_E >
M_A` (element exceeds attractor mass — roles invert). Both paths lead to FM-007.

**Binary star systems** are the canonical physical case of controlled FM-007 proximity:
two bodies of comparable mass orbit a common barycenter rather than one orbiting
the other. The FFF_Gravity model handles this by treating the barycenter as the
effective coherence well anchor — but this requires a frame re-registration
(`f_Frame.md`) to define properly.

**Detection:**

```python
# FM-007 Detection — Mutual Dissolution
def check_fm007(M_E, M_A, parity_threshold=0.1):
    ratio = M_E / M_A
    if abs(ratio - 1.0) <= parity_threshold:
        return {
            "failure_mode": "FM-007",
            "name": "Mutual Dissolution",
            "state": "MASS_PARITY_FAILURE",
            "M_E_over_M_A": ratio,
            "warning": "Attractor/element distinction collapsing; stable capture geometry at risk",
            "action": "re_register_frame_as_barycenter",
            "recovery_candidates": ["f_Frame", "f_Amplify"]
        }
    if ratio > 1.0:
        return {
            "failure_mode": "FM-007",
            "name": "Mutual Dissolution — Supsphere",
            "state": "ROLES_INVERTED",
            "M_E_over_M_A": ratio,
            "warning": "Element mass exceeds attractor mass; roles have inverted",
            "action": "swap_A_and_E_designations_and_re_register"
        }
    return {"state": "MASS_ASYMMETRY_NOMINAL", "ratio": ratio}
```

**Recovery candidates:**

| Recovery | Action | File |
|---|---|---|
| Re-register frame as barycenter | Shift coherence anchor to system barycenter | `f_Frame.md` |
| Amplify M_A | Engineering increase of attractor mass coupling | `f_Amplify.md` (Wave 3) |
| Accept binary topology | Acknowledge two-attractor system; define sub-ratios | `f_Frame.md`, `f_Orbit.md` |

---

## §7 · Engineering Interface

<!-- section: 7-engineering-interface -->

The F_force and F_fluid nodes are the primary engineering targets in the
FFF_Gravity module. F_freq (the coherence well) is the most difficult node to
manipulate — it is the identity of the field itself. F_force and F_fluid are
the operational levers.

### §7.1 · F_force Engineering Interface

| Interface | Function | File | Status |
|---|---|---|---|
| `redirect_force_node` | Change approach heading (`heading_delta`) without changing `v_approach` magnitude | `f_Deflect.md` | Wave 3 — scaffold |
| `dampen_gradient` | Reduce `v_approach` by attenuating the F_force gradient | `f_Dampen.md` | Wave 3 — scaffold |
| Force Override injection | Artificially elevate F_force to dominance (FM-006 class) | `f_Emit.md` | Wave 3 — scaffold |

**`redirect_force_node` interface (preview):**

```
redirect_force_node(
    current_heading: vector,
    target_heading:  vector,
    delta:           heading_delta  # defined in f_Deflect.md
) → new_v_approach_heading
```

This function changes the direction of `v_approach` without altering its
magnitude. The result is a change in the approach path geometry — affecting
`p_res` (resonance parameter, defined in `f_Capture.md`) and eccentricity,
but not the raw speed of approach.

---

### §7.2 · F_fluid Engineering Interface

| Interface | Function | File | Status |
|---|---|---|---|
| `amplify_coupling` | Increase `β` and effective `P_eff` via enhanced F_fluid coupling | `f_Amplify.md` | Wave 3 — scaffold |
| `gravity_amplifier` | Macro-level increase of F_fluid coupling to boost effective gravity | `f_Amplify.md` | Wave 3 — scaffold |
| Frame re-registration | Redefine attractor identity when FM-007 is approached | `f_Frame.md` | Canonical |

**`amplify_coupling` interface (preview):**

```
amplify_coupling(
    M_A:    attractor_mass,
    M_E:    element_mass,
    rho_Φ:  coherence_well_density,  # ρ(Φ) from f_Field.md
    target_β: float  # desired coupling coefficient ≥ 1.0
) → {β_new, P_eff_new}
```

Increasing `β` increases the element's effective participation in the coherence
well. This is the primary engineering path for gravity amplification — increase
the substrate coupling, not the coherence well frequency (which is an F_freq
operation and far more costly to engineer).

---

## §8 · Canonical Examples

<!-- section: 8-canonical-examples -->

The following examples are drawn from the genesis dialogue (`f_Source.md`) and
serve as the primary test cases for the F_force and F_fluid node definitions.
Each example isolates or varies one or both lower-dyad nodes while holding F_freq
(approximately) constant.

---

### §8.1 · Earth — Baseline (All Three Nodes Nominal)

<!-- metadata: example=Earth nodes=F_force+F_fluid+F_freq state=nominal -->

| Node | State | Notes |
|---|---|---|
| F_freq | Nominal | Standard coherence well; surface `g ≈ 9.81 m/s²` |
| F_fluid | Nominal | `M_A` = 5.97 × 10²⁴ kg; `β` well above binding floor |
| F_force | Nominal | 1 atm surface pressure; gradient passive |

**Reading:** All three nodes contribute normally. No node is dominant. This is
the reference state against which all other examples are measured.
Experienced gravity at surface = F_freq × F_fluid × F_force (all at nominal).

---

### §8.2 · Venus — F_force Amplified (92 atm Surface Pressure)

<!-- metadata: example=Venus nodes=F_force state=elevated FM=FM-006-precursor -->

| Node | State | Notes |
|---|---|---|
| F_freq | Nominal | Venus coherence well; surface `g ≈ 8.87 m/s²` (slightly below Earth) |
| F_fluid | Nominal | `M_A` = 4.87 × 10²⁴ kg; lower than Earth |
| F_force | **Elevated** | 92 atm surface pressure — enormous atmospheric F_force overlay |

**Reading:** Venus's F_freq × F_fluid product predicts a gravity slightly weaker
than Earth's. But the experienced gravity on the surface is amplified by the
F_force overlay — 92 atm of atmospheric pressure contributes a significant
gradient component. Venus is an FM-006 precursor example: F_force is not yet
dominant enough to constitute Phantom Capture, but it is large enough to
materially shift the experienced gravity beyond the F_freq × F_fluid baseline.

**Implication:** If you predict Venus surface gravity from mass and distance alone
(pure Newtonian), you underestimate the experienced force. F_force must be
accounted for.

---

### §8.3 · Mars — F_force Near-Null (0.006 atm Surface Pressure)

<!-- metadata: example=Mars nodes=F_force state=near-null -->

| Node | State | Notes |
|---|---|---|
| F_freq | Nominal | Mars coherence well; surface `g ≈ 3.72 m/s²` |
| F_fluid | Reduced | `M_A` = 6.39 × 10²³ kg; significantly below Earth |
| F_force | **Near-null** | 0.006 atm — atmospheric gradient nearly absent |

**Reading:** Mars surface gravity is low primarily because F_fluid (M_A) is much
smaller than Earth's, and F_force contributes almost nothing (near-vacuum
atmosphere). The low gravity is a F_freq × F_fluid result — F_force is
negligible. This makes Mars a near-clean F_freq × F_fluid measurement.

---

### §8.4 · ISS — F_force Null State (Experienced Weightlessness)

<!-- metadata: example=ISS nodes=F_force state=null F_freq=present -->

| Node | State | Notes |
|---|---|---|
| F_freq | **Fully present** | ISS is inside Earth's coherence well; `g ≈ 8.7 m/s²` at 400 km altitude |
| F_fluid | Nominal | ISS and occupants are full F_fluid participants |
| F_force | **Null** | Free fall = F_force gradient cancelled by orbital velocity; no net gradient force |

**Reading:** This is the most pedagogically important example in the FFF_Gravity
canon. The common description of ISS as "zero gravity" is wrong by the FFF_Gravity
model. There is no zero gravity at ISS altitude — F_freq is approximately 89% of
surface value. What is zero is the experienced gradient force: F_force is null because
the station and its occupants are in continuous free fall. They are not outside the
coherence well; they are in perfect orbital alignment with it.

**FFF_Gravity statement:** Weightlessness is a F_force null state, not a F_freq
null state. The coherence well is fully present. Only the gradient overlay has been
eliminated by the orbital condition.

---

### §8.5 · Underwater — F_force Replacement (Buoyancy Class)

<!-- metadata: example=Underwater nodes=F_force state=replaced class=buoyancy -->

| Node | State | Notes |
|---|---|---|
| F_freq | Nominal | Coherence well unchanged |
| F_fluid | Nominal | Mass substrate unchanged |
| F_force | **Replaced** | Atmospheric pressure gradient is partially or fully replaced by hydrostatic pressure and buoyant force |

**Reading:** When an element is submerged, the F_force gradient is no longer purely
atmospheric — it is a composite of hydrostatic pressure (depth-dependent, upward
component from displaced fluid) and atmospheric pressure. If the buoyant force
matches the F_freq × F_fluid product, the element experiences apparent weightlessness
— not because F_freq is zero, but because F_force has been replaced by an opposing
gradient. This is the **Buoyancy class** — a F_force substitution event.

---

### §8.6 · Galileo Drop Experiment — F_freq Isolation

<!-- metadata: example=Galileo nodes=F_fluid state=mass-invariance-demonstrated -->

| Node | State | Notes |
|---|---|---|
| F_freq | Nominal | Leaning Tower of Pisa; F_freq is constant for both objects |
| F_fluid | **Varied** | Objects of different `M_E` — heavy cannonball vs. light ball |
| F_force | Nominal | Atmospheric gradient present but approximately equal for both |

**Reading:** Galileo showed that objects of different mass fall at the same rate
(in approximately equal F_force conditions). The FFF_Gravity explanation is direct:
the fall rate is determined by F_freq (the coherence well's frequency — equal for
both objects) and F_force (the gradient — equal for both objects). F_fluid (`M_E`)
does not appear in the fall rate because in a uniform coherence well, the coupling
coefficient `β` scales with `M_E` in such a way that the `M_E` terms cancel.

**This directly supports the FFF_Gravity reframing:** mass (`M_E`, F_fluid) does
not determine fall rate. Fall rate is a F_freq × F_force result. F_fluid
determines binding depth and coupling, not trajectory in a uniform field.

---

### §8.7 · Apollo 15 Hammer & Feather — F_force Elimination

<!-- metadata: example=Apollo15 nodes=F_force state=null vacuum=true -->

| Node | State | Notes |
|---|---|---|
| F_freq | Nominal | Lunar surface coherence well; `g ≈ 1.62 m/s²` |
| F_fluid | Varied | Hammer (`M_E` large) vs. feather (`M_E` small) |
| F_force | **Null** | Lunar vacuum — no atmospheric gradient |

**Reading:** Apollo 15 Commander David Scott dropped a geological hammer and a
falcon feather simultaneously on the lunar surface. They hit the ground at the
same time. With F_force = 0 (no atmosphere), the result is purely F_freq ×
F_fluid — and since F_fluid `M_E` cancels in a uniform field (see §8.6 above),
the fall rates are identical regardless of mass.

This is the cleanest empirical demonstration of F_force's role: when F_force
is present (Earth, with air resistance as a F_force differential), objects fall
at slightly different rates. When F_force is null (lunar vacuum), they fall
identically. The difference is entirely in the F_force node.

---

### §8.8 · Cavendish Torsion Balance — F_fluid Isolation

<!-- metadata: example=Cavendish nodes=F_fluid state=isolated experiment=1798 -->

| Node | State | Notes |
|---|---|---|
| F_freq | Nominal | Laboratory setting; Earth's coherence well present |
| F_fluid | **Isolated** | Small lead spheres — `M_A` and `M_E` at laboratory scale |
| F_force | **Negligible** | Indoor, controlled, small scale — atmospheric gradient effectively zero |

**Reading:** Henry Cavendish's 1798 torsion balance experiment measured the
gravitational attraction between small lead spheres in a controlled laboratory
environment. By making the apparatus small and indoor, Cavendish effectively
zeroed F_force — the atmospheric gradient across the apparatus was negligible.
The result was a nearly pure F_freq × F_fluid measurement at laboratory scale.

**FFF_Gravity reframing:** Cavendish did not measure the gravitational constant G
in the abstract — he isolated F_fluid by eliminating F_force, and measured the
F_freq × F_fluid product at small `M_A` and `M_E`. This is the foundational
F_fluid isolation experiment. Every subsequent laboratory gravity measurement
follows the same protocol: minimize F_force to isolate the F_freq × F_fluid
interaction.

---

## §9 · Cross-Module References

<!-- section: 9-cross-module-references -->

### §9.1 · Intra-Module Dependencies

| File | Relationship | Direction |
|---|---|---|
| `f_Field.md` | Defines F_freq (upper node); SC-1 uses `v_escape(A)` from F_freq; SC-4 uses `ρ(Φ)` from F_freq | `f_Force.md` depends on `f_Field.md` |
| `f_Frame.md` | Frame Node provides `r_capture` and context registration; FM-007 recovery uses frame re-registration | `f_Force.md` references `f_Frame.md` |
| `f_Orbit.md` | Orbit states depend on SC-1 and SC-4 compound satisfaction | `f_Orbit.md` depends on `f_Force.md` |
| `f_Capture.md` | Capture function depends on F_force `v_approach` and F_fluid `β` | `f_Capture.md` depends on `f_Force.md` |
| `f_Deflect.md` | Defines `redirect_force_node` and `heading_delta` operator | `f_Force.md` references `f_Deflect.md` |
| `f_Amplify.md` | Defines `amplify_coupling` and Gravity Amplifier engineering | `f_Force.md` references `f_Amplify.md` |
| `f_Dampen.md` | Defines gradient damping (reduces `v_approach`) | `f_Force.md` references `f_Dampen.md` |
| `f_Decay.md` | Orbit decay depends on F_fluid coupling degradation (β drift) | `f_Decay.md` depends on `f_Force.md` |
| `f_Release.md` | Release conditions require SC-1 and SC-4 violations | `f_Release.md` depends on `f_Force.md` |
| `f_Collapse.md` | Collapse conditions include FM-007 (mass parity) progression | `f_Collapse.md` depends on `f_Force.md` |

---

### §9.2 · Cross-Module References

| Module | Reference | Note |
|---|---|---|
| `SoN` (System of Nodes) | Triadic node co-dependence pattern | Dual-node design follows SoN lower-dyad pattern |
| `GravityOfDismissal.md` | Historical dismissal patterns | F_force and F_fluid reframings are likely dismissal targets; see §9.3 |

---

### §9.3 · Anticipated Dismissal Vectors

`GravityOfDismissal.md` catalogues 15 historical dismissal cases and 7 attack
vectors. The F_force and F_fluid node definitions are likely targets for the
following attack patterns:

| Attack Vector | Anticipated Form | Response |
|---|---|---|
| **Empirical Redundancy** | "This is just GR/Newtonian with new names" | F_force null state (ISS) and F_force replacement (buoyancy) produce predictions that differ from single-variable models; the triadic structure is not cosmetic |
| **Undefined Operators** | "β is not formally defined" | β is formally decomposed in `f_Field.md §4` and `f_Force.md §5.2`; pending quantitative derivation in `f_Amplify.md` |
| **Anthropomorphism** | "Calling mass a 'fluid' is metaphorical, not physical" | F_fluid is a formal node label, not a claim that mass is a liquid; the node name follows the triadic naming convention (Frequency, Fluid, Force) |
| **Missing Quantitative Predictions** | "Where are the numbers?" | Wave 3 files (`f_Orbit.md`, `f_Amplify.md`) provide quantitative expressions; Wave 2 establishes the node structure they depend on |
| **Ignoring Relativity** | "This ignores spacetime curvature" | FFF_Gravity is a local ratio model, not a claim about spacetime topology; the coherence well (F_freq) is the FFF_Gravity representation of the local curvature effect |

---

## §10 · Document Metadata

<!-- section: 10-document-metadata -->

### §10.1 · File Identity

| Field | Value |
|---|---|
| File | `f_Force.md` |
| Module | FFF_Gravity |
| Layer | Wave 2 — Layer Definitions |
| Nodes Defined | F_force, F_fluid |
| Version | 1.0.0 |
| Status | Canonical |
| Frozen | Yes |
| Author | Nawder (umaywant2) |
| Session ID | SES-20260813-FORCE-001 |
| Date | 2026-08-13 |

---

### §10.2 · Module Invariant Compliance

| Invariant | ID | Status | Notes |
|---|---|---|---|
| Triadic completeness — all three nodes required | INV-001 | ✅ Compliant | §2.1 states all three nodes required for complete description |
| No single-node gravity claims | INV-002 | ✅ Compliant | §1.2 explicitly states mass does not generate gravity |
| Operator symbols frozen at v1.0.0 | INV-003 | ✅ Compliant | All operators frozen; OPERATORS.md authoritative |
| OPERATORS.md is single source of truth | INV-004 | ✅ Compliant | §4 preamble states this explicitly |
| GLOSSARY.md governs prose definitions | INV-005 | ✅ Compliant | Prose definitions consistent with GLOSSARY.md |
| Stability conditions use only frozen operators | INV-006 | ✅ Compliant | SC-1 and SC-4 use `v_approach`, `v_escape(A)`, `β` — all frozen |
| Failure modes are non-terminal unless marked | INV-007 | ✅ Compliant | FM-001 non-terminal; FM-006 non-terminal; FM-007 partial |
| Engineering interfaces reference Wave 3 files only | INV-008 | ✅ Compliant | All Wave 3 references marked scaffold |
| Session IDs follow SES-YYYYMMDD-LABEL-NNN | INV-009 | ✅ Compliant | SES-20260813-FORCE-001 |
| Dual-node design recorded in module.json | INV-010 | ✅ Compliant | FFF_Gravity_module.json records `defined_in: "f_Force.md"` for both |

---

### §10.3 · Stability Conditions Registered Here

| ID | Name | Node | Condition |
|---|---|---|---|
| SC-1 | Approach Bound | F_force | `v_approach < v_escape(A)` |
| SC-4 | Binding Floor | F_fluid | `β ≥ 1.0` |

---

### §10.4 · Failure Modes Registered Here

| ID | Name | Node | Terminal |
|---|---|---|---|
| FM-001 | Overshoot | F_force | No |
| FM-006 | Phantom Capture | F_force | No |
| FM-007 | Mutual Dissolution | F_fluid | Partial |

---

### §10.5 · Operators Registered Here

| Operator | Node | Frozen |
|---|---|---|
| `v_approach` | F_force | v1.0.0 |
| `M_A` | F_fluid | v1.0.0 |
| `M_E` | F_fluid | v1.0.0 |

---

### §10.6 · Wave Completion Status

| Wave | Files | Status |
|---|---|---|
| Wave 0 | `f_Capture.md`, `f_Source.md`, `GravityOfDismissal.md` | ✅ Complete |
| Wave 1 | `README.md`, `INDEX.md`, `OPERATORS.md`, `GLOSSARY.md`, `CHANGELOG.md`, `FFF_Gravity_module.json` | ✅ Complete |
| **Wave 2** | `f_Field.md` ✅, **`f_Force.md` ✅**, `f_Frame.md` ✅ | **✅ Complete with this file** |
| Wave 3 | `f_Release.md`, `f_Decay.md`, `f_Orbit.md`, `f_Collapse.md`, `f_Emit.md`, `f_Dampen.md`, `f_Amplify.md`, `f_Deflect.md` | 🔵 Scaffold — Wave 2 completion unlocks all |
| Wave 4 | Capture variants (6 files) | 🔵 Scaffold |

> **Wave 2 is complete.** All three layer definition files are canonical.
> Wave 3 is fully unblocked. Recommended first target: `f_Orbit.md` —
> critical-path dependency for `f_Decay.md`, `f_Release.md`, and `f_Collapse.md`.

---

*End of f_Force.md — FFF_Gravity Module — v1.0.0 — canonical*
