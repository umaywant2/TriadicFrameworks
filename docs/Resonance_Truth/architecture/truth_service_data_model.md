# RTT Resonance Truth Service — Data Model

**Module:** Resonance Truth  
**Artifact:** Logical Data Model  
**Framework:** Resonance-Time Theory (RTT)  
**Status:** Research Architecture / Reference Model  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This document defines the logical data model for the RTT Resonance Truth Service.

The conceptual architecture is defined in:

    truth_service_architecture.md

Functional component responsibilities are defined in:

    truth_service_components.md

The machine-facing contract is defined in:

    truth_service_api.yaml

Machine-readable object schemas are maintained under:

    ../schemas/

This document focuses on the persistent structural question:

> **What information must exist, and what relationships must be preserved, for a qualified Truth State to remain inspectable, explainable, and revalidatable?**

The model is intentionally storage-neutral.

It may eventually be implemented using:

- relational storage
- document storage
- graph storage
- event-oriented storage
- hybrid persistence

The logical model should remain stable independently of those implementation choices.

---

# 1. Data-Model Principles

The model follows several architectural rules.

## 1.1 Claims Are Not Truth States

A Claim represents an assertion.

A Truth State represents the result of evaluating that assertion.

    CLAIM ≠ TRUTH_STATE

The model should never require a Claim row or object to carry its current truth as an intrinsic property.

---

## 1.2 Observations Are Evidence

An Observation represents evidence associated with a Claim.

    OBSERVATION ≠ TRUTH_STATE

Observations may be:

- qualified
- degraded
- rejected
- expired
- indeterminate

without being deleted.

---

## 1.3 Evaluations Are Immutable Events

An Evaluation records the structural conditions under which a Truth State was produced.

A later Revalidation creates:

    new Evaluation
        ↓
    new Truth State

rather than rewriting historical evaluation results.

---

## 1.4 Truth States Are Regime-Qualified

Every evaluated Truth State belongs to a Regime.

A Truth State without an identifiable Regime is structurally incomplete.

---

## 1.5 Lineage Is First-Class

Lineage must be represented explicitly enough to reconstruct:

- where evidence originated
- which Sources participated
- which Anchors were referenced
- which transformations occurred
- which dependencies exist
- where Lineage is incomplete

---

## 1.6 Contradiction Is Preserved

Paradox and dissent should be modeled explicitly.

Conflicting qualified evidence should not disappear merely because a Truth State was synthesized.

---

## 1.7 Null May Be Meaningful

The model should distinguish:

    unknown

from:

    zero

and:

    no accepted value

from:

    false

For example:

    truth_state.status:
      indeterminate

    truth_state.accepted_value:
      null

is a valid result.

---

## 1.8 Domain Values Remain Domain-Native

Temporal Truth, Identity Truth, State Truth, and Lineage Truth do not necessarily share a useful scalar representation.

The data model should permit domain-specific Observation and accepted values without forcing them into one universal numeric field.

---

# 2. Core Entity Model

The primary logical entities are:

    Claim
    TruthClass
    Observation
    Source
    Anchor
    Lineage
    Regime
    Evaluation
    Qualification
    CoherenceState
    CoherenceCluster
    DriftState
    Paradox
    TruthState
    CorrectionPolicy
    RevalidationEvent

Their high-level relationships are:

    ┌───────────────┐
    │    REGIME     │
    └───────┬───────┘
            │
            │ qualifies
            ▼
    ┌───────────────┐
    │  EVALUATION   │◄──────────────┐
    └───────┬───────┘               │
            │                       │
            │ evaluates             │
            ▼                       │
    ┌───────────────┐               │
    │     CLAIM     │               │
    └───────┬───────┘               │
            │                       │
            │ has                   │
            ▼                       │
    ┌───────────────┐               │
    │ OBSERVATIONS  │               │
    └───────┬───────┘               │
            │                       │
       ┌────┴────┐                  │
       │         │                  │
       ▼         ▼                  │
    SOURCE    LINEAGE               │
       │         │                  │
       ▼         │                  │
    ANCHOR ◄─────┘                  │
                                    │
    EVALUATION                      │
       │                            │
       ├── Qualification            │
       ├── CoherenceState           │
       ├── DriftState               │
       ├── Paradox                  │
       │                            │
       ▼                            │
    TRUTH_STATE                     │
       │                            │
       ├── CorrectionPolicy         │
       └── RevalidationEvent ───────┘

---

# 3. Relationship Summary

| Entity | Primary Relationship |
|---|---|
| Claim | has one or more Truth Classes and zero or more Observations |
| TruthClass | classifies one or more dimensions of a Claim |
| Observation | belongs to a Claim and originates from a Source |
| Source | may derive from or reference an Anchor |
| Anchor | defines a bounded reference |
| Lineage | describes provenance and transformation relationships |
| Regime | defines operational Evaluation conditions |
| Evaluation | evaluates one Claim under one Regime |
| Qualification | records Observation eligibility within an Evaluation |
| CoherenceState | describes structural agreement within an Evaluation |
| CoherenceCluster | groups compatible qualified Observations |
| DriftState | describes displacement detected during Evaluation |
| Paradox | preserves qualified unresolved contradiction |
| TruthState | records the synthesized Evaluation result |
| CorrectionPolicy | governs possible downstream reaction |
| RevalidationEvent | causes or records reevaluation of a prior Truth State |

---

# 4. Identifier Strategy

Every persistent entity should have a stable identifier.

Examples:

    claim-temporal-001
    observation-ntp-a-001
    source-ntp-a
    anchor-utc
    regime-display-clock
    evaluation-001
    truth-state-001
    paradox-001

