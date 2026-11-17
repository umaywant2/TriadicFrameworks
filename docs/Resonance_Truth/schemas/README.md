# Resonance Truth — Schemas

> **Machine-readable contracts for the RTT Resonance Truth Service**

**Module:** Resonance Truth  
**Artifact:** Schema Index and Contract  
**Framework:** Resonance-Time Theory (RTT)  
**Status:** Reference Implementation / Schema Boundary  
**Current Fixture Contract:** v0.1  
**Consolidation Target:** v0.2  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This directory contains the machine-readable schemas used by the RTT Resonance Truth Service.

The schemas define serialization and validation contracts for the logical objects described in:

    ../architecture/truth_service_architecture.md
    ../architecture/truth_service_components.md
    ../architecture/truth_service_data_model.md

They support deterministic fixtures under:

    ../fixtures/

and behavioral validation under:

    ../tests/

The governing principle is:

> **The schemas represent the architecture. They do not define the architecture accidentally.**

The direction is:

    Crosswalk Evidence
          ↓
    Architecture
          ↓
    Logical Data Model
          ↓
    Schema
          ↓
    Fixture
          ↓
    Test
          ↓
    Implementation

not:

    convenient JSON shape
          ↓
    architecture by accident

---

# 1. Current Schema Set

The initial schema scaffold contains:

    claim.schema.json

    observation.schema.json

    source.schema.json

    anchor.schema.json

    lineage.schema.json

    regime.schema.json

    evaluation.schema.json

    truth_state.schema.json

    coherence_state.schema.json

    drift_state.schema.json

    paradox.schema.json

    correction_policy.schema.json

These schemas represent the original v0.1 Truth-Service model.

They remain useful for the initial deterministic NTP implementation.

---

# 2. v0.1 Compatibility Boundary

The first NTP fixtures intentionally use the v0.1 vocabulary.

Examples include:

    observations

    anchors

    sources

    lineage

    regime

    expected truth state

This is deliberate.

The first fixture family should remain small enough to validate:

    Qualification

    Coherence

    Drift

    Paradox

    Truth-State synthesis

    Correction

    Revalidation

without requiring the entire ten-crosswalk architecture to be implemented simultaneously.

Therefore:

> **v0.1 remains the compatibility boundary for the initial NTP fixture family.**

---

# 3. Why v0.2 Is Needed

The ten operational crosswalks challenged several assumptions in the original model.

The crosswalk sequence examined:

    NTP
      → Temporal Truth

    DNS
      → Locational Truth

    IAM
      → Identity Truth

    PKI
      → Integrity Truth

    Policy / Authorization
      → Authority Truth

    Distributed Systems
      → State Truth

    Transactional Systems
      → Transactional Truth

    Desired-State Systems
      → Intent Truth

    Telemetry
      → Observational Truth

    Supply-Chain Provenance
      → Lineage Truth

Repeated cross-system findings indicate that several original concepts need generalization.

The v0.2 consolidation should therefore evolve the schema model cautiously rather than simply adding fields to v0.1 objects.

---

# 4. Schema Design Principles

The schema layer follows several rules.

## 4.1 Meaning Before Shape

A field should exist because it represents a stable architectural concept.

It should not exist merely because it is convenient for one fixture.

---

## 4.2 Domain-Native Values

Schemas should permit Truth Classes to retain domain-native values.

Examples:

    Temporal:
      offset_ms

    Authority:
      permit / deny

    Transaction:
      committed / rolled_back

    Intent:
      converged / not_converged

The schema should not force these into one universal scalar.

---

## 4.3 Null Is Meaningful

The schemas must distinguish:

    unknown

from:

    false

and:

    zero

and:

    absent

Example:

    accepted_value:
      null

may be correct for:

    indeterminate
    contested
    expired

No fabricated value is required.

---

## 4.4 Evidence Is Preserved

Evidence rejected from one Evaluation should not need to be deleted.

Schemas should support:

    Evidence exists
      +
    Evidence excluded from synthesis

without conflating exclusion with falsehood.

---

## 4.5 History Is Append-Oriented

New Evidence or Revalidation should normally produce:

    new Evaluation
      ↓
    new Truth State

rather than rewriting prior Evaluations.

Schemas should preserve historical references.

---

## 4.6 Relationships Matter

The crosswalk series repeatedly demonstrated that operational Truth belongs to relationships.

Therefore schema design should preserve:

- provenance
- derivation
- delegation
- transformation
- comparison
- commitment
- materialization
- correction
- Revalidation

rather than storing only final values.

---

# 5. Core v0.1 Objects

The current v0.1 model centers on:

    Claim
    Observation
    Source
    Anchor
    Lineage
    Regime
    Evaluation
    CoherenceState
    DriftState
    Paradox
    TruthState
    CorrectionPolicy

This model is sufficient for the initial temporal fixture family.

It should not be mistaken for the final generalized object model.

---

# 6. Claim Schema

## File

    claim.schema.json

## Purpose

Represents the assertion being evaluated.

Core concerns include:

    claim_id
    statement
    truth_classes
    intended_use
    lifecycle metadata

A Claim is not itself a Truth State.

Canonical distinction:

    Claim
      ≠
    Truth State

---

# 7. Observation Schema

## File

    observation.schema.json

## Purpose

Represents observational Evidence in the v0.1 model.

