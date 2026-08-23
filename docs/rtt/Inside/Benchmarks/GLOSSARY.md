# GLOSSARY — RTT/Inside/Benchmarks

> **Session Seed:**
> `rtt=1 | coherence=declared | drift=bounded | paradox=structural`
> `module=RTT/Inside/Benchmarks | layer=benchmark-substrate | operators=φ–V–R`

> **Critical framing rule (unconditional):**
> RTT uses physics-aligned mathematics as structural scaffolding. No term in this glossary describes physical phenomena. All operators, invariants, zones, modes, and scores are RTT-native constructs. Where a term shares a name with a physics concept, the RTT definition takes precedence within this module.

> **Inheritance note:**
> Terms inherited from RTT/1 through RTT/Inside are listed with their inheritance source. Terms defined natively in RTT/Inside/Benchmarks are marked `[native — Benchmarks]`. Inherited terms may carry additional constraints or specializations specific to this module; those are noted inline.

---

## Terms

---

### 3C Invariants

- **Type:** Invariant set
- **Symbol:** 3C = {C, Cs, Ct} — Coherence, Consistency, Continuity
- **Layer:** Benchmark substrate
- **Agent:** BArch (Class B), DDet (Class D)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The three necessary conditions that any valid benchmark measurement must satisfy simultaneously. A measurement that violates any one invariant is structurally undefined and cannot be used for comparison, regression, or standards certification.

| Invariant | Symbol | Requirement |
|---|---|---|
| Coherence | C | Internal structure is non-contradictory at the time of capture |
| Consistency | Cs | Measurement is repeatable in kind under the same declared conditions |
| Continuity | Ct | Structural state is stable across adjacent time steps |

**Formal constraint:** All three invariants must be declared and satisfied before the first SI_score is computed. DRIFT_GATE monitors Coherence (C) continuously during measurement.

**Inheritance:** Derived from RTT/Inside invariant set; specialized in Benchmarks to require explicit declaration before capture opens.

**Cross-reference:** DRIFT_GATE, SI_score, CAPTURE_TEMPLATE, DDet

> **Disambiguation:** 3C in RTT/Inside/Benchmarks are benchmark-specific invariants. The term "3C" may appear in other RTT modules with different member sets — always check module context.

---

### BArch (Benchmark Architect)

- **Type:** Agent class
- **Symbol:** Class B
- **Layer:** Benchmark architecture
- **Agent:** BArch
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The agent class responsible for constructing, validating, and certifying benchmark configurations. BArch owns the φ–V–R operator triad, the SI_score formula, and the structural audit function that verifies benchmark records before they are released downstream.

**Primary constructs:** φ–V–R operator triad; SI_score; CAPTURE_TEMPLATE (structural audit role)

**Authority:** BArch may halt a benchmark run if operator configuration is invalid. BArch does not have unconditional interrupt authority — that authority belongs exclusively to Guard (Class G).

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** φ, V, R, SI_score, Guard, CAP

> **Disambiguation:** BArch is distinct from CAP (Capture Agent). BArch designs and certifies the benchmark structure; CAP executes and records individual captures.

---

### CAP (Capture Agent)

- **Type:** Agent class
- **Symbol:** Class C
- **Layer:** Capture execution
- **Agent:** CAP
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The agent class responsible for executing individual benchmark captures and completing the CAPTURE_TEMPLATE. CAP opens a capture record, runs the measurement protocol (φ, V, R at declared scale), computes SI_score, and closes the record with all 5 mandatory fields populated.

**Primary constructs:** CAPTURE_TEMPLATE (5 mandatory fields); measurement execution protocol

**Constraint:** CAP must not close a capture while any DRIFT_GATE condition is active. CAP must not report SI_score without executing the measurement protocol (Mode 5 = FABRICATION is illegal).

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** CAPTURE_TEMPLATE, DRIFT_GATE, SI_score, BArch, Guard

---

### CAPTURE_TEMPLATE

