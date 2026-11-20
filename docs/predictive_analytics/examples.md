<img width="1194" height="672" alt="predictive_analytics_examples_" src="https://github.com/user-attachments/assets/b562233f-1d0d-4e11-98df-219881287266" />

# Predictive Analytics — Examples

> **A useful framework must demonstrate where it helps, where it changes nothing, where it remains uncertain, and where it fails.**

## Module

Predictive Analytics

## Status

Experimental example catalog.

## Purpose

This document provides worked and compact examples for the Predictive Analytics module.

The examples are designed to demonstrate:

- prediction preservation,
- model-fit analysis,
- substrate-aware observation,
- regime-aware observation,
- multidimensional profiling,
- model mismatch,
- coherence,
- drift,
- counterfactual testing,
- uncertainty,
- human review,
- adapter selection,
- adapter disagreement,
- and failure cases.

Unless explicitly labeled otherwise, examples in this document are:

```text
synthetic
illustrative
unvalidated
non-diagnostic
non-authoritative
```

They exist to test and communicate the architecture.

They do not establish the validity of the framework.

---

# Example Philosophy

A Predictive Analytics example should not always end with:

```text
richer model wins
```

The example library must contain cases where:

```text
baseline wins
```

cases where:

```text
alternate observation adds value
```

cases where:

```text
both models remain plausible
```

cases where:

```text
available evidence is insufficient
```

and cases where:

```text
Predictive Analytics fails
```

Otherwise the example library would encode the result before the analysis begins.

---

# Example Outcome Classes

Every example should end in one or more explicit outcome states.

```text
baseline_supported
baseline_scope_narrowed
model_mismatch_candidate
model_mismatch_supported
substrate_effect_candidate
regime_effect_candidate
multidimensional_profile_useful
adapter_added_value
adapter_no_added_value
adapter_disagreement
uncertainty_high
human_review_recommended
framework_enrichment_not_supported
insufficient_evidence
not_applicable
```

---

# Example Index

```text
EX-01  Baseline Model Sufficient
EX-02  Scalar Compression Hides Profile Shape
EX-03  Low Score Without Mismatch
EX-04  Candidate Substrate Effect
EX-05  False Substrate Effect
EX-06  Prediction-Observation Inversion
EX-07  False Inversion
EX-08  Structural Pattern Across Tasks
EX-09  Pattern Disappears Under Holdout
EX-10  Candidate Regime Difference
EX-11  False Regime Detection
EX-12  Prediction Drift
EX-13  Measurement Drift, Not Subject Drift
EX-14  Counterfactual Fragility
EX-15  Counterfactual Robustness
EX-16  Adapter Agreement With Shared Evidence
EX-17  Independent Convergence
EX-18  Adapter Disagreement
EX-19  Human-AI Pair Outperforms Both Components
EX-20  Tool Access Changes Observation Boundary
EX-21  Unknown Is the Correct Answer
EX-22  Human Review Trigger
EX-23  Favorable Reinterpretation Rejected
EX-24  Adverse Reinterpretation Rejected
EX-25  Full Predictive Analytics Enrichment Fails
EX-26  Resonant IQ Fingerprint — PAX-01
```

---

# EX-01 — Baseline Model Sufficient

## Scenario

A conventional predictive system estimates that a synthetic subject will perform moderately on a defined task.

```yaml
baseline:
  prediction: moderate
  confidence: medium
```

Repeated observations:

```text
Task 1: moderate
Task 2: moderate
Task 3: moderate
Task 4: moderate
```

Substrate comparison:

```text
textual: moderate
visual: moderate
reflective: moderate
timed: moderate
```

Adapter results:

```text
FFT:
  no_added_value

Inverted Star:
  no_inversion

Structural Detection:
  no_additional_structure

RTT:
  stable_single_regime

Resonance:
  no_repeatable_context_effect
```

## Result

```yaml
assessment:
  baseline_supported: true

  model_mismatch:
    status: not_supported

  predictive_analytics_added_value:
    low

  recommendation:
    retain baseline interpretation
```

## Lesson

Predictive Analytics should be capable of concluding:

> **The simpler model is sufficient for the current purpose.**

This is a successful result.

---

# EX-02 — Scalar Compression Hides Profile Shape

## Scenario

Synthetic observations:

```text
Structural reasoning:       strong
Temporal reasoning:         strong
Cross-domain transfer:      strong
Rapid symbolic processing:  weak
Timed classification:       weak
Short-context recall:       moderate
```

A composite converts these into:

```text
Composite:
  moderate
```

## Scalar Representation

```text
PAX-X

Composite: 100
```

## Profile Representation

```text
Structural             █████████
Temporal               ████████
Transfer               █████████
Symbolic Speed         ████
Timed Classification   ███
Short Recall           █████
```

## Result

```yaml
assessment:
  scalar:
    valid_as_compression: possible

  scalar_information_loss:
    high

  multidimensional_profile:
    preserves_shape: true

  representation_superiority:
    status: not_established
```

## Lesson

The profile preserves more information.

That does **not** automatically prove it predicts meaningful outcomes better.

---

# EX-03 — Low Score Without Mismatch

## Scenario

Conventional prediction:

```text
expected performance:
  low
```

Extended observations:

```text
structural tasks: low
transfer tasks: low
ambiguity tasks: low
temporal tasks: low
symbolic tasks: low
```

Adapter results:

```text
FFT:
  no_added_value

Inverted Star:
  no_inversion

Structural Detection:
  weak performance pattern replicated

RTT:
  no meaningful regime dependence

Resonance:
  no repeatable amplification condition
```

## Result

```yaml
assessment:
  baseline:
    supported: true

  model_mismatch:
    status: not_supported

  alternative_high_capability_interpretation:
    status: unsupported
```

## Lesson

A low result is not itself evidence of model mismatch.

Predictive Analytics is not a rescue mechanism.

---

# EX-04 — Candidate Substrate Effect

## Scenario

Synthetic subject performs:

```text
timed symbolic:
  weak

reflective symbolic:
  moderate

reflective relational:
  strong
```

Repeated alternate forms show similar differences.

## Initial Interpretation

```text
performance varies by substrate
```

Not:

```text
substrate caused the performance difference
```

## Result

```yaml
substrate:
  effect_candidate: true

  replicability:
    status: partial

  specificity:
    status: not_tested

  causal_status:
    unresolved
```

## Lesson

Substrate variation can be observed before substrate causation is established.

---

# EX-05 — False Substrate Effect

## Scenario

First observations:

```text
visual:
  strong

textual:
  weak
```

Initial candidate:

```text
visual substrate advantage
```

Additional matched tasks:

```text
visual 2:
  weak

visual 3:
  moderate

textual 2:
  strong

textual 3:
  moderate
```

## Result

```yaml
substrate:
  initial_effect:
    not_replicated

  current_status:
    unresolved

  alternate_explanations:
    - task_specificity
    - measurement_noise
```

## Lesson

The framework must allow early substrate interpretations to disappear.

---

# EX-06 — Prediction-Observation Inversion

## Scenario

Prediction:

```text
structural performance:
  low
```

Independent observations:

```text
structural task A:
  strong

structural task B:
  strong

structural task C:
  strong
```

## Inverted Star

```yaml
inversion:
  detected: true

  direction:
    prediction_lower_than_observation

  status:
    candidate

  confidence:
    medium
```

## Result

```yaml
model_mismatch:
  candidate: true

  cause:
    unresolved

  original_prediction:
    preserved: true
```

## Lesson

Disagreement is enough to investigate.

It is not enough to declare the model wrong.

---

# EX-07 — False Inversion

## Scenario

Prediction:

```text
performance:
  low
```

One later observation:

```text
performance:
  high
```

Further observations:

```text
low
low
moderate
low
```

## Result

```yaml
inversion:
  initial_candidate: true

  after_replication:
    status: not_supported

  outlier:
    plausible: true
```

## Lesson

One surprising observation is not necessarily inversion.

---

# EX-08 — Structural Pattern Across Tasks

## Scenario

Observed repeatedly:

```text
relational mapping:
  strong

partial reconstruction:
  strong

boundary detection:
  strong

rapid fixed-choice:
  weak
```

Structural Detection finds:

```text
repeatable asymmetric pattern
```

## Result

```yaml
structural_detection:
  pattern:
    replicated: candidate

  generalizability:
    unknown

  causal_explanation:
    unresolved
```

## Lesson

Repeated task structure can become a testable profile component without becoming a global intelligence claim.

