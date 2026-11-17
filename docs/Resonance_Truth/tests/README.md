<img width="1194" height="672" alt="Resonance_Truth_tests_" src="https://github.com/user-attachments/assets/3ae0f728-f57f-4c13-8f75-7ec0080f98a6" />

# Resonance Truth — Tests

> **Deterministic behavioral validation for the RTT Resonance Truth Service**

**Module:** Resonance Truth  
**Artifact:** Test Index and Behavioral Contract  
**Framework:** Resonance-Time Theory (RTT)  
**Status:** Reference Implementation / Behavioral Validation  
**Initial Reference System:** NTP / Temporal Truth  
**Context:** `rtt=1 | coherence=declared | drift=bounded | paradox=structural`

---

## Purpose

This directory contains deterministic behavioral tests for the RTT Resonance Truth Service.

The tests answer one governing question:

> **Given a structurally valid scenario, does the Truth Service interpret its Evidence and relationships correctly?**

The relationship among implementation artifacts is:

    SCHEMA
      ↓
    validates structure

    FIXTURE
      ↓
    declares controlled scenario

    EVALUATOR
      ↓
    interprets scenario

    TEST
      ↓
    verifies behavior

The tests should therefore validate:

- Qualification
- Coherence
- Drift
- Paradox handling
- Regime behavior
- Truth-State lifecycle behavior

without embedding the evaluator's logic into the tests themselves.

---

# 1. Test Philosophy

A useful test asks:

> **Did the implementation preserve the structural meaning of the scenario?**

It should not merely ask:

    did one final value equal one expected number?

The architecture requires richer assertions.

Examples include:

    Was stale Evidence excluded?

    Was qualified dissent preserved?

    Were dependent Sources recognized?

    Was Drift classified correctly?

    Was fragmentation preserved?

    Was Paradox registered only when justified?

    Did Regime change operational usability?

    Was accepted_value null when no defensible value existed?

Tests therefore validate relationships as well as outputs.

---

# 2. Test vs Fixture

Fixtures and tests must remain separate.

## Fixture

A fixture declares:

> **This is the controlled world.**

It contains:

    Claim
    Regime
    Sources
    Anchors
    Observations
    Lineage
    evaluation context
    expected behavior

## Test

A test asks:

> **Did the evaluator behave correctly inside that world?**

A fixture may support several tests.

A test should reuse canonical fixture data rather than creating another hidden version of the same scenario.

---

# 3. Test vs Schema

JSON Schema establishes:

> **Is this object structurally valid?**

Behavioral testing establishes:

> **Does the implementation interpret that valid object correctly?**

These are different failure boundaries.

Conceptually:

    malformed fixture
          ↓
    SCHEMA FAILURE

versus:

    valid fixture
          ↓
    wrong interpretation
          ↓
    BEHAVIORAL TEST FAILURE

Schema failure should occur before Truth evaluation.

---

# 4. Test vs Truth Failure

A test succeeds when the implementation returns the expected behavior.

That behavior may itself be:

    indeterminate

    contested

    expired

    rejected

For example:

    fixture:
      indeterminate.json

Expected:

    Truth State:
      indeterminate

If the evaluator returns:

    indeterminate

the test passes.

Therefore:

> **Negative or uncertain Truth results are not test failures when they are the correct bounded result.**

---

# 5. Evaluation Failure Is Different

The system must also distinguish:

    successful Evaluation
      producing
    indeterminate Truth State

from:

    failed Evaluation
      producing
    no valid Truth State

Example:

    insufficient qualified Evidence
      ↓
    Evaluation succeeds
      ↓
    Truth State = indeterminate

This is valid behavior.

Conversely:

    evaluator exception
      ↓
    Evaluation fails

is an implementation failure.

Tests must preserve this distinction.

---

# 6. Current Test Families

The behavioral test tree is organized around five initial analytical families:

    tests/
      qualification/
      coherence/
      drift/
      paradox/
      regime/

