<img width="1194" height="672" alt="Resonance_Truth_architecture_truth_service_components_" src="https://github.com/user-attachments/assets/2b614d15-8803-42c7-ac22-926576c18d25" />

# RTT Resonance Truth Service — Components

**Module:** Resonance Truth  
**Artifact:** Component Model  
**Framework:** Resonance-Time Theory (RTT)  
**Status:** Research Architecture / Reference Model  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This document defines the functional components of the RTT Resonance Truth Service.

The conceptual architecture is defined in:

    truth_service_architecture.md

The machine-facing API contract is defined in:

    truth_service_api.yaml

The logical entity model is defined in:

    truth_service_data_model.md

This document focuses on a different question:

> **Which component owns each stage of the operational truth lifecycle?**

The component model begins with a Claim and a declared Regime, gathers and qualifies Observations, evaluates their structural relationships, synthesizes a Truth State, governs possible Correction, and schedules future Revalidation.

The primary processing sequence is:

    Claim Intake
        ↓
    Truth-Class Resolver
        ↓
    Regime Resolver
        ↓
    Anchor / Source Registry
        ↓
    Observation Intake
        ↓
    Lineage Resolver
        ↓
    Qualification Engine
        ↓
    Coherence Engine
        ↓
    Drift Engine
        ↓
    Paradox Register
        ↓
    Truth-State Synthesizer
        ↓
    Correction Policy Engine
        ↓
    Revalidation Scheduler
        ↓
    Audit + Lineage Store

---

# 1. Component Design Principles

The component architecture follows several rules.

## 1.1 Components Own Decisions

Each major structural decision should have an identifiable owner.

Examples:

- Observation eligibility → Qualification Engine
- Observation agreement → Coherence Engine
- displacement → Drift Engine
- unresolved contradiction → Paradox Register
- operational boundary → Regime Resolver
- resulting state → Truth-State Synthesizer
- downstream adjustment → Correction Policy Engine
- future reevaluation → Revalidation Scheduler

This avoids hiding unrelated decisions inside one generalized evaluator.

---

## 1.2 Components Preserve Evidence

A component should not silently discard information simply because that information does not contribute to the current Truth State.

For example:

    Observation
        ↓
    Qualification Engine
        ↓
    REJECTED FROM SYNTHESIS

does not imply:

    DELETE OBSERVATION

The rejected Observation remains part of the Evaluation record.

---

## 1.3 Components May Return Indeterminate Results

An internal component should be able to report that it cannot establish a sufficiently qualified result.

Examples include:

    lineage: incomplete

    coherence: indeterminate

    drift: unknown

    regime: unresolved

Such states should propagate visibly rather than automatically being replaced with defaults.

---

## 1.4 Components Do Not Manufacture Precision

If a domain provides measurable quantities, components may preserve them.

Example:

    drift:
      magnitude: 14
      unit: milliseconds

If the domain does not provide meaningful numeric precision:

    drift:
      magnitude: null
      dimension: semantic

remains valid.

---

## 1.5 Runtime and Research Components Remain Separate

The runtime component plane evaluates Claims.

The research component plane evaluates operational reference systems.

Research-system scores should never influence runtime Truth-State synthesis.

---

# 2. Component Topology

The primary component topology is:

    ┌──────────────────────────┐
    │       Claim Intake       │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ Truth-Class Resolver     │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │     Regime Resolver      │
    └────────────┬─────────────┘
                 │
          ┌──────┴──────┐
          │             │
          ▼             ▼
    ┌──────────────┐  ┌──────────────────┐
    │ Anchor       │  │ Source           │
    │ Registry     │  │ Registry         │
    └──────┬───────┘  └────────┬─────────┘
           │                   │
           └─────────┬─────────┘
                     ▼
    ┌──────────────────────────┐
    │    Observation Intake    │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │    Lineage Resolver      │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │  Qualification Engine    │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │    Coherence Engine      │
    └────────────┬─────────────┘
                 │
          ┌──────┴──────┐
          │             │
          ▼             ▼
    ┌──────────────┐  ┌──────────────────┐
    │ Drift Engine │  │ Paradox Register │
    └──────┬───────┘  └────────┬─────────┘
           │                   │
           └─────────┬─────────┘
                     ▼
    ┌──────────────────────────┐
    │ Truth-State Synthesizer  │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ Correction Policy Engine │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │ Revalidation Scheduler   │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │  Audit + Lineage Store   │
    └──────────────────────────┘

The topology represents logical responsibility.

It does not require every logical component to become a separately deployed service.

---

# 3. Claim Intake

## Responsibility

Claim Intake owns registration and structural validation of Claims.

It answers:

> **What is being asserted?**

## Inputs

- statement
- declared Truth Classes
- intended use
- external reference
- request metadata

