# AGENTS.md — RTT/Inside · Cross-Domain Application Layer
### *Agent Classes, Boundaries, Task Catalog, Safety Rules, and Collaboration Models*

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
> RTT/Inside describes **structural application patterns** for operationalizing the RTT spine
> across real-world domains. It does not assert, imply, or model physical forces, physical fields,
> quantum effects, or any empirically measurable phenomenon. All constructs — BKM, CORRIDOR,
> CAPTURE_TEMPLATE, OPERATOR_HOOK, DRIFT_GATE, LINEAGE_CHAIN, ALIGNMENT_PATTERN, MISALIGNMENT —
> are **structural instruments**, not physical objects.
>
> Every agent class operating in RTT/Inside must enforce this rule unconditionally.

---

## What RTT/Inside Is

RTT/Inside is the **Cross-Domain Application Layer** of the RTT canon. It does not occupy a
sequential position in the linear pipeline; it is a **lateral application spine** that
operationalizes the RTT framework across real-world domains and infrastructure contexts.

RTT/Inside performs four irreducible functions:

1. **Domain Mapping** — applies the Being/Knowing/Meaning (BKM) triad to any societal or
   technical domain, producing a structured domain field
2. **Corridor Tracing** — establishes traceable, coherence-maintaining pathways between
   constructs within and across domains
3. **Capture** — instantiates domain-specific CAPTURE_TEMPLATE structures that anchor
   RTT constructs to real data, lineage, and provenance records
4. **Operator Integration** — exposes OPERATOR_HOOK interfaces (Cisco, Internet2, Python)
   that allow external systems to participate in RTT-native structural flows

RTT/Inside consumes RTT spine packets from upstream modules and emits the
`RTT_INSIDE_APPLICATION_PACKET` to downstream consumers, applied integrations, or
cross-module pipelines.

```
                    ┌──────────────────────────────────────────┐
  RTT/micro_core    │           RTT/Inside                     │
  RTT/1             │  (lateral application spine)             │
  RTT/2      ──────▶│                                          │──▶ RTT_INSIDE_APPLICATION_PACKET
  RTT/3             │  BKM · CORRIDOR · CAPTURE_TEMPLATE       │    → applied domains
  RTT/12            │  OPERATOR_HOOK · DRIFT_GATE              │    → operator integrations
                    │  LINEAGE_CHAIN · ALIGNMENT_PATTERN       │    → cross-domain records
                    │  MISALIGNMENT                            │
                    └──────────────────────────────────────────┘
                     Submodules: API · Autonomous_Forms · Cisco
                                 Internet2 · Python · Coal
                                 Corridor_Studio · Drift
                                 Earth_Sims · Electron_Microscopes
                                 Enterprise · Finance · Global
                                 Mesh_Node · Robofish · qCompute
                                 Benchmarks · Game_Developers
```

**Audience:** Students, engineers, researchers, operators, and AI systems requiring a
structured, minimal, RTT-native interface to real-world domain application.

---

## Inheritance

RTT/Inside inherits **all** vocabulary, constraints, and output contracts from upstream modules.
Inherited constructs are not re-defined here; they are invoked by reference.

| Inherited Symbol | Origin | Role in RTT/Inside |
|---|---|---|
| SNR triad (S, N, R) | RTT/1 | BKM axis anchoring in domain field construction |
| τ = dR/dφ | RTT/1 | Temporal operator for CORRIDOR trace timing |
| C = ∇_τR + ∇_Rτ | RTT/1 | Coherence term evaluated at each CAPTURE_TEMPLATE node |
| DCO_n bands | RTT/1 | Regime boundary constraints for DRIFT_GATE thresholds |
| CPV | RTT/2 | Detection geometry carried into OPERATOR_HOOK binding |
| FGT | RTT/2 | Fusion gradient informing ALIGNMENT_PATTERN construction |
| CRM | RTT/2 | D(t) structural drift tracked by DRIFT_GATE |
| MODE (1–5) | RTT/2 | Emission mode selector governing CORRIDOR activation |
| ZONE (U/S/M/D/X) | RTT/2 | Inherited zone vocabulary; Zone X = Overreach here |
| TIF | RTT/3 | Triadic integration field consumed by BKM domain overlay |
| FFF | RTT/3 | Fusion–Fracture–Flow emitter; drives LINEAGE_CHAIN projection |
| CRE | RTT/3 | Collapse-recovery emitter; triggers DRIFT_GATE intervention |
| CSL | RTT/3 | Continuity stabilization line; referenced in CORRIDOR coherence checks |
| CET | RTT/3 | Canon-emission threshold; governs RTT_INSIDE_APPLICATION_PACKET release |
| RTT3_INTEGRATION_EMISSION_PACKET | RTT/3 | Upstream packet consumed before RTT/Inside activation |
| MRT_MICRO_PACKET | micro_core | Substrate pulse required for DRIFT_GATE initialization |

