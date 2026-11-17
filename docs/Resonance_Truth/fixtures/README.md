# Resonance Truth — Fixtures

> **Deterministic reference scenarios for the RTT Resonance Truth Service**

**Module:** Resonance Truth  
**Artifact:** Fixture Index and Contract  
**Framework:** Resonance-Time Theory (RTT)  
**Status:** Reference Implementation / Deterministic Test Data  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This directory contains deterministic fixtures used to exercise the RTT Resonance Truth Service.

Fixtures provide controlled operational scenarios containing known:

- Claims
- Truth Classes
- Regimes
- Reference relationships
- Sources
- Evidence
- Lineage
- expected qualification behavior
- expected Coherence conditions
- expected Drift
- expected Paradox behavior
- expected Truth-State outcomes
- expected Correction behavior
- expected Revalidation behavior

The governing principle is:

> **A fixture describes a truth environment. A test asks whether the implementation interprets that environment correctly.**

Fixtures should therefore remain declarative.

They define:

    what exists

    what was observed

    where Evidence came from

    what Regime applies

    what relationships are known

Tests determine whether the Truth Service produces the expected operational interpretation.

---

# 1. Why Fixtures Exist

The first implementation should not begin by depending on live external infrastructure.

Live systems introduce variables such as:

- network availability
- changing remote state
- timing variability
- Source availability
- authentication
- environmental conditions
- implementation differences
- nondeterministic failure

Those conditions are important later.

They are undesirable when initially testing the Truth-Service model itself.

Deterministic fixtures allow the architecture to be tested independently from environmental noise.

The initial progression is:

    STATIC FIXTURE
         ↓
    VALIDATE STRUCTURE
         ↓
    RUN EVALUATION
         ↓
    INSPECT RESULT
         ↓
    COMPARE EXPECTATION
         ↓
    REFINE MODEL
         ↓
    LATER TEST LIVE SYSTEMS

---

# 2. Fixture Philosophy

A useful fixture should answer:

> **What exactly is the Truth Service being asked to evaluate?**

Each fixture should preserve enough structure to reconstruct the scenario without relying on hidden assumptions.

A fixture should make visible:

    Claim
      ↓
    Truth Class
      ↓
    Regime
      ↓
    Reference Basis
      ↓
    Evidence
      ↓
    Source / Actor
      ↓
    Lineage
      ↓
    Expected Structural Condition

It should not simply contain:

    expected_answer: true

That would erase the architecture we are trying to test.

---

# 3. Fixture vs Test

Fixtures and tests serve different purposes.

## Fixture

A fixture declares:

> **This is the scenario.**

Example:

    three qualified temporal Sources
    provide mutually compatible Observations

## Test

A test asks:

> **Does the implementation classify that scenario correctly?**

Example:

    expected Coherence:
      coherent

    expected Truth State:
      operationally_accepted

The distinction is:

    FIXTURE
      =
    controlled evidence environment

    TEST
      =
    behavioral assertion about that environment

---

# 4. Fixture vs Example

Fixtures should also remain distinct from explanatory examples.

## Example

Optimized for:

    human understanding

May simplify or omit implementation detail.

## Fixture

Optimized for:

    deterministic evaluation

Should contain enough structure for machine execution and repeatable testing.

A documentation example may inspire a fixture.

The fixture becomes the executable representation.

---

# 5. Fixture Requirements

Every fixture should identify, either directly or through clearly referenced common objects:

1. fixture identifier
2. fixture description
3. primary Truth Class
4. Claim
5. Regime
6. applicable reference relationships
7. Sources / participants
8. Evidence
9. Lineage
10. Evaluation time or evaluation context
11. expected structural properties
12. expected outcome

Fixtures should avoid unnecessary fields.

The goal is:

> **minimum complete structure**

not:

> **maximum possible serialization**

---

# 6. Determinism

A deterministic fixture should produce the same logical evaluation result when processed by the same evaluator version and configuration.

Fixture behavior should not depend upon:

- current wall-clock time unless explicitly injected
- random values
- live network responses
- external DNS
- external NTP servers
- remote APIs
- mutable third-party services