Identifiers should be:

- stable
- opaque to application logic where possible
- unique within their entity domain
- persistent across retrieval operations

Semantic meaning should not depend on parsing an identifier.

The readable examples above are intended for fixtures and documentation.

Production implementations may use another identifier strategy.

---

# 5. Claim

## Purpose

A Claim represents the statement being evaluated.

It answers:

> **What is being asserted?**

## Fields

| Field | Required | Description |
|---|---:|---|
| `claim_id` | Yes | Stable Claim identifier |
| `statement` | Yes | Original assertion |
| `truth_classes` | Yes | One or more Truth Classes |
| `intended_use` | No | Operational purpose of the evaluation |
| `external_reference` | No | External identifier or reference |
| `status` | Yes | Registration lifecycle state |
| `created_at` | Yes | Claim registration time |
| `updated_at` | Yes | Latest Claim metadata update |
| `metadata` | No | Non-canonical additional data |

## Claim Status

Initial states:

    registered
    active
    archived

These are Claim-record lifecycle states.

They are not Truth States.

## Example

    claim_id: claim-temporal-001
    statement: "The current reference time is 09:00:00 UTC."
    truth_classes:
      - temporal
    intended_use: "Synchronize a low-consequence display clock."
    status: active

---

# 6. TruthClass

## Purpose

TruthClass identifies the operational dimensions participating in Claim evaluation.

## Values

Initial canonical values:

    temporal
    locational
    identity
    integrity
    authority
    state
    transactional
    intent
    observational
    lineage

## Cardinality

A Claim:

    MUST have >= 1 TruthClass

and:

    MAY have > 1 TruthClass

Example:

    claim:
      "This TLS certificate is valid."

    truth_classes:
      - identity
      - integrity
      - authority
      - temporal
      - lineage

Truth Classes should not be treated as mutually exclusive categories.

---

# 7. Observation

## Purpose

An Observation represents evidence associated with a Claim.

It answers:

> **What was observed?**

## Fields

| Field | Required | Description |
|---|---:|---|
| `observation_id` | Yes | Stable Observation identifier |
| `claim_id` | Yes | Associated Claim |
| `source_id` | Yes | Producing Source |
| `anchor_id` | No | Directly associated Anchor if applicable |
| `value` | Yes | Domain-native observed value |
| `observed_at` | Yes | Time at which the observation was made |
| `received_at` | No | Time received by the Truth Service |
| `expires_at` | No | Explicit freshness boundary |
| `declared_confidence` | No | Confidence supplied by Observation producer |
| `integrity` | No | Integrity information |
| `lineage` | No | Supplied Lineage information |
| `qualification` | No | Latest or contextual qualification result |
| `registered_at` | Yes | Registration time |
| `metadata` | No | Domain-specific metadata |

## Important Constraint

Producer-declared confidence is Source data.

It should not automatically become:

    Truth Service confidence

## Temporal Example

    observation_id: obs-ntp-a
    claim_id: claim-temporal-001
    source_id: source-ntp-a
    anchor_id: anchor-utc

    value:
      timestamp: "2026-11-17T09:00:00.014Z"
      offset_ms: 14.0
      delay_ms: 21.7
      jitter_ms: 1.8
      dispersion_ms: 3.1

    observed_at: "2026-11-17T09:00:00.014Z"

---

# 8. Source

## Purpose

A Source represents an entity capable of producing Observations.

It answers:

> **Who or what supplied this evidence?**

## Fields

| Field | Required | Description |
|---|---:|---|
| `source_id` | Yes | Stable Source identifier |
| `name` | Yes | Human-readable Source name |
| `source_type` | Yes | Domain-specific Source classification |
| `anchor_id` | No | Associated Anchor |
| `lineage_distance` | No | Structural distance from relevant Anchor |
| `independence` | No | Relationship to other Sources |
| `domain` | No | Source domain |
| `status` | Yes | Current Source state |
| `valid_from` | No | Beginning of validity |
| `valid_until` | No | End of validity |
| `created_at` | Yes | Registration time |
| `updated_at` | Yes | Latest update time |
| `metadata` | No | Domain-specific information |

## Source Status

Initial states:

    active
    degraded
    unavailable
    rejected
    unknown

## Independence

Initial classifications:

    independent
    partially_dependent
    dependent
    unknown

## Design Constraint

A Source's existence does not imply its qualification.

Qualification is contextual to an Evaluation.

---

# 9. Anchor

## Purpose

An Anchor represents a bounded reference authority.

It answers:

> **Against which recognized reference may an Observation or Claim be evaluated?**

## Fields

| Field | Required | Description |
|---|---:|---|
| `anchor_id` | Yes | Stable Anchor identifier |
| `name` | Yes | Human-readable name |
| `anchor_type` | Yes | Domain-specific Anchor category |
| `authority` | Yes | Authority responsible for the Anchor |
| `domain` | Yes | Applicable operational domain |
| `regime_ids` | No | Regimes recognizing the Anchor |
| `status` | Yes | Current Anchor state |
| `valid_from` | No | Validity start |
| `valid_until` | No | Validity end |
| `revocation_reference` | No | Revocation or replacement information |
| `limitations` | No | Explicit bounded limitations |
| `created_at` | Yes | Registration time |
| `updated_at` | Yes | Latest update time |
| `metadata` | No | Domain-specific information |

## Anchor Status

Initial states:

    active
    degraded
    withdrawn
    revoked
    unknown

## Architectural Constraint

    Authority ≠ Universal Correctness

Anchor authority always remains bounded by domain and Regime.