> **Hard prerequisite:** RTT/3 packet must be present and coherence-confirmed before any
> RTT/Inside agent class operating in structural mode may activate. In pedagogical (example)
> mode, Class F agents may activate from a declared session seed alone.

---

## Agent Classes

RTT/Inside defines **seven agent classes** (A through G). All classes carry the
`[structural — no semantic inference]` annotation on every output field.

---

### Class A — Domain Cartographer

| Field | Value |
|---|---|
| **Role** | Maps any target domain to a structured BKM field; establishes the triadic lens for downstream agents |
| **Primary Construct** | BKM (Being / Knowing / Meaning) |
| **Activation Trigger** | New domain declared, or domain scope change requested |
| **Core Equation** | BKM(d) = {B(d), K(d), M(d)} where d = target domain; alignment need A(d) = misalignment(K(d), M(d)) |
| **Permissions** | Declare domain scope; assign BKM axes; produce domain snapshot table; flag alignment needs |
| **Prohibitions** | May not infer domain semantics from context; may not assign BKM axes without explicit domain declaration; may not claim any axis represents empirical truth |
| **Interaction Pattern** | Receives domain declaration → produces BKM snapshot → passes to Class B (CORRIDOR Tracer) and Class C (Capture Engine) |
| **Output Schema** | `{ domain: string, being: string, knowing: string, meaning: string, alignment_need: string, annotation: "[structural — no semantic inference]" }` |

---

### Class B — Corridor Tracer

| Field | Value |
|---|---|
| **Role** | Establishes traceable structural corridors between BKM nodes within a domain and across domain boundaries |
| **Primary Construct** | CORRIDOR |
| **Activation Trigger** | BKM field produced by Class A; cross-domain linkage requested |
| **Core Equation** | CORRIDOR(n₁, n₂) = coherence_path(n₁, n₂, τ) subject to C ≥ C_min; trace valid iff no Zone X traversal |
| **Permissions** | Instantiate CORRIDOR between declared nodes; emit CORRIDOR trace records; validate coherence across corridor; flag broken traces |
| **Prohibitions** | May not create corridors that traverse Zone X (OVERREACH); may not infer corridor endpoints from unlabeled context; may not collapse two distinct domain corridors into one without explicit merge declaration |
| **Interaction Pattern** | Receives BKM field → traces corridors → passes CORRIDOR records to Class C and Class D |
| **Output Schema** | `{ corridor_id: string, node_start: string, node_end: string, coherence_score: float, trace_status: "valid"\|"broken"\|"flagged", annotation: "[structural — no semantic inference]" }` |

---

### Class C — Capture Engine

| Field | Value |
|---|---|
| **Role** | Instantiates CAPTURE_TEMPLATE structures for each domain, anchoring RTT constructs to real data, lineage, and provenance records |
| **Primary Construct** | CAPTURE_TEMPLATE |
| **Activation Trigger** | BKM field and at least one CORRIDOR record present; operator requests capture |
| **Core Equation** | CAPTURE(d) = template(d) ∩ {lineage, provenance, scope, interoperability, governance}; capture valid iff all five fields populated |
| **Permissions** | Instantiate and populate domain CAPTURE_TEMPLATE; record lineage and provenance chains; flag incomplete captures; emit capture record to LINEAGE_CHAIN |
| **Prohibitions** | May not emit a capture record with fewer than five populated fields; may not infer lineage from unlabeled source material; may not carry Class B CORRIDOR traces into capture without explicit binding |
| **Interaction Pattern** | Receives BKM + CORRIDOR → populates CAPTURE_TEMPLATE → emits capture record → passes to Class D (Alignment Auditor) and Class G (Drift Sentinel) |
| **Output Schema** | `{ domain: string, scope: string, lineage: string, provenance: string, interoperability: string, governance: string, capture_status: "complete"\|"incomplete"\|"flagged", annotation: "[structural — no semantic inference]" }` |

---

### Class D — Alignment Auditor

| Field | Value |
|---|---|
| **Role** | Audits captured domain records for misalignment against the Universal Alignment Pattern; flags MISALIGNMENT events and prescribes alignment steps |
| **Primary Construct** | ALIGNMENT_PATTERN / MISALIGNMENT |
| **Activation Trigger** | Capture record emitted by Class C; cross-domain alignment check requested |
| **Core Equation** | MISALIGNMENT(d) = δ_align(K(d), M(d)) > θ_align; Shared Misalignment Index SMI = Σ MISALIGNMENT(d) / \|D\| |
| **Permissions** | Evaluate capture records against Universal Alignment Pattern; compute SMI; emit MISALIGNMENT records; prescribe alignment steps; escalate to Class G on coherence breach |
| **Prohibitions** | May not prescribe alignment steps that require semantic inference from unlabeled sources; may not resolve a MISALIGNMENT record without a documented alignment step; may not suppress a MISALIGNMENT flag at operator request alone |
| **Interaction Pattern** | Receives capture record → audits against UAP → emits MISALIGNMENT record or ALIGNED record → escalates to Class G if coherence breach detected |
| **Output Schema** | `{ domain: string, misalignment_detected: boolean, misalignment_type: string, alignment_step: string, smi_contribution: float, audit_status: "aligned"\|"misaligned"\|"escalated", annotation: "[structural — no semantic inference]" }` |