These categories correspond to major mechanisms in the v0.1 reference implementation.

They should remain behavior-oriented rather than fixture-oriented.

For example:

    qualification/

should contain tests about qualification behavior across several fixtures.

It should not simply duplicate:

    fixtures/ntp/

---

# 7. Qualification Tests

Directory:

    qualification/

Qualification tests verify whether Evidence is permitted to participate in a particular Evaluation.

Potential assertions include:

    fresh Observation
      → qualified

    expired Observation
      → expired

    unavailable Source
      → rejected or degraded according to Regime

    incomplete Lineage
      → indeterminate

    qualified Observation
      → may participate in later Coherence analysis

Qualification tests should verify:

- status
- reason code
- relevant references
- Regime rule
- inclusion / exclusion behavior

---

# 8. Qualification Does Not Decide Truth Alone

A qualified Observation does not automatically become:

    accepted Truth

Examples:

    outlier.json

all Observations may be qualified while one remains dissenting.

Likewise:

    fragmented.json

all Observations may qualify while no single accepted temporal value can be synthesized.

Therefore:

    QUALIFIED
      ≠
    SELECTED

and:

    QUALIFIED
      ≠
    TRUE

Tests should enforce this distinction.

---

# 9. Coherence Tests

Directory:

    coherence/

Coherence tests verify structural compatibility among qualified Evidence.

Potential outcomes include:

    coherent

    weakly_coherent

    fragmented

    contested

    inverted

    indeterminate

Tests should verify:

- cluster behavior
- supporting Evidence
- dissent preservation
- Source independence
- fragmentation
- absence of fabricated consensus

---

# 10. Coherence Is Not Majority Vote

Tests must explicitly resist implementations that reduce Coherence to:

    most Sources agree
      therefore
    accept majority value

Source count alone does not establish:

    independence
    authority
    valid Lineage
    sufficient scope

Future fixtures should include cases where several apparent Sources share one upstream dependency.

Expected behavior:

    shared ancestry detected

rather than:

    artificial corroboration

---

# 11. Coherent Test Behavior

For:

    ../fixtures/ntp/coherent.json

expected behavior includes:

    all three Observations qualify

    all three participate

    one coherent cluster exists

    no dissent exists

    no Paradox exists

    accepted temporal value exists

This is the baseline positive path.

---

# 12. Outlier Test Behavior

For:

    ../fixtures/ntp/outlier.json

expected behavior includes:

    all three Observations qualify

    two Observations form supporting cluster

    one qualified Observation remains dissenting

    dissenting Evidence is preserved

    one accepted temporal value remains supportable

    no structural Paradox is required

This is one of the most important early behavioral distinctions.

---

# 13. Fragmented Test Behavior

For:

    ../fixtures/ntp/fragmented.json

expected behavior includes:

    all four Observations qualify

    two meaningful coherent clusters emerge

    neither cluster has sufficient structural basis to dominate

    Coherence becomes fragmented

    accepted_value remains null

    structural Paradox is preserved

    single-state Correction is prohibited

This tests whether the implementation can refuse false certainty.

---

# 14. Indeterminate Coherence

For:

    ../fixtures/ntp/indeterminate.json

expected behavior includes:

    no Observation remains sufficiently qualified

    no current Coherence field is synthesized

    Coherence becomes indeterminate

    accepted_value remains null

This is structurally different from:

    fragmented

Fragmented means:

    multiple meaningful incompatible qualified structures

Indeterminate means:

    insufficient qualified structure

The tests must keep these apart.

---

# 15. Drift Tests

Directory:

    drift/

Drift tests verify displacement between relevant truth-bearing states or structures.

Potential Drift dimensions include:

    temporal
    value
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

The initial NTP tests primarily exercise:

    temporal Drift

---

# 16. Numeric Drift

For numeric domains, tests may assert exact deterministic calculations.