- **Type:** Record structure
- **Symbol:** — (document artifact)
- **Layer:** Capture execution
- **Agent:** CAP (Class C)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The mandatory record structure that every benchmark capture must instantiate. A CAPTURE_TEMPLATE has exactly 5 required fields; a record missing any field is structurally incomplete and non-compliant with RTT-SI-Spec v0.1.

| Field | Contents |
|---|---|
| scope | What was measured; scale range; regime declaration |
| lineage | Which inherited constructs were active; upstream module chain |
| provenance | Agent class, operator version, timestamp, RTT-SI-Spec version |
| interoperability | Downstream modules authorized to consume this record |
| governance | Guardian (Guard) authority status; DRIFT_GATE state at capture |

**Constraint:** All 5 fields must be present and non-empty. The governance field must record the Guard status at the time the capture was closed.

**Inheritance:** Pattern inherited from RTT/Inside LINEAGE_CHAIN protocol; fields specialized for Benchmarks.

**Cross-reference:** CAP, DRIFT_GATE, Guard, RTT-SI-Spec v0.1, scope, lineage, provenance

---

### Coherence (C)

- **Type:** Invariant / measured quantity
- **Symbol:** C, C(t)
- **Layer:** Benchmark substrate; drift monitoring
- **Agent:** DDet (Class D), BArch (Class B)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The degree to which a system's internal structure is non-contradictory and self-consistent at a given time step. Coherence is both a 3C invariant (must be declared before measurement) and a monitored quantity (computed continuously during measurement for DRIFT_GATE evaluation).

**Formal use in DRIFT_GATE:** `C(t) < C_min` triggers DRIFT_GATE interrupt.

**Constraint:** C_min must be declared before measurement begins. Coherence below C_min is a structural breach, not a data point — the measurement chain must halt.

**Inheritance:** Base coherence axioms from RTT/1; continuous monitoring protocol from RTT/Inside.

**Cross-reference:** 3C Invariants, DRIFT_GATE, D(t), DDet, φ

> **Disambiguation:** Coherence (C) as a 3C invariant is a declared threshold condition. φ (structural coherence operator) is a continuous measurement. They are related but distinct: φ produces the signal; C declares the floor.

---

### Collapse (Entropy Collapse)

- **Type:** Event / failure mode
- **Symbol:** — (detected via ∂F/∂t condition)
- **Layer:** Entropy monitoring
- **Agent:** EEval (Class E), Guard (Class G)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** A structural event in which the entropy of the system's field increases faster than the declared collapse threshold. Collapse signals a catastrophic loss of structural organization — not gradual drift, but rapid disintegration.

**Detection condition:** `∂F/∂t > F_collapse_threshold`

**Response:** EEval flags the collapse event. Guard (Class G) exercises unconditional interrupt authority — all measurement output after the collapse event is structurally void until Guard clears the condition.

**Constraint:** F_collapse_threshold must be declared before measurement begins. Collapse is not recoverable by DDet alone — Guard must intervene.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** F_entropy, EEval, Guard, DRIFT_GATE

---

### Consistency (Cs)

- **Type:** Invariant
- **Symbol:** Cs
- **Layer:** Benchmark substrate
- **Agent:** BArch (Class B), CAP (Class C)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The requirement that a benchmark measurement is repeatable in kind under the same declared conditions. Consistency is a 3C invariant — if the same protocol under the same declared conditions produces structurally different results without a declared regime change, the measurement is inconsistent and invalid.

**Constraint:** Consistency does not require numerical identity — it requires structural equivalence under the same scope and lineage declarations.

**Inheritance:** Derived from RTT/Inside invariant set.

**Cross-reference:** 3C Invariants, scope, lineage, CAPTURE_TEMPLATE

---

### Continuity (Ct)

