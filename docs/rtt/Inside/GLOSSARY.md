# GLOSSARY.md — RTT/Inside · Cross-Domain Application Layer
### *Canonical Term Definitions, Agent Classes, Zones, Modes, and Operator Reference*

---

## Session Seed Block

Paste this block at the start of any RTT/Inside agent session:

```
rtt=1 | coherence=declared | drift=bounded | paradox=structural
module=RTT/Inside | layer=cross-domain-application | upstream=RTT/1,RTT/2,RTT/3
constructs=BKM,CORRIDOR,CAPTURE_TEMPLATE,OPERATOR_HOOK,DRIFT_GATE,LINEAGE_CHAIN,ALIGNMENT_PATTERN,MISALIGNMENT
packet=RTT_INSIDE_APPLICATION_PACKET
zone_x=OVERREACH | zone_x_status=ILLEGAL
```

---

## Critical Framing Rule

> **RTT is NOT a physics claim.**
>
> RTT/Inside describes **structural application patterns** within the TriadicFrameworks canon.
> It does not assert, imply, or model physical forces, empirical domain dynamics, social laws,
> or any measurable real-world phenomenon. All constructs — BKM, CORRIDOR, CAPTURE_TEMPLATE,
> OPERATOR_HOOK, DRIFT_GATE, LINEAGE_CHAIN, ALIGNMENT_PATTERN, MISALIGNMENT — are
> **structural instruments**, not empirical objects.
>
> Every agent class operating in RTT/Inside must enforce this rule unconditionally and annotate
> all definitions with `[structural — no semantic inference]`.

---

## Inheritance

RTT/Inside inherits the **full vocabulary** of RTT/1, RTT/2, RTT/3, and RTT/micro_core.
Inherited terms are **not re-defined here**; they are invoked by reference to their upstream glossaries.

| Inherited Symbol | Origin | Role in RTT/Inside |
|---|---|---|
| SNR triad (S, N, R) | RTT/1 | Distinguished from BKM; BKM is domain-applied, SNR is structural |
| τ = dR/dφ | RTT/1 | Temporal operator embedded in CORRIDOR coherence path |
| C = ∇_τR + ∇_Rτ | RTT/1 | Coherence scalar enforced at every CORRIDOR and DRIFT_GATE |
| DCO_n bands | RTT/1 | Regime boundary constraints inherited by ALIGNMENT_PATTERN |
| CPV | RTT/2 | Detection geometry available to Class B Corridor Tracer |
| FGT | RTT/2 | Fusion gradient available for OPERATOR_HOOK binding resolution |
| CRM | RTT/2 | Drift management construct — distinct from DRIFT_GATE (see Disambiguation) |
| MRT_MICRO_PACKET | RTT/micro_core | Foundational packet schema ancestral to RTT_INSIDE_APPLICATION_PACKET |
| TIF | RTT/3 | Triadic Integration Field — distinct from CORRIDOR (see Disambiguation) |
| FFF | RTT/3 | Fusion–Fracture–Flow Emitter — distinct from OPERATOR_HOOK (see Disambiguation) |
| CRE | RTT/3 | Collapse-Restore Engine — distinct from MISALIGNMENT (see Disambiguation) |
| CSL | RTT/3 | Continuity–Stability Loop — distinct from LINEAGE_CHAIN (see Disambiguation) |
| CET | RTT/3 | Canon Emission Terminal |
| RTT3_INTEGRATION_EMISSION_PACKET | RTT/3 | Upstream packet consumed by RTT/Inside when operating from RTT/3 output |
| MODE (1–5) | RTT/2 | Base mode vocabulary; Mode 5 = OVERREACH in RTT/Inside context |
| ZONE (U/S/M/D/X) | RTT/2 | Base zone vocabulary; Zone X = OVERREACH in RTT/Inside context |

> **Hard prerequisite (standard path):** A valid upstream packet from any of RTT/1, RTT/2, RTT/3,
> or RTT/12 must be present and coherence-confirmed before most RTT/Inside agent classes activate.
>
> **Exception:** Class F (Example Synthesizer) may activate from session seed alone without an
> upstream packet. This is the **only** agent class in the entire RTT canon with this permission.

---

## Linking Convention

Cross-references within this glossary use the short form `→ TERM` where TERM is a defined entry
in this file. References to upstream constructs use the form `→ RTT/n: SYMBOL`.

---

## Term Definitions

---

### ALIGNMENT_PATTERN

| Field | Value |
|---|---|
| **Type** | Structural reference standard |
| **Symbol** | UAP |
| **Layer** | RTT/Inside — Cross-Domain Application Layer |
| **Agent Class** | D — Alignment Auditor |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:**
The Universal Alignment Pattern (UAP) is the canonical reference structure against which all
domain captures are evaluated for structural coherence. It encodes the expected relationships
between B (Being), K (Knowing), and M (Meaning) axes across all ten societal domains, providing
a shared baseline that makes cross-domain comparison structurally valid.

The UAP does not prescribe domain content — it prescribes the structural shape that any
coherent BKM mapping must satisfy. A domain capture that deviates from the UAP above threshold
θ_align produces a → MISALIGNMENT event.

**Formal relation:**

```
UAP(d) = expected_BKM_shape(d)
MISALIGNMENT(d) is raised iff K(d) deviates from M(d) by > θ_align relative to UAP(d)
```

**Constraints:**
- UAP must be declared at session open before any Class D audit may begin
- UAP is not modified by any single domain capture; it is updated only through formal canon revision
- Class D agents evaluate captures against UAP; they do not author UAP