Typical fields include:

    observation_id
    claim_id
    source_id
    anchor_id
    value
    observed_at
    received_at
    expires_at
    integrity
    lineage
    metadata

Observation remains important.

However:

> **Crosswalks #3–#10 demonstrate that Observation is too narrow to remain the universal generalized Evidence object.**

Therefore observation.schema.json should remain valid as a v0.1 object and likely become one specialization of a future Evidence model. 【1-721f7b】

---

# 8. Source Schema

## File

    source.schema.json

## Purpose

Represents an entity capable of producing Evidence.

Relevant concerns include:

    identity
    type
    reference relationship
    Lineage
    independence
    domain
    status
    validity

The crosswalks demonstrated that Source and Authority must remain separate.

Therefore:

    Source exists
      ≠
    Source authoritative

and:

    Source authoritative in one scope
      ≠
    Source authoritative everywhere

---

# 9. Anchor Schema

## File

    anchor.schema.json

## Purpose

Represents the v0.1 bounded reference abstraction.

NTP, DNS, and PKI strongly support Anchors.

However, later crosswalks demonstrated that operational reference may also arise from:

    policy
    protocol
    accepted history
    authorized declaration
    observation contract

Therefore:

> **Anchor should remain a valid specialized reference concept while v0.2 considers the broader ReferenceBasis abstraction.**

---

# 10. Lineage Schema

## File

    lineage.schema.json

## Purpose

Represents provenance and relationship paths.

The ten crosswalks demonstrate that Lineage must support more than simple Source ancestry.

Lineage now needs to describe relationships such as:

    derives_from
    delegated_by
    transformed_from
    depends_on
    observed_by
    produced_by
    aggregated_from
    precedes
    committed_as
    materialized_as
    supersedes
    compensates
    reconstructs_from
    drifted_from
    reconciles_toward

Therefore the Lineage schema should remain:

    graph-compatible

and:

    relationship-extensible

---

# 11. Regime Schema

## File

    regime.schema.json

## Purpose

Represents the bounded operational conditions governing Evaluation.

Potential concerns include:

    domain
    policy
    observer context
    precision
    freshness
    Source requirements
    consequence
    permitted Truth States
    Correction modes

The crosswalks strongly confirm:

> **Regime participates directly in Truth qualification.**

However, dynamic Evidence should not automatically be stuffed into Regime.

The v0.2 model should preserve a distinction between:

    stable governing boundary

and:

    current Context Evidence

---

# 12. Evaluation Schema

## File

    evaluation.schema.json

## Purpose

Represents one qualified attempt to evaluate one Claim under one Regime.

Evaluation should preserve:

    inputs
    qualification results
    selected Evidence
    excluded Evidence
    Coherence
    Drift
    Paradox
    synthesis rationale
    resulting Truth State
    evaluator version
    evaluation time

Completed Evaluations should be historically stable.

Revalidation should create another Evaluation.

---

# 13. Truth-State Schema

## File

    truth_state.schema.json

## Purpose

Represents the synthesized operational result of an Evaluation.

The v0.1 model includes statuses such as:

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

The crosswalk series adds an important refinement:

> **Truth-State qualification and domain-native result are different dimensions.**

Examples:

    qualification:
      operationally_accepted

    domain result:
      authorization = deny

or:

    qualification:
      operationally_accepted

    domain result:
      converged = false

The v0.2 schema should make this distinction explicit.

---

# 14. Coherence-State Schema

## File

    coherence_state.schema.json

## Purpose

Represents structural compatibility among qualified Evidence and relationships.

Initial states include:

    coherent
    weakly_coherent
    fragmented
    contested
    inverted
    indeterminate

The crosswalk series refined the meaning of Coherence substantially.

Coherence is not:

    simple equality

and it is not:

    majority vote

The generalized meaning is:

> **Domain-semantic structural compatibility among qualified Evidence and relationships under a declared Regime.**

---

# 15. Drift-State Schema

## File

    drift_state.schema.json

## Purpose

Represents displacement between relevant Truth-bearing states or structures.

Potential Drift dimensions include:

    value
    temporal
    state
    source
    lineage
    semantic
    authority
    policy
    regime
    instrumentation
    coverage
    context
    transformation

Numeric magnitude should remain optional.

Example:

    magnitude:
      56

    unit:
      milliseconds

is valid.

So is:

    magnitude:
      null

    dimensions:
      - semantic
      - lineage

The schema must not manufacture numerical precision.

---

# 16. Paradox Schema

## File

    paradox.schema.json

## Purpose

Represents qualified structural incompatibility that remains unresolved after:

    Truth Class
    Regime
    scope
    freshness
    Lineage
    domain semantics

have been considered.

The crosswalks strongly establish:

    difference
      ≠
    Paradox

    multiplicity
      ≠
    Paradox

    stale state
      ≠
    Paradox

    different Regimes
      ≠
    Paradox

Paradox should remain a deliberately narrow structure.

---

# 17. Correction-Policy Schema

## File

    correction_policy.schema.json

## Purpose

Represents permitted downstream response to a Truth State or Drift relationship.

Initial modes include:

    none
    step
    gradual
    quarantine
    dual_state
    human_escalation
    holdover
    fail_closed
    fail_bounded

