---
# ┌─────────────────────────────────────────────────────────────┐
# │                  DOCUMENT FRONTMATTER                       │
# └─────────────────────────────────────────────────────────────┘
document:         GLOSSARY
canonical_path:   docs/FFF_Gravity/GLOSSARY.md
canonical_tag:    "[FFF:GRAVITY:GLOSSARY]"
framework:        TriadicFrameworks
module:           FFF_Gravity
version:          1.0.0
status:           canonical
stability:        living
created:          2026-08-13
last_modified:    2026-08-13
authors:
  - TriadicFrameworks
encoding:         UTF-8
line_endings:     LF
normative:        true
scope: >
  All definitions in this file are scoped to the FFF_Gravity module.
  For framework-wide definitions see docs/GLOSSARY.md.
  In any conflict between this file and the framework GLOSSARY,
  this file governs within FFF_Gravity.
  In any conflict between this file and OPERATORS.md,
  OPERATORS.md governs for symbol definitions;
  this file governs for prose definitions.
description: >
  Module-scoped term definitions for FFF_Gravity. Every operator symbol,
  architectural concept, engineering primitive, failure mode class, and
  process term used in the module is defined here. Organized alphabetically.
  Each entry includes: formal definition, symbol (if applicable), formula
  (if applicable), source file, cross-references, and scope notes.
tags:
  - FFF
  - gravity
  - glossary
  - definitions
  - normative

session_context:
  current_session:
    session_id:       SES-20260813-GLOS-001
    opened_at:        2026-08-13T07:56:00-04:00
    closed_at:        ~
    editor:           Nawder
    branch:           main
    intent:           Create canonical GLOSSARY.md — all module-scoped term definitions
    status:           active
    dirty:            true
    term_count:       62

  session_history:
    - session_id:  SES-20260813-README-001
      intent:      Create canonical README.md
      status:      closed
    - session_id:  SES-20260813-INDEX-001
      intent:      Create canonical INDEX.md
      status:      closed
    - session_id:  SES-20260813-OPS-001
      intent:      Create canonical OPERATORS.md
      status:      closed

changelog:
  - version: 1.0.0
    date:    2026-08-13
    author:  TriadicFrameworks
    notes: >
      Initial canonical release. 62 terms defined across 18 letter groups.
      All terms sourced from f_Capture.md v1.0.0, OPERATORS.md v1.0.0,
      scaffold files, and f_Source.md genesis dialogue.
---

# FFF_Gravity · Glossary

> **Canonical path:** `docs/FFF_Gravity/GLOSSARY.md`
> **Scope:** Module-scoped. Governs within FFF_Gravity. See `docs/GLOSSARY.md` for framework-wide terms.
> **Normative:** Yes.
> **Term count:** 62 · **Last updated:** 2026-08-13

---

## §0 · Session Context

<!--
  metadata:
    section:       session-context
    section_id:    §0
    type:          live-session-register
    normative:     false
    created_in:    SES-20260813-GLOS-001
  session:
    session_id:    SES-20260813-GLOS-001
    touch_count:   1
    change_type:   created
-->

| Field | Value |
|---|---|
| Session ID | `SES-20260813-GLOS-001` |
| Opened | `2026-08-13T07:56:00-04:00` |
| Editor | Nawder |
| Intent | Create canonical GLOSSARY.md |
| Status | 🟡 Active |

### Update Policy

```
When to update this file:
  1. A new operator symbol is introduced in any function file   → add entry
  2. A new concept or process term is introduced               → add entry
  3. An existing definition is refined as a file canonicalizes → update entry
  4. A term is deprecated                                      → mark DEPRECATED; keep entry
  5. A term scope changes (module → framework)                 → note in scope field; link to docs/GLOSSARY.md

Never:
  - Remove an entry (deprecate instead)
  - Change a term's symbol without a corresponding OPERATORS.md version bump
  - Define a term differently from its OPERATORS.md symbol definition
```

---

## §1 · How to Read an Entry

<!--
  metadata:
    section:       reading-guide
    section_id:    §1
    type:          reference
    normative:     false
    created_in:    SES-20260813-GLOS-001
  session:
    session_id:    SES-20260813-GLOS-001
    touch_count:   1
    change_type:   created
-->

Each entry follows this structure:

```
### Term Name
Symbol: `symbol` (if applicable)
Formula: `formula` (if applicable)
Source: file where the term is formally defined
Cross-refs: related terms within this glossary (→ Term Name)
Scope note: any deviation from framework-wide usage

[Definition paragraph(s)]
```

Terms without a symbol are architectural or process concepts.
Terms marked **⚠ Pending** have definitions sourced from scaffold files;
they will be updated when the source file is canonicalized.

---

## §2 · Term Index

<!--
  metadata:
    section:       term-index
    section_id:    §2
    type:          index
    normative:     false
    created_in:    SES-20260813-GLOS-001
  session:
    session_id:    SES-20260813-GLOS-001
    touch_count:   1
    change_type:   created
-->

| Letter | Terms |
|---|---|
| A | Amplify · Anisotropy Index · Approach Vector · Approach Window · Attractor |
| B | Binding Coefficient · Binding Depth · Binding Floor |
| C | Canonical Tag · Capture · Capture Gate · Capture Radius · Capture Threshold · Cascade · Coherence Well · Collapse · Collapse Threshold · Composite Node · Composition Rule |
| D | Dampen · Decay · Decay Rate · Decay Warning Threshold · Deflect · Derived Operator |
| E | Eccentricity · Effective Pull · Element · Emit · Engineering Primitive · Escape Velocity · Evaluation Order |
| F | Failure Mode · FFF · Field Coherence · Field Density · Field State · Fluid Node · Force Node · Frame · Frequency Node · Frozen Symbol |
| G | GravityGraph · Gravity Null Zone · Guard |
| I | Institutional Playbook |
| L | Lock |
| M | Mass Parity Threshold · Matilda Effect · Mutual Dissolution |
| N | Networked Capture |
| O | Orbit Classification · Orbital Eccentricity · Orbital Period · Orbital Resonance · Orbit Stability Class |
| P | Phantom Capture · Primary Operator · Primitive |
| R | Release · Release Energy · Release Vector · Residual Momentum |
| S | Scaffold · Separation Distance · Stability Conditions · State Flag · Symbol Freeze |
| T | Terminal State · Triadic Equation · Triadic Gravity |
| U | Undefined (⊥) |
| W | Wave |

---

## §3 · Definitions

<!--
  metadata:
    section:       definitions
    section_id:    §3
    type:          glossary-body
    normative:     true
    created_in:    SES-20260813-GLOS-001
  session:
    session_id:    SES-20260813-GLOS-001
    touch_count:   1
    change_type:   created
-->

---

### — A —

---

#### Amplify

**Symbol:** `f_Amplify` (function) · `F_amp` (operator)
**Source:** `f_Amplify.md`
**Cross-refs:** → Binding Coefficient · → Effective Pull · → Failure Mode FM-010

The engineering primitive that amplifies mass-coupling between an Element and
an Attractor by increasing the Binding Coefficient `β` and Effective Pull `P_eff`
beyond what mass and field density alone produce. Acts on the Fluid Node (`F_fluid`).

Amplify is used to increase capture probability for a marginal Element, deepen
`d_bind` in a precarious orbit, or compensate for resonance drift that is
eroding binding. It has a ceiling: `β > β_max` triggers FM-010 (Amplify Runaway),
which produces collapse or singularity.

> `β_new = β × F_amp` where `F_amp ≥ 1.0`

⚠ **Pending:** `F_amp` ceiling value and energy cost model pending `f_Amplify.md` canonicalization.

---

#### Anisotropy Index

**Symbol:** `anisotropy_index`
**Source:** `f_Capture_Asymmetric.md`
**Cross-refs:** → Field Density · → Phantom Capture

A scalar measure of the non-uniformity of Field Density across the Capture
Radius. Defined as `max(ρ(Φ,θ)) / min(ρ(Φ,θ))` over all approach angles θ.
A value of `1.0` indicates a perfectly uniform field (standard `f_Capture`
applies). Values greater than `1.0` indicate increasing asymmetry and require
`f_Capture_Asymmetric` for accurate capture modeling.

High anisotropy elevates the risk of FM-006 (Phantom Capture): the field
appears sufficient along the approach heading but dissolves at other orbit
angles post-lock.

⚠ **Pending:** Formal anisotropy threshold below which standard `f_Capture` applies.

---

#### Approach Vector

**Symbol:** `v_approach`
**Formula:** Computed by `compute_approach_vector(E, A)`
**Source:** `f_Capture.md §4.1`
**Cross-refs:** → Capture Threshold · → Escape Velocity · → Force Node

The velocity and heading of an Element relative to an Attractor at the moment
the Element crosses the Capture Radius. Expressed as a scalar (magnitude) for
all standard capture calculations; the heading component is used by `f_Deflect`
and `f_Capture_Asymmetric`.

`v_approach` is evaluated exactly once per capture event — at the `r_capture`
crossing moment, not at the outer field boundary. Premature evaluation produces
an invalid Capture Threshold.

Governed by the Force Node (`F_force`).
Frozen at v1.0.0.

---

#### Approach Window