Time-dependent fixtures should use explicit timestamps.

Example:

    evaluation_time:
      fixed timestamp

rather than:

    evaluation_time:
      now

This makes:

    freshness
    expiration
    holdover
    Revalidation

reproducible.

---

# 7. Expected Results

Expected behavior should remain separate from raw input Evidence where possible.

Conceptually:

    fixture:
      input:
        ...

      expected:
        ...

This prevents the evaluator from accidentally consuming:

    expected result

as if it were:

    Evidence.

Expected results may include:

- qualification status
- selected Evidence
- excluded Evidence
- Coherence
- Drift
- Paradox
- domain result
- Truth-State qualification
- Correction
- lifecycle transition

Not every fixture needs every expectation.

---

# 8. Explanation Requirement

A fixture should not pass merely because:

    actual.status == expected.status

The implementation should eventually be capable of explaining:

> **Why did this fixture produce this result?**

Tests should therefore be able to inspect:

- qualification reasons
- participating Evidence
- excluded Evidence
- Coherence rationale
- Drift rationale
- Paradox rationale
- Regime rules
- synthesis rationale

A deterministic answer without deterministic explanation is incomplete.

---

# 9. Lineage Requirement

Fixtures must preserve relevant Lineage.

This is especially important when testing:

- Source independence
- shared upstream dependencies
- derivation
- transformations
- delegation
- committed history
- derived Evidence

Two Evidence items that share one upstream origin should not automatically be treated as independent merely because they have different identifiers.

Fixture design must make those relationships visible.

---

# 10. Negative Results

A fixture may successfully produce a negative domain result.

Examples include:

    present:
      false

    authorization:
      deny

    committed:
      false

    converged:
      false

These do not automatically imply:

    test failure

or:

    Truth-State rejection

A Truth Service may coherently determine a negative result.

The fixture contract therefore distinguishes:

    DOMAIN RESULT

from:

    TRUTH-STATE QUALIFICATION

---

# 11. Indeterminate Results

A fixture may intentionally produce:

    indeterminate

This should be treated as a successful expected result when the available Evidence does not support a stronger conclusion.

Example:

    no qualified Sources
          ↓
    insufficient Evidence
          ↓
    INDETERMINATE

A test must not require the evaluator to manufacture an accepted value.

---

# 12. Evidence Gaps

A fixture may intentionally contain missing Evidence.

The fixture should distinguish:

    qualified absence

from:

    Evidence Gap

Example:

    expected Evidence:
      unavailable

does not automatically mean:

    expected condition:
      absent

When gaps are part of the scenario, the fixture should make them explicit.

---

# 13. Crosswalk-Derived Fixture Model

The ten operational crosswalks introduced a generalized conceptual model containing:

    Claim

    Truth Class

    Subject / Target

    Regime

    ReferenceBasis

    EvidenceItem

    Evidence Graph

    Entity / Role

    AuthorityRelationship

    Lineage

    Coverage

    Gap

    Qualification

    AcceptanceRule

    Coherence

    Drift

    Paradox

    Domain Result

    Truth-State Qualification

    TruthComparison

    Materialization

    Correction

    Revalidation

Not every fixture requires every concept.

The fixture should include only the structures necessary to exercise the behavior being tested.

---

# 14. Fixture Minimalism

Avoid fixtures that become miniature production databases.

For example, a temporal Coherence fixture may require:

    Claim
    Regime
    Reference
    three Sources
    three Observations
    Lineage
    expected Coherence

It may not require:

    AuthorityRelationship
    TruthComparison
    Coverage
    Gap
    MaterializedTruthState

unless those concepts are part of the test.

The rule is:

> **Include enough structure to make the result explainable, and no more than the scenario requires.**

---

# 15. Initial Fixture Family — NTP

The first fixture family is:

    fixtures/ntp/

NTP provides the initial deterministic reference implementation for:

    Temporal Truth

The initial scenarios are:

    coherent.json

    minor_drift.json

    outlier.json

    fragmented.json

    stale.json

    indeterminate.json

These fixtures exercise the foundational Truth-Service behaviors before additional reference systems are introduced into executable tests.