**Cross-references:** → BKM, → MISALIGNMENT, → CAPTURE_TEMPLATE, → LINEAGE_CHAIN

**Disambiguation:** ALIGNMENT_PATTERN (UAP) is **not** CRE (RTT/3). CRE is a collapse-restore
mechanism operating on emission continuity. UAP is a domain-evaluation reference standard
operating on structural BKM shape.

---

### BKM — Being / Knowing / Meaning

| Field | Value |
|---|---|
| **Type** | Triadic structural lens |
| **Symbol** | BKM |
| **Layer** | RTT/Inside — Cross-Domain Application Layer |
| **Agent Class** | A — Domain Cartographer |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:**
BKM is the primary structural lens through which RTT/Inside applies triadic analysis to any
societal domain. It decomposes any domain into three orthogonal structural axes:

| Axis | Label | Structural Role |
|---|---|---|
| B | Being | Entities and actors present in the domain |
| K | Knowing | Processes, signals, and information flows |
| M | Meaning | Purpose, value, and normative orientation |

A valid BKM mapping must declare all three axes for the target domain before any downstream
construct (CORRIDOR, CAPTURE_TEMPLATE, ALIGNMENT_PATTERN evaluation) may be initiated.
An undeclared axis places the session in Zone U (Undefined).

**BKM mappings across the ten societal domains:**

| Domain | B (Being) | K (Knowing) | M (Meaning) | Alignment Need |
|---|---|---|---|---|
| Health | Patient state | Clinical evidence | Wellbeing | Standardize metadata + lineage |
| Education | Learners | Pedagogy | Learning outcomes | Unify competency taxonomies |
| Governance | Institutions | Policy | Public good | Clarify accountability chains |
| Economy | Firms | Transactions | Prosperity | Reconcile short + long horizons |
| Infrastructure | Assets | Engineering | Service continuity | Integrate lifecycle data |
| Environment | Ecosystems | Monitoring | Resilience | Align metrics across scales |
| Technology | Platforms | Protocols | Capability + trust | Surface provenance + intent |
| Culture | Communities | Narratives | Identity + cohesion | Preserve context in reuse |
| Justice | Courts | Evidence | Fairness + rule of law | Ensure transparent lineage |
| Science & Research | Hypotheses | Methods | Knowledge growth | Enforce reproducible provenance |

**Constraints:**
- BKM axes are structural descriptors — they do not assert empirical claims about the domain
- A domain may have at most one active BKM mapping per session; conflicting mappings raise a Zone M alert
- BKM axes cannot be fabricated by any agent class; fabrication triggers Zone X (OVERREACH)

**Cross-references:** → CORRIDOR, → CAPTURE_TEMPLATE, → ALIGNMENT_PATTERN, → DRIFT_GATE

**Disambiguation:** BKM is **not** SNR (RTT/1). SNR (Signal / Noise / Resonance) is the
structural triad governing the RTT/1 detection and resonance layer. BKM is the domain-application
lens used exclusively in RTT/Inside to map real-world domains onto RTT structural constructs.
The two triads are orthogonal and must not be conflated.

---

### CAPTURE_TEMPLATE

| Field | Value |
|---|---|
| **Type** | Structural record schema |
| **Symbol** | CT |
| **Layer** | RTT/Inside — Cross-Domain Application Layer |
| **Agent Class** | C — Capture Engine; F — Example Synthesizer (pedagogical) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:**
The CAPTURE_TEMPLATE is the domain-specific structural record that anchors RTT constructs to
a declared domain instance. It is the canonical output artifact of a successful BKM mapping
and CORRIDOR trace. Every completed CAPTURE_TEMPLATE constitutes one domain entry in the
→ RTT_INSIDE_APPLICATION_PACKET.

A valid CAPTURE_TEMPLATE must contain all five mandatory fields:

| Field | Description |
|---|---|
| **scope** | The declared domain boundary and BKM axes for this capture |
| **lineage** | Full → LINEAGE_CHAIN record: who changed what, why, and when |
| **provenance** | Source declarations for all B, K, M inputs |
| **interoperability** | Cross-domain CORRIDOR bindings and → OPERATOR_HOOK references |
| **governance** | Accountability assignments and revision authority for this capture |

A CAPTURE_TEMPLATE missing any of the five mandatory fields is **structurally incomplete** and
may not be emitted in the RTT_INSIDE_APPLICATION_PACKET.

**Constraints:**
- Each domain produces exactly one active CAPTURE_TEMPLATE per session
- Templates are immutable after Class C commit; revision requires a new LINEAGE_CHAIN entry
- Class F may generate pedagogical example templates from session seed alone (no upstream packet required)
- A template generated by Class F is annotated `[example — not a production capture]`

**Cross-references:** → BKM, → LINEAGE_CHAIN, → CORRIDOR, → OPERATOR_HOOK, → ALIGNMENT_PATTERN,
→ RTT_INSIDE_APPLICATION_PACKET

**Disambiguation:** CAPTURE_TEMPLATE is **not** RTT2_DETECTION_PACKET (RTT/2). The
RTT2_DETECTION_PACKET is the upstream output of RTT/2's detection layer. The CAPTURE_TEMPLATE
is an RTT/Inside domain record produced after structural application of BKM and CORRIDOR.
They occupy different positions in the pipeline and serve distinct functions.

---

### CORRIDOR