## Outputs

- Claim
- Claim identifier
- registration status

## Responsibilities

Claim Intake should:

- preserve the original statement
- assign a stable Claim identifier
- validate required fields
- preserve intended use
- preserve externally supplied references
- record registration time

## Non-Responsibilities

Claim Intake should not:

- determine whether the Claim is true
- select Sources
- resolve a Regime
- assign confidence
- synthesize a Truth State

## Example

Input:

    statement:
      "The current reference time is 09:00:00 UTC."

    truth_classes:
      - temporal

Output:

    claim_id:
      claim-temporal-001

    status:
      registered

No truth determination has occurred.

---

# 4. Truth-Class Resolver

## Responsibility

The Truth-Class Resolver determines which operational Truth Classes participate in evaluation.

It answers:

> **What kinds of truth are present in this Claim?**

## Truth Classes

The current classes are:

- Temporal
- Locational
- Identity
- Integrity
- Authority
- State
- Transactional
- Intent
- Observational
- Lineage

## Inputs

- Claim
- declared Truth Classes
- optional classification evidence

## Outputs

- confirmed Truth Classes
- suggested Truth Classes
- unresolved classifications
- rationale

## Design Rule

Explicitly declared Truth Classes should remain distinguishable from inferred or suggested classes.

For example:

    declared:
      - integrity

    suggested:
      - temporal
      - authority
      - lineage

The architecture should not silently expand a Claim's declared meaning.

## Example

Claim:

> This TLS certificate is valid.

Potential dimensions:

    Identity
    Integrity
    Authority
    Temporal
    Lineage

The resolver identifies inspection dimensions.

It does not determine certificate validity.

---

# 5. Regime Resolver

## Responsibility

The Regime Resolver determines the operational boundary under which the Claim should be evaluated.

It answers:

> **Under what conditions must this result remain valid?**

## Inputs

- Claim
- Truth Classes
- requested Regime
- policy constraints
- observer context
- intended use

## Outputs

- resolved Regime
- Regime identifier
- compatibility requirements
- unresolved Regime conflicts

## Regime Properties

A Regime may define:

- domain
- observer context
- jurisdiction
- applicable scope
- policy version
- precision requirement
- maximum Observation age
- minimum independent Sources
- consequence level
- permitted Truth States
- permitted Correction modes

## Example

For the same temporal Claim:

    Regime A:
      display clock
      maximum error: moderate
      consequence: low

    Regime B:
      transaction ordering
      maximum error: strict
      consequence: high

The observations may be identical.

The operational result may differ.

## Failure Behavior

If no suitable Regime is available:

    regime:
      unresolved

The service should not silently apply an arbitrary default Regime.

---

# 6. Anchor Registry

## Responsibility

The Anchor Registry maintains recognized bounded reference authorities.

It answers:

> **Which references may legitimately anchor this evaluation?**

## Inputs

- Anchor registrations
- Anchor status changes
- Regime
- domain
- validity information
- revocation information

## Outputs

- eligible Anchors
- Anchor status
- Anchor scope
- validity boundaries
- limitations

## Anchor States

An Anchor may be:

- active
- degraded
- withdrawn
- revoked
- unknown

## Design Rule

Anchor authority is bounded.

An Anchor recognized in one Regime should not automatically be considered authoritative in another.

## Example

For Temporal Truth:

    Anchor:
      UTC reference

For Identity Truth:

    Anchor:
      recognized identity authority

For Intent Truth:

    Anchor:
      declared configuration or policy

The abstraction is structural, not domain-specific.

---

# 7. Source Registry

## Responsibility

The Source Registry maintains entities capable of supplying Observations.

It answers:

> **Who or what produced this Observation?**

## Inputs

- Source registration
- Source status
- associated Anchor
- domain
- Lineage distance
- independence classification
- validity information

## Outputs

- Source records
- Source status
- Anchor relationship
- Lineage distance
- independence metadata

## Source States

Initial Source states include:

- active
- degraded
- unavailable
- rejected
- unknown

## Design Rule

The Source Registry describes Sources.

It does not by itself decide whether a Source is qualified for a particular Evaluation.

That decision belongs to the Qualification Engine.

---

# 8. Observation Intake

## Responsibility

Observation Intake registers evidence associated with Claims.

It answers:

> **What was actually observed?**

## Inputs

- Claim identifier
- Source identifier
- optional Anchor identifier
- observed value
- observation time
- receipt time
- expiration time
- Lineage
- integrity information
- Source-declared confidence
- domain metadata

## Outputs

- Observation
- Observation identifier
- registration time

## Design Rule

Observation Intake should preserve domain-native values.

It should not force all Observations into one scalar type.