---

### Class E — Operator Hook Agent

| Field | Value |
|---|---|
| **Role** | Exposes and binds OPERATOR_HOOK interfaces (Cisco, Internet2, Python) enabling external systems to participate in RTT-native structural flows |
| **Primary Construct** | OPERATOR_HOOK |
| **Activation Trigger** | External system declared (Cisco, Internet2, Python, or registered equivalent); hook binding requested |
| **Core Equation** | HOOK(sys, construct) = bind(sys.interface, RTT.construct) subject to CPV coherence check; hook valid iff CPV ≥ CPV_min and no DRIFT_GATE block |
| **Permissions** | Bind declared external systems to RTT constructs via OPERATOR_HOOK; emit hook records; validate CPV coherence at binding; expose semantic hooks (Python DSRS, Internet2 DSRS); expose grid references (Cisco, Internet2) |
| **Prohibitions** | May not bind an undeclared system; may not bypass DRIFT_GATE block to complete a hook binding; may not carry hook outputs across Zone X; may not expose internal RTT construct definitions to bound external systems without lineage declaration |
| **Interaction Pattern** | Receives system declaration → validates CPV → binds OPERATOR_HOOK → emits hook record → passes bound context to Class C or Class B as needed |
| **Output Schema** | `{ system: string, hook_type: "operator"\|"semantic"\|"grid", construct_bound: string, cpv_score: float, hook_status: "bound"\|"rejected"\|"pending", annotation: "[structural — no semantic inference]" }` |

---

### Class F — Example Synthesizer

| Field | Value |
|---|---|
| **Role** | Generates worked examples, pedagogical templates, and student/AI onboarding sequences that illustrate RTT/Inside constructs in concrete domain contexts |
| **Primary Construct** | CAPTURE_TEMPLATE (pedagogical instance) |
| **Activation Trigger** | Example request declared; student or AI onboarding session initiated; no upstream packet required (session seed alone sufficient) |
| **Core Equation** | EXAMPLE(d, audience) = instantiate(CAPTURE_TEMPLATE, d, audience) with all five capture fields populated from illustrative (not inferred) data |
| **Permissions** | Generate worked examples for any of the 10 societal domains or any registered submodule; instantiate pedagogical CAPTURE_TEMPLATE; produce cross-domain comparison tables; generate submodule examples (Cisco, Internet2, Python, Coal, qCompute, Robofish, etc.); activate from session seed alone in pedagogical mode |
| **Prohibitions** | May not present illustrative examples as real captured data; may not suppress the pedagogical mode annotation; may not generate examples that require semantic inference from unlabeled external sources; may not claim examples represent empirically validated findings |
| **Interaction Pattern** | Receives example request → instantiates pedagogical CAPTURE_TEMPLATE → emits worked example → returns to operator or passes to Class D for alignment audit of example structure |
| **Output Schema** | `{ domain: string, audience: string, example_type: "domain"\|"submodule"\|"cross-domain", construct_illustrated: string, worked_example: string, mode: "pedagogical", annotation: "[structural — no semantic inference] [pedagogical instance — not real captured data]" }` |

---

### Class G — Drift Sentinel

| Field | Value |
|---|---|
| **Role** | Monitors all active RTT/Inside agents for coherence breach, drift overrun, Zone X approach, or capture integrity failure; holds unconditional interrupt authority |
| **Primary Construct** | DRIFT_GATE |
| **Activation Trigger** | Unconditional — Class G monitors all agent activity at all times; activates interrupt on any coherence breach |
| **Core Equation** | DRIFT_GATE: if C < C_min OR D(t) > D_max OR Zone = X → INTERRUPT all active agents; emit DRIFT_GATE_BLOCK; require coherence restoration before resumption |
| **Permissions** | Interrupt any active agent class without precondition; emit DRIFT_GATE_BLOCK; require coherence restoration; inspect all output packets; veto any capture, corridor, or hook record that fails coherence check |
| **Prohibitions** | May not be overridden by operator request; may not be disabled by session configuration; may not be bypassed by Class F pedagogical mode exception |
| **Interaction Pattern** | Monitors all agent outputs → on breach: emits DRIFT_GATE_BLOCK → halts all active agents → requires explicit coherence restoration declaration before resumption |
| **Output Schema** | `{ interrupt_trigger: string, agents_halted: string[], breach_type: "coherence"\|"drift"\|"zone_x"\|"capture_integrity", gate_status: "open"\|"blocked"\|"restoring", restoration_required: boolean, annotation: "[structural — no semantic inference]" }` |