---

# 16. NTP Fixture — Coherent

## File

    ntp/coherent.json

## Purpose

Represents several qualified temporal Sources whose Observations form a coherent temporal field.

Expected characteristics:

    Sources:
      multiple

    Evidence:
      qualified

    Coherence:
      coherent

    Drift:
      bounded

    Paradox:
      none material

Expected Truth-State qualification:

    operationally_accepted

This is the baseline positive fixture.

---

# 17. NTP Fixture — Minor Drift

## File

    ntp/minor_drift.json

## Purpose

Represents coherent temporal Evidence while local temporal state differs modestly from the qualified observed state.

Expected characteristics:

    Evidence:
      qualified

    Coherence:
      coherent

    Drift:
      present
      bounded

Potential Correction:

    gradual

or another Regime-defined bounded correction mode.

The fixture tests:

> **Drift does not automatically imply loss of operational acceptance.**

---

# 18. NTP Fixture — Outlier

## File

    ntp/outlier.json

## Purpose

Represents an otherwise coherent Evidence field containing one materially divergent Source or Observation.

Expected behavior:

    preserve divergent Evidence

    identify primary coherent cluster

    evaluate Source independence

    avoid deleting dissent

    avoid treating simple majority as Truth automatically

Potential expected structure:

    Coherence:
      coherent or weakly_coherent

    dissent:
      present

The final Truth-State qualification depends on the fixture's declared Regime.

---

# 19. NTP Fixture — Fragmented

## File

    ntp/fragmented.json

## Purpose

Represents multiple meaningful Evidence clusters that cannot be safely collapsed into one temporal state.

Potential structure:

    Cluster A:
      Source 1
      Source 2

    Cluster B:
      Source 3
      Source 4

Expected Coherence:

    fragmented

Potential Truth-State qualification:

    contested

or:

    indeterminate

depending on Regime.

The fixture tests whether the implementation resists manufacturing certainty.

---

# 20. NTP Fixture — Stale

## File

    ntp/stale.json

## Purpose

Represents previously usable temporal Evidence that no longer satisfies the applicable freshness requirement.

Potential lifecycle:

    operationally_accepted
          ↓
    degraded
          ↓
    held_over
          ↓
    expired

The exact expected state belongs to the fixture's declared evaluation time and Regime.

The fixture tests:

    freshness
    aging
    uncertainty
    holdover
    expiration
    Revalidation

---

# 21. NTP Fixture — Indeterminate

## File

    ntp/indeterminate.json

## Purpose

Represents a scenario in which no available Evidence can support a sufficiently qualified temporal state.

Possible structure:

    Evidence A:
      expired

    Evidence B:
      rejected

    Evidence C:
      indeterminate

Expected:

    selected Evidence:
      none

    Coherence:
      indeterminate

    Drift:
      unknown

    Truth-State qualification:
      indeterminate

    accepted value:
      null

This fixture establishes one of the most important service invariants:

> **No qualified answer is a valid answer.**

---

# 22. Expected Fixture Progression

The initial NTP fixture family tests increasing structural difficulty:

    COHERENT
       ↓
    MINOR DRIFT
       ↓
    OUTLIER
       ↓
    FRAGMENTED
       ↓
    STALE
       ↓
    INDETERMINATE

This progression should not be interpreted as one mandatory runtime lifecycle.

It is a test sequence covering different operational conditions.

---

# 23. Fixture Naming

Fixture filenames should describe the structural condition being exercised.

Preferred:

    coherent.json

    fragmented.json

    stale.json

Avoid names such as:

    test1.json

    sample2.json

    scenario_final_v3.json

The filename should tell a reader:

> **What condition is this fixture intended to demonstrate?**

---

# 24. Fixture Identity

Each fixture should also contain a stable internal identifier.

Example:

    fixture_id:
      ntp-coherent-001

The identifier should remain stable even if the filename later changes.

Fixture identity may be referenced by:

- tests
- documentation
- expected-result files
- regression reports

---

# 25. Fixture Metadata

Useful fixture metadata may include:

    fixture_id

    title

    description

    reference_system

    primary_truth_class

    fixture_version

    schema_version

    evaluator_version