### Temporal Example

    value:
      timestamp: ...
      offset_ms: ...
      delay_ms: ...
      jitter_ms: ...

### Integrity Example

    value:
      digest: ...
      signature_status: ...

### State Example

    value:
      declared_state: ...
      observed_state: ...

## Non-Responsibilities

Observation Intake does not determine:

- qualification
- Coherence
- Drift
- Truth State

It preserves evidence for later evaluation.

---

# 9. Lineage Resolver

## Responsibility

The Lineage Resolver reconstructs the path connecting an Observation to Sources, Anchors, dependencies, and transformations.

It answers:

> **How did this Observation arrive here?**

## Inputs

- Observation
- Source
- Anchor
- supplied Lineage hops
- known dependencies
- transformation records

## Outputs

- Lineage graph
- Lineage distance
- transformation count
- known gaps
- completeness state

## Example

    Anchor UTC
        ↓
    Source A
        ↓
    Observation 1

A more complex path might be:

    Anchor
      ↓
    Authority
      ↓
    Upstream Source
      ↓
    Aggregator
      ↓
    Transformation
      ↓
    Local Source
      ↓
    Observation

## Lineage Result

A result may indicate:

    complete: true

or:

    complete: false
    gaps:
      - upstream dependency unavailable

## Design Rule

The Lineage Resolver should expose missing Lineage.

It should not invent provenance to produce a complete graph.

---

# 10. Qualification Engine

## Responsibility

The Qualification Engine determines whether Observations may participate in the current Evaluation.

It answers:

> **Is this Observation suitable for this evaluation under this Regime?**

## Inputs

- Observation
- Source
- Anchor
- Lineage
- Regime
- current evaluation time

## Qualification Dimensions

Evaluation may consider:

- freshness
- Source status
- Anchor status
- Lineage completeness
- Regime compatibility
- precision compatibility
- integrity
- Source independence
- duplication
- structural validity

## Outputs

Each Observation receives a Qualification result:

- qualified
- degraded
- rejected
- expired
- indeterminate

Each result should include rationale.

## Example

    observation_id:
      obs-003

    qualification:
      status: rejected

      reason:
        observation exceeds regime maximum age

This means:

> Observation 003 cannot participate in the current synthesis.

It does not mean:

> Observation 003 was never true.

## Critical Constraint

    REJECTED FROM SYNTHESIS
            ≠
    FACTUALLY FALSE

---

# 11. Coherence Engine

## Responsibility

The Coherence Engine evaluates relationships among qualified Observations.

It answers:

> **Do these Observations form a mutually usable state?**

## Inputs

- qualified Observations
- Source identities
- Source independence
- Lineage relationships
- Regime
- domain-specific comparison rules

## Outputs

- Coherence State
- clusters
- supporting Observations
- dissenting Observations
- outliers
- rationale

## Coherence States

- coherent
- weakly_coherent
- fragmented
- contested
- inverted
- indeterminate

## Example

    Observation A → X
    Observation B → X
    Observation C → Y

Potential output:

    coherence:
      coherent

    supporting:
      A
      B

    dissenting:
      C

That result is only justified if Source independence and other structural conditions support it.

## Shared Lineage

Suppose:

    Upstream U
      ├── A → X
      ├── B → X
      └── C → X

The engine should avoid treating A, B, and C automatically as three independent confirmations.

Lineage informs Coherence.

---

# 12. Coherence Cluster Manager

## Responsibility

The Coherence Cluster Manager groups mutually compatible qualified Observations without forcing incompatible observations into a common result.

It answers:

> **Which Observations belong to the same coherent field?**

## Inputs

- qualified Observations
- comparison relationships
- Source independence
- Lineage
- Regime

## Outputs

One or more Coherence clusters.

Example:

    Cluster A
      obs-001
      obs-002
      obs-003

    Cluster B
      obs-004
      obs-005

## Cluster Classification

A cluster may be classified as:

- supporting
- dissenting
- outlier
- unresolved

## Design Rule

Cluster formation precedes final selection.

The system should not begin with a desired answer and then assign Observations around it.

---

# 13. Drift Engine

## Responsibility

The Drift Engine evaluates displacement among relevant states.

It answers:

> **How far has the state moved from its reference, prior state, or expectation?**

## Inputs

Possible comparisons include:

- local state vs qualified Observation
- prior Truth State vs current evidence
- declared state vs observed state
- Source vs Source
- expected state vs actual state
- Regime requirements vs current condition

## Drift Dimensions

Initial dimensions include:

- value
- semantic
- Source
- Lineage
- temporal
- Regime
- confidence
- policy

## Outputs

A Drift State may contain:

- magnitude
- unit
- direction
- dimensions
- bounded status
- baseline reference
- local value
- observed value
- rationale