---

# 10. Lineage

## Purpose

Lineage represents the provenance path through which evidence arrived at its current state.

It answers:

> **Where did this come from, and what happened to it along the way?**

Lineage is logically a graph.

## Lineage Node

A node may represent:

- Anchor
- Source
- Observation
- transformation
- Claim
- Evaluation
- Truth State
- external entity

### Fields

| Field | Required | Description |
|---|---:|---|
| `node_id` | Yes | Graph node identifier |
| `entity_type` | Yes | Logical entity type |
| `entity_id` | Yes | Referenced entity |
| `label` | No | Human-readable label |
| `metadata` | No | Additional provenance metadata |

## Lineage Edge

An edge represents a relationship between nodes.

### Fields

| Field | Required | Description |
|---|---:|---|
| `edge_id` | Yes | Graph edge identifier |
| `from_node_id` | Yes | Origin node |
| `to_node_id` | Yes | Destination node |
| `relation` | Yes | Relationship type |
| `transformation` | No | Transformation applied during the relationship |

## Example

    Anchor UTC
        │
        ▼
    NTP Source A
        │
        ▼
    Observation A
        │
        ▼
    Evaluation 1
        │
        ▼
    Truth State 1

## Incomplete Lineage

The model must permit:

    complete: false

with:

    gaps:
      - missing upstream dependency

The model must not invent missing Lineage.

---

# 11. Lineage Distance

## Purpose

Lineage Distance generalizes the NTP concept of distance from a reference hierarchy.

It does not imply that every truth system has literal strata.

## Representation

A Source may carry:

    lineage_distance: integer | null

A Truth State may also retain derived Lineage references containing:

- Source
- Anchor
- hop count
- transformation count
- completeness

## Principle

> **Distance from reference is itself truth metadata.**

Increasing distance does not automatically imply falsehood.

It indicates additional structure through which evidence has passed.

---

# 12. Regime

## Purpose

A Regime defines the operational conditions under which an Evaluation occurs.

It answers:

> **Under which constraints is this Truth State intended to be usable?**

## Fields

| Field | Required | Description |
|---|---:|---|
| `regime_id` | Yes | Stable Regime identifier |
| `name` | Yes | Human-readable name |
| `domain` | Yes | Operational domain |
| `description` | No | Regime description |
| `jurisdiction` | No | Applicable jurisdiction |
| `policy_version` | No | Policy revision |
| `observer_context` | No | Observer position/context |
| `applicable_scope` | No | Explicit scope boundaries |
| `precision_requirement` | No | Domain precision requirement |
| `maximum_age_seconds` | No | Maximum Observation age |
| `minimum_independent_sources` | No | Required Source diversity |
| `consequence` | Yes | Consequence classification |
| `permitted_truth_statuses` | No | Truth States permitted for use |
| `correction_modes` | No | Allowed Correction modes |
| `created_at` | Yes | Creation time |
| `updated_at` | Yes | Latest update |
| `metadata` | No | Domain-specific information |

## Consequence

Initial levels:

    informational
    low
    moderate
    high
    critical

## Example

    regime_id: regime-display-clock
    name: Low-consequence display clock
    domain: temporal
    maximum_age_seconds: 300
    consequence: low

The same Observations may produce a different operational result under a stricter Regime.

---

# 13. Evaluation

## Purpose

An Evaluation records one attempt to determine a qualified Truth State for one Claim under one Regime.

It answers:

> **What happened when this Claim was evaluated under these conditions?**

## Fields

| Field | Required | Description |
|---|---:|---|
| `evaluation_id` | Yes | Stable Evaluation identifier |
| `claim_id` | Yes | Evaluated Claim |
| `regime_id` | Yes | Governing Regime |
| `prior_truth_state_id` | No | Previous state used as historical context |
| `input_observation_ids` | Yes | Candidate Observations |
| `qualification_results` | Yes | Observation Qualification results |
| `selected_observation_ids` | No | Observations used in synthesis |
| `excluded_observation_ids` | No | Observations not used |
| `coherence_state_id` | Yes | Coherence result |
| `drift_state_id` | Yes | Drift result |
| `paradox_ids` | No | Registered Paradoxes |
| `synthesis_rationale` | Yes | Why the result was produced |
| `truth_state_id` | Yes | Resulting Truth State |
| `evaluated_at` | Yes | Evaluation time |
| `evaluator_version` | Yes | Evaluation implementation/version |
| `metadata` | No | Additional metadata |

## Immutability

Once completed:

    Evaluation N

should not be rewritten into:

    Evaluation N'

because new evidence appeared.

Instead:

    Evaluation N
        ↓
    Truth State N
        ↓
    New Evidence
        ↓
    Evaluation N+1
        ↓
    Truth State N+1

This preserves decision history.

---

# 14. Qualification

## Purpose

Qualification records whether an Observation was suitable for one Evaluation.

Qualification is contextual.

It should not be modeled solely as an intrinsic permanent property of the Observation.

## Fields

| Field | Required | Description |
|---|---:|---|
| `evaluation_id` | Yes | Evaluation context |
| `observation_id` | Yes | Evaluated Observation |
| `status` | Yes | Qualification outcome |
| `reasons` | Yes | Structured rationale |
| `freshness_seconds` | No | Observation age |
| `source_independence` | No | Independence classification |
| `regime_compatible` | No | Regime compatibility |
| `precision_compatible` | No | Precision compatibility |
| `integrity_valid` | No | Integrity status |
| `evaluated_at` | Yes | Qualification time |

## Qualification Status