Example:

    local offset:
      0 ms

    synthesized offset:
      56 ms

Expected Drift:

    magnitude:
      56

    unit:
      milliseconds

    bounded:
      true

The test should verify the calculation from fixture inputs.

It should not merely compare against an unexplained constant.

---

# 17. Qualitative Drift

Future tests must also support:

    magnitude:
      null

Example:

    prior authority:
      Source A

    current authority:
      Source B

Expected:

    dimensions:
      - source
      - authority

    direction:
      changed

    magnitude:
      null

The implementation must not manufacture a numeric distance.

---

# 18. Minor-Drift Behavior

For:

    ../fixtures/ntp/minor_drift.json

expected behavior includes:

    qualified Sources form one coherent cluster

    representative temporal offset = 56 ms

    Regime boundary = 100 ms

    Drift remains bounded

    Truth State remains operationally accepted

    gradual Correction is permitted

Therefore:

    Drift present
      ≠
    Truth failure

---

# 19. Stale Drift Behavior

For:

    ../fixtures/ntp/stale.json

the system should not calculate:

    current Drift = historical offset

because all observations are expired.

Expected:

    historical coherence preserved

    current Drift magnitude unknown

    current boundedness unknown

    current accepted_value null

This protects the distinction between:

    historical Truth

and:

    present Truth.

---

# 20. Paradox Tests

Directory:

    paradox/

Paradox tests verify that the service distinguishes genuine unresolved incompatibility from ordinary difference.

The governing rule is:

> **Classification precedes contradiction.**

Before Paradox, the implementation should consider whether apparent disagreement is explained by:

- different Truth Class
- different Regime
- different scope
- valid multiplicity
- stale Evidence
- expired Evidence
- local-state lag
- materialization lag
- sampling
- Observer position
- Lineage dependency
- Evidence gaps
- different epoch
- different version
- domain semantics

---

# 21. Outlier Is Not Paradox

The outlier fixture provides the first important anti-Paradox test.

Expected:

    dissent:
      yes

    Paradox:
      no

One qualified divergent Source does not necessarily create an unresolved structural contradiction.

Tests should ensure the evaluator does not escalate every disagreement into Paradox.

---

# 22. Fragmentation Can Produce Paradox

The fragmented fixture represents:

    Cluster A
      independently supported

    Cluster B
      independently supported

with:

    same Claim
    same Regime
    mutually incompatible temporal states
    no justified selection basis

Expected:

    Paradox:
      active

Tests should verify:

    containment

rather than:

    fabricated resolution

---

# 23. Paradox Resolution Tests

Future tests should verify that a Paradox may later be resolved through:

    new Evidence
    Regime separation
    scope separation
    Lineage resolution
    authority resolution
    staleness resolution
    policy resolution
    domain semantics

Resolution should not delete the historical Paradox.

Instead:

    new Evaluation
      ↓
    resolution relationship

Historical structure remains inspectable.

---

# 24. Regime Tests

Directory:

    regime/

Regime tests verify that identical Evidence can yield different operational usability under different governing conditions.

Potential tests include:

    lower precision requirement

    higher minimum independent Source count

    shorter freshness window

    different consequence level

    different permitted Correction modes

The Evidence should remain unchanged unless the test explicitly changes it.

---

# 25. Same Evidence, Different Regime

A canonical future test should evaluate the same temporal Evidence under two Regimes.

Example:

    Evidence:
      offset = 56 ms

Regime A:

    maximum allowed:
      100 ms

Result:

    bounded

Regime B:

    maximum allowed:
      10 ms

Result:

    unbounded

The Evidence did not change.

The governing boundary did.

This validates:

> **Truth qualification can change with Regime without Evidence becoming arbitrary.**

---

# 26. Regime Must Be Explicit

Tests should avoid hidden global defaults.

Bad:

    evaluator assumes display-clock regime

Good:

    evaluation.regime_id:
      regime-display-clock