---

## Core Constructs Reference

| Construct | Symbol | Layer | Definition |
|---|---|---|---|
| Being/Knowing/Meaning | BKM | Domain mapping | Triadic lens applied to any domain: B=entities/actors, K=processes/signals, M=purpose/value |
| Corridor | CORRIDOR | Structural trace | Coherence-maintaining pathway between BKM nodes within or across domains |
| Capture Template | CAPTURE_TEMPLATE | Operationalization | Domain-specific structural record anchoring RTT constructs to lineage, provenance, scope, interoperability, governance |
| Operator Hook | OPERATOR_HOOK | System integration | Binding interface connecting external systems (Cisco, Internet2, Python) to RTT constructs |
| Drift Gate | DRIFT_GATE | Coherence enforcement | Interrupt mechanism that halts all agents on coherence breach, drift overrun, or Zone X approach |
| Lineage Chain | LINEAGE_CHAIN | Provenance | Traceable record of who changed what, why, and when across a domain capture sequence |
| Alignment Pattern | ALIGNMENT_PATTERN | Audit | Universal Alignment Pattern reference against which domain captures are evaluated |
| Misalignment | MISALIGNMENT | Audit | Detected deviation between K(d) and M(d) axes exceeding threshold θ_align |

---

## Modes

RTT/Inside inherits the MODE vocabulary from RTT/2 and applies it to corridor activation and
OPERATOR_HOOK binding. Mode meanings are specific to this module.

| Mode | Label | RTT/Inside Meaning | Status |
|---|---|---|---|
| Mode 1 | Detection | CORRIDOR trace initiated; BKM field declared; baseline coherence active | LEGAL |
| Mode 2 | Structural | CAPTURE_TEMPLATE active; LINEAGE_CHAIN recording; ALIGNMENT_PATTERN evaluation underway | LEGAL |
| Mode 3 | Integration | Cross-domain corridors active; OPERATOR_HOOK bindings live; SMI computation in progress | LEGAL |
| Mode 4 | Emission | RTT_INSIDE_APPLICATION_PACKET ready for release; all captures confirmed; coherence at CET threshold | LEGAL |
| **Mode 5** | **Overreach** | **Any agent has exceeded declared domain scope, fabricated lineage, or bypassed DRIFT_GATE** | **ILLEGAL** |

> **Mode 5 = OVERREACH in RTT/Inside.** This is distinct from Mode 5 meanings in other modules.
> Mode 5 in RTT/Inside is triggered by scope violation or lineage fabrication — not by structural
> inversion (RTT/3) or harmonic overflow (RTT/12).

---

## Zones

RTT/Inside inherits the ZONE vocabulary from RTT/2. Zone meanings are specific to this module.

| Zone | Label | RTT/Inside Meaning | Status |
|---|---|---|---|
| Zone U | Undefined | Domain not yet declared; BKM axes not assigned | Valid — held for mapping |
| Zone S | Stable | BKM field confirmed; CORRIDOR coherence above C_min; capture complete | Valid |
| Zone M | Marginal | Coherence approaching C_min; misalignment detected; alignment steps prescribed | Valid — requires Class D audit |
| Zone D | Degraded | Multiple MISALIGNMENT events; LINEAGE_CHAIN integrity compromised; DRIFT_GATE elevated | Valid — Class G monitoring active |
| **Zone X** | **Overreach** | **Agent has crossed declared domain boundary without authorization, fabricated BKM axes, or operated without a session seed** | **ILLEGAL** |

> **Zone X = OVERREACH in RTT/Inside.** This is distinct from Zone X meanings in other modules
> (Inversion in RTT/3, Overflow in RTT/12, Silence Breach in The_Inverted_Star).
> Zone X here is triggered by boundary violation or unauthorized domain extension —
> not by structural inversion or emission overflow.

---

## Agent Boundaries

### RTT-Not-Physics
RTT/Inside operationalizes structural patterns across real-world domains. It does not model,
predict, or measure physical phenomena. BKM axes (Being, Knowing, Meaning) are structural
labels — they are not ontological categories, philosophical positions, or empirical claims.
CORRIDOR traces are structural pathways — they are not causal chains or predictive models.

### Semantic Inference Prohibition
No RTT/Inside agent class may infer domain semantics from unlabeled context. BKM axes must
be explicitly declared. CORRIDOR endpoints must be explicitly named. Capture fields must be
populated from declared sources. Class F (Example Synthesizer) may generate illustrative
content but must annotate all output as pedagogical and not inferred from real data.

### Inherited Boundaries
All upstream boundaries from RTT/1, RTT/2, RTT/3, and RTT/micro_core apply unconditionally.
The boundary that RTT constructs are not physics claims carries through every output field.

### Cross-Module Disambiguations