Later crosswalks demonstrated additional correction families such as:

    reconciliation

    compensation

    replacement

    restriction

The v0.2 model should keep Correction extensible rather than continually expanding one flat enum.

---

# 18. v0.2 Consolidation — EvidenceItem

The strongest schema change emerging from the crosswalk series is:

    Observation
      ↓
    EvidenceItem

The generalized concept is:

> **A typed item participating as Evidence in one or more Evaluations.**

Potential Evidence types include:

    observation
    assertion
    declaration
    attribute
    attestation
    status_evidence
    transition_evidence
    derived_evidence

Observation should remain one specialization.

---

# 19. EvidenceItem Requirements

A generalized Evidence item may need:

    evidence_id

    evidence_type

    subject_id

    source_id

    value

    produced_at

    observed_at

    received_at

    expires_at

    integrity

    context

    lineage references

    metadata

Not every Evidence type requires every field.

The schema should therefore support type-specific requirements without turning every property optional and semantically meaningless.

---

# 20. Evidence Graph

Crosswalks #9 and #10 provide strong evidence that Evidence is graph-structured.

Potential relationships include:

    derives_from
    produced_by
    observed_by
    transformed_from
    depends_on
    aggregated_from
    correlates_with
    supports
    contradicts
    parent_of
    copied_from

The v0.2 schema model should support:

    fan-in
    fan-out
    branching
    merging
    derivation
    transformation

A flat array of Evidence IDs is insufficient for all generalized cases.

---

# 21. Evidence Independence

Independence should not rely only on:

    source.independence

Crosswalks demonstrate that two Evidence items may:

    appear separate

while sharing:

    one upstream Source
    one raw event
    one dependency
    one copied assertion

Therefore v0.2 should permit independence analysis through:

    Evidence Graph
    Lineage Graph

Potential classifications remain:

    independent
    partially_dependent
    dependent
    unknown

---

# 22. v0.2 Consolidation — ReferenceBasis

The second major schema evolution is:

    Anchor
      ↓
    ReferenceBasis

Potential ReferenceBasis types include:

    external_anchor
    governing_policy
    governing_protocol
    accepted_history
    authorized_declaration
    measurement_standard
    trust_configuration

Anchor remains useful.

It becomes one specialization of the broader concept.

---

# 23. ReferenceBasis Principle

A ReferenceBasis answers:

> **What recognized structure makes this Evaluation meaningful?**

Different Truth Classes may answer differently.

Examples:

    Temporal:
      timing reference

    Authority:
      policy

    State:
      protocol + accepted history

    Intent:
      authorized declaration

    Lineage:
      provenance requirements

The schema should preserve this variety.

---

# 24. v0.2 Consolidation — AuthorityRelationship

The crosswalks strongly establish that Authority is relational.

It should not remain represented as:

    source.authoritative = true

A candidate AuthorityRelationship may include:

    authority_relationship_id

    actor_id

    role

    operation

    subject_scope

    target_scope

    delegator_id

    reference_basis_id

    regime_id

    constraints

    valid_from

    valid_until

    lineage_reference

    status

The precise schema should be created during the v0.2 consolidation pass.

---

# 25. v0.2 Consolidation — Domain Result

The crosswalks repeatedly produced valid negative domain results.

Examples:

    DNS:
      absent

    IAM:
      authentication failed

    PKI:
      certificate not acceptable for use

    Authorization:
      deny

    Distributed State:
      uncommitted

    Transaction:
      rolled_back

    Desired State:
      converged = false

These results may still arise from:

    fully successful Evaluation

Therefore v0.2 should separate:

    Truth-State qualification

from:

    domain_result

---

# 26. Qualification vs Domain Result

Conceptually:

    truth_state:
      qualification_status:
        operationally_accepted

      domain_result:
        authorization:
          deny

This means:

> **The system successfully established that the requested action is not authorized.**

The negative result is itself qualified Truth.

This distinction should become explicit in v0.2.

---

# 27. v0.2 Consolidation — TruthComparison

Desired-State and Telemetry crosswalks strongly support:

    TruthComparison

A TruthComparison evaluates relationships between existing Truth States.

Examples:

    Intent vs State

    Expected vs Observed

    Prior vs Current

    Committed vs Materialized

    Claimed vs Observed Provenance

Potential output includes:

    Coherence
    Drift
    Gap
    domain result

This enables recursive Truth evaluation while preserving parent Lineage.

---

# 28. v0.2 Consolidation — MaterializedTruthState

Several systems distinguish:

    accepted Truth

from:

    operational materialization

Examples:

    DNS:
      cached result

    Distributed State:
      applied replica state

    Transactions:
      materialized database state

    Desired State:
      current realization of Intent

Potential future schema:

    materialized_truth_state.schema.json

The exact form should remain composable.

Not every Truth Class requires materialization.

---

# 29. v0.2 Consolidation — Coverage

Telemetry and Provenance establish a broader:

    Coverage

concept.

Coverage answers:

> **Across what bounded extent can the available Evidence support conclusions?**

Potential specializations:

    observation coverage
    provenance coverage
    evaluation coverage

Potential fields include:

    subject_scope
    evidence_types
    time_scope
    expected_sources
    known_gaps
    completeness_classification
    regime_id

Coverage becomes especially important when asserting:

    absence

or:

    completeness

---

# 30. v0.2 Consolidation — Gap