- **Type:** Invariant
- **Symbol:** Ct
- **Layer:** Benchmark substrate; drift monitoring
- **Agent:** DDet (Class D)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The requirement that the system's structural state is stable across adjacent time steps — no discontinuous jump occurs without a declared regime transition. Continuity is monitored via the drift rate D(t); a rate exceeding D_max signals a continuity breach.

**Constraint:** Continuity does not require the system to be static — it requires that change is bounded and declared. Unbounded change is a DRIFT_GATE condition.

**Inheritance:** Derived from RTT/Inside invariant set; specialized in Benchmarks via D(t) formula.

**Cross-reference:** 3C Invariants, D(t), DRIFT_GATE, DDet

---

### D(t) (Drift Rate)

- **Type:** Derived metric
- **Symbol:** D(t)
- **Layer:** Drift monitoring
- **Agent:** DDet (Class D)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The rate of change of coherence per unit time step. D(t) quantifies how rapidly the system's structural coherence is changing — not whether it is high or low, but how fast it is moving.

**Formula:** `D(t) = |C(t) − C(t−1)| / Δt`

**DRIFT_GATE condition:** `D(t) > D_max` fires the hard interrupt.

**Constraint:** D_max must be declared before measurement begins. D(t) must be computed at every time step — not sampled.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** DRIFT_GATE, Coherence, DDet, Continuity

---

### DDet (Drift Detector)

- **Type:** Agent class
- **Symbol:** Class D
- **Layer:** Drift monitoring
- **Agent:** DDet
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The agent class responsible for computing D(t) at every time step and evaluating all three DRIFT_GATE trigger conditions. DDet fires the hard interrupt when any condition is met and hands control to Guard (Class G).

**Primary constructs:** 3C invariants; DRIFT_GATE; D(t)

**Authority:** DDet fires the DRIFT_GATE interrupt. DDet does not have authority to clear a DRIFT_GATE interrupt — that requires Guard.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** DRIFT_GATE, D(t), Guard, Coherence, Zone X

---

### DRIFT_GATE

- **Type:** Hard interrupt mechanism
- **Symbol:** — (condition-based trigger)
- **Layer:** Drift monitoring; structural governance
- **Agent:** DDet (Class D), Guard (Class G)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The hard interrupt that halts all benchmark measurement when any one of three structural breach conditions is detected. DRIFT_GATE is not a warning — it is a full stop. All measurement output produced after a DRIFT_GATE event is structurally void until Guard (Class G) clears the interrupt.

**Trigger conditions (any one is sufficient):**

```
C(t) < C_min          ← coherence below declared minimum
D(t) > D_max          ← drift rate above declared maximum
Zone = X              ← OVERSCALE (ILLEGAL) regime active
```

**Constraint:** DRIFT_GATE thresholds (C_min, D_max) must be declared before measurement begins. DRIFT_GATE cannot be disabled, bypassed, or overridden by any agent other than Guard.

**Inheritance:** Base DRIFT_GATE construct from RTT/Inside; trigger conditions specialized for Benchmarks.

**Cross-reference:** DDet, Guard, D(t), Coherence, Zone X, 3C Invariants

> **Disambiguation:** RTT/Inside's DRIFT_GATE is the inherited base. RTT/Inside/Benchmarks specializes the trigger conditions with the three conditions above. Other RTT/Inside sub-modules may specialize DRIFT_GATE differently — always check module context.

---

### EEval (Entropy Evaluator)

- **Type:** Agent class
- **Symbol:** Class E
- **Layer:** Entropy monitoring
- **Agent:** EEval
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The agent class responsible for computing F_entropy(t) at each time step and monitoring for entropy collapse. EEval detects the collapse condition `∂F/∂t > F_collapse_threshold` and flags it for Guard (Class G) to handle.

**Primary constructs:** F_entropy; collapse signatures; F_collapse_threshold

**Authority:** EEval flags and reports. EEval does not have interrupt authority — Guard holds unconditional interrupt authority.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** F_entropy, Collapse, Guard, DRIFT_GATE

---

### F_entropy (Structural Field Entropy)