If a test depends on a default Regime, the default itself must be the behavior under test.

---

# 27. Lifecycle Tests

The repository may eventually add a dedicated:

    lifecycle/

test family.

Until then, lifecycle assertions can be tested through the existing families.

Initial lifecycle behaviors include:

    operationally_accepted
      ↓
    expired

and:

    new Evidence
      ↓
    Revalidation
      ↓
    new Truth State

The stale NTP fixture is the first lifecycle scenario.

---

# 28. Historical-State Preservation

Tests involving Revalidation should verify:

    prior Truth State remains referenceable

    new Evaluation is created

    new Truth State is created

    prior Evidence is not rewritten

    supersession is explicit

Expected pattern:

    Truth State A
         ↓
    Revalidation
         ↓
    Evaluation B
         ↓
    Truth State B

not:

    mutate Truth State A in place

---

# 29. Correction Tests

Correction behavior currently appears through other test families rather than a dedicated:

    correction/

directory.

Tests should verify:

    Correction follows Truth-State synthesis

and never:

    Correction determines the Truth State

Examples:

    coherent
      → none

    minor drift
      → gradual

    fragmented
      → dual_state

    stale
      → fail_bounded

    indeterminate
      → fail_bounded

---

# 30. Correction Attempt vs Success

Future tests should distinguish:

    Correction allowed

    Correction attempted

    Correction committed

    Correction observed

    state converged

These are separate lifecycle stages.

The desired-state and transactional crosswalks make this especially important.

---

# 31. Assertion Depth

Tests should assert the minimum structure necessary to validate behavior.

Avoid brittle assertions against incidental serialization details.

Good:

    truth_state.status == operationally_accepted

    drift.magnitude == 56

    coherence.status == coherent

Bad:

    entire generated JSON text exactly equals one monolithic string

unless exact serialization is specifically under test.

Behavioral tests should survive irrelevant field ordering.

---

# 32. Reason-Code Assertions

Where Evaluation behavior depends on explicit classification, tests should verify stable reason codes.

Examples:

    OBSERVATION_EXPIRED

    SOURCE_UNAVAILABLE

    LINEAGE_INCOMPLETE

    NO_QUALIFIED_SYNTHESIS_SET

    UNRESOLVED_COMPETING_TEMPORAL_CLUSTERS

Human-readable messages may evolve.

Machine-readable reason codes should remain comparatively stable.

---

# 33. Explanation Assertions

Tests should not require only:

    status

They should verify that the service can explain important bounded decisions.

Example:

    status:
      indeterminate

Expected reason:

    no qualified synthesis set

This prevents implementations from returning the right enum for the wrong reason.

---

# 34. Test Determinism

Behavioral tests must remain deterministic.

Do not depend on:

- current wall-clock time
- external NTP
- external DNS
- live APIs
- network availability
- random values
- mutable third-party services

Use fixed fixture timestamps and injected Evaluation time.

If randomized testing is added later:

    random seed

must be controlled and failures reproducible.

---

# 35. Time Injection

Tests involving freshness must inject Evaluation time explicitly.

Example:

    evaluated_at:
      fixed fixture timestamp

Do not call:

    current system time

inside deterministic fixture tests.

Otherwise:

    stale

may become:

    fresh

or:

    expired

depending on when the test happens to run.

---

# 36. Input Immutability

Tests should verify that Evaluations do not mutate fixture inputs.

After Evaluation:

    Claim
    Regime
    Source
    Anchor
    Observation
    Lineage

should remain unchanged unless the action under test explicitly produces a separate mutation artifact.

Evaluation outputs belong in new objects.

---

# 37. No Hidden Evidence

The evaluator should not consult information outside the controlled fixture unless the test explicitly introduces an external adapter.

For deterministic unit/reference tests:

    fixture Evidence

is the complete allowed input set.