## Numeric Example

    magnitude:
      14

    unit:
      milliseconds

    dimension:
      temporal

    bounded:
      true

## Non-Numeric Example

    magnitude:
      null

    dimension:
      semantic

    direction:
      unknown

    bounded:
      null

## Design Rule

The Drift Engine may report that Drift exists without declaring whether the Drift is acceptable.

Acceptance is Regime-dependent.

---

# 14. Paradox Register

## Responsibility

The Paradox Register preserves unresolved qualified contradictions.

It answers:

> **Which contradictions remain after qualification and Coherence analysis?**

## Inputs

- qualified Observations
- Coherence clusters
- Drift findings
- applicable Regimes

## Outputs

Paradox objects containing:

- Paradox identifier
- type
- competing Observations
- competing clusters
- applicable Regimes
- description
- containment mode
- resolution condition
- status

## Paradox Types

### Structural

Valid structures imply incompatible states.

### Semantic

The same language carries incompatible meanings.

### Regime

Different states are valid under different operational boundaries.

## Containment Modes

- preserve
- isolate
- separate_by_regime
- escalate
- resolved

## Design Rule

The register does not exist solely to remove contradictions.

Its first function is to preserve and characterize them.

---

# 15. Truth-State Synthesizer

## Responsibility

The Truth-State Synthesizer integrates evaluation outputs into a qualified operational state.

It answers:

> **Given everything presently known, what state can this service support?**

## Inputs

- Claim
- Truth Classes
- Regime
- qualified Observations
- selected Sources
- Anchors
- Lineage
- Coherence State
- Drift State
- Paradoxes

## Outputs

A Truth State containing:

- status
- accepted value
- Regime
- Truth Classes
- Anchor references
- Source references
- Observation references
- Lineage references
- Coherence
- Drift
- Paradoxes
- uncertainty
- permitted uses
- prohibited uses
- Correction Policy
- evaluation time
- expiration time
- Revalidation conditions

## Supported Truth States

- declared
- observed
- corroborated
- operationally_accepted
- contested
- degraded
- held_over
- expired
- rejected
- indeterminate

## Null Result

The synthesizer must be able to produce:

    status:
      indeterminate

    accepted_value:
      null

This is a successful Evaluation.

## Design Rule

The synthesizer integrates component results.

It should not silently redo their work using hidden rules.

---

# 16. Correction Policy Engine

## Responsibility

The Correction Policy Engine determines what downstream response is permitted when a Truth State differs from current operational state.

It answers:

> **What may change because of this Truth State?**

## Inputs

- Truth State
- prior Truth State
- Drift
- Regime
- consequence level
- configured policy

## Outputs

A Correction Policy.

## Supported Modes

- none
- step
- gradual
- quarantine
- dual_state
- human_escalation
- holdover
- fail_closed
- fail_bounded

## Example

    drift:
      magnitude: 14
      unit: milliseconds
      bounded: true

    correction:
      mode: gradual

A different Regime may produce:

    correction:
      mode: quarantine

from the same Drift.

## Critical Constraint

The Correction Policy Engine does not determine what is true.

It determines what action is permitted in response to a Truth State.

---

# 17. Revalidation Scheduler

## Responsibility

The Revalidation Scheduler determines when a Truth State must be evaluated again.

It answers:

> **When does this state need to be challenged?**

## Inputs

- Truth State
- Regime
- expiration
- Source status
- Anchor status
- Drift
- paradox status
- configured lifecycle rules

## Triggers

Initial Revalidation triggers include:

- elapsed time
- expiration
- Source change
- Anchor change
- Regime change
- contradictory Observation
- excessive Drift
- reduced Source diversity
- policy change
- manual challenge

## Outputs

- next Revalidation time
- active Revalidation triggers
- Revalidation request

## Lifecycle

    ACCEPT
      ↓
    USE
      ↓
    AGE
      ↓
    REVALIDATE
      │
      ├── RENEW
      ├── DEGRADE
      ├── CONTEST
      ├── HOLD OVER
      ├── REJECT
      └── EXPIRE

## Design Rule

Revalidation creates a new Evaluation.

It does not rewrite the old Evaluation.

---

# 18. Holdover Manager

## Responsibility

The Holdover Manager governs provisional continuity when fresh qualified evidence temporarily becomes unavailable.

It answers:

> **May the previous Truth State remain provisionally usable?**

## Inputs

- previous Truth State
- time since last qualified Evaluation
- historical stability
- expected Drift
- Regime
- consequence level
- Source availability

## Outputs

- holdover permitted
- holdover denied
- holdover expiration
- degraded uncertainty
- permitted uses

## Example

    previous_state:
      operationally_accepted

    source_status:
      temporarily_unavailable

    regime:
      permits_holdover

    result:
      held_over