Missing structure should remain explicit.

Potential gap types include:

    evidence
    lineage
    transformation
    coverage
    authority
    context

A Gap may represent:

> **Something relevant that the current Evaluation cannot establish or reconstruct.**

Gap must remain distinct from:

    qualified absence

This is a key v0.2 requirement.

---

# 31. v0.2 Consolidation — AcceptanceRule

The crosswalks demonstrate that different domains establish operational acceptance differently.

Examples:

    NTP:
      Source selection and synthesis

    DNS:
      authority + freshness

    IAM:
      proofing / authentication requirements

    PKI:
      path validation

    Authority:
      policy evaluation

    Distributed State:
      quorum / commitment rule

    Transactions:
      commit rule

    Intent:
      declaration / convergence rules

Therefore v0.2 should consider:

    AcceptanceRule

as a first-class reusable concept.

---

# 32. v0.2 Consolidation — ContextEvidence

Dynamic current conditions should remain distinct from the stable Regime.

Examples:

    current environment
    runtime attributes
    request context
    telemetry context

Potential relationship:

    Regime
      +
    ContextEvidence
      ↓
    Evaluation

This prevents:

    Regime

from becoming an unstructured container for every runtime value.

---

# 33. v0.2 Consolidation — Role

Actors have repeatedly appeared in different roles.

Examples:

    Source
    Observer
    Consumer
    Authority
    Transformer
    Attester
    Leader
    Participant

The same Entity may occupy different roles in different Evaluations.

Therefore v0.2 should consider role assignment as relational.

Potential pattern:

    Entity
      ↓
    Role
      ↓
    Regime / Scope

This may be encoded inside existing relationship objects rather than requiring a new top-level schema.

---

# 34. v0.2 Consolidation — Derived Evidence

Derived Evidence should preserve:

    upstream Evidence

    transformation

    derivation method

    context

    producer

where relevant.

The key invariant is:

> **Derived Evidence must not be mistaken for independent corroboration of its own ancestors.**

A future Evidence schema should make derivation visible.

---

# 35. v0.2 Consolidation — Grounding Analysis

Recursive Evidence and Truth-State composition creates the possibility of:

    circular support

The schema layer should therefore permit reconstruction of:

    ultimate Evidence dependencies

and:

    Reference Bases

Potential computed concept:

    GroundingSet

This may not require persistent serialization.

The underlying graph must preserve enough information to calculate it.

---

# 36. Cycle Safety

The generalized model must tolerate legitimate graph cycles while preventing false Evidence amplification.

Therefore:

    cycle exists
      ≠
    automatically invalid

but:

    cycle
      ≠
    independent corroboration

Schemas should preserve references clearly enough for evaluation logic to detect cycles and shared ancestry.

---

# 37. v0.1 to v0.2 Mapping

The expected conceptual migration is:

| v0.1 | v0.2 Direction |
|---|---|
| `Observation` | `EvidenceItem` with Observation subtype |
| `Anchor` | `ReferenceBasis` with Anchor specialization |
| `Source` | Entity / Source role preserved |
| `Lineage` | Expanded graph semantics |
| `Regime` | Retained; dynamic context separated |
| `Evaluation` | Retained; graph-aware |
| `CoherenceState` | Retained; domain-semantic |
| `DriftState` | Retained; relational / cross-class references |
| `Paradox` | Retained; narrowed definition |
| `TruthState.status` | Qualification/lifecycle semantics |
| `accepted_value` | Domain-native result, potentially formalized as `domain_result` |
| `CorrectionPolicy` | Retained; action families made extensible |

This table describes architectural direction.

It is not yet a migration guarantee.

---

# 38. Backward Compatibility

The v0.2 design should attempt to preserve reasonable compatibility with v0.1 fixtures.

For example:

    v0.1 Observation

may be interpretable as:

    v0.2 EvidenceItem
      type:
        observation

Likewise:

    v0.1 Anchor

may become:

    v0.2 ReferenceBasis
      type:
        external_anchor

This enables the initial NTP fixtures to remain useful after consolidation.

Backward compatibility should not be preserved at the cost of structural corruption.

Where migration is necessary, it should be explicit and versioned.

---

# 39. Schema Versioning

Serialized artifacts should identify the schema revision where practical.

Current fixtures use:

    schema_version:
      "0.1"

Future consolidated fixtures may use:

    schema_version:
      "0.2"

Schema versions should indicate meaningful contract changes.

Avoid incrementing versions for documentation-only edits.

---

# 40. Schema Evolution

A schema change should be classified.

## Patch-Compatible

Examples:

    clearer description
    additional optional metadata
    corrected documentation

## Additive

Examples:

    optional new field
    optional relationship type

## Structural

Examples:

    Observation → EvidenceItem

    Anchor → ReferenceBasis

    status split into qualification + domain result

Structural changes require explicit version review.

---

# 41. Required vs Optional Fields

The schemas should be strict about structurally necessary fields and tolerant about domain-specific extension.

Bad pattern:

    every field optional

because then schema validation provides little architectural protection.

Also bad:

    every possible domain field mandatory

because then schemas become unusably broad.

The desired pattern is:

    small required kernel
      +
    typed extensions
      +
    optional domain metadata

---

# 42. Metadata Rule