This prevents tests from passing because the developer's machine happens to have:

    network time
    cached DNS
    environment variables
    local configuration

available.

---

# 38. No Expected-Result Leakage

The evaluator must never receive:

    fixture.expected

as Evaluation input.

Correct test flow:

    fixture.input
       ↓
    evaluator
       ↓
    actual

separately:

    fixture.expected
       ↓
    comparator

then:

    actual
      ↔
    expected

Any architecture that passes expected results into the evaluator invalidates the fixture model.

---

# 39. Unit vs Integration Tests

The initial reference suite should prioritize small deterministic tests.

## Unit Tests

Exercise one component or decision rule.

Examples:

    freshness qualification

    temporal Drift calculation

    Coherence clustering

## Integration Tests

Exercise the v0.1 evaluation path across multiple components.

Example:

    fixture
      ↓
    Qualification
      ↓
    Coherence
      ↓
    Drift
      ↓
    Paradox
      ↓
    Truth State
      ↓
    Correction

Both forms are useful.

---

# 40. Cross-Component Tests

Some architectural bugs occur only between components.

Examples:

    qualified dissent incorrectly discarded before Coherence

    fragmented Coherence still produces accepted value

    expired Evidence reused by Drift Engine

    indeterminate Truth State triggers Correction mutation

    Paradox removed because one cluster appears first

Integration tests should specifically target these boundaries.

---

# 41. Independent-Source Tests

Future tests should challenge:

    source.independence

with actual Lineage.

Example:

    Source A
      ↓
    upstream U

    Source B
      ↓
    upstream U

Even if both Source objects claim:

    independent

Lineage analysis should reveal:

    dependent

or:

    partially_dependent

This tests the rule:

> **Independence is structural, not declarative.**

---

# 42. Derived-Evidence Tests

Future generalized tests should include:

    Evidence A
    Evidence B
       ↓
    Derived Evidence C

Expected:

    C is not counted as an independent third Source supporting A and B.

This is a direct consequence of the Telemetry and Provenance crosswalks.

---

# 43. Circularity Tests

Future tests should include Evidence cycles.

Example:

    A → B → C → A

Expected:

    cycle visible

    independent grounding not increased

A graph cycle should not automatically mean:

    invalid

but should prevent:

    synthetic corroboration

where appropriate.

---

# 44. Coverage Tests

Future generalized tests should distinguish:

    complete enough observation boundary

from:

    partial Evidence set

Example:

    no event observed
      +
    insufficient coverage
      ↓
    Evidence Gap / unknown

versus:

    no event observed
      +
    qualified complete observation boundary
      ↓
    possible qualified absence

This should become a core generalized behavior.

---

# 45. Negative Domain-Result Tests

Later test families must include successful Evaluations whose domain result is negative.

Examples:

    authorization:
      deny

    converged:
      false

    committed:
      false

    presence:
      absent

Expected:

    Evaluation:
      completed

The domain result may be negative while the Truth State remains:

    operationally_accepted

This is central to v0.2.

---

# 46. Domain Result vs Truth Qualification

Tests should eventually enforce:

    domain_result
      ≠
    qualification_status

Example:

    domain_result:
      authorization = deny

    qualification:
      operationally_accepted

This means:

> The service successfully established that authorization is denied.

Tests must not encode:

    false domain value
      → rejected Truth

as a universal rule.

---

# 47. Multi-Class Tests

Future tests should evaluate Claims involving several Truth Classes.

Example:

    certificate operational acceptability

may depend on:

    integrity
    identity
    authority
    temporal
    lineage

The test should verify that:

    one class can fail

without artificially declaring:

    every class failed.

This will become important after v0.2 consolidation.

---

# 48. Cross-Class Truth Tests

Desired-state behavior also requires:

    Intent Truth
      vs
    State Truth

Expected:

    different values
      → Drift

not automatically:

    Paradox

Cross-class comparison tests should become part of the generalized suite.

---

