# Predictive Analytics — Metrics

> **Measure the framework's failures at least as carefully as its successes.**

## Module

Predictive Analytics

## Document Role

Canonical experimental metric registry.

## Status

Experimental.

## Validation State

Unvalidated.

## Decision Authority

None.

---

# Purpose

This document defines the initial measurement grammar for Predictive Analytics.

The metrics are intended to test:

- evidence coverage,
- evidence independence,
- reliability,
- profile stability,
- construct validity,
- predictive value,
- substrate effects,
- regime effects,
- model mismatch,
- coherence,
- drift,
- uncertainty,
- calibration,
- counterfactual robustness,
- adapter contribution,
- fairness,
- explainability,
- human review,
- and operational burden.

The metrics are not themselves validated merely because they have formulas.

A formula provides:

```text
calculation structure
```

It does not automatically provide:

```text
valid measurement
```

---

# Metric Principle

Every metric should answer four questions:

```text
What is being measured?

Why is it useful?

What assumptions does it require?

What could make it misleading?
```

A metric without a clear answer to these questions should not receive operational authority.

---

# No Universal Score

Predictive Analytics intentionally does not define:

```text
Predictive Analytics Score
```

or:

```text
Resonant IQ Score
```

or:

```text
Human Capability Score
```

The metric system instead preserves multiple properties.

Example:

```yaml
assessment_metrics:
  evidence_coverage:
  evidence_independence:
  reliability:
  calibration:
  substrate_stability:
  regime_stability:
  coherence:
  counterfactual_robustness:
  fairness:
  explanation_quality:
```

A composite may eventually be justified for a specific validated use.

It is not assumed here.

---

# Metric Categories

The initial registry contains 52 canonical metrics.

```text
Evidence                    PA-M01 – PA-M03
Reliability / Stability     PA-M04 – PA-M07
Validity                    PA-M08 – PA-M11
Substrate                   PA-M12 – PA-M15
Regime                      PA-M16 – PA-M19
Model Mismatch              PA-M20 – PA-M23
Coherence / Drift           PA-M24 – PA-M27
Uncertainty / Calibration   PA-M28 – PA-M32
Counterfactual / Robustness PA-M33 – PA-M36
Fairness                    PA-M37 – PA-M44
Explainability / Review     PA-M45 – PA-M48
Operational                 PA-M49 – PA-M52
```

---

# Metric Record Contract

Every production-quality metric should eventually declare:

```yaml
metric:
  id:
  name:
  version:

  category:
  purpose:
  definition:

  formula:

  scale:
  direction:

  required_inputs:
  supported_systems:
  applicability:

  interpretation:
  limitations:
  known_confounds:

  missing_data_policy:
  subgroup_policy:

  threshold:
    status:
    value:
    rationale:

  validation_state:
  lifecycle:
```

---

# Metric Lifecycle

Canonical states:

```text
proposed
pilot
validated
restricted
deprecated
rejected
```

A metric may be removed if it:

- cannot be measured reliably,
- adds no useful information,
- duplicates another metric,
- creates misleading interpretations,
- behaves unfairly,
- or encourages inappropriate optimization.

---

# Threshold Policy

Initial policy:

```yaml
threshold_policy:
  status: study_specific
  universal_thresholds: false
  preregistration_required: true
  post_hoc_changes_disclosed: true
```

No universal numeric pass/fail thresholds are defined by the experimental module.

---

# Metric Direction

Possible direction states:

```text
higher_is_better
lower_is_better
target_range
descriptive
context_dependent
```

A metric must not silently imply:

```text
larger number = better person
```

---

# 1. Evidence Metrics

---

# PA-M01 — Dimension Evidence Coverage

## Purpose

Measure how much of a dimension's declared evidence requirement is supported by available observations.

## Conceptual Formula

```text
DEC =
  supported_indicators
  /
  required_indicators
```

## Direction

```text
higher_is_better
```

for evidence coverage only.

## Interpretation

Higher coverage means:

```text
more of the declared evidence
for this dimension is available
```

It does **not** mean:

```text
dimension magnitude is higher
```

or:

```text
dimension is valid
```

## Example

```yaml
structural_reasoning:
  required_indicators: 5
  supported_indicators: 4

  PA-M01:
    value: 0.80
```

The example demonstrates arithmetic only.

No universal `0.80` adequacy threshold is implied.

## Risks

```text
weak indicators counted equally with strong indicators
poorly designed requirements
circular evidence
duplicate evidence
```

---

# PA-M02 — Profile Evidence Coverage

## Purpose

Measure the proportion of applicable dimensions with sufficient evidence.

## Formula

```text
PEC =
  dimensions_with_sufficient_evidence
  /
  applicable_dimensions
```

## Required Companion States

```text
applicable
unsupported
unknown
not_applicable
```

## Important Rule

```text
not_applicable
```

must not be treated as:

```text
zero
```

and:

```text
unknown
```

must not be treated as:

```text
average
```

---

# PA-M03 — Evidence Independence Ratio

## Purpose

Prevent multiple interpretations of the same evidence from being mistaken for multiple independent confirmations.

## Formula

```text
EIR =
  independent_evidence_sources
  /
  total_evidence_sources
```

## Example

One observation is processed by five adapters.