Holdover is not equivalent to fresh acceptance.

The state should visibly indicate that fresh qualification is unavailable.

---

# 19. Audit + Lineage Store

## Responsibility

The Audit + Lineage Store preserves the evaluation history required to reconstruct Truth States.

It answers:

> **Why did the system reach this state?**

and:

> **How did the evidence arrive here?**

## Stores

The store should preserve:

- Claims
- Truth Classes
- Regimes
- Anchors
- Sources
- Observations
- Lineage
- Qualification results
- Coherence States
- Drift States
- Paradoxes
- Evaluations
- Truth States
- Correction Policies
- Revalidation events

## Design Rule

Evaluation history should be append-oriented.

Existing Evaluations and Truth States should not normally be rewritten when new evidence arrives.

## Historical Chain

    Evaluation 1
        ↓
    Truth State 1
        ↓
    Revalidation
        ↓
    Evaluation 2
        ↓
    Truth State 2
        ↓
    Revalidation
        ↓
    Evaluation 3
        ↓
    Truth State 3

This allows the system to reconstruct not only:

> What does the service currently support?

but also:

> How did the supported state change?

---

# 20. Explainability Service

## Responsibility

The Explainability Service translates stored evaluation structure into an inspectable explanation.

It answers:

> **Why does this Truth State exist?**

## Inputs

- Evaluation
- Qualification results
- Source and Anchor records
- Lineage
- Coherence findings
- Drift findings
- Paradox findings
- Regime findings
- synthesis rationale

## Outputs

An Evaluation Explanation containing:

- participating Observations
- excluded Observations
- exclusion reasons
- selected Sources
- relevant Anchors
- Lineage relationships
- Coherence rationale
- Drift rationale
- Paradox rationale
- Regime rationale
- synthesis rationale

## Critical Constraint

Explainability should arise from stored evaluation evidence.

It should not require an unrelated model to invent a plausible explanation after the decision.

---

# 21. API Gateway

## Responsibility

The API Gateway exposes the supported external service contract.

It answers:

> **How do external consumers interact with the Truth Service?**

## Principal Operations

The external flow is:

    Register Claim
         ↓
    Register Observations
         ↓
    Evaluate Claim
         ↓
    Retrieve Truth State
         ↓
    Inspect Evaluation
         ↓
    Inspect Lineage
         ↓
    Inspect Paradox
         ↓
    Request Revalidation

## Design Rule

The API Gateway exposes service capabilities.

It should not require the internal architecture to map one-to-one onto HTTP endpoints.

For example:

    Coherence Engine

does not require:

    POST /coherence-engine

The Coherence Engine may remain an internal component invoked during Evaluation.

---

# 22. Evaluation Coordinator

## Responsibility

The Evaluation Coordinator orchestrates one complete Evaluation without owning the specialized decision logic of subordinate components.

It answers:

> **Which components must participate, and in what order, to evaluate this Claim?**

## Flow

    Claim
      ↓
    Resolve Truth Classes
      ↓
    Resolve Regime
      ↓
    Resolve Sources / Anchors
      ↓
    Resolve Lineage
      ↓
    Qualify Observations
      ↓
    Evaluate Coherence
      ↓
    Evaluate Drift
      ↓
    Register Paradox
      ↓
    Synthesize Truth State
      ↓
    Determine Correction Policy
      ↓
    Schedule Revalidation
      ↓
    Persist Evaluation

## Design Rule

The coordinator should orchestrate.

It should not contain hidden alternative implementations of:

- Qualification
- Coherence
- Drift
- Paradox
- synthesis

This keeps component responsibility inspectable.

---

# 23. Component Input / Output Matrix

| Component | Primary Input | Primary Output |
|---|---|---|
| Claim Intake | Claim request | Claim |
| Truth-Class Resolver | Claim | Truth Classes |
| Regime Resolver | Claim + intended use | Regime |
| Anchor Registry | Domain + Regime | Anchors |
| Source Registry | Source identity | Source records |
| Observation Intake | Raw evidence | Observation |
| Lineage Resolver | Observation + Source | Lineage graph |
| Qualification Engine | Observation + Regime | Qualification |
| Coherence Engine | Qualified Observations | Coherence State |
| Cluster Manager | Qualified Observations | Coherence clusters |
| Drift Engine | Current + reference states | Drift State |
| Paradox Register | Conflicting qualified evidence | Paradoxes |
| Truth-State Synthesizer | Evaluation results | Truth State |
| Correction Policy Engine | Truth State + Regime | Correction Policy |
| Revalidation Scheduler | Truth State + lifecycle conditions | Revalidation trigger |
| Holdover Manager | Prior state + Source loss | Holdover decision |
| Audit + Lineage Store | Evaluation artifacts | Immutable history |
| Explainability Service | Stored Evaluation | Explanation |
| API Gateway | External request | Service response |
| Evaluation Coordinator | Evaluation request | Complete Evaluation |

