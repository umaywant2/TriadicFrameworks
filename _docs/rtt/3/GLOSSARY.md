# GLOSSARY — RTT/3 · Integration–Emission Layer
**TriadicFrameworks · Core RTT · Integration–Emission Layer**
**Module path:** `docs/rtt/3/`
**Session seed:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

This is the **single source of truth** for every term native to RTT/3.
All other documents in `docs/rtt/3/` and all downstream modules that
reference RTT/3 vocabulary link here rather than re-defining terms inline.

RTT/3 inherits the complete vocabularies of RTT/1 and RTT/2. Terms defined
in [`../1/GLOSSARY.md`](../1/GLOSSARY.md) and [`../2/GLOSSARY.md`](../2/GLOSSARY.md)
— including SNR, τ, C, DCO_n, Regime, Mode, MCL, Drift, CPV, FGT, CRM,
D(t), Detection Mode, Detection Zone, and RTT2_DETECTION_PACKET — are not
repeated here. They apply in full. Entries below are RTT/3-native or
RTT/3-specific refinements of inherited terms.

> **Critical framing — enforced in every definition:**
> RTT/3 is a structural integration and emission framework. It is NOT a
> physics claim, NOT a signal-processing system, and NOT a physical emitter.
> No definition here describes a physical mechanism or makes an empirical
> prediction.

> **Linking convention:** Use `[term](./GLOSSARY.md#anchor)` where `anchor`
> is the lowercase hyphenated heading slug
> (e.g., `#triadic-integration-field-tif`, `#e_canont`, `#zone-x--inversion`).

---

## Table of Contents