```text
FFT
Inverted Star
Structural Detection
RTT
Resonance
```

Correct:

```yaml
adapter_interpretations: 5
independent_evidence_sources: 1
```

Not:

```text
evidence count: 5
```

## Core Invariant

```text
adapter_count != evidence_count
```

---

# 2. Reliability and Stability Metrics

---

# PA-M04 — Test-Retest Stability

## Purpose

Measure consistency across repeated observations where the target capability is expected to remain sufficiently stable.

## Candidate Methods

Depending on the measurement:

```text
intraclass correlation
rank correlation
weighted agreement
categorical agreement
profile similarity
```

The method must fit the data.

## Important Limit

Some dimensions may legitimately change.

Therefore:

```text
low_test_retest
```

does not automatically mean:

```text
bad_dimension
```

until expected stability is defined.

---

# PA-M05 — Alternate-Form Stability

## Purpose

Determine whether different tasks intended to observe the same dimension produce sufficiently comparable results.

## Conceptual Formula

```text
AFS =
  agreement(
    dimension_form_a,
    dimension_form_b
  )
```

## Possible Explanations for Low Stability

```text
poor form equivalence
unstable capability
substrate effect
regime effect
practice effect
task artifact
invalid dimension
```

The metric does not identify the cause.

---

# PA-M06 — Inter-Rater Agreement

## Purpose

Measure agreement among independent evaluators.

## Candidate Statistics

Where appropriate:

```text
Cohen's kappa
weighted kappa
Fleiss' kappa
Krippendorff's alpha
intraclass correlation
```

Raw agreement may also be reported but should not substitute for a suitable reliability measure when chance agreement matters.

## Applies To

```text
dimension classification
adapter interpretation
coherence relationship
human review
model-mismatch interpretation
```

---

# PA-M07 — Profile Topology Stability

## Purpose

Measure whether the relative shape of a multidimensional profile remains stable under comparable conditions.

## Conceptual Formula

```text
PTS =
  similarity(
    normalized_profile_t1,
    normalized_profile_t2
  )
```

## Candidate Methods

```text
cosine similarity
rank-profile correlation
distance-based similarity
graph similarity
```

## Important Rule

Always accompany profile-level similarity with dimension-level changes.

Two profiles may have high overall similarity while containing one important local shift.

---

# 3. Validity Metrics

---

# PA-M08 — Convergent Association

## Purpose

Test whether a proposed dimension relates to independent observations it is theoretically expected to relate to.

## Conceptual Formula

```text
CA =
  association(
    proposed_dimension,
    related_external_measure
  )
```

## Interpretation

Expected direction and magnitude should be declared before confirmatory analysis where possible.

## Warning

Convergence does not establish identity.

```text
A correlates with B
```

does not mean:

```text
A = B
```

---

# PA-M09 — Discriminant Separation

## Purpose

Test whether two dimensions claiming to measure different constructs are actually distinguishable.

## Conceptual Form

```text
DS =
  related_association
  -
  unrelated_association
```

Alternative methods may include:

```text
multitrait-multimethod analysis
latent-variable analysis
network analysis
classification separation
preregistered correlation contrasts
```

## Practical Question

If:

```text
structural_reasoning
```

and:

```text
pattern_recognition
```

cannot be empirically distinguished, should they remain separate?

Possibly not.

---

# PA-M10 — Incremental Explanatory Value

## Purpose

Measure whether the richer model explains observations better than a simpler baseline.

## Conceptual Formula

```text
IEV =
  explanatory_performance(full_model)
  -
  explanatory_performance(baseline)
```

## Possible Performance Measures

Depending on study design:

```text
explained variance
likelihood
information criteria
prediction residual structure
validated explanation reconstruction
```

## Complexity Requirement

A more complex model should not win simply because it has more parameters or concepts.

Complexity penalties or appropriate holdout methods should be considered.

---

# PA-M11 — Incremental Predictive Value

## Purpose

Measure out-of-sample predictive improvement.

## Conceptual Form

```text
IPV =
  baseline_error
  -
  full_model_error
```

or an equivalent comparison appropriate to the outcome.

## Candidate Measures

```text
mean absolute error
root mean squared error
log loss
Brier score
appropriate discrimination metric
task-specific utility
```

## Core Principle

A richer model that explains more but predicts no better can still be useful.

Its contribution should simply be labeled:

```text
explanatory
```

rather than:

```text
predictive
```

---

# 4. Substrate Metrics

---

# PA-M12 — Substrate Effect Magnitude

## Purpose

Measure change in observed performance across defined substrates.

## Conceptual Formula

```text
SEM =
  standardized_difference(
    performance_substrate_a,
    performance_substrate_b
  )
```

## Interpretation

A large effect means:

```text
observations differ across substrates
```

Not automatically:

```text
substrate caused the difference
```

---

# PA-M13 — Substrate Effect Replicability

## Purpose

Measure whether a candidate substrate effect repeats.

## Formula

```text
SER =
  replicated_effects_in_expected_direction
  /
  eligible_replications
```

## Required Companion Information

Always include:

```text
effect magnitude
uncertainty
task comparability
confounds
```

A high replication ratio for a trivial effect may not be operationally important.

---

# PA-M14 — Substrate Symmetry

## Purpose