---

# 24. Decision Ownership Matrix

| Decision | Owner |
|---|---|
| What is being asserted? | Claim Intake |
| Which Truth Classes are involved? | Truth-Class Resolver |
| Which operational boundary applies? | Regime Resolver |
| Which reference Anchors exist? | Anchor Registry |
| Which Sources exist? | Source Registry |
| What evidence was received? | Observation Intake |
| Where did evidence come from? | Lineage Resolver |
| May an Observation participate? | Qualification Engine |
| Do qualified Observations agree? | Coherence Engine |
| Which Observations form clusters? | Coherence Cluster Manager |
| How far has state moved? | Drift Engine |
| Which contradictions remain? | Paradox Register |
| What Truth State is supported? | Truth-State Synthesizer |
| What downstream correction is permitted? | Correction Policy Engine |
| When must the state be challenged again? | Revalidation Scheduler |
| May prior state persist without fresh evidence? | Holdover Manager |
| Why did the service decide this? | Explainability Service |
| What history is preserved? | Audit + Lineage Store |
| Which components execute an Evaluation? | Evaluation Coordinator |

A decision should have one primary owner even when several components provide evidence.

---

# 25. NTP Reference Flow

The initial deterministic reference implementation maps NTP-like structures through the components as follows:

    NTP-like temporal Claim
            ↓
    Claim Intake
            ↓
    Temporal Truth
            ↓
    Regime Resolver
            ↓
    Time Reference Anchor
            ↓
    NTP-like Sources
            ↓
    Temporal Observations
            ↓
    Lineage Resolver
            ↓
    Observation Qualification
            ↓
    Coherence Clustering
            ↓
    Temporal Drift
            ↓
    Outlier / Paradox Preservation
            ↓
    Temporal Truth State
            ↓
    Bounded Correction Policy
            ↓
    Revalidation Schedule

The mapping includes:

| NTP Mechanism | Component Responsibility |
|---|---|
| Reference clock | Anchor Registry |
| Time Source | Source Registry |
| association | Source / Lineage relationship |
| stratum | Lineage Resolver |
| time sample | Observation Intake |
| filtering | Qualification Engine |
| Source selection | Qualification / Coherence |
| clustering | Coherence Cluster Manager |
| offset | Drift Engine |
| jitter | Drift / Observation stability analysis |
| dispersion | uncertainty / freshness evaluation |
| combination | Truth-State Synthesizer |
| clock discipline | Correction Policy Engine |
| polling | Revalidation Scheduler |
| loss of synchronization | Holdover / lifecycle handling |

This is a structural crosswalk.

The Truth Service does not attempt to reproduce NTP internally.

---

# 26. Runtime Processing Sequence

A complete runtime Evaluation proceeds as follows.

## Step 1 — Receive Claim

Claim Intake validates and registers the assertion.

## Step 2 — Resolve Truth Classes

The Truth-Class Resolver establishes applicable inspection dimensions.

## Step 3 — Resolve Regime

The Regime Resolver establishes operational acceptance conditions.

## Step 4 — Resolve References

Anchor and Source Registries establish known references and Source relationships.

## Step 5 — Register Observations

Observation Intake records evidence without prematurely evaluating it.

## Step 6 — Resolve Lineage

The Lineage Resolver reconstructs known provenance and dependencies.

## Step 7 — Qualify Observations

The Qualification Engine determines which Observations may participate.

## Step 8 — Analyze Coherence

The Coherence Engine and Cluster Manager determine the structure of agreement.

## Step 9 — Measure Drift

The Drift Engine compares relevant states.

## Step 10 — Register Paradox

Unresolved qualified contradictions are preserved.

## Step 11 — Synthesize Truth State

The Truth-State Synthesizer produces the current operational state.

## Step 12 — Determine Correction

The Correction Policy Engine specifies permitted downstream response.

## Step 13 — Schedule Revalidation

The Revalidation Scheduler establishes future challenge conditions.

## Step 14 — Persist

The Audit + Lineage Store records the complete Evaluation.

## Step 15 — Explain

The Explainability Service exposes the decision structure when requested.

---

# 27. Failure Propagation

Component failure should remain visible.

Examples:

    Lineage Resolver
      → incomplete

does not automatically become:

    Evaluation
      → failed

The Regime may permit partial Lineage.

Likewise:

    Drift Engine
      → magnitude unknown

may still permit an Evaluation if the domain does not support numeric Drift measurement.

The architecture should distinguish:

## Component Uncertainty

A component cannot fully characterize its dimension.

## Evaluation Indeterminacy

The Evaluation cannot support a qualified Truth State.