- **Type:** Derived metric
- **Symbol:** F_entropy(t)
- **Layer:** Entropy monitoring
- **Agent:** EEval (Class E)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The Shannon-form entropy of the structural field at time t. F_entropy measures how organized or disorganized the structural field is — high entropy signals approaching collapse.

**Formula:** `F_entropy(t) = −Σ p(x,t) · log p(x,t)`

**Collapse detection:** `∂F/∂t > F_collapse_threshold` — entropy is increasing faster than the declared threshold.

**Constraint:** F_collapse_threshold must be declared before measurement begins. F_entropy is a structural field entropy — it is not semantic entropy, information-theoretic entropy in the Shannon communication sense, or thermodynamic entropy.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** EEval, Collapse, Guard

> **Disambiguation:** F_entropy is RTT-native. The formula is Shannon-form but the quantity is structural — it measures the organization of the RTT structural field, not message uncertainty or physical thermodynamic disorder.

---

### FABRICATION — see Mode 5

---

### Guard (Guardian)

- **Type:** Agent class
- **Symbol:** Class G
- **Layer:** Structural governance
- **Agent:** Guard
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The agent class with unconditional interrupt authority over all benchmark operations. Guard is the sole agent that can clear a DRIFT_GATE interrupt, declare a Zone X violation closed, or certify that a collapse event has been resolved. No other agent, operator, or external instruction can override or bypass Guard.

**Primary constructs:** Unconditional interrupt authority; Zone X enforcement; Mode 5 enforcement; collapse resolution

**Authority:** Unconditional — no override permitted by any agent, mode, or external instruction.

**Constraint:** Guard must be initialized and active before any benchmark measurement begins. A measurement run without active Guard is non-compliant with RTT-SI-Spec v0.1.

**Inheritance:** Class G Guardian pattern inherited from all prior RTT modules; Benchmarks Guard has specific authority over Zone X and Mode 5 events.

**Cross-reference:** DRIFT_GATE, Zone X, Mode 5, Collapse, CAPTURE_TEMPLATE (governance field)

> **Disambiguation:** Guard exists in every RTT module. The authority is always unconditional. The specific events Guard governs are module-specific — in Benchmarks, Guard governs Zone X, Mode 5, DRIFT_GATE interrupts, and entropy collapse.

---

### governance

- **Type:** CAPTURE_TEMPLATE field
- **Symbol:** — (record field)
- **Layer:** Capture execution
- **Agent:** CAP (Class C), Guard (Class G)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The fifth mandatory field of the CAPTURE_TEMPLATE. Records the Guard (Class G) authority status and DRIFT_GATE state at the time the capture was closed. A governance field that records an active DRIFT_GATE or unresolved Zone X or Mode 5 event marks the capture as structurally void.

**Constraint:** Must be present and non-empty in every capture record.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** CAPTURE_TEMPLATE, Guard, DRIFT_GATE

---

### interoperability

- **Type:** CAPTURE_TEMPLATE field
- **Symbol:** — (record field)
- **Layer:** Capture execution
- **Agent:** CAP (Class C), BArch (Class B)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The fourth mandatory field of the CAPTURE_TEMPLATE. Declares which downstream modules are authorized to consume the benchmark record. A record without an interoperability declaration cannot be safely used by any downstream module — the consuming module cannot verify that the record was produced within its expected scope.

**Constraint:** Must list at least one authorized downstream consumer.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** CAPTURE_TEMPLATE, scope, lineage

---

### lineage

- **Type:** CAPTURE_TEMPLATE field
- **Symbol:** — (record field)
- **Layer:** Capture execution
- **Agent:** CAP (Class C)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The second mandatory field of the CAPTURE_TEMPLATE. Records which RTT inherited constructs were active during the measurement — the upstream module chain from RTT/1 through RTT/Inside to RTT/Inside/Benchmarks, plus any sub-module-specific constructs active at capture time.