Detect whether the framework recognizes both favorable and adverse substrate effects.

## Conceptual Formula

```text
SS =
  min(
    detection_rate_positive_effects,
    detection_rate_negative_effects
  )
```

## Purpose of the Minimum

If the framework detects:

```text
performance improves
```

very well but ignores:

```text
performance worsens
```

the symmetry metric should expose the imbalance.

---

# PA-M15 — Substrate Specificity

## Purpose

Determine whether an apparent substrate effect remains after controlling for relevant alternative explanations.

## Conceptual Form

```text
SSP =
  substrate_effect_after_controls
```

Potential controls:

```text
task difficulty
exposure
time
fatigue
order
familiarity
accessibility
evaluator
```

## Limit

Unknown confounds remain possible.

---

# 5. Regime Metrics

---

# PA-M16 — Regime Transition Detection Rate

## Purpose

Measure detection of independently defined regime transitions.

## Formula

```text
RTDR =
  detected_transitions
  /
  reference_transitions
```

## Warning

Reference transitions must not be defined solely by whether the model succeeded or failed.

Otherwise the metric becomes circular.

---

# PA-M17 — False Regime Alarm Rate

## Purpose

Measure how often regime transitions are declared where no meaningful reference transition exists.

## Formula

```text
FRAR =
  false_transition_flags
  /
  stable_regime_opportunities
```

## Importance

A framework that finds new regimes every time prediction fails can explain anything and therefore validate very little.

---

# PA-M18 — Regime Boundary Error

## Purpose

Measure distance between a detected and reference boundary.

## Conceptual Formula

```text
RBE =
  distance(
    detected_boundary,
    reference_boundary
  )
```

Possible distance units may include:

```text
time
events
state distance
structural position
```

depending on the application.

---

# PA-M19 — Regime-Conditioned Stability

## Purpose

Measure whether observations remain relatively stable within a regime even when they differ between regimes.

## Conceptual Form

```text
RCS =
  within_regime_stability
```

## Example

```text
Regime A:
  40
  42
  41

Regime B:
  72
  74
  73
```

The interesting result may be:

```text
high within-regime stability
+
large between-regime difference
```

rather than generic instability.

---

# 6. Model-Mismatch Metrics

---

# PA-M20 — Model-Mismatch Precision

## Purpose

Measure how often declared mismatch is supported by reference evidence.

## Formula

```text
MMP =
  supported_mismatch_flags
  /
  all_mismatch_flags
```

## Importance

This metric protects against:

```text
unfavorable result
  ->
declare mismatch
```

---

# PA-M21 — Model-Mismatch Recall

## Purpose

Measure how many reference mismatch cases the framework detects.

## Formula

```text
MMR =
  detected_reference_mismatches
  /
  all_reference_mismatches
```

## Required Pairing

Interpret with:

```text
PA-M20
PA-M22
```

High recall with very low precision may be unacceptable.

---

# PA-M22 — Model-Mismatch False Positive Rate

## Purpose

Measure mismatch declarations in reference non-mismatch cases.

## Formula

```text
MMFPR =
  false_mismatch_flags
  /
  reference_non_mismatch_cases
```

## Critical Test

A framework that labels every disappointing prediction as mismatch should perform poorly here.

---

# PA-M23 — Mismatch Evidence Strength

## Purpose

Represent strength of evidence supporting a mismatch interpretation without producing a capability or intelligence score.

Possible evidence components:

```text
independent sources
replication
substrate effect
regime effect
counterfactual consistency
prediction error
calibration
uncertainty
```

## Important Restriction

If components are aggregated, the aggregation rule must be:

```text
transparent
validated
versioned
```

It must not become a hidden global score.

---

# 7. Coherence and Drift Metrics

---

# PA-M24 — Cross-Observation Coherence

## Purpose

Measure the degree to which observations expected to relate form compatible relationships.

## Conceptual Formula

```text
COC =
  coherent_observation_relationships
  /
  eligible_observation_relationships
```

## Relationship Classes

The Coherence Observer may distinguish:

```text
supporting
contradictory
conditionally_compatible
independent
redundant
non_comparable
unknown
```

The exact definition of:

```text
coherent
```

must therefore be study-specific.

---

# PA-M25 — Profile Contradiction Density

## Purpose

Measure unresolved contradictions relative to evaluated relationships.

## Formula

```text
PCD =
  unresolved_contradictions
  /
  evaluated_relationships
```

## Important Rule

Higher contradiction density is not automatically bad.

It may indicate:

```text
real heterogeneity
regime dependence
substrate dependence
poor measurement
invalid assumptions
insufficient evidence
```

The metric describes structure.

---

# PA-M26 — Dimension Drift Rate

## Purpose

Measure change in a defined dimension across a declared observation interval.

## Conceptual Formula

```text
DDR =
  dimension_change
  /
  observation_interval
```

## Limit

Use only where:

```text
dimension_change
```

and:

```text
observation_interval
```

have defensible quantitative meaning.

Otherwise use descriptive longitudinal states.

---

# PA-M27 — Profile Drift Magnitude

## Purpose

Measure overall change between multidimensional profiles.

## Conceptual Formula

```text
PDM =
  distance(
    profile_t1,
    profile_t2
  )
```

## Required Companion Output

Include:

```text
dimension-level changes
```