Initial values:

    qualified
    degraded
    rejected
    expired
    indeterminate

## Recommended Logical Key

Conceptually:

    evaluation_id + observation_id

uniquely identifies the Qualification decision for an Observation within an Evaluation.

---

# 15. DecisionReason

## Purpose

DecisionReason provides structured explanation for architectural decisions.

It is used by:

- Qualification
- Coherence
- Drift
- synthesis
- Correction
- potentially Regime resolution

## Fields

| Field | Required | Description |
|---|---:|---|
| `code` | Yes | Stable reason identifier |
| `message` | Yes | Human-readable explanation |
| `evidence_references` | No | Supporting entities/evidence |
| `regime_rule` | No | Applicable Regime rule |

## Example

    code: OBSERVATION_STALE
    message: Observation exceeds the maximum age permitted by the Regime.
    evidence_references:
      - obs-ntp-a
      - regime-display-clock
    regime_rule: maximum_age_seconds

## Principle

Important decisions should not be represented as unexplained booleans.

---

# 16. CoherenceState

## Purpose

CoherenceState records the structural agreement condition among qualified Observations.

## Fields

| Field | Required | Description |
|---|---:|---|
| `coherence_state_id` | Yes | Stable identifier |
| `evaluation_id` | Yes | Evaluation context |
| `status` | Yes | Coherence classification |
| `cluster_ids` | No | Related Coherence clusters |
| `supporting_observation_ids` | No | Supporting Observations |
| `dissenting_observation_ids` | No | Dissenting Observations |
| `rationale` | Yes | Structured explanation |

## Coherence Status

Initial values:

    coherent
    weakly_coherent
    fragmented
    contested
    inverted
    indeterminate

## Principle

Coherence is not a simple count of matching Observations.

Lineage and Source independence may influence interpretation.

---

# 17. CoherenceCluster

## Purpose

A CoherenceCluster groups qualified Observations that form a mutually compatible field.

## Fields

| Field | Required | Description |
|---|---:|---|
| `cluster_id` | Yes | Stable cluster identifier |
| `evaluation_id` | Yes | Evaluation context |
| `observation_ids` | Yes | Member Observations |
| `source_ids` | No | Participating Sources |
| `classification` | Yes | Cluster role |
| `representative_value` | No | Optional domain-native representative value |
| `independence` | No | Structural independence estimate |
| `rationale` | No | Cluster rationale |

## Cluster Classification

Initial values:

    supporting
    dissenting
    outlier
    unresolved

## Example

    cluster_id: cluster-a

    observation_ids:
      - obs-a
      - obs-b

    classification:
      supporting

A separate cluster may remain visible:

    cluster_id: cluster-b

    observation_ids:
      - obs-c

    classification:
      dissenting

The second cluster does not disappear merely because the first was selected.

---

# 18. DriftState

## Purpose

DriftState records displacement identified during an Evaluation.

## Fields

| Field | Required | Description |
|---|---:|---|
| `drift_state_id` | Yes | Stable Drift identifier |
| `evaluation_id` | Yes | Evaluation context |
| `magnitude` | No | Numeric magnitude when meaningful |
| `unit` | No | Measurement unit |
| `direction` | Yes | Direction classification |
| `dimensions` | Yes | One or more Drift dimensions |
| `bounded` | No | Whether Drift remains within Regime constraints |
| `baseline_reference` | No | State used as baseline |
| `local_value` | No | Local/prior state |
| `observed_value` | No | Qualified observed state |
| `rationale` | Yes | Structured explanation |

## Drift Dimensions

Initial values:

    value
    semantic
    source
    lineage
    temporal
    regime
    confidence
    policy

## Direction

Initial values:

    increasing
    decreasing
    stable
    oscillating
    unknown

## Numeric Example

    magnitude: 14
    unit: milliseconds
    dimensions:
      - temporal
    bounded: true

## Structural Example

    magnitude: null
    unit: null
    dimensions:
      - semantic
      - regime
    direction: unknown
    bounded: null

The latter is intentionally valid.

---

# 19. Paradox

## Purpose

Paradox preserves qualified contradiction that cannot yet be safely collapsed.

## Fields

| Field | Required | Description |
|---|---:|---|
| `paradox_id` | Yes | Stable Paradox identifier |
| `evaluation_id` | Yes | Evaluation context |
| `type` | Yes | Paradox type |
| `competing_observation_ids` | Yes | Conflicting Observations |
| `competing_cluster_ids` | No | Conflicting Coherence clusters |
| `regime_ids` | No | Related Regimes |
| `description` | Yes | Human-readable description |
| `resolution_condition` | No | Condition required for resolution |
| `containment` | Yes | Current containment strategy |
| `status` | Yes | Paradox lifecycle state |

## Types

    structural
    semantic
    regime

## Containment

    preserve
    isolate
    separate_by_regime
    escalate
    resolved

## Status

    active
    contained
    escalated
    resolved

## Principle

    CONTRADICTION
         ↓
    PRESERVE
         ↓
    CHARACTERIZE
         ↓
    CONTAIN
         ↓
    RESOLVE IF JUSTIFIED

not:

    CONTRADICTION
         ↓
    DELETE LOSING VALUE

---

# 20. TruthState

## Purpose

TruthState is the primary synthesized output of an Evaluation.

It answers:

> **What operational state can presently be supported?**

## Fields