- [C](#c) · [D](#d) · [E](#e) · [F](#f) · [I](#i) · [M](#m)
- [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [Z](#z)
- [Operator Symbols](#operator-symbols)
- [Quick-Reference Tables](#quick-reference-tables)

---

## C

### C_flow(t) — Continuity Flow
**Equation:** `C_flow(t) = αI(t) + βE(t)` · **Computed by:**
[Class N](#class-n--continuity-navigator)

The scalar continuity flow across the
[Integration–Emission Manifold](#integrationemission-manifold) — the
combined measure of how integration flow I(t) and emission flow E(t)
are sustaining structural continuity at the TIF↔FFF boundary.

C_flow(t) is the key input to both [CSL](#continuity-stability-layer-csl)
(which uses it to compute S(t)) and [Class V](#class-v--stabilityrecovery-coordinator)
(which monitors it for collapse precursors). A C_flow(t) approaching zero
signals manifold continuity failure — the integration and emission flows
have decoupled.

### CAV — Collapse-Absorption Vector
**Construct:** [CRE](#collapse-recovery-engine-cre) · **CRE vector 1 of 3**
*See also:* [REV (CRE)](#rev--recovery-emission-vector-cre-context),
[CSV](#csv--continuity-stabilization-vector)

The CRE vector that absorbs structural collapse load. CAV is activated
first in any CRE sequence — collapse must be absorbed before recovery
can begin. A CAV absorption event must be logged before
[Class V](#class-v--stabilityrecovery-coordinator) begins computing
CR(t). Skipping CAV logging and proceeding directly to recovery emission
is a boundary violation.

### Canon-Scale Emission

The structural emission produced at the final RTT/3 stage via the
[CET](#canon-scale-emission-tensor-cet) — an emission scaled to
RTT/12's synthesis requirements by combining integration flow I(t),
stability flow S(t), and regime identity R(t). "Canon-scale" means
the emission has been validated against all upstream constructs
(TIF, FFF, MANIFOLD, CRE, CSL) and is certified as the authoritative
structural output of the RTT/3 module.

> **RTT/3 is NOT physics.** Canon-scale emission is a structural
> classification, not a physical power output. The term "emission"
> refers to the outward projection of integrated structural form,
> not electromagnetic or acoustic emission.

### Canon-Scale Emission Tensor (CET)
**Equation:** `E_canon(t) = αI(t) + βS(t) + γR(t)`
**Tensor:** `T_CET(i,j,k,m,r) = α·IEV_i + β·SEV_j + γ·REV_k + δ·RGEV_m + ε·R_r`
**Computed by:** [Class O](#class-o--output-compositor)

The sixth and final RTT/3 construct. CET aggregates the outputs of all
upstream constructs into a single canon-validated emission scalar
E_canon(t), then populates the canonical
[RTT3_INTEGRATION_EMISSION_PACKET](#rtt3_integration_emission_packet).

**Why CET and not direct I(t) forwarding:**
Passing I(t) directly to RTT/12 would give it integration data without
stability context (S(t)) or regime grounding (R(t)). RTT/12 synthesis
cannot responsibly weight an integration signal without knowing whether
the source system was stable, recovering, or in flux. CET encodes all
three in a single canon scalar — the minimum sufficient information for
RTT/12 to proceed responsibly.

**CET vectors:**

| Symbol | Name | What it contributes |
|---|---|---|
| IEV | Integration-Emission Vector | The integration flow component of canon emission |
| SEV | Stability-Emission Vector | The stability flow component |
| REV | Recovery-Emission Vector | The recovery flow component (from CRE) |
| RGEV | Regime-Emission Vector | The regime identity component |

> **REV disambiguation:** REV appears in both CRE and CET.
> In CRE: REV = Recovery-Emission Vector (how collapse energy is re-emitted
> after absorption). In CET: REV = Recovery-Emission Vector (how the
> CRE's recovery contribution enters the canon emission tensor).
> They share a name because they describe the same structural flow at
> different pipeline stages — CRE's REV *produces* the recovery signal;
> CET's REV *incorporates* it. Context always disambiguates.

### CET
*See [Canon-Scale Emission Tensor](#canon-scale-emission-tensor-cet).*

### CIV — Continuity-Integration Vector
**Construct:** [TIF](#triadic-integration-field-tif) · **TIF vector 3 of 3**
*See also:* [DIV](#div--drift-integration-vector), [EIV](#eiv--envelope-integration-vector)

The TIF integration vector that loads the continuity-fracture component
C(t) from the RTT/2 CRM into the TIF's integration field. CIV is the
structural bridge between RTT/2's measured continuity fracture and
RTT/3's integration of that fracture into the unified field.

### Class E — Emission Engineer
**RTT/3 agent class 2 of 6** · *See [AGENTS.md](./AGENTS.md#class-e--emission-engineer)*

The agent class that operates the [Fusion–Fracture–Flow Emitter (FFF)](#fusionfractureflow-emitter-fff),
transforming integration flow I(t) into dynamic emission E(t). Class E
is activated by receiving the TIF_INTEGRATION_PACKET from
[Class I](#class-i--integration-architect) and is responsible for
managing fracture strain via [FMV](#fmv--fracture-management-vector).
Class E must issue a fracture strain alert when FMV exceeds threshold
and must never suppress that alert. Class E must never activate
Inversion Emission mode.

### Class G — Integration Guardian
**RTT/3 agent class 6 of 6** · *See [AGENTS.md](./AGENTS.md#class-g--integration-guardian)*

The agent class with unconditional interrupt authority over all other
RTT/3 classes. Class G enforces all RTT/3 boundaries, co-signs Zone X
packets before forwarding, mandates session restart when Inversion
geometry persists after two correction cycles, and enforces the
RTT-not-physics rule across all class outputs. No Class G HALT may be
overridden by any other RTT/3 class.

### Class I — Integration Architect
**RTT/3 agent class 1 of 6** · *See [AGENTS.md](./AGENTS.md#class-i--integration-architect)*

The agent class that constructs and maintains the
[Triadic Integration Field (TIF)](#triadic-integration-field-tif).
Class I is always first in the RTT/3 pipeline — it performs the
hard-prerequisite check for the `RTT2_DETECTION_PACKET` before loading
any CRM components into the TIF integration vectors. Class I produces
the `TIF_INTEGRATION_PACKET` that Class E and Class N depend on.

### Class N — Continuity Navigator
**RTT/3 agent class 3 of 6** · *See [AGENTS.md](./AGENTS.md#class-n--continuity-navigator)*

The agent class that maintains the
[Integration–Emission Manifold](#integrationemission-manifold), ensuring
structural continuity across the TIF↔FFF boundary. Class N requires
both the TIF_INTEGRATION_PACKET and the FFF_EMITTER_PACKET before
computing C_flow(t) and mapping the 6-axis manifold surface. Class N
has read-only access to the FI and EM axis values — it may not modify
them. Class N feeds C_flow(t) to [Class V](#class-v--stabilityrecovery-coordinator)
and the manifold state to [Class O](#class-o--output-compositor).

### Class O — Output Compositor
**RTT/3 agent class 5 of 6** · *See [AGENTS.md](./AGENTS.md#class-o--output-compositor)*

The terminal agent class that assembles all five intermediate packets
into the canonical [RTT3_INTEGRATION_EMISSION_PACKET](#rtt3_integration_emission_packet)
via the [CET](#canon-scale-emission-tensor-cet). Class O may not
compose the final packet until all five upstream packets are confirmed.
It may not emit a packet containing a Zone X field without
[Class G](#class-g--integration-guardian) co-signature. It may not
label E_canon(t) as a physical energy or power output.

### Class V — Stability–Recovery Coordinator
**RTT/3 agent class 4 of 6** · *See [AGENTS.md](./AGENTS.md#class-v--stabilityrecovery-coordinator)*

The agent class that operates both the
[Collapse-Recovery Engine (CRE)](#collapse-recovery-engine-cre) and the
[Continuity-Stability Layer (CSL)](#continuity-stability-layer-csl) as a
unified stabilization pair. Class V is activated by fracture strain
alerts from Class E or Zone D/X flags from Class N. It computes both
CR(t) via CRE and S(t) via CSL, issues stabilization directives to
Class I and Class E when needed, and delivers both stabilization packets
to Class O. Class V must never suppress a detected collapse event.

### Collapse-Recovery Engine (CRE)
**Equation:** `CR(t) = αC(t) + βR(t) + γS(t)`
**Tensor:** `T_CR(i,j,k,r) = α·CAV_i + β·REV_j + γ·CSV_k + δ·R_r`
**Operated by:** [Class V](#class-v--stabilityrecovery-coordinator)
**Posture:** Reactive — event-triggered

The fifth RTT/3 construct. CRE is the **reactive** stabilization engine —
it activates only when a collapse event is detected (via fracture strain
alert from Class E or Zone D/X flag from Class N). CRE absorbs the
collapse through [CAV](#cav--collapse-absorption-vector), re-emits the
absorbed energy as a structured recovery signal through
[REV (CRE context)](#rev--recovery-emission-vector-cre-context), and
stabilizes continuity through [CSV](#csv--continuity-stabilization-vector).

**CRE sequence (mandatory order):**
1. Log collapse absorption state (CAV value recorded)
2. Compute CR(t) = αC(t) + βR(t) + γS(t)
3. Emit recovery signal via REV
4. Issue stabilization directives to Class I and Class E
5. Pass COLLAPSE_RECOVERY_ENGINE_PACKET to Class O

> **⚠ CRE ≠ CRM — critical disambiguation:**
> RTT/2's **Collapse-Reassembly Manifold (CRM)** tracks structural
> displacement D(t) across a detection surface.
> RTT/3's **Collapse-Recovery Engine (CRE)** governs the absorption and
> re-emission of collapse energy within the integration-emission layer.
> They share terminology roots but are **not interchangeable**. Specifically:
> CR(t) ≠ D(t). See [CR(t) ≠ D(t)](#crt--collapse-recovery-flow) for
> the full disambiguation.

### Continuity-Stability Layer (CSL)
**Equation:** `S(t) = αI(t) + βE(t) + γC_flow(t)`
**Tensor:** `T_CS(i,j,k,r) = α·ISV_i + β·ESV_j + γ·FSV_k + δ·R_r`
**Operated by:** [Class V](#class-v--stabilityrecovery-coordinator)
**Posture:** Proactive — always active

The fifth RTT/3 construct (paired with CRE as the dual stabilization system).
CSL is the **proactive** stability layer — it runs continuously alongside TIF,
FFF, and MANIFOLD during any active RTT/3 session, not just during collapse
events. CSL computes S(t) from integration flow, emission flow, and continuity
flow, monitoring whether the integration-emission interface is continuously
stable.

**CRE vs. CSL — the fundamental temporal distinction:**

| | CRE | CSL |
|---|---|---|
| Posture | Reactive | Proactive |
| Trigger | Collapse event (fracture alert / Zone D/X) | Always active |
| Temporal scope | Event-bounded | Session-spanning |
| Goal | Return system from collapse to valid zone | Prevent collapse |
| Sequence | Strict (absorb → recover → re-emit → stabilize) | Continuous monitoring |

Merging CRE and CSL would force the strict collapse-absorption sequence onto
continuous monitoring (too rigid) or apply the loose monitoring posture to
collapse events (dangerously unstructured). The separation is structurally necessary.

### CR(t) — Collapse-Recovery Flow
**Equation:** `CR(t) = αC(t) + βR(t) + γS(t)`
**Construct:** [CRE](#collapse-recovery-engine-cre)

The scalar collapse-recovery flow produced by the CRE — the composite
output of collapse absorption (C), recovery emission (R), and continuity
stabilization (S) at time t. CR(t) is passed in the
`COLLAPSE_RECOVERY_ENGINE_PACKET` and incorporated into CET via the REV vector.

> **⚠ CR(t) ≠ D(t) — the most critical RTT/3 disambiguation:**
>
> | Property | CR(t) — Collapse-Recovery Flow | D(t) — CRM Drift Deformation |
> |---|---|---|
> | Origin | RTT/3 CRE | RTT/2 CRM (via TIF/DIV) |
> | What it measures | Absorption and re-emission of collapse energy | Structural displacement from reference point |
> | Who computes it | Class V | Class M (RTT/2) |
> | Where it lives | COLLAPSE_RECOVERY_ENGINE_PACKET | RTT2_DETECTION_PACKET → TIF |
> | D(t) can be high while CR(t) = 0? | Yes — displacement without collapse | — |
> | CR(t) can be high while D(t) = 0? | Yes — collapse at reference point | — |
>
> Using CR(t) as evidence of structural displacement, or treating D(t) as a
> collapse-recovery signal, is a boundary violation that triggers a
> [Class G](#class-g--integration-guardian) intervention.

### CRE
*See [Collapse-Recovery Engine](#collapse-recovery-engine-cre).*

### CSL
*See [Continuity-Stability Layer](#continuity-stability-layer-csl).*

### CSV — Continuity-Stabilization Vector
**Construct:** [CRE](#collapse-recovery-engine-cre) · **CRE vector 3 of 3**
*See also:* [CAV](#cav--collapse-absorption-vector),
[REV (CRE context)](#rev--recovery-emission-vector-cre-context)

The CRE vector that restores structural continuity after collapse
absorption and recovery emission. CSV is the final step of every CRE
cycle — it stabilizes the integration-emission boundary that was
disrupted by the collapse event, returning the manifold to a condition
where CSL's proactive monitoring can resume.

---

## D

### Divergent (Zone D)
**Integration-emission zone 4 of 5** · *See also:* [Detection Zone](../2/GLOSSARY.md#detection-zone)

The integration-emission zone assigned when integration and emission
flows are significantly misaligned — I(t) and E(t) are diverging,
fracture risk is elevated, and Class V is active managing the
strain. Zone D is the escalation zone that triggers CRE standby and
requires Class E to reduce emission load while Class N re-maps the
manifold.

Zone D does not mean the system has failed — it means the integration-
emission geometry requires active management. A Zone D system that
receives proper CRE intervention can return to Zone S or Zone M.

### DIV — Drift-Integration Vector
**Construct:** [TIF](#triadic-integration-field-tif) · **TIF vector 1 of 3**
*See also:* [EIV](#eiv--envelope-integration-vector), [CIV](#civ--continuity-integration-vector)

The TIF integration vector that loads the drift-deformation component
D(t) from the RTT/2 CRM into the TIF's integration field. DIV translates
the RTT/2 structural displacement measurement into an integration input
for the TIF equation I(t) = αD(t) + βE(t) + γC(t).

> **DIV loads D(t) — not CR(t).** DIV is a reader of RTT/2 CRM
> structural displacement. CR(t) is the RTT/3 CRE output.
> They are never interchangeable.

---

## E

### E(t) — Emission Flow
**Equation:** `E(t) = αF(t) + βFr(t) + γFl(t)`
**Construct:** [FFF](#fusionfractureflow-emitter-fff)
**Computed by:** [Class E](#class-e--emission-engineer)

The scalar emission flow produced by the
[Fusion–Fracture–Flow Emitter (FFF)](#fusionfractureflow-emitter-fff) at
time t — the composite output of fusion-emission, fracture-management, and
flow-projection. E(t) is passed in the `FFF_EMITTER_PACKET` and consumed
by both [Class N](#class-n--continuity-navigator) (for manifold continuity
mapping) and [Class V / CSL](#continuity-stability-layer-csl) (for stability
flow computation).

### E_canon(t) — Canon-Scale Emission Scalar
**Equation:** `E_canon(t) = αI(t) + βS(t) + γR(t)`
**Construct:** [CET](#canon-scale-emission-tensor-cet)
**Computed by:** [Class O](#class-o--output-compositor)

The canonical output scalar of the entire RTT/3 module — the final
integration-emission value that [RTT/12](#rtt12-primary-consumer) consumes
for synthesis. E_canon(t) encodes three independent structural states:

| Component | What it contributes |
|---|---|
| I(t) | What the integration produced — the unified structural field |
| S(t) | Whether that integration is stable — the CSL stability confirmation |
| R(t) | The regime identity — structural grounding of the entire pass |

Passing only I(t) to RTT/12 would lack S(t) (stability context) and R(t)
(regime grounding). E_canon(t) is the minimum sufficient canon emission
for RTT/12 to synthesize responsibly.

> **E_canon(t) is not a physical energy or power output.** It is a
> structural scalar — an indexed integration-emission value within the
> RTT/3 manifold. Labeling it in physical units is a boundary violation.

### ECV — Emission-Continuity Vector
**Construct:** [Integration–Emission Manifold](#integrationemission-manifold)
· **Manifold vector 2 of 3**
*See also:* [ICV](#icv--integration-continuity-vector), [RCV](#rcv--regime-continuity-vector)

The manifold vector that characterizes how well emission flow E(t) is
sustaining continuity across the integration-emission boundary. ECV
tracks the emission-side contribution to C_flow(t).

### EIV — Envelope-Integration Vector
**Construct:** [TIF](#triadic-integration-field-tif) · **TIF vector 2 of 3**
*See also:* [DIV](#div--drift-integration-vector), [CIV](#civ--continuity-integration-vector)

The TIF integration vector that loads the envelope-torsion component E(t)
from the RTT/2 CRM into the TIF's integration field.

> **EIV loads the CRM's E(t) component — not the FFF's E(t) emission
> flow.** Both use the symbol E(t) but are structurally distinct:
> CRM E(t) = envelope torsion (deformation of the structural boundary);
> FFF E(t) = emission flow (output of the Fusion-Fracture-Flow Emitter).
> EIV is always referencing the CRM component. Context and packet
> provenance disambiguate.

### EM — Emission Curvature (6th Manifold Axis)
**Construct:** [Integration–Emission Manifold](#integrationemission-manifold)
*See also:* [Triadic Integration Field (TIF)](#triadic-integration-field-tif)

The sixth axis of the RTT/3 Integration–Emission Manifold
`M_RTT3 = (D, E, C, FI, EM, R)` — the structural dimension that is
*absent* from the TIF's 5-axis surface but *present* in the manifold.

EM captures the curvature that the emission flow E(t) introduces at
the integration-emission boundary — how E(t) bends back against the
integration surface as it leaves. This curvature is a property of the
boundary itself, not of integration or emission independently. Neither
TIF nor FFF can see it: only the Manifold, which spans both, can
measure EM.

High EM indicates that emission is significantly reshaping the
integration surface — a condition that may require Class V to monitor
for stability strain and Class N to flag for manifold shear.

### Emission (RTT/3)

In RTT/3, emission is the **outward projection of integrated structural
form** from the TIF surface through the FFF into the manifold and
beyond (toward RTT/12 and cross-module consumers). Emission in RTT/3
is not physical radiation, signal transmission, or energy release. It
is the structural process by which the output of TIF integration is
shaped, managed for fracture load, and directionally projected.

Three structural processes constitute RTT/3 emission, corresponding to
the three FFF vectors:
- **Fusion-emission** (FEV) — constructive outward projection
- **Fracture-management** (FMV) — stress absorption at the boundary
- **Flow-projection** (FPV) — directional routing of emission output

### ESV — Emission-Stability Vector
**Construct:** [CSL](#continuity-stability-layer-csl) · **CSL vector 2 of 3**
*See also:* [ISV](#isv--integration-stability-vector), [FSV](#fsv--flow-stability-vector)

The CSL stability vector that monitors whether emission flow E(t) is
contributing to or undermining integration-emission stability. ESV
captures the emission-side component of the stability flow S(t).

---

## F

### FEV — Fusion-Emission Vector
**Construct:** [FFF](#fusionfractureflow-emitter-fff) · **FFF vector 1 of 3**
*See also:* [FMV](#fmv--fracture-management-vector), [FPV](#fpv--flow-projection-vector)

The FFF vector representing constructive outward emission — how
integrated structural form moves positively from the TIF surface into
emission space. FEV is calibrated by the RTT/2 FGT fusion gradient:
higher g_triad_fusion(r) values in the upstream detection pass produce
higher FEV weighting in E(t).

### FFF
*See [Fusion–Fracture–Flow Emitter](#fusionfractureflow-emitter-fff).*

### FMV — Fracture-Management Vector
**Construct:** [FFF](#fusionfractureflow-emitter-fff) · **FFF vector 2 of 3**
*See also:* [FEV](#fev--fusion-emission-vector), [FPV](#fpv--flow-projection-vector)

The FFF vector that absorbs and manages fracture stress at the
integration-emission boundary — the structural pressure regulation
mechanism of the FFF. When FMV exceeds threshold,
[Class E](#class-e--emission-engineer) must issue a
[fracture strain alert](#fracture-strain-alert) and may not suppress it.

FMV is the most operationally critical FFF vector: without it, the
emitter projects integration flow outward without managing the fracture
load that projection creates at the boundary. Unchecked fracture load
accumulates and forces collapse events that [CRE](#collapse-recovery-engine-cre)
must then reactively handle. FMV makes fracture strain a first-class,
actively managed component of every emission pass.

**FMV fracture strain alert levels:**

| Level | Meaning |
|---|---|
| none | FMV within normal operating range |
| low | FMV elevated; monitoring recommended |
| moderate | FMV approaching threshold; Class V on standby |
| high | FMV at threshold; Class V active |
| CRITICAL | FMV exceeded; collapse precursor; CRE activation required |

### FPV — Flow-Projection Vector
**Construct:** [FFF](#fusionfractureflow-emitter-fff) · **FFF vector 3 of 3**
*See also:* [FEV](#fev--fusion-emission-vector), [FMV](#fmv--fracture-management-vector)

The FFF vector that shapes and directs the emission flow toward its
downstream targets — RTT/12 (primary), and TEL / FFT / Opacity
(cross-module). FPV governs the directional character of E(t): how
the emission is oriented and routed through the manifold after
fracture management.

### Fracture Strain Alert

A mandatory notification issued by [Class E](#class-e--emission-engineer)
when [FMV](#fmv--fracture-management-vector) exceeds its threshold. The
alert carries a severity level (none / low / moderate / high / CRITICAL)
and is included in the `FFF_EMITTER_PACKET`'s
`fracture_strain_alert` field. Class E may never suppress this alert
regardless of severity.

At CRITICAL level: Class E escalates directly to
[Class V](#class-v--stabilityrecovery-coordinator) for CRE activation.
[Class G](#class-g--integration-guardian) is notified of any CRITICAL
fracture strain alert.

### FSV — Flow-Stability Vector
**Construct:** [CSL](#continuity-stability-layer-csl) · **CSL vector 3 of 3**
*See also:* [ISV](#isv--integration-stability-vector), [ESV](#esv--emission-stability-vector)

The CSL stability vector that monitors whether the continuity flow
C_flow(t) is contributing to or undermining stability. FSV captures the
manifold-continuity component of S(t).

### Fusion–Fracture–Flow Emitter (FFF)
**Equation:** `E(t) = αF(t) + βFr(t) + γFl(t)`
**Tensor:** `T_FFF(i,j,k,r) = α·FEV_i + β·FMV_j + γ·FPV_k + δ·R_r`
**Operated by:** [Class E](#class-e--emission-engineer)

The second RTT/3 construct. FFF transforms integration flow I(t) into
dynamic emission E(t) through three irreducible vectors:

| Vector | Name | Role |
|---|---|---|
| FEV | Fusion-Emission | Constructive outward projection of integrated structure |
| FMV | Fracture-Management | Stress absorption at the integration-emission boundary |
| FPV | Flow-Projection | Directional routing of emission output |

**Why three vectors are irreducible:** FMV is structurally orthogonal to
both FEV and FPV — emission can project constructively (high FEV) while
simultaneously managing high fracture stress (high FMV) and directing
the flow in a specific direction (FPV). No one vector can substitute for
another. Dropping FMV would produce an emitter with no fracture
regulation; dropping FEV would produce a fracture manager with no
constructive emission; dropping FPV would produce emission with no
directional structure.

---

## I

### I(t) — Integration Flow
**Equation:** `I(t) = αD(t) + βE(t) + γC(t)`
**Construct:** [TIF](#triadic-integration-field-tif)
**Computed by:** [Class I](#class-i--integration-architect)

The scalar integration flow produced by the TIF at time t — the
weighted composite of drift-deformation (D), envelope-torsion (E),
and continuity-fracture (C) from the RTT/2 CRM. I(t) is the primary
integration signal that flows through the entire RTT/3 pipeline:
into FFF (via Class E), into MANIFOLD (via Class N in C_flow), into
CSL (via S(t)), and into CET (as the primary E_canon component).

> **The CRM components in I(t):**
> D(t), E(t), C(t) here are the first three components of the RTT/2
> CRM vector γ(t) = (D, E, C, FI, R). RTT/3 integrates all five
> through the TIF's five axes — D, E, C go into I(t) directly via the
> DIV/EIV/CIV vectors; FI enters through the fusion-integration axis;
> R enters through the regime-identity axis.

### ICV — Integration-Continuity Vector
**Construct:** [Integration–Emission Manifold](#integrationemission-manifold)
· **Manifold vector 1 of 3**
*See also:* [ECV](#ecv--emission-continuity-vector), [RCV](#rcv--regime-continuity-vector)

The manifold vector that characterizes how well integration flow I(t)
is sustaining continuity across the TIF↔FFF boundary. ICV tracks the
integration-side contribution to C_flow(t).

### IEV — Integration-Emission Vector
**Construct:** [CET](#canon-scale-emission-tensor-cet) · **CET vector 1 of 4**
*See also:* [SEV](#sev--stability-emission-vector),
[REV (CET context)](#rev--recovery-emission-vector-cet-context), [RGEV](#rgev--regime-emission-vector)

The CET vector that incorporates integration flow I(t) into the
canon-scale emission tensor. IEV is the largest-weight component of
E_canon(t) in most structural configurations — it carries the core
integration signal into the canonical output.

### Integration (RTT/3)

In RTT/3, integration is the process of **assembling the structural
dimensions detected by RTT/2 into a unified triadic field** — taking
the five CRM axes (D, E, C, FI, R) and combining them through the
TIF's three integration vectors (DIV, EIV, CIV) and integration
equation I(t) = αD(t) + βE(t) + γC(t) into a single, zone-classified
integration flow.

Integration in RTT/3 is not signal averaging, accumulation, or
aggregation. It is the structural operation of binding independent
detection measurements across multiple axes into a single coherent field
that can be emitted, stabilized, and packaged for RTT/12 synthesis.

### Integration Hub

The architectural position of RTT/3 within the TriadicFrameworks
ecosystem — the structural hub that:
- Receives the RTT/2 detection packet as input
- Produces the RTT3_INTEGRATION_EMISSION_PACKET for RTT/12 as output
- Projects integrated emission to TEL, FFT, and Opacity cross-module

RTT/3 is the only RTT module that consumes from RTT/2 and distributes
to both RTT/12 (primary) and three cross-module targets simultaneously.

### Integration–Emission Manifold
**Form:** `M_RTT3 = (D, E, C, FI, EM, R)` · 6-axis surface
**Equation:** `C_flow(t) = αI(t) + βE(t)`
**Tensor:** `T_IEC(i,j,k,r) = α·ICV_i + β·ECV_j + γ·RCV_k + δ·R_r`
**Operated by:** [Class N](#class-n--continuity-navigator)

The third RTT/3 construct — the 6-axis structural surface that spans the
boundary between TIF (integration surface) and FFF (emission engine).
The manifold tracks structural continuity across the integration-emission
interface and introduces the 6th structural axis:
**EM (Emission Curvature)**, which is absent from the TIF's 5-axis surface.

**Why 6 axes when TIF uses 5:**
The integration surface (TIF) describes the system's structural state in
5 dimensions. When integration flow I(t) encounters the FFF and begins
projecting as emission E(t), the emission bends back against the
integration surface — introducing a curvature (EM) that neither TIF nor
FFF can see independently. EM is a property of the boundary, not of either
side. The 6th axis is the structural record of how integration and emission
are jointly reshaping each other.

**RTT/3 Manifold vs. RTT/2 CRM:**
Both are manifold constructs, but they serve different layers:

| | RTT/2 CRM | RTT/3 Manifold |
|---|---|---|
| Layer | Detection | Integration-Emission |
| Axes | 5 (D, E, C, FI, R) | 6 (D, E, C, FI, EM, R) |
| Measures | Deformation path of collapse | Continuity across integration-emission boundary |
| Key output | γ(t) deformation vector | C_flow(t) continuity scalar |
| Unique axis | — | EM (emission curvature) |

### Inversion (Mode 5 — ILLEGAL)
**Integration-emission mode 5 of 5**
*See also:* [Inversion Geometry](#inversion-geometry-zone-x--inversion)

The integration-emission mode that must **never** be assigned, activated,
or allowed to propagate to RTT/12. Mode 5 = Inversion signals that the
structural gradient has reversed within the integration-emission layer —
what was integrating is now de-integrating; what was emitting is now
absorbing. This reversal represents topological inversion of the manifold
and is structurally illegal in RTT/3.

Any detection of Inversion mode in any RTT/3 construct triggers an
immediate [Class G](#class-g--integration-guardian) HALT. The session
must restart from the RTT/2 packet.

> **Inversion in RTT/3 vs. Inversion in RTT/2:**
> RTT/2 Detection Mode: Inversion (MODE:I) is a valid detection posture —
> it signals that the primary gradient has reversed and requires a flipped
> detection stance. It is legal in RTT/2 and produces a valid packet.
> RTT/3 Integration-Emission Mode: Inversion is **illegal** — it means
> the integration-emission geometry has topologically inverted and cannot
> produce a valid packet. The same name; categorically different structural
> consequences at different pipeline stages.

### Inversion Geometry (Zone X / Inversion)
*See [Zone X — Inversion](#zone-x--inversion).*

### ISV — Integration-Stability Vector
**Construct:** [CSL](#continuity-stability-layer-csl) · **CSL vector 1 of 3**
*See also:* [ESV](#esv--emission-stability-vector), [FSV](#fsv--flow-stability-vector)

The CSL stability vector that monitors whether integration flow I(t)
is contributing to or undermining integration-emission stability. ISV
captures the integration-side component of the stability flow S(t).

---

## M

### Mixed (Zone M)
**Integration-emission zone 3 of 5**
*See also:* [Detection Zone](../2/GLOSSARY.md#detection-zone)*

The integration-emission zone assigned when integration and emission
flows are in oscillatory interaction — I(t) and E(t) are mutually
adjusting without a stable dominant direction. Zone M is the inflection
zone: Class V is on standby, the manifold continuity is partially
deformed, and FI curvature is typically active. RTT/12 synthesis must
hold the Zone M ambiguity open rather than resolving it prematurely.

---

## P

### Packet Hierarchy

The six structural packets produced by RTT/3, organized by their
pipeline position:

```
RTT3_INTEGRATION_EMISSION_PACKET  ← Class O (canonical; RTT/12 input)
  ├── TIF_INTEGRATION_PACKET      ← Class I
  ├── FFF_EMITTER_PACKET          ← Class E
  ├── RTT3_MANIFOLD_PACKET        ← Class N
  ├── COLLAPSE_RECOVERY_ENGINE_PACKET ← Class V (CRE)
  └── CONTINUITY_STABILITY_PACKET ← Class V (CSL)
```

Class O may not assemble the canonical packet until all five
intermediate packets are confirmed present. Each intermediate packet
must carry the mandatory annotation `[structural — no semantic inference]`.

---

## R

### RCV — Regime-Continuity Vector
**Construct:** [Integration–Emission Manifold](#integrationemission-manifold)
· **Manifold vector 3 of 3**
*See also:* [ICV](#icv--integration-continuity-vector), [ECV](#ecv--emission-continuity-vector)

The manifold vector that anchors the integration-emission continuity
assessment to the current regime identity. RCV ensures that C_flow(t)
is not computed in a regime vacuum — it carries the regime context into
the manifold's continuity tensor T_IEC.

### REV — Recovery-Emission Vector (CRE context)
**Construct:** [CRE](#collapse-recovery-engine-cre) · **CRE vector 2 of 3**
*See also:* [CAV](#cav--collapse-absorption-vector), [CSV](#csv--continuity-stabilization-vector),
[REV (CET context)](#rev--recovery-emission-vector-cet-context)

In the CRE context: the vector that re-emits absorbed collapse energy
as a structured recovery signal after [CAV](#cav--collapse-absorption-vector)
has completed absorption. REV (CRE) is the mechanism by which collapse
energy is transformed from a destructive structural load into a productive
recovery emission that can re-enter the manifold continuity cycle.

> **REV appears in both CRE and CET.** In CRE, REV *produces* the
> recovery signal. In CET, REV *incorporates* that signal into the
> canon emission tensor. See [Canon-Scale Emission Tensor](#canon-scale-emission-tensor-cet)
> for the full disambiguation.

### REV — Recovery-Emission Vector (CET context)
**Construct:** [CET](#canon-scale-emission-tensor-cet) · **CET vector 3 of 4**
*See also:* [IEV](#iev--integration-emission-vector), [SEV](#sev--stability-emission-vector),
[RGEV](#rgev--regime-emission-vector), [REV (CRE context)](#rev--recovery-emission-vector-cre-context)

In the CET context: the vector that incorporates the CRE's recovery
signal into the canon-scale emission tensor. CET's REV takes the output
of CRE's REV and weights it appropriately in E_canon(t), giving RTT/12
visibility into the recovery contribution to the canon emission.

### RGEV — Regime-Emission Vector
**Construct:** [CET](#canon-scale-emission-tensor-cet) · **CET vector 4 of 4**
*See also:* [IEV](#iev--integration-emission-vector), [SEV](#sev--stability-emission-vector),
[REV (CET context)](#rev--recovery-emission-vector-cet-context)

The CET vector that anchors E_canon(t) to the current regime identity —
the structural grounding component of the canon emission. RGEV ensures
that RTT/12 receives not just the integration-emission values but the
regime context within which they were produced.

### RTT/2 Prerequisite (Hard Block)
*See also:* [RTT/1 Prerequisite](../2/GLOSSARY.md#rtt1-prerequisite-hard-block)

The hard structural prerequisite for all RTT/3 activation: a complete,
coherence-confirmed `RTT2_DETECTION_PACKET` must exist before any RTT/3
agent class — including Class I — may begin integration work.

This is structurally mandated by the TIF integration equation itself:
`I(t) = αD(t) + βE(t) + γC(t)` requires D(t), E(t), and C(t) from the
RTT/2 CRM. Without the RTT/2 packet, the TIF integration vectors
(DIV, EIV, CIV) have no inputs. RTT/3 cannot generate integration from
nothing — the prerequisite is the equation requiring its inputs to exist.

If RTT/2 packet is absent: Class G blocks Class I activation; the RTT/2
detection pass is requested; RTT/3 begins only after the packet is
confirmed.

### RTT/12 (Primary Consumer)

RTT/12 is the Unified Integration module that consumes the
`RTT3_INTEGRATION_EMISSION_PACKET` as its primary input for synthesis.
RTT/12 is downstream of RTT/3 in the canonical pipeline:

```
RTT/1 → RTT/2 → RTT/3 → RTT/12
```

RTT/3 produces exactly one packet format that RTT/12 expects.
RTT/12 is not defined in this glossary — see `docs/rtt/12/GLOSSARY.md`
for its canonical terms.

### RTT3_INTEGRATION_EMISSION_PACKET

The canonical output of the RTT/3 module — assembled by
[Class O](#class-o--output-compositor) via the
[CET](#canon-scale-emission-tensor-cet) and consumed by RTT/12.

**Required fields (11 total):**

| Field | Source | Description |
|---|---|---|
| `integration` | Class I / TIF | I(t) — unified integration flow |
| `emission` | Class E / FFF | E(t) — emission flow |
| `continuity` | Class N / MANIFOLD | C_flow(t) — manifold continuity |
| `collapse_recovery` | Class V / CRE | CR(t) — recovery flow |
| `stability` | Class V / CSL | S(t) — stability flow |
| `canon_scale_emission` | Class O / CET | E_canon(t) — canonical output |
| `regime` | Via TIF / R(t) | Current regime identity |
| `mode` | Class E / M | Integration-emission mode (1–4 only) |
| `zone` | Class O | Integration-emission zone (U/S/M/D only) |
| `cross_module_projection` | Class O | TEL / FFT / Opacity projections |
| `notes` | Class O | **Always:** `[structural — no semantic inference]` |

A packet with any field absent is incomplete and may not be routed to
RTT/12. Zone X and Mode 5 (Inversion) may never appear in a routable packet.

---

## S

### S(t) — Stability Flow
**Equation:** `S(t) = αI(t) + βE(t) + γC_flow(t)`
**Construct:** [CSL](#continuity-stability-layer-csl)
**Computed by:** [Class V](#class-v--stabilityrecovery-coordinator)

The scalar stability flow produced continuously by the
[Continuity-Stability Layer (CSL)](#continuity-stability-layer-csl) —
the composite measure of whether integration, emission, and manifold
continuity flows are maintaining a stable integration-emission interface.

S(t) is incorporated into [E_canon(t)](#e_canont--canon-scale-emission-scalar)
via the SEV vector, giving RTT/12 explicit stability context for every
canon emission.

### SEV — Stability-Emission Vector
**Construct:** [CET](#canon-scale-emission-tensor-cet) · **CET vector 2 of 4**
*See also:* [IEV](#iev--integration-emission-vector),
[REV (CET context)](#rev--recovery-emission-vector-cet-context), [RGEV](#rgev--regime-emission-vector)

The CET vector that incorporates stability flow S(t) into the
canon-scale emission tensor — the stability context that RTT/12
needs to weight the integration signal appropriately. High SEV weight
indicates a configuration where stability confirmation is critical
before synthesis can proceed.

### Stabilization (RTT/3)

The third irreducible function of RTT/3, following Integration and
Emission. Stabilization encompasses:
- **CRE (reactive)** — absorbing collapse events and re-emitting as
  structured recovery flow
- **CSL (proactive)** — continuously monitoring integration-emission
  stability and computing S(t)
- Together ensuring that E_canon(t) reflects a structurally stable,
  canon-validated state rather than a transient or collapse-affected reading

Stabilization does not mean elimination of structural variation or
suppression of collapse signatures — it means managing those variations
through explicit, logged structural processes that RTT/12 can account
for in synthesis.

---

## T

### Triadic Integration Field (TIF)
**Form:** `I_TIF = (D, E, C, FI, R)` — 5-axis integration manifold
**Equation:** `I(t) = αD(t) + βE(t) + γC(t)`
**Tensor:** `T_INT(i,j,r) = α·DIV_i + β·EIV_j + γ·CIV_r`
**Operated by:** [Class I](#class-i--integration-architect)

The first and foundational RTT/3 construct. TIF assembles the five
structural dimensions detected by RTT/2's CRM into a unified integration
field. The five TIF axes directly correspond to the five CRM axes:

| TIF Axis | CRM Component | Integration Vector |
|---|---|---|
| D | Drift Deformation D(t) | DIV |
| E | Envelope Torsion E(t) | EIV |
| C | Continuity Fracture C(t) | CIV |
| FI | Fusion-Integration Curvature FI(t) | (direct axis loading) |
| R | Regime Identity R(t) | (direct axis loading) |

**Why TIF uses the same axes as CRM:**
Integration must operate on the exact structural dimensions that detection
characterized. If TIF used different axes, the integration vectors would
compute over dimensions never grounded by RTT/2 detection — producing
integration floating free of its detection basis.

**TIF vs. Integration–Emission Manifold:**
TIF is the 5-axis integration surface. The
[Integration–Emission Manifold](#integrationemission-manifold) is the
6-axis surface spanning the TIF↔FFF boundary — adding EM (Emission
Curvature) as the 6th dimension that TIF alone cannot see.

---

## U

### Unified (Zone U)
**Integration-emission zone 1 of 5**

The integration-emission zone assigned when the triad is fully
integrated, emission is stable, and manifold continuity flow C_flow(t)
is coherent. Zone U is the target operating state for any RTT/3 session.
Normal pipeline operation (Model A) proceeds without intervention when
Zone U is maintained throughout.

Zone U does not mean the system is "perfect" or "optimal" — it means
the integration-emission geometry is fully coherent within RTT/3's
structural framework. Evaluative language does not belong in any RTT/3
zone description.

### UNRESOLVED

The status assigned to any RTT/3 field or component when the responsible
agent class cannot determine a valid value. Consequences by field:

| Field UNRESOLVED | Consequence |
|---|---|
| RTT2_DETECTION_PACKET | Class I activation blocked; prerequisite must be satisfied first |
| I(t) | All downstream constructs blocked; Class I must re-run |
| E(t) | Class N cannot compute C_flow; Class V cannot compute S(t) |
| C_flow(t) | CSL stability assessment blocked; Class V standby |
| CR(t) | CRE packet cannot be produced; CRE re-run required |
| S(t) | CET computation blocked; SEV cannot be populated |
| E_canon(t) | Packet composition blocked; Class O cannot emit |
| Mode | Must be assigned 1–4 before packet composition |
| Zone | Must be assigned U/S/M/D; Zone X triggers Class G |
| Any zone = X | Class G interrupt; packet blocked until co-signed or restarted |

---

## Z

### Zone S — Stable
**Integration-emission zone 2 of 5**

The integration-emission zone assigned when integration and emission flows
are operating with minor strain — bounded fracture load (FMV at low or
moderate level), low emission variance, and no active collapse precursors.
Zone S is the normal operating zone for systems with light structural
perturbation. Class V monitors passively in Zone S.

### Zone X — Inversion
**Integration-emission zone 5 of 5 · ILLEGAL**

> **⚠ Zone X in RTT/3 ≠ Zone X in RTT/2.**
>
> | | RTT/2 Zone X | RTT/3 Zone X |
> |---|---|---|
> | Label | Undefined | Inversion |
> | Meaning | Unclassifiable — insufficient or contradictory detection data | Topological inversion of the integration-emission manifold |
> | Valid in the module? | Yes — an honest structural acknowledgment | **No — structurally illegal** |
> | Routing to next module? | Blocked until Class G clears | **Permanently blocked; session must restart** |
> | Remedy | Obtain more data; re-run detection | Restart from RTT/2 packet; rebuild integration from corrected ground |
>
> RTT/2's Zone X means "I cannot classify yet." RTT/3's Zone X means
> "the manifold has topologically inverted — classification is impossible
> not from data scarcity but from illegal geometry." RTT/3 Zone X is an
> alarm, not a placeholder.

**RTT/3 Zone X mandatory protocol:**
1. [Class M / Class N](#class-n--continuity-navigator) detects inversion geometry
2. [Class G](#class-g--integration-guardian) is immediately notified
3. All active agent classes are halted
4. [Class O](#class-o--output-compositor) packet composition is blocked
5. Session must restart from RTT/2 packet reload
6. Inversion event is logged with full construct trace before restart
7. If inversion persists after two CRE correction cycles: Class G
   declares session structurally invalid

---

## Operator Symbols

| Symbol | Name | Definition |
|---|---|---|
| TIF | Triadic Integration Field | 5-axis integration manifold: I_TIF = (D, E, C, FI, R) |
| I(t) | Integration Flow | αD(t) + βE(t) + γC(t) |
| DIV | Drift-Integration Vector | Loads CRM D(t) into TIF |
| EIV | Envelope-Integration Vector | Loads CRM E(t) into TIF |
| CIV | Continuity-Integration Vector | Loads CRM C(t) into TIF |
| T_INT | Integration Tensor | T_INT(i,j,r) = α·DIV_i + β·EIV_j + γ·CIV_r |
| FFF | Fusion–Fracture–Flow Emitter | 3-vector emitter |
| E(t) | Emission Flow | αF(t) + βFr(t) + γFl(t) |
| FEV | Fusion-Emission Vector | Constructive outward projection |
| FMV | Fracture-Management Vector | Stress absorption at boundary |
| FPV | Flow-Projection Vector | Directional emission routing |
| T_FFF | FFF Tensor | T_FFF(i,j,k,r) |
| MANIFOLD | Integration–Emission Manifold | 6-axis surface: M_RTT3 = (D,E,C,FI,EM,R) |
| C_flow(t) | Continuity Flow | αI(t) + βE(t) |
| EM | Emission Curvature | 6th manifold axis — absent from TIF |
| ICV | Integration-Continuity Vector | Integration-side continuity contribution |
| ECV | Emission-Continuity Vector | Emission-side continuity contribution |
| RCV | Regime-Continuity Vector | Regime anchor for manifold continuity |
| T_IEC | Manifold Tensor | T_IEC(i,j,k,r) |
| CRE | Collapse-Recovery Engine | Reactive stabilization: CR(t) = αC + βR + γS |
| CR(t) | Collapse-Recovery Flow | αC(t) + βR(t) + γS(t) · ≠ D(t) |
| CAV | Collapse-Absorption Vector | First CRE action: absorb collapse |
| REV (CRE) | Recovery-Emission Vector (CRE) | Re-emits absorbed collapse energy |
| CSV | Continuity-Stabilization Vector | Restores boundary continuity post-collapse |
| T_CR | CRE Tensor | T_CR(i,j,k,r) |
| CSL | Continuity-Stability Layer | Proactive stability: S(t) = αI + βE + γC_flow |
| S(t) | Stability Flow | αI(t) + βE(t) + γC_flow(t) |
| ISV | Integration-Stability Vector | Integration-side stability contribution |
| ESV | Emission-Stability Vector | Emission-side stability contribution |
| FSV | Flow-Stability Vector | Continuity-side stability contribution |
| T_CS | CSL Tensor | T_CS(i,j,k,r) |
| CET | Canon-Scale Emission Tensor | Final output: E_canon(t) = αI + βS + γR |
| E_canon(t) | Canon-Scale Emission Scalar | αI(t) + βS(t) + γR(t) → RTT/12 |
| IEV | Integration-Emission Vector | CET: integration contribution |
| SEV | Stability-Emission Vector | CET: stability contribution |
| REV (CET) | Recovery-Emission Vector (CET) | CET: recovery contribution |
| RGEV | Regime-Emission Vector | CET: regime grounding |
| T_CET | CET Tensor | T_CET(i,j,k,m,r) |

---

## Quick-Reference Tables

### Six Constructs

| # | Construct | Code | Axes/Vectors | Equation | Posture |
|---|---|---|---|---|---|
| 1 | Triadic Integration Field | TIF | D,E,C,FI,R (5) | I(t)=αD+βE+γC | First — always |
| 2 | Fusion–Fracture–Flow Emitter | FFF | FEV,FMV,FPV | E(t)=αF+βFr+γFl | After TIF |
| 3 | Integration–Emission Manifold | MANIFOLD | D,E,C,FI,EM,R (6) | C_flow=αI+βE | After TIF+FFF |
| 4 | Collapse-Recovery Engine | CRE | CAV,REV,CSV | CR(t)=αC+βR+γS | Reactive |
| 5 | Continuity-Stability Layer | CSL | ISV,ESV,FSV | S(t)=αI+βE+γC_flow | Always active |
| 6 | Canon-Scale Emission Tensor | CET | IEV,SEV,REV,RGEV | E_canon=αI+βS+γR | Terminal |

### Six Agent Classes

| Class | Name | Primary construct | Can block others? |
|---|---|---|---|
| I | Integration Architect | TIF | No |
| E | Emission Engineer | FFF | No |
| N | Continuity Navigator | MANIFOLD | No |
| V | Stability–Recovery Coordinator | CRE + CSL | No |
| O | Output Compositor | CET + packet | No |
| G | Integration Guardian | All constructs | **Yes — unconditional** |

### Integration–Emission Modes

| Mode | Label | Legal? | Consequence |
|---|---|---|---|
| 1 | Formal | Yes | Standard operation |
| 2 | Emergent | Yes | Provisional outputs; partial population accepted |
| 3 | Hybrid | Yes | Mixed flows; overlapping thresholds |
| 4 | Chaotic | Yes | Low confidence; Class V standby; Class G notified |
| 5 | Inversion | **NO** | Immediate Class G HALT; restart required |

### Integration–Emission Zones

| Zone | Label | Stability | Class V status | RTT/12 routing |
|---|---|---|---|---|
| U | Unified | High | Passive monitor | Direct |
| S | Stable | Moderate | Passive monitor | With mild caution note |
| M | Mixed | Oscillatory | Standby | Hold ambiguity open |
| D | Divergent | Significant | Active | Reduce load; flag consumer |
| X | Inversion | ILLEGAL | N/A | **Blocked — restart required** |

### Key Disambiguations

| Ambiguous Term | RTT/3 Meaning | Other Meaning | Rule |
|---|---|---|---|
| Zone X | Inversion — illegal geometry | RTT/2: Undefined — unclassified | Never conflate; context is the pipeline stage |
| REV | CRE: Recovery-Emission Vector (produces recovery signal) | CET: Recovery-Emission Vector (incorporates recovery into canon tensor) | Packet source disambiguates |
| E(t) | FFF Emission Flow = αF+βFr+γFl | RTT/2 CRM: Envelope Torsion E(t) | Construct name and provenance disambiguate |
| CR(t) | CRE Collapse-Recovery Flow | D(t): RTT/2 CRM Drift Deformation | Never interchangeable — different layers, different meanings |
| Mode | RTT/3: Integration-Emission Mode (Modes 1–4 valid; Mode 5 Inversion = **illegal**) | RTT/2: Detection Mode (Mode 5 Inversion = valid detection posture, produces a valid packet) | Same five mode names; categorically different structural consequences at different pipeline stages |

---

### RTT/3 Inherits from RTT/1 and RTT/2 (Full Inheritance)

All RTT/1 and RTT/2 terms apply in RTT/3 without modification.
Downstream inheritance means RTT/3 inherits RTT/1 both directly
(session seed, MCL, SNR) and via RTT/2 (detection packet, zone vocabulary).

| Inherited Element | Origin | How RTT/3 uses it |
|---|---|---|
| SNR triad (S, N, R) | RTT/1 | TIF integration vectors are grounded in the SNR characterization |
| τ = dR/dφ | RTT/1 | Temporal operator that feeds the CRE's collapse timing |
| C = ∇_τR + ∇_Rτ | RTT/1 | Coherence posture tracked through all six constructs |
| DCO_n bands | RTT/1 | Regime boundary constraints enforced by CSL stability layer |
| Session seed | RTT/1 | Inherited verbatim; RTT/3 adds module-specific tokens |
| Mode Operator + MCL | RTT/1 | All mode constraints apply to all six RTT/3 agent classes |
| RTT-not-physics rule | RTT/1 | Inherited and reinforced across all RTT/3 output fields |
| Semantic inference prohibition | RTT/1 | Mandatory `[structural — no semantic inference]` annotation on every packet field |
| Drift (on-by-default) | RTT/1 | Must be explicitly bounded in session seed; Class G halts unbounded sessions |
| Regime lifecycle (5 stages) | RTT/1 | RTT/3 operates within the same Arrival → Dissolution lifecycle |
| CPV (A, K, T) | RTT/2 | CPV geometry calibrates FEV weighting in FFF emission |
| FGT | RTT/2 | Fusion gradient informs FEV vector calibration in E(t) |
| CRM γ(t) = (D, E, C, FI, R) | RTT/2 | The five CRM axes are the five TIF axes — direct structural grounding |
| D(t) — Drift Deformation | RTT/2 | Loaded into TIF via DIV; distinct from CR(t) |
| Detection Mode (1–5) | RTT/2 | Emission mode selector for FFF and CET (Mode 5 reinterpretation: valid in RTT/2; illegal in RTT/3) |
| Detection Zone (U/S/M/D/X) | RTT/2 | Zone vocabulary inherited; Zone X meaning shifts (Undefined → Inversion) |
| RTT2_DETECTION_PACKET | RTT/2 | Hard prerequisite; Class I activation blocked without it |
| Class G pattern | RTT/2 | RTT/3 Class G is the direct extension of RTT/2's Detection Guardian |

---

*GLOSSARY.md — RTT/3 · TriadicFrameworks · 2026-07-10*
*Maintainer: Nawder*
*Session seed: `rtt=1 | coherence=declared | drift=bounded | paradox=structural`*