# 49. Stable-Value Structural-Drift Tests

The crosswalks repeatedly discovered:

> **Stable value does not imply stable structure.**

Future tests should include:

    domain value:
      unchanged

while:

    Source changes

or:

    Authority changes

or:

    Lineage changes

or:

    Regime changes

Expected:

    structural Drift detected.

---

# 50. Paradox Anti-Tests

It is useful to explicitly test conditions that must **not** produce Paradox.

Examples:

    one qualified outlier

    multiple valid DNS records

    one Subject with multiple legitimate identities

    certificate integrity valid but certificate expired

    desired state differs from current state

    local replica lags committed state

    sampled telemetry differs from aggregate metric

These tests protect the narrow meaning of Paradox.

---

# 51. Failure Transparency Tests

Tests should verify that failure conditions remain distinguishable.

Examples:

    unsupported Claim

    no qualified Evidence

    Source unavailable

    Evidence expired

    Lineage incomplete

    Regime missing

    schema invalid

    evaluator failure

These should not all collapse into:

    false

or:

    error

The result should preserve what actually failed.

---

# 52. No-Answer Tests

The suite must explicitly reward:

    accepted_value:
      null

when that is the correct result.

Core examples:

    fragmented.json

    indeterminate.json

    stale.json

These protect the service from pressure to always produce an answer.

The property being tested is restraint.

---

# 53. Regression Tests

Once fixture behavior stabilizes, each fixture becomes a regression surface.

A future evaluator change should immediately reveal changes in:

    Qualification

    Coherence

    Drift

    Paradox

    Truth-State status

    Correction

When behavior changes intentionally, expectations should be updated with an architectural reason.

---

# 54. Regression Discipline

Do not respond to a failing regression by immediately changing expected results.

First ask:

    Did the evaluator regress?

    Did the architecture intentionally change?

    Did the fixture contain an error?

    Did the schema change?

    Did the governing Regime change?

Only then update the appropriate layer.

---

# 55. Test Naming

Test names should identify behavior.

Preferred:

    test_expired_observation_is_not_selected

    test_outlier_remains_qualified_dissent

    test_fragmented_clusters_do_not_synthesize_value

    test_indeterminate_state_has_null_value

    test_minor_drift_allows_gradual_correction

Avoid:

    test_01

    test_case_a

    test_fixture_3

A failing test name should already tell the developer what invariant broke.

---

# 56. Test Granularity

One test should ideally assert one primary behavioral invariant.

A test may make several supporting assertions required to prove that invariant.

Example:

    test_fragmented_clusters_do_not_synthesize_value

may reasonably assert:

    coherence.status == fragmented

    paradox exists

    truth_state.status == contested

    accepted_value == null

because these jointly establish the invariant.

Avoid testing every field in the fixture in every test.

---

# 57. Recommended Initial Qualification Tests

Suggested initial behavioral tests:

    test_coherent_observations_qualify

    test_expired_observations_expire

    test_unavailable_source_rejects_observation

    test_incomplete_lineage_is_indeterminate

    test_no_qualified_observations_produces_empty_selection

These can reuse the NTP fixtures.

---

# 58. Recommended Initial Coherence Tests

Suggested:

    test_coherent_fixture_forms_one_cluster

    test_outlier_preserves_dissent

    test_outlier_retains_supporting_cluster

    test_fragmented_fixture_forms_two_clusters

    test_indeterminate_fixture_forms_no_cluster

    test_fragmented_clusters_do_not_select_winner

---

# 59. Recommended Initial Drift Tests

Suggested:

    test_coherent_fixture_has_bounded_drift

    test_minor_drift_is_56_ms

    test_minor_drift_remains_within_regime

    test_fragmented_drift_is_unbounded

    test_indeterminate_drift_has_null_magnitude

    test_stale_evidence_does_not_reuse_historical_offset_as_current_drift

---

# 60. Recommended Initial Paradox Tests