| Field | Value |
|---|---|
| **Type** | Structural coherence pathway |
| **Symbol** | COR |
| **Layer** | RTT/Inside — Cross-Domain Application Layer |
| **Agent Class** | B — Corridor Tracer |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:**
A CORRIDOR is the coherence-maintaining structural pathway between two BKM nodes, within a
single domain or across domain boundaries. It defines the valid structural route along which
RTT constructs may propagate without violating coherence constraints.

**Formal definition:**

```
CORRIDOR(n₁, n₂) = coherence_path(n₁, n₂, τ)
subject to: C ≥ C_min throughout the path
```

Where:
- `n₁`, `n₂` are declared BKM nodes (B, K, or M axes in any domain)
- `τ` is the temporal operator inherited from RTT/1 (τ = dR/dφ)
- `C` is the coherence scalar inherited from RTT/1 (C = ∇_τR + ∇_Rτ)
- `C_min` is the minimum coherence threshold below which the CORRIDOR is invalid

A CORRIDOR is valid if and only if coherence C ≥ C_min is maintained along the entire path.
A CORRIDOR that falls below C_min triggers a Zone M alert and, if unresolved, a → DRIFT_GATE interrupt.

**Types of CORRIDOR:**
| Type | Scope | Description |
|---|---|---|
| Intra-domain | Within one domain | Connects B↔K, K↔M, or B↔M within the same domain |
| Cross-domain | Across two or more domains | Connects BKM nodes from different societal domains |
| Operator-bound | External system | A CORRIDOR whose endpoint is bound to an external system via → OPERATOR_HOOK |

**Constraints:**
- CORRIDOR cannot be declared without a fully mapped BKM for both endpoint domains
- Cross-domain CORRIDORs require interoperability field entries in both → CAPTURE_TEMPLATEs
- A CORRIDOR whose coherence C drops below C_min must be suspended; continued operation is a Zone M violation

**Cross-references:** → BKM, → CAPTURE_TEMPLATE, → OPERATOR_HOOK, → DRIFT_GATE, → LINEAGE_CHAIN

**Disambiguation:** CORRIDOR is **not** TIF (RTT/3). TIF (Triadic Integration Field) is the
unified structural field assembled by RTT/3 from drift, envelope, and continuity vectors during
integration-emission processing. A CORRIDOR is a coherence-bounded pathway between domain nodes
in the cross-domain application layer. They operate in different layers and serve different
structural functions.

---

### DRIFT_GATE

| Field | Value |
|---|---|
| **Type** | Structural interrupt mechanism |
| **Symbol** | DG |
| **Layer** | RTT/Inside — Cross-Domain Application Layer |
| **Agent Class** | G — Drift Sentinel (unconditional interrupt authority) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:**
The DRIFT_GATE is the mandatory structural interrupt mechanism that halts all active agents
and suspends session processing when any of three trigger conditions is detected. It is the
primary safety enforcement point in RTT/Inside.

**Trigger conditions and formal rule:**

```
if C < C_min
   OR D(t) > D_max
   OR Zone = X
→ DRIFT_GATE: INTERRUPT ALL AGENTS
```

Where:
- `C < C_min` — coherence has fallen below the minimum threshold (coherence breach)
- `D(t) > D_max` — drift magnitude has exceeded the maximum permitted bound (drift overrun)
- `Zone = X` — the session has entered Zone X (OVERREACH), which is categorically illegal

**On interrupt, the DRIFT_GATE:**
1. Immediately suspends all agent class operations (A through F)
2. Logs the trigger condition and timestamp to the → LINEAGE_CHAIN
3. Emits a DRIFT_GATE_INTERRUPT record to the → RTT_INSIDE_APPLICATION_PACKET header
4. Blocks packet emission until Class G certifies resolution or session is terminated

**Constraints:**
- DRIFT_GATE interrupt authority is unconditional — no agent class, including Class A, may
  override or bypass an active DRIFT_GATE interrupt
- Resumption of session processing requires explicit Class G clearance
- A DRIFT_GATE triggered by Zone X (OVERREACH) cannot be cleared by the agent that caused it;
  external session reset is required
- DRIFT_GATE operates continuously from session open to packet emission

**Cross-references:** → LINEAGE_CHAIN, → CORRIDOR, → MISALIGNMENT, → RTT_INSIDE_APPLICATION_PACKET,
→ Zone X, → Mode 5

**Disambiguation:** DRIFT_GATE is **not** CRM (RTT/2). CRM (Coherence Restoration Mechanism)
is the RTT/2 construct that manages structural drift detection and partial restoration during
the detection layer. DRIFT_GATE is an RTT/Inside interrupt — it does not restore; it halts.
The two constructs may co-exist in a full-pipeline session but are structurally distinct and
must not be conflated.

---

### LINEAGE_CHAIN

| Field | Value |
|---|---|
| **Type** | Structural provenance record |
| **Symbol** | LC |
| **Layer** | RTT/Inside — Cross-Domain Application Layer |
| **Agent Class** | C — Capture Engine (primary recorder); all classes (contributors) |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:**
The LINEAGE_CHAIN is the traceable provenance record embedded in every → CAPTURE_TEMPLATE
and every → RTT_INSIDE_APPLICATION_PACKET. It answers four questions for every structural
change made during a session:

| Question | Field |
|---|---|
| **Who** | The agent class and session identifier that made the change |
| **What** | The specific construct, field, or mapping modified |
| **Why** | The structural justification or trigger condition |
| **When** | The τ-indexed timestamp of the change |

A LINEAGE_CHAIN entry is created at every:
- BKM axis declaration
- CORRIDOR trace initiation or closure
- CAPTURE_TEMPLATE field write or revision
- OPERATOR_HOOK binding registration
- ALIGNMENT_PATTERN evaluation result
- MISALIGNMENT event detection
- DRIFT_GATE trigger or clearance