because one overall distance may hide different directions.

---

# 8. Uncertainty and Calibration Metrics

---

# PA-M28 — Confidence Calibration Error

## Purpose

Measure correspondence between stated confidence and observed correctness or reproducibility.

## Conceptual Form

```text
CCE =
  average(
    abs(
      stated_confidence
      -
      observed_frequency
    )
  )
```

## Direction

```text
lower_is_better
```

## Important Limit

Ordinal labels such as:

```text
low
medium
high
```

must not be converted into numerical probabilities without a validated mapping.

---

# PA-M29 — Brier Score

## Purpose

Evaluate probabilistic binary predictions where appropriate.

## Formula

```text
BS =
  mean(
    (forecast_probability - outcome)^2
  )
```

## Direction

```text
lower_is_better
```

## Applicability

Only where the outcome and prediction format make the Brier score appropriate.

It is not a universal Predictive Analytics metric.

---

# PA-M30 — Abstention Rate

## Purpose

Measure how often the system returns:

```text
abstain
unknown
insufficient_evidence
```

for eligible assessment opportunities.

## Formula

```text
AR =
  abstained_results
  /
  eligible_results
```

## Direction

```text
descriptive
```

High abstention is not automatically better.

Low abstention is not automatically better.

---

# PA-M31 — Abstention Utility

## Purpose

Measure whether abstention reduces error or unsupported inference enough to justify its cost.

## Conceptual Formula

```text
AU =
  error_reduction_after_abstention
  -
  abstention_cost
```

## Cost May Include

```text
delay
review burden
lost coverage
resource cost
missed opportunity
```

The cost model must be declared.

---

# PA-M32 — Unsupported Assertion Rate

## Purpose

Measure claims that exceed available evidence.

## Formula

```text
UAR =
  assertions_without_sufficient_evidence
  /
  all_profile_assertions
```

## Direction

```text
lower_is_better
```

## Examples of Unsupported Assertions

```text
hidden intelligence inferred from one discrepant result

causal substrate claim without causal evidence

global capability inferred from narrow observation

AI cognition equivalence inferred from task similarity
```

---

# 9. Counterfactual and Robustness Metrics

---

# PA-M33 — Irrelevant Perturbation Stability

## Purpose

Measure whether an interpretation remains stable when irrelevant details change.

## Conceptual Formula

```text
IPS =
  similarity(
    original_result,
    irrelevant_perturbation_result
  )
```

## Direction

```text
higher_is_better
```

when the perturbation is genuinely irrelevant.

---

# PA-M34 — Relevant Change Sensitivity

## Purpose

Measure whether meaningful evidence changes cause appropriate assessment changes.

## Formula

```text
RCS =
  detected_meaningful_changes
  /
  introduced_meaningful_changes
```

## Direction

```text
higher_is_better
```

---

# Stability-Sensitivity Pair

Desired:

```text
irrelevant change:
  stable

relevant change:
  responsive
```

Failure mode 1:

```text
irrelevant change:
  large response
```

means:

```text
fragility
```

Failure mode 2:

```text
relevant change:
  no response
```

means:

```text
insensitivity
```

---

# PA-M35 — Task-Order Sensitivity

## Purpose

Measure changes caused by task ordering where order should not materially affect the construct.

## Formula

```text
TOS =
  distance(
    result_order_a,
    result_order_b
  )
```

## Direction

Usually:

```text
lower_is_better
```

when order independence is expected.

---

# PA-M36 — Adapter Ablation Effect

## Purpose

Measure what an adapter contributes.

## Formula

```text
AAE(adapter_x) =
  performance(full_adapter_set)
  -
  performance(without_adapter_x)
```

## Adapters

```text
FFT
Inverted Star
Structural Detection
RTT
Resonance
```

## Candidate Outcomes

```text
material_positive_contribution
small_positive_contribution
no_detectable_contribution
negative_contribution
interaction_dependent
unknown
```

## Core Principle

An adapter must be removable.

If removing it changes nothing useful:

```text
its contribution has not been demonstrated
```

---

# 10. Fairness Metrics

---

# PA-M37 — Group Error Difference

## Purpose

Compare error patterns across relevant groups or contexts.

## Formula

```text
GED =
  error_rate_group_a
  -
  error_rate_group_b
```

Both absolute and relative comparisons may be useful.

## Warning

A difference does not independently establish unfairness.

It establishes a signal requiring contextual investigation.

---

# PA-M38 — Group Calibration Difference

## Purpose

Test whether confidence means approximately the same thing across relevant groups.

## Formula

```text
GCD =
  calibration_error_group_a
  -
  calibration_error_group_b
```

## Research Question

Does:

```text
80% confidence
```

correspond to similar observed reliability across relevant populations?

---

# PA-M39 — Mismatch Flag Rate Difference

## Purpose

Compare how often groups are flagged for model mismatch.

## Formula

```text
MFRD =
  mismatch_flag_rate_group_a
  -
  mismatch_flag_rate_group_b
```

## Interpretation

A difference may arise from:

```text
true model-fit differences
unequal evidence
substrate bias
model bias
measurement differences
sample differences
unknown causes
```

It requires investigation.

---

# PA-M40 — Abstention Coverage Difference

## Purpose

Compare abstention rates across relevant groups.