## Infrastructure Failure

The implementation could not execute the component.

These are structurally different conditions.

---

# 28. Component Status

Operational implementations may expose component status such as:

- available
- degraded
- unavailable
- unknown

This status describes the implementation component.

It must remain distinct from Truth-State status.

For example:

    Coherence Engine:
      available

does not imply:

    coherence:
      coherent

Similarly:

    Truth Service:
      available

does not imply:

    Claim:
      operationally_accepted

---

# 29. Security Boundaries

Each component should operate under least-privilege assumptions.

## Claim Intake

Treat Claim content as untrusted input.

## Observation Intake

Treat Observation content and metadata as untrusted input.

## Source Registry

Do not infer trust from Source existence alone.

## Anchor Registry

Protect Anchor lifecycle and revocation operations.

## Lineage Resolver

Do not invent missing provenance.

## Qualification Engine

Make qualification policy inspectable.

## Regime Resolver

Protect Regime selection from silent manipulation.

## Truth-State Synthesizer

Do not allow metadata fields to override canonical evaluation fields.

## Correction Policy Engine

Separate evaluation permission from mutation authority.

## Audit Store

Preserve Evaluation history against unauthorized rewriting.

## Explainability Service

Avoid exposing protected Source information beyond permitted access boundaries.

---

# 30. Deployment Model

The component model is logical.

A reference implementation may begin as a single application:

    ┌──────────────────────────────────────┐
    │ Resonance Truth Service             │
    │                                     │
    │ Claim Intake                        │
    │ Truth-Class Resolver                │
    │ Regime Resolver                     │
    │ Anchor / Source Registry            │
    │ Observation Intake                  │
    │ Lineage Resolver                    │
    │ Qualification Engine                │
    │ Coherence Engine                    │
    │ Drift Engine                        │
    │ Paradox Register                    │
    │ Truth-State Synthesizer             │
    │ Correction Policy Engine            │
    │ Revalidation Scheduler              │
    │ Explainability Service              │
    │ Evaluation Coordinator              │
    └──────────────────┬───────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Persistent Store│
              └─────────────────┘

There is no architectural requirement to begin with microservices.

Components should be separated by responsibility before they are separated by deployment.

---

# 31. Extension Points

Later Truth Classes may require domain-specific evaluators.

Potential extension points include:

- temporal comparison
- namespace resolution
- identity verification
- integrity verification
- authorization policy evaluation
- state comparison
- transaction finality
- desired-state comparison
- telemetry correlation
- provenance analysis

These should plug into shared architectural components rather than replacing them.

For example:

    Qualification Engine
        │
        ├── Temporal Qualification
        ├── Identity Qualification
        ├── Integrity Qualification
        └── Lineage Qualification

Likewise:

    Drift Engine
        │
        ├── Temporal Drift
        ├── State Drift
        ├── Semantic Drift
        └── Policy Drift

Domain specialization should occur below stable component responsibilities.

---

# 32. Research Scoring Components

Research scoring belongs outside the runtime Evaluation path.

A minimal Research Plane may contain:

    Reference-System Registry
            ↓
    Crosswalk Evidence Store
            ↓
    Scoring Engine
            ↓
    Comparative Profile

## Reference-System Registry

Records:

- NTP
- DNS
- IAM
- PKI
- Policy / IAM
- Distributed Systems
- Ledgers
- Desired-State Systems
- Telemetry
- Supply-Chain Provenance

## Crosswalk Evidence Store

Preserves the evidence supporting each architectural mapping.

## Scoring Engine

Evaluates:

- Anchor Quality
- Lineage Visibility
- Observation Quality
- Coherence Detection
- Drift Detection
- Paradox Handling
- Regime Awareness
- Freshness / Revalidation
- Correction Discipline
- Failure Transparency

## Comparative Profile

Produces the ten-dimensional structural profile and RTT meta-score.

## Critical Separation

    Research Score
          │
          X
          │
    Runtime Truth State

No direct dependency should exist.

---

# 33. Component Evolution Rule

A new Reference System may expose behavior that the current component model cannot represent.

When this occurs:

    New Mechanism
         ↓
    Identify Missing Capability
         ↓
    Ask:
      Is it domain-specific?
         │
       ┌─┴─┐
      Yes  No
       │    │
       ▼    ▼
    Extension   Candidate Core Change
                    ↓
              Test Other Crosswalks
                    ↓
              Promote if justified

The architecture should resist adding new core components from a single example unless the mechanism is sufficiently fundamental.

This keeps the component model bounded.

---

# 34. Component-Level Tests

Each component should eventually support deterministic tests.

## Claim Intake

- accepts valid Claim
- rejects structurally invalid Claim
- preserves original statement

## Truth-Class Resolver