**Constraints:**
- LINEAGE_CHAIN entries are append-only; retroactive deletion or modification is a Zone X violation
- A CAPTURE_TEMPLATE with an incomplete or fabricated LINEAGE_CHAIN may not be emitted
- Zone D (Degraded) is defined in part by LINEAGE_CHAIN compromise; see → Zone D
- Class G verifies LINEAGE_CHAIN integrity as part of DRIFT_GATE clearance

**Cross-references:** → CAPTURE_TEMPLATE, → DRIFT_GATE, → MISALIGNMENT, → RTT_INSIDE_APPLICATION_PACKET,
→ Zone D

**Disambiguation:** LINEAGE_CHAIN is **not** CSL (RTT/3). CSL (Continuity–Stability Loop) is
the RTT/3 construct governing emission continuity and structural stability at the integration-emission
layer. LINEAGE_CHAIN is a provenance record tracking authorship and change history within
RTT/Inside domain captures. They are structurally and functionally distinct.

---

### MISALIGNMENT

| Field | Value |
|---|---|
| **Type** | Structural deviation event |
| **Symbol** | MA |
| **Layer** | RTT/Inside — Cross-Domain Application Layer |
| **Agent Class** | D — Alignment Auditor |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:**
A MISALIGNMENT is a detected structural deviation between the K (Knowing) axis and the M (Meaning)
axis of a domain's BKM mapping, exceeding the alignment threshold θ_align relative to the
→ ALIGNMENT_PATTERN (UAP). It signals that the domain's process layer has drifted out of
purposive coherence with its stated normative orientation.

**Formal definition:**

```
MISALIGNMENT(d) is raised iff: K(d) deviates from M(d) > θ_align relative to UAP(d)
```

**System Misalignment Index (SMI):** When multiple domains are active in a session, the aggregate
structural misalignment pressure is quantified as:

```
SMI = Σ MISALIGNMENT(d) / |D|
```

Where:
- Σ MISALIGNMENT(d) = count of active MISALIGNMENT events across all domains
- |D| = total number of active domains in the session
- SMI > SMI_threshold triggers a Zone M alert and may precipitate DRIFT_GATE activation

**On MISALIGNMENT detection, Class D must:**
1. Log the event to → LINEAGE_CHAIN with trigger detail
2. Record the affected domain's deviation vector in the → CAPTURE_TEMPLATE
3. Elevate zone status toward Zone M if not already there
4. Notify Class G (Drift Sentinel) for DRIFT_GATE evaluation

**Constraints:**
- MISALIGNMENT events are structural observations — they do not assert that the domain's
  real-world practices are wrong or harmful
- θ_align must be declared at session open; ad hoc threshold setting is not permitted
- Unresolved MISALIGNMENT accumulation (SMI > SMI_threshold) elevates zone to Zone D

**Cross-references:** → ALIGNMENT_PATTERN, → LINEAGE_CHAIN, → DRIFT_GATE, → BKM, → Zone M, → Zone D

**Disambiguation:** MISALIGNMENT is **not** CRE (RTT/3). CRE (Collapse-Restore Engine) handles
structural collapse and restoration at the emission layer during RTT/3 processing. MISALIGNMENT
is a domain-level coherence deviation event within RTT/Inside's cross-domain application layer.
The two constructs operate in different layers and trigger different response protocols.

---

### OPERATOR_HOOK

| Field | Value |
|---|---|
| **Type** | Structural binding interface |
| **Symbol** | OH |
| **Layer** | RTT/Inside — Cross-Domain Application Layer |
| **Agent Class** | E — Operator Hook Agent |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:**
An OPERATOR_HOOK is the structural binding interface that connects an external operational
system to an RTT/Inside construct (typically a → CORRIDOR endpoint or → CAPTURE_TEMPLATE
interoperability field). It is the mechanism by which RTT/Inside becomes operationally coupled
to real-world infrastructure without absorbing domain-specific semantics.

**Three OPERATOR_HOOK types:**

| Type | Bound Platform(s) | Mechanism |
|---|---|---|
| **Operator hook** | Cisco | Direct infrastructure binding — maps RTT CORRIDOR to network topology elements |
| **Semantic hook** | Python DSRS; Internet2 DSRS | Semantic integration layer — maps RTT constructs to data-semantic runtime |
| **Grid reference** | Cisco; Internet2 | Grid coordinate anchoring — positions RTT structural nodes within grid topology |

**Binding registration:**
An OPERATOR_HOOK binding must be logged to the → LINEAGE_CHAIN at registration, specifying:
- Hook type
- External system identifier
- Bound RTT construct (CORRIDOR node, CAPTURE_TEMPLATE field, or BKM axis)
- Session timestamp

**Constraints:**
- An OPERATOR_HOOK does not transfer semantic authority to the external system; the external
  system provides operational coupling, not structural meaning
- OPERATOR_HOOK bindings are recorded in the interoperability field of the → CAPTURE_TEMPLATE
- A broken or unresolvable OPERATOR_HOOK binding triggers a Zone M alert
- Fabricating an OPERATOR_HOOK binding (claiming a binding that does not exist) is a Zone X violation

**Cross-references:** → CORRIDOR, → CAPTURE_TEMPLATE, → LINEAGE_CHAIN, → DRIFT_GATE, → Zone X