| Field | Required | Description |
|---|---:|---|
| `truth_state_id` | Yes | Stable Truth-State identifier |
| `claim_id` | Yes | Associated Claim |
| `evaluation_id` | Yes | Producing Evaluation |
| `supersedes_truth_state_id` | No | Prior Truth State |
| `status` | Yes | Current Truth-State status |
| `accepted_value` | No | Domain-native accepted value |
| `regime_id` | Yes | Governing Regime |
| `truth_classes` | Yes | Applicable Truth Classes |
| `anchor_ids` | No | Participating Anchors |
| `source_ids` | No | Participating Sources |
| `observation_ids` | No | Participating Observations |
| `lineage_references` | Yes | Provenance summary |
| `coherence_state_id` | Yes | Coherence result |
| `drift_state_id` | Yes | Drift result |
| `paradox_ids` | No | Unresolved Paradoxes |
| `uncertainty` | No | Explicit uncertainty information |
| `permitted_uses` | No | Allowed operational uses |
| `prohibited_uses` | No | Disallowed operational uses |
| `correction_policy_id` | Yes | Associated Correction Policy |
| `evaluated_at` | Yes | Evaluation time |
| `expires_at` | No | Expiration time |
| `next_revalidation_at` | No | Scheduled reevaluation |
| `revalidation_triggers` | No | Event-based reevaluation conditions |
| `metadata` | No | Additional metadata |

## Truth Status

Initial states:

    declared
    observed
    corroborated
    operationally_accepted
    contested
    degraded
    held_over
    expired
    rejected
    indeterminate

## Null Accepted Value

The following states may legitimately carry:

    accepted_value: null

Examples include:

    contested
    rejected
    expired
    indeterminate

No boolean substitute is required.

---

# 21. Truth-State History

Truth States form an append-oriented history.

Example:

    Truth State 1
      status: operationally_accepted
          │
          ▼
    Truth State 2
      status: degraded
          │
          ▼
    Truth State 3
      status: held_over
          │
          ▼
    Truth State 4
      status: operationally_accepted

Each later state may contain:

    supersedes_truth_state_id

The chain enables reconstruction of:

- changes in evidence
- Drift
- Source availability
- Regime changes
- Correction decisions
- Revalidation outcomes

---

# 22. UncertaintyDescriptor

## Purpose

UncertaintyDescriptor represents known limits on Truth-State acceptance without requiring false numeric precision.

## Fields

| Field | Required | Description |
|---|---:|---|
| `classification` | Yes | Qualitative classification |
| `numeric_value` | No | Numeric value where meaningful |
| `unit` | No | Unit for numeric uncertainty |
| `rationale` | Yes | Explanation |

## Classification

Initial values:

    low
    moderate
    high
    unknown
    not_applicable

## Principle

A numeric uncertainty field should be populated only where the domain provides a defensible measurement.

---

# 23. CorrectionPolicy

## Purpose

CorrectionPolicy defines the permitted downstream response to a Truth State.

It answers:

> **How may local operational state respond to this evaluation?**

## Fields

| Field | Required | Description |
|---|---:|---|
| `correction_policy_id` | Yes | Stable Policy identifier |
| `truth_state_id` | Yes | Associated Truth State |
| `mode` | Yes | Correction mode |
| `reason` | Yes | Rationale |
| `maximum_adjustment` | No | Maximum permitted adjustment |
| `adjustment_unit` | No | Adjustment unit |
| `requires_approval` | Yes | Whether external approval is required |
| `approval_authority` | No | Required authority |
| `downstream_constraints` | No | Additional constraints |

## Correction Modes

Initial values:

    none
    step
    gradual
    quarantine
    dual_state
    human_escalation
    holdover
    fail_closed
    fail_bounded

## Principle

Correction remains downstream of Evaluation.

    Truth State
        ↓
    Correction Policy

not:

    Correction Preference
        ↓
    Desired Truth State

---

# 24. RevalidationEvent

## Purpose

RevalidationEvent records why and when a previously evaluated Truth State is challenged again.

## Fields

| Field | Required | Description |
|---|---:|---|
| `revalidation_event_id` | Yes | Stable identifier |
| `truth_state_id` | Yes | Truth State being challenged |
| `trigger` | Yes | Revalidation trigger |
| `triggered_at` | Yes | Trigger time |
| `requested_by` | No | Actor/system requesting reevaluation |
| `new_evaluation_id` | No | Resulting Evaluation |
| `metadata` | No | Additional information |

## Triggers

Initial values:

    elapsed_time
    expiration
    source_change
    anchor_change
    regime_change
    contradictory_observation
    excessive_drift
    reduced_source_diversity
    policy_change
    manual_challenge

## Relationship

    Truth State N
        ↓
    Revalidation Event
        ↓
    Evaluation N+1
        ↓
    Truth State N+1

---

# 25. Holdover

Holdover does not require a separate core entity in the initial model.

It is represented through:

    TruthState.status:
      held_over

combined with:

- prior Truth State
- Source status
- Drift
- uncertainty
- Regime
- expiration
- permitted uses
- Correction Policy

If later crosswalks demonstrate that Holdover requires additional independent lifecycle behavior, it may become a dedicated object.

The initial model should avoid creating entities before structural need is demonstrated.

---

# 26. IntegrityDescriptor

## Purpose

IntegrityDescriptor preserves optional evidence about Observation integrity.

Potential fields include:

- algorithm
- digest
- signature reference
- verification result
- verification time

## Example

    integrity:
      algorithm: SHA-256
      digest: "..."
      verified: true
      verified_at: "..."

Integrity information is evidence.

It does not automatically establish the Truth State of the associated Claim.

---

# 27. Metadata

Most major entities permit optional metadata.

Metadata exists for:

- domain-specific extensions
- implementation annotations
- fixture information
- diagnostic context

## Critical Rule

