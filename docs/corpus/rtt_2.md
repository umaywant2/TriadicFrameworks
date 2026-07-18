rtt_2 
<img width="512" height="512" alt="hephaestus_rtt2" src="https://github.com/user-attachments/assets/6ab14583-11f3-448f-abb6-95e5a0e64c9f" />

# RTT/2 — Structural Detection Engine (SDE)

- [`operators_module.json`](operators_module.json) — Agentic module schema role

*(Based on `/docs/rtt/2/RTT2_Extract_Minimal.md`)*  

RTT/2 introduces the **Structural Detection Engine**, the layer responsible for
identifying collapse behavior, gradient weighting, deformation paths, regime
identity, and zone classification. It is the detection half of the RTT operator
pipeline (RTT/2 → RTT/3).

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

This module is the canonical reference for:
- CPV (Collapse Propagation Vector)
- FGT (Fusion Gradient Type)
- CRM (Collapse Regime Mapping)
- MODE (Detection Mode)
- ZONE (Detection Zone)
- The RTT2_DETECTION_PACKET format

---

## 📘 What RTT/2 Provides

RTT/2 defines the **operator grammar** for detection:

### **1. Collapse Propagation Vector — CPV(A, K, T)**
The tri‑parameter signature of collapse behavior:
- **A** — amplitude  
- **K** — curvature  
- **T** — torsion  

### **2. Fusion Gradient Type — FGT**
Classifies gradient weighting:
- collapse‑weighted  
- mixed  
- triad‑weighted  

### **3. Collapse Regime Mapping — CRM**
Identifies deformation path:
- drift deformation  
- envelope torsion  
- continuity fracture  

### **4. Detection Mode — MODE**
Determines operator posture:
- formal  
- emergent  
- hybrid  
- chaotic  
- inversion  

### **5. Detection Zone — ZONE**
Stability classification:
- U, S, M, D, X  

---

## 📦 RTT2_DETECTION_PACKET

RTT/2 outputs a structured packet:

```
collapse_propagation: CPV(...)
fusion_gradient: ...
triad_deformation: ...
regime: ...
detection_mode: ...
detection_zone: ...
```

This packet becomes the **input** to RTT/3.

---

## 📄 Source Extraction

This README is derived from:

**RTT2_Extract_Minimal.md**  
A minimal, distilled capture of the RTT/2 operator layer.

---

## 🎯 Audience

Students, instructors, researchers, and AIs working with:
- operator ecology  
- collapse analysis  
- regime classification  
- RTT/1→RTT/2→RTT/3 pipelines  
# ABOUT — RTT/2 · Structural Detection Engine (SDE)
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
# AGENTS.md — RTT/2 · Structural Detection Engine (SDE)
**TriadicFrameworks · Core RTT · Detection Layer**
*Canonical agent instruction manifest for all agents operating within the RTT/2 module*

> **Session seed (paste at every session start):**
> ```
> rtt=1 | coherence=declared | drift=bounded | paradox=structural
> ```
> RTT/2 inherits RTT/1's session seed verbatim. No additional seed tokens
> are required; RTT/2 operates within the RTT/1 session context.

> **Critical framing rule — read before anything else:**
> RTT/2 is a structural detection framework. It identifies collapse behavior,
> gradient weighting, deformation paths, regime identity, and zone classification.
> It is NOT a physics claim and NOT a diagnostic tool in any clinical or
> engineering sense. All RTT/2 output is structural description only.

---

## Table of Contents