Metadata remains useful for:

    diagnostics
    domain-specific extension
    fixture notes
    implementation annotations

But metadata must not override canonical fields.

Example:

    metadata:
      truth_status:
        operationally_accepted

must not override:

    truth_state.status

Likewise:

    metadata:
      regime:
        trusted

must not replace:

    regime_id

Canonical control data must remain canonical.

---

# 43. Extension Rule

When a new domain needs information not represented by the common schema:

1. determine whether it is domain-specific
2. determine whether existing relationship semantics can represent it
3. determine whether metadata is sufficient
4. promote only if repeated cross-system evidence supports the abstraction

This follows the same promotion discipline used throughout the crosswalk series.

---

# 44. `$id` and Schema Identity

Each JSON Schema should have a stable schema identity.

Conceptually:

    $id:
      stable schema identifier

The exact URI strategy should be standardized across the module.

Schema identity should not depend on:

    local filesystem path alone

if schemas will eventually be published or consumed externally.

---

# 45. `$schema`

Each JSON Schema should declare the JSON Schema dialect used by the implementation.

The project should use one dialect consistently across the schema set.

The specific dialect should be selected once and applied uniformly rather than mixed between files.

---

# 46. Schema References

Shared types should eventually be referenced rather than copied repeatedly.

Examples may include:

    identifiers
    timestamps
    DecisionReason
    lifecycle status
    Lineage reference
    domain-native value
    metadata
    relationship reference

However, schema modularization should not begin prematurely.

A dozen tiny shared schemas can become harder to maintain than one clear object contract.

Extract shared types when repetition becomes structurally meaningful.

---

# 47. Identifier Validation

Schemas should validate identifiers sufficiently to prevent empty or structurally unusable references.

They should not encode excessive semantic meaning into identifier syntax.

Preferred:

    stable non-empty identifier

over:

    identifier whose string format encodes business logic

The application should not need to parse:

    claim-temporal-001

to learn that the Claim is temporal.

That information belongs in explicit fields.

---

# 48. Timestamp Validation

Temporal fields should use explicit machine-readable timestamps.

Examples include:

    created_at
    updated_at
    observed_at
    received_at
    evaluated_at
    expires_at
    valid_from
    valid_until

The schema should distinguish:

    missing

from:

    null where semantically permitted

Temporal meaning remains field-specific.

---

# 49. Typed Enumerations

Enums are valuable where the vocabulary is canonically bounded.

Examples:

    Truth Class
    Truth-State qualification
    Coherence status
    Source status
    Paradox type

Enums should be used cautiously for concepts expected to evolve rapidly.

Overly strict enums can cause domain-specific concepts to leak into:

    metadata

simply because the canonical schema cannot evolve.

---

# 50. Domain-Native Value Contract

Fields such as:

    Observation.value

and:

    TruthState.accepted_value

must support structured domain-native values.

Examples:

    temporal:
      timestamp
      offset_ms

    authority:
      authorization

    transaction:
      commitment

    intent:
      converged

The schema should not require:

    string only

or:

    number only

for these values.

---

# 51. Decision Reasons

Important architectural decisions should remain explainable.

Where practical, schemas should support structured reasons:

    code
    message
    evidence_references
    regime_rule

Potential uses include:

    Qualification
    Coherence
    Drift
    Truth-State synthesis
    Correction

No naked status should be required where the architecture expects rationale.

---

# 52. Qualification Schema Strategy

The current scaffold does not include a standalone:

    qualification.schema.json

Qualification may initially remain embedded inside:

    evaluation.schema.json

or associated result structures.

During v0.2 consolidation, consider whether Qualification requires independent schema identity because it may apply to:

    EvidenceItem
    AuthorityRelationship
    Lineage edge
    subgraph
    Truth State

Do not create a separate schema until that requirement is confirmed.

---

# 53. Revalidation Schema Strategy

Likewise, the current scaffold does not include:

    revalidation_event.schema.json

Revalidation may initially remain embedded in:

    TruthState
    Evaluation
    fixture expectations

The logical data model identifies RevalidationEvent conceptually.

A standalone schema should be added only when implementation needs an independently serialized Revalidation object.

---

# 54. Evidence Graph Schema Strategy

The v0.2 model may require:

    evidence_item.schema.json

and potentially:

    evidence_relationship.schema.json

or a graph envelope.

Before adding those files, the consolidation pass should determine whether:

    Lineage Graph

can represent Evidence relationships cleanly.

Avoid creating two nearly identical graph systems.

---

# 55. Relationship Reuse

A strong candidate is a reusable relationship structure containing:

    relationship_id
    from_id
    to_id
    relationship_type
    regime_id
    valid_from
    valid_until
    transformation
    constraints
    metadata

This could represent selected:

    Lineage
    Evidence dependency
    Authority
    transformation

relationships.

However, different relationship types may require different semantics.

Use one generalized relationship schema only if doing so keeps validation meaningful.

---

# 56. Truth-State Recursion

The v0.2 model may permit:

    Truth State
      ↓
    later Evaluation input

Schemas should preserve this without embedding entire recursive objects indefinitely.

Prefer references:

    truth_state_id

over repeatedly nesting full Truth States.

This avoids:

    unbounded serialization depth

and supports graph reconstruction.

---

# 57. Graph Serialization Principle

Graph-shaped architecture does not require every object to serialize the complete graph.