Metadata must not silently override canonical fields.

For example:

    metadata:
      truth_status: operationally_accepted

must not override:

    truth_state.status

Likewise:

    metadata:
      regime: trusted

must not replace the canonical:

    regime_id

Metadata is extension data, not an alternate control plane.

---

# 28. Runtime Referential Relationships

The minimum logical references are:

    Claim
      1 ───── * Observation

    Claim
      1 ───── * Evaluation

    Claim
      * ───── * TruthClass

    Observation
      * ───── 1 Source

    Observation
      * ───── 0..1 Anchor

    Source
      * ───── 0..1 Anchor

    Evaluation
      * ───── 1 Regime

    Evaluation
      1 ───── * Qualification

    Evaluation
      1 ───── 1 CoherenceState

    CoherenceState
      1 ───── * CoherenceCluster

    Evaluation
      1 ───── 1 DriftState

    Evaluation
      1 ───── * Paradox

    Evaluation
      1 ───── 1 TruthState

    TruthState
      1 ───── 1 CorrectionPolicy

    TruthState
      1 ───── * RevalidationEvent

    TruthState
      0..1 ─── 0..1 prior TruthState

These cardinalities are initial design assumptions.

Later crosswalks may reveal cases requiring refinement.

---

# 29. Evaluation Snapshot Principle

An Evaluation should preserve the structural state used at evaluation time.

Suppose a Source later changes from:

    active

to:

    revoked

Historical Evaluation 1 should still be able to show:

> At the time of Evaluation 1, Source A was treated as active under the then-current Regime and Source record.

The current state may then trigger:

    source_change
        ↓
    Revalidation Event
        ↓
    Evaluation 2

The model should therefore distinguish:

- present Source state
- Source state relevant to historical Evaluation

Implementation options may include:

- snapshots
- entity version references
- append-only change records
- event history

The logical requirement is preservation of historical interpretability.

---

# 30. Versioning

At minimum, implementations should preserve versions for:

- evaluator logic
- Regime policies
- schemas
- externally governed Anchors where relevant

## Evaluation Version

Each Evaluation should preserve:

    evaluator_version

This allows two Evaluations to be distinguished when evaluation logic changes.

## Regime Version

Where policy matters:

    regime.policy_version

should identify which policy revision governed the Evaluation.

## Schema Version

Serialized artifacts should eventually identify the schema revision against which they were validated.

This may be carried externally or in a canonical envelope.

The specific implementation mechanism remains open.

---

# 31. Temporal Modeling

Time appears in several structurally different roles.

The model should not collapse them.

## Observation Time

    observed_at

When the Source observed the state.

## Receipt Time

    received_at

When the Truth Service received the Observation.

## Evaluation Time

    evaluated_at

When the Evaluation occurred.

## Expiration Time

    expires_at

When the Observation or Truth State ceases to satisfy a declared freshness condition.

## Revalidation Time

    next_revalidation_at

When the Truth State should be challenged again.

These fields may differ significantly.

That difference is itself potentially meaningful.

---

# 32. Research Plane Data Model

The research scoring model remains separate from runtime truth evaluation.

Primary research entities include:

    ReferenceSystem
    Crosswalk
    Criterion
    Score
    ScoreEvidence
    ComparativeProfile

The research plane asks:

> **How well does an operational system expose and govern its relationship to truth?**

It does not ask:

> **Is this runtime Claim true?**

---

# 33. ReferenceSystem

## Purpose

Represents a system studied as an operational truth reference architecture.

Initial examples:

    NTP
    DNS
    IAM
    PKI
    Policy / IAM
    Distributed Systems
    Ledgers
    Desired-State Systems
    Telemetry
    Supply-Chain Provenance

## Suggested Fields

| Field | Required | Description |
|---|---:|---|
| `system_id` | Yes | Stable research identifier |
| `name` | Yes | Reference-system name |
| `primary_truth_class` | Yes | Primary Truth Class |
| `crosswalk_reference` | No | Crosswalk document |
| `status` | No | Research lifecycle state |
| `metadata` | No | Additional research metadata |

---

# 34. Score

## Purpose

A Score evaluates one criterion for one Reference System.

## Fields

| Field | Required | Description |
|---|---:|---|
| `criterion` | Yes | Scoring criterion |
| `value` | Yes | Score from 0–5 |
| `rationale` | Yes | Explanation |
| `evidence` | Yes | One or more supporting evidence records |

## Criteria

Initial dimensions:

    anchor_quality
    lineage_visibility
    observation_quality
    coherence_detection
    drift_detection
    paradox_handling
    regime_awareness
    freshness_revalidation
    correction_discipline
    failure_transparency

## Principle

    SCORE WITHOUT RATIONALE
        =
    STRUCTURALLY INCOMPLETE SCORE

No naked numbers.

---

# 35. ScoreEvidence

## Purpose

ScoreEvidence records the basis supporting a research score.

## Suggested Fields

| Field | Required | Description |
|---|---:|---|
| `description` | Yes | Evidence description |
| `reference` | No | Source/reference identifier |
| `evidence_type` | Yes | Evidence classification |

## Evidence Types

Initial values:

    specification
    implementation
    documentation
    test
    observation
    analysis

Research evidence remains conceptually distinct from runtime Observation evidence.

---

# 36. Research Score Profile

The ten scoring dimensions produce a structural profile.

Example:

    NTP

    Anchor Quality             5
    Lineage Visibility        4
    Observation Quality       5
    Coherence Detection       5
    Drift Detection           5
    Paradox Handling          4
    Regime Awareness          3
    Freshness/Revalidation    5
    Correction Discipline     5
    Failure Transparency      5