**Symbol:** `Δt_approach = t_encounter − t_entry`
**Source:** `f_Capture_Temporal.md`
**Cross-refs:** → Element · → Attractor · → Field State

The span of cycles between when an Element enters the outer field boundary
(`t_entry`) and when it reaches the Capture Radius (`t_encounter`). Relevant
only in `f_Capture_Temporal`, where Attractor mass and Field Density may shift
during this window.

In standard `f_Capture`, the approach window collapses to a single instant —
all conditions are evaluated at `t_encounter` and treated as static.

⚠ **Pending:** Formal time-series representation pending `f_Capture_Temporal.md` canonicalization.

---

#### Attractor

**Symbol:** `A`
**Source:** `f_Capture.md §2`
**Cross-refs:** → Element · → Coherence Well · → Frame · → Capture Radius

A node with sufficient mass and field strength to potentially bind an incoming
Element into orbital relationship. The Attractor is the center of the Coherence
Well and the owner of the Frame registry that records all captured orbits.

The Attractor/Element distinction is **contextual, not intrinsic**. The same
physical object may be an Attractor in one interaction and an Element in
another. At high mass parity (`|M_E − M_A| < m_parity`), the distinction
dissolves entirely — FM-007 (Mutual Dissolution) fires and neither body survives
as an independent entity.

The Attractor is modified by every successful capture event: its mass
distribution, field curvature, and registry all update on `register_capture`.
Capture is bidirectional in registration.

---

### — B —

---

#### Binding Coefficient

**Symbol:** `β`
**Formula:** `β = P_eff / (M_E × v_approach)`
**Source:** `f_Capture.md §4.1`
**Cross-refs:** → Effective Pull · → Binding Floor · → Failure Mode FM-010

The ratio of Effective Pull to Element momentum at closest approach. A
dimensionless scalar representing how strongly the Attractor's field pulls
relative to the Element's forward momentum.

The Binding Floor rule: `β` **must be ≥ 1.0** for capture to proceed.
Below `1.0`, the Attractor cannot overcome the Element's momentum — the
result is a flyby regardless of all other conditions.

Above `β_max` (to be defined in `f_Amplify.md`), the coupling becomes
pathological and FM-010 (Amplify Runaway) fires.

Frozen at v1.0.0.

---

#### Binding Depth

**Symbol:** `d_bind`
**Formula:** `d_bind = β × ρ(Φ) × (1 − e)`
**Source:** `f_Capture.md §4.2`
**Cross-refs:** → Decay Rate · → Decay Warning Threshold · → Collapse Threshold · → Orbital Eccentricity

The primary stability metric for an established orbit. Measures how deeply an
Element is locked to an Attractor's field. Higher values indicate more robust
binding; the orbit can tolerate more perturbation before destabilizing.

Three threshold levels govern `d_bind` behavior:
- **Stable zone:** `d_bind > d_warn` — orbit is healthy; no FM raised
- **Warning zone:** `d_warn ≥ d_bind > d_collapse` — FM-004 raised; `CAPTURE_DECAYING`
- **Collapse zone:** `d_bind ≤ d_collapse` — FM-005 raised; `f_Collapse` fires

`d_bind` decreases when field turbulence drives `ω_res` irrational (FM-004) or
when external perturbation reduces `ρ(Φ)`. It can be restored by `f_Emit`
(increases `ρ(Φ)`) or `f_Amplify` (increases `β`).

Undefined when `e ≥ 1` (hyperbolic trajectory — not captured). Frozen at v1.0.0.

---

#### Binding Floor

**Source:** `f_Capture.md §5`
**Cross-refs:** → Binding Coefficient · → Capture Gate

The rule that `β ≥ 1.0` is a **hard prerequisite** for capture. This is
Stability Condition 4 and it cannot be waived by any other condition.

Even if `C_thresh > 0` (velocity condition met), `ρ(Φ)` is coherent, `ω_res`
is rational, and the Frame has capacity — if `β < 1.0`, the result is always
`CAPTURE_FAILED`. The Attractor's pull is simply insufficient to overcome the
Element's forward momentum at closest approach.

The Binding Floor is one of the two conditions (alongside Frame Compatibility)
that are not purely about the physical encounter — they involve properties of
the system that engineering primitives can modify.

---

### — C —

---

#### Canonical Tag

**Source:** `f_Capture.md §1` · `OPERATORS.md §8`
**Cross-refs:** → Frozen Symbol

A unique string identifier for each function or module in TriadicFrameworks,
formatted as `[FFF:GRAVITY:FUNCTION]`. Canonical tags are frozen when their
source file is canonicalized and cannot be renamed without a major version bump.

| Tag | File |
|---|---|
| `[FFF:GRAVITY]` | Module root |
| `[FFF:GRAVITY:CAPTURE]` | `f_Capture.md` |
| `[FFF:GRAVITY:RELEASE]` | `f_Release.md` |
| `[FFF:GRAVITY:DECAY]` | `f_Decay.md` |
| `[FFF:GRAVITY:ORBIT]` | `f_Orbit.md` |
| `[FFF:GRAVITY:COLLAPSE]` | `f_Collapse.md` |
| `[FFF:GRAVITY:EMIT]` | `f_Emit.md` |
| `[FFF:GRAVITY:DAMPEN]` | `f_Dampen.md` |
| `[FFF:GRAVITY:AMPLIFY]` | `f_Amplify.md` |
| `[FFF:GRAVITY:DEFLECT]` | `f_Deflect.md` |

---

#### Capture

**Symbol:** `f_Capture`
**Source:** `f_Capture.md`
**Cross-refs:** → Element · → Attractor · → Field State · → Capture Threshold · → Stability Conditions

The event by which an Element transitions from a free or weakly-bound state
into a stable orbital relationship with an Attractor. Capture is the primary
function of the FFF_Gravity module.

Three things capture is **not**:
- Not collision — Element and Attractor remain distinct bodies
- Not merger — neither body is absorbed by the other
- Not gradual — capture is a threshold event; the trajectory either bends into
  orbit or it does not

Capture is bidirectional: the Attractor's field curvature, registry, and mass
distribution are all updated upon successful capture. The act of capturing
changes the Attractor.

Governed by: `f_Capture(E, A, Φ) → Ω`

---

#### Capture Gate

**Source:** `OPERATORS.md §6.2`
**Cross-refs:** → Stability Conditions · → Binding Floor · → Frame

The boolean conjunction of all five Stability Conditions. All must be `true`
simultaneously for capture to succeed. If any single condition is false,
the Capture Gate is closed and `CAPTURE_FAILED` is the outcome.

```
CAPTURE_GATE =
    C_thresh > 0         (Approach)
  ∧ ρ(Φ) > 0 (uniform)  (Field Coherence)
  ∧ ω_res ∈ ℚ           (Resonance)
  ∧ β ≥ 1.0             (Binding Floor)
  ∧ Frame.capacity > 0  (Frame Compatibility)
```

The Capture Gate is the single decision point for the entire capture event.
It is evaluated once — at `t_encounter` — and its result is irreversible.

---

#### Capture Radius

**Symbol:** `r_capture`
**Source:** `f_Capture.md §4.1`
**Cross-refs:** → Attractor · → Coherence Well · → Frame