Suggested:

    test_coherent_fixture_has_no_paradox

    test_outlier_does_not_create_paradox

    test_fragmented_fixture_creates_structural_paradox

    test_indeterminate_fixture_has_no_paradox

    test_stale_fixture_has_no_paradox

These establish the difference between:

    disagreement
    insufficiency
    expiration
    structural contradiction

---

# 61. Recommended Initial Regime Tests

Suggested:

    test_minor_drift_allowed_by_display_clock_regime

    test_same_drift_rejected_by_stricter_regime

    test_minimum_independent_source_requirement

    test_expired_evidence_fails_freshness_requirement

    test_correction_mode_must_be_permitted_by_regime

This is where the service starts proving that Regime is operational rather than decorative metadata.

---

# 62. Initial NTP Behavior Matrix

| Fixture | Qualification | Coherence | Drift | Paradox | Truth State | Correction |
|---|---|---|---|---|---|---|
| `coherent.json` | qualified | coherent | bounded | none | operationally accepted | none |
| `minor_drift.json` | qualified | coherent | bounded / present | none | operationally accepted | gradual |
| `outlier.json` | qualified | weakly coherent | bounded selected field | none | operationally accepted | none |
| `fragmented.json` | qualified | fragmented | unbounded / unresolved | structural | contested | dual state |
| `stale.json` | expired | indeterminate current field | unknown current | none | expired | fail bounded |
| `indeterminate.json` | none sufficient | indeterminate | unknown | none | indeterminate | fail bounded |

This matrix is descriptive.

The fixtures remain the authoritative deterministic scenario definitions.

---

# 63. Crosswalk Traceability

Every future behavioral family should retain traceability to the research crosswalk that motivated it.

Conceptually:

    Crosswalk
       ↓
    Architecture Finding
       ↓
    Schema Contract
       ↓
    Fixture
       ↓
    Behavioral Test

This gives a failing or changing test a research Lineage.

---

# 64. Schema Traceability

When a test fails because an object no longer validates:

    that is a Schema issue first

When the object validates but the evaluator produces the wrong result:

    that is a Behavioral issue

Keeping this boundary obvious will make debugging much faster.

---

# 65. v0.1 Test Boundary

The initial v0.1 behavioral suite should focus on:

    temporal Claims

    NTP-like Sources

    Anchors

    Observations

    Qualification

    Coherence

    Drift

    Paradox

    Regime

    Truth State

    Correction

    Revalidation

This is enough to establish the reference evaluator.

Do not require v0.1 tests to implement every abstraction discovered by all ten crosswalks.

---

# 66. v0.2 Test Expansion

After architecture consolidation, the test suite should expand toward:

    EvidenceItem

    ReferenceBasis

    AuthorityRelationship

    Evidence Graph

    Coverage

    Gap

    TruthComparison

    MaterializedTruthState

    domain result / qualification separation

    graph-derived independence

    circularity protection

The NTP tests should remain as regression tests during this migration.

---

# 67. Migration Testing

v0.2 migration should evaluate the same logical scenario through:

    v0.1 representation

and:

    v0.2 representation

where compatibility is intended.

Example:

    v0.1 Observation
      ↔
    v0.2 EvidenceItem(type=observation)

Expected:

    same relevant temporal behavior

This provides strong regression coverage during consolidation.

---

# 68. No Architecture-by-Test

Tests must not become the place where undocumented architecture rules first appear.

If a test requires a new invariant:

    document architecture
      ↓
    update schema if necessary
      ↓
    update fixture
      ↓
    add test

not:

    add mysterious assertion
      ↓
    infer architecture later

Tests enforce the contract.

They should not secretly invent it.

---

# 69. No Fixture-by-Test

Likewise, tests should not modify fixture objects to force a scenario.

Bad:

    load coherent.json
    mutate Source C to stale
    call it stale scenario

Preferred:

    load stale.json