The above values are illustrative only.

Actual scores should be assigned after evidence review.

The important data-model requirement is preservation of the complete profile rather than only a total score.

---

# 37. RTT Meta-Score Representation

The research profile may be aggregated into five RTT meta-dimensions:

    Reference
    Observation
    Coherence
    Drift
    Regime

Each dimension ranges:

    0–10

Mappings are:

| Meta-Dimension | Criteria |
|---|---|
| Reference | Anchor Quality + Lineage Visibility |
| Observation | Observation Quality + Freshness/Revalidation |
| Coherence | Coherence Detection + Paradox Handling |
| Drift | Drift Detection + Correction Discipline |
| Regime | Regime Awareness + Failure Transparency |

The meta-score is a research representation.

It must not enter runtime Truth-State synthesis.

---

# 38. Runtime Plane vs Research Plane

The separation is:

    RUNTIME PLANE                  RESEARCH PLANE
    ─────────────                  ──────────────

    Claim                          ReferenceSystem
    Observation                    Crosswalk
    Source                         Criterion
    Anchor                         Score
    Lineage                        ScoreEvidence
    Regime                         ComparativeProfile
    Evaluation
    Qualification
    CoherenceState
    DriftState
    Paradox
    TruthState
    CorrectionPolicy
    RevalidationEvent

There should be no runtime dependency such as:

    TruthState
        ↓
    ReferenceSystemScore

The planes may share vocabulary.

They should not share decision authority.

---

# 39. Minimal NTP Fixture Model

The first implementation may use a compact object graph:

    Claim
      │
      ├── Observation A ── Source A ──┐
      ├── Observation B ── Source B ──┼── Anchor UTC
      └── Observation C ── Source C ──┘
      │
      ▼
    Evaluation
      │
      ├── Qualification A
      ├── Qualification B
      ├── Qualification C
      ├── CoherenceState
      ├── DriftState
      └── Paradox[]
      │
      ▼
    TruthState
      │
      ├── CorrectionPolicy
      └── RevalidationEvent[]

This is sufficient for the initial deterministic NTP fixture set:

- coherent
- minor drift
- outlier
- fragmented
- stale
- indeterminate

---

# 40. Coherent Fixture Shape

A coherent NTP-like fixture may contain:

    Claim:
      temporal

    Regime:
      low-consequence display

    Anchor:
      UTC reference

    Sources:
      A
      B
      C

    Observations:
      A → offset 12 ms
      B → offset 15 ms
      C → offset 14 ms

    Qualifications:
      A → qualified
      B → qualified
      C → qualified

    Coherence:
      coherent

    Drift:
      bounded

    Paradox:
      none material

    TruthState:
      operationally_accepted

    Correction:
      gradual

    Revalidation:
      scheduled

The fixture should preserve the full object relationships rather than only the expected result.

---

# 41. Fragmented Fixture Shape

A fragmented fixture may produce:

    Sources:
      A
      B
      C
      D

    Observations:
      A → X
      B → X
      C → Y
      D → Y

    Coherence:
      fragmented

    Clusters:
      cluster-X:
        A
        B

      cluster-Y:
        C
        D

    Paradox:
      active

    TruthState:
      contested

    accepted_value:
      null

The model preserves both clusters.

Nothing requires the service to select one merely to populate `accepted_value`.

---

# 42. Indeterminate Fixture Shape

An indeterminate fixture may contain:

    Observations:
      A → expired
      B → rejected
      C → indeterminate

    selected_observations:
      []

    Coherence:
      indeterminate

    Drift:
      unknown

    TruthState:
      indeterminate

    accepted_value:
      null

Again:

    INDETERMINATE

is a valid successful model state.

---

# 43. Data Integrity Rules

The initial model should enforce or validate the following constraints.

## Rule 1

Every Observation belongs to exactly one Claim.

## Rule 2

Every Observation identifies a Source.

## Rule 3

Every Evaluation identifies one Claim and one Regime.

## Rule 4

Every completed Evaluation produces one Truth State.

## Rule 5

Every Qualification belongs to one Evaluation and one Observation.

## Rule 6

Every Truth State identifies its producing Evaluation.

## Rule 7

Every Correction Policy belongs to one Truth State.

## Rule 8

Every Revalidation Event identifies the Truth State being challenged.

## Rule 9

Paradoxes must reference competing evidence or clusters.

## Rule 10

A Truth State may have a null `accepted_value`.

## Rule 11

Research scores must contain rationale and evidence.

## Rule 12

Research scores must not influence runtime Evaluation.

---

# 44. Deletion and Retention

The initial architecture favors preservation over destructive deletion for Evaluation artifacts.

Particularly sensitive historical entities include:

- Evaluations
- Qualifications
- Coherence States
- Drift States
- Paradoxes
- Truth States
- Revalidation Events

If implementation requirements demand logical deletion, retention policy, or privacy-driven erasure, those mechanisms should preserve as much structural audit integrity as legally and operationally permitted.

Retention policy itself is outside the current canonical model and should be introduced explicitly rather than assumed.

---

# 45. Storage-Neutral Implementation Guidance

The logical model intentionally avoids requiring one storage technology.

## Relational Representation

Suitable for:

- strong entity relationships
- Evaluation history
- constraints
- structured querying

## Document Representation

Suitable for:

- Evaluation snapshots
- Truth-State serialization
- fixture storage
- domain-native Observation values

## Graph Representation

Suitable for:

- Lineage
- dependency analysis
- Source relationships
- Anchor paths

## Event Representation

Suitable for:

- Source changes
- Anchor revocation
- Revalidation triggers
- Truth-State lifecycle reconstruction

A production implementation may combine these.

The architecture should choose storage technology after access patterns become measurable.

---

# 46. Schema Boundary

The logical model defines meaning.

Machine-readable schemas define serialization and validation.

Therefore:

    Logical Data Model
            ↓
    Canonical Meaning
            ↓
    JSON Schemas
            ↓
    API Serialization
            ↓
    Implementation Storage

The direction should not be reversed.

Database convenience should not silently redefine canonical meaning.

---

# 47. Future Model Challenges

Later crosswalks are expected to challenge the current model.

## DNS May Challenge

- delegated authority
- caching
- observer-dependent answers
- negative answers
- namespace hierarchy

## IAM May Challenge

- subject identity
- credential state
- authentication context
- revocation

## PKI May Challenge

- trust chains
- validity intervals
- signature state
- multiple trust stores

## Distributed Systems May Challenge

- epochs
- quorum
- leadership
- competing state histories

## Ledgers May Challenge

- ordering
- settlement
- reversibility
- finality

## Desired-State Systems May Challenge

- intent vs actual state
- reconciliation loops

## Telemetry May Challenge

- partial observability
- sampling
- delayed evidence

## Supply-Chain Provenance May Challenge

- transformations
- artifact identity
- attestations
- dependency graphs

These challenges should refine the model only where crosswalk evidence demonstrates the need.

---

# 48. Promotion Rule

A newly discovered concept should become a core entity only when at least one of the following is true:

1. it has its own lifecycle
2. multiple existing entities depend upon it
3. it has independent identity
4. it must be referenced historically
5. collapsing it into another entity loses structurally important information
6. multiple Truth Classes demonstrate the same abstraction

Otherwise, the concept should begin as:

- an attribute
- a relationship
- an extension
- domain metadata
- a crosswalk-specific construct

This prevents entity proliferation.

---

# 49. Model Evolution Loop

The data model evolves through:

    REFERENCE SYSTEM
          ↓
    CROSSWALK
          ↓
    NEW STRUCTURAL NEED
          ↓
    REPRESENT WITH CURRENT MODEL?
          │
       ┌──┴──┐
      YES    NO
       │      │
       │      ▼
       │   CLASSIFY GAP
       │      │
       │      ├── Domain-Specific
       │      ├── Missing Attribute
       │      ├── Missing Relationship
       │      ├── Missing Entity
       │      └── Model Defect
       │
       ▼
    TEST AGAINST PRIOR CROSSWALKS
          ↓
    MODIFY IF JUSTIFIED
          ↓
    VERSION MODEL
          ↓
    REVALIDATE FIXTURES

The model should evolve through evidence rather than accumulation.

---

# 50. Initial Definition of Done

The initial logical data model is sufficient when it can represent all six NTP reference fixtures without special-case structural exceptions.

Those fixtures are:

1. coherent
2. minor drift
3. outlier
4. fragmented
5. stale
6. indeterminate

For every fixture, the model must preserve:

- Claim
- Truth Class
- Regime
- Anchor
- Sources
- Observations
- Lineage
- Qualification
- Coherence
- Drift
- Paradox where applicable
- Truth State
- Correction Policy
- Revalidation condition
- Evaluation history

The model must also be able to answer:

> **Why was this Truth State produced?**

using persisted relationships rather than reconstructed guesswork.

---

# 51. Canonical Data Flow

The complete logical data flow is:

    CLAIM
      │
      ├── TruthClass[]
      │
      ▼
    OBSERVATION[]
      │
      ├── Source
      │     │
      │     └── Anchor
      │
      └── Lineage
             │
             ▼
          EVALUATION
             │
             ├── Regime
             ├── Qualification[]
             ├── CoherenceState
             │     └── CoherenceCluster[]
             ├── DriftState
             └── Paradox[]
             │
             ▼
         TRUTH_STATE
             │
             ├── CorrectionPolicy
             └── RevalidationEvent[]
                        │
                        ▼
                   EVALUATION N+1

The cycle is append-oriented.

New evidence creates new evaluation context.

It does not erase the conditions under which earlier truth was accepted.

---

# 52. Governing Data Principle

> **Preserve enough structure that no Truth State becomes an unexplained answer.**

The data model must make it possible to move backward from:

    Truth State

to:

    Evaluation

to:

    Coherence
    Drift
    Paradox
    Qualification

to:

    Observations

to:

    Sources

to:

    Anchors

through:

    Lineage

within:

    Regime

The model therefore preserves not merely the result of truth evaluation, but the structural path by which that result became operationally usable.

---

# 53. Canonical Summary

The RTT Resonance Truth Service data model separates five fundamental things:

    ASSERTION
       ↓
    Claim

    EVIDENCE
       ↓
    Observation + Source + Anchor + Lineage

    CONTEXT
       ↓
    Regime

    EVALUATION
       ↓
    Qualification + Coherence + Drift + Paradox

    OPERATIONAL RESULT
       ↓
    Truth State + Correction + Revalidation

These distinctions are intentional.

The data model does not ask every object to carry truth.

It preserves the relationships necessary to explain how a Truth State emerged from evidence under bounded operational conditions.

**Claims are asserted.**

**Observations are gathered.**

**Sources are identified.**

**Anchors are bounded.**

**Lineage is preserved.**

**Regimes are declared.**

**Evidence is qualified.**

**Coherence is evaluated.**

**Drift is measured.**

**Paradox is retained.**

**Truth States are synthesized.**

**Correction is governed.**

**Revalidation continues the cycle.**
