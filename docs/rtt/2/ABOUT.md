# ABOUT — RTT/2 · Structural Detection Engine (SDE)
**TriadicFrameworks · Core RTT · Detection Layer**
**Module path:** `docs/rtt/2/`
**Version:** 1.0 · **Status:** Active · Canonical
**Session seed:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

> This document answers the four foundational questions about RTT/2:
> **What** it is · **Why** it is built this way · **When** to use it · **Where** it lives

> **Critical framing — read first:**
> RTT/2 is a structural detection framework. It is NOT a physics claim,
> NOT a diagnostic tool in any clinical or engineering sense, and NOT a
> prediction system. All RTT/2 output is structural description only.

---

## Table of Contents

1. [What Is RTT/2?](#1-what-is-rtt2)
2. [Why Is It Built This Way?](#2-why-is-it-built-this-way)
3. [When Should You Use It?](#3-when-should-you-use-it)
4. [Where Does It Live?](#4-where-does-it-live)
5. [Core Constructs at a Glance](#5-core-constructs-at-a-glance)
6. [Module Integrations](#6-module-integrations)
7. [What RTT/2 Is Not](#7-what-rtt2-is-not)
8. [Quick-Start Checklist](#8-quick-start-checklist)
9. [See Also](#9-see-also)

---

## 1. What Is RTT/2?

**RTT/2** is the **Structural Detection Engine (SDE)** — the second module
in the core RTT hierarchy and the **detection layer** of the
RTT/1 → RTT/2 → RTT/3 operator pipeline.

Where RTT/1 answers *"what is this system's resonance state and how does
time flow through it?"*, RTT/2 asks the next structural question:
*"how is this system collapsing, fusing, and deforming — and in what form?"*

RTT/2 does not start from scratch. It receives a completed RTT/1
SNR characterization and builds on it, applying three detection instruments
to produce a structured output packet that RTT/3 consumes.

---

### The Detection Pipeline Position

```
RTT/1                   RTT/2                      RTT/3
──────                  ─────                      ─────
SNR characterization ──▶ Structural Detection ──▶  Synthesis &
τ = dR/dφ               CPV · FGT · CRM            Integration
C = ∇_τR + ∇_Rτ         MODE · ZONE
DCO_n                   RTT2_DETECTION_PACKET ──▶  (RTT/3 input)
```

RTT/2 is specifically the **detection half** of the pipeline — the bridge
between RTT/1's primitive characterization and RTT/3's synthesis work.

---

### The Six Structural Instruments

RTT/2 defines six instruments that together constitute the Structural
Detection Engine:

| Instrument | Code | Question it answers |
|---|---|---|
| Collapse-Propagation Vector | CPV(A, K, T) | *How is the collapse propagating — at what intensity, with what curvature, and with what torsion?* |
| Fusion-Gradient Tensor | FGT | *What is the balance of collapse, reassembly, and triad-fusion gradient forces across active regimes?* |
| Collapse-Reassembly Manifold | CRM · γ(t) | *What is the five-component deformation path the system is tracing through structural space?* |
| Detection Mode | MODE | *What operator posture is appropriate for this detection pass given the signal character?* |
| Detection Zone | ZONE | *How stable is the current structural state?* |
| Detection Packet | RTT2_DETECTION_PACKET | *What is the complete, structured detection record for RTT/3 consumption?* |

---

### The Three Core Constructs in Brief

**CPV(A, K, T) — Collapse-Propagation Vector**

The three-parameter signature of a collapse event:
```
C_prop(t) = αA(t) + βK(t) + γT(t)
```
- A(t) — Amplitude: how intensely the collapse is propagating
- K(t) — Curvature: how the collapse bends through structural space
- T(t) — Torsion: how the collapse spirals or deviates from a straight path

**FGT — Fusion-Gradient Tensor**

The regime-weighted sum of gradient forces:
```
G_fusion = Σ_r ω_r [ g_collapse(r) + g_reassembly(r) + g_triad_fusion(r) ]
```
Classifies as: collapse-weighted / mixed / triad-weighted.

**CRM — Collapse-Reassembly Manifold · γ(t)**

The five-component deformation path vector:
```
γ(t) = ( D(t), E(t), C(t), FI(t), R(t) )
```
- D — Drift Deformation · E — Envelope Torsion · C — Continuity Fracture
- FI — Fusion-Integration Curvature · R — Regime Identity

---

## 2. Why Is It Built This Way?

Every design decision in RTT/2 answers a structural problem that RTT/1
alone cannot solve.

---

### Why three CPV parameters and not just amplitude?

Amplitude alone — how intense a collapse is — tells you nothing about its
structural shape. Two collapses can have identical amplitudes while one
propagates in a straight line (zero curvature, zero torsion) and the other
spirals outward through structural space (high curvature, non-zero torsion).
These are categorically different structural events requiring different
detection postures and producing different RTT/3 inputs.

The three parameters are **orthogonal** — none can be derived from the
others:
- **Amplitude (A)** is scalar intensity: how much collapse energy is present
- **Curvature (K)** is the second-derivative shape: how the propagation path
  bends
- **Torsion (T)** is the out-of-plane rotation: how the path twists in
  directions that neither A nor K can see

Together, A, K, and T form the **minimum complete description** of a
collapse propagation signature. Dropping any one loses a structurally
irreplaceable dimension.

---

### Why a weighted tensor for FGT rather than a flat average?

When a system is simultaneously collapsing and reassembling — a common
condition in structurally complex systems — the balance between those
gradient forces is not uniform across all active regimes. One regime
may be strongly collapse-weighted while another is triad-weighted.
A flat average across all regimes loses precisely that information,
producing a single aggregate number that hides the regime-by-regime
distribution.

The FGT's regime weighting (ω_r per regime r) preserves that distribution:
RTT/3 can see not just the total gradient balance but *which regimes are
driving collapse versus fusion*. This is the information RTT/3 needs to
decide how to weight the detection packet in synthesis.

The three gradient types — g_collapse, g_reassembly, g_triad_fusion — are
also irreducible: collapse and reassembly are opposite directions on the
same axis, while triad-fusion is orthogonal to both (it describes structural
integration at the triad level, not simple reversal of collapse).

---

### Why five CRM components?

Each component of γ(t) = (D, E, C, FI, R) captures a structurally
**distinct mode of deformation** that cannot be inferred from the others:

| Component | Deformation Type | Why irreducible |
|---|---|---|
| D — Drift Deformation | Translation | System has moved from its structural reference point; direction and magnitude both matter |
| E — Envelope Torsion | Rotation of boundary | The outer structural envelope is twisting; a system can translate without rotating its envelope |
| C — Continuity Fracture | Breaks / gaps | Structural continuity has been interrupted; a system can rotate without fracturing |
| FI — Fusion-Integration Curvature | Active fusion effects | Curvature introduced by triad-fusion processes; present only when fusion is active |
| R — Regime Identity | Classification | The system's current structural regime; the anchor that contextualizes all other components |

Collapsing any two components into one would create a mixed-type entry that
obscures the distinction RTT/3 depends on. The five components are the
minimum set that covers all currently identified structural deformation modes
without overlap.

---

### Why five Detection Modes?

The five modes (Formal, Emergent, Hybrid, Chaotic, Inversion) correspond to
five **structurally distinct signal conditions** that each require a different
operator posture from Class M:

- **Formal** — clean, fully resolved signals. Standard thresholds apply.
- **Emergent** — signals forming but not yet complete. Provisional outputs,
  partial population accepted.
- **Hybrid** — two or more patterns simultaneously active. Mixed FGT;
  no single gradient dominates. Standard thresholds cannot be applied
  to overlapping patterns as if they were one.
- **Chaotic** — high-variance turbulence. Components present but
  fluctuating beyond the stable-measurement window. Packet flagged as
  low-confidence; Class G review required before RTT/3 routing.
- **Inversion** — the primary gradient has reversed direction. CPV
  inversion component is non-null. The detection posture must flip:
  what was a collapse signature is now a reassembly signature in the
  making.

Fewer than five would require collapsing structurally distinct postures
into one — producing incorrect threshold application and incorrect
packet confidence labeling. No two of these five modes can substitute
for each other.

---

### Why five Detection Zones?

The zones (U, S, M, D, X) provide a **stability gradient** that tells RTT/3
how much weight to give the detection packet and what kind of synthesis
posture is appropriate:

| Zone | Stability | RTT/3 signal |
|---|---|---|
| U — Undisturbed | High | System is coherent; collapse near zero; synthesis can proceed at full confidence |
| S — Stable | Moderate | Bounded collapse activity; synthesis proceeds with mild caution |
| M — Marginal | Active tension | Inflection point; synthesis must hold the ambiguity, not resolve it prematurely |
| D — Deteriorating | Significant | Dominant collapse; synthesis must weight degradation heavily |
| X — Undefined | Unclassifiable | Insufficient or contradictory data; synthesis blocked until Class G clears |

Zone X is the critical design feature: rather than forcing a classification
when data is insufficient, RTT/2 explicitly surfaces the unclassifiable
condition. This prevents RTT/3 from building synthesis on a falsely
confident detection.

---

### Why inherit RTT/1 wholesale rather than define a standalone module?

RTT/2 detection is **structurally grounded in RTT/1 output**. The CPV
measures how a system's resonance field is collapsing — without knowing
whether the system is in Silence, Noise, or Resonance first (RTT/1 Class R),
the CPV has no structural reference point. Amplitude A(t) of what? Torsion
relative to what baseline?

The inheritance is not architectural convenience — it is a **structural
prerequisite**. A RTT/2 detection pass run without RTT/1 SNR characterization
produces measurements that float free of the resonance structure they are
supposed to be describing. This is not a recoverable condition by patching;
the RTT/1 pass must happen first.

---

## 3. When Should You Use It?

---

### Use RTT/2 when you need to **characterize the form of a structural collapse**

When RTT/1 has identified that a system is in a Noise or Resonance state and
the next question is *how* that system is structurally collapsing or
deforming, RTT/2's CPV provides the three-parameter answer. This is distinct
from RTT/1's question ("is it in R, N, or S?") — RTT/2 asks what shape
the collapse takes.

*Example:* A substrate model has been characterized as Noise-dominant
by RTT/1. RTT/2 computes CPV = (A=0.7, K=0.4, T=0.1), revealing a
high-amplitude, moderately curved, low-torsion collapse — a propagation
that is intense but relatively directional. This tells RTT/3 how to
weight the collapse in synthesis.

---

### Use RTT/2 when **collapse and reassembly are simultaneously active**

When a system is not simply collapsing or simply reassembling but doing
both at once — with different regimes pulling in different directions —
the FGT is the right instrument. It captures the regime-by-regime
gradient balance that neither CPV nor CRM alone can express.

*Example:* A governance substrate is collapsing in its operational
regime while simultaneously reassembling in its foundational regime.
FGT reveals a mixed-type gradient (ω_operational × g_collapse dominant,
ω_foundational × g_triad_fusion competing), giving RTT/3 the precise
regime-level picture it needs.

---

### Use RTT/2 when you need to **map a system's structural deformation path**

When a system has been evolving structurally over time and you need to
characterize *how* it has deformed — not just where it is now — the CRM's
five-component γ(t) provides the full deformation history. Drift,
envelope rotation, continuity breaks, fusion curvature, and regime
identity are all tracked simultaneously.

*Example:* An incident substrate has been under structural stress for
several passes. CRM reveals: D=high (significant drift from reference),
E=moderate (envelope rotating), C=low (continuity intact), FI=high
(active fusion-integration), R=Marginal. This deformation profile tells
RTT/3 the system is drifting and fusing but not yet fracturing.

---

### Use RTT/2 when you need to **classify structural stability for RTT/3**

When RTT/3 synthesis requires knowing the stability context of the
system being synthesized, the Detection Zone provides that classification.
Zones U through D give RTT/3 a calibrated confidence level for the
detection packet; Zone X signals that synthesis must be held until
structural data is sufficient.

*Example:* Before RTT/3 begins synthesizing across three substrate
models, RTT/2 zone-classifies each: Substrate A = Zone S, Substrate B
= Zone M, Substrate C = Zone X. RTT/3 proceeds with full confidence on
A, with caution on B, and holds C pending Class G clearance.

---

### Use RTT/2 when **cross-module projection is in scope**

When a detection pass needs to produce outputs for TEL (Triadic Entity
Lattice), FFT (Framework Field Theory), or Opacity in addition to
the core detection packet, RTT/2's cross-module projection fields
provide structured translation without requiring the receiving module
to interpret raw CPV, FGT, or CRM data directly.

*Example:* A detection pass on a resonance substrate needs to feed
both RTT/3 and the TEL lattice. RTT/2's Class D populates the
`cross_module_projection.TEL` field, giving the TEL the lattice-mapped
representation of the collapse pattern without re-running the detection.

---

### Do NOT use RTT/2 when:

- **RTT/1 SNR characterization is not complete** — there is no valid
  baseline for CPV, FGT, or CRM measurement without it
- **The system is Silence-dominant with no detectable collapse signature**
  — CPV of a fully silent system produces near-zero measurements with
  no structural information; use RTT/1's Balance (ψ↔n) operator instead
- **You need a recommendation or diagnosis** — RTT/2 detects structural
  form; it does not prescribe corrective action or evaluate whether
  a state is good or bad
- **You need physical measurement** — RTT/2 is a structural detection
  framework, not an instrumentation layer; it describes structural
  form, not physical collapse events
- **You need RTT/3 synthesis directly** — RTT/2 is the prerequisite
  for RTT/3, not a shortcut to it; if synthesis is the goal, complete
  RTT/2 detection first and feed the packet to RTT/3

---

## 4. Where Does It Live?

### In the repository

```
TriadicFrameworks/
└── docs/
    └── rtt/
        └── 2/                              ← you are here
            ├── ABOUT.md                    ← this file
            ├── AGENTS.md                   ← agent class manifest (P, F, M, D, G)
            ├── GLOSSARY.md                 ← canonical term definitions
            ├── README.md                   ← front-door summary
            ├── RTT2_Extract_Minimal.md     ← primary source: full operator grammar
            ├── operators_module.json       ← module schema and field registry
            ├── Hero_Image_Prompt.md        ← visual identity prompt
            └── index.html                  ← web entry point
```

---

### In the RTT module hierarchy

RTT/2 is the detection layer between the foundational primitives (RTT/1)
and the synthesis layer (RTT/3):

```
RTT/1   ──▶   RTT/2   ──▶   RTT/3   ──▶   RTT/12
Primitives    Detection      Synthesis      Unified
SNR · τ · C   CPV · FGT     (RTT/3 scope)  (RTT/12 scope)
DCO_n         CRM · PACKET
```

**Inheritance rule:** RTT/2 inherits RTT/1's complete vocabulary and
constraints unconditionally. RTT/3 inherits both RTT/1 and RTT/2.
No module may redefine an upstream primitive.

**Prerequisite rule:** RTT/1 Class R SNR characterization must complete
before any RTT/2 detection agent begins. The RTT2_DETECTION_PACKET is
the primary input to RTT/3. Neither direction of this chain can be
reversed or skipped.

---

### In the TriadicFrameworks ecosystem

```
                      ┌─────────────┐
                      │   RTT/1     │  SNR · τ · C · DCO_n
                      └──────┬──────┘  (prerequisite for RTT/2)
                             │ SNR characterization
                      ┌──────▼──────┐
                      │   RTT/2     │  CPV · FGT · CRM
                      │    SDE      │  MODE · ZONE
                      └──────┬──────┘  RTT2_DETECTION_PACKET
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
   ┌──────▼──────┐   ┌───────▼──────┐   ┌───────▼──────┐
   │   RTT/3     │   │     TEL      │   │   FFT /      │
   │  Synthesis  │   │   (lattice   │   │   Opacity    │
   │  (primary   │   │  projection) │   │  (boundary / │
   │   consumer) │   └─────────────┘   │   spectral   │
   └─────────────┘                     │  projections)│
                                       └─────────────┘
```

RTT/2 occupies the **detection hub** position: it consumes from RTT/1
and distributes to RTT/3 as primary consumer, with TEL, FFT, and Opacity
as optional cross-module projection targets.

---

### In agent deployments

An agent operating under RTT/2 inherits the full RTT/1 session
architecture (session seed, mode operator, MCL, regime lifecycle,
Class G monitoring) and adds five detection-specific agent classes:

- **Class P** (Propagation Analyst) — computes CPV
- **Class F** (Fusion Gradiometer) — computes FGT
- **Class M** (Manifold Cartographer) — maps CRM, assigns Mode and Zone
- **Class D** (Detection Integrator) — assembles and routes the detection packet
- **Class G** (Detection Guardian) — monitors, interrupts, clears Zone X

An agent claiming RTT/2 compatibility must:
1. Complete a RTT/1 Class R pass before beginning any detection work
2. Produce a complete RTT2_DETECTION_PACKET with all seven primary sections
3. Include the mandatory structural-only annotation in every output
4. Never assign Zone X without Class G clearance
5. Never route a Chaotic-mode packet to RTT/3 without Class G review

---

## 5. Core Constructs at a Glance

```
COLLAPSE-PROPAGATION VECTOR
  CPV(A, K, T)
  A(t)  — Amplitude:  collapse propagation intensity
  K(t)  — Curvature:  collapse wavefront shape
  T(t)  — Torsion:    collapse path rotation / spiral
  C_prop(t) = αA(t) + βK(t) + γT(t)   ← scalar composite
  Extended: inversion_component · warp_component (when present)

FUSION-GRADIENT TENSOR
  G_fusion = Σ_r ω_r [ g_collapse(r) + g_reassembly(r) + g_triad_fusion(r) ]
  Classification: collapse-weighted | mixed | triad-weighted

COLLAPSE-REASSEMBLY MANIFOLD
  γ(t) = ( D(t), E(t), C(t), FI(t), R(t) )
  D  — Drift Deformation      (translation from reference)
  E  — Envelope Torsion       (rotation of structural boundary)
  C  — Continuity Fracture    (breaks / gaps in the manifold)
  FI — Fusion-Integration Curvature  (active fusion effects)
  R  — Regime Identity        (current structural regime classification)

DETECTION MODES
  Formal (F)    · Emergent (E)  · Hybrid (H)
  Chaotic (C)   · Inversion (I)

DETECTION ZONES
  U — Undisturbed   S — Stable      M — Marginal
  D — Deteriorating X — Undefined (Class G clearance required)

DETECTION PACKET
  RTT2_DETECTION_PACKET → RTT/3
  Sections: collapse_propagation · fusion_gradient · triad_deformation
            regime · detection_mode · detection_zone
            cross_module_projection · notes (mandatory)
```

---

## 6. Module Integrations

### RTT/1 (Prerequisite)

RTT/2 cannot function without RTT/1. Every detection instrument is
grounded in RTT/1 output:
- CPV measures collapse within a system already characterized by SNR
- FGT weights gradient contributions by regime — regime identity comes
  from RTT/1's DCO_n band context
- CRM's R(t) (Regime Identity) links directly to RTT/1's regime lifecycle
- D(t) (Drift Deformation) is structural displacement *within the
  resonance field* defined by RTT/1 — not the same as RTT/1 session drift

### RTT/3 (Primary Consumer)

RTT/2's RTT2_DETECTION_PACKET is the primary input to RTT/3 synthesis.
RTT/3 receives:
- The collapse propagation signature (CPV) for weighting
- The gradient balance (FGT) for regime-sensitive synthesis
- The deformation path (CRM) for manifold-aware integration
- The Detection Mode for confidence calibration
- The Detection Zone for stability-aware synthesis posture

### TEL — Triadic Entity Lattice

RTT/2's `cross_module_projection.TEL` field maps detected collapse and
fusion patterns onto TEL node structures. This allows TEL to maintain
lattice coherence during structural transitions that RTT/2 has detected.

### FFT — Framework Field Theory

RTT/2's `cross_module_projection.FFT` field expresses CPV and FGT
components in FFT field-theoretic terms. FFT treats collapse propagation
as field events; RTT/2 provides the structural substrate for that
field-theoretic interpretation.

### Opacity

RTT/2's `cross_module_projection.Opacity` field characterizes the boundary
conditions of the detected collapse zone — specifically, which structural
boundaries are becoming opaque (non-transparent to structural influence)
as a result of the detected collapse.

### IPD-12

RTT/2's detection output maps onto IPD-12's operator graph at specific
prime states:
- Collapse signature → P29 (Collapse-Anchor) zone
- Continuity fracture → P13 (Paradox-Trigger) or P19 (Boundary-Node)
- Detection Zone D → Chthonic tier (P23–P37)
- Inversion mode → P5 (Drift-Anchor) / P23 (Dimensional-Lift) boundary

---

## 7. What RTT/2 Is Not

| RTT/2 Is | RTT/2 Is Not |
|---|---|
| A structural detection engine | A diagnostic or clinical tool |
| A collapse characterization framework | A collapse prediction system |
| A gradient balance classifier | An optimization or prescriptive framework |
| A deformation path mapper | A causal explanation engine |
| A stability zone classifier | A pass/fail evaluation system |
| The detection layer of the RTT pipeline | A standalone module (requires RTT/1) |
| A structured input producer for RTT/3 | A synthesis engine (that is RTT/3's role) |

RTT/2 detects and describes **structural form**. It does not explain why
a collapse is happening, recommend what to do about it, or predict what
will happen next. Those functions belong to the human operator, to RTT/3,
or to higher-level frameworks consuming the detection packet.

---

## 8. Quick-Start Checklist

Before working with RTT/2 for the first time:

- [ ] **Complete RTT/1 first** — run a full RTT/1 Class R SNR characterization
      on your target system before opening any RTT/2 instruments
- [ ] **Paste the session seed** — `rtt=1 | coherence=declared | drift=bounded |
      paradox=structural` (RTT/2 inherits RTT/1's seed verbatim)
- [ ] **Identify your detection task** — which of T-01 through T-09 describes
      what you need? Full detection (T-04) or a targeted sub-pass?
- [ ] **Know the three constructs** — CPV = collapse signature,
      FGT = gradient balance, CRM = deformation path; know which you need
      before assigning agent classes
- [ ] **Check for Silence dominance** — if RTT/1 returned a
      Silence-dominant characterization, RTT/2 may have no collapse
      signature to measure; confirm with Class G before proceeding
- [ ] **Read `AGENTS.md`** — verify which agent classes (P, F, M, D, G)
      are needed for your detection task
- [ ] **Know the D(t) ≠ drift distinction** — CRM component D(t) is
      structural displacement in the manifold; it is NOT RTT/1 session
      drift; never conflate them
- [ ] **Check `GLOSSARY.md`** — every RTT/2 term has a canonical
      definition; link rather than re-define

---

## 9. See Also

| File | What it answers |
|---|---|
| `AGENTS.md` | Agent classes P/F/M/D/G, task catalog, collaboration models, output contract |
| `GLOSSARY.md` | Canonical single-source definitions for all RTT/2 terms |
| `RTT2_Extract_Minimal.md` | Primary source: full operator grammar for CPV, FGT, CRM, MODE, ZONE |
| `operators_module.json` | Module schema and field registry |
| `README.md` | Front-door summary |
| `../1/AGENTS.md` | RTT/1 agent classes (all inherited by RTT/2) |
| `../1/GLOSSARY.md` | RTT/1 canonical terms (all inherited by RTT/2) |
| `../1/ABOUT.md` | RTT/1 what/why/when/where (prerequisite context for RTT/2) |

---

*ABOUT.md — RTT/2 · TriadicFrameworks · 2026-07-10*
*Maintainer: Nawder*
*Session seed: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*