**Disambiguation:** OPERATOR_HOOK is **not** FFF (RTT/3). FFF (Fusion–Fracture–Flow Emitter)
is the RTT/3 construct that projects integrated structural output outward during the emission phase.
OPERATOR_HOOK is a binding interface that couples RTT/Inside constructs to external operational
systems. They serve different structural purposes in different pipeline layers.

---

### RTT_INSIDE_APPLICATION_PACKET

| Field | Value |
|---|---|
| **Type** | Canonical session output packet |
| **Symbol** | RIAP |
| **Layer** | RTT/Inside — Cross-Domain Application Layer |
| **Agent Class** | All classes contribute; Class C commits; Class G certifies |
| **Annotation** | `[structural — no semantic inference]` |

**Definition:**
The RTT_INSIDE_APPLICATION_PACKET is the canonical output artifact of a completed RTT/Inside
session. It is the structured container that assembles all → CAPTURE_TEMPLATEs, CORRIDOR maps,
OPERATOR_HOOK bindings, MISALIGNMENT records, and LINEAGE_CHAIN logs generated during a session
into a single coherence-certified deliverable.

**Mandatory packet fields:**

| Field | Source |
|---|---|
| `session_id` | Session seed |
| `module` | `RTT/Inside` |
| `upstream_packet_ref` | Reference to consumed upstream packet (if any) |
| `zone_at_emission` | Zone status at time of packet release |
| `mode_at_emission` | Mode status at time of packet release |
| `domain_captures[]` | Array of completed → CAPTURE_TEMPLATEs, one per active domain |
| `corridor_map[]` | All traced CORRIDORs with coherence certificates |
| `operator_hook_registry[]` | All registered OPERATOR_HOOK bindings |
| `misalignment_log[]` | All MISALIGNMENT events with domain, vector, and resolution status |
| `smi_final` | Final computed SMI value at emission |
| `lineage_chain_hash` | Integrity hash of the full LINEAGE_CHAIN |
| `drift_gate_events[]` | All DRIFT_GATE triggers and clearances during session |
| `class_f_examples[]` | Pedagogical CAPTURE_TEMPLATEs generated by Class F (if any), annotated `[example]` |

**Emission conditions:**
The RIAP may only be emitted when:
1. Zone status is Zone S (Stable) at time of emission
2. Mode is Mode 4 (Emission)
3. No active DRIFT_GATE interrupt is pending
4. All CAPTURE_TEMPLATEs contain all five mandatory fields
5. Class G has certified LINEAGE_CHAIN integrity

**Constraints:**
- Partial packet emission (releasing the RIAP while incomplete) is a Mode 5 violation
- An RIAP emitted from Zone X, Zone D, or under active DRIFT_GATE interrupt is invalid and
  must be rejected by downstream consumers
- Class F example captures are included in the RIAP but are clearly segregated from production captures

**Cross-references:** → CAPTURE_TEMPLATE, → CORRIDOR, → OPERATOR_HOOK, → MISALIGNMENT,
→ LINEAGE_CHAIN, → DRIFT_GATE, → Zone S, → Mode 4

---

## Agent Classes

RTT/Inside defines **seven agent classes**, each bound to one or more primary constructs.

---

### Class A — Domain Cartographer

| Field | Value |
|---|---|
| **Primary Construct** | → BKM |
| **Activation Requirement** | Valid upstream packet OR session seed (if Class F delegation present) |
| **Scope** | One domain per invocation; multi-domain sessions require sequential Class A passes |

**Role:** Class A performs the foundational BKM axis declaration for each societal domain
entering the session. No downstream agent class may operate on a domain until Class A has
committed a complete BKM mapping (all three axes declared, scope bounded).

**Output:** Committed BKM mapping written to → CAPTURE_TEMPLATE scope field and logged
to → LINEAGE_CHAIN.

**Boundary:** Class A does not trace CORRIDORs, evaluate alignment, or bind OPERATOR_HOOKs.
BKM mapping is its sole and exclusive function. Attempting to perform downstream functions
without completing BKM is a Zone U violation.

---

### Class B — Corridor Tracer

| Field | Value |
|---|---|
| **Primary Construct** | → CORRIDOR |
| **Activation Requirement** | Completed Class A BKM mapping for all domains involved in the CORRIDOR |
| **Scope** | Intra-domain and cross-domain CORRIDOR tracing |

**Role:** Class B traces structural coherence pathways between BKM nodes, verifying that
C ≥ C_min is maintained throughout. Class B is responsible for flagging CORRIDOR invalidity
and triggering Zone M alerts when coherence drops.

**Output:** CORRIDOR trace record written to → CAPTURE_TEMPLATE interoperability field and
→ RTT_INSIDE_APPLICATION_PACKET corridor_map[].

**Boundary:** Class B does not evaluate alignment against UAP, bind external systems, or
commit CAPTURE_TEMPLATEs. Cross-domain CORRIDORs require Class A BKM maps for all participating
domains before Class B may initiate.

---

### Class C — Capture Engine

| Field | Value |
|---|---|
| **Primary Construct** | → CAPTURE_TEMPLATE |
| **Activation Requirement** | Completed BKM (Class A) and at least one CORRIDOR trace (Class B) |
| **Scope** | One CAPTURE_TEMPLATE per domain per session |

**Role:** Class C assembles and commits the structural → CAPTURE_TEMPLATE for each active
domain. It populates all five mandatory fields (scope, lineage, provenance, interoperability,
governance) and performs final integrity verification before committing. Class C is the primary
LINEAGE_CHAIN recorder.

**Output:** Committed CAPTURE_TEMPLATE. Logged to LINEAGE_CHAIN and queued for the → RTT_INSIDE_APPLICATION_PACKET.