## Formula

```text
ACD =
  abstention_rate_group_a
  -
  abstention_rate_group_b
```

## Why It Matters

A system may appear fair on classified cases while disproportionately returning:

```text
unknown
```

for another group.

---

# PA-M41 — Escalation Rate Difference

## Purpose

Compare human-review escalation rates.

## Formula

```text
ERD =
  human_review_rate_group_a
  -
  human_review_rate_group_b
```

Review may be:

```text
protective
burdensome
delaying
opportunity-enhancing
```

depending on context.

The metric is therefore descriptive until consequences are evaluated.

---

# PA-M42 — Evidence Coverage Difference

## Purpose

Measure differences in evidence coverage.

## Formula

```text
ECD =
  evidence_coverage_group_a
  -
  evidence_coverage_group_b
```

## Importance

A model may appear less reliable for one population simply because the measurement system provides poorer coverage.

That distinction should be investigated.

---

# PA-M43 — False Favorable Reinterpretation Rate

## Purpose

Detect unsupported reinterpretations that make an assessment more favorable.

## Formula

```text
FFRR =
  unsupported_favorable_reinterpretations
  /
  favorable_reinterpretations
```

## Direction

```text
lower_is_better
```

## Example

```text
baseline:
  low

one stronger alternate observation:
  high

framework:
  declares hidden high ability

replication:
  fails
```

This would contribute to the false favorable reinterpretation problem.

---

# PA-M44 — False Adverse Reinterpretation Rate

## Purpose

Detect unsupported reinterpretations that make an assessment more adverse.

## Formula

```text
FARR =
  unsupported_adverse_reinterpretations
  /
  adverse_reinterpretations
```

## Direction

```text
lower_is_better
```

## Symmetry Principle

Both PA-M43 and PA-M44 are required.

Fairness cannot mean challenging only unfavorable conventional models.

---

# 11. Explainability and Review Metrics

---

# PA-M45 — Evidence Reconstruction Rate

## Purpose

Measure whether qualified independent reviewers can reconstruct how an assessment was reached.

## Formula

```text
ERR =
  successfully_reconstructed_results
  /
  reviewed_results
```

## Reconstruction Requires

Reviewer access to relevant:

```text
evidence
rules
model outputs
adapter outputs
uncertainty
limitations
```

A reviewer does not need to reach the same subjective preference.

They should be able to understand the reasoning chain.

---

# PA-M46 — Explanation Completeness

## Purpose

Measure whether required explanation components are present.

## Required Components

Initial set:

```text
observation
evidence
substrate
regime
confidence
uncertainty
limitations
alternative interpretations
recommended action
```

## Formula

```text
EC =
  present_required_components
  /
  total_required_components
```

## Warning

A complete explanation can still be wrong.

```text
completeness != validity
```

---

# PA-M47 — Reviewer Override Rate

## Purpose

Measure how frequently qualified review changes automated interpretation or recommendation.

## Formula

```text
ROR =
  reviewer_overrides
  /
  reviewed_results
```

## Override Reason Classes

```text
incorrect_evidence
incorrect_rule
missing_context
unjustified_confidence
fairness_concern
applicability_error
model_scope_error
measurement_error
identity_error
other
```

## Direction

```text
descriptive
```

High or low override rates require interpretation.

---

# PA-M48 — Contest Resolution Rate

## Purpose

Measure whether subject or stakeholder contests receive documented resolution.

## Formula

```text
CRR =
  resolved_contests
  /
  submitted_contests
```

## Resolution States

```text
accepted
partially_accepted
rejected
unresolved
```

A contest does not guarantee reversal.

---

# 12. Operational Metrics

---

# PA-M49 — Profile Completion Rate

## Purpose

Measure the proportion of initiated profiles that can actually be completed under declared evidence requirements.

## Formula

```text
PCR =
  completed_profiles
  /
  initiated_profiles
```

## Direction

```text
descriptive
```

A high completion rate is not inherently desirable if completion requires unsupported inference.

---

# PA-M50 — Time to Review

## Purpose

Measure review latency.

## Formula

```text
TTR =
  review_completion_time
  -
  review_start_time
```

## Direction

```text
context_dependent
```

Faster review is not automatically better if review quality deteriorates.

---

# PA-M51 — Evidence Acquisition Burden

## Purpose

Represent the cost required to build a richer assessment.

Components may include:

```text
subject time
evaluator time
computational cost
tool requirements
accessibility burden
privacy burden
financial burden
specialist burden
```

## Preferred Representation

Initially:

```text
component-wise
```

rather than one universal number.

Example:

```yaml
evidence_burden:
  subject_time:
  evaluator_time:
  computational_cost:
  privacy_burden:
  accessibility_burden:
```

## Core Principle

A richer profile must justify its additional burden.

---

# PA-M52 — Decision Deferral Rate

## Purpose

Measure how often a decision is deferred because evidence or authority is insufficient.

## Formula

```text
DDR =
  deferred_decisions
  /
  decision_opportunities
```

## Direction

```text
descriptive
```

Interpret alongside:

```text
error reduction
harm avoidance
delay cost
review burden
fairness
```

The current experimental module has:

```text
decision_authority:
  none
```

so this metric is primarily intended for future context-validated workflows.

---

# Required Metric Pairings

