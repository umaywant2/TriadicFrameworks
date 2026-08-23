# AGENTS.md — RTT/2 · Structural Detection Engine (SDE)
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