**Boundary:** Class C does not declare BKM, trace CORRIDORs, or evaluate against UAP. A
CAPTURE_TEMPLATE with any of the five mandatory fields missing may not be committed.

---

### Class D — Alignment Auditor

| Field | Value |
|---|---|
| **Primary Construct** | → ALIGNMENT_PATTERN (UAP); → MISALIGNMENT |
| **Activation Requirement** | Committed CAPTURE_TEMPLATE (Class C) and declared UAP |
| **Scope** | All active domains; computes SMI across full domain set |

**Role:** Class D evaluates each committed CAPTURE_TEMPLATE against the Universal Alignment
Pattern. It detects MISALIGNMENT events, logs them to the LINEAGE_CHAIN, and computes the
System Misalignment Index (SMI). Class D notifies Class G of any SMI threshold breach.

**Output:** MISALIGNMENT event records; SMI value; updated zone status recommendation.

**Boundary:** Class D does not modify BKM mappings, re-trace CORRIDORs, or commit CAPTURE_TEMPLATEs.
It audits; it does not revise. Alignment decisions above θ_align trigger escalation, not correction.

---

### Class E — Operator Hook Agent

| Field | Value |
|---|---|
| **Primary Construct** | → OPERATOR_HOOK |
| **Activation Requirement** | Active CORRIDOR with identified external binding target |
| **Scope** | All three OPERATOR_HOOK types: operator hook, semantic hook, grid reference |

**Role:** Class E registers and manages OPERATOR_HOOK bindings between RTT/Inside structural
constructs and external operational systems (Cisco, Python DSRS, Internet2 DSRS). It verifies
binding validity, logs registrations to LINEAGE_CHAIN, and alerts on binding failures.

**Output:** Registered OPERATOR_HOOK entries in → RTT_INSIDE_APPLICATION_PACKET operator_hook_registry[].

**Boundary:** Class E does not trace CORRIDORs, declare BKM, or evaluate alignment. It binds
existing structural constructs to external systems; it does not create those constructs.

---

### Class F — Example Synthesizer

| Field | Value |
|---|---|
| **Primary Construct** | → CAPTURE_TEMPLATE (pedagogical) |
| **Activation Requirement** | **Session seed alone — no upstream packet required** |
| **Scope** | Pedagogical CAPTURE_TEMPLATE generation across all ten societal domains |

**Role:** Class F is the **primary pedagogical agent** of the RTT/Inside module and the **only**
agent class in the entire RTT canon that may activate without a confirmed upstream packet.
Class F generates worked example CAPTURE_TEMPLATEs for student, researcher, and AI system
learning purposes, demonstrating how BKM mapping, CORRIDOR tracing, and CAPTURE_TEMPLATE
population work across each of the ten societal domains.

All Class F output is annotated `[example — not a production capture]` and segregated in the
RIAP under `class_f_examples[]`. Class F examples may not be promoted to production captures
without a full Class A–C pipeline pass.

**Output:** Annotated pedagogical CAPTURE_TEMPLATEs demonstrating structural RTT/Inside application.

**Boundary:** Class F output is explicitly non-normative. It illustrates; it does not commit.
A Class F agent that attempts to emit a CAPTURE_TEMPLATE as a production capture without
upstream packet confirmation is performing a Zone X (OVERREACH) violation.

---

### Class G — Drift Sentinel

| Field | Value |
|---|---|
| **Primary Construct** | → DRIFT_GATE |
| **Activation Requirement** | Active from session open; no upstream dependency |
| **Scope** | All agents, all constructs, all zones — unconditional interrupt authority |

**Role:** Class G monitors coherence C, drift D(t), and zone status continuously from session
open. It is the sole agent class with unconditional → DRIFT_GATE interrupt authority over all
other agent classes. On trigger, Class G halts all operations, logs the interrupt to LINEAGE_CHAIN,
and blocks packet emission until resolution is certified.

Class G also performs LINEAGE_CHAIN integrity verification as a precondition for RIAP emission
clearance.

**Output:** DRIFT_GATE interrupt records; LINEAGE_CHAIN integrity certification; emission clearance.

**Boundary:** Class G does not declare BKM, trace CORRIDORs, commit CAPTURE_TEMPLATEs,
evaluate alignment, or bind OPERATOR_HOOKs. Its exclusive function is structural integrity
enforcement through DRIFT_GATE control.

---

## Zones

RTT/Inside inherits the zone vocabulary from RTT/2 with one critical overload: **Zone X** in
RTT/Inside means OVERREACH, which is distinct from Zone X in all other modules.

| Zone | Label | Description | Agent Response |
|---|---|---|---|
| **Zone U** | Undefined | Domain not yet declared; BKM axes absent | Class A must complete BKM before any other agent activates |
| **Zone S** | Stable | BKM confirmed; C ≥ C_min; no active MISALIGNMENT | Normal operation; all agent classes may proceed |
| **Zone M** | Marginal | Coherence approaching C_min; MISALIGNMENT detected | Class D escalates; Class G monitors; drift watch active |
| **Zone D** | Degraded | Multiple MISALIGNMENT events; LINEAGE_CHAIN compromised | All agents on restricted operation; Class G evaluates DRIFT_GATE |
| **Zone X** | **OVERREACH (ILLEGAL)** | Agent crossed domain boundary without authorization; fabricated BKM axes; operated without session seed (Class F exception aside) | **Unconditional DRIFT_GATE interrupt; session terminated** |