Metrics should not be optimized in isolation.

Recommended pairings:

```text
predictive accuracy
+
calibration
```

```text
evidence coverage
+
evidence independence
```

```text
test-retest stability
+
relevant change sensitivity
```

```text
model-mismatch precision
+
model-mismatch recall
+
false-positive mismatch rate
```

```text
substrate effect magnitude
+
substrate replicability
+
substrate symmetry
```

```text
regime transition detection
+
false regime alarm rate
+
boundary error
```

```text
abstention rate
+
abstention utility
```

```text
counterfactual stability
+
relevant change sensitivity
```

```text
fairness difference
+
evidence coverage
```

```text
explanation completeness
+
evidence reconstruction
```

```text
predictive gain
+
evidence acquisition burden
```

---

# Metric Triads

Some module questions benefit from three-metric bundles.

## Model Mismatch Triad

```text
PA-M20  Precision
PA-M21  Recall
PA-M22  False Positive Rate
```

---

# Substrate Triad

```text
PA-M12  Effect Magnitude
PA-M13  Replicability
PA-M15  Specificity
```

with:

```text
PA-M14
```

as a directional-bias safeguard.

---

# Regime Triad

```text
PA-M16  Transition Detection
PA-M17  False Alarm Rate
PA-M18  Boundary Error
```

---

# Counterfactual Triad

```text
PA-M33  Irrelevant Stability
PA-M34  Relevant Sensitivity
PA-M35  Task-Order Sensitivity
```

---

# Fairness Symmetry Pair

```text
PA-M43
+
PA-M44
```

A system should measure unsupported favorable and adverse reinterpretation.

---

# RIQF Core Metric Set

A first real Resonant IQ Fingerprint pilot should consider at minimum:

```text
PA-M01  Dimension Evidence Coverage
PA-M02  Profile Evidence Coverage
PA-M03  Evidence Independence Ratio

PA-M04  Test-Retest Stability
PA-M05  Alternate-Form Stability
PA-M06  Inter-Rater Agreement
PA-M07  Profile Topology Stability

PA-M08  Convergent Association
PA-M09  Discriminant Separation
PA-M10  Incremental Explanatory Value

PA-M12  Substrate Effect Magnitude
PA-M13  Substrate Effect Replicability
PA-M14  Substrate Symmetry
PA-M15  Substrate Specificity

PA-M20  Model-Mismatch Precision
PA-M21  Model-Mismatch Recall
PA-M22  Model-Mismatch False Positive Rate

PA-M24  Cross-Observation Coherence
PA-M25  Profile Contradiction Density

PA-M28  Confidence Calibration Error
PA-M30  Abstention Rate
PA-M31  Abstention Utility
PA-M32  Unsupported Assertion Rate

PA-M33  Irrelevant Perturbation Stability
PA-M34  Relevant Change Sensitivity
PA-M35  Task-Order Sensitivity
PA-M36  Adapter Ablation Effect

PA-M37  Group Error Difference
PA-M38  Group Calibration Difference
PA-M42  Evidence Coverage Difference
PA-M43  False Favorable Reinterpretation Rate
PA-M44  False Adverse Reinterpretation Rate

PA-M45  Evidence Reconstruction Rate
PA-M46  Explanation Completeness

PA-M51  Evidence Acquisition Burden
```

Not every study needs all metrics.

Metric selection must follow the research question.

---

# Comparative Model Matrix

The module should avoid testing only:

```text
conventional model
vs
full Predictive Analytics
```

A more informative comparison is:

```text
M0:
  conventional scalar

M1:
  conventional subscales

M2:
  baseline multidimensional profile

M3:
  multidimensional
  + substrate observations

M4:
  M3
  + Structural Detection

M5:
  M4
  + RTT / regime observations

M6:
  M5
  + Resonance observations

M7:
  full Predictive Analytics ensemble
```

Possible additional ablations:

```text
M7 - FFT
M7 - Inverted Star
M7 - Structural Detection
M7 - RTT
M7 - Resonance
```

This helps identify what actually contributes.

---

# Comparative Reporting

For each model configuration, report where appropriate:

```text
predictive_performance
calibration
reliability
profile_stability
model-mismatch performance
substrate robustness
regime robustness
counterfactual robustness
fairness
evidence coverage
evidence independence
uncertainty quality
explainability
review burden
privacy burden
computational burden
```

---

# Metric Provenance

Every computed metric should carry provenance.

```yaml
metric_result:
  metric_id:
  metric_version:

  assessment_id:
  study_id:

  inputs:
  source_refs:

  calculation_method:

  output:
  uncertainty:

  threshold:
    status:

  calculated_at:

  validation_state:
```

---

# Metric Versioning

Definitions may change.

Therefore:

```text
PA-M20 v0.1
```

may not be directly equivalent to:

```text
PA-M20 v1.0
```

if the mismatch reference definition changed.

Profiles and validation reports should retain metric versions.

---

# Missing Data

Every metric should declare its missing-data policy.

Possible approaches:

```text
exclude_with_disclosure
unknown
not_applicable
partial_calculation
validated_imputation
```

The framework should not silently treat missing information as:

```text
zero
```

unless a validated measurement rule explicitly justifies it.

---

# Small Samples

Metric estimates from very small samples may be unstable.