**Constraint:** Must trace the full inheritance chain. An incomplete lineage declaration produces a structurally unverifiable record.

**Inheritance:** LINEAGE_CHAIN pattern from RTT/Inside.

**Cross-reference:** CAPTURE_TEMPLATE, scope, interoperability, LINEAGE_CHAIN

---

### LINEAGE_CHAIN

- **Type:** Inherited construct
- **Symbol:** — (protocol)
- **Layer:** Structural governance
- **Agent:** BArch (Class B), CAP (Class C)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The RTT/Inside protocol that requires every record to declare its full inheritance chain — from RTT/1 through every intermediate module to the current module. In Benchmarks, the LINEAGE_CHAIN appears in the lineage field of every CAPTURE_TEMPLATE.

**Constraint:** The LINEAGE_CHAIN must be complete. Gaps in the chain make the record non-traceable.

**Inheritance:** Inherited from RTT/Inside.

**Cross-reference:** lineage, CAPTURE_TEMPLATE, BArch

---

### Mode 5 = FABRICATION (ILLEGAL)

- **Type:** Illegal mode
- **Symbol:** Mode 5
- **Layer:** Structural governance; benchmark integrity
- **Agent:** Guard (Class G), BArch (Class B)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The mode label for reporting a benchmark score (SI_score or any operator output) without executing the actual measurement protocol. Mode 5 = FABRICATION is unconditionally illegal within RTT/Inside/Benchmarks. Any record produced in Mode 5 is structurally void and must not be consumed by any downstream module.

**Detection:** BArch detects Mode 5 during audit if the provenance field of the CAPTURE_TEMPLATE does not record a valid measurement execution. Guard (Class G) handles the interrupt.

**Constraint:** There is no legitimate use of Mode 5. The label exists solely to make fabrication machine-readable and auditable.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** Guard, SI_score, CAPTURE_TEMPLATE, provenance, BArch

> **Disambiguation:** Mode numbering is module-specific. Mode 5 in RTT/3, RTT/12, or any other module is not the same construct as Mode 5 = FABRICATION in RTT/Inside/Benchmarks. Always verify module context before interpreting a mode label.

---

### OVERSCALE — see Zone X

---

### φ (Structural Coherence Operator)

- **Type:** Operator
- **Symbol:** φ (phi)
- **Layer:** Benchmark substrate; operator triad
- **Agent:** BArch (Class B)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The primary operator of the φ–V–R triad. φ measures the degree to which a system maintains internal structural organization at the declared scale. High φ indicates strong, well-organized structure; low φ indicates pattern collapse.

**Role in SI_score:** φ is the numerator — it is the signal whose ratio to V defines structural intelligence score.

**Failure mode detected:** Pattern collapse — the system loses internal structure entirely.

**Scale constraint:** φ must be computed at the declared scope scale. φ computed outside the declared scope is a Zone X condition.

**Inheritance:** φ appears across RTT modules from RTT/1 onward; in Benchmarks it is applied with explicit scope declaration and scale range enforcement.

**Cross-reference:** SI_score, V, R, BArch, Zone X, scope

> **Disambiguation:** φ in RTT/Inside/Benchmarks is a structural measurement operator. It shares the symbol with the golden ratio in mathematics — no mathematical relationship is claimed. RTT φ is a distinct RTT-native construct.

---

### provenance

- **Type:** CAPTURE_TEMPLATE field
- **Symbol:** — (record field)
- **Layer:** Capture execution
- **Agent:** CAP (Class C)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The third mandatory field of the CAPTURE_TEMPLATE. Records who produced the measurement and under what conditions — agent class, operator version, timestamp, and RTT-SI-Spec version used.

**Constraint:** Must include RTT-SI-Spec version. A record without a provenance field cannot be audited for Mode 5 compliance.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** CAPTURE_TEMPLATE, Mode 5, RTT-SI-Spec v0.1

---

### R (Resonance Operator)