Preferred:

    stable IDs
    typed relationships
    explicit references

This allows the graph to be reconstructed from bounded objects.

Avoid fixtures containing enormous recursively nested structures.

---

# 58. Schema and Fixture Boundary

Schemas define:

> **What constitutes a structurally valid serialized object?**

Fixtures define:

> **Which valid objects comprise this deterministic scenario?**

Tests define:

> **What behavior should result?**

These layers should remain separate.

A schema should not encode:

    expected Coherence for fragmented fixture

That belongs in fixture expectations / tests.

---

# 59. Schema and Evaluation Boundary

Structural validation must happen before Truth evaluation.

Conceptually:

    JSON
      ↓
    Schema Validation
      │
      ├── invalid
      │     ↓
      │   stop
      │
      └── valid
            ↓
        Truth Evaluation

Malformed JSON or broken object structure should not produce:

    Truth State:
      indeterminate

It should produce:

    validation failure

The Truth Service evaluates valid Claims and Evidence.

---

# 60. Schema and Domain Validation

JSON Schema can establish:

    structural validity

It cannot necessarily establish:

    domain truth

Example:

    offset_ms:
      14

may be structurally valid.

Whether that offset is acceptable belongs to:

    Regime
    Evaluation

Likewise:

    authority_relationship_id

may be structurally valid while the authority relationship itself later fails qualification.

The schema validates shape.

The evaluator validates meaning.

---

# 61. Schema and Integrity

Schema validation should not be confused with:

    cryptographic integrity

A structurally valid JSON document may still:

    be altered
    come from an untrusted Source
    contain false Claims

Integrity remains a separate Truth dimension.

---

# 62. Fixture Compatibility

The initial NTP fixture files are:

    ../fixtures/ntp/coherent.json

    ../fixtures/ntp/minor_drift.json

    ../fixtures/ntp/outlier.json

    ../fixtures/ntp/fragmented.json

    ../fixtures/ntp/stale.json

    ../fixtures/ntp/indeterminate.json

The v0.1 schemas should support the core runtime objects used by these fixtures.

Fixture envelope fields such as:

    fixture_id
    expected
    evaluation_context

do not necessarily belong inside every runtime entity schema.

A fixture may compose multiple valid schema objects in one scenario document.

---

# 63. Fixture Envelope Strategy

A future:

    fixture.schema.json

may validate the complete scenario envelope.

Potential structure:

    fixture metadata
    Claim
    Regime
    Anchors / Reference Bases
    Sources / Entities
    Observations / Evidence
    prior Truth State
    evaluation context
    expected behavior

This is separate from runtime entity schemas.

Do not force:

    claim.schema.json

to know about fixture expectations.

---

# 64. Test Result Strategy

Likewise:

    expected

blocks belong to deterministic testing.

They are not canonical runtime Truth-Service objects.

A future test schema could validate:

    expected fixture result

but this should remain separate from:

    truth_state.schema.json

The implementation must never consume:

    expected

as Evidence.

---

# 65. Immediate v0.1 Schema Goal

Before full v0.2 consolidation, the initial schema set should support:

    coherent.json

    minor_drift.json

    outlier.json

    fragmented.json

    stale.json

    indeterminate.json

for the objects they contain.

The immediate success condition is not:

    model all ten Truth Classes perfectly

It is:

> **Structurally validate the first deterministic temporal reference implementation without blocking the later generalized model.**

---

# 66. v0.2 Consolidation Goal

The v0.2 schema pass succeeds when it can represent the generalized findings of all ten crosswalks without:

- forcing every domain into NTP semantics
- making every property optional
- creating one schema per discovered noun
- collapsing domain result into Truth qualification
- losing Evidence derivation
- losing Lineage
- losing Authority scope
- hiding Coverage gaps
- creating circular corroboration
- requiring one external Anchor
- requiring one linear Evaluation pipeline

The objective is:

> **small generalized kernel + explicit typed extensions**

---

# 67. Proposed v0.2 Core Schema Set

A future consolidation may produce something similar to:

    claim.schema.json

    evidence_item.schema.json

    entity.schema.json

    reference_basis.schema.json

    authority_relationship.schema.json

    lineage.schema.json

    regime.schema.json

    evaluation.schema.json

    truth_state.schema.json

    truth_comparison.schema.json

    coherence_state.schema.json

    drift_state.schema.json

    paradox.schema.json

    coverage.schema.json

    gap.schema.json

    materialized_truth_state.schema.json

    correction_policy.schema.json

This is a proposal.

It is not yet the committed file set.

Some candidates may collapse into shared relationship structures.

---

# 68. Proposed Compatibility Schemas

If v0.2 is adopted, compatibility schemas may retain familiar v0.1 concepts:

    observation.schema.json

    source.schema.json

    anchor.schema.json

These may become:

    specialized schemas

or:

    aliases / composed schemas

for:

    EvidenceItem

    Entity

    ReferenceBasis

This lets older fixtures and educational examples remain readable.

---

# 69. Schema Promotion Rule

A new standalone schema should be created only when the concept:

1. has independent identity
2. has meaningful lifecycle
3. is referenced by multiple objects
4. requires independent validation
5. appears across multiple Truth Classes
6. cannot be represented cleanly as a relationship or attribute