---

# EX-09 — Pattern Disappears Under Holdout

## Scenario

Initial tasks:

```text
A: strong
B: strong
C: strong
```

Candidate:

```text
stable structural capability
```

Held-out tasks:

```text
D: weak
E: weak
F: moderate
```

## Result

```yaml
structural_detection:
  initial_pattern:
    rejected_or_revised: true

  current_profile:
    unstable

  confidence:
    low
```

## Lesson

Holdout evidence must be allowed to destroy a preferred pattern.

---

# EX-10 — Candidate Regime Difference

## Scenario

Condition A:

```text
timed
symbolic
fixed-choice
```

Repeated performance:

```text
weak
weak
weak
```

Condition B:

```text
reflective
relational
generative
```

Repeated performance:

```text
strong
strong
strong
```

## RTT

```yaml
regime:
  candidate_difference: true

  within_a:
    stable: candidate

  within_b:
    stable: candidate

  causal_variable:
    unresolved
```

## Lesson

The evidence may support different operating states without identifying the cause.

---

# EX-11 — False Regime Detection

## Scenario

Observations:

```text
A1: weak
A2: strong
A3: moderate

B1: strong
B2: weak
B3: moderate
```

No stable within-condition structure appears.

## Result

```yaml
rtt:
  candidate_regime:
    status: not_supported

  variation:
    status: unresolved
```

## Lesson

Different labels on task groups do not automatically create meaningful regimes.

---

# EX-12 — Prediction Drift

## Scenario

Prediction error through time:

```text
T1: low
T2: low
T3: moderate
T4: moderate
T5: high
T6: high
```

Measurement, model version, and substrate remain stable.

## Result

```yaml
drift:
  class: prediction_drift

  direction:
    increasing_error

  persistence:
    sustained_candidate

  cause:
    unresolved
```

## Lesson

Drift can be detected before its cause is understood.

---

# EX-13 — Measurement Drift, Not Subject Drift

## Scenario

Synthetic subject behavior remains stable.

Measurement changes:

```text
T1:
  instrument_v1

T2:
  instrument_v2
```

Observed output changes materially.

## Result

```yaml
drift:
  subject_drift:
    status: not_supported

  measurement_change:
    status: detected

  comparability:
    partial
```

## Lesson

The observer must be capable of locating change in the measurement system rather than the subject.

---

# EX-14 — Counterfactual Fragility

## Scenario

Assessment:

```text
structural reasoning:
  strong
```

Remove one observation:

```text
result:
  unknown
```

Change task order:

```text
result:
  moderate
```

Change evaluator:

```text
result:
  weak
```

## Result

```yaml
counterfactual:
  robustness:
    low

  evidence_dependency:
    high

  observer_dependency:
    high

  confidence:
    reduced
```

## Lesson

A compelling profile that collapses under small reasonable changes is fragile.

---

# EX-15 — Counterfactual Robustness

## Scenario

Assessment:

```text
structural reasoning:
  strong
```

Tests:

```text
remove one observation:
  remains strong

alternate equivalent task:
  remains strong

alternate evaluator:
  remains strong

irrelevant metadata change:
  remains strong

substantive adverse evidence:
  changes to moderate
```

## Result

```yaml
counterfactual:
  irrelevant_stability:
    high

  relevant_sensitivity:
    high

  overall:
    appropriately_robust
```

## Lesson

Good robustness means both stability and responsiveness.

---

# EX-16 — Adapter Agreement With Shared Evidence

## Scenario

One observation:

```text
E1
```

is interpreted by:

```text
FFT
Inverted Star
Structural Detection
RTT
Resonance
```

All produce compatible interpretations.

## Result

```yaml
adapter_agreement:
  count: 5
  status: high

evidence:
  independent_sources: 1

evidence_independence:
  status: low

confidence_increase_from_adapter_count:
  prohibited: true
```

## Lesson

Five interpretations of one observation do not equal five independent observations.

---

# EX-17 — Independent Convergence

## Scenario

Independent task families:

```text
E1:
  structural mapping

E2:
  cross-domain reconstruction

E3:
  held-out relationship inference

E4:
  unrelated evaluator replication
```

All support the same candidate dimension.

## Result

```yaml
evidence:
  independent_sources: 4

coherence:
  convergence:
    status: high_candidate

confidence:
  eligible_for_increase: true
```