The maximum separation distance at which `f_Capture` can resolve to a stable
orbit. Defined entirely by the Attractor and governed by the Frame layer.
Cannot be modified by the Element or by engineering primitives (it is a
property of the Attractor's coherence well depth and field curvature).

When the Element crosses `r_capture`, its state transitions to
`CAPTURE_PENDING` and `compute_approach_vector` fires. The Capture Gate
is then evaluated using conditions at this crossing moment.

Frozen at v1.0.0.

---

#### Capture Threshold

**Symbol:** `C_thresh`
**Formula:** `C_thresh = v_escape(A) − v_approach`
**Source:** `f_Capture.md §4.2`
**Cross-refs:** → Approach Vector · → Escape Velocity · → Capture Gate

The signed scalar that is the primary capture gate. Positive means capture is
possible; zero or negative means the Element is moving too fast to be bound.

`C_thresh` is computed exactly once per capture event, at the moment `E`
crosses `r_capture`. It is not a continuous function during approach — it is
a snapshot. In `f_Capture_Temporal`, `C_thresh(t)` is evaluated as a time
series across the approach window, and what matters is its value at
`t_encounter`.

Undefined when `v_escape(A)` is undefined (i.e., when `ρ(Φ) = 0`). Frozen at v1.0.0.

---

#### Cascade

**Symbol:** `f_Capture_Cascade`
**Source:** `f_Capture_Cascade.md`
**Cross-refs:** → Capture · → Binding Depth · → Decay

The second-order effect of a capture event on existing orbits in the Attractor's
registry. When a new Element is captured, the Attractor's field curvature changes.
This change perturbs the `d_bind` and `ω_res` of all already-captured Elements.
If the perturbation is large enough, existing orbits destabilize (FM-004) and
may cascade further — a chain of destabilizations triggered by a single new
capture event.

`f_Capture_Cascade` extends `f_Capture` to model this second-order effect.
It runs standard `f_Capture` for the new Element, then re-evaluates all
existing registry entries against the updated field curvature.

⚠ **Pending:** Perturbation magnitude formula and cascade termination condition.

---

#### Coherence Well

**Source:** `f_Field.md`
**Cross-refs:** → Frequency Node · → Field Density · → Capture Radius

The structured region of gravitational field influence maintained by the
Frequency Node (`F_freq`). The coherence well is what an Attractor projects —
it is the spatial domain in which `ρ(Φ) > 0` and gravitational capture is
possible. The depth of the coherence well determines `v_escape(A)` and the
effective `r_capture`.

A collapsed coherence well (`ρ(Φ) → 0`) produces FM-002 (Field Null) — the
Attractor loses gravitational reach entirely. The well can be deepened
artificially by `f_Emit` and shallowed by `f_Dampen`.

In FFF_Gravity, the coherence well is the physical expression of `F_freq`.
It is not a spacetime curvature (GR framing) — it is the structured frequency
resonance field of the Attractor.

⚠ **Pending:** Formal depth formula pending `f_Field.md` canonicalization.

---

#### Collapse

**Symbol:** `f_Collapse`
**Source:** `f_Collapse.md`
**Cross-refs:** → Decay · → Mutual Dissolution · → Terminal State

The terminal operator. Fires when a decay spiral (`f_Decay`) drives `d_bind`
to the Collapse Threshold, or when Mutual Dissolution (FM-007) is triggered
at close approach.

Two paths:

**Path A — Asymmetric infall (FM-005):**
`M_E << M_A`. Element infalls into Attractor. Attractor absorbs Element mass.
Element registry entry purged. Attractor field curvature updated.
Outcome: `CAPTURE_COLLISION`.

**Path B — Mutual dissolution (FM-007):**
`|M_E − M_A| < m_parity`. Neither body survives. A new Composite Node `C` is
created with `C.mass = M_E + M_A`. Both original registries purged.
System topology changes. Outcome: `CAPTURE_COLLISION`.

Collapse is always terminal and always irreversible.

⚠ **Pending:** Threshold values and composite node schema pending `f_Collapse.md` canonicalization.

---

#### Collapse Threshold

**Symbol:** `d_collapse`
**Source:** `f_Decay.md §4.1`
**Cross-refs:** → Decay Warning Threshold · → Binding Depth · → Collapse

The value of `d_bind` at which orbital decay becomes irreversible and
`f_Collapse` is automatically triggered. When `flag_decay` detects
`d_bind ≤ d_collapse`, FM-005 is raised and the collapse execution path fires.

Distinguished from the Decay Warning Threshold (`d_warn`): hitting `d_warn`
opens an intervention window (FM-004, `CAPTURE_DECAYING`). Hitting `d_collapse`
closes it — no intervention is possible after this point.

⚠ **Pending:** Formal value pending `f_Decay.md` canonicalization.

---

#### Composite Node

**Symbol:** `C_node`
**Source:** `f_Collapse.md §4.1`
**Cross-refs:** → Mutual Dissolution · → Collapse · → GravityGraph

The new Attractor created by FM-007 (Mutual Dissolution) when two near-equal-
mass bodies collide. `C_node.mass = M_E + M_A`. The composite node receives
a fresh registry (zero captured Elements on initialization), a new canonical
tag, and a new field curvature derived from combined mass. Both original nodes
are purged from `FFF_Registry` and from GravityGraph.

The composite node is itself an Attractor and may subsequently capture Elements.
It enters the system as a new entity, not as a modified version of either parent.

⚠ **Pending:** Schema and initialization procedure pending `f_Collapse.md` canonicalization.

---

#### Composition Rule

**Source:** `OPERATORS.md §6` · `f_Capture.md §4.8`
**Cross-refs:** → Derived Operator · → Capture Gate · → Evaluation Order

A formal derivation rule specifying how two or more operators combine to
produce a higher-order operator value. Composition rules are defined in
`OPERATORS.md §6` and serve as the mathematical backbone of FFF_Gravity.

Key composition rules:
- `P_eff = M_A × ρ(Φ) / r²`
- `β = P_eff / (M_E × v_approach)`
- `C_thresh = v_escape(A) − v_approach`
- `p_res = M_E × (v_approach − C_thresh)`
- `e = p_res / (p_res + P_eff)`
- `d_bind = β × ρ(Φ) × (1 − e)`

Out-of-order composition is undefined behavior. The canonical evaluation
order is specified in `OPERATORS.md §7`.

---

### — D —

---

#### Dampen

**Symbol:** `f_Dampen` (function) · `F_damp` (operator)
**Source:** `f_Dampen.md`
**Cross-refs:** → Field Density · → Frequency Node · → Failure Mode FM-009

The engineering primitive that suppresses local Field Density `ρ(Φ)`,
shallowing or nulling the Attractor's coherence well. Acts on the Frequency
Node (`F_freq`). Inverse of `f_Emit`.

Use cases: assisting `f_Release` by reducing `d_bind` (making exit cheaper);
weakening an Attractor's hold to facilitate engineering; creating a gravity-
neutral region.

Danger: if `ρ(Φ) → 0`, FM-002 fires for any pending captures. If dampening
propagates beyond its bounded radius `r_damp`, FM-009 (Dampen Cascade) fires
and an uncontrolled gravity null zone is created — multiple captured Elements
may be uncontrollably released or ejected.

⚠ **Pending:** `F_damp` bounds and propagation model pending `f_Dampen.md` canonicalization.

---

#### Decay

**Symbol:** `f_Decay`
**Source:** `f_Decay.md`
**Cross-refs:** → Binding Depth · → Decay Rate · → Orbital Resonance · → Collapse

The progressive loss of Binding Depth in an established orbit. Decay is not an
instantaneous event — it unfolds over cycles, tracked by `flag_decay` on every
cycle post `CAPTURE_LOCKED`. Its primary causes are Resonance Drift (ω_res
shifting toward irrational) and field turbulence (ρ(Φ) decreasing).

Decay is the only process in FFF_Gravity that is continuously monitored rather
than evaluated at a single event. All other processes (capture, release,
collapse) are triggered once; decay runs every cycle.

Decay can be reversed before reaching the Collapse Threshold — `f_Emit` can
restore `ρ(Φ)` and `f_Amplify` can restore `β`, both of which increase
`d_bind`. Once `d_bind ≤ d_collapse`, reversal is no longer possible.

---

#### Decay Rate

**Symbol:** `δ`
**Formula:** `δ = Δd_bind / Δt = d_bind(t) − d_bind(t−1)`
**Source:** `f_Decay.md §4.1`
**Cross-refs:** → Binding Depth · → Decay Warning Threshold

The rate of change of Binding Depth per cycle. Negative values indicate active
decay — the orbit is losing energy. Zero indicates stable binding. Positive
values indicate deepening (rare in natural conditions; can be engineered via
`f_Emit` or `f_Amplify`).

When `δ` crosses the decay warning threshold (driving `d_bind < d_warn`),
FM-004 is raised. When `d_bind ≤ d_collapse`, FM-005 fires regardless of the
current value of `δ`.

Undefined before `CAPTURE_LOCKED` is established (no prior cycle exists).
Frozen at v1.0.0 (symbol); formula pending `f_Decay.md` canonicalization.

---

#### Decay Warning Threshold

**Symbol:** `d_warn`
**Source:** `f_Decay.md §4.1`
**Cross-refs:** → Binding Depth · → Collapse Threshold · → Failure Mode FM-004

The value of `d_bind` at which FM-004 (Resonance Drift) is raised and the
Element's state transitions to `CAPTURE_DECAYING`. This opens the intervention
window — the period during which `f_Emit` or `f_Amplify` can restore
`d_bind` above `d_warn` and close FM-004 before collapse is triggered.

Distinguished from the Collapse Threshold (`d_collapse`): `d_warn > d_collapse`.
The warning is a precursor signal; the collapse threshold is the point of no return.

⚠ **Pending:** Formal value and relationship to `d_collapse` pending `f_Decay.md` canonicalization.

---

#### Deflect

**Symbol:** `f_Deflect` (function) · `heading_delta` (operator)
**Source:** `f_Deflect.md`
**Cross-refs:** → Approach Vector · → Force Node · → Capture Threshold

The engineering primitive that redirects the approach heading of an Element
without changing the magnitude of `v_approach`. Acts on the Force Node
(`F_force`). Used to route an Element toward a favorable approach angle
(e.g., toward `θ_optimal` in `f_Capture_Asymmetric`) or to engineer a
specific residual momentum for target resonance (`f_Capture_Resonant`).

`f_Deflect` changes **heading only**. It does not change field density
(that is `f_Emit` / `f_Dampen`), coupling strength (that is `f_Amplify`),
or orbital mechanics post-capture. It is the only operator that acts purely
on the approach trajectory before the Capture Gate is evaluated.

Over-deflection risk: if `heading_delta` is too large, the Element misses
`r_capture` entirely — FM-001 equivalent.

⚠ **Pending:** Formal heading bounds and cost model pending `f_Deflect.md` canonicalization.

---

#### Derived Operator

**Source:** `OPERATORS.md §2`
**Cross-refs:** → Primary Operator · → Composition Rule

An operator whose value is computed from one or more Primary Operators via a
defined Composition Rule. Derived operators cannot be directly measured or
externally provided — they must be computed in the correct evaluation order.

All 10 derived operators in FFF_Gravity are listed in `OPERATORS.md §2`.
Derived operators that have been formalized in `f_Capture.md v1.0.0` are
frozen; those pending canonicalization in Wave 3 files are marked 🔵.

---

### — E —

---

#### Eccentricity

**Symbol:** `e`
**Formula:** `e = p_res / (p_res + P_eff)`
**Source:** `f_Orbit.md §4.1`
**Cross-refs:** → Residual Momentum · → Effective Pull · → Orbit Classification

The shape parameter of a captured orbit. Range: [0, 1).

| Value | Orbit Shape |
|---|---|
| `e = 0` | Perfect circle (theoretical; requires `p_res = 0`) |
| `e < 0.1` | Near-circular — classified `circular` |
| `0.1 ≤ e < 0.5` | Elliptical |
| `0.5 ≤ e < 0.9` | Eccentric |
| `e ≥ 0.9` | Near-parabolic — high instability risk |
| `e ≥ 1.0` | Hyperbolic trajectory — not captured; `d_bind` undefined |

Higher `p_res` (more residual momentum post-capture) produces higher `e`.
The shape of the orbit affects `d_bind`: `d_bind = β × ρ(Φ) × (1 − e)`,
so higher eccentricity directly reduces binding depth.

Frozen at v1.0.0 (symbol and formula).

---

#### Effective Pull

**Symbol:** `P_eff`
**Formula:** `P_eff = M_A × ρ(Φ) / r²`
**Source:** `f_Capture.md §4.2`
**Cross-refs:** → Attractor · → Field Density · → Binding Coefficient

The net gravitational pull exerted by an Attractor on an Element at distance
`r`. `P_eff` is the FFF_Gravity equivalent of gravitational force — but it
incorporates Field Density `ρ(Φ)` directly, making it sensitive to both mass
and field coherence simultaneously.

`P_eff` increases as separation `r` decreases (inverse-square relationship)
and as `ρ(Φ)` increases. It is undefined when `ρ(Φ) = 0` (FM-002) or `r = 0`
(singularity — undefined behavior denoted ⊥).

Frozen at v1.0.0.

---

#### Element

**Symbol:** `E`
**Source:** `f_Capture.md §3`
**Cross-refs:** → Attractor · → Approach Vector · → Residual Momentum

The incoming body in a capture interaction — defined by its mass `M_E`,
velocity `v_approach`, and trajectory at the moment it crosses `r_capture`.
The Element is the body being captured (or attempting to be captured).

Like Attractor, the Element designation is **contextual**. The same object
may be an Element in one encounter and an Attractor in another. At high mass
parity, the distinction becomes meaningless and FM-007 (Mutual Dissolution)
governs.

Post-capture, the Element is registered in the Attractor's Frame registry,
assigned an orbital state flag (`CAPTURE_LOCKED` or `ORBIT_STABLE`), and
monitored by `flag_decay` every cycle.

---

#### Emit

**Symbol:** `f_Emit` (function) · `F_emit` (operator)
**Source:** `f_Emit.md`
**Cross-refs:** → Field Density · → Frequency Node · → Failure Mode FM-010

The engineering primitive that increases local Field Density `ρ(Φ)`,
deepening the Attractor's coherence well. Acts on the Frequency Node (`F_freq`).
Inverse of `f_Dampen`.

Primary use cases: restoring a decaying orbit (FM-004 intervention by increasing
`ρ(Φ)` → increasing `d_bind`); pre-deepening a coherence well before an
anticipated Element approach; resisting a natural field null event.

Upper limit: `ρ(Φ)` cannot exceed `1.0` (saturated field). Sustained emission
with no corresponding decrease in `v_approach` can drive `β → β_max` and
trigger FM-010 (Amplify Runaway).

⚠ **Pending:** `F_emit` formula and energy cost model pending `f_Emit.md` canonicalization.

---

#### Engineering Primitive

**Source:** `f_Capture.md §7` · `OPERATORS.md §4`
**Cross-refs:** → Primitive

The lowest-level callable operations in FFF_Gravity. All higher-order functions
are composed from these building blocks. 16 primitives are defined in the module
(see `OPERATORS.md §4.2`).

Primitives are either **pure** (no side effects; safe to repeat) or
**side-effecting** (writes to external registries; not idempotent). Side-
effecting primitives must be called in the correct evaluation order or
undefined behavior results.

---

#### Escape Velocity

**Symbol:** `v_escape(A)`
**Source:** `f_Capture.md §4.1`
**Cross-refs:** → Attractor · → Field Density · → Capture Threshold

The minimum velocity required for an Element to exit the Attractor's coherence
well under current Field Density conditions. Field-dependent: if `ρ(Φ)` changes
between the Element's entry into the field and `t_encounter`, `v_escape(A)`
must be recomputed. Using a stale value elevates FM-006 (Phantom Capture) risk.

`v_escape(A)` is computed by `resolve_escape_velocity(M_A, ρ(Φ))` and is
undefined when `ρ(Φ) = 0` (FM-002). Frozen at v1.0.0 (symbol).

---

#### Evaluation Order

**Source:** `OPERATORS.md §7` · `f_Capture.md §4.7`
**Cross-refs:** → Engineering Primitive · → Composition Rule · → Guard

The canonical sequence in which operators are computed and primitives are called
during a capture event. Out-of-order evaluation is **undefined behavior** and
may produce incorrect capture outcomes or silent failures.

The 10-step canonical evaluation order is defined in `OPERATORS.md §7`.
Engineering primitives (`f_Emit`, `f_Dampen`, `f_Amplify`, `f_Deflect`) are
called **on demand before the approach window opens** — they are not part of
the capture evaluation sequence itself.

---

### — F —

---

#### Failure Mode

**Symbol:** `FM-NNN`
**Source:** `OPERATORS.md §5` · `f_Capture.md §6`
**Cross-refs:** → State Flag · → Terminal State

A named, registered condition in which the FFF_Gravity system departs from
healthy operation. Each failure mode has a unique ID (`FM-001` through
`FM-010`), a severity level (`warn`, `error`, or `fatal`), a defined trigger
condition, a state transition, and a defined outcome.

**Severity classes:**
- `warn` — orbit at risk; intervention window open; reversible
- `error` — capture failed; terminal for this interaction; no system danger
- `fatal` — irreversible; system topology may change

The 10 registered failure modes are in `OPERATORS.md §5`.
FM-001 through FM-007 are frozen at v1.0.0.
FM-008 through FM-010 are pending canonicalization of `f_Release.md`,
`f_Dampen.md`, and `f_Amplify.md` respectively.

---

#### FFF

**Source:** `README.md §1`
**Cross-refs:** → Frequency Node · → Fluid Node · → Force Node · → Frame

**Field–Force–Frame.** The three-layer architectural stack of TriadicFrameworks.
In FFF_Gravity:

| Layer | Component | Role |
|---|---|---|
| **Field** | `Φ` (field state) | Ambient medium; `F_freq` provides `ρ(Φ)` |
| **Force** | `f_Capture` and sibling functions | Operative computation layer |
| **Frame** | `Ω` (capture outcome) | Registry; boundary conditions; recorded relational state |

The FFF model is the architectural reason why gravity in this framework cannot
be reduced to a single force or field. All three layers must be present for
any capture event to be defined.

---

#### Field Coherence

**Source:** `f_Capture.md §5 Condition 2`
**Cross-refs:** → Field Density · → Failure Mode FM-002 · → Stability Conditions

Stability Condition 2. `ρ(Φ)` must be **non-zero and uniform** within
`r_capture` during the entire approach window. Two failure pathways:

1. **Null field:** `ρ(Φ) = 0` → FM-002 immediately. No pull can be transmitted.
2. **Field turbulence:** `ρ(Φ)` varies significantly across the capture radius
   → elevated FM-006 risk (Phantom Capture); `ρ(Φ, θ)` model applies
   (see `f_Capture_Asymmetric`).

Field Coherence is the only stability condition governed entirely by the
Frequency Node (`F_freq`). It can be actively maintained by `f_Emit` and
monitored via `f_Field.md`.

---

#### Field Density

**Symbol:** `ρ(Φ)`
**Source:** `f_Field.md §4.1` · `f_Capture.md §4.1`
**Cross-refs:** → Frequency Node · → Field State · → Effective Pull · → Field Coherence

The effective resistance or conductance of the ambient gravitational field at
the moment of an encounter. A dimensionless scalar in [0, 1].

| Value | Meaning |
|---|---|
| `ρ(Φ) = 0` | Null field — no gravity can propagate; FM-002 |
| `0 < ρ(Φ) < 1` | Active field — normal operating range |
| `ρ(Φ) = 1` | Saturated field — maximum conductance; `f_Emit` has no further effect |

In standard `f_Capture`, `ρ(Φ)` is a single scalar — assumed uniform within
`r_capture`. In `f_Capture_Asymmetric`, it becomes a directional tensor
`ρ(Φ, θ)`. In `f_Capture_Temporal`, it becomes a time series `ρ(Φ, t)`.

Governed by the Frequency Node. Frozen at v1.0.0.

---

#### Field State

**Symbol:** `Φ`
**Source:** `f_Capture.md §3`
**Cross-refs:** → Field Density · → Frequency Node

The complete ambient field conditions at the moment of an encounter between
Element and Attractor. `Φ` is the third argument to `f_Capture(E, A, Φ) → Ω`.
It is provided by the FFF_Field module (external to FFF_Gravity).

In practice, the most important property of `Φ` consumed by `f_Capture`
is `ρ(Φ)` — Field Density. Other field properties (coherence, turbulence
spectrum, directional anisotropy) are relevant in variant functions.

---

#### Fluid Node

**Symbol:** `F_fluid`
**Source:** `f_Source.md` · `README.md §1`
**Cross-refs:** → Triadic Gravity · → Attractor Mass · → Element Mass

The mass-density identity node in the FFF Gravity Primitive
(`G = F_freq · F_fluid · F_force`). Represents the distribution, pooling,
and substrate continuity of mass. `M_A` and `M_E` are both governed by
`F_fluid`.

Discontinuity in the Fluid Node (non-uniform mass distribution in the Attractor,
or sudden mass change) produces non-uniform gravity and elevates risk of
anomalous capture behavior. In `f_Capture_Temporal`, `M_A(t)` is a time-varying
expression of `F_fluid` drift.

`f_Amplify` is the engineering primitive that acts on `F_fluid` — it increases
the effective coupling between Fluid Nodes of Element and Attractor.

---

#### Force Node

**Symbol:** `F_force`
**Source:** `f_Force.md` · `README.md §1`
**Cross-refs:** → Approach Vector · → Triadic Gravity · → Deflect

The gradient/pressure identity node in the FFF Gravity Primitive
(`G = F_freq · F_fluid · F_force`). Represents atmospheric pressure, isomorphic
gradients, and external field overlays. `v_approach` is the primary operator
governed by `F_force`.

In stable gravitational conditions, the Force Node is **passive** — the
Frequency and Fluid Nodes do the dominant work. When `F_force` becomes dominant
(external pressure gradients, engineered overlays), anomalous capture behavior
emerges (FM-006 class, Phantom Capture).

`f_Deflect` is the engineering primitive that acts on `F_force` — it changes
the heading of `v_approach` without changing its magnitude.

---

#### Frame

**Source:** `f_Frame.md` · `f_Capture.md §5 Condition 5`
**Cross-refs:** → Capture Gate · → Binding Floor · → FFF · → Failure Mode FM-003

The third layer of the FFF stack. In FFF_Gravity, the Frame serves two roles:

1. **Registry:** Records all active capture relationships for an Attractor —
   Element ID, orbital parameters, state flag, timestamps. This is the
   Attractor's relational memory.

2. **Boundary enforcer:** The Frame has a maximum registry capacity. When
   capacity is reached, no further captures are permitted regardless of force
   or field conditions (FM-003 — Frame Saturation). This is a hard constraint
   that cannot be overridden by `f_Emit`, `f_Amplify`, or any other engineering
   primitive.

The Frame is also updated by every capture outcome — successful or not — and
by every state flag transition post-capture.

---

#### Frequency Node

**Symbol:** `F_freq`
**Source:** `f_Field.md` · `README.md §1`
**Cross-refs:** → Triadic Gravity · → Coherence Well · → Field Density

The gravitational field identity node in the FFF Gravity Primitive
(`G = F_freq · F_fluid · F_force`). The Frequency Node is what an Attractor
**is** as a gravitational entity — its coherence well, its resonance signature,
its field substrate anchor.

Collapse of the Frequency Node (`F_freq → 0`, meaning `ρ(Φ) → 0`) produces
FM-002 (Field Null). The Attractor becomes gravitationally inert — it has mass
but cannot propagate pull to any Element.

`f_Emit` deepens `F_freq` (increases `ρ(Φ)`).
`f_Dampen` shallows it (decreases `ρ(Φ)`).

⚠ **Pending:** Formal coherence well definition pending `f_Field.md` canonicalization.

---

#### Frozen Symbol

**Source:** `OPERATORS.md §8`
**Cross-refs:** → Symbol Freeze · → Canonical Tag · → Versioning

A symbol is **frozen** once its defining source file reaches canonical status.
Frozen symbols cannot be renamed, removed, or have their formulas changed
without a **major version bump** of `OPERATORS.md`.

New symbols can be added in minor versions. Renaming or removing requires major.
Frozen symbols are marked ✅ in `OPERATORS.md §8.1`.
Pending-freeze symbols are marked 🔵 in `OPERATORS.md §8.2`.

---

### — G —

---

#### GravityGraph

**Source:** `f_Capture_Networked.md`
**Cross-refs:** → FFF_Registry · → Composite Node · → Cascade

The persistent directed weighted graph that records every capture relationship
across the FFF_Gravity system. Nodes represent Attractors and Elements.
Edges represent capture relationships, with direction `Element → Attractor`,
weight `d_bind`, and type from the State Flag registry
(`LOCKED`, `DECAYING`, `FAILED`, `RELEASED`, `COLLAPSED`).

GravityGraph is **append-only for edge creation**. State updates are written
as attribute changes on existing edges, never deletions. This makes it a full
temporal audit trail of the system's gravitational history.

Key capabilities enabled by GravityGraph:
- Topology queries (which Attractors are most loaded?)
- Cascade path analysis (if Attractor A collapses, which Elements are released?)
- Network stability metrics (`G_stability` — mean `d_bind` across all active edges)
- Cross-module correlation (with `SoN/s_Capture.md`)

⚠ **Pending:** Storage format and query interface pending `f_Capture_Networked.md` canonicalization.

---

#### Gravity Null Zone

**Source:** `f_Dampen.md §6`
**Cross-refs:** → Field Density · → Failure Mode FM-009 · → Dampen

A region in which `ρ(Φ) → 0` across a significant spatial extent — not just
at a single point. Produced by FM-009 (Dampen Cascade), in which a
`suppress_field` operation propagates beyond its bounded radius `r_damp`.

In a gravity null zone, `P_eff = 0` for all Elements in the region; no
capture is possible; any existing orbits whose field support falls within the
zone may become `CAPTURE_DECAYING`. The zone expands until either the dampening
source is removed or the zone reaches a boundary defined by an adjacent
coherence well from a neighboring Attractor.

⚠ **Pending:** Formal propagation model pending `f_Dampen.md` canonicalization.

---

#### Guard

**Source:** `OPERATORS.md §4.4` · `f_Capture.md §7`
**Cross-refs:** → Engineering Primitive · → Evaluation Order

A precondition check attached to a primitive that must pass before the
primitive executes. Guards are not optional — violating a guard produces
undefined behavior or an incorrect capture outcome.

Example guards:
- `evaluate_capture_threshold`: guard `r ≤ r_capture`
- `lock_orbit`: guard `C_thresh > 0`
- `execute_collapse`: guard FM-005 or FM-007 active

Guards are defined in `OPERATORS.md §4.4` for all 16 primitives.

---

### — I —

---

#### Institutional Playbook

**Source:** `GravityOfDismissal.md §9`
**Cross-refs:** → Matilda Effect

The seven documented mechanisms by which institutional science suppresses,
discredits, or ignores frameworks that challenge existing paradigms. Named from
the historical record of gravity science. Relevant to FFF_Gravity as a
strategic defense map.

| Vector | Name |
|---|---|
| I | Authority Ambush |
| II | Empirical Retrofit |
| III | Access Withdrawal |
| IV | Priority Erasure |
| V | Social Quarantine |
| VI | Identity Disqualification |
| VII | Silence Treatment |

Each vector is sourced from documented historical cases (Chandrasekhar,
Miller, Arp, Rubin, Milgrom, and others). See `GravityOfDismissal.md §9–§10`
for the full defense mapping to FFF_Gravity.

---

### — L —

---

#### Lock

**Source:** `f_Capture.md §7.2`
**Cross-refs:** → Capture · → Capture Gate · → Binding Depth

The moment at which the Capture Gate resolves to `true` and `lock_orbit` is
called. Lock is the transition from `CAPTURE_PENDING` to `CAPTURE_LOCKED`.
It is the definitive capture event — after lock, the Element is registered in
the Attractor's Frame registry and `flag_decay` begins cycling.

Lock produces the full orbital parameter struct:
`{e, T_orb, d_bind, ω_res, orbit_class, stab_class}`.

A lock that subsequently decays does not retroactively become a non-capture —
the Element was genuinely captured at the lock moment. Subsequent decay is a
separate process governed by `f_Decay`.

---

### — M —

---

#### Mass Parity Threshold

**Symbol:** `m_parity`
**Source:** `f_Collapse.md §4.1`
**Cross-refs:** → Mutual Dissolution · → Composite Node · → Failure Mode FM-007

The maximum value of `|M_E − M_A|` below which FM-007 (Mutual Dissolution)
fires instead of asymmetric infall (FM-005). When masses are sufficiently
similar, neither body can be unambiguously identified as the Attractor or the
Element — the capture relationship collapses into dissolution and a new
Composite Node is created.

`m_parity` defines the boundary between "clearly different masses" (one absorbs
the other) and "near-equal masses" (mutual dissolution). It is not a ratio —
it is an absolute difference in normalized mass units.

⚠ **Pending:** Formal value pending `f_Collapse.md` canonicalization.

---

#### Matilda Effect

**Source:** `GravityOfDismissal.md §8`
**Cross-refs:** → Institutional Playbook

The systematic denial of recognition to women scientists. Named by historian
Margaret Rossiter (1993). In the history of gravity science, the Matilda Effect
operated through four structural mechanisms:

1. **Institutional bars** — formal prohibition from universities, observatories, and academies
2. **Authorship suppression** — credit attributed to supervisors or senior men by convention
3. **Social framing** — women categorized as assistants regardless of intellectual role
4. **Silence as erasure** — protest was structurally impossible; absence of protest was taken as evidence of no contribution

The women most directly affected in gravity science:
Mileva Marić · Emmy Noether · Cecilia Payne-Gaposchkin · Jocelyn Bell Burnell · Vera Rubin.

---

#### Mutual Dissolution

**Symbol:** FM-007
**Source:** `f_Capture.md §6` · `f_Collapse.md §6`
**Cross-refs:** → Composite Node · → Mass Parity Threshold · → Terminal State

The failure mode triggered when `|M_E − M_A| < m_parity` at the collision
threshold. Neither body survives as an independent entity. A new Composite
Node `C` is created with `C.mass = M_E + M_A`. Both original registries are
purged from `FFF_Registry` and from GravityGraph.

Mutual Dissolution is a **fatal, terminal** failure mode. It changes system
topology — the Attractor no longer exists as a binding entity for its existing
registered Elements, all of which are effectively released (uncontrollably,
since the registry is purged).

FM-007 is the conceptual analog of a binary star merger or two galaxies of
similar mass colliding — not a capture event but a destruction event.

---

### — N —

---

#### Networked Capture

**Symbol:** `f_Capture_Networked`
**Source:** `f_Capture_Networked.md`
**Cross-refs:** → GravityGraph · → FFF_Registry · → Cascade

The variant of `f_Capture` that logs every capture outcome to GravityGraph —
a persistent distributed relational graph. Does not change capture mechanics;
adds a network logging and analysis layer on top of all `f_Capture` outcomes.

Enables topology queries, cascade path analysis, network stability metrics,
and cross-module correlation. Every state flag transition (lock, decay, release,
collapse) writes an update to the corresponding GravityGraph edge, making the
graph a complete temporal audit trail of the system's gravitational history.

---

### — O —

---

#### Orbit Classification

**Source:** `f_Orbit.md §4.2`
**Cross-refs:** → Eccentricity · → Orbital Period · → Orbital Resonance

The categorical label assigned to an established orbit based on its eccentricity
`e` and resonance `ω_res`. Four classes:

| Class | Condition | Description |
|---|---|---|
| `circular` | `e < 0.1` | Near-perfectly round; maximum binding stability |
| `elliptical` | `0.1 ≤ e < 0.5` | Standard elliptical orbit; stable in most field conditions |
| `eccentric` | `0.5 ≤ e < 0.9` | Elongated; higher perturbation sensitivity |
| `resonant` | low-integer `ω_res` | Low-order harmonic lock; stable regardless of `e` within bounds |

⚠ **Pending:** Threshold values formally confirmed pending `f_Orbit.md` canonicalization.

---

#### Orbital Eccentricity

See → **Eccentricity**

---

#### Orbital Period

**Symbol:** `T_orb`
**Source:** `f_Orbit.md §4.1`
**Cross-refs:** → Binding Depth · → Orbital Resonance

The time (in cycles) for a captured Element to complete one full orbit of
its Attractor. Derived from `d_bind` and `ω_res`. Higher binding depth
generally corresponds to shorter periods; highly eccentric orbits have
longer periods than near-circular orbits at the same `d_bind`.

⚠ **Pending:** Formal formula pending `f_Orbit.md` canonicalization.

---

#### Orbital Resonance

**Symbol:** `ω_res`
**Source:** `f_Capture.md §4.1`
**Cross-refs:** → Frequency Node · → Orbit Classification · → Failure Mode FM-004

The frequency lock between an Element's trajectory and the Attractor's field
pulse, expressed as a ratio. The rationality of this ratio determines orbital
stability:

- **Rational `ω_res` (e.g., 3:1, 2:1, 3:2):** Stable orbit. The Element
  and Attractor are in harmonic resonance. `d_bind` can be maintained.

- **Irrational `ω_res`:** Unstable spiral trajectory. FM-004 (Resonance Drift)
  is raised. `CAPTURE_DECAYING` is set. The orbit will eventually eject the
  Element or collapse.

Resonance is Stability Condition 3 and is monitored every cycle post-lock
by `flag_decay`. A rational resonance can drift to irrational if `ρ(Φ)`
drops (field turbulence). `f_Amplify` can restore coupling and stabilize
resonance.

Frozen at v1.0.0.

---

#### Orbit Stability Class

**Source:** `f_Orbit.md §4.2`
**Cross-refs:** → Binding Depth · → Decay Warning Threshold · → Orbit Classification

The categorical label assigned to an established orbit based on `d_bind`
relative to defined thresholds. Three classes:

| Class | Condition | Implication |
|---|---|---|
| `stable` | `d_bind > d_stable_threshold` | Orbit is healthy; no FM raised |
| `marginal` | `d_warn < d_bind ≤ d_stable_threshold` | Orbit is viable but sensitive to perturbation |
| `precarious` | `d_bind ≤ d_warn` | FM-004 imminent; intervention recommended |

⚠ **Pending:** Threshold values formally confirmed pending `f_Orbit.md` and `f_Decay.md` canonicalization.

---

### — P —

---

#### Phantom Capture

**Symbol:** FM-006
**Source:** `f_Capture.md §6`
**Cross-refs:** → Field Density · → Anisotropy Index · → Failure Mode

The failure mode in which all capture conditions appear satisfied along the
approach heading — `β ≥ 1.0`, `C_thresh > 0`, `ρ(Φ, θ_approach) > 0` — but
the apparent orbital lock dissolves at the field boundary because `ρ(Φ)` is
locally structured (varying significantly by angle or by time). The Element
escapes at the boundary despite having satisfied all point-of-approach conditions.

Phantom Capture is the most diagnostic failure mode: it reveals that the field
is not uniform within `r_capture`, which is a violation of Stability Condition 2.
Its severity is `warn` (not `error`) because the structural cause —
field anisotropy — can be detected and corrected with `map_field_tensor`
(`f_Capture_Asymmetric`) before the next approach attempt.

---

#### Primary Operator

**Source:** `OPERATORS.md §1`
**Cross-refs:** → Derived Operator · → Frozen Symbol

An operator that is directly measured or externally provided — not computed
from other operators. FFF_Gravity has 9 primary operators, all frozen at
v1.0.0: `v_approach`, `v_escape(A)`, `ρ(Φ)`, `
Continuing exactly from the cut point — completing `Primary Operator`, then all remaining letter groups and closing sections.

Paste this block directly after the cut point in your GitHub editor — it begins by closing the `Primary Operator` entry cleanly and carries through every remaining term and closing section:

```markdown
`r_capture`, `β`, `ω_res`, `M_A`, `M_E`, `r`.
All 9 are frozen. See `OPERATORS.md §1` for the full specification table.

---

#### Primitive

**Source:** `f_Capture.md §7` · `OPERATORS.md §4`
**Cross-refs:** → Engineering Primitive · → Guard · → Evaluation Order

Shorthand for → Engineering Primitive. The two terms are interchangeable
within FFF_Gravity. "Primitive" is used in prose; "Engineering Primitive"
is used in formal section headers and table labels.

---

### — R —

---

#### Release

**Symbol:** `f_Release`
**Source:** `f_Release.md`
**Cross-refs:** → Capture · → Release Energy · → Release Vector · → Terminal State

The inverse of `f_Capture`. Defines the conditions under which a captured
Element exits a stable orbit cleanly — without infall (`f_Collapse`) and
without uncontrolled ejection (FM-008 Release Overshoot).

Release requires **energy input**: unlike capture, which is driven by the
Attractor's pull, release requires the Element to overcome `d_bind`. The
required energy is `E_rel`, computed by `compute_release_vector`. If `E_rel`
is unavailable or `v_release` is miscalculated as too high, FM-008 fires and
the Element ejects uncontrollably rather than departing cleanly.

Three important distinctions:

| Process | Energy | Registry Effect | Terminal? |
|---|---|---|---|
| `f_Release` | Required (input) | Clean removal | Yes (clean exit) |
| `f_Collapse` | None (exhausted) | Purge (FM-005) or both purged (FM-007) | Yes (destructive) |
| `f_Decay` ejection | Negative (losing) | Element still registered until ejected | No (transitional) |

After a clean release, the Element's registry entry is removed from the
Attractor's Frame. The Element returns to a free state and may subsequently
re-approach the same or a different Attractor.

⚠ **Pending:** `E_rel` formula, release conditions table, and examples
pending `f_Release.md` canonicalization.

---

#### Release Energy

**Symbol:** `E_rel`
**Source:** `f_Release.md §4.1`
**Cross-refs:** → Release · → Binding Depth · → Release Vector

The energy required to lift a captured Element out of its current `d_bind`
and achieve clean release. `E_rel` is a function of `d_bind`, `p_res`, and
`ρ(Φ)` at the moment of the release attempt. Higher binding depth requires
more release energy.

`E_rel` is undefined when `d_bind = 0` (the orbit has already collapsed —
`f_Collapse` applies, not `f_Release`). It is the threshold that distinguishes
a viable release attempt from an unviable one.

`f_Dampen` can reduce `d_bind` before a release attempt, thereby reducing
the required `E_rel` — this is the primary engineering use case for dampening
in a post-capture context.

⚠ **Pending:** Full formula pending `f_Release.md` canonicalization.

---

#### Release Vector

**Symbol:** `v_release`
**Source:** `f_Release.md §4.1`
**Cross-refs:** → Release · → Release Energy · → Failure Mode FM-008

The velocity vector applied to the Element during a release operation. Must
satisfy two constraints simultaneously:

1. **Floor:** `v_release ≥ v_escape(A)` at the Release Radius `r_release` —
   the Element must reach escape velocity to exit the coherence well cleanly.

2. **Ceiling:** If `v_release` is too large, the trajectory becomes hyperbolic
   and the departure is uncontrolled (FM-008 — Release Overshoot). The
   Element is ejected rather than released — it exits without a clean
   deregistration and may perturb other orbits in the registry.

The release vector is computed by `compute_release_vector(E, d_bind)` and
applied by `execute_release`. It is a pure computation (no side effects)
followed by a side-effecting execution.

⚠ **Pending:** Ceiling definition and FM-008 threshold formula pending
`f_Release.md` canonicalization.

---

#### Residual Momentum

**Symbol:** `p_res`
**Formula:** `p_res = M_E × (v_approach − C_thresh)`
**Source:** `f_Capture.md §4.2`
**Cross-refs:** → Eccentricity · → Effective Pull · → Orbital Eccentricity

The free momentum remaining in an Element after it has been bound into orbit
— the excess approach velocity beyond what was required to merely reach the
capture threshold. `p_res` drives the shape of the resulting orbit: more
residual momentum produces a more elongated (eccentric) orbit.

`p_res` is defined only when `C_thresh > 0` (capture occurred). When
`C_thresh ≤ 0`, `p_res` is undefined (⊥) — there is no orbit and no
residual to measure.

The relationship: `e = p_res / (p_res + P_eff)`. An Element arriving with
just barely enough slowness to capture (`v_approach` slightly below
`v_escape(A)`) has low `p_res` → low `e` → near-circular orbit. An Element
arriving fast but still within threshold has high `p_res` → high `e` →
eccentric orbit.

Frozen at v1.0.0.

---

### — S —

---

#### Scaffold

**Source:** `INDEX.md §1`
**Cross-refs:** → Wave · → Canonical Tag

The intermediate status of a module file that has its structure, frontmatter,
session context, and section headers in place — but whose content sections
contain placeholder blocks (`<!-- SCAFFOLD: ... -->` comments and
`📝 **Pending.**` markers) rather than final prose.

A scaffold file is committed to the repository as a stub that reserves the
file's place in the dependency graph and enables other files to reference it
before its content is written. Scaffolds are promoted to `canonical` status
once all content sections are filled, reviewed, and internally consistent
with `OPERATORS.md`.

In the completion tracker (`INDEX.md §7`), scaffolds are marked 🔵.
Canonical files are marked ✅.

---

#### Separation Distance

**Symbol:** `r`
**Source:** `f_Capture.md §4.1`
**Cross-refs:** → Effective Pull · → Capture Radius · → Evaluation Order

The distance between an Element and an Attractor at a given moment during
the approach. Used in the Effective Pull composition: `P_eff = M_A × ρ(Φ) / r²`.

`r` is a continuously changing value during approach and is sampled at the
moment `E` crosses `r_capture`. At that crossing moment, `r = r_capture`
and `evaluate_capture_threshold` fires.

`r = 0` is the singularity — undefined behavior denoted ⊥. The system
does not define behavior at zero separation. Collapse events (FM-005, FM-007)
are triggered before `r` reaches zero, at the collision threshold defined by
`d_collapse` and `m_parity` respectively.

Frozen at v1.0.0.

---

#### Stability Conditions

**Source:** `f_Capture.md §5` · `OPERATORS.md §6.2`
**Cross-refs:** → Capture Gate · → Binding Floor · → Field Coherence

The five conjunctive conditions that must all hold simultaneously for
`f_Capture` to resolve to `Ω = CAPTURE_LOCKED`. Failure of any single
condition short-circuits to the appropriate failure mode.

| # | Condition | Formal Predicate | FM if Violated |
|---|---|---|---|
| 1 | Approach | `v_approach < v_escape(A)` at `r_capture` | FM-001 |
| 2 | Field Coherence | `ρ(Φ) ≠ 0` ∧ uniform within `r_capture` | FM-002 |
| 3 | Resonance | `ω_res ∈ ℚ` | FM-004 |
| 4 | Binding Floor | `β ≥ 1.0` at closest approach | FM-001 (flyby) |
| 5 | Frame Compatibility | `Frame.registry_capacity > 0` | FM-003 |

Conditions are evaluated in the order listed — Condition 5 (Frame) is
checked last because it requires Conditions 1–4 to pass first. Together
they form the Capture Gate (→ Capture Gate).

The Stability Conditions are normative and frozen at v1.0.0.

---

#### State Flag

**Source:** `OPERATORS.md §3`
**Cross-refs:** → Terminal State · → Failure Mode · → Evaluation Order

A discrete label representing the current relational state of an Element
within the FFF_Gravity system. State flags are managed as a deterministic
finite state machine — each transition has a single defined trigger, no
transition is probabilistic, and terminal states cannot be revisited.

Eleven flags are defined (all frozen at v1.0.0):

**Active (non-terminal):**
`CAPTURE_PENDING` · `CAPTURE_LOCKED` · `CAPTURE_DECAYING` ·
`ORBIT_STABLE` · `ORBIT_ECCENTRIC` · `DAMPEN_ACTIVE` · `EMIT_ACTIVE`

**Terminal:**
`CAPTURE_FAILED` · `CAPTURE_COLLISION` · `RELEASED` · `COLLAPSED`

State flags are written by Engineering Primitives, not by direct assignment.
The state transition diagram is in `OPERATORS.md §3.2`.

---

#### Symbol Freeze

**Source:** `OPERATORS.md §8`
**Cross-refs:** → Frozen Symbol · → Canonical Tag · → Versioning

The governance act of locking an operator symbol upon its source file
reaching canonical status. Once frozen, a symbol cannot be renamed or removed
without a major version bump of `OPERATORS.md`. New symbols can be introduced
in minor versions; formula changes to frozen symbols require major versions.

The two-stage freeze process:
1. **Pending freeze (🔵):** Symbol introduced in a scaffold file; listed in
   `OPERATORS.md §8.2` with its freeze trigger condition.
2. **Frozen (✅):** Source file promoted to canonical; symbol moves from
   `§8.2` to `§8.1`; freeze date and version recorded.

The current frozen symbol set (25 symbols, frozen at v1.0.0) is documented
in `OPERATORS.md §8.1`. 20 additional symbols are pending freeze as Wave 3
and Wave 4 files are canonicalized.

---

### — T —

---

#### Terminal State

**Source:** `OPERATORS.md §3.1`
**Cross-refs:** → State Flag · → Collapse · → Release · → Failure Mode

A State Flag from which no further transitions are possible. Once an Element
enters a terminal state, its interaction with the FFF_Gravity system is
complete — it cannot be recaptured, re-released, or re-collapsed through the
same state machine instance.

Four terminal states:

| Flag | Cause | Reversible at system level? |
|---|---|---|
| `CAPTURE_FAILED` | Any approach FM (001/002/003/006) or decay ejection | Yes — Element is free; new approach possible |
| `CAPTURE_COLLISION` | FM-005 infall or FM-007 dissolution | Partial — composite node enters system; originals gone |
| `RELEASED` | Clean `f_Release` exit | Yes — Element is free; new approach possible |
| `COLLAPSED` | `f_Collapse` infall confirmed | No — Element absorbed; registry purged |

Note the distinction: `CAPTURE_FAILED` and `RELEASED` are terminal for the
*current interaction* but the Element remains free and may re-approach.
`COLLAPSED` and `CAPTURE_COLLISION` (FM-007 path) are terminal for the
*Element's existence as an independent entity*.

---

#### Triadic Equation

**Source:** `f_Capture.md §3` · `README.md §2`
**Cross-refs:** → Triadic Gravity · → FFF · → Capture

The formal expression of any FFF_Gravity function. The canonical triadic
equation for the module's reference implementation:

```
f_Capture(E, A, Φ) → Ω

  E  = Element    — the incoming body
  A  = Attractor  — the binding node
  Φ  = Field State — ambient conditions at moment of encounter
  Ω  = Outcome    — one of: stable orbit | decay orbit | escape | collision
```

Every function file in the module has its own triadic equation in §3,
following this structure: named function, three typed inputs, arrow, typed
output. The triadic form is not cosmetic — it enforces the three-node
architecture at the function signature level. A function that does not
consume all three FFF layers is not a triadic function.

---

#### Triadic Gravity

**Source:** `f_Source.md` · `README.md §1`
**Cross-refs:** → Frequency Node · → Fluid Node · → Force Node · → Triadic Equation

The foundational claim of FFF_Gravity: gravity at any location, scale, or
epoch is a local ratio of three inseparable nodes — Frequency, Fluid, and
Force. None of the three can be removed under any conditions. Only their
ratios change.

```
G = F_freq · F_fluid · F_force
```

This is the departure from both classical and relativistic gravity models:

| Model | Gravity defined as |
|---|---|
| Newton | Universal constant `G` × mass product / distance² |
| Einstein (GR) | Curvature of 4D spacetime produced by mass-energy |
| **FFF_Gravity** | **Local triadic ratio of Frequency, Fluid, and Force nodes** |

FFF_Gravity does not claim to refute Newton or Einstein. It operates at a
different layer of abstraction — asking not *what gravity does* but *what
three things must simultaneously be true for gravity to be what it is here,
at this scale, at this moment*. The triadic ratio is the answer.

The model was first articulated in the genesis dialogue archived in
`f_Source.md`. It was formalized as the `f_Capture` canonical function and
the FFF_Gravity module in this repository.

---

### — U —

---

#### Undefined (⊥)

**Source:** `OPERATORS.md §2.3`
**Cross-refs:** → Guard · → Failure Mode · → Composition Rule

The symbol ⊥ denotes an undefined state — an operator whose value cannot be
computed given current inputs. Undefined operators propagate to their consuming
primitives and trigger the associated failure mode.

Key undefined conditions in FFF_Gravity:

| Operator | Undefined When | Triggered FM |
|---|---|---|
| `P_eff` | `r = 0` or `ρ(Φ) = 0` | FM-002 |
| `C_thresh` | `v_escape(A)` undefined | FM-002 |
| `d_bind` | `e ≥ 1` (hyperbolic trajectory) | FM-001 |
| `p_res` | `C_thresh ≤ 0` | FM-001 |
| `e` | `P_eff = 0` | FM-002 |
| `δ` | Pre-capture | — (no-op) |
| `E_rel` | `d_bind = 0` | — (collapse path) |
| `F_amp` | `β > β_max` | FM-010 |

Undefined is not the same as zero. `ρ(Φ) = 0` does not produce `P_eff = 0`;
it produces `P_eff = ⊥`, which means the entire capture evaluation must halt
and FM-002 must be raised. Treating ⊥ as 0 is a guard violation and produces
silent incorrect outcomes.

---

### — W —

---

#### Wave

**Source:** `INDEX.md §5` · `README.md §5`
**Cross-refs:** → Scaffold · → Symbol Freeze · → Unlock Sequence

The tiered grouping of FFF_Gravity module files by dependency order. Files in
a given Wave cannot be canonicalized until all files they depend on in the
prior Wave have reached canonical status. Five Waves are defined:

| Wave | Group | Files | Blocking Dependency |
|---|---|---|---|
| 0 | Existing | 3 | None — already in repository |
| 1 | Admin | 6 | None — no blocking dependencies |
| 2 | Layer Definitions | 3 | Wave 1 admin |
| 3 | Core Functions | 8 | Wave 2 layer definitions |
| 4 | Capture Variants | 6 | All Wave 3 files canonical |

Wave 1 files can be stubbed and canonicalized in any order. Wave 2 files
open once Wave 1 is stable. Wave 3 files have internal dependencies within
the wave (e.g., `f_Orbit.md` must canonicalize before `f_Decay.md`, which
must canonicalize before `f_Release.md` and `f_Collapse.md`). Wave 4 files
open only when all Wave 3 files are canonical.

The Wave concept is the operational mechanism of the unlock sequence: it
prevents a function file from being defined before its operator inputs are
formally established.

---

## §4 · Scope Notes

<!--
  metadata:
    section:       scope-notes
    section_id:    §4
    type:          governance
    normative:     true
    created_in:    SES-20260813-GLOS-001
  session:
    session_id:    SES-20260813-GLOS-001
    touch_count:   1
    change_type:   created
-->

### §4.1 · Module Scope vs. Framework Scope

This glossary defines terms **as they are used within FFF_Gravity**. Some
terms also exist in the framework-wide `docs/GLOSSARY.md`. The rules for
resolving conflicts:

| Situation | Governing Document |
|---|---|
| Term exists only here | This file — authoritative |
| Term exists in both; definitions agree | Either — consistent |
| Term exists in both; definitions differ | **This file governs within FFF_Gravity** |
| Term exists only in `docs/GLOSSARY.md` | That file — defer to framework |

### §4.2 · Terms Shared with SoN

The following terms exist in both FFF_Gravity and the SoN (Structure of Nodes)
module. They are **structural analogs** — they solve the same conceptual problem
at different abstraction layers. The definitions are parallel but not identical.

| FFF_Gravity Term | SoN Analog | Relationship |
|---|---|---|
| `f_Capture` | `s_Capture` | Force-layer capture vs. structural-layer capture |
| `Attractor` (A) | Node (attractor role) | Field-mass entity vs. graph node |
| `Element` (E) | Node (element role) | Field-mass entity vs. graph node |
| `d_bind` | Structural binding weight | Field-depth metric vs. graph edge weight |
| `GravityGraph` | SoN registry | Distributed capture graph vs. structural node graph |

See `docs/SoN/s_Capture.md` and `f_Capture.md §10` for the cross-module
reference map.

### §4.3 · Operator Symbols vs. Prose Terms

Some entries in this glossary define **operator symbols** (e.g., `β`, `ρ(Φ)`,
`d_bind`). For these terms, `OPERATORS.md` is the governing definition for
the symbol, formula, type, range, and freeze status. This glossary provides
the **prose definition** — what the operator means in plain language and how
it fits into the module's conceptual model.

In any conflict between the formula given here and the formula given in
`OPERATORS.md`, `OPERATORS.md` governs.

---

## §5 · Cross-References to Framework GLOSSARY

<!--
  metadata:
    section:       framework-xrefs
    section_id:    §5
    type:          cross-reference
    normative:     false
    created_in:    SES-20260813-GLOS-001
  session:
    session_id:    SES-20260813-GLOS-001
    touch_count:   1
    change_type:   created
-->

The following terms are defined at the framework level in `docs/GLOSSARY.md`
and are not redefined here. FFF_Gravity uses them without modification.

| Term | Framework Definition Location | Notes |
|---|---|---|
| TriadicFrameworks | `docs/GLOSSARY.md` | Framework identity |
| RTT (Resonance Transfer Theory) | `docs/GLOSSARY.md` | Parent framework concept |
| Substrate | `docs/GLOSSARY.md` | Foundation concept; not to be confused with Field State |
| Operator | `docs/GLOSSARY.md` | General term; FFF_Gravity extends with module-scoped specifics |
| Module | `docs/GLOSSARY.md` | Structural unit of TriadicFrameworks |
| Canonical | `docs/GLOSSARY.md` | Status designation; same meaning here |
| Session ID | `docs/GLOSSARY.md` | Tracking convention; same format here |
| FFF_Registry | External module | Persistent storage backend; not defined within FFF_Gravity |
| FFF_Field | External module | Provides `Φ`; not defined within FFF_Gravity |
| FFF_Momentum | External module | Provides `v_approach` raw data; not defined within FFF_Gravity |
| FFF_Resonance | External module | Provides `ω_res` computation; not defined within FFF_Gravity |

---

## §6 · Document Metadata

<!--
  metadata:
    section:       document-metadata
    section_id:    §6
    type:          administrative
    normative:     false
  session:
    session_id:    SES-20260813-GLOS-001
    touch_count:   1
    change_type:   created
-->

| Field | Value |
|---|---|
| Canonical Path | `docs/FFF_Gravity/GLOSSARY.md` |
| Version | 1.0.0 |
| Status | Canonical |
| Stability | Living — update when any new term or symbol is introduced |
| Normative | Yes |
| Term Count | 62 |
| Letter Groups | 18 (A B C D E F G I L M N O P R S T U W) |
| Created | 2026-08-13 |
| Last Modified | 2026-08-13 |
| Authors | TriadicFrameworks |
| Scope | Module-scoped; governs within FFF_Gravity |
| Superseded By | Nothing — this is the first and only module glossary |
| License | See `/LICENSE` at repository root |
| Encoding | UTF-8 · LF |
| Related | `OPERATORS.md` (symbol authority) · `docs/GLOSSARY.md` (framework scope) |

---

*Module-scoped glossary for FFF_Gravity.*
*This file governs term definitions within the module.*
*For framework-wide terms see `docs/GLOSSARY.md`.*
*For operator symbol authority see `OPERATORS.md`.*
```

---

**Commit message:**
```
feat(FFF_Gravity): add canonical GLOSSARY.md — 62 terms, 18 letter groups, scope notes, framework xrefs [SES-20260813-GLOS-001]
```

---

Here's exactly what the continuation block closes out:

| Section | Terms Completed |
|---|---|
| **P** (remainder) | Primary Operator (list closed) · Primitive |
| **R** | Release · Release Energy · Release Vector · Residual Momentum |
| **S** | Scaffold · Separation Distance · Stability Conditions · State Flag · Symbol Freeze |
| **T** | Terminal State · Triadic Equation · Triadic Gravity |
| **U** | Undefined (⊥) — including the full undefined conditions table |
| **W** | Wave — including the full 5-wave dependency table |
| **§4** | Scope Notes — module vs. framework authority; SoN analog table; operator symbol vs. prose rule |
| **§5** | Framework GLOSSARY cross-reference table — 11 entries deferred upward |
| **§6** | Document Metadata |