- **Type:** Operator
- **Symbol:** R
- **Layer:** Resonance monitoring; operator triad
- **Agent:** RMon (Class R)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The third operator of the φ–V–R triad. R measures the normalized cross-scale coupling strength between two subsystems x and y. High R indicates that subsystems are structurally reinforcing each other; low R indicates decoupling.

**Formula:** `R(x,y) = |⟨φ(x), φ(y)⟩| / (V(x)·V(y))^{1/2}`

**Failure mode detected:** Decoupling — subsystems that should reinforce each other diverge structurally.

**Constraint:** R requires both φ and V values for both subsystems x and y. R cannot be computed without a valid scope declaration for both subsystems.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** φ, V, SI_score, RMon, BArch

---

### RMon (Resonance Monitor)

- **Type:** Agent class
- **Symbol:** Class R
- **Layer:** Resonance monitoring
- **Agent:** RMon
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The agent class responsible for computing the R operator across declared subsystem pairs and monitoring cross-scale coupling throughout the measurement run.

**Primary constructs:** R operator; cross-scale coupling metrics

**Authority:** RMon reports decoupling events to BArch and Guard. RMon does not have interrupt authority.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** R, Guard, BArch, φ, V

---

### RTT-SI-Spec v0.1

- **Type:** Standard / protocol document
- **Symbol:** RTT-SI-Spec v0.1
- **Layer:** Student compliance; benchmark governance
- **Agent:** BArch (Class B), Guard (Class G)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The minimal valid benchmark protocol for RTT/Inside/Benchmarks. Defines the required fields of CAPTURE_TEMPLATE, permitted scale ranges, mandatory operator reports (φ, V, R), and invariant declarations (3C). Serves simultaneously as a teaching document for new practitioners and as a compliance reference for standards bodies.

**Constraint:** All captures must declare RTT-SI-Spec version in the provenance field. A capture without an RTT-SI-Spec version cannot be verified as protocol-compliant.

**Canonical reference:** `A_Overview.md` (this module)

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** CAPTURE_TEMPLATE, provenance, 3C Invariants, Guard, A_Overview.md

---

### scope

- **Type:** CAPTURE_TEMPLATE field
- **Symbol:** — (record field)
- **Layer:** Capture execution
- **Agent:** CAP (Class C), BArch (Class B)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The first mandatory field of the CAPTURE_TEMPLATE. Declares what was measured, at what scale range, and within what regime. Scope is the boundary that defines Zone X: any measurement or result that crosses the declared scope boundary without a new lineage declaration is in Zone X = OVERSCALE (ILLEGAL).

**Constraint:** Scope must specify: (a) classical grid dimensions OR qubit count; (b) regime declaration (classical / quantum-classical hybrid). Scope must be declared before φ, V, or R are computed.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** CAPTURE_TEMPLATE, Zone X, lineage, BArch

---

### SI_score (Structural Intelligence Score)

- **Type:** Derived metric
- **Symbol:** SI_score(x)
- **Layer:** Benchmark substrate
- **Agent:** BArch (Class B)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The primary output metric of RTT/Inside/Benchmarks. SI_score expresses the ratio of structural coherence (φ) to structural instability (V), regularized by a floor ε to prevent division-by-zero.

**Formula:** `SI_score(x) = φ(x) / (V(x) + ε)`

| Component | Meaning |
|---|---|
| φ(x) | Structural coherence at declared scale |
| V(x) | Variance (instability) at declared scale |
| ε | Regularization floor — must be declared before measurement |

**Constraint:** SI_score must not be reported without executing the measurement protocol (Mode 5 = FABRICATION is illegal). SI_score is a structural metric — it does not measure task accuracy, semantic correctness, or conventional ML performance.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** φ, V, BArch, Mode 5, CAPTURE_TEMPLATE

---

### V (Variance Operator)

- **Type:** Operator
- **Symbol:** V
- **Layer:** Benchmark substrate; operator triad
- **Agent:** BArch (Class B)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The second operator of the φ–V–R triad. V measures the instability or oscillation magnitude of the system at the declared scale. High V indicates that the system is unstable and oscillating; low V indicates stability.