Not every value must be present immediately.

Avoid metadata that merely duplicates the whole fixture.

---

# 26. Schema Version

Fixtures should eventually identify the schema revision against which they were authored.

Example:

    schema_version:
      "0.2"

This will become particularly important because the ten-system crosswalk series changed the architecture beyond its original v0.1 assumptions.

Schema versioning allows:

    old fixture
       ↓
    old model

and:

    revised fixture
       ↓
    revised model

to remain distinguishable.

---

# 27. Fixture Version

Fixture content may evolve independently of schema version.

Therefore:

    fixture_version

and:

    schema_version

should remain distinct.

Example:

    fixture_version:
      "1.1"

    schema_version:
      "0.2"

A fixture may change because:

- Evidence was corrected
- expected behavior changed
- additional Lineage was added
- rationale improved

without requiring a new global schema version.

---

# 28. Regression Role

Once a fixture produces a stable expected result, it becomes a regression artifact.

Future architecture or evaluator changes should ask:

> **Did this fixture's result change?**

If yes:

    expected architecture change?

or:

    unintended regression?

The fixture therefore becomes part of model lineage.

---

# 29. Fixture Change Discipline

When a fixture changes materially, preserve:

- what changed
- why
- which expected outcomes changed
- which architecture revision motivated the change

Do not quietly edit Evidence until a failing test disappears.

The fixture exists to challenge the implementation.

The implementation should not define the fixture retroactively.

---

# 30. Crosswalk Lineage

Fixtures should preserve connection to the research crosswalk that motivated them.

For the NTP family:

    ../../crosswalks/01_ntp_temporal_truth.md

Conceptual progression:

    Reference System
          ↓
    Crosswalk
          ↓
    Architectural Finding
          ↓
    Fixture
          ↓
    Test

This gives each executable scenario research Lineage.

---

# 31. Fixture Independence

Some fixtures intentionally test Source independence.

When two Sources share an upstream dependency, the fixture must preserve that relationship.

Example:

    Reference A
        ↓
    Upstream Source U
       ├── Source 1
       └── Source 2

The evaluator should not treat:

    Source 1
    Source 2

as:

    two fully independent references

if their Evidence derives from the same upstream Source.

This becomes especially important after the Observational and Provenance crosswalks.

---

# 32. Derived Evidence

A fixture may include Evidence derived from other Evidence.

Example:

    Raw Observation A
    Raw Observation B
          ↓
      Aggregation
          ↓
    Derived Evidence C

The fixture must preserve:

    C derives_from A + B

A test should not count:

    A
    B
    C

as:

    three independent corroborating Sources.

---

# 33. Circular Evidence

Fixtures used to test recursive Truth or derived Evidence should eventually include circularity scenarios.

Example:

    Evidence A
      ↓
    Derived B
      ↓
    Derived C
      ↓
    cited as support for A

Expected behavior:

    cycle detected

    no artificial independence gain

These fixtures are not required for the initial NTP implementation.

They belong to later generalized testing.

---

# 34. Fixture Coverage

A fixture should declare enough coverage context to explain claims of:

    absence

or:

    completeness

For example:

    no Observation found

is not sufficient to conclude:

    event absent

unless the fixture establishes that the observation boundary was sufficient to support that inference.

Coverage becomes increasingly important for:

    telemetry
    provenance
    identity
    distributed state

---

# 35. Fixture Gaps

A fixture may intentionally model:

    Evidence Gap

    Lineage Gap

    Coverage Gap

    Authority Gap

    Context Gap

A gap should remain explicit.

Do not fill the missing field with synthetic data simply to satisfy schema validation.

If the schema cannot represent a structurally valid gap, the schema needs review.

---

# 36. Truth-State Expectations

Fixture expectations should eventually distinguish:

    domain_result

from:

    Truth-State qualification

Example:

    domain_result:
      authorization: deny

    truth_status:
      operationally_accepted

or:

    domain_result:
      converged: false

    truth_status:
      operationally_accepted

This prevents tests from assuming:

    positive domain result
      =
    success