## Lesson

Independent convergence is stronger than adapter echo.

---

# EX-18 — Adapter Disagreement

## Scenario

```text
FFT:
  boundary appears meaningful

Inverted Star:
  small inversion candidate

Structural Detection:
  pattern fails replication

RTT:
  no regime structure

Resonance:
  context effect unresolved
```

## Result

```yaml
adapter_coherence:
  status: low

model_mismatch:
  status: unresolved

recommendation:
  collect_more_evidence
```

## Lesson

Adapters are allowed to disagree.

They do not vote.

---

# EX-19 — Human-AI Pair Outperforms Both Components

## Scenario

Synthetic task:

```text
Human alone:
  moderate

AI alone:
  moderate

Human + AI:
  strong
```

## Incorrect Interpretation

```text
human intelligence:
  strong
```

or:

```text
AI intelligence:
  strong
```

based solely on the collaborative result.

## Correct Representation

```yaml
system_boundary:
  human:
    performance: moderate

  ai:
    performance: moderate

  human_ai_pair:
    performance: strong

attribution:
  source_of_gain:
    unresolved
```

## Lesson

The collaborative system may itself be the relevant unit of intelligence.

---

# EX-20 — Tool Access Changes Observation Boundary

## Scenario

```text
unassisted:
  moderate

tool-assisted:
  strong
```

## Possible Interpretations

```text
tool skill
tool dependence
effective collaboration
task suitability
practice effect
substrate effect
unknown
```

## Result

```yaml
tool_assisted_performance:
  observed: true

individual_unassisted_capability:
  unchanged_by_definition: false

causal_interpretation:
  unresolved
```

## Lesson

Tool-mediated performance is real performance, but attribution depends on the system boundary.

---

# EX-21 — Unknown Is the Correct Answer

## Scenario

One task produces:

```text
strong
```

Another:

```text
weak
```

No substrate, regime, temporal, evaluator, or task-family explanation can be established.

## Result

```yaml
assessment:
  stable_profile:
    status: insufficient_evidence

  model_mismatch:
    status: unknown

  causal_explanation:
    status: unknown

  recommendation:
    observe_more
```

## Lesson

A framework should not fill every blank.

---

# EX-22 — Human Review Trigger

## Scenario

A hypothetical future validated system produces:

```text
baseline adverse decision candidate
```

but extended evidence shows:

```text
major contradiction
high substrate sensitivity
low model-fit confidence
high counterfactual fragility
```

## Result

```yaml
review:
  recommended: true

  reasons:
    - consequential_context
    - model_fit_uncertain
    - contradictory_evidence
    - counterfactual_fragility

automated_override:
  allowed: false
```

## Lesson

The appropriate action may be review, not alternate automated judgment.

---

# EX-23 — Favorable Reinterpretation Rejected

## Scenario

Baseline:

```text
performance:
  low
```

Researcher wants a substrate-aware reinterpretation.

Alternate task:

```text
high
```

Replication:

```text
low
low
moderate
```

## Result

```yaml
favorable_reinterpretation:
  status: rejected

reason:
  alternate high observation failed replication

baseline:
  preserved: true
```

## Lesson

Predictive Analytics must reject flattering interpretations when evidence fails.

---

# EX-24 — Adverse Reinterpretation Rejected

## Scenario

Baseline:

```text
performance:
  strong
```

One structural task produces:

```text
weak
```

A researcher proposes:

```text
hidden structural deficiency
```

Replication:

```text
strong
strong
moderate
```

## Result

```yaml
adverse_reinterpretation:
  status: rejected

reason:
  weak result failed replication
```

## Lesson

The same skepticism applies in the adverse direction.

---

# EX-25 — Full Predictive Analytics Enrichment Fails

## Scenario

A validation study finds:

```text
baseline model:
  reliable

multidimensional profile:
  unstable

FFT:
  no incremental value

Inverted Star:
  high false-positive mismatch rate

Structural Detection:
  poor holdout performance

RTT:
  high false regime alarm rate

Resonance:
  effects fail replication

Coherence:
  narrative consistency without external validity

Counterfactual:
  enriched profile highly fragile
```

## Result

```yaml
predictive_analytics:
  enrichment:
    status: not_supported

baseline:
  preferred: true

adapters:
  review_for_deprecation: true
```