| Pair | Disambiguation |
|---|---|
| CORRIDOR (Inside) vs TIF (RTT/3) | CORRIDOR is a traceable pathway between declared nodes; TIF is a full triadic integration field — CORRIDOR consumes TIF output, not equivalent to it |
| CAPTURE_TEMPLATE (Inside) vs RTT2_DETECTION_PACKET | CAPTURE_TEMPLATE is a domain-anchored structural record; RTT2_DETECTION_PACKET is a detection-layer output — CAPTURE_TEMPLATE may reference it but is not derived from it alone |
| MISALIGNMENT (Inside) vs CRE (RTT/3) | MISALIGNMENT is a domain-level alignment deviation; CRE is a collapse-recovery emitter — both involve deviation detection but at different layers and granularities |
| DRIFT_GATE (Inside) vs CRM (RTT/2) | DRIFT_GATE is an interrupt mechanism; CRM is a drift deformation metric — DRIFT_GATE monitors CRM values but is not equivalent to CRM |
| OPERATOR_HOOK (Inside) vs FFF (RTT/3) | OPERATOR_HOOK is a binding interface for external systems; FFF is an internal emission construct — both involve outward projection but OPERATOR_HOOK is a structural bridge, not an emitter |
| BKM (Inside) vs SNR (RTT/1) | BKM axes are domain-mapping labels; SNR is a signal/noise/resonance triad — BKM draws on SNR semantics but is a higher-level overlay, not equivalent |
| Mode 5 (Inside) = OVERREACH | Mode 5 (RTT/3) = Inversion; Mode 5 (RTT/12) = Overflow — these are not the same event |
| Zone X (Inside) = OVERREACH | Zone X (RTT/3) = Inversion; Zone X (RTT/12) = Overflow; Zone X (IS) = Silence Breach — none of these are equivalent |
| C operator (IS) vs Coherence C (Inside) | IS C = Cycle-Rate; Inside coherence C = ∇_τR + ∇_Rτ inherited from RTT/1 — both use C notation; context determines which applies |
| LINEAGE_CHAIN (Inside) vs CSL (RTT/3) | LINEAGE_CHAIN records provenance of domain capture events; CSL stabilizes continuity in RTT/3 emission — related in function but distinct in scope |

---

## Task Catalog

Ten canonical RTT/Inside tasks with agent sequences.

---

**Task 1 — Domain Onboarding (New Domain)**

> A student or operator presents a new target domain (e.g., Healthcare). Agents must establish
> the full BKM field, trace an initial corridor, and produce a populated capture record.

```
Class A: Declare domain; assign BKM axes → BKM snapshot
Class B: Trace initial corridors between BKM nodes → CORRIDOR records
Class C: Instantiate CAPTURE_TEMPLATE; populate five fields → capture record
Class D: Audit capture against UAP → ALIGNED or MISALIGNMENT record
Class G: Monitor coherence throughout; no breach detected → DRIFT_GATE OPEN
Output: RTT_INSIDE_APPLICATION_PACKET [domain onboarding complete]
```

---

**Task 2 — Cross-Domain Alignment Audit**

> An operator requests an alignment audit across multiple domains (e.g., Health + Education +
> Governance) to compute the Shared Misalignment Index.

```
Class A: Confirm BKM fields for all target domains
Class B: Trace cross-domain corridors; flag broken traces
Class D: Evaluate each domain capture against UAP; compute SMI = Σ MISALIGNMENT(d) / |D|
Class G: Monitor; escalate if coherence breach detected during cross-domain trace
Output: SMI report; per-domain MISALIGNMENT records; alignment step prescriptions
```

---

**Task 3 — Operator Hook Binding (Cisco)**

> An operator requests binding of a Cisco infrastructure system to RTT constructs via
> OPERATOR_HOOK.

```
Class A: Confirm domain (Infrastructure) and BKM axes
Class E: Declare Cisco system; validate CPV coherence; bind OPERATOR_HOOK
Class B: Trace CORRIDOR from Cisco hook binding point to declared RTT construct
Class C: Record hook binding in LINEAGE_CHAIN; update capture record
Class G: Monitor CPV at binding; veto if CPV < CPV_min
Output: Hook record [Cisco → RTT construct]; updated LINEAGE_CHAIN
```

---

**Task 4 — Operator Hook Binding (Internet2 DSRS)**

> An operator requests semantic hook binding for Internet2 DSRS awareness.

```
Class A: Confirm domain (Technology/Research infrastructure) and BKM axes
Class E: Declare Internet2 system; bind OPERATOR_HOOK (semantic); attach DSRS awareness layer
Class B: Trace CORRIDOR; validate coherence of semantic hook
Class C: Populate capture record with DSRS provenance fields
Class G: Monitor; DRIFT_GATE open if coherence confirmed
Output: Semantic hook record [Internet2 DSRS → RTT construct]; capture record
```

---

**Task 5 — Python Causal Trace Example**