and:

    negative domain result
      =
    failure

---

# 37. Correction Expectations

A fixture may declare expected Correction behavior.

Possible examples:

    none

    gradual

    quarantine

    human_escalation

    reconciliation

    append_corrective_transition

Correction expectations should remain separate from:

    Truth-State expectation

because:

    Evaluation
      ≠
    Action

---

# 38. Revalidation Expectations

Fixtures involving lifecycle should define deterministic Revalidation conditions.

Examples:

    revalidate_at:
      fixed timestamp

or:

    trigger:
      source_change

or:

    trigger:
      contradictory_evidence

or:

    trigger:
      regime_change

Avoid dependence on:

    now

unless the test harness injects a fixed clock.

---

# 39. Materialization Expectations

Later fixture families may need to distinguish:

    accepted Truth State

from:

    local materialization.

Example:

    transaction:
      committed

    materialization:
      incomplete

This is valid.

Tests should not require:

    committed
      =
    fully materialized

unless the domain Regime requires that relationship.

---

# 40. Future Fixture Families

After NTP stabilizes, future fixture families may include:

    fixtures/dns/

    fixtures/iam/

    fixtures/pki/

    fixtures/authority/

    fixtures/distributed_state/

    fixtures/transactions/

    fixtures/desired_state/

    fixtures/telemetry/

    fixtures/provenance/

These directories should be created only when the corresponding reference case has enough deterministic scenarios to justify executable fixtures.

Do not create empty forests merely because the crosswalk names are known.

---

# 41. Candidate DNS Fixtures

Future DNS fixtures might exercise:

    fresh cached result

    expired cached result

    multiple valid records

    qualified negative result

    delegation change

    stable value with changed Lineage

These remain future candidates.

---

# 42. Candidate Identity Fixtures

Future IAM fixtures might exercise:

    successful proofing

    successful authentication

    failed authentication

    revoked credential

    federated assertion

    same assertion under different relying-party Regimes

These remain future candidates.

---

# 43. Candidate PKI Fixtures

Future PKI fixtures might exercise:

    valid certification path

    valid signature + expired certificate

    valid signature + revoked certificate

    unrecognized trust Anchor

    policy mismatch

    trust-store change

These remain future candidates.

---

# 44. Candidate Authority Fixtures

Future policy fixtures might exercise:

    coherent permit

    coherent deny

    same Subject / different Operation

    same Subject / different Target

    changed Environment

    policy revision

    delegated authority

    revoked delegation

These remain future candidates.

---

# 45. Candidate Distributed-State Fixtures

Future distributed-state fixtures might exercise:

    committed state

    uncommitted local entry

    stale replica

    leader / epoch change

    no quorum

    divergent uncommitted histories

    committed but not applied state

These remain future candidates.

---

# 46. Candidate Transactional Fixtures

Future transactional fixtures might exercise:

    committed transaction

    rollback

    crash after commit

    recovery

    compensating transaction

    pending transaction

    same state / different history

    commitment vs finality

These remain future candidates.

---

# 47. Candidate Desired-State Fixtures

Future Intent fixtures might exercise:

    converged state

    bounded Drift

    missing desired resource

    stale desired generation

    failed Correction

    oscillation

    conflicting Intent

    unauthorized Intent update

These remain future candidates.

---

# 48. Candidate Telemetry Fixtures

Future Observational fixtures might exercise:

    correlated signals

    missing trace

    Evidence Gap

    qualified absence

    sampled traces

    delayed telemetry

    instrumentation Drift

    shared Evidence dependency

    different Observer views

These remain future candidates.

---

# 49. Candidate Provenance Fixtures

Future Lineage fixtures might exercise:

    complete provenance

    missing transformation

    conflicting attestations

    shared dependency

    copied Evidence

    transformed artifact

    reproducible artifact

    circular derived Claim

    upstream revocation

    corrected provenance

These remain future candidates.

---

# 50. Fixture Validation

Fixture files should themselves be validated before their expected behavior is tested.

Validation layers may include:

    JSON syntax

    schema validation

    reference integrity

    identifier uniqueness

    required relationships

    Lineage consistency