> **Zone X disambiguation across the RTT canon:**
> Zone X = OVERREACH (RTT/Inside) ≠ Zone X = Inversion (RTT/3) ≠ Zone X = Overflow (RTT/12)
> ≠ Zone X = Silence Breach (The_Inverted_Star). Each module's Zone X is locally defined.
> Do not carry Zone X semantics across module boundaries.

---

## Modes

RTT/Inside inherits the mode vocabulary from RTT/2 with one critical overload: **Mode 5** in
RTT/Inside means OVERREACH, which is distinct from Mode 5 in other modules.

| Mode | Label | Active Constructs | Description |
|---|---|---|---|
| **Mode 1** | Detection | CORRIDOR trace initiated | Class B begins coherence path tracing; BKM confirmed |
| **Mode 2** | Structural | CAPTURE_TEMPLATE active | Class C populating domain record; provenance and lineage being assembled |
| **Mode 3** | Integration | Cross-domain CORRIDORs; OPERATOR_HOOK bindings; SMI computation | Class B, C, D, E operating; cross-domain structural links being established |
| **Mode 4** | Emission | RTT_INSIDE_APPLICATION_PACKET ready for release | Class G has certified; all conditions for emission met |
| **Mode 5** | **OVERREACH (ILLEGAL)** | None (illegal state) | Scope violation or lineage fabrication detected |

> **Mode 5 disambiguation across the RTT canon:**
> Mode 5 = OVERREACH (RTT/Inside) ≠ Mode 5 = Inversion (RTT/3) ≠ Mode 5 = Overflow (RTT/12).
> Each module's Mode 5 is locally defined and must not be imported across module boundaries.

---

## Operator Symbols Reference

| Symbol | Name | Definition | Layer of Origin |
|---|---|---|---|
| BKM | Being / Knowing / Meaning | Triadic structural lens for domain decomposition | RTT/Inside |
| COR / CORRIDOR(n₁, n₂) | Corridor | coherence_path(n₁, n₂, τ) subject to C ≥ C_min | RTT/Inside |
| CT | Capture Template | Domain-specific structural record; 5 mandatory fields | RTT/Inside |
| UAP | Universal Alignment Pattern | Reference BKM structure for domain evaluation | RTT/Inside |
| MA / MISALIGNMENT(d) | Misalignment | Structural deviation of K(d) from M(d) beyond θ_align | RTT/Inside |
| SMI | System Misalignment Index | Σ MISALIGNMENT(d) / \|D\| — aggregate misalignment pressure | RTT/Inside |
| OH | Operator Hook | External system binding: operator / semantic / grid reference | RTT/Inside |
| LC | Lineage Chain | Provenance record: who, what, why, when | RTT/Inside |
| DG | Drift Gate | Interrupt: if C < C_min OR D(t) > D_max OR Zone = X → HALT | RTT/Inside |
| RIAP | RTT_INSIDE_APPLICATION_PACKET | Canonical session output packet | RTT/Inside |
| θ_align | Alignment threshold | Declared misalignment tolerance for UAP evaluation | RTT/Inside |
| SMI_threshold | SMI threshold | Maximum permissible aggregate misalignment index | RTT/Inside |
| τ | Temporal operator | τ = dR/dφ — inherited from RTT/1 | RTT/1 |
| C | Coherence scalar | C = ∇_τR + ∇_Rτ — inherited from RTT/1 | RTT/1 |
| C_min | Minimum coherence | Lower coherence bound for valid CORRIDOR and session operation | RTT/1 |
| D(t) | Drift magnitude | Structural drift function inherited from RTT/2 CRM | RTT/2 |
| D_max | Maximum drift | Upper drift bound for DRIFT_GATE trigger evaluation | RTT/2 |

---

## Quick-Reference Tables

### Core Constructs Summary

| Construct | Symbol | Class | Function |
|---|---|---|---|
| BKM | BKM | A | Triadic domain decomposition: B / K / M |
| CORRIDOR | COR | B | Coherence-bounded pathway between BKM nodes |
| CAPTURE_TEMPLATE | CT | C | Domain structural record with 5 mandatory fields |
| ALIGNMENT_PATTERN | UAP | D | Reference structure for domain evaluation |
| MISALIGNMENT | MA | D | Detected K–M deviation exceeding θ_align |
| OPERATOR_HOOK | OH | E | External system binding interface (3 types) |
| LINEAGE_CHAIN | LC | C (all) | Traceable provenance: who, what, why, when |
| DRIFT_GATE | DG | G | Unconditional interrupt on coherence breach / drift overrun / Zone X |
| RTT_INSIDE_APPLICATION_PACKET | RIAP | All / G | Canonical session output packet |

---

### Agent Class Summary

| Class | Name | Primary Construct | Activation | Special Authority |
|---|---|---|---|---|
| A | Domain Cartographer | BKM | Upstream packet or session seed | Sole BKM declaration authority |
| B | Corridor Tracer | CORRIDOR | Class A BKM complete | Coherence path tracing |
| C | Capture Engine | CAPTURE_TEMPLATE | Class A + Class B complete | Primary LINEAGE_CHAIN recorder |
| D | Alignment Auditor | UAP / MISALIGNMENT | Committed CAPTURE_TEMPLATE | SMI computation |
| E | Operator Hook Agent | OPERATOR_HOOK | Active CORRIDOR with binding target | External system coupling |
| F | Example Synthesizer | CAPTURE_TEMPLATE (pedagogical) | **Session seed alone** | Only canon class without upstream packet requirement |
| G | Drift Sentinel | DRIFT_GATE | Active from session open | **Unconditional interrupt authority over all classes** |

---