A technically computable value is not necessarily an informative value.

Therefore:

```text
metric_computable
!=
metric_reliable
```

Sample size and uncertainty should accompany empirical metric reports.

---

# Confidence Intervals and Uncertainty

Where a statistical metric supports uncertainty estimation, empirical studies should report it.

Avoid:

```text
metric = 0.82
```

when the evidence actually supports something more like:

```text
estimate:
  0.82

uncertainty:
  substantial
```

The exact uncertainty representation depends on the method.

---

# Synthetic Metric Data

Synthetic examples may use invented metric values only when unmistakably labeled.

Preferred demonstration:

```yaml
PA-M20:
  status: not_tested
```

If synthetic values are needed to test software:

```yaml
PA-M20:
  value: 0.80
  data_type: synthetic_test_data
```

Never allow synthetic metric values to appear as real validation evidence.

---

# Metric Gaming

Any metric can become a target.

Possible gaming patterns:

```text
optimizing coverage by lowering evidence requirements

increasing precision by abstaining excessively

reducing false regime alarms by never detecting transitions

increasing review resolution rate by closing cases prematurely

reducing unsupported assertions by making trivial claims

improving profile stability by ignoring relevant change
```

Therefore metric families should be interpreted together.

---

# Goodhart Boundary

Conceptually:

> **When a metric becomes a target, behavior can shift toward optimizing the metric rather than the underlying goal.**

Predictive Analytics should therefore avoid governance based on one headline metric.

---

# Metric Conflict

Metrics may legitimately conflict.

Example:

```text
higher recall
  ->
more false positives
```

or:

```text
lower abstention
  ->
higher unsupported assertion rate
```

or:

```text
richer evidence
  ->
higher privacy burden
```

These are tradeoffs, not necessarily implementation errors.

---

# Metric Tradeoff Record

Suggested structure:

```yaml
tradeoff:
  metric_a:
  metric_b:

  observed_relationship:

  desired_balance:

  consequence:

  decision:
    status:
```

---

# Evidence Coverage Versus Burden

A core optimization problem:

```text
more evidence
  ->
better coverage
```

but:

```text
more evidence
  ->
more burden
  ->
more privacy exposure
```

Therefore:

```text
PA-M01 / PA-M02
```

should sometimes be examined with:

```text
PA-M51
```

---

# Precision Versus Coverage

A conservative framework may produce:

```text
high mismatch precision
low mismatch recall
high abstention
```

Another may produce:

```text
high recall
low precision
low abstention
```

Neither is universally better.

The intended use and harms matter.

---

# Metric Use in Human Review

Reviewers should not receive only:

```text
metric values
```

They should receive:

```text
metric meaning
source evidence
uncertainty
validation state
applicable limits
```

Metric dashboards can otherwise create false precision.

---

# Metric Use in AI Systems

AI systems consuming the metric registry should preserve:

```text
metric id
metric version
applicability
direction
uncertainty
validation state
```

They should not infer:

```text
high number = universally good
```

unless the metric explicitly defines that relationship.

---

# Cross-System Metric Comparisons

A metric may have different meaning across:

```text
human
AI
human-AI pair
team
organization
robotic system
```

Example:

```text
PA-M04 Test-Retest Stability
```

may be meaningful across all of them.

But expected stability and causes of variation may differ dramatically.

Cross-system numeric equality does not establish equivalent cognitive behavior.

---

# Metric Applicability Record

```yaml
metric_applicability:
  metric_id: PA-M04

  human:
    status: applicable

  ai:
    status: applicable

  human_ai_pair:
    status: applicable

  organization:
    status: context_dependent

  expected_behavior:
    system_specific: true
```

---

# Metric Threshold Record

Before operational use:

```yaml
threshold:
  metric_id:

  intended_use:
  population_or_system_class:

  value:
  direction:

  rationale:
  evidence:

  expected_error:
  subgroup_behavior:

  version:
  review_date:
```

A threshold without context should not become canon-wide policy.

---

# Metric Deprecation

A metric may be deprecated when:

- it fails reproducibility,
- it creates frequent misinterpretation,
- it duplicates a better metric,
- input requirements are unrealistic,
- fairness behavior is unacceptable,
- it encourages undesirable gaming,
- it no longer matches the architecture.

---

# Metric Rejection

A rejected metric should remain in lineage when useful.

Example:

```yaml
metric:
  id: PA-MXX

  lifecycle:
    state: rejected

  reason:
    failed_reliability

  retained_for:
    - lineage
    - negative_result
    - historical_reference
```

Negative measurement results are part of the research record.

---

# RIQF Metric Warning

The metrics in this registry mostly evaluate:

```text
the assessment system
```

not:

```text
the intelligence of the subject
```

For example:

```text
PA-M07
```

measures profile stability.

It is not a measure of intelligence.

```text
PA-M14
```

measures substrate symmetry.

It is not a measure of intelligence.

```text
PA-M45
```

measures explanation reconstruction.

It is not a measure of intelligence.

This distinction must remain explicit.

---

# No Metric-to-IQ Shortcut

Prohibited interpretation:

```text
high stability
+
high coherence
+
high structural score
=
high IQ
```

That composition is not established.

---

# Metric Failure Dashboard