A fixture that cannot be parsed or whose internal references are broken should fail before Truth evaluation begins.

---

# 51. Structural Validation vs Truth Evaluation

These stages must remain separate.

## Structural Validation

Asks:

> **Is this fixture well formed?**

## Truth Evaluation

Asks:

> **What qualified Truth State does this well-formed scenario produce?**

A malformed fixture should not produce:

    indeterminate Truth

It should produce:

    fixture / schema validation failure

This preserves architectural boundaries.

---

# 52. Fixture Integrity

A fixture should be immutable during one test execution.

The evaluator must not alter the source fixture to record:

- qualification
- Truth State
- Correction
- test status

Evaluation outputs should be written to separate runtime objects.

This protects repeatability.

---

# 53. Expected Output Separation

Recommended logical pattern:

    fixture input
      ↓
    evaluator
      ↓
    actual result
      ↓
    compare
      ↕
    expected result

Never:

    fixture input
      ↓
    evaluator mutates fixture
      ↓
    expected result overwritten

The fixture remains the controlled environment.

---

# 54. Human Readability

Fixtures are machine-consumable, but they should remain inspectable by humans.

Prefer:

    explicit Source IDs

    readable descriptions

    stable names

    clear timestamps

    bounded numeric values

over:

    opaque random data

unless opacity itself is required by the test.

A developer should be able to inspect a fixture and understand why the expected result is plausible.

---

# 55. Synthetic Fixture Disclosure

The initial NTP fixtures are deterministic synthetic scenarios.

They are not captures of live NTP infrastructure.

This should remain explicit.

Their purpose is:

    architecture testing

not:

    measurement of external systems

Later captured real-world data, if introduced, should be labeled separately.

---

# 56. Fixture Provenance

Even synthetic fixtures have provenance.

Useful metadata may preserve:

    source_crosswalk

    scenario_origin

    fixture_version

    schema_version

    authoring note

This helps identify:

> **Why does this fixture exist?**

The answer should point back to an architectural behavior being tested.

---

# 57. Fixture-to-Test Mapping

Each fixture should eventually map to one or more behavioral test categories.

Example:

    coherent.json
      ↓
    qualification/
    coherence/
    drift/

    fragmented.json
      ↓
    coherence/
    paradox/
    regime/

    stale.json
      ↓
    qualification/
    lifecycle/
    regime/

    indeterminate.json
      ↓
    qualification/
    coherence/
    lifecycle/

A fixture may legitimately support multiple tests.

---

# 58. Tests Should Reuse Fixtures

Avoid duplicating nearly identical scenario data independently across test directories.

Preferred:

    fixture
      ↓
    multiple tests

rather than:

    qualification test copy
    coherence test copy
    lifecycle test copy

Duplicated fixtures create hidden Lineage and maintenance Drift.

A single canonical fixture should be referenced where practical.

---

# 59. Fixture Evolution

When architecture consolidation produces the v0.2 model, fixtures may need to evolve.

Likely changes include:

    Observation
      ↓
    EvidenceItem

    Anchor
      ↓
    ReferenceBasis

and possible addition of:

    AuthorityRelationship
    Coverage
    Gap
    domain_result

The initial NTP fixtures should remain intentionally small.

Do not retrofit every generalized concept into them merely because those concepts exist.

---

# 60. Thin-Layer Rule

The fixtures layer should remain thin.

Its purpose is not to duplicate:

    architecture/
    crosswalks/
    schemas/

It should provide:

> **specific deterministic scenarios capable of exercising those layers.**

When a fixture requires a long theoretical explanation, that explanation probably belongs in:

    crosswalks/

or:

    architecture/

The fixture should reference the concept and remain executable.

---

# 61. Qualification Requirement

Fixture Evidence should not arrive pre-labeled as:

    qualified

unless the scenario explicitly tests externally supplied qualification.

Preferred:

    input Evidence:
      facts / metadata

    expected qualification:
      qualified

The evaluator should perform qualification.

This prevents the fixture from giving the engine its answer.

---

# 62. Coherence Requirement

Likewise, Sources should not usually be labeled:

    coherent_source: true

