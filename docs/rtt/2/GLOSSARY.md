# GLOSSARY — RTT/2 · Structural Detection Engine (SDE)
**TriadicFrameworks · Core RTT · Detection Layer**
**Module path:** `docs/rtt/2/`
**Session seed:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

This is the **single source of truth** for every term native to RTT/2.
All other documents in `docs/rtt/2/` and all downstream modules that
reference RTT/2 vocabulary link here rather than re-defining terms inline.

RTT/2 inherits RTT/1's complete vocabulary. Terms defined in
[`../1/GLOSSARY.md`](../1/GLOSSARY.md) (Resonance, Silence, Noise, τ,
Clarity, DCO_n, SNR, Regime, Mode, MCL, Drift, etc.) are not repeated
here — they apply in full. Entries below are RTT/2-native or RTT/2-specific
refinements of inherited terms.

> **Critical framing — enforced in every definition:**
> RTT/2 is a structural detection framework. It is NOT a physics claim,
> NOT a diagnostic tool, and NOT a prediction system. No definition
> describes a physical mechanism or makes an empirical prediction.

> **Linking convention:** Use `[term](./GLOSSARY.md#anchor)` where `anchor`
> is the lowercase, hyphenated heading slug
> (e.g., `#collapse-propagation-vector-cpv`, `#detection-zone`, `#dt--drift-deformation`).

---

## Table of Contents