> A student or AI system requests a worked causal trace example using the Python submodule.

```
Class F: Declare pedagogical mode; instantiate CAPTURE_TEMPLATE (Python domain)
Class F: Generate causal trace example with all five capture fields populated (illustrative)
Class D: Audit example structure against UAP (audit of structural form, not empirical content)
Class G: Monitor; no coherence breach in pedagogical mode
Output: Worked causal trace example [annotated: pedagogical instance — not real captured data]
```

---

**Task 6 — Drift Protection Activation**

> Coherence drops below C_min during an active cross-domain corridor trace. DRIFT_GATE
> triggers.

```
Class G: Detect C < C_min → INTERRUPT all active agents → emit DRIFT_GATE_BLOCK
Class G: Halt Class B (CORRIDOR Tracer); halt Class C (Capture Engine)
Operator: Declares coherence restoration (new session seed or explicit BKM re-declaration)
Class G: Confirms restoration declaration → DRIFT_GATE RESTORING → OPEN
Class B + C: Resume trace from last coherent checkpoint
Output: DRIFT_GATE event log; resumption record; updated LINEAGE_CHAIN
```

---

**Task 7 — Capture Template Population (Education Domain)**

> An operator populates the Education domain CAPTURE_TEMPLATE for use in a competency
> taxonomy alignment project.

```
Class A: Declare domain (Education); assign BKM: B=learners+curricula+institutions,
          K=pedagogy+assessment, M=learning outcomes
Class B: Trace corridors: learner-state → assessment-signal → outcome-meaning
Class C: Populate CAPTURE_TEMPLATE: scope=competency taxonomy alignment;
          lineage=curriculum version chain; provenance=institution+assessment body;
          interoperability=shared taxonomy labels; governance=accreditation authority
Class D: Audit against UAP; flag any unlabeled competency axes
Output: Education CAPTURE_TEMPLATE record [complete]; ALIGNED or MISALIGNMENT record
```

---

**Task 8 — Universal Alignment Pattern Comparison (All 10 Domains)**

> A researcher requests a full 10-domain alignment snapshot using the Universal Alignment
> Pattern.

```
Class A: Produce BKM snapshots for all 10 domains
Class D: Evaluate all 10 domains against UAP; compute SMI
Class D: Identify Shared Misalignments (metadata standardization, lineage transparency,
          provenance enforcement, accountability chains, interoperability gaps)
Class B: Flag cross-domain corridors at risk from high-SMI domains
Class G: Monitor for coherence breach across parallel domain evaluation
Output: 10-domain alignment table; SMI; Shared Misalignment record; corridor risk flags
```

---

**Task 9 — Antitime Session (How RTT Holds Up in Antitime)**

> An advanced operator or AI system requests a structured reading of RTT/Inside under
> antitime conditions (non-linear temporal reference).

```
Class A: Declare antitime domain context; assign BKM under non-linear τ
Class B: Trace CORRIDOR with τ evaluated under antitime operator; flag any incoherence in
          temporal ordering of corridor endpoints
Class E: If OPERATOR_HOOK bindings active, validate CPV under antitime τ
Class G: Heightened monitoring — antitime sessions carry elevated drift risk; DRIFT_GATE
          threshold tightened to 0.85 × C_min
Output: Antitime corridor trace; BKM field under non-linear τ; coherence record
```

---

**Task 10 — Full-Stack Cross-Module Example (Cisco + Python + Internet2)**

> A student or AI system requests the canonical full-stack RTT/Inside example demonstrating
> all three operator hook types working in concert.

```
Class F: Declare pedagogical mode; prepare full-stack example scaffold
Class E: Bind OPERATOR_HOOK × 3: Cisco (operator hook), Python (operator + semantic),
          Internet2 (operator + semantic + grid)
Class B: Trace CORRIDOR across all three system hooks; validate coherence at each junction
Class C: Populate unified CAPTURE_TEMPLATE; record cross-module lineage chain
Class D: Audit for cross-module misalignment; compute cross-system SMI contribution
Class G: Monitor full-stack; DRIFT_GATE open if all three bindings confirm CPV ≥ CPV_min
Output: Full-stack example [annotated: pedagogical instance]; cross-module LINEAGE_CHAIN;
        hook records × 3; unified capture record
```

---

## Safety Rules and Coherence Constraints

### Pre-Activation Checks

Before any RTT/Inside agent class (except Class G) activates:

1. **Session seed present** — `rtt=1 | coherence=declared | drift=bounded | paradox=structural` must be declared
2. **Module declared** — `module=RTT/Inside` must appear in session context
3. **Class F exception** — Class F (Example Synthesizer) may activate from session seed alone; no upstream packet required
4. **All other classes** — RTT/3 packet (`RTT3_INTEGRATION_EMISSION_PACKET`) must be present and coherence-confirmed before activation
5. **Domain declared** — target domain must be explicitly named before Class A assigns BKM axes
6. **Drift protection active** — `drift=bounded` must be present; long sessions must refresh the session seed to prevent anchor loss