Instead the fixture should contain enough structure for the Coherence Engine to determine whether:

    Evidence is compatible

    Sources are independent

    clusters exist

    dissent exists

Expected Coherence belongs in the expected-result section or test assertion.

---

# 63. Drift Requirement

For measurable Drift, provide:

    baseline state

and:

    observed state

rather than only:

    expected_drift: 14

The Drift Engine should derive:

    magnitude

where possible.

For structural Drift, provide:

    before / baseline relationship

and:

    current relationship

so the evaluator can classify the difference.

---

# 64. Paradox Requirement

Do not create a Paradox fixture by simply setting:

    paradox: true

Instead provide:

    qualified incompatible structure

and allow the evaluator to determine whether:

    Paradox

remains after:

    Truth Class
    Regime
    freshness
    Lineage
    scope
    domain semantics

are considered.

---

# 65. Regime Requirement

Every Evaluation fixture must identify the governing Regime or provide enough information to resolve it deterministically.

Avoid:

    default regime

unless the default itself is explicitly part of the test.

Regime is part of Truth qualification.

It cannot remain hidden test harness state.

---

# 66. Evaluation Time Requirement

Any fixture testing:

    freshness

    expiration

    holdover

    validity interval

    revalidation timing

must provide a deterministic Evaluation time.

Example:

    evaluation_context:
      evaluated_at:
        "2026-01-01T00:05:00Z"

The exact timestamp is fixture data.

The important rule is that it is fixed.

---

# 67. Fixture Success Condition

The initial fixture layer succeeds when the six NTP scenarios can be processed deterministically and the evaluator can explain each result.

The implementation should be able to answer, for each fixture:

    What was the Claim?

    Which Regime applied?

    Which Evidence was considered?

    Which Evidence qualified?

    Which Evidence was excluded?

    Why?

    What Coherence state existed?

    What Drift was detected?

    What Paradox remained?

    What domain result emerged?

    What Truth-State qualification resulted?

    What Correction was permitted?

    When should Revalidation occur?

If those answers are reproducible, the fixture layer is doing its job.

---

# 68. Governing Fixture Principle

> **Fixtures should encode the conditions of Truth evaluation, not the conclusion of Truth evaluation.**

A good fixture provides:

    structure

    Evidence

    Lineage

    Regime

A good test then asks the evaluator to discover:

    qualification

    Coherence

    Drift

    Paradox

    domain result

    Truth State

That preserves the distinction between:

    scenario

and:

    answer

---

# 69. Navigation

Initial fixture family:

    ./ntp/coherent.json
    ./ntp/minor_drift.json
    ./ntp/outlier.json
    ./ntp/fragmented.json
    ./ntp/stale.json
    ./ntp/indeterminate.json

Related architecture:

    ../architecture/README.md
    ../architecture/truth_service_architecture.md
    ../architecture/truth_service_components.md
    ../architecture/truth_service_data_model.md
    ../architecture/implementation_roadmap.md

Related crosswalk:

    ../crosswalks/01_ntp_temporal_truth.md

Related schemas:

    ../schemas/

Related behavioral tests:

    ../tests/

---

## Canonical Summary

The fixture layer turns the Resonance Truth architecture into deterministic operational scenarios.

A fixture says:

    Here is the Claim.

    Here is the Regime.

    Here is the Evidence.

    Here are the Sources.

    Here is the Lineage.

    Here is the evaluation boundary.

The evaluator must determine:

    What qualifies?

    What coheres?

    What Drifts?

    What conflicts?

    What domain result can be supported?

    How qualified is that result?

    What may happen next?

The test then asks:

> **Did the evaluator get the structure right?**

The first implementation begins with six NTP scenarios:

    coherent
    minor drift
    outlier
    fragmented
    stale
    indeterminate

They are deliberately synthetic.

They are deliberately bounded.

They are deliberately boring enough to reproduce.

That is exactly what we want.

**Crosswalks challenge the architecture.**

**Schemas declare the contract.**

**Fixtures create the controlled world.**

**Tests ask whether the Truth Service can observe that world without inventing another one.**