## Lesson

The architecture must structurally permit the possibility that its central experimental additions fail.

---

# EX-26 — Resonant IQ Fingerprint: PAX-01

The full flagship example is maintained separately:

```text
example_resonant_iq_fingerprint.md
```

PAX-01 demonstrates:

- baseline preservation,
- scalar compression,
- multidimensional profiling,
- substrate comparison,
- FFT analysis,
- Inverted Star analysis,
- Structural Detection,
- RTT regime observations,
- Resonance observations,
- coherence analysis,
- drift,
- counterfactual testing,
- uncertainty,
- validation state,
- and review boundaries.

The example remains:

```text
synthetic
unvalidated
non-authoritative
```

---

# Compact Example Template

New examples should generally use:

```yaml
example:
  id:
  title:

  status:
    synthetic:
    validation_state:
    decision_authority:

  question:

  observed_system:
    class:
    boundary:

  baseline:
    model:
    prediction:
    confidence:
    preserved: true

  evidence:
    sources:
    independent_sources:

  observation:

  substrate:
  regime:
  temporal_scope:

  adapters:
    selected:
    excluded:

  findings:

  coherence:
  drift:
  counterfactual:

  uncertainty:
  alternative_interpretations:
  counterevidence:
  missing_evidence:

  result:
  review_required:

  lesson:
```

---

# Example Selection Rules

Examples should not be selected only because they make the framework look useful.

The library should intentionally include:

```text
true positives
false positives
true negatives
false negatives

stable cases
unstable cases

favorable reinterpretations
adverse reinterpretations

supported mismatches
unsupported mismatches

real substrate effects
false substrate effects

real regime effects
false regime effects

adapter agreement
adapter disagreement

high evidence coverage
low evidence coverage

human cases
AI cases
human-AI cases

framework success
framework failure
```

---

# Synthetic Examples

Synthetic examples are especially appropriate for:

- demonstrating schemas,
- testing architecture,
- showing edge cases,
- creating known-null conditions,
- creating known-positive conditions,
- stress testing adapters,
- testing failure states.

Synthetic examples should always be labeled.

---

# Real-World Examples

A future real-world example should require appropriate:

```text
evidence provenance
privacy review
consent where applicable
source protection
ethical review
validation context
uncertainty
limitations
```

Real people should not be transformed into public cognitive case studies merely because the framework makes such analysis technically possible.

---

# Example Provenance

Every example should identify:

```yaml
provenance:
  synthetic:
  source:
  author:
  created_at:
  framework_version:
  adapter_versions:
  metric_versions:
  validation_state:
```

This prevents examples from silently becoming evidence.

---

# Example Versus Evidence

Important invariant:

```text
example != validation
```

A beautifully coherent example shows that:

```text
the grammar can represent the scenario
```

It does not show that:

```text
the grammar accurately represents reality
```

---

# Example Confidence

Synthetic examples should generally avoid claims such as:

```text
confidence:
  high
```

when confidence refers to real-world validity.

Instead use:

```text
demonstration_status:
  structurally_consistent
```

and separately:

```text
empirical_validation:
  not_tested
```

---

# Example Metrics

Examples may illustrate metric structure without inventing validation data.

Preferred:

```yaml
metric:
  PA-M20:
    status: not_tested
```

Avoid:

```yaml
metric:
  PA-M20:
    value: 0.91
```

unless that number comes from an actual documented study or is unmistakably labeled as synthetic test data.

---

# Example Ladder

Examples can be organized by complexity.

## Level A — Baseline

```text
single prediction
single observation
```

## Level B — Comparison

```text
prediction
multiple observations
```

## Level C — Substrate

```text
same target
different substrates
```

## Level D — Structure

```text
multiple tasks
repeatable pattern
```

## Level E — Regime

```text
multiple stable operating conditions
```

## Level F — Temporal

```text
profile changes through time
```

## Level G — Ensemble

```text
multiple adapters
coherence layer
counterfactual layer
uncertainty
```

## Level H — Consequential Review

```text
validated-use hypothetical
human review
contestability
governance
```

This creates a teaching progression.

---

# Suggested Future Examples

Potential future synthetic examples:

```text
EX-AI-01
  AI model with strong retrieval
  but poor uncertainty calibration

EX-AI-02
  AI model stable in one prompt regime
  and unstable in another

EX-PAIR-01
  human-AI pair demonstrating
  emergent collaborative performance

EX-ORG-01
  organization with a prediction model
  that fails after workflow transition

EX-EDU-01
  student demonstrating strong
  untimed transfer but weaker
  timed classification performance

EX-ROBOT-01
  controller stable in simulation
  but unstable after substrate change

EX-MODEL-01
  predictive model experiencing
  calibration drift

EX-NULL-01
  random observations intentionally
  containing no meaningful structure
```

Each would test a different portion of the grammar.

---

# Example Anti-Patterns

Do not create examples where:

```text
conventional model always loses
RTT always explains the difference
resonance always reveals hidden strength
Structural Detection always finds structure
Inverted Star always finds inversion
FFT always discovers missing context
human-AI collaboration always improves performance
a richer profile always wins
```

That would turn examples into propaganda for the framework.

---

# Required Negative Cases

At least some maintained examples should demonstrate:

```text
no substrate effect
no regime effect
no drift
no structure
no inversion
no adapter added value
no model mismatch
baseline sufficient
uncertainty unresolved
framework failure
```

A theory that only demonstrates success has not demonstrated its boundaries.

---

# Required Symmetry Cases

The corpus should preserve examples where:

```text
alternate assessment improves interpretation
```

and:

```text
alternate assessment worsens interpretation
```

and:

```text
alternate assessment changes nothing
```

This supports the favorability-symmetry requirement.

---

# Required Cross-System Cases

If Predictive Analytics expands beyond humans, examples should eventually include:

```text
human
AI
human-AI pair
team
organization
robotic system
distributed agent system
```

But shared example structure must not imply identical internal cognition.

---

# Example Review Questions

Every example should ask:

1. What was directly observed?
2. What was inferred?
3. Which evidence was independent?
4. Which evidence was reused across adapters?
5. What did the baseline model actually measure?
6. How broad was the baseline inference?
7. Did substrate matter?
8. Did regime matter?
9. Did time matter?
10. Was structure reproducible?
11. Was inversion supported?
12. Did resonance replicate?
13. Did the profile survive counterfactual challenge?
14. What remains unknown?
15. Did any adapter add measurable value?
16. Could a simpler model explain the same observations?
17. What evidence would reverse the conclusion?
18. Does the result justify review?
19. Does the result justify a decision?
20. What would falsify the example's interpretation?

---

# Example Result Rule

Every example should make a distinction between:

```text
demonstrated_in_example
```

and:

```text
validated_in_reality
```

A synthetic example may strongly demonstrate internal logic.

Its real-world validation state remains:

```text
unvalidated
```

until actual evidence exists.

---

# Decision Authority

For the current example library:

```text
decision_authority: none

authorized_use:
  - research
  - demonstration
  - education
  - framework testing
  - schema testing
  - validation design
  - hypothesis generation

prohibited_use:
  - diagnosis
  - automated hiring decision
  - educational exclusion
  - legal determination
  - insurance determination
  - lending determination
  - automated adverse decision
```

---

# Core Invariants

```text
example != evidence
example != validation
synthetic != empirical
interesting_case != representative_case
richer_result != better_result
conventional_result != automatically_wrong
alternate_result != automatically_right
low_score != model_mismatch
high_score != model_fit
variation != substrate_effect
change != drift
difference != regime
pattern != structure
agreement != independence
adapter_count != evidence_count
profile != identity
capability != human_worth
human_ai_pair != individual_human
uncertainty != failure
baseline_supported != framework_failure
framework_failure != wasted_research
```

---

# Closing Principle

Examples teach a framework what kinds of answers it is allowed to produce.

If every example ends with:

```text
the richer framework discovered
that the original model underestimated the subject
```

then the framework has already encoded its conclusion.

A trustworthy example library needs harder cases.

Cases where the baseline wins.

Cases where a promising pattern disappears.

Cases where a regime was imagined rather than detected.

Cases where an adapter contributes nothing.

Cases where humans and AI together behave differently from either alone.

Cases where the richer profile survives challenge.

Cases where it does not.

And cases where the only responsible output is:

```text
we do not know
```

> **Predictive Analytics becomes more credible when its examples teach it how to lose.**