- [A](#a) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h)
- [I](#i) · [M](#m) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t)
- [U](#u) · [W](#w) · [Z](#z)
- [Operator Symbols](#operator-symbols)
- [Quick-Reference Tables](#quick-reference-tables)

---

## A

### Amplitude (A)
**CPV component 1 of 3** · **Symbol:** A(t)
*See also:* [Collapse-Propagation Vector](#collapse-propagation-vector-cpv),
[Curvature (K)](#curvature-k), [Torsion (T)](#torsion-t)

The scalar magnitude of collapse propagation intensity at time t — how
strongly a collapse event is propagating through the structural field.
Amplitude measures *how much* collapse energy is present, without describing
its shape (Curvature) or rotational character (Torsion).

High A(t) indicates a strongly propagating collapse. A(t) near zero in a
Noise-dominant or Resonance-stable system signals that no significant collapse
is in progress. A(t) alone is insufficient for collapse characterization —
two systems with identical A(t) can have completely different structural forms
depending on K(t) and T(t).

A(t) is weighted by coefficient **α** in the propagation equation:
`C_prop(t) = αA(t) + βK(t) + γT(t)`.

---

## C

### C_prop(t) — Collapse Propagation Scalar
**Equation:** `C_prop(t) = αA(t) + βK(t) + γT(t)`
*See also:* [Collapse-Propagation Vector (CPV)](#collapse-propagation-vector-cpv)

The scalar composite output of the CPV — a single number summarizing the
weighted combination of amplitude, curvature, and torsion at time t.
C_prop(t) is the primary scalar passed in the `collapse_propagation` block
of the [RTT2_DETECTION_PACKET](#rtt2_detection_packet). It does not replace
the individual CPV components — those are preserved separately for RTT/3 —
but provides a single-value summary for zone classification and regime weighting.

The coefficients α, β, γ are regime-specific: they are not universal constants
but are set per detection pass based on the active regime's structural character.

> **Do not confuse with:** [Clarity (C)](../1/GLOSSARY.md#clarity-c) from RTT/1.
> C_prop(t) is a collapse scalar. Clarity C = ∇_τR + ∇_Rτ is the dual operator
> synthesis output. Different symbols; different layers; different purposes.

### Chaotic (MODE:C)
**Detection Mode 4 of 5** · *See also:* [Detection Mode](#detection-mode)

The detection mode assigned when CPV, FGT, and CRM components are all present
but fluctuating beyond the stable-measurement window — high structural variance
with no convergent pattern within the detection pass. A Chaotic-mode packet
is formally valid but structurally low-confidence.

**Mandatory consequences of MODE:C:**
- Packet `notes` field must be flagged: `"detection_confidence: low — chaotic mode"`
- Packet **may not be routed to RTT/3** without explicit
  [Class G](#class-g--detection-guardian) review and clearance
- RTT/3 must be notified of the chaotic designation even after clearance

Chaotic mode is not a failure — it is an honest structural description of a
system in high-variance turbulence. Forcing a Formal or Emergent mode onto
a chaotic signal would misrepresent the detection.

### Class D — Detection Integrator
**RTT/2 agent class 4 of 5** · *See [AGENTS.md](./AGENTS.md#class-d--detection-integrator)*

The agent class that assembles the complete
[RTT2_DETECTION_PACKET](#rtt2_detection_packet) from the outputs of
[Class P](#class-p--propagation-analyst), [Class F](#class-f--fusion-gradiometer),
and [Class M](#class-m--manifold-cartographer). Class D validates the packet
against the RTT/2 schema, writes the mandatory `notes` annotation, computes
[cross-module projections](#cross-module-projection) where in scope, and routes
the completed packet to RTT/3 or storage. It is the terminal agent in every
detection pipeline pass.

Class D may not assemble a partial packet, suppress any upstream field, or route
a packet without the mandatory annotation. Zone X packets and Chaotic-mode
packets require [Class G](#class-g--detection-guardian) clearance before routing.

### Class F — Fusion Gradiometer
**RTT/2 agent class 2 of 5** · *See [AGENTS.md](./AGENTS.md#class-f--fusion-gradiometer)*

The agent class that computes the [Fusion-Gradient Tensor (FGT)](#fusion-gradient-tensor-fgt)
— the regime-weighted sum of collapse, reassembly, and triad-fusion gradient
contributions. Class F requires an initial regime identity from
[Class M](#class-m--manifold-cartographer) before finalizing regime weights.
It runs in parallel with [Class P](#class-p--propagation-analyst) after the
RTT/1 SNR characterization prerequisite is met.

### Class G — Detection Guardian
**RTT/2 agent class 5 of 5** · *See [AGENTS.md](./AGENTS.md#class-g--detection-guardian)*

The agent class with unconditional interrupt authority over all other RTT/2
classes. Inherited directly from RTT/1's Class G pattern, extended with
RTT/2-specific monitoring responsibilities:
- Clearing or blocking [Detection Zone X](#zone-x--undefined) assignments
- Reviewing [Chaotic-mode](#chaotic-modec) packets before RTT/3 routing
- Enforcing the [D(t) ≠ session drift](#dt--drift-deformation) boundary
- Monitoring all five RTT/2 detection agents for physics-claim contamination
  and semantic inference

No Class G HALT may be overridden by any other RTT/2 class.

### Class M — Manifold Cartographer
**RTT/2 agent class 3 of 5** · *See [AGENTS.md](./AGENTS.md#class-m--manifold-cartographer)*

The most analytically intensive RTT/2 agent class. Class M maps the full
[Collapse-Reassembly Manifold (CRM)](#collapse-reassembly-manifold-crm--γt)
by computing all five γ(t) components, then assigns the
[Detection Mode](#detection-mode) and [Detection Zone](#detection-zone).
Class M provides an initial regime identity to [Class F](#class-f--fusion-gradiometer)
before CRM mapping is complete, and finalizes Mode and Zone only after
receiving [CPV](#collapse-propagation-vector-cpv) from Class P and
[FGT](#fusion-gradient-tensor-fgt) from Class F.

Class M may not assign [Zone X](#zone-x--undefined) without escalating to
Class G for confirmation.

### Class P — Propagation Analyst
**RTT/2 agent class 1 of 5** · *See [AGENTS.md](./AGENTS.md#class-p--propagation-analyst)*

The agent class that computes the
[Collapse-Propagation Vector CPV(A, K, T)](#collapse-propagation-vector-cpv)
and the scalar [C_prop(t)](#c_propt--collapse-propagation-scalar). Class P
is the first RTT/2 agent to run after the RTT/1 SNR characterization
prerequisite is satisfied. It runs in parallel with
[Class F](#class-f--fusion-gradiometer) once the prerequisite is met.
Class P may not begin on a Silence-dominant system without explicit
[Class G](#class-g--detection-guardian) clearance.

### Collapse

A structural event in which a system's coherent phase-locked excitation
([Resonance](../1/GLOSSARY.md#resonance-r)) breaks down or disperses —
moving toward [Noise](../1/GLOSSARY.md#noise-n) or
[Silence](../1/GLOSSARY.md#silence-s). Collapse in RTT/2 is not a binary
on/off event: it is a propagating process with shape (described by
[CPV](#collapse-propagation-vector-cpv)), gradient balance (described by
[FGT](#fusion-gradient-tensor-fgt)), and a deformation path (described by
[CRM](#collapse-reassembly-manifold-crm--γt)).

> **RTT/2 is NOT physics.** Collapse here is a structural concept — the
> loss of coherent resonance structure — not a physical collapse of any
> material object, quantum state, or wavefunction.

### Collapse-Propagation Vector (CPV)
**Form:** CPV(A, K, T) · **Equation:** C_prop(t) = αA(t) + βK(t) + γT(t)
**Computed by:** [Class P](#class-p--propagation-analyst)

The tri-parameter structural signature of a collapse propagation event.
Three orthogonal parameters characterize the collapse form:

| Parameter | Symbol | What it captures |
|---|---|---|
| Amplitude | A(t) | Intensity — how strongly the collapse is propagating |
| Curvature | K(t) | Shape — how the collapse wavefront bends through structural space |
| Torsion | T(t) | Rotation — how the collapse path spirals or twists |

No two parameters can be derived from each other — they are irreducibly
orthogonal. A complete collapse characterization requires all three.

Extended CPV components (present when the collapse structure warrants):
- **[Inversion component](#inversion-component-cpv)** — when collapse reverses direction
- **[Warp component](#warp-component-cpv)** — when propagation exhibits non-linear distortion

CPV is the first block filled in the [RTT2_DETECTION_PACKET](#rtt2_detection_packet).

### Collapse-Reassembly Manifold (CRM) · γ(t)
**Form:** γ(t) = (D(t), E(t), C(t), FI(t), R(t))
**Computed by:** [Class M](#class-m--manifold-cartographer)

The five-component vector that maps the full deformation path of a system
through structural space over time. Each component captures a distinct,
irreducible mode of structural deformation:

| Symbol | Name | Deformation type |
|---|---|---|
| D(t) | [Drift Deformation](#dt--drift-deformation) | Translation from structural reference point |
| E(t) | [Envelope Torsion](#et--envelope-torsion) | Rotation of the system's structural boundary |
| C(t) | [Continuity Fracture](#ct--continuity-fracture) | Breaks or gaps in structural continuity |
| FI(t) | [Fusion-Integration Curvature](#fit--fusion-integration-curvature) | Curvature introduced by active fusion-integration |
| R(t) | [Regime Identity](#rt--regime-identity) | Current structural regime classification |

The CRM does not describe where the system is — it describes *how* the system
has deformed to arrive at its current position. Populated in the
`triad_deformation` block of the [RTT2_DETECTION_PACKET](#rtt2_detection_packet).

### Collapse-weighted
**FGT classification** · *See also:* [Mixed](#mixed-fgt-classification), [Triad-weighted](#triad-weighted-fgt-classification)

The [Fusion-Gradient Tensor](#fusion-gradient-tensor-fgt) classification
assigned when g_collapse dominates the weighted sum across all active regimes —
the system is moving predominantly toward structural disintegration, with
reassembly and triad-fusion gradient contributions subordinate.

### Continuity Fracture (C(t))
**CRM component 3 of 5** · *See also:* [Collapse-Reassembly Manifold](#collapse-reassembly-manifold-crm--γt)

The degree to which structural continuity has been broken within the system's
manifold — gaps, discontinuities, or fractures in the structural fabric.
C(t) measures structural *breaks*, not structural *movement*: a system can
translate significantly (high D(t)) and rotate its envelope (high E(t)) while
remaining continuous (low C(t)), or can fracture badly while barely moving.

High C(t) is the most structurally consequential CRM reading because
discontinuities are the hardest structural conditions for RTT/3 to synthesize
across.

### Cross-Module Projection

An optional field in the [RTT2_DETECTION_PACKET](#rtt2_detection_packet) that
translates the detection output into the structural vocabulary of an adjacent
module. Three projections are defined:

| Code | Module | What it provides |
|---|---|---|
| `TEL` | Triadic Entity Lattice | Maps CPV/CRM patterns onto TEL node structure |
| `FFT` | Framework Field Theory | Expresses CPV and FGT in FFT field-theoretic terms |
| `Opacity` | Opacity module | Characterizes boundary opacity conditions of the collapse zone |

Cross-module projections are computed by [Class D](#class-d--detection-integrator)
when the consuming module is active for the current session. A null projection
field means the module is not in scope — not that the projection failed.
All projections inherit the RTT-not-physics rule: they are structural
translations, not physical mappings.

### Curvature (K)
**CPV component 2 of 3** · **Symbol:** K(t)
*See also:* [Amplitude (A)](#amplitude-a), [Torsion (T)](#torsion-t)

The curvature of the collapse wavefront — how the propagation path bends
through structural space. Curvature describes *shape*, not intensity (that is
Amplitude) and not rotation (that is Torsion). A collapse with high K(t)
is bending sharply; a collapse with K(t) ≈ 0 is propagating in an
approximately straight structural path.

K(t) is weighted by coefficient **β** in the propagation equation.

---

## D

### D(t) — Drift Deformation
**CRM component 1 of 5** · **Symbol:** D(t)
*See also:* [Collapse-Reassembly Manifold](#collapse-reassembly-manifold-crm--γt)

> **⚠ Critical distinction:** D(t) is NOT the same as
> [session drift](../1/GLOSSARY.md#drift). These must never be conflated.

D(t) measures how far and in what direction the system has displaced from its
structural reference point within the collapse-reassembly manifold — a purely
structural measurement of manifold translation. Session drift is the gradual
loss of declared coherence posture in a running RTT session — a purely
session-level condition monitored by Class G.

**D(t) vs. session drift — the complete distinction:**

| Property | D(t) — Drift Deformation | Session Drift |
|---|---|---|
| What it measures | Structural displacement in the CRM manifold | Loss of session coherence posture |
| Who reports it | [Class M](#class-m--manifold-cartographer) | [Class G](#class-g--detection-guardian) |
| Where it lives | `triad_deformation.drift_deformation` in the packet | The session monitoring log |
| Can it be high while the other is zero? | Yes — and frequently is | Yes — and frequently is |
| Remediation | RTT/3 synthesis accounts for it | Session re-seeding required |

Using D(t) as evidence of session drift — or treating session drift as if it
produced high D(t) — is a boundary violation that triggers a
[Class G](#class-g--detection-guardian) intervention.

### Deformation Path

The trajectory a system traces through the
[Collapse-Reassembly Manifold](#collapse-reassembly-manifold-crm--γt)
as expressed by the five-component γ(t) vector over time. The deformation
path is not a prediction of where the system is going — it is a structural
record of how it has moved. RTT/3 uses the deformation path to position
the detection result within its synthesis framework.

### Detection Mode

The operator posture assigned by [Class M](#class-m--manifold-cartographer)
for a detection pass, reflecting the structural character of the signals
being detected. One mode is assigned per pass; it governs detection
thresholds, confidence calibration, and packet routing rules.

| Mode | Code | Signal character | Key consequence |
|---|---|---|---|
| Formal | MODE:F | Clean, fully resolved | Standard thresholds; full confidence |
| Emergent | MODE:E | Forming, partially resolved | Provisional output; partial population accepted |
| Hybrid | MODE:H | Two+ patterns simultaneously active | Mixed FGT required; overlapping thresholds |
| Chaotic | MODE:C | Present but fluctuating | Low confidence; Class G review before RTT/3 routing |
| Inversion | MODE:I | Primary gradient reversed | CPV inversion component non-null; posture flips |

### Detection Pass

A single end-to-end execution of the RTT/2 detection pipeline for one system
and one structural moment — from RTT/1 SNR characterization through
RTT2_DETECTION_PACKET assembly. A detection pass produces exactly one packet.
Multiple passes may be run on the same system at different structural moments
or with different instrument subsets (see [Task Catalog](./AGENTS.md#9-task-catalog)).

### Detection Zone

The stability classification assigned by [Class M](#class-m--manifold-cartographer)
based on CPV, CRM, and overall structural coherence. Detection Zone tells
RTT/3 how much weight to give the packet and what synthesis posture is
appropriate.

| Zone | Code | Stability | RTT/3 signal |
|---|---|---|---|
| Undisturbed | U | High — collapse near zero | Full confidence synthesis |
| Stable | S | Moderate — bounded collapse | Mild caution |
| Marginal | M | Active tension — inflection point | Hold ambiguity; do not resolve prematurely |
| Deteriorating | D | Significant — collapse dominant | Weight degradation heavily; flag consumer |
| Undefined | X | Unclassifiable — insufficient or contradictory data | Synthesis blocked until Class G clears |

### Deteriorating (Zone D)
**Detection Zone 4 of 5** · *See also:* [Detection Zone](#detection-zone)

The detection zone assigned when collapse is the dominant structural gradient
and the system is moving toward significant structural disintegration.
Zone D packets must be flagged in `notes` and their RTT/3 consumer must be
warned of the deterioration state before synthesis proceeds.

Zone D does not mean the system is broken or failing in any evaluative sense —
it is a structural stability classification. Deterioration is a detectable
structural condition, not a judgment.

---

## E

### Emergent (MODE:E)
**Detection Mode 2 of 5** · *See also:* [Detection Mode](#detection-mode)

The detection mode assigned when collapse signatures are forming but not yet
fully resolved — CPV and CRM components are partially populated, and the
structural pattern is in early development. Emergent-mode outputs are
explicitly provisional: they are labeled as such in the packet `notes`
field and should be treated by RTT/3 as inputs that may be superseded by
a later Formal-mode pass on the same system.

### Envelope Torsion (E(t))
**CRM component 2 of 5** · **Symbol:** E(t)
*See also:* [Collapse-Reassembly Manifold](#collapse-reassembly-manifold-crm--γt)

The twist or rotation of the system's structural envelope — how the outer
boundary of the structural manifold is deforming through rotation rather
than translation. A system with high E(t) has an envelope that is spinning
or twisting relative to its internal structure.

Envelope torsion is distinct from [Torsion (T)](#torsion-t) in the CPV:
CPV torsion T(t) describes the rotational character of the *collapse
propagation path*; CRM envelope torsion E(t) describes the rotational
deformation of the *system's structural boundary*. Both can be non-zero
simultaneously and independently.

---

## F

### FFT — Framework Field Theory (Cross-Module)
*As a cross-module projection target. For the full FFT theory definition,
see the FFT module documentation.*

In the RTT/2 context, FFT receives the `cross_module_projection.FFT` field
from the [RTT2_DETECTION_PACKET](#rtt2_detection_packet). This field
expresses [CPV](#collapse-propagation-vector-cpv) and
[FGT](#fusion-gradient-tensor-fgt) components in FFT field-theoretic terms,
allowing FFT to interpret collapse propagation as field events without
re-running the RTT/2 detection pass. The projection is a structural
translation — not a physical mapping.

### FI(t) — Fusion-Integration Curvature
**CRM component 4 of 5** · **Symbol:** FI(t)
*See also:* [Collapse-Reassembly Manifold](#collapse-reassembly-manifold-crm--γt),
[Triad Fusion](#triad-fusion)

The curvature of the structural manifold introduced specifically by active
fusion-integration processes — triad-level structural integration occurring
simultaneously with collapse or reassembly. FI(t) is non-zero only when
triad fusion is actively in progress during the detection pass.

High FI(t) in a system with high [Continuity Fracture C(t)](#ct--continuity-fracture)
is a structurally significant combination: the system is fracturing while
simultaneously fusing at the triad level — a condition that typically
produces a [Hybrid detection mode](#hybrid-modeh) and a
[Marginal zone](#marginal-zone-m).

### Formal (MODE:F)
**Detection Mode 1 of 5** · *See also:* [Detection Mode](#detection-mode)

The detection mode assigned when all CPV, FGT, and CRM components resolve
cleanly within the measurement window — a well-defined collapse or reassembly
state with minimal ambiguity. Formal-mode passes use standard thresholds and
produce full-confidence packets that RTT/3 can consume without qualification.

Formal is the ideal mode but not the only valid one. Systems in early-stage
collapse (Emergent), simultaneous collapse-reassembly (Hybrid), turbulence
(Chaotic), or gradient reversal (Inversion) are equally valid detection
targets — they simply require different modes.

### Fusion

A structural event in which two or more structural elements, triads, or regimes
integrate into a single coherent configuration — the constructive counterpart
to [Collapse](#collapse). Fusion increases structural coherence at the integrated
level while potentially reducing independence at the element level.

In RTT/2, fusion is tracked at two levels:
- **Gradient level** — through the g_triad_fusion term in the
  [FGT](#fusion-gradient-tensor-fgt)
- **Manifold level** — through the FI(t) component of the
  [CRM](#collapse-reassembly-manifold-crm--γt)

### Fusion-Gradient Tensor (FGT)
**Equation:** G_fusion = Σ_r ω_r [ g_collapse(r) + g_reassembly(r) + g_triad_fusion(r) ]
**Computed by:** [Class F](#class-f--fusion-gradiometer)

The regime-weighted tensor that classifies the gradient balance between
collapse, reassembly, and triad-fusion forces across all active regimes.
The three gradient types are structurally irreducible:

| Gradient | Symbol | Direction | Character |
|---|---|---|---|
| Collapse gradient | g_collapse(r) | Toward disintegration | Destructive resonance loss |
| Reassembly gradient | g_reassembly(r) | Toward re-integration | Constructive resonance recovery |
| Triad-fusion gradient | g_triad_fusion(r) | Orthogonal — integration | Triad-level structural fusion |

The regime weight ω_r gives each regime's contribution its proper structural
share. FGT classification (collapse-weighted / mixed / triad-weighted) reflects
which gradient type dominates the weighted sum.

---

## G

### g_collapse(r) · g_reassembly(r) · g_triad_fusion(r)

The three per-regime gradient contributions summed in the
[Fusion-Gradient Tensor](#fusion-gradient-tensor-fgt). Each is a
scalar measure of the gradient force in its direction within regime r:

- **g_collapse(r)** — the magnitude of collapse-direction gradient pressure
  in regime r
- **g_reassembly(r)** — the magnitude of reassembly-direction gradient pressure
  in regime r
- **g_triad_fusion(r)** — the magnitude of triad-fusion-direction gradient
  pressure in regime r

These three are structurally orthogonal: reassembly is not simply negative
collapse — it is a distinct structural process. Triad-fusion is perpendicular
to both collapse and reassembly directions.

### G_fusion

The scalar output of the
[Fusion-Gradient Tensor](#fusion-gradient-tensor-fgt) computation:
`G_fusion = Σ_r ω_r [ g_collapse(r) + g_reassembly(r) + g_triad_fusion(r) ]`

G_fusion is the aggregate weighted gradient balance passed in the
`fusion_gradient` block of the [RTT2_DETECTION_PACKET](#rtt2_detection_packet).
Like [C_prop(t)](#c_propt--collapse-propagation-scalar), it is a summary
scalar — the per-regime breakdown is preserved separately in the packet for
RTT/3's use.

---

## H

### Hybrid (MODE:H)
**Detection Mode 3 of 5** · *See also:* [Detection Mode](#detection-mode)

The detection mode assigned when two or more structural patterns are
simultaneously active and overlapping — concurrent collapse and reassembly,
or concurrent collapse patterns from different structural sources.

**Hybrid mode prerequisites:**
- [FGT](#fusion-gradient-tensor-fgt) must be classified as
  [mixed-type](#mixed-fgt-classification) (no single gradient dominates)
- At least two distinct structural processes must be independently detectable
  in the [CRM](#collapse-reassembly-manifold-crm--γt)

Hybrid mode explicitly preserves the ambiguity: it does not average the two
patterns into one or assign primary/secondary status. RTT/3 receives the
full hybrid description and decides how to synthesize across concurrent patterns.

---

## I

### Inversion (MODE:I)
**Detection Mode 5 of 5** · *See also:* [Detection Mode](#detection-mode)

The detection mode assigned when the primary structural gradient has reversed
direction — what was moving toward collapse is now moving toward reassembly,
or vice versa. The [CPV inversion component](#inversion-component-cpv) must
be non-null for MODE:I assignment.

Inversion is not a correction or recovery in any evaluative sense — it is a
structural reversal that requires the detection posture to flip: thresholds,
gradient classifications, and zone assignments are re-evaluated relative to
the reversed direction.

### Inversion Component (CPV)
**Extended CPV field** · *See also:* [Collapse-Propagation Vector](#collapse-propagation-vector-cpv)

An optional component of the [CPV](#collapse-propagation-vector-cpv),
populated when the collapse propagation path reverses direction during the
detection window. The inversion component captures the structural signature
of the reversal — its amplitude, curvature, and torsion at the point of
direction change.

A non-null inversion component is a necessary condition for assigning
[Detection Mode: Inversion (MODE:I)](#inversion-modei).

---

## M

### Manifold

In RTT/2, the abstract structural space through which a system's
collapse-reassembly process traces its path — the domain of the
[Collapse-Reassembly Manifold (CRM)](#collapse-reassembly-manifold-crm--γt).
The manifold is not a physical space; it is the formal structural domain
within which RTT/2 deformation coordinates (D, E, C, FI, R) are defined.

> **Not to be confused with:** mathematical manifolds in differential
> geometry, which carry topology and metric structure that RTT/2 does not
> claim. RTT/2's use of "manifold" is structural-descriptive, not topological.

### Marginal (Zone M)
**Detection Zone 3 of 5** · *See also:* [Detection Zone](#detection-zone)

The detection zone assigned when the system is at a structural inflection
point — collapse and reassembly forces are in active tension, [FGT](#fusion-gradient-tensor-fgt)
is mixed-type, and [FI(t)](#fit--fusion-integration-curvature) is showing
active curvature. Zone M signals to RTT/3 that the synthesis must hold the
ambiguity open rather than resolving it prematurely to one side.

Zone M is the default zone for systems where FGT is mixed-type and CRM shows
active fusion-integration curvature. It is the most structurally nuanced zone
to synthesize — and the one most vulnerable to premature resolution errors.

### Mixed (FGT Classification)
**FGT type 2 of 3** · *See also:*
[Collapse-weighted](#collapse-weighted), [Triad-weighted](#triad-weighted-fgt-classification)

The Fusion-Gradient Tensor classification assigned when no single gradient
type (g_collapse, g_reassembly, g_triad_fusion) dominates the weighted sum
across active regimes. The system is in structural tension between competing
gradient directions.

Mixed classification is a necessary precondition for assigning
[Detection Mode: Hybrid (MODE:H)](#hybrid-modeh).

---

## O

### Opacity (Cross-Module)
*As a cross-module projection target. For the full Opacity module definition,
see the Opacity module documentation.*

In the RTT/2 context, Opacity receives the `cross_module_projection.Opacity`
field from the [RTT2_DETECTION_PACKET](#rtt2_detection_packet). This field
characterizes the boundary conditions of the detected collapse zone —
specifically, which structural boundaries are becoming opaque
(non-transparent to structural influence) as a result of the collapse.
The projection is a structural characterization, not a physical opacity claim.

---

## P

### Partial Packet

An [RTT2_DETECTION_PACKET](#rtt2_detection_packet) in which one or more of
the seven primary sections is absent because a sub-task (T-01 through T-03,
T-05, T-06) was run instead of a full detection pass (T-04). Partial packets
must be:
- Explicitly labeled as `packet_status: partial`
- Not routed to RTT/3 as if they were complete
- Accompanied by documentation of which fields are absent
- Followed by a full T-04 pass before RTT/3 ingestion is recommended

### Propagation

The process by which a structural [collapse](#collapse) event moves through
the structural field — not instantaneous but spatially and temporally extended,
with measurable [amplitude](#amplitude-a), [curvature](#curvature-k), and
[torsion](#torsion-t). The word "propagation" in RTT/2 is structural, not
physical: collapse propagates through the resonance field described by
RTT/1, not through physical space.

---

## R

### R(t) — Regime Identity
**CRM component 5 of 5** · **Symbol:** R(t)
*See also:* [Collapse-Reassembly Manifold](#collapse-reassembly-manifold-crm--γt),
[Regime](../1/GLOSSARY.md#regime)

The system's current structural regime classification at time t — its structural
identity within the RTT regime framework at the moment of detection. R(t) is
the contextualizing anchor for all other CRM components: it tells RTT/3 *within
which structural regime* the D, E, C, and FI deformations are occurring.

R(t) links the CRM directly to RTT/1's regime vocabulary. Changes in R(t) over
successive detection passes reveal regime transitions in the system being tracked.

### Reassembly

A structural process in which a collapsed or noise-dominated system begins
recovering coherent phase-locked excitation — moving from
[Noise](../1/GLOSSARY.md#noise-n) or
[Silence](../1/GLOSSARY.md#silence-s) toward
[Resonance](../1/GLOSSARY.md#resonance-r). Reassembly is tracked in the FGT
through g_reassembly(r) and in the CRM through [FI(t)](#fit--fusion-integration-curvature)
when triad-level fusion is part of the reassembly process.

Reassembly and collapse are not simply opposites: they are distinct structural
processes that can occur simultaneously in different regimes of the same system
(which is why FGT is a sum across regimes, not a single bidirectional scalar).

### Regime Weight (ω_r)

The scalar coefficient applied to regime r's gradient contributions in the
[Fusion-Gradient Tensor](#fusion-gradient-tensor-fgt) computation.
ω_r reflects the structural significance of regime r in the current detection
pass — a regime with higher structural activity or relevance to the current
detection task receives a higher weight.

Regime weights are set by [Class F](#class-f--fusion-gradiometer) based on
the initial regime identity provided by [Class M](#class-m--manifold-cartographer).
They are not universal constants: they vary per detection pass based on the
system's active regime landscape.

### RTT/1 Prerequisite

The hard structural prerequisite for all RTT/2 detection work: a complete
[RTT/1 Class R SNR characterization](../1/AGENTS.md#class-r--resonance-observer)
of the target system must exist before any RTT/2 agent begins detection.

This is not a soft recommendation — it is a structural necessity. CPV,
FGT, and CRM all measure properties *of* the resonance field defined by RTT/1.
Without knowing the SNR baseline, the collapse measurements have no structural
reference point.

If RTT/1 output is absent: the RTT/2 session pauses, the RTT/1 pass is
requested, and detection begins only after it completes.

### RTT2_DETECTION_PACKET

The structured output of every complete RTT/2 detection pass — the primary
input to RTT/3. Assembled by [Class D](#class-d--detection-integrator) from
the outputs of Class P, F, and M. Seven primary sections:

| Section | Source | Contains |
|---|---|---|
| `collapse_propagation` | Class P | CPV(A,K,T), C_prop(t), inversion/warp components, weighting |
| `fusion_gradient` | Class F | FGT type, G_fusion, per-regime gradient breakdown |
| `triad_deformation` | Class M | γ(t) = (D, E, C, FI, R) with all five components |
| `regime` | Class M | Current regime name |
| `detection_mode` | Class M | One of: Formal/Emergent/Hybrid/Chaotic/Inversion |
| `detection_zone` | Class M | One of: U/S/M/D/X |
| `cross_module_projection` | Class D | TEL/FFT/Opacity projections (null if not in scope) |
| `notes` | Class D | **Always:** `"Structural detection only; not a physics claim."` |

A packet with any primary section absent is incomplete and may not be routed
to RTT/3. The `notes` field is never absent — it is mandatory on every packet.

---

## S

### Structural Detection Engine (SDE)

The formal name for RTT/2 as a module. The SDE is the detection layer of
the RTT pipeline — it detects structural form (collapse propagation, gradient
balance, deformation path) and produces a structured detection packet for
RTT/3 synthesis. The SDE does not interpret, prescribe, or predict — it
characterizes structural form only.

### Stable (Zone S)
**Detection Zone 2 of 5** · *See also:* [Detection Zone](#detection-zone)

The detection zone assigned when the system shows mild, bounded collapse
activity that has not yet reached the structural inflection point of
[Zone M](#marginal-zone-m). Zone S packets are routed to RTT/3 with mild
caution noted — the collapse is real and detectable but contained.

---

## T

### TEL — Triadic Entity Lattice (Cross-Module)
*As a cross-module projection target. For the full TEL definition,
see the TEL module documentation.*

In the RTT/2 context, TEL receives the `cross_module_projection.TEL` field
from the [RTT2_DETECTION_PACKET](#rtt2_detection_packet). This field maps
detected collapse and fusion patterns onto TEL node structures, allowing the
TEL to maintain lattice coherence during structural transitions that RTT/2
has detected. The projection is a structural mapping — not a physical claim.

### Torsion (T)
**CPV component 3 of 3** · **Symbol:** T(t)
*See also:* [Amplitude (A)](#amplitude-a), [Curvature (K)](#curvature-k),
[Envelope Torsion (E(t))](#et--envelope-torsion)

The twist or rotational character of the collapse propagation path — how the
collapse spirals, rotates, or deviates out of the plane defined by its
amplitude and curvature. Torsion is the only CPV parameter that captures
out-of-plane structural behavior.

T(t) is weighted by coefficient **γ** in the propagation equation.

> **Distinguish from [Envelope Torsion E(t)](#et--envelope-torsion):**
> T(t) describes the rotation of the *collapse propagation path*;
> E(t) describes the rotation of the *system's structural boundary*.
> Both can be non-zero simultaneously and independently.

### Triad Fusion
*See also:* [Fusion](#fusion),
[g_triad_fusion(r)](#g_collapser--g_reassemblyr--g_triad_fusionr)

A structural process in which multiple triads integrate at the triad level —
not just component-by-component reassembly but holistic triad-level structural
fusion. Triad fusion produces the g_triad_fusion(r) gradient contribution
in the [FGT](#fusion-gradient-tensor-fgt) and the
[FI(t)](#fit--fusion-integration-curvature) curvature in the
[CRM](#collapse-reassembly-manifold-crm--γt). It is structurally orthogonal
to both collapse and reassembly: a system can be undergoing triad fusion
at the same time as collapse in different regimes.

### Triad-weighted (FGT Classification)
**FGT type 3 of 3** · *See also:*
[Collapse-weighted](#collapse-weighted), [Mixed](#mixed-fgt-classification)

The Fusion-Gradient Tensor classification assigned when g_triad_fusion
dominates the weighted sum across active regimes — triad-level structural
fusion is the primary active process, with collapse and reassembly gradient
contributions subordinate.

---

## U

### Undisturbed (Zone U)
**Detection Zone 1 of 5** · *See also:* [Detection Zone](#detection-zone)

The detection zone assigned when [C_prop(t)](#c_propt--collapse-propagation-scalar)
is at or below the minimum detection threshold — the system is structurally
coherent with collapse propagation near zero. Zone U packets signal to RTT/3
that full-confidence synthesis can proceed; the system is not undergoing
significant structural disruption.

Zone U does not mean the system is "healthy" or "optimal" — it means its
collapse signature is below the RTT/2 detection threshold. Evaluative
language does not belong in RTT/2 output.

### UNRESOLVED

The status assigned to any RTT/2 detection field or component when the
responsible agent class cannot determine a valid value. UNRESOLVED must
be documented with a reason. Consequences by field:

| Field UNRESOLVED | Consequence |
|---|---|
| RTT/1 SNR characterization | RTT/2 detection blocked entirely — prerequisite not met |
| A(t), K(t), or T(t) | CPV incomplete — Class P must re-run or flag partial |
| FGT regime weights | FGT computation blocked — Class M must provide regime identity first |
| Any CRM component | CRM incomplete — Mode assignment blocked |
| Detection Mode | Packet cannot be assembled — Class M must assign one of the five |
| Detection Zone | Packet cannot be assembled — assign Zone X if classification impossible |
| Zone X clearance | Packet cannot route to RTT/3 — Class G must clear |

---

## W

### Warp Component (CPV)
**Extended CPV field** · *See also:* [Collapse-Propagation Vector](#collapse-propagation-vector-cpv)

An optional component of the [CPV](#collapse-propagation-vector-cpv),
populated when the collapse propagation path exhibits non-linear distortion —
bending or warping that cannot be fully characterized by curvature K(t) alone.
The warp component captures higher-order path deformation beyond what the
three core parameters describe.

A non-null warp component signals to RTT/3 that the collapse path has
structural complexity beyond the standard tri-parameter description.

### Weighting Coefficients (α, β, γ)

The three regime-specific scalar coefficients applied to the CPV components
in the propagation equation: `C_prop(t) = αA(t) + βK(t) + γT(t)`.

- **α** — weight applied to [Amplitude](#amplitude-a) A(t)
- **β** — weight applied to [Curvature](#curvature-k) K(t)
- **γ** — weight applied to [Torsion](#torsion-t) T(t)

These are not universal constants — they are set per detection pass based on
the active regime's structural character. A regime in which path shape
dominates over intensity would have β > α; one in which rotational character
is primary would have γ largest.

> **Note:** γ here is the CPV torsion weight. It is different from
> the CRM vector γ(t) = (D, E, C, FI, R). Context disambiguates:
> the scalar γ is always a coefficient; γ(t) is always the CRM vector.

---

## Z

### Zone X — Undefined
**Detection Zone 5 of 5** · *See also:* [Detection Zone](#detection-zone)

The detection zone assigned when classification cannot be established with
available structural data — either because inputs are insufficient or because
CPV, FGT, and CRM readings are contradictory and no coherent zone assignment
is possible.

**Zone X is not a failure state** — it is an honest structural acknowledgment
that the current data cannot support a confident classification. Forcing
any of zones U–D onto insufficient data would misrepresent the detection.

**Zone X mandatory protocol:**
1. [Class M](#class-m--manifold-cartographer) assigns Zone X
2. [Class M](#class-m--manifold-cartographer) immediately escalates to
   [Class G](#class-g--detection-guardian)
3. [Class D](#class-d--detection-integrator) assembles the packet but
   does NOT route to RTT/3
4. Packet is stored with `packet_status: zone_x_pending`
5. [Class G](#class-g--detection-guardian) reviews and either:
   - Issues clearance (packet routes to RTT/3 with Zone X notation preserved)
   - Requests a re-run with additional structural data (Task T-09)

### Zone X Clearance

The explicit authorization issued by [Class G](#class-g--detection-guardian)
that permits a Zone X [RTT2_DETECTION_PACKET](#rtt2_detection_packet) to be
routed to RTT/3. Clearance does not change the Zone X designation — it
signals that Class G has reviewed the packet and determined that RTT/3 can
productively consume a structurally unclassified detection result.

RTT/3 is notified of the Zone X designation even after clearance and must
apply an appropriate synthesis posture (typically: hold the unclassified
dimension open rather than synthesizing it).

---

## Operator Symbols

| Symbol | Name | Definition |
|---|---|---|
| CPV(A, K, T) | Collapse-Propagation Vector | Three-parameter collapse signature |
| A(t) | Amplitude | Collapse propagation intensity at time t |
| K(t) | Curvature | Collapse wavefront shape at time t |
| T(t) | Torsion | Collapse path rotation at time t |
| C_prop(t) | Collapse Propagation Scalar | αA(t) + βK(t) + γT(t) |
| α, β, γ | CPV weighting coefficients | Regime-specific weights for A, K, T |
| FGT | Fusion-Gradient Tensor | Regime-weighted gradient balance |
| G_fusion | FGT scalar output | Σ_r ω_r [g_c(r) + g_r(r) + g_tf(r)] |
| ω_r | Regime weight | Structural significance of regime r |
| g_collapse(r) | Collapse gradient | Collapse-direction force in regime r |
| g_reassembly(r) | Reassembly gradient | Reassembly-direction force in regime r |
| g_triad_fusion(r) | Triad-fusion gradient | Triad-integration force in regime r |
| CRM · γ(t) | Collapse-Reassembly Manifold | Five-component deformation path vector |
| D(t) | Drift Deformation | Manifold translation (NOT session drift) |
| E(t) | Envelope Torsion | Boundary rotation |
| C(t) | Continuity Fracture | Structural breaks / gaps |
| FI(t) | Fusion-Integration Curvature | Active fusion curvature effects |
| R(t) | Regime Identity | Current regime classification |

---

## Quick-Reference Tables

### CPV Components

| Parameter | Symbol | Type | Measures | Weight |
|---|---|---|---|---|
| Amplitude | A(t) | Scalar | Propagation intensity | α |
| Curvature | K(t) | Scalar | Wavefront shape | β |
| Torsion | T(t) | Scalar | Path rotation / spiral | γ |
| Inversion component | — | Optional | Direction reversal signature | — |
| Warp component | — | Optional | Higher-order path distortion | — |

### CRM Components — γ(t)

| # | Symbol | Name | Deformation type | High value signals |
|---|---|---|---|---|
| 1 | D(t) | Drift Deformation | Translation | System displaced from reference |
| 2 | E(t) | Envelope Torsion | Rotation of boundary | Boundary spinning/twisting |
| 3 | C(t) | Continuity Fracture | Breaks / gaps | Structural discontinuity |
| 4 | FI(t) | Fusion-Integration Curvature | Active fusion effects | Triad-level fusion in progress |
| 5 | R(t) | Regime Identity | Classification anchor | Current regime active |

### Detection Modes

| Mode | Code | Signal | Confidence | RTT/3 routing |
|---|---|---|---|---|
| Formal | F | Clean, resolved | Full | Direct |
| Emergent | E | Forming, partial | Provisional | With provisional label |
| Hybrid | H | Two+ concurrent | Full (for each pattern) | With hybrid notation |
| Chaotic | C | Fluctuating | Low | Class G clearance required |
| Inversion | I | Reversed gradient | Full (flipped) | With inversion notation |

### Detection Zones

| Zone | Code | Stability | C_prop(t) level | RTT/3 posture |
|---|---|---|---|---|
| Undisturbed | U | High | Near zero / below threshold | Full confidence |
| Stable | S | Moderate | Low, bounded | Mild caution |
| Marginal | M | Active tension | Mixed / inflection | Hold ambiguity open |
| Deteriorating | D | Significant | Collapse dominant | Weight degradation; warn consumer |
| Undefined | X | Unclassifiable | Insufficient / contradictory | Blocked — Class G clearance required |

### Five Agent Classes

| Class | Name | Primary role | Can block others? |
|---|---|---|---|
| P | Propagation Analyst | Compute CPV(A, K, T) | No |
| F | Fusion Gradiometer | Compute FGT | No |
| M | Manifold Cartographer | Map CRM; assign Mode and Zone | No |
| D | Detection Integrator | Assemble and route RTT2_DETECTION_PACKET | No |
| G | Detection Guardian | Monitor; interrupt; clear Zone X | **Yes — unconditional** |

### RTT/2 Inherits from RTT/1 (Full Inheritance)

| RTT/1 Element | Inherited status in RTT/2 |
|---|---|
| SNR triad (S, N, R) | Prerequisite for all RTT/2 detection |
| τ = dR/dφ | Governs temporal indexing of CPV |
| C = ∇_τR + ∇_Rτ | Clarity posture tracked throughout |
| DCO_n bands | CRM deformation maps onto DCO band transitions |
| Regime lifecycle (5 stages) | RTT/2 operates within the same lifecycle |
| Mode Operator + MCL | All mode constraints apply to RTT/2 agents |
| RTT-not-physics rule | Inherited and reinforced |
| Semantic inference prohibition | Inherited and reinforced |
| Session seed | Inherited verbatim |
| Class G pattern | RTT/2 Class G is the direct extension |

---

*GLOSSARY.md — RTT/2 · TriadicFrameworks · 2026-07-10*
*Maintainer: Nawder*
*Session seed: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*