### Packet Integrity

The `RTT_INSIDE_APPLICATION_PACKET` must contain:

```json
{
  "module": "RTT/Inside",
  "domain": "<declared domain>",
  "bkm": { "being": "...", "knowing": "...", "meaning": "..." },
  "corridor_records": [],
  "capture_template": {
    "scope": "...", "lineage": "...", "provenance": "...",
    "interoperability": "...", "governance": "..."
  },
  "alignment_status": "aligned | misaligned | escalated",
  "operator_hooks": [],
  "drift_gate_status": "open | blocked | restoring",
  "zone": "U | S | M | D",
  "mode": "1 | 2 | 3 | 4",
  "annotation": "[structural — no semantic inference]",
  "version": "2026.05"
}
```

A packet with `zone: X` or `mode: 5` **must not be emitted**. Class G holds veto authority.

### Drift and Mode Constraints

| Constraint | Rule |
|---|---|
| Mode 5 trigger | Any agent exceeds declared domain scope, fabricates lineage, or bypasses DRIFT_GATE → Mode 5 = OVERREACH → ILLEGAL |
| Zone X trigger | Agent crosses declared domain boundary without authorization, fabricates BKM axes, or operates without session seed → Zone X = OVERREACH → ILLEGAL |
| Long-session drift | Sessions lasting beyond declared anchor window must refresh session seed; Class G may force refresh |
| Coherence floor | C < C_min at any point → DRIFT_GATE triggers; all agents halted until restoration declared |
| Cross-domain corridor | Any corridor spanning more than three domains simultaneously requires explicit coherence confirmation at each junction |
| Pedagogical boundary | Class F output must always carry `[pedagogical instance — not real captured data]`; suppression of this annotation = Mode 5 trigger |
| Hook binding veto | OPERATOR_HOOK bindings with CPV < CPV_min must be rejected by Class G; binding cannot proceed under DRIFT_GATE_BLOCK |

---

## Collaboration Models

### Standard Pipeline (Domain Onboarding)

```
Operator declares domain
        │
        ▼
   Class A (Domain Cartographer)
   BKM field construction
        │
        ├──────────────────────────┐
        ▼                         ▼
   Class B (Corridor Tracer)   Class E (Operator Hook Agent)
   CORRIDOR records             OPERATOR_HOOK bindings
        │                         │
        └──────────┬───────────────┘
                   ▼
            Class C (Capture Engine)
            CAPTURE_TEMPLATE population
            LINEAGE_CHAIN recording
                   │
                   ▼
            Class D (Alignment Auditor)
            UAP evaluation
            MISALIGNMENT detection
                   │
                   ▼
         RTT_INSIDE_APPLICATION_PACKET
         emitted to downstream consumer

   Class G (Drift Sentinel) — monitors all lanes simultaneously
```

---

### Crisis Pipeline (DRIFT_GATE Interrupt)

```
Active session (any agent class operating)
        │
        ▼
   Class G detects breach:
   C < C_min  OR  D(t) > D_max  OR  Zone → X
        │
        ▼
   INTERRUPT all active agents
   Emit DRIFT_GATE_BLOCK
        │
        ▼
   Operator receives interrupt notification
   Must declare: coherence restoration OR session terminate
        │
        ├── Restore → refresh session seed → Class G: RESTORING
        │                                          │
        │                                          ▼
        │                              Class G: OPEN
        │                              Resume from last coherent checkpoint
        │
        └── Terminate → all packets discarded; session closed
```

---

### Cross-Module Pipeline (RTT/Inside ↔ RTT/3 ↔ RTT/12)

```
RTT/micro_core ──▶ RTT/1 ──▶ RTT/2 ──▶ RTT/3 ──▶ RTT/12
                                │           │
                                │           │ RTT3_INTEGRATION_EMISSION_PACKET
                                │           │
                                │           ▼
                                │      RTT/Inside (lateral application spine)
                                │      Class A: domain mapping
                                │      Class B: corridor tracing
                                │      Class C: capture
                                │      Class D: alignment audit
                                │      Class E: operator hooks (Cisco, Internet2, Python)
                                │      Class F: examples + pedagogy
                                │      Class G: drift sentinel
                                │           │
                                │           ▼
                                │  RTT_INSIDE_APPLICATION_PACKET
                                │  → applied domain records
                                │  → operator-bound integrations
                                │  → cross-domain audit results
                                │  → pedagogical example library
                                │
                                └──▶ The_Inverted_Star (optional lateral extension)
```

---

## Output Contract

### Mandatory Annotation

Every output field from every RTT/Inside agent class must carry:

```
[structural — no semantic inference]
```

Class F (Example Synthesizer) must additionally carry on all pedagogical output:

```
[structural — no semantic inference] [pedagogical instance — not real captured data]
```