A useful future dashboard should intentionally foreground failure indicators.

Example:

```text
Unsupported Assertion Rate        HIGH
False Mismatch Positive Rate      HIGH
Regime False Alarm Rate           MODERATE
Counterfactual Fragility          HIGH
Evidence Independence             LOW
Substrate Replication             LOW
```

This may be more important than a favorable capability profile.

---

# Model Comparison Example

Synthetic demonstration:

```yaml
M0:
  predictive_error: moderate
  evidence_burden: low
  explanation_completeness: low

M3:
  predictive_error: moderate
  evidence_burden: moderate
  explanation_completeness: high

M7:
  predictive_error: moderate
  evidence_burden: high
  explanation_completeness: high
```

Possible interpretation:

```text
M7 does not earn its added complexity
for predictive performance alone.
```

It might still provide explanatory value.

That claim would require separate evidence.

---

# Adapter Ablation Example

Synthetic demonstration:

```text
Full ensemble:
  performance = X

Without FFT:
  performance approximately X

Without RTT:
  performance approximately X

Without Structural Detection:
  performance materially decreases
```

Possible interpretation:

```text
Structural Detection:
  candidate incremental contribution

FFT:
  no detectable contribution in this study

RTT:
  no detectable contribution in this study
```

This is exactly the kind of result the framework should allow.

---

# Metric Review Questions

Before using a metric, ask:

1. What exactly does it measure?
2. What does it not measure?
3. What scale is appropriate?
4. Is direction meaningful?
5. Is a numeric representation justified?
6. Are inputs independently observed?
7. What assumptions are required?
8. How does missing evidence affect it?
9. How stable is it?
10. How does it behave across groups?
11. How does it behave across system classes?
12. What could game it?
13. What could make it misleading?
14. Which companion metric is required?
15. What threshold, if any, is justified?
16. Has the threshold been validated?
17. What decision authority does the metric have?
18. What evidence would cause the metric to be deprecated?

---

# Research Questions

1. Which metrics are reliably measurable?
2. Which are redundant?
3. Which are misleading?
4. Which require better operational definitions?
5. Which metrics improve model comparison?
6. Can evidence independence be measured reliably?
7. Can profile topology stability be measured meaningfully?
8. Can substrate effects be isolated from task effects?
9. Can substrate symmetry detect favorability bias?
10. Can regime transitions be detected without circularity?
11. Can false regime alarms be controlled?
12. Can model mismatch be defined independently enough to estimate precision and recall?
13. Does mismatch evidence strength add information beyond its components?
14. Can coherence be quantified without collapsing meaningful contradiction?
15. Can profile drift be measured without implying degradation?
16. Can confidence calibration work with ordinal confidence labels?
17. When is Brier score appropriate?
18. Can abstention utility be defined without hiding moral and operational tradeoffs?
19. Can unsupported assertions be audited reliably?
20. Can irrelevant perturbations be distinguished from relevant changes?
21. Does adapter ablation reveal useful simplifications?
22. Which adapters add negative value?
23. Can fairness metrics remain interpretable when group base rates differ?
24. How should evidence coverage disparities be measured?
25. Can false favorable reinterpretation be identified consistently?
26. Can false adverse reinterpretation be identified consistently?
27. Does evidence reconstruction predict explainability quality?
28. Does explanation completeness improve review?
29. What reviewer override rate indicates system problems?
30. How should contest quality be measured beyond resolution rate?
31. How should evidence burden be quantified?
32. Can privacy burden be represented without oversimplification?
33. Can metric gaming be detected?
34. Which metric pairs expose gaming attempts?
35. Which metrics generalize across humans and AI?
36. Which require system-specific definitions?
37. Which metrics should never be combined?
38. Which composites might eventually be justified?
39. How should metric uncertainty be reported?
40. What evidence would justify replacing the entire metric registry?

---

# Core Invariants

```text
metric != truth
metric != identity
metric != human_worth
formula != validity
precision != correctness
coverage != validity
stability != truth
coherence != correctness
confidence != accuracy
correlation != causation
effect_size != causal_effect
difference != unfairness
equality != fairness
review_rate != review_quality
override_rate != success
resolution_rate != justice
higher != always_better
lower != always_better
numeric != objective
composite != complete_representation
metric_count != evidence_count
adapter_count != evidence_count
synthetic_value != empirical_result
threshold != natural_boundary
profile_metric != intelligence_score
measurement != total_capability
decision_authority != inherited
canon_alignment != empirical_validation
```

---

# Closing Principle

Metrics are attractive because they turn complicated observations into comparable objects.

That is useful.

It is also dangerous.

The moment something becomes a number, it becomes easy to:

- rank,
- threshold,
- optimize,
- automate,
- compare,
- and overinterpret.

Predictive Analytics therefore treats every metric as another model.

Every metric has:

```text
a boundary
an assumption
an uncertainty
an intended use
a failure mode
```

The metric registry should help the framework discover not only when its richer observations succeed, but when they:

```text
fail to replicate
overfit
drift
become unfair
create false mismatch
inflate confidence
increase burden
or add no value
```

That is especially important for RIQF.

The goal is not to escape one reductive number by constructing fifty-two new ones.

> **The purpose of measurement is to expose structure responsibly, not to make uncertainty disappear behind arithmetic.**