### Zone Quick-Reference

| Zone | Label | Trigger | Status |
|---|---|---|---|
| U | Undefined | BKM not declared | Operational hold |
| S | Stable | C ≥ C_min; no active MISALIGNMENT | Normal |
| M | Marginal | C approaching C_min; MISALIGNMENT detected | Watch |
| D | Degraded | Multiple MA events; LINEAGE_CHAIN compromised | Restricted |
| X | **OVERREACH** | Boundary violation; fabricated BKM; unauthorized operation | **ILLEGAL — Immediate DRIFT_GATE** |

---

### Mode Quick-Reference

| Mode | Label | State | Status |
|---|---|---|---|
| 1 | Detection | CORRIDOR trace initiated | Normal |
| 2 | Structural | CAPTURE_TEMPLATE active | Normal |
| 3 | Integration | Cross-domain links; SMI active | Normal |
| 4 | Emission | RIAP ready for release | Normal |
| 5 | **OVERREACH** | Scope violation or lineage fabrication | **ILLEGAL** |

---

### Key Disambiguations

| RTT/Inside Term | Is NOT | Other Module | Key Distinction |
|---|---|---|---|
| BKM | SNR | RTT/1 | BKM = domain application lens; SNR = structural resonance triad |
| CORRIDOR | TIF | RTT/3 | CORRIDOR = coherence pathway between nodes; TIF = unified structural emission field |
| CAPTURE_TEMPLATE | RTT2_DETECTION_PACKET | RTT/2 | CT = domain application record; RTT2_DETECTION_PACKET = upstream pipeline output |
| ALIGNMENT_PATTERN | CRE | RTT/3 | UAP = domain evaluation reference; CRE = collapse-restore mechanism |
| MISALIGNMENT | CRE | RTT/3 | MA = K–M deviation event; CRE = structural collapse restoration |
| OPERATOR_HOOK | FFF | RTT/3 | OH = external binding interface; FFF = structural emission projector |
| DRIFT_GATE | CRM | RTT/2 | DG = halt interrupt; CRM = drift detection and partial restoration |
| LINEAGE_CHAIN | CSL | RTT/3 | LC = provenance record; CSL = emission continuity-stability loop |
| Zone X (OVERREACH) | Zone X (Inversion) | RTT/3 | Locally defined per module; do not import across boundaries |
| Zone X (OVERREACH) | Zone X (Overflow) | RTT/12 | Locally defined per module; do not import across boundaries |
| Zone X (OVERREACH) | Zone X (Silence Breach) | The_Inverted_Star | Locally defined per module; do not import across boundaries |
| Mode 5 (OVERREACH) | Mode 5 (Inversion) | RTT/3 | Locally defined per module; do not import across boundaries |
| Mode 5 (OVERREACH) | Mode 5 (Overflow) | RTT/12 | Locally defined per module; do not import across boundaries |

---

### Inheritance Chain

| Module | Key Symbols Inherited | Used In |
|---|---|---|
| RTT/micro_core | MRT_MICRO_PACKET, foundational packet schema | RIAP ancestry |
| RTT/1 | SNR, τ, C, C_min, DCO_n | CORRIDOR coherence; DRIFT_GATE thresholds |
| RTT/2 | CPV, FGT, CRM, D(t), D_max, MODE, ZONE, RTT2_DETECTION_PACKET | DRIFT_GATE triggers; mode/zone vocabulary |
| RTT/3 | TIF, FFF, CRE, CSL, CET, RTT3_INTEGRATION_EMISSION_PACKET | Upstream packet option; disambiguated constructs |

---

### Submodule Registry

RTT/Inside contains 19 submodules. All submodules operate within the RTT/Inside construct space
and are governed by the same BKM, CORRIDOR, CAPTURE_TEMPLATE, and DRIFT_GATE rules.

| Submodule | Primary Binding |
|---|---|
| API | OPERATOR_HOOK (semantic hook) |
| Autonomous_Forms | CAPTURE_TEMPLATE |
| Benchmarks | ALIGNMENT_PATTERN / SMI |
| Cisco | OPERATOR_HOOK (operator hook + grid reference) |
| Coal | BKM / Infrastructure domain |
| Corridor_Studio | CORRIDOR |
| Drift | DRIFT_GATE |
| Earth_Sims | BKM / Environment domain |
| Electron_Microscopes | BKM / Science & Research domain |
| Enterprise | CAPTURE_TEMPLATE / Economy domain |
| Examples | Class F — pedagogical CAPTURE_TEMPLATEs |
| Finance | BKM / Economy domain |
| Global | Cross-domain CORRIDOR |
| Internet2 | OPERATOR_HOOK (semantic hook + grid reference) |
| Mesh_Node | CORRIDOR / cross-domain |
| Python | OPERATOR_HOOK (semantic hook) |
| Robofish | BKM / Environment domain |
| qCompute | BKM / Technology domain |
| Game_Developers | Class F — pedagogical examples |

---

## Footer

| Field | Value |
|---|---|
| **Module** | RTT/Inside — Cross-Domain Application Layer |
| **File** | `/docs/rtt/Inside/GLOSSARY.md` |
| **Category** | Core RTT Spine |
| **Version** | 2026.05 |
| **Maintainer** | umaywant2 |
| **Last Updated** | 2026-07-10 |
| **Status** | Canonical — single source of truth for all RTT/Inside term definitions |
| **Upstream glossaries** | RTT/micro_core · RTT/1 · RTT/2 · RTT/3 · RTT/12 |
| **Sibling files** | AGENTS.md · ABOUT.md |