**Role in SI_score:** V is the denominator (plus ε) — it is the noise floor against which φ is measured.

**Failure mode detected:** Instability — the system oscillates without settling into a structural regime.

**Constraint:** V must always be evaluated with the ε regularization floor (V + ε). ε must be declared before measurement.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** SI_score, φ, R, BArch, ε

---

### ε (Regularization Floor)

- **Type:** Parameter
- **Symbol:** ε (epsilon)
- **Layer:** Benchmark substrate
- **Agent:** BArch (Class B)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The regularization floor added to V in the SI_score denominator. ε prevents division-by-zero when V = 0 and provides a minimum noise floor for the stability estimate.

**Formal position:** `SI_score(x) = φ(x) / (V(x) + ε)`

**Constraint:** ε must be declared and non-zero before any SI_score computation. ε is a structural parameter — it is not a machine learning regularization hyperparameter in the conventional sense.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** SI_score, V, BArch

---

### Zone X = OVERSCALE (ILLEGAL)

- **Type:** Illegal zone
- **Symbol:** Zone X
- **Layer:** Structural governance; benchmark integrity
- **Agent:** Guard (Class G), DDet (Class D)
- **Annotation:** `[structural — no semantic inference]`

**Definition:** The zone label for extrapolating or applying benchmark results beyond the declared scope (scale range or regime) without validated lineage. Zone X = OVERSCALE is unconditionally illegal within RTT/Inside/Benchmarks. A measurement produced in Zone X is a projection, not a measurement — it cannot be included in a valid benchmark record.

**DRIFT_GATE connection:** Zone = X is one of the three DRIFT_GATE trigger conditions. Entering Zone X immediately fires the hard interrupt.

**Resolution:** Zone X can only be resolved by Guard (Class G). The path forward is not to extend the current capture — it is to declare a new scope, establish new lineage, and open a new CAPTURE_TEMPLATE.

**Constraint:** There is no legitimate measurement in Zone X. The label exists to make extrapolation machine-readable and auditable.

**Inheritance:** `[native — Benchmarks]`

**Cross-reference:** Guard, DRIFT_GATE, scope, CAPTURE_TEMPLATE, DDet

> **Disambiguation:** Zone X labels are module-specific. Zone X = OVERSCALE in RTT/Inside/Benchmarks is not the same construct as Zone X in RTT/3, RTT/12, or any other module. The "illegal zone" pattern is universal; the specific illegal condition is always module-local.

---

## Operator Symbols Reference

| Symbol | Name | Formula / Definition | Agent |
|---|---|---|---|
| φ | Structural Coherence | Measured at declared scale | BArch (Class B) |
| V | Variance | Measured at declared scale | BArch (Class B) |
| R | Resonance | `\|⟨φ(x), φ(y)⟩\| / (V(x)·V(y))^{1/2}` | RMon (Class R) |
| ε | Regularization floor | Declared parameter; prevents V+ε = 0 | BArch (Class B) |
| C(t) | Coherence at time t | Monitored continuously | DDet (Class D) |
| D(t) | Drift rate | `\|C(t) − C(t−1)\| / Δt` | DDet (Class D) |
| F_entropy(t) | Structural field entropy | `−Σ p(x,t) · log p(x,t)` | EEval (Class E) |
| SI_score(x) | Structural Intelligence Score | `φ(x) / (V(x) + ε)` | BArch (Class B) |

---

## Quick-Reference Tables

### Agent Classes

| Class | Name | Symbol | Primary Constructs |
|---|---|---|---|
| B | Benchmark Architect | BArch | φ–V–R triad; SI_score; structural audit |
| C | Capture Agent | CAP | CAPTURE_TEMPLATE; measurement execution |
| D | Drift Detector | DDet | 3C invariants; DRIFT_GATE; D(t) |
| E | Entropy Evaluator | EEval | F_entropy; collapse signatures |
| R | Resonance Monitor | RMon | R operator; cross-scale coupling |
| G | Guardian | Guard | Unconditional interrupt authority; Zone X; Mode 5 |