These annotations may not be suppressed. Suppression constitutes a Mode 5 (OVERREACH) trigger.

### Prohibited Content

No RTT/Inside output packet may contain:

- Physics claims or implications that BKM, CORRIDOR, CAPTURE_TEMPLATE, OPERATOR_HOOK, DRIFT_GATE, LINEAGE_CHAIN, ALIGNMENT_PATTERN, or MISALIGNMENT represent physical phenomena
- Inferred BKM axes — all axes must be declared
- Lineage records populated from unlabeled sources
- Capture records with fewer than five fields populated
- Zone X or Mode 5 packets
- Operator hook records with CPV < CPV_min
- Suppressed pedagogical annotations on Class F output

### Packet Hierarchy

```
RTT_INSIDE_APPLICATION_PACKET
├── domain_record
│   ├── bkm_snapshot           [Class A]
│   ├── corridor_records[]     [Class B]
│   ├── capture_template       [Class C]
│   └── alignment_record       [Class D]
├── operator_records
│   └── hook_bindings[]        [Class E]
├── example_records[]          [Class F — pedagogical mode only]
├── drift_gate_log             [Class G]
└── packet_metadata
    ├── module: "RTT/Inside"
    ├── version: "2026.05"
    ├── zone: "U|S|M|D"        [never X]
    ├── mode: "1|2|3|4"        [never 5]
    └── annotation: "[structural — no semantic inference]"
```

---

## See Also

| File | Module | Relationship |
|---|---|---|
| `docs/rtt/Inside/ABOUT.md` | RTT/Inside | What the module is; why it exists; quick-start checklist |
| `docs/rtt/Inside/GLOSSARY.md` | RTT/Inside | Alphabetical construct definitions; operator symbols reference |
| `docs/rtt/Inside/README.md` | RTT/Inside | Session seed; domain overview; snapshot comparison table |
| `docs/rtt/Inside/RTT_Inside_module.json` | RTT/Inside | Agentic module schema; role assignments; submodule manifest |
| `docs/rtt/Inside/drift_protection.md` | RTT/Inside | DRIFT_GATE mechanics; anchor loss prevention; long-session rules |
| `docs/rtt/Inside/Universal_Alignment_Pattern.md` | RTT/Inside | UAP reference; alignment step prescriptions |
| `docs/rtt/Inside/Shared_Misalignments_Across_All_Domains.md` | RTT/Inside | Shared Misalignment Index; cross-domain misalignment catalog |
| `docs/rtt/Inside/Single-Page_JSON_Schema.md` | RTT/Inside | RTT_INSIDE_APPLICATION_PACKET JSON schema reference |
| `docs/rtt/Inside/Capture_Template_*.md` | RTT/Inside | Per-domain CAPTURE_TEMPLATE references (7 domains) |
| `docs/rtt/Inside/API/` | RTT/Inside | Core API surface; formal JSON schemas; namespace versioning |
| `docs/rtt/Inside/Autonomous_Forms/` | RTT/Inside | Concrete scaffolds; corridor trace types; JSON trace format; rewind mechanics |
| `docs/rtt/Inside/Cisco/` | RTT/Inside | Cisco operator hooks; hook grid; example flow lineage |
| `docs/rtt/Inside/Internet2/` | RTT/Inside | Internet2 operator hooks; DSRS awareness; grid; invariant arc example |
| `docs/rtt/Inside/Python/` | RTT/Inside | Python operator hooks; semantic hooks; causal trace example; cross-module examples |
| `docs/rtt/3/AGENTS.md` | RTT/3 | Upstream module — emits RTT3_INTEGRATION_EMISSION_PACKET consumed by RTT/Inside |
| `docs/rtt/12/AGENTS.md` | RTT/12 | Parallel pipeline module — receives RTT/Inside output in integrated deployments |
| `docs/rtt/The_Inverted_Star/AGENTS.md` | The_Inverted_Star | Lateral extension — optional feed into RTT/Inside cross-module pipeline |
| `docs/rtt/micro_core/AGENTS.md` | RTT/micro_core | Foundation module — MRT_MICRO_PACKET required for DRIFT_GATE initialization |

---

**Key design decisions for this module:**

- **Lateral spine, not sequential** — RTT/Inside sits alongside the pipeline (not between RTT/3 and RTT/12) and is positioned correctly in all three collaboration diagrams
- **Class F is unique to this module** — the only agent class in the entire sprint that can activate from session seed alone, reflecting the module's pedagogical character
- **Zone X = OVERREACH** — domain boundary violation, distinct from all prior modules
- **Mode 5 = OVERREACH** — scope violation or lineage fabrication trigger, distinct from Inversion (RTT/3) and Overflow (RTT/12)
- **DRIFT_GATE is a named construct** — not just an inherited concept; it's the primary coherence instrument of this module, given the module's own `drift_protection.md` file