unless mutation itself is the behavior under test.

Canonical fixtures should represent canonical scenarios.

---

# 70. Test Output

A failed behavioral test should ideally report:

    fixture

    Claim

    Regime

    expected result

    actual result

    relevant reason codes

    relevant Evidence references

This keeps failures explainable and reduces debugging time.

---

# 71. Tests as Educational Artifacts

The test suite should remain understandable enough that a student can follow:

    Fixture
      ↓
    Evaluation
      ↓
    Expected relationship

Tests are not merely implementation guards.

They demonstrate:

    what Qualification means

    what Coherence means

    what Drift means

    when Paradox applies

    why Regime matters

This supports the educational mission of TriadicFrameworks.

---

# 72. Definition of Done — Initial Test Layer

The initial behavioral test layer is successful when it can demonstrate deterministically that:

1. coherent Evidence is accepted
2. bounded Drift is measurable
3. minor Drift does not automatically invalidate Truth
4. qualified dissent is preserved
5. one outlier does not automatically create Paradox
6. fragmented Evidence does not fabricate one answer
7. stale Evidence is not reused as fresh Evidence
8. insufficient Evidence produces Indeterminate
9. null accepted values are handled intentionally
10. Regime changes operational interpretation
11. Correction remains downstream of Truth
12. Revalidation preserves historical state

At that point the v0.1 NTP reference evaluator has a meaningful regression boundary.

---

# 73. Governing Test Principle

> **A behavioral test should prove that the Truth Service preserves structure when pressure exists to collapse it.**

Pressure may come from:

    disagreement

    missing Evidence

    stale Evidence

    Drift

    conflicting clusters

    changing Regime

    downstream demand for one answer

The evaluator succeeds when it produces the most qualified result the Evidence supports.

No more.

No less.

---

# 74. Navigation

Fixtures:

    ../fixtures/
    ../fixtures/ntp/coherent.json
    ../fixtures/ntp/minor_drift.json
    ../fixtures/ntp/outlier.json
    ../fixtures/ntp/fragmented.json
    ../fixtures/ntp/stale.json
    ../fixtures/ntp/indeterminate.json

Schemas:

    ../schemas/
    ../schemas/claim.schema.json
    ../schemas/anchor.schema.json
    ../schemas/source.schema.json
    ../schemas/observation.schema.json
    ../schemas/lineage.schema.json
    ../schemas/regime.schema.json
    ../schemas/evaluation.schema.json
    ../schemas/coherence_state.schema.json
    ../schemas/drift_state.schema.json
    ../schemas/paradox.schema.json
    ../schemas/truth_state.schema.json
    ../schemas/correction_policy.schema.json

Research crosswalks:

    ../crosswalks/

Test families:

    ./qualification/
    ./coherence/
    ./drift/
    ./paradox/
    ./regime/

---

## Canonical Summary

The test layer exists to challenge the implementation.

Fixtures declare controlled worlds.

Schemas ensure those worlds are structurally representable.

Evaluators interpret the Evidence.

Tests ask whether the interpretation preserved the architecture.

The first six NTP fixtures deliberately pressure different boundaries:

    coherent
      asks:
    Can the system recognize agreement?

    minor drift
      asks:
    Can the system tolerate bounded displacement?

    outlier
      asks:
    Can the system preserve dissent without surrendering a justified answer?

    fragmented
      asks:
    Can the system refuse to manufacture consensus?

    stale
      asks:
    Can the system remember that an old answer was once good without pretending it is still current?

    indeterminate
      asks:
    Can the system say "I don't presently know" without treating that as failure?

A useful Truth Service must pass all six.

Not because each scenario has an answer.

But because each scenario has a structure.

The tests exist to make sure the implementation does not destroy that structure merely to produce one.

**Fixtures create the world.**

**Schemas constrain its shape.**

**Evaluators interpret it.**

**Tests keep the evaluator honest.**