- preserves explicit class
- distinguishes suggested class
- supports multiple classes

## Regime Resolver

- resolves compatible Regime
- detects missing Regime
- preserves Regime conflict

## Lineage Resolver

- reconstructs complete Lineage
- exposes missing hop
- detects shared dependency

## Qualification Engine

- qualifies eligible Observation
- rejects stale Observation
- rejects incompatible Regime
- preserves rejection rationale

## Coherence Engine

- identifies coherent group
- identifies dissent
- identifies fragmentation
- avoids simple vote-count behavior

## Drift Engine

- measures numeric Drift
- represents qualitative Drift
- permits unknown magnitude

## Paradox Register

- preserves structural contradiction
- separates Regime contradiction
- records resolution condition

## Truth-State Synthesizer

- produces accepted state
- produces contested state
- produces null accepted value
- produces Indeterminate state

## Correction Policy Engine

- separates correction from evaluation
- obeys Regime constraints

## Revalidation Scheduler

- schedules expiration
- responds to Source change
- responds to contradictory Observation

## Holdover Manager

- permits bounded holdover
- rejects disallowed holdover
- expires holdover

## Explainability Service

- reconstructs rationale from stored Evaluation

---

# 35. Initial Component Milestone

The first working component chain does not require every component at full generality.

The minimum NTP reference chain is:

    Claim Intake
        ↓
    Regime Resolver
        ↓
    Anchor Registry
        ↓
    Source Registry
        ↓
    Observation Intake
        ↓
    Lineage Resolver
        ↓
    Qualification Engine
        ↓
    Coherence Engine
        ↓
    Drift Engine
        ↓
    Truth-State Synthesizer
        ↓
    Correction Policy Engine
        ↓
    Revalidation Scheduler
        ↓
    Audit Store

The Paradox Register becomes mandatory when testing:

- outlier
- fragmented
- incompatible-Regime

fixtures.

---

# 36. Initial Success Condition

The component architecture succeeds at its first milestone when the following scenario is reproducible.

Given:

    Claim:
      Current reference time is T.

    Truth Class:
      Temporal

    Regime:
      Low-consequence display clock

    Sources:
      A
      B
      C

    Observations:
      A → T + 12 ms
      B → T + 15 ms
      C → T + 14 ms

the components can:

1. register the Claim
2. identify the Temporal Truth Class
3. resolve the Regime
4. identify Sources and Anchor
5. preserve Lineage
6. qualify the Observations
7. identify Coherence
8. measure bounded Drift
9. synthesize a Truth State
10. determine permitted Correction
11. schedule Revalidation
12. persist the Evaluation
13. explain every major decision

A second fixture should then alter Source C materially enough to test whether disagreement remains visible.

---

# 37. Governing Component Principle

> **One structural question, one primary decision owner.**

The component architecture should make it possible to ask:

    Who qualified this Observation?

    Who determined Coherence?

    Who measured Drift?

    Who preserved the contradiction?

    Who resolved the Regime?

    Who synthesized the Truth State?

    Who permitted Correction?

    Who scheduled Revalidation?

and receive a clear answer.

This prevents the service from becoming an opaque generalized evaluator in which evidence, policy, inference, and action disappear into one undifferentiated decision.

---

# 38. Canonical Component Summary

The component model can be reduced to the following operational sequence:

    INTAKE
      │
      ▼
    Claim
      │
      ▼
    CLASSIFY
      │
      ▼
    Truth Class
      │
      ▼
    BOUND
      │
      ▼
    Regime
      │
      ▼
    REFERENCE
      │
      ▼
    Anchor + Source
      │
      ▼
    OBSERVE
      │
      ▼
    Observation
      │
      ▼
    TRACE
      │
      ▼
    Lineage
      │
      ▼
    QUALIFY
      │
      ▼
    Eligible Evidence
      │
      ▼
    COMPARE
      │
      ▼
    Coherence
      │
      ├──────────────┐
      ▼              ▼
    MEASURE        CONTAIN
      │              │
      ▼              ▼
    Drift          Paradox
      │              │
      └──────┬───────┘
             ▼
    SYNTHESIZE
             │
             ▼
        Truth State
             │
             ▼
    GOVERN RESPONSE
             │
             ▼
        Correction
             │
             ▼
    CHALLENGE AGAIN
             │
             ▼
       Revalidation
             │
             ▼
    PRESERVE HISTORY
             │
             ▼
     Audit + Lineage

The components exist to make the truth relationship inspectable.

They should not hide uncertainty, collapse contradiction prematurely, or obscure the boundary between observation and action.

**Observe.**

**Trace.**

**Qualify.**

**Compare.**

**Measure.**

**Contain.**

**Synthesize.**

**Govern.**

**Revalidate.**

**Preserve.**
