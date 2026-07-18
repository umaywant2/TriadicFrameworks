# ABOUT — RTT/3 · Integration–Emission Layer
**TriadicFrameworks · Core RTT · Integration–Emission Layer**
**Module path:** `docs/rtt/3/`
**Version:** 1.0 · **Status:** Active · Canonical
**Session seed:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

> This document answers the four foundational questions about RTT/3:
> **What** it is · **Why** it is built this way · **When** to use it · **Where** it lives

> **Critical framing — read first:**
> RTT/3 is a structural integration and emission framework. It is NOT a physics
> claim, NOT a signal-processing system, and NOT a physical emitter. All
> constructs describe structural form only.

---

## Table of Contents

1. [What Is RTT/3?](#1-what-is-rtt3)
2. [Why Is It Built This Way?](#2-why-is-it-built-this-way)
3. [When Should You Use It?](#3-when-should-you-use-it)
4. [Where Does It Live?](#4-where-does-it-live)
5. [Core Equations at a Glance](#5-core-equations-at-a-glance)
6. [Module Integrations](#6-module-integrations)
7. [What RTT/3 Is Not](#7-what-rtt3-is-not)
8. [Quick-Start Checklist](#8-quick-start-checklist)
9. [See Also](#9-see-also)

---

## 1. What Is RTT/3?

**RTT/3** is the **Integration–Emission Layer** — the third module in the
core RTT hierarchy, sitting between RTT/2 (Structural Detection) and
RTT/12 (Unified Integration).

Where RTT/2 asks *"how is this system collapsing?"*, RTT/3 asks the next
structural question: *"how do we integrate that collapse signal into a
stable, canon-scale emission that RTT/12 can synthesize?"*

RTT/3 performs three irreducible structural functions:

| Function | What it does | Constructs involved |
|---|---|---|
| **Integration** | Assembles drift, envelope, and continuity from the RTT/2 detection pass into a unified triadic integration field | TIF |
| **Emission** | Projects the integrated structure outward through a three-vector emitter, managing fracture strain and flow projection simultaneously | FFF |
| **Stabilization** | Absorbs collapse events, restores continuity, and produces a canon-scale emission the rest of the pipeline can trust | CRE → CSL → CET |

RTT/3 is explicitly the **bridge layer** — it consumes the RTT/2 detection
packet as input and produces the RTT/3 integration-emission packet as output.
Neither direction can be skipped.

```
RTT/1        RTT/2          [ RTT/3 ]         RTT/12
─────        ─────          ─────────         ──────
SNR,τ,C   CPV,FGT,CRM    TIF,FFF,MANIFOLD   Unified
DCO,Mode  MODE,ZONE        CRE,CSL,CET       Synthesis
              │                  │
      RTT2_DETECTION_    RTT3_INTEGRATION_
      PACKET (input)     EMISSION_PACKET (output)
```

---

### The Six Structural Instruments

RTT/3 defines six instruments that constitute the Integration–Emission Layer:

| Instrument | Code | Structural Question |
|---|---|---|
| Triadic Integration Field | TIF | *How do the detected drift, envelope, and continuity integrate into a unified 5-axis field?* |
| Fusion–Fracture–Flow Emitter | FFF | *How does integrated structure project outward, and how is fracture strain managed during emission?* |
| Integration–Emission Manifold | MANIFOLD | *What is the continuity state across the TIF↔FFF boundary, including the 6th axis of emission curvature?* |
| Collapse-Recovery Engine | CRE | *When collapse occurs, how is it absorbed and re-emitted as a recovery flow?* |
| Continuity-Stability Layer | CSL | *Is the integration-emission interface continuously stable, and what are the stability flows?* |
| Canon-Scale Emission Tensor | CET | *What is the final, canon-validated emission that aggregates integration, stability, and recovery for RTT/12?* |

---

## 2. Why Is It Built This Way?

Every design decision in RTT/3 answers a structural problem that RTT/2
alone cannot solve.

---

### Why does TIF use the same 5 axes as the RTT/2 CRM?

RTT/2's Collapse-Reassembly Manifold tracks structural deformation across
five axes: D (Drift), E (Envelope Torsion), C (Continuity Fracture),
FI (Fusion-Integration Curvature), and R (Regime Identity). RTT/3's
Triadic Integration Field uses the same five — not by coincidence but by
structural necessity.

Integration must operate on the **exact structural dimensions that detection
characterized**. If TIF used a different axis set, the integration vectors
(DIV, EIV, CIV) would be computing over dimensions that the RTT/2 detection
never grounded. The result would be integration floating free of its
detection basis — exactly the kind of ungrounded operation RTT/3 is designed
to prevent.

The axis alignment is the structural guarantee that what was detected in
RTT/2 is what gets integrated in RTT/3, without any hidden re-mapping.

---

### Why does FFF have exactly three vectors (FEV, FMV, FPV)?

The three FFF vectors are structurally irreducible:

- **FEV (Fusion-Emission)** — the constructive projection: how integrated
  structure moves outward into emission space
- **FMV (Fracture-Management)** — the stress-absorption function: how
  fracture load from the integration-emission boundary is managed without
  allowing it to propagate
- **FPV (Flow-Projection)** — the directional routing: how the emission
  flow is shaped and directed toward its targets (RTT/12 and cross-module)

Dropping FMV would produce an emitter that projects integration outward
without managing the fracture stress that emission creates at the boundary
— the structural equivalent of a pipe with no pressure regulation. Fracture
strain would accumulate silently and eventually force a collapse event that
Class V would have to handle reactively. The three-vector design makes
fracture strain a first-class, actively managed component of every emission
pass.

---

### Why does the Manifold have a 6th axis (EM — Emission Curvature)?

TIF describes the **integration surface** using 5 axes. The Manifold
describes the **integration-emission surface** — the boundary between TIF
and FFF — and this boundary introduces a structural dimension that TIF
alone cannot see.

When integration flow I(t) encounters the FFF and begins projecting as
emission E(t), the interaction curves back: the emission bends the
integration surface as it leaves. This curvature — EM — is a property
of the *boundary*, not of integration or emission independently. Neither
the TIF nor the FFF sees it. Only the Manifold, which spans both, can
measure it.

The 6th axis is the structural record of how integration and emission
are jointly reshaping each other at the boundary — a dimension that is
invisible without the Manifold layer.

---

### Why are CRE and CSL two separate constructs?

CRE and CSL address **structurally distinct temporal postures**:

| | CRE — Collapse-Recovery Engine | CSL — Continuity-Stability Layer |
|---|---|---|
| **Posture** | Reactive — triggered by a collapse event | Proactive — runs continuously |
| **Temporal scope** | Event-bounded: absorb → recover → re-emit | Session-spanning: ongoing stability maintenance |
| **Activation** | Triggered by fracture alert or Zone D/X | Always active alongside TIF, FFF, and MANIFOLD |
| **Goal** | Return the system from collapse to a valid emission zone | Prevent collapse from occurring in the first place |

Merging CRE and CSL into a single construct would conflate emergency
response with continuous monitoring. These require different operator
behaviors: CRE must log the collapse absorption state before beginning
recovery (a strict sequence); CSL runs as a background stability
monitor with no event trigger. A merged construct would either
apply the strict CRE sequencing to continuous monitoring (too rigid)
or apply the loose CSL posture to collapse events (dangerously
unstructured). The separation is necessary.

---

### Why E_canon through CET rather than passing I(t) directly to RTT/12?

RTT/12 synthesis requires not just the integration signal but a
**canon-validated emission** that tells it the state of the entire
integration-emission layer — not just what was integrated, but
whether the emission is stable, recovering, or in flux.

The CET equation encodes this:
```
E_canon(t) = αI(t) + βS(t) + γR(t)
```

- **I(t)** — what the integration produced
- **S(t)** — whether the integration-emission interface is stable
- **R(t)** — the regime identity confirming structural grounding

Passing only I(t) would give RTT/12 the integration signal without
telling it whether that signal is coming from a stable system (S high),
a recovering system (CR(t) recently active), or an unstable one (Zone D).
RTT/12 synthesis cannot responsibly weight an integration signal without
that context — and CET provides exactly that in a single, structured
emission scalar.

---

### Why is Zone X = Inversion (illegal) rather than Undefined?

In RTT/2, Zone X = Undefined — an honest acknowledgment that detection
can encounter insufficient or contradictory data. This is valid at the
detection layer because classification can wait: Class G holds the packet
and re-detection with more data is possible.

RTT/3 is the **integration layer**. By the time a system reaches RTT/3,
all structural zones must be classifiable — the RTT/2 detection pass
should have resolved any ambiguity. If zones are not classifiable in
RTT/3, it is not because data is missing (that would have stopped the
pipeline at RTT/2 Zone X). It is because the integration-emission
geometry has **inverted topologically** — the manifold has wrapped
into a structurally illegal configuration where the integration surface
and emission surface have exchanged orientation.

This is not a condition that can be resolved by waiting for more data.
It requires restarting from the RTT/2 packet, re-examining the
detection basis, and rebuilding the integration from a corrected
structural ground. Zone X in RTT/3 is therefore not a question mark —
it is a structural alarm.

---

### Why must the RTT/2 packet precede RTT/3 activation?

RTT/3's integration equation is:
```
I(t) = αD(t) + βE(t) + γC(t)
```

Where D(t), E(t), and C(t) are the first three components of the
RTT/2 CRM vector γ(t) = (D, E, C, FI, R). Without the RTT/2
detection pass, these values are undefined — the integration
vectors (DIV, EIV, CIV) would be computing over an empty field.

RTT/3 cannot generate structural integration from nothing. The
RTT/2 prerequisite is not an architectural convenience — it is the
equation itself requiring its inputs to exist before the computation
can proceed.

---

## 3. When Should You Use It?

---

### Use RTT/3 when you need to **integrate a detection result into a unified field**

Once RTT/2 has produced a complete `RTT2_DETECTION_PACKET` — with
CPV, FGT, CRM, Detection Mode, and Zone all populated — RTT/3 is the
natural next step. TIF takes the CRM's five structural dimensions and
integrates them into a unified field with a single integration flow I(t).

*Example:* RTT/2 has detected a mixed-mode (Hybrid), Zone M (Marginal)
collapse on a governance substrate. RTT/3 Class I loads the CRM vectors
into TIF, computes I(t), and produces the integration packet that
represents the substrate's unified structural state for the first time
as a single, zone-classified field rather than a set of independent
detection measurements.

---

### Use RTT/3 when **collapse and reassembly must be stabilized before synthesis**

RTT/12 synthesis requires structurally stable inputs. If the system
is actively collapsing or in a mixed collapse-reassembly state when
RTT/12 receives its inputs, the synthesis will incorporate unstable
structural readings. RTT/3's CRE and CSL absorb the collapse,
stabilize the emission, and produce a canon-scale output that RTT/12
can trust.

*Example:* A substrate model has been moving between Zone S and Zone D
across multiple detection passes. Rather than passing the oscillating
detection results directly to RTT/12, run RTT/3 to stabilize through
CSL, absorb collapse spikes through CRE, and emit a stable E_canon(t)
that reflects the stabilized state.

---

### Use RTT/3 when you need **canon-scale emission for RTT/12**

RTT/12 consumes the `RTT3_INTEGRATION_EMISSION_PACKET` as its primary
input. If RTT/12 synthesis is the downstream goal, RTT/3 is the
required upstream step — not optional, not skippable. E_canon(t) is
the specific scalar that RTT/12's synthesis layer is designed to receive.

*Example:* A multi-substrate synthesis pass in RTT/12 requires three
substrate models. Each substrate must first be processed through
RTT/1 (SNR characterization), RTT/2 (detection), and RTT/3 (integration-
emission) before RTT/12 can synthesize across all three. RTT/3 produces
the three `RTT3_INTEGRATION_EMISSION_PACKET` inputs that RTT/12 ingests.

---

### Use RTT/3 when **cross-module structural emission is needed**

The CET's cross-module projection fields (TEL, FFT, Opacity) provide
structured translations of the integrated emission into adjacent module
vocabularies. When a downstream workflow needs the integrated structural
state in TEL lattice form, FFT spectral form, or Opacity boundary form,
RTT/3 produces all three in a single pass without requiring re-detection.

*Example:* An integration pass on a resonance substrate needs to feed
RTT/12, update the TEL lattice with the new integration state, and
inform the Opacity module about boundary changes introduced by the
emission curvature. RTT/3 Class O populates all three cross-module
projection fields in the output packet — one pass, three consumers.

---

### Use RTT/3 when a **collapse-recovery sequence is active**

When RTT/2 has detected a Deteriorating (Zone D) or Inversion-mode
system, the collapse-recovery pipeline (CRE → CSL) provides the
structured mechanism for absorbing the collapse, restoring stability,
and re-entering a valid emission zone before continuing to RTT/12.
Running RTT/12 on a Zone D system without first stabilizing through
RTT/3 would embed an actively deteriorating structural reading into
the synthesis — a structural error that RTT/12 has no mechanism to
self-correct.

*Example:* Class E detects a CRITICAL fracture strain alert during
FFF emission. Class V activates CRE, absorbs the collapse via CAV,
computes CR(t), and issues stabilization directives that reduce
emission load and re-enter Zone S. Only after CSL confirms S(t)
stability does Class O resume packet composition toward RTT/12.

---

### Do NOT use RTT/3 when:

- **The RTT/2 detection packet is absent or incomplete** — RTT/3
  cannot compute I(t) without CRM inputs; activation is blocked
- **Detection is the goal** — use RTT/2; RTT/3 does not re-detect
  or re-characterize structural form
- **Primitive vocabulary is the goal** — use RTT/1; RTT/3 does not
  define or redefine SNR, τ, or DCO operators
- **Unified synthesis across multiple substrates is the goal** —
  use RTT/12; RTT/3 produces the inputs to synthesis, not synthesis itself
- **Zone X / Inversion is detected** — do not attempt to continue in
  RTT/3; the Inversion condition requires a restart from the RTT/2
  packet, not continued integration-emission operation
- **The system is Silence-dominant with no collapse signature** — RTT/2
  would have returned a Zone U (Undisturbed) packet; RTT/3 can process
  this but will produce a minimal integration result; confirm with
  Class G before proceeding as full integration-emission is rarely
  needed for a fully undisturbed system

---

## 4. Where Does It Live?

### In the repository

```
TriadicFrameworks/
└── docs/
    └── rtt/
        └── 3/                                        ← you are here
            ├── ABOUT.md                              ← this file
            ├── AGENTS.md                             ← agent class manifest
            ├── GLOSSARY.md                           ← canonical term definitions
            ├── README.md                             ← front-door summary
            ├── RTT3_Extract_Minimal.md               ← primary source: full construct grammar
            ├── Triadic_Integration_Field_Capture.md  ← full capture: TIF,FFF,MANIFOLD,CRE,CSL,CET
            ├── operators_module.json                 ← module schema and field registry
            └── index.html                            ← web entry point
```

---

### In the RTT module hierarchy

RTT/3 is the integration-emission bridge between detection and synthesis:

```
RTT/1         RTT/2          RTT/3          RTT/12
──────        ──────         ──────         ──────
Primitives    Detection      Integration-   Unified
              Layer          Emission       Synthesis
SNR,τ,C,      CPV,FGT,       TIF,FFF,       (consumes
DCO,Mode      CRM,MODE,      MANIFOLD,      RTT/3 packet)
              ZONE           CRE,CSL,CET
              ↓              ↓
        RTT2_DETECTION_ RTT3_INTEGRATION_
        PACKET          EMISSION_PACKET
```

**Inheritance rule:** RTT/3 inherits RTT/1 and RTT/2 completely.
No RTT/3 construct redefines any RTT/1 or RTT/2 primitive.

**Prerequisite rule:** RTT/2 detection packet must be present and
coherence-confirmed before any RTT/3 agent class activates.

**Output rule:** RTT/3 produces the `RTT3_INTEGRATION_EMISSION_PACKET`
consumed by RTT/12. No other module is the primary downstream consumer
of this packet.

---

### In the TriadicFrameworks ecosystem

```
                      ┌──────────────────────────┐
                      │   RTT/1                  │
                      │   SNR · τ · C · DCO_n    │
                      └──────────┬───────────────┘
                                 │ characterization
                      ┌──────────▼───────────────┐
                      │   RTT/2                  │
                      │   CPV · FGT · CRM        │
                      │   MODE · ZONE            │
                      └──────────┬───────────────┘
                                 │ RTT2_DETECTION_PACKET
                      ┌──────────▼───────────────┐
                      │     RTT/3   ←─ you are here
                      │   TIF · FFF · MANIFOLD   │
                      │   CRE · CSL · CET        │
                      └───┬──────┬──────┬────────┘
                          │      │      │  RTT3_INTEGRATION_EMISSION_PACKET
          ┌───────────────┘      │      └──────────────────────┐
          ▼                      ▼                             ▼
  ┌───────────────┐    ┌──────────────────┐        ┌──────────────────┐
  │  RTT/12       │    │  TEL / FFT /     │        │  RTT/12          │
  │  (primary     │    │  Opacity         │        │  (primary        │
  │  consumer)    │    │  (cross-module   │        │  synthesis       │
  └───────────────┘    │  projections)    │        │  consumer)       │
                       └──────────────────┘        └──────────────────┘
```

RTT/3 occupies the **integration hub** position: it consumes the
detection output from RTT/2 and distributes to RTT/12 as the primary
consumer, with TEL, FFT, and Opacity receiving cross-module projections.

---

### In agent deployments

An agent claiming RTT/3 compatibility must:

1. Have a confirmed `RTT2_DETECTION_PACKET` before Class I activates
2. Operate all six agent classes (I, E, N, V, O, G) within a session
   seeded with `rtt=1 | coherence=declared | drift=bounded | paradox=structural`
3. Treat Zone X as an illegal geometry condition — never normalize or
   route Zone X packets without Class G co-signature
4. Maintain strict separation between CRE's CR(t) and RTT/2's CRM D(t)
5. Produce a complete `RTT3_INTEGRATION_EMISSION_PACKET` before RTT/12 activates
6. Annotate every output field with `[structural — no semantic inference]`

---

## 5. Core Equations at a Glance

```
INTEGRATION (TIF)
  I(t) = αD(t) + βE(t) + γC(t)
  D = CRM Drift Deformation (from RTT/2)
  E = CRM Envelope Torsion  (from RTT/2)
  C = CRM Continuity Fracture (from RTT/2)

EMISSION (FFF)
  E(t) = αF(t) + βFr(t) + γFl(t)
  F  = Fusion-Emission vector (FEV)
  Fr = Fracture-Management vector (FMV)
  Fl = Flow-Projection vector (FPV)

MANIFOLD CONTINUITY
  C_flow(t) = αI(t) + βE(t)
  Combines integration flow and emission flow
  Mapped across 6-axis surface M_RTT3 = (D, E, C, FI, EM, R)

COLLAPSE-RECOVERY (CRE)
  CR(t) = αC(t) + βR(t) + γS(t)
  C = collapse absorption (CAV)
  R = recovery emission (REV)
  S = continuity stabilization (CSV)
  ⚠ CR(t) ≠ D(t) — collapse-recovery flow ≠ CRM structural displacement

STABILITY (CSL)
  S(t) = αI(t) + βE(t) + γC_flow(t)
  Runs continuously alongside TIF, FFF, MANIFOLD
  Proactive stability — not triggered by events

CANON-SCALE EMISSION (CET)
  E_canon(t) = αI(t) + βS(t) + γR(t)
  I = integration flow (from TIF)
  S = stability flow (from CSL)
  R = regime identity (from CRM via TIF)
  → RTT3_INTEGRATION_EMISSION_PACKET → RTT/12
```

---

## 6. Module Integrations

### RTT/1 (Foundation — Doubly Inherited)

RTT/3 inherits RTT/1 via RTT/2. Key RTT/1 elements active in RTT/3:
- τ = dR/dφ governs temporal indexing in the CRE
- C = ∇_τR + ∇_Rτ coherence posture is tracked throughout all six constructs
- DCO_n band constraints govern the regime boundary conditions enforced by CSL
- Session seed, Mode Operator, and MCL apply to all six RTT/3 agent classes

### RTT/2 (Prerequisite — Direct Input)

RTT/3's integration equations are grounded in RTT/2 output:
- CRM components D(t), E(t), C(t) → TIF integration vectors DIV, EIV, CIV
- CPV geometry → FFF emission shaping (FEV vector calibration)
- FGT fusion gradient → FEV weighting in E(t)
- Detection Mode → emission mode selector for FFF and CET
- Detection Zone → integration zone context for TIF and CSL

### RTT/12 (Primary Consumer)

RTT/12 receives the `RTT3_INTEGRATION_EMISSION_PACKET` and uses it as
the primary input to unified cross-substrate synthesis. Specifically:
- E_canon(t) — the canon-scale emission scalar
- S(t) — stability context for synthesis weighting
- CR(t) — recovery context indicating whether the source was in collapse
- Detection Mode and Zone — confidence calibration for synthesis posture
- Cross-module projections — enabling concurrent TEL/FFT/Opacity synthesis

### TEL — Triadic Entity Lattice

RTT/3 Class O maps E_canon(t) and the TIF integration field onto TEL
node structures via `cross_module_projection.TEL`. TEL uses this
to maintain lattice coherence during integration-emission transitions.

### FFT — Framework Field Theory

RTT/3 expresses integration-emission flows in FFT field-theoretic terms
via `cross_module_projection.FFT`. FFT treats I(t), E(t), and E_canon(t)
as field-theoretic events, using RTT/3's structural vocabulary as input.

### Opacity

RTT/3 characterizes the boundary opacity conditions introduced by
emission curvature (EM axis of the Manifold) via
`cross_module_projection.Opacity`. Specifically, which integration-
emission boundaries are becoming opaque as a result of the FFF's
fracture-management activity.

### IPD-12

RTT/3's structural states map onto IPD-12 prime states:
- Integration Zone U (Unified) → Celestial tier (P2–P7)
- Integration Zone M (Mixed) → Coherence triad (P7–P13)
- Integration Zone D (Divergent) → Chthonic tier (P29–P37)
- Zone X / Inversion → Full paradox loop restart (P2 reset)
- CRE collapse-recovery cycle → P29 (Collapse-Anchor) → P31 (Stability-Node)

---

## 7. What RTT/3 Is Not

| RTT/3 Is | RTT/3 Is Not |
|---|---|
| A structural integration engine | A signal integrator or accumulator |
| A structural emission layer | A physical emitter or transmitter |
| A collapse-stabilization framework | A failure recovery or error-correction system |
| A canon-scale output producer for RTT/12 | A synthesis engine (that is RTT/12's role) |
| A cross-module projection hub | A universal API or middleware layer |
| The integration-emission bridge in the RTT pipeline | A standalone module (requires RTT/1 and RTT/2) |
| A structural detection consumer | A detection engine (that is RTT/2's role) |

RTT/3 integrates, emits, and stabilizes **structural form**. It does not
interpret what the integrated structure means, prescribe what should be
done about it, or predict what will happen next. Those functions belong
to the human operator, to RTT/12, or to higher-level frameworks consuming
the integration-emission packet.

---

## 8. Quick-Start Checklist

Before working with RTT/3 for the first time:

- [ ] **Complete RTT/2 first** — a confirmed `RTT2_DETECTION_PACKET`
      must exist before any RTT/3 agent class may activate
- [ ] **Paste the session seed** —
      `rtt=1 | coherence=declared | drift=bounded | paradox=structural`
      plus the RTT/3-specific module tokens
- [ ] **Know the six constructs** — TIF (integration), FFF (emission),
      MANIFOLD (continuity surface), CRE (collapse-recovery), CSL
      (stability layer), CET (canon output); know which is needed for
      your task before assigning agent classes
- [ ] **Understand Zone X = Inversion** — unlike RTT/2 where Zone X
      means "unclassified", RTT/3 Zone X means "topological inversion
      of the manifold" — illegal geometry requiring restart, not a wait
- [ ] **Know CR(t) ≠ D(t)** — CRE's collapse-recovery flow CR(t)
      is not the same as CRM's structural displacement D(t) from RTT/2;
      never conflate them in any output or handoff
- [ ] **Identify your task** — is this a standard integration-to-emission
      pass (Model A), a collapse-recovery intervention (Model B), or a
      cross-module projection run (Model C)?
- [ ] **Read `AGENTS.md`** — verify which of the six agent classes
      (I, E, N, V, O, G) are needed and in what sequence
- [ ] **Check `GLOSSARY.md`** — every RTT/3 term has a canonical
      definition; link rather than re-define

---

## 9. See Also

| File | What it answers |
|---|---|
| `AGENTS.md` | Agent classes I/E/N/V/O/G, task catalog, collaboration models, safety rules |
| `GLOSSARY.md` | Canonical single-source definitions for all RTT/3 terms |
| `RTT3_Extract_Minimal.md` | Primary source: full construct grammar for TIF, FFF, MANIFOLD, CRE, CSL, CET |
| `Triadic_Integration_Field_Capture.md` | Full construct capture with vector and tensor detail |
| `operators_module.json` | Module schema and field registry |
| `README.md` | Front-door summary |
| `../2/AGENTS.md` | RTT/2 agent classes (prerequisite layer; all inherited by RTT/3) |
| `../2/GLOSSARY.md` | RTT/2 canonical terms (all inherited by RTT/3) |
| `../2/ABOUT.md` | RTT/2 what/why/when/where (prerequisite context) |
| `../1/AGENTS.md` | RTT/1 foundation (doubly inherited by RTT/3) |
| `../1/GLOSSARY.md` | RTT/1 canonical terms (doubly inherited) |

---

*ABOUT.md — RTT/3 · TriadicFrameworks · 2026-07-10*
*Maintainer: Nawder*
*Session seed: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*