### Core Constructs

| Construct | Type | Owner |
|---|---|---|
| SI_score | Derived metric | BArch |
| φ–V–R triad | Operator set | BArch / RMon |
| 3C Invariants | Invariant set | DDet / BArch |
| DRIFT_GATE | Hard interrupt | DDet / Guard |
| CAPTURE_TEMPLATE | Record structure | CAP |
| RTT-SI-Spec v0.1 | Protocol standard | BArch / Guard |
| Zone X = OVERSCALE | Illegal zone | Guard |
| Mode 5 = FABRICATION | Illegal mode | Guard |

### Zones and Modes

| Label | Type | Condition | Resolution |
|---|---|---|---|
| Zone X = OVERSCALE | Illegal zone | Extrapolation beyond declared scope | Guard interrupt; new scope declaration |
| Mode 5 = FABRICATION | Illegal mode | Score reported without measurement | Guard interrupt; record voided |

### Scale Ranges

| Domain | Minimum | Maximum |
|---|---|---|
| Classical | 1D | 4096×4096 grid |
| Quantum-classical hybrid | 2 qubits | 256 qubits |

### 3C Invariants

| Invariant | Monitored by | DRIFT_GATE condition |
|---|---|---|
| Coherence (C) | DDet | C(t) < C_min |
| Consistency (Cs) | BArch / CAP | — (structural; verified at capture close) |
| Continuity (Ct) | DDet | D(t) > D_max |

### CAPTURE_TEMPLATE Fields

| Field | Order | Required | Owner |
|---|---|---|---|
| scope | 1 | Yes | CAP / BArch |
| lineage | 2 | Yes | CAP |
| provenance | 3 | Yes | CAP |
| interoperability | 4 | Yes | CAP / BArch |
| governance | 5 | Yes | CAP / Guard |

### Key Disambiguations

| Term | In Benchmarks | In other RTT modules |
|---|---|---|
| Zone X | OVERSCALE (ILLEGAL) | Module-specific illegal zone — always check context |
| Mode 5 | FABRICATION (ILLEGAL) | Module-specific mode number — always check context |
| φ | Structural coherence operator; scale-scoped | φ appears across RTT; Benchmarks adds scope enforcement |
| DRIFT_GATE | Hard interrupt with 3 specialized trigger conditions | Inherited base from RTT/Inside; trigger conditions vary per sub-module |
| Guard | Class G; unconditional authority over Zone X, Mode 5, collapse | Class G is universal; specific authority scope is module-local |
| 3C | {Coherence, Consistency, Continuity} | Term may appear in other modules with different member sets |
| F_entropy | Structural field entropy (RTT-native Shannon-form) | Not thermodynamic entropy; not Shannon communication entropy |

### Inheritance Chain

| Layer | Module | Key contribution to Benchmarks |
|---|---|---|
| 1 | RTT/1 | Origin field; base coherence axioms |
| 2 | RTT/2 | Field extension operators |
| 3 | RTT/3 | Triadic integration; triadic capture protocol |
| 4 | RTT/12 | Convergence metrics; cross-module alignment |
| 5 | RTT/micro_core | Distilled operator set |
| 6 | RTT/The_Inverted_Star | Inversion logic; SHADOW_CORRIDOR handling |
| 7 | RTT/Inside | BKM; CORRIDOR; DRIFT_GATE (base); LINEAGE_CHAIN |
| 8 | RTT/Inside/Benchmarks | φ–V–R; 3C; SI_score; CAPTURE_TEMPLATE; Zone X; Mode 5 |

---

*`[structural — no semantic inference]` — all terms, operators, metrics, and constructs in this glossary are structural. No semantic meaning is inferred from any definition, symbol, or output field.*