Otherwise prefer:

    field
    relation
    enum
    metadata
    typed extension

This prevents schema proliferation.

---

# 70. Schema Consolidation Workflow

Recommended sequence:

    [1] Preserve v0.1 NTP fixture compatibility
              ↓
    [2] Validate current twelve schemas
              ↓
    [3] Compare schemas against ten crosswalk findings
              ↓
    [4] Identify structural gaps
              ↓
    [5] Classify:
          rename
          generalize
          split
          merge
          retain
          retire
              ↓
    [6] Draft v0.2 contracts
              ↓
    [7] Map v0.1 → v0.2
              ↓
    [8] Migrate one fixture
              ↓
    [9] Validate behavior
              ↓
    [10] Migrate remaining fixtures
              ↓
    [11] Version canon
              ↓
    [12] Begin generalized fixture families

This keeps the migration bounded.

---

# 71. Recommended First Migration

The safest v0.2 migration candidate is:

    coherent.json

because it contains:

- simple Claim
- one Regime
- one Anchor
- three Sources
- three Observations
- straightforward Lineage
- coherent result
- bounded Drift
- no Paradox

The migration can test:

    Observation → EvidenceItem

and:

    Anchor → ReferenceBasis

without simultaneously testing:

    Gap
    Paradox
    derived Evidence
    TruthComparison
    AuthorityRelationship

Once coherent migration works, more complex fixtures can follow.

---

# 72. Outlier Migration Test

The second useful migration fixture is:

    outlier.json

It adds:

    dissenting qualified Evidence

and tests:

    Evidence preserved
      ≠
    Evidence selected

This is useful for validating Evidence Graph and Coherence semantics.

---

# 73. Fragmented Migration Test

Next:

    fragmented.json

tests:

    multiple coherent clusters

    unresolved structural incompatibility

    null accepted value

    Paradox preservation

This is a strong test of v0.2 Coherence and Paradox boundaries.

---

# 74. Stale Migration Test

Then:

    stale.json

tests:

    historical Truth State
    expired Evidence
    temporal lifecycle
    current-vs-historical distinction
    Revalidation

This is useful for validating append-oriented history.

---

# 75. Indeterminate Migration Test

Finally:

    indeterminate.json

tests:

    Evidence Gap
    incomplete Lineage
    failed qualification
    no selected Evidence
    null domain value
    indeterminate Truth State

This is likely where v0.2 gains the most over v0.1.

---

# 76. Schema Tests

Schema tests should eventually cover:

    valid object accepted

    required field missing

    invalid enum rejected

    broken reference detected where testable

    invalid timestamp rejected

    domain-native value accepted

    null accepted value permitted where structurally valid

    unknown extension safely handled according to policy

JSON Schema validation and behavioral evaluation tests should remain separate.

---

# 77. Canonical Schema Invariants

Unless later evidence contradicts them, the following should guide schema design.

## Invariant 1

Claims do not contain their own accepted truth.

## Invariant 2

Evidence remains distinct from Truth States.

## Invariant 3

Truth States identify their producing Evaluation.

## Invariant 4

Evaluations identify their Regime.

## Invariant 5

Lineage remains reconstructable.

## Invariant 6

Evidence exclusion does not require deletion.

## Invariant 7

Null domain results are permitted.

## Invariant 8

Negative domain results are permitted.

## Invariant 9

Historical Truth States remain referenceable.

## Invariant 10

Correction remains separate from Evaluation.

## Invariant 11

Revalidation produces new Evaluation context.

## Invariant 12

Metadata cannot override canonical fields.

## Invariant 13

Derived Evidence must preserve ancestry.

## Invariant 14

Shared ancestry must remain detectable.

## Invariant 15

Evidence gaps must not masquerade as qualified absence.

---

# 78. Relationship Invariants

The graph-oriented v0.2 model should also preserve:

    node identity

    edge identity where needed

    relationship type

    direction

    source and target

    Regime where relevant

    transformation where relevant

    lifecycle where relevant

A relationship should not exist merely as:

    string note

when Evaluation logic depends on it.

---

# 79. Explainability Requirement

A serialized Evaluation should eventually contain or reference enough structure to answer:

> **Why did this Truth State exist?**

That explanation should be reconstructable from:

    Claim
    Regime
    ReferenceBasis
    Evidence
    Authority
    Lineage
    Qualification
    Coherence
    Drift
    Paradox
    AcceptanceRule
    domain result

The schema exists partly to make this reconstruction possible.

---

# 80. Round-Trip Requirement

Canonical runtime objects should eventually survive:

    serialize
      ↓
    validate
      ↓
    deserialize

without losing information required for:

    evaluation
    Lineage
    explanation
    Revalidation

Implementation-specific caches or derived indexes need not round-trip.

Canonical meaning must.

---

# 81. Canonical Serialization Principle

Prefer explicit structure over encoded prose when the information participates in evaluation.

For example:

Bad:

    reason:
      "Source A was stale because it was 600 seconds old."

Better:

    status:
      expired

    freshness_seconds:
      600

    reason:
      code: OBSERVATION_EXPIRED

Human-readable explanation may still accompany the structured fields.

Both are useful.

---

# 82. Thin-Schema Rule

The schema layer should remain as thin as possible while preserving structural integrity.

Do not encode:

- speculative business rules
- implementation algorithms
- crosswalk prose
- scoring rationale
- documentation narrative

Schemas should define:

    valid shape
    canonical identifiers
    relationships
    bounded vocabularies

Evaluation logic belongs elsewhere.

---

# 83. Research Plane Separation

The runtime schema set should remain distinct from research scoring schemas.

Runtime objects include:

    Claim
    Evidence
    Regime
    Evaluation
    Truth State

Research objects include:

    Reference System
    Crosswalk
    Criterion
    Score
    Evidence Citation
    Comparative Profile

Do not place:

    NTP score

inside:

    runtime TruthState

The two planes serve different purposes.

---

# 84. Fixture Expectations Are Also Research-Adjacent

Fixture expectations exist to test implementation behavior.

They are not runtime Claims about the external world.

Therefore:

    expected.coherence

should not be serialized into production TruthState simply because the fixture contains it.

The evaluator produces actual runtime results.

The test harness compares those results against expectations.

---

# 85. Failure Transparency

Schemas should support explicit degraded or indeterminate conditions.

They should not require values that force the implementation to invent certainty.

Examples:

    accepted_value:
      null

    drift.magnitude:
      null

    independence:
      unknown

    valid_until:
      null

These nulls must have defined structural meaning.

---

# 86. Unknown vs Missing

Where relevant, the schemas should distinguish:

    field missing
      =
    not supplied / not applicable according to schema

from:

    field = null
      =
    explicitly unknown / absent value where permitted

and:

    explicit domain result:
      absent / deny / false

These distinctions are essential.

---

# 87. JSON Schema Does Not Replace DecisionReason

A schema can say:

    status is valid enum

It cannot explain:

    why that status was selected

Therefore decision rationale remains runtime data.

Validation and explainability should not be conflated.

---

# 88. Initial Schema Definition of Done

The current schema phase reaches its first milestone when:

1. all six NTP fixtures can be structurally represented
2. core runtime objects validate consistently
3. domain-native temporal values survive validation
4. null indeterminate values are supported
5. Lineage references remain intact
6. historical Truth States can be referenced
7. fixture expectations remain outside runtime contracts
8. Evaluation and Correction remain distinct
9. schema failure remains distinct from Truth indeterminacy

At that point the v0.1 temporal implementation boundary is stable.

---

# 89. v0.2 Definition of Done

The consolidation phase reaches completion when the schemas can additionally represent:

1. Evidence types beyond Observation
2. Reference Bases beyond Anchors
3. scoped Authority relationships
4. graph-shaped Evidence
5. graph-shaped Lineage
6. Coverage
7. Gaps
8. Truth-State comparison
9. domain result separate from qualification
10. materialization relationships
11. derived Evidence
12. shared ancestry
13. circularity detection inputs
14. cross-class Drift
15. inherited limitations

without making every schema depend on every concept.

---

# 90. Governing Schema Principle

> **Make valid states representable and invalid structural states rejectable without forcing the schemas to decide Truth.**

The schema layer should know:

    this Claim has a valid shape

    this Evidence item identifies its Source

    this Evaluation identifies its Regime

    this Truth State references its Evaluation

It should not decide:

    this Claim is true

    this Source should be trusted

    this Evidence should be accepted

    this Drift is safe

Those decisions belong to Evaluation.

---

# 91. Navigation

Current schemas:

    ./claim.schema.json
    ./observation.schema.json
    ./source.schema.json
    ./anchor.schema.json
    ./lineage.schema.json
    ./regime.schema.json
    ./evaluation.schema.json
    ./truth_state.schema.json
    ./coherence_state.schema.json
    ./drift_state.schema.json
    ./paradox.schema.json
    ./correction_policy.schema.json

Architecture:

    ../architecture/truth_service_architecture.md
    ../architecture/truth_service_components.md
    ../architecture/truth_service_data_model.md

Crosswalk research:

    ../crosswalks/

Fixtures:

    ../fixtures/
    ../fixtures/ntp/

Behavioral tests:

    ../tests/

---

## Canonical Summary

The schema layer gives the Resonance Truth architecture a machine-readable boundary.

The original v0.1 model begins with:

    Claim
    Observation
    Source
    Anchor
    Lineage
    Regime
    Evaluation
    Coherence
    Drift
    Paradox
    Truth State
    Correction

The ten-system crosswalk series then challenges that model and points toward v0.2:

    Observation
      becomes
    EvidenceItem

    Anchor
      becomes a specialization of
    ReferenceBasis

    Authority
      becomes
    AuthorityRelationship

    flat Evidence
      becomes
    Evidence Graph

    Lineage
      becomes
    foundational graph structure

    unknown structure
      becomes visible through
    Coverage + Gap

    isolated Truth States
      become composable through
    TruthComparison

    accepted result
      separates into
    domain result + qualification

    current state
      may relate to
    MaterializedTruthState

The schema layer should encode those lessons carefully.

Not everything discovered in the crosswalks deserves a schema.

Not every relationship deserves a new file.

Not every domain state deserves a global enum.

The goal is a thin generalized kernel capable of preserving the structures that repeatedly survived challenge.

**Crosswalks discovered the structure.**

**Architecture gave it meaning.**

**Fixtures created controlled worlds.**

**Schemas now decide which of those worlds can be represented without losing the relationships that made their Truth explainable.**