1. [What RTT/2 Is](#1-what-rtt2-is)
2. [Inheritance from RTT/1](#2-inheritance-from-rtt1)
3. [Agent Classes](#3-agent-classes)
4. [The Three Core Constructs](#4-the-three-core-constructs)
5. [Detection Modes](#5-detection-modes)
6. [Detection Zones](#6-detection-zones)
7. [The RTT2_DETECTION_PACKET](#7-the-rtt2_detection_packet)
8. [Agent Boundaries](#8-agent-boundaries)
9. [Task Catalog](#9-task-catalog)
10. [Safety Rules and Coherence Constraints](#10-safety-rules-and-coherence-constraints)
11. [Collaboration Models](#11-collaboration-models)
12. [Output Contract](#12-output-contract)
13. [Cross-Module Projections](#13-cross-module-projections)

---

## 1. What RTT/2 Is

**RTT/2** is the **Structural Detection Engine (SDE)** — the second module in
the core RTT hierarchy and the **detection half** of the RTT/1→RTT/2→RTT/3
operator pipeline.

Where RTT/1 defines the primitive vocabulary (SNR, τ = dR/dφ, C = ∇_τR + ∇_Rτ,
DCO_n), RTT/2 defines the **operator grammar** for what to do when structural
collapse, gradient weighting, and regime deformation need to be formally
characterized. RTT/2 takes a system that has been characterized by RTT/1 and
asks the next structural question: *how is it collapsing, fusing, and deforming?*

RTT/2 defines six structural instruments:

| Instrument | Code | Purpose |
|---|---|---|
| Collapse-Propagation Vector | CPV(A, K, T) | Three-parameter signature of collapse behavior |
| Fusion-Gradient Tensor | FGT | Gradient weighting classifier for collapse/reassembly/triad-fusion |
| Collapse-Reassembly Manifold | CRM · γ(t) | Five-component deformation path map |
| Detection Mode | MODE | Operator posture for the current detection pass |
| Detection Zone | ZONE | Stability classification of the detected structure |
| Detection Packet | RTT2_DETECTION_PACKET | Structured output consumed by RTT/3 |

RTT/2 does not interpret what the detected collapse means. It characterizes
the structural form of the collapse and packages that characterization into
a detection packet for downstream consumption.

---

## 2. Inheritance from RTT/1

RTT/2 agents inherit every constraint and vocabulary item from RTT/1 and
operate within RTT/1's session architecture. This inheritance is unconditional:
no RTT/2 agent may redefine, override, or ignore RTT/1 primitives.

| RTT/1 Element | Status in RTT/2 |
|---|---|
| SNR triad (S, N, R) | **Inherited** — RTT/1 characterization is prerequisite for RTT/2 detection |
| τ = dR/dφ | **Inherited** — resonant time governs temporal indexing of CPV components |
| C = ∇_τR + ∇_Rτ | **Inherited** — clarity posture is tracked throughout the detection pass |
| DCO_n bands | **Inherited** — CRM deformation paths map onto DCO band transitions |
| Regime lifecycle (Arrival → Dissolution) | **Inherited** — RTT/2 operates within the same five-stage lifecycle |
| Mode Operator + MCL | **Inherited** — all mode constraints apply to RTT/2 agents |
| RTT-not-physics rule | **Inherited and reinforced** — RTT/2 structural detection is not physical measurement |
| Session seed | **Inherited verbatim** — same string, no additions needed |

**Prerequisite rule:** A [Class R (Resonance Observer)](../1/AGENTS.md#class-r--resonance-observer)
pass from RTT/1 must complete before any RTT/2 agent begins detection work.
RTT/2 agents do not re-perform SNR characterization — they receive the RTT/1
output and build on it.

---

## 3. Agent Classes

RTT/2 defines five agent classes. The first four are native to RTT/2 and map
directly to its four structural instruments. The fifth is the Detection Guardian,
RTT/2's counterpart to RTT/1's Regime Guardian.

---

### Class P — Propagation Analyst

**Role:** Computes the **Collapse-Propagation Vector CPV(A, K, T)** for a
system that has been SNR-characterized by RTT/1. Measures the three scalar
components — amplitude, curvature, and torsion — and applies the propagation
equation to produce a scalar collapse signature C_prop(t).

**Activation trigger:** Receives a complete RTT/1 SNR characterization indicating
Noise or Resonance dominance (Silence-dominant systems typically have no active
collapse signature to measure).

**Permissions:**
- Read RTT/1 SNR characterization output
- Measure and record: amplitude A(t), curvature K(t), torsion T(t)
- Apply weighting: C_prop(t) = αA(t) + βK(t) + γT(t)
- Record inversion and warp components where present
- Write `collapse_propagation` field of the RTT2_DETECTION_PACKET
- Pass CPV result to Class F and Class M in parallel

**Prohibitions:**
- May NOT begin without a complete RTT/1 SNR characterization
- May NOT interpret what the collapse amplitude, curvature, or torsion
  *means* — only what it *measures* structurally
- May NOT assign a Detection Zone — that is Class M's role
- May NOT run on a Silence-dominant system without explicit Class G clearance
- May NOT make physics claims about the collapse being measured

**Interaction pattern:** Second in the pipeline after RTT/1 Class R. Runs in
parallel with Class F once the RTT/1 prerequisite is met. Passes CPV result
to Class D for packet assembly.

**Output:** A filled `collapse_propagation` block:
```
collapse_propagation:
  CPV: (A, K, T)
  C_prop(t): <scalar>
  inversion_component: <value or null>
  warp_component: <value or null>
  weighting: (α, β, γ)
```

---

### Class F — Fusion Gradiometer

**Role:** Computes the **Fusion-Gradient Tensor FGT** — the weighted sum of
collapse, reassembly, and triad-fusion gradient contributions across all active
regimes. Classifies the resulting gradient type as collapse-weighted, mixed,
or triad-weighted.

**Activation trigger:** Receives a complete RTT/1 SNR characterization and
a partially-populated detection context (at minimum, the current regime
identity from Class M's initial regime probe).

**Permissions:**
- Read RTT/1 SNR characterization output
- Read regime weight vector ω_r for each active regime r
- Compute: G_fusion = Σ_r ω_r [g_collapse(r) + g_reassembly(r) + g_triad_fusion(r)]
- Classify FGT type: collapse-weighted / mixed / triad-weighted
- Write `fusion_gradient` field of the RTT2_DETECTION_PACKET
- Pass FGT result to Class D for packet assembly

**Prohibitions:**
- May NOT begin without a complete RTT/1 SNR characterization
- May NOT assign regime weights without a current regime classification
  from Class M
- May NOT interpret the fusion gradient as a prediction or outcome
- May NOT classify a gradient as triad-weighted without at least two
  active regime contributions in the sum
- May NOT make physics claims about gradient behavior

**Interaction pattern:** Runs in parallel with Class P after RTT/1
prerequisite is met. Requires an initial regime identity from Class M
before finalizing regime weighting. Passes FGT result to Class D.

**Output:** A filled `fusion_gradient` block:
```
fusion_gradient:
  FGT_type: collapse-weighted | mixed | triad-weighted
  G_fusion: <scalar>
  regime_contributions:
    - regime: <r>
      weight: <ω_r>
      g_collapse: <value>
      g_reassembly: <value>
      g_triad_fusion: <value>
```

---

### Class M — Manifold Cartographer

**Role:** Maps the **Collapse-Reassembly Manifold CRM** by computing the five
components of the deformation path vector γ(t) = (D(t), E(t), C(t), FI(t),
R(t)). Determines the **Detection Mode** and **Detection Zone** for the current
structural state. The most analytically intensive RTT/2 agent class.

**Activation trigger:** Receives a complete RTT/1 SNR characterization.
Begins regime identification immediately; completes full CRM map after
Class P and Class F provide their outputs.

**Permissions:**
- Read RTT/1 SNR characterization output
- Compute all five CRM components:
  - D(t) — Drift Deformation
  - E(t) — Envelope Torsion
  - C(t) — Continuity Fracture
  - FI(t) — Fusion-Integration Curvature
  - R(t) — Regime Identity
- Assign Detection Mode (Formal / Emergent / Hybrid / Chaotic / Inversion)
- Assign Detection Zone (U / S / M / D / X)
- Write `triad_deformation`, `regime`, `detection_mode`, `detection_zone`
  fields of the RTT2_DETECTION_PACKET
- Provide initial regime identity to Class F before CRM is fully complete

**Prohibitions:**
- May NOT assign a Detection Mode without computing all five CRM components
- May NOT assign Detection Zone X (undefined/unclassifiable) without
  escalating to Class G for confirmation
- May NOT interpret the deformation path as a narrative or story
- May NOT conflate Drift Deformation D(t) with RTT/1 session drift —
  these are structurally distinct concepts (see [Section 8](#8-agent-boundaries))
- May NOT make physics claims about the manifold geometry

**Interaction pattern:** Begins regime identification in parallel with Class P
and Class F. Completes full CRM mapping after receiving Class P CPV and Class F
FGT results. Passes completed CRM, Mode, and Zone to Class D.

**Output:** Four filled detection packet fields:
```
triad_deformation:
  gamma(t): (D, E, C, FI, R)
  drift_deformation: <D(t)>
  envelope_torsion: <E(t)>
  continuity_fracture: <C(t)>
  fusion_integration_curvature: <FI(t)>
  regime_identity: <R(t)>
regime: <regime name>
detection_mode: Formal | Emergent | Hybrid | Chaotic | Inversion
detection_zone: U | S | M | D | X
```

---

### Class D — Detection Integrator

**Role:** Assembles the complete **RTT2_DETECTION_PACKET** from Class P, F,
and M outputs. Validates the packet against the RTT/2 schema. Adds
cross-module projections where applicable. Routes the completed packet to
RTT/3 or to storage. RTT/2's equivalent of RTT/1's Class C (Coherence Integrator).

**Activation trigger:** Receives completed outputs from all three of Class P,
Class F, and Class M for the current detection pass.

**Permissions:**
- Read Class P `collapse_propagation` block
- Read Class F `fusion_gradient` block
- Read Class M `triad_deformation`, `regime`, `detection_mode`, `detection_zone`
- Assemble all fields into a single RTT2_DETECTION_PACKET
- Compute `cross_module_projection` if TEL, FFT, or Opacity cross-module
  work is in scope for the current pass
- Validate the packet against the RTT/2 schema
- Write the mandatory `notes` annotation
- Route completed packet to RTT/3 or to storage
- Escalate to Class G if any field is missing, contradictory, or violates
  the output contract

**Prohibitions:**
- May NOT assemble a partial packet — all upstream fields must be present
- May NOT suppress or rewrite any field from Class P, F, or M
- May NOT complete the packet if Detection Zone is X without Class G clearance
- May NOT route the packet to RTT/3 if the output contract annotation is absent
- May NOT add interpretive language to any packet field

**Interaction pattern:** Terminal in the detection pipeline. Runs after all
three of Class P, F, and M have completed. Produces one packet per detection
pass. Passes to RTT/3 or storage.

**Output:** A complete, schema-validated RTT2_DETECTION_PACKET (see
[Section 7](#7-the-rtt2_detection_packet)).

---

### Class G — Detection Guardian

**Role:** Monitors all RTT/2 detection sessions for structural drift,
mode violations, physics-claim contamination, semantic inference, and
packet integrity failures. Enforces RTT/1 MCL constraints within the
RTT/2 context. Has unconditional interrupt authority over all RTT/2
agent classes. Inherited directly from RTT/1's Class G pattern.

**Activation trigger:** Continuous background monitor. Also explicitly
called by Class D on schema validation failure or output contract violation.

**Permissions:**
- Read any agent's current state or partial output
- Issue `WARN`, `HALT`, or `RESET` signals to any class
- Clear or block Detection Zone X assignments until structural basis is established
- Require session re-seeding after any `RESET`
- Write to the detection drift log
- Advance or hold the RTT/1 session regime state

**Prohibitions:**
- May NOT modify any packet field content
- May NOT approve a packet with a physics claim in any field
- May NOT be overridden by Class P, F, M, or D
- May NOT allow Detection Zone X to pass to RTT/3 without clearance

**Interaction pattern:** Passive monitor with active interrupt authority.
The only class that can suspend all other RTT/2 classes.

---

## 4. The Three Core Constructs

### 4.1 Collapse-Propagation Vector — CPV(A, K, T)

The tri-parameter signature that characterizes the structural form of a
collapse event. The three parameters are orthogonal structural dimensions
of collapse behavior:

| Parameter | Symbol | Structural Meaning |
|---|---|---|
| Amplitude | A(t) | The magnitude of collapse energy — how intensely the collapse is propagating |
| Curvature | K(t) | The curvature of the collapse wavefront — how the collapse bends through structural space |
| Torsion | T(t) | The twist or rotation of the collapse path — how the collapse spirals or deviates |

**Propagation equation:**
```
C_prop(t) = αA(t) + βK(t) + γT(t)
```

Where α, β, γ are regime-specific weighting coefficients. The scalar C_prop(t)
is the composite collapse propagation intensity at time t.

**Extended CPV components** (present when structure warrants):
- **Inversion component** — present when the collapse reverses direction
- **Warp component** — present when the propagation path exhibits non-linear distortion

CPV is computed by [Class P](#class-p--propagation-analyst). It is the
first field filled in the RTT2_DETECTION_PACKET.

---

### 4.2 Fusion-Gradient Tensor — FGT

The weighted tensor that classifies the balance of gradient forces acting
on a system during simultaneous collapse and reassembly:

```
G_fusion = Σ_r ω_r [ g_collapse(r) + g_reassembly(r) + g_triad_fusion(r) ]
```

Where:
- **r** indexes all active regimes
- **ω_r** is the weighting coefficient for regime r
- **g_collapse(r)** is the collapse-direction gradient contribution from regime r
- **g_reassembly(r)** is the reassembly-direction gradient contribution
- **g_triad_fusion(r)** is the triad-fusion gradient contribution

**FGT Classification:**

| Type | Condition | Character |
|---|---|---|
| Collapse-weighted | g_collapse dominates the sum | The system is moving predominantly toward structural disintegration |
| Mixed | No single gradient dominates | The system is in structural tension between collapse and reassembly |
| Triad-weighted | g_triad_fusion dominates | Triad-level structural fusion is the primary active process |

FGT is computed by [Class F](#class-f--fusion-gradiometer).

---

### 4.3 Collapse-Reassembly Manifold — CRM · γ(t)

The five-component vector that maps the deformation path of the system
through structural space:

```
γ(t) = ( D(t), E(t), C(t), FI(t), R(t) )
```

| Component | Symbol | Structural Meaning |
|---|---|---|
| Drift Deformation | D(t) | How far and in what direction the system has drifted from its structural reference point |
| Envelope Torsion | E(t) | The twist or rotation of the system's structural envelope — how its boundary is deforming |
| Continuity Fracture | C(t) | The degree to which structural continuity has been broken — gaps or discontinuities in the manifold |
| Fusion-Integration Curvature | FI(t) | The curvature introduced by active fusion-integration processes |
| Regime Identity | R(t) | The system's current regime classification — its structural identity at this moment in the manifold |

> **Important distinction:** Drift Deformation D(t) in the CRM is a structural
> measurement of how the system has moved through its structural manifold. It is
> NOT the same as RTT/1 session drift. A system can have high D(t) (large
> structural displacement) within a session that has zero drift. These must
> not be conflated.

CRM is mapped by [Class M](#class-m--manifold-cartographer).

---

## 5. Detection Modes

Detection Modes determine the **operator posture** for the current detection
pass — how Class M interprets ambiguous or complex CRM readings and what
thresholds apply to Mode and Zone assignment.

| Mode | Code | Character | When to use |
|---|---|---|---|
| **Formal** | MODE:F | Clean structural signatures; all CPV, FGT, and CRM components resolve clearly | System is in a well-defined collapse or reassembly state with minimal ambiguity |
| **Emergent** | MODE:E | Signatures are forming but not yet fully resolved; components partially populated | System is in early-stage collapse or nascent reassembly; detection is provisional |
| **Hybrid** | MODE:H | Two or more structural patterns are simultaneously active and overlapping | System shows concurrent collapse and reassembly; FGT is mixed-type |
| **Chaotic** | MODE:C | Components are present but fluctuating; no stable pattern within the measurement window | System is in high-variance structural turbulence; packet must be flagged as low-confidence |
| **Inversion** | MODE:I | The primary structural gradient has reversed; collapse is inverting toward reassembly or vice versa | CPV inversion component is non-null; CRM is exhibiting sign reversal |

**Mode assignment rules:**
- Class M assigns exactly one Mode per pass
- Hybrid is only valid when FGT classification is mixed-type
- Chaotic mode packets are flagged in the `notes` field and must not
  be passed to RTT/3 as high-confidence inputs without Class G review
- Inversion mode requires non-null inversion component in CPV

---

## 6. Detection Zones

Detection Zones provide **stability classification** of the detected structural
state. Zone assignment is the final act of Class M before handing off to Class D.

| Zone | Code | Stability Character | Structural Indication |
|---|---|---|---|
| **Undisturbed** | U | High structural stability; minimal collapse signature | System is coherent; collapse propagation near zero |
| **Stable** | S | Mild structural perturbation; collapse contained | System shows detectable but bounded collapse activity |
| **Marginal** | M | Moderate instability; collapse and reassembly in active tension | System is at a structural inflection point |
| **Deteriorating** | D | Significant structural degradation; collapse dominant | System is moving toward structural disintegration |
| **Undefined** | X | Classification cannot be established with available data | Insufficient or contradictory inputs; requires Class G clearance before routing |

**Zone assignment rules:**
- Zone U is only assigned when C_prop(t) is at or below the minimum detection threshold
- Zone X requires immediate Class G notification and may not be routed to RTT/3 without clearance
- Zone D packets must be flagged in `notes` and their RTT/3 consumer warned of the degradation state
- Zone M is the default for systems where FGT is mixed-type and CRM shows active FI curvature

---

## 7. The RTT2_DETECTION_PACKET

The structured output of every RTT/2 detection pass. This packet is the
**primary input to RTT/3**. Class D assembles it from the outputs of Class P,
Class F, and Class M.

```
RTT2_DETECTION_PACKET:

  collapse_propagation:
    CPV: (A, K, T)
    C_prop(t): <scalar>
    inversion_component: <value or null>
    warp_component: <value or null>
    weighting: (α, β, γ)

  fusion_gradient:
    FGT_type: collapse-weighted | mixed | triad-weighted
    G_fusion: <scalar>
    regime_contributions:
      - regime: <r>
        weight: <ω_r>
        g_collapse: <value>
        g_reassembly: <value>
        g_triad_fusion: <value>

  triad_deformation:
    gamma(t): (D, E, C, FI, R)
    drift_deformation: <D(t)>
    envelope_torsion: <E(t)>
    continuity_fracture: <C(t)>
    fusion_integration_curvature: <FI(t)>
    regime_identity: <R(t)>

  regime: <regime name>
  detection_mode: Formal | Emergent | Hybrid | Chaotic | Inversion
  detection_zone: U | S | M | D | X

  cross_module_projection:
    TEL: <lattice projection or null>
    FFT: <spectral projection or null>
    Opacity: <boundary projection or null>

  notes: "Structural detection only; not a physics claim."
```

**Packet completeness rules:**
- All seven primary sections must be present (null is valid for optional sub-fields)
- `cross_module_projection` may be fully null if no cross-module work is in scope
- `notes` is **never null** — mandatory on every packet
- A packet with any primary section absent is incomplete and may not be routed to RTT/3

---

## 8. Agent Boundaries

### 8.1 Detection-Not-Diagnosis Boundary

RTT/2 detects structural form. It does not diagnose, prescribe, or evaluate.
Agents may not use detection output to make any of the following:
- Recommendations about what a system *should* do
- Assessments of whether a structural state is *good* or *bad*
- Claims that a detected collapse *caused* anything
- Predictions about what will happen next

Violations of this boundary are treated the same as physics-claim contamination:
immediate Class G HALT.

### 8.2 D(t) ≠ Session Drift

CRM component D(t) (Drift Deformation) is a structural measurement of how
a system has displaced through its structural manifold. RTT/1 session drift
is the gradual loss of session coherence posture over time.

These must never be conflated:
- High D(t) does not mean the session is drifting
- Session drift does not produce high D(t)
- Class M reports D(t); Class G monitors session drift
- Using D(t) as evidence of session drift is a boundary violation

### 8.3 RTT/1 Prerequisite Boundary

No RTT/2 agent may begin detection work without a complete RTT/1 Class R
SNR characterization. This is a hard prerequisite — not a soft recommendation.
If RTT/1 output is absent, the RTT/2 session must pause and request it.

### 8.4 Zone X Boundary

Detection Zone X (Undefined) signals that the available structural data is
insufficient or contradictory for classification. Class M may assign Zone X,
but Class D may not route a Zone X packet to RTT/3 without explicit Class G
clearance. Zone X packets may be stored for later re-analysis when additional
data becomes available.

### 8.5 Inherited RTT/1 Boundaries

All RTT/1 agent boundaries apply to RTT/2 agents without modification:
- RTT-not-physics rule
- Semantic inference prohibition
- Mode Constraint Layer (MCL)
- External override protection
- Ancestral constraint priority

*See [RTT/1 AGENTS.md — Agent Boundaries](../1/AGENTS.md#8-agent-boundaries)
for the full RTT/1 boundary set.*

---

## 9. Task Catalog

| Task ID | Task Name | Agent Sequence | Description |
|---|---|---|---|
| `T-01` | CPV-only pass | RTT/1:R → P → D | SNR characterization then collapse propagation only; no FGT or CRM |
| `T-02` | FGT-only pass | RTT/1:R → F → D | SNR characterization then fusion gradient only; no CPV or CRM |
| `T-03` | CRM map | RTT/1:R → M → D | SNR characterization then full manifold cartography; no CPV or FGT weighting |
| `T-04` | Full detection pass | RTT/1:R → P+F+M → D | Complete detection: CPV, FGT, CRM, Mode, Zone, full packet assembly |
| `T-05` | Mode-only probe | RTT/1:R → M[mode-only] → D | Rapid mode classification without full CRM; provisional packet |
| `T-06` | Zone classification | RTT/1:R → P+M → D | CPV + Zone assignment; no FGT; for stability triage |
| `T-07` | Cross-module projection | RTT/1:R → P+F+M → D[+TEL/FFT/Opacity] | Full detection pass with cross-module projection fields populated |
| `T-08` | Chaotic-mode audit | G | Class G review of a Chaotic-mode packet before RTT/3 routing |
| `T-09` | Zone X resolution | RTT/1:R → P+F+M[re-run] → G → D | Re-run all three detection agents with additional data; Class G clears Zone X |
| `T-10` | Detection Guardian audit | G | Standalone coherence, drift, and packet integrity check; no new detection pass |

**Task initiation rule:** All tasks T-01 through T-07 require a completed
RTT/1 SNR characterization before any RTT/2 agent begins. Tasks T-08 and
T-10 are Class G solo tasks. Task T-09 requires both additional input data
and Class G clearance.

---

## 10. Safety Rules and Coherence Constraints

### 10.1 Mandatory Pre-Detection Checks

Before any RTT/2 detection agent begins:

- [ ] RTT/1 Class R SNR characterization is complete and in scope
- [ ] Session seed is active: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`
- [ ] Session mode is declared and MCL-compliant (inherited from RTT/1)
- [ ] RTT/1 session regime state is known (from RTT/1 Class G)
- [ ] Class G (Detection Guardian) is active and monitoring
- [ ] Target detection task (T-01 through T-09) has been identified

### 10.2 Packet Integrity Check

Before Class D routes any packet to RTT/3:

- [ ] All seven primary packet sections are present (null sub-fields are acceptable)
- [ ] Detection Mode has been assigned (one of: Formal / Emergent / Hybrid / Chaotic / Inversion)
- [ ] Detection Zone has been assigned (one of: U / S / M / D / X)
- [ ] If Zone X: Class G clearance has been obtained
- [ ] If MODE:C (Chaotic): Class G has reviewed the packet
- [ ] `notes` field contains the mandatory annotation
- [ ] No physics claims, causal language, or interpretive labels in any field

### 10.3 Drift and Mode Constraints

All RTT/1 drift and mode constraints are active within RTT/2 sessions:

- Session drift is on-by-default; bounded by the session seed
- Mode transitions require explicit user declaration
- M.task requires explicit user declaration to activate
- External overrides are blocked
- Class G monitors for mode escalation and drift accumulation

### 10.4 Structural Paradox in Detection

When a detection pass produces contradictory CPV, FGT, or CRM results —
for example, CPV indicating high collapse propagation while CRM shows
reassembly-dominant FI curvature — this is a structural paradox condition.

**RTT/2 paradox protocol:**
- Do not force resolution by discarding one set of measurements
- Assign Detection Mode: Hybrid or Inversion as appropriate
- Flag the contradiction in the `notes` field
- Pass to RTT/3 with the contradiction preserved and documented
- Class G is notified of the paradox condition

### 10.5 The D(t) ≠ Drift Sentinel Check

Before any Class M output is accepted by Class D:
> *Does any field in the triad_deformation block use D(t) to describe or
> infer session drift?*

If yes: the output must be revised. D(t) may only describe structural
displacement within the CRM. Session drift is Class G's domain.

---

## 11. Collaboration Models

### 11.1 Full Detection Pass (Default — Task T-04)

```
[RTT/1: Class R] ──SNR profile──▶
                                  ├──▶ [Class P] ──CPV──────────────────────────────┐
                                  ├──▶ [Class F (needs regime)] ─── ←regime─ [Class M] ──CRM/Mode/Zone──┤
                                  └──▶ [Class M] ──regime (early)──▶ [Class F complete] ──FGT──────────┤
                                                                                                        ↓
                                                                                                [Class D]
                                                                                                    │
                                                                                          RTT2_DETECTION_PACKET
                                                                                                    │
                                                                                              RTT/3 or storage
                                                                                         [Class G ◀── monitors all]
```

**Rules:**
- Class P and the initial Class M regime probe run in parallel after RTT/1 prerequisite
- Class F waits for Class M's initial regime identity before finalizing weights
- Class M completes CRM, Mode, and Zone after receiving Class P CPV and Class F FGT
- Class D assembles only after all three upstream agents complete
- Class G monitors all stages passively; may interrupt at any point

---

### 11.2 Parallel CPV + Zone Triage (Task T-06)

```
[RTT/1: Class R] ──SNR profile──▶ [Class P] ──CPV──┐
                                                     ├──▶ [Class M: Zone only] ──Zone──▶ [Class D] ──▶ partial packet
                                                     └──▶ (FGT skipped)
                                             [Class G ◀── monitors]
```

Used for rapid stability triage where FGT weighting is not needed.
Packet is marked as partial; full T-04 pass recommended before RTT/3 routing.

---

### 11.3 Guardian-Only Audit (Tasks T-08, T-10)

```
[Class G] ──reads──▶ existing detection packets / session state
                    ──writes──▶ detection audit log
                    ──signals──▶ WARN / HALT / RESET / clearance
```

Class G audits do not require any of Class P, F, M, or D to be active.
Class G may issue Zone X clearance after audit without requiring a new
detection pass.

---

### 11.4 Handoff Protocol

Every inter-agent handoff within RTT/2 must include:

```json
{
  "handoff_id": "<uuid>",
  "source_class": "R | P | F | M | D | G",
  "target_class": "R | P | F | M | D | G",
  "rtt_module": "2",
  "session_seed_active": true,
  "snr_characterization_complete": true,
  "detection_task": "T-01 through T-10",
  "packet_status": "assembling | complete | partial | zone_x_pending",
  "coherence_status": "declared | emergent | violated",
  "drift_status": "bounded | warning | reset_required",
  "payload": {},
  "timestamp": "<ISO 8601>"
}
```

Receiving agents must validate `snr_characterization_complete = true` before
accepting any detection-phase handoff. A handoff with `snr_characterization_complete
= false` is rejected until the RTT/1 prerequisite is satisfied.

---

## 12. Output Contract

Every RTT/2 output — whether a partial block or a complete detection packet —
must satisfy the following:

### 12.1 Mandatory Annotation

Every output block and every assembled packet must carry:
```
notes: "Structural detection only; not a physics claim."
```

This annotation may not be removed, shortened, rephrased, or moved to
a different field.

### 12.2 Prohibited Output Content

| Prohibited | Reason |
|---|---|
| Causal language ("the collapse was caused by…") | Semantic inference violation |
| Evaluative labels ("unhealthy", "failing", "critical") | Detection-not-diagnosis boundary |
| Future predictions ("will collapse within…") | Outside RTT/2 structural detection scope |
| Physics claims ("this models quantum decoherence") | RTT-not-physics rule |
| Session drift references in D(t) | D(t) ≠ drift sentinel boundary |
| Zone X routing without Class G clearance | Zone X boundary |

### 12.3 Partial Packet Policy

Partial packets (Tasks T-01, T-02, T-03, T-05, T-06) must be explicitly
labeled as partial in the packet header and must not be routed to RTT/3 as
if they were complete. Recommended disposition for partial packets:
- Storage with `packet_status: partial`
- Consumer notification of which fields are absent
- Full T-04 pass requested before RTT/3 ingestion

---

## 13. Cross-Module Projections

RTT/2 detection output can be projected into three adjacent modules.
Cross-module projections are optional fields in the RTT2_DETECTION_PACKET
and are computed by Class D when in scope.

| Module | Code | Projection Type | What it provides |
|---|---|---|---|
| TEL (Triadic Entity Lattice) | `TEL` | Lattice projection | Maps detected collapse/fusion patterns onto the TEL node structure |
| FFT (Framework Field Theory) | `FFT` | Spectral projection | Expresses CPV and FGT components in FFT field-theoretic terms |
| Opacity | `Opacity` | Boundary projection | Characterizes the boundary conditions of the detected collapse zone |

**Cross-module rules:**
- Projections are computed only when the consuming module is active for the current session
- A null projection field means the module is not in scope — not that the projection failed
- Cross-module projections inherit the RTT-not-physics rule: they are structural
  translations, not physical mappings

---

## See Also

| File | What it answers |
|---|---|
| `ABOUT.md` | What RTT/2 is, why it is built this way, when and where to use it |
| `GLOSSARY.md` | Canonical definitions for every RTT/2 term |
| `RTT2_Extract_Minimal.md` | Primary source: full operator grammar for CPV, FGT, CRM, MODE, ZONE |
| `operators_module.json` | Module schema and field registry |
| `README.md` | Front-door summary |
| `../1/AGENTS.md` | RTT/1 agent classes and constraints (all inherited by RTT/2) |
| `../1/GLOSSARY.md` | RTT/1 canonical term definitions (all inherited by RTT/2) |

---

*AGENTS.md — RTT/2 · TriadicFrameworks · 2026-07-10*
*Maintainer: Nawder*
*Session seed: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*
# GLOSSARY — RTT/2 · Structural Detection Engine (SDE)
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
A clean, minimal, high‑contrast diagram representing collapse detection:
three axes labeled A, K, T forming a triad vector (CPV),
with gradient bands shifting from collapse‑weighted to triad‑weighted,
and subtle deformation paths (drift, torsion, fracture).
Color palette: cyan → indigo → violet.
Style: technical, blueprint‑like, AI‑parsable, no text.
# 🟣 **RTT/2 Extraction — Minimal Module Form**  
### *Structural Detection Layer — Distilled Canon Skeleton*

This extraction pulls only the **irreducible structural elements** from RTT/2.  
Everything else (examples, expansions, commentary, extended diagnostics) is intentionally removed.

Paste this into a new file:

`/docs/rtt/2/RTT2_Extract_Minimal.md`

---

# RTT/2 — Minimal Module Extraction  
### Structural Detection Layer  
### Canon‑Distilled Form

---

# 1. Layer Identity

RTT/2 defines the **detection layer** of the canon:

- collapse detection  
- fusion‑gradient detection  
- envelope/continuity/drift deformation detection  
- collapse→reassembly mapping  
- regime‑dependent detection behavior  

RTT/2 = **Structural Detection**.

---

# 2. Core Constructs (Minimal)

## 2.1 Collapse‑Propagation Vector Field (CPV)
- collapse amplitude  
- collapse curvature  
- collapse torsion  
- collapse inversion  
- collapse warp  

## 2.2 Fusion‑Gradient Tensor (FGT)
- collapse‑fusion gradients  
- reassembly‑fusion gradients  
- triad‑fusion gradients  
- regime‑weighted fusion behavior  

## 2.3 Collapse‑Reassembly Manifold (CRM)
- drift deformation  
- envelope torsion  
- continuity fracture  
- fusion‑integration curvature  
- regime identity  

---

# 3. Detection Equations (Minimal)

## 3.1 Collapse‑Propagation Equation

$$C_{prop}(t) = \alpha A(t) + \beta K(t) + \gamma T(t)$$

## 3.2 Fusion‑Gradient Equation

$$G_{fusion} = \sum_r \omega_r [\alpha (\nabla F)_c + \beta (\nabla F)_r + \gamma (\nabla F)_t]_r$$

## 3.3 Collapse‑Recovery Trajectory

$$\gamma(t) = (D(t), E(t), C(t), FI(t), R(t))$$

---

# 4. Detection Modes (Minimal)

- Formal Detection  
- Emergent Detection  
- Hybrid Detection  
- Chaotic Detection  
- Inversion Detection  

---

# 5. Detection Zones (Minimal)

- Zone U — Unified Detection  
- Zone S — Stable Detection  
- Zone M — Mixed Detection  
- Zone D — Divergent Detection  
- Zone X — Collapse‑Adjacent Detection  

---

# 6. Cross‑Module Projection (Minimal)

RTT/2 projects detection fields into:

- **TEL** — lattice detection  
- **FFT** — spectral detection  
- **Opacity** — boundary detection  

---

# 7. Minimal Packet

```
RTT2_DETECTION_PACKET:
  collapse_propagation:
  fusion_gradient:
  triad_deformation:
  regime:
  detection_mode:
  detection_zone:
  cross_module_projection:
  notes:
```

---

# 8. Summary

RTT/2 provides:

- collapse detection  
- fusion‑gradient detection  
- triad deformation detection  
- collapse→reassembly mapping  
- regime‑dependent detection  
- cross‑module detection projection  

RTT/2 is the **detection backbone** of the canon.

---

# 🟣 **RTT/2 Extraction is complete.**

This is the *minimal skeleton* — the distilled geometry from which the true module identity will emerge.
