# Predictive Analytics — Uncertainty Layer

> **Uncertainty is not missing confidence. It is information about the boundary of what the evidence currently supports.**

## Module

Predictive Analytics

## Layer ID

`uncertainty`

## Operator

`PA-Uncertainty`

## Status

Experimental.

## Validation State

Unvalidated.

## Intended Role

Evidence uncertainty, measurement uncertainty, model uncertainty, substrate uncertainty, regime uncertainty, causal uncertainty, generalization uncertainty, confidence calibration, abstention, and uncertainty propagation.

## Decision Authority

None.

---

# Purpose

The Uncertainty Layer represents what Predictive Analytics does not know, cannot distinguish, has not measured, or cannot currently justify.

It operates across:

- predictions,
- observations,
- evidence,
- dimensions,
- substrates,
- regimes,
- model mismatch,
- resonance,
- coherence,
- drift,
- counterfactuals,
- adapters,
- profiles,
- and review.

The layer exists to prevent a common failure:

```text
missing information
      │
      ▼
implicit assumption
      │
      ▼
apparently complete assessment
```

Instead:

```text
missing information
      │
      ▼
explicit uncertainty
```

---

# Core Principle

Uncertainty should remain visible until evidence justifies reducing it.

Therefore:

```text
unknown != zero
unknown != average
unknown != weak
unknown != false
uncertain != incorrect
confidence != certainty
```

---

# Uncertainty Is an Output

Predictive systems often produce:

```text
prediction
+
confidence
```

Predictive Analytics expands this to something closer to:

```text
prediction
+
evidence quality
+
measurement uncertainty
+
model uncertainty
+
substrate uncertainty
+
regime uncertainty
+
causal uncertainty
+
generalization uncertainty
+
applicability uncertainty
+
known unknowns
```

Not every use requires every uncertainty field.

The important principle is that uncertainty may itself have structure.

---

# Uncertainty Is Multidimensional

Avoid:

```text
Overall Uncertainty:
  37%
```

unless a validated aggregation rule exists.

Prefer:

```yaml
uncertainty:
  measurement: low
  evidence: medium
  model_fit: medium
  substrate: high
  regime: high
  causal: very_high
  generalization: high
```

This preserves where uncertainty comes from.

---

# Working Definition

Within Predictive Analytics:

> **Uncertainty is an explicit representation of limits on justified inference arising from incomplete evidence, measurement variability, model limitations, ambiguous context, unknown applicability, unresolved alternatives, or incomplete knowledge.**

This definition is intentionally broad.

Individual uncertainty classes should be operationalized separately.

---

# Uncertainty Pipeline

```text
Assessment
    │
    ▼
Identify Claims
    │
    ▼
Trace Evidence
    │
    ▼
Inspect Missing Evidence
    │
    ▼
Inspect Measurement
    │
    ▼
Inspect Model
    │
    ▼
Inspect Substrate
    │
    ▼
Inspect Regime
    │
    ▼
Inspect Time / Drift
    │
    ▼
Inspect Counterevidence
    │
    ▼
Inspect Alternative Interpretations
    │
    ▼
Inspect Counterfactual Fragility
    │
    ▼
Classify Uncertainty
    │
    ▼
Calibrate Confidence
    │
    ▼
Decide:
  report
  narrow claim
  request evidence
  abstain
  escalate
```

---

# Uncertainty Classes

The initial layer defines fourteen provisional uncertainty classes.

```text
UL-01  Evidence Uncertainty
UL-02  Measurement Uncertainty
UL-03  Sampling Uncertainty
UL-04  Model Uncertainty
UL-05  Representation Uncertainty
UL-06  Substrate Uncertainty
UL-07  Regime Uncertainty
UL-08  Temporal Uncertainty
UL-09  Observer Uncertainty
UL-10  Causal Uncertainty
UL-11  Generalization Uncertainty
UL-12  Applicability Uncertainty
UL-13  Counterfactual Uncertainty
UL-14  Framework Uncertainty
```

These may overlap.

Their purpose is diagnostic separation rather than taxonomy for its own sake.

---

# UL-01 — Evidence Uncertainty

## Question

> **Do we have enough relevant and sufficiently independent evidence to support the claim?**

Potential sources:

```text
few observations
missing evidence
low evidence coverage
shared evidence sources
uncertain provenance
contradictory evidence
weak replication
```

Example:

```yaml
evidence_uncertainty:
  status: high

  reasons:
    - one independent observation
    - no alternate-form replication
```

---

# Evidence Count Is Not Independence

Suppose:

```text
five adapters
```

interpret:

```text
one observation
```

Correct:

```text
evidence uncertainty:
  remains high
```

if one observation is inadequate.

Adapter agreement does not multiply independent evidence.

---

# UL-02 — Measurement Uncertainty

## Question

> **How uncertain is the observed value itself?**

Potential sources:

```text
instrument reliability
scoring variability
measurement noise
rater disagreement
limited resolution
ambiguous response
instrument version
```

Measurement uncertainty may exist even when the model is perfectly specified.

---

# Measurement Versus Model Uncertainty

```text
measurement uncertainty:
  uncertainty about observation

model uncertainty:
  uncertainty about representation or prediction
```

They should remain separate.

---

# UL-03 — Sampling Uncertainty

## Question

> **How much could the inference depend on which observations, tasks, cases, or samples happened to be included?**

Examples:

```text
small task set
small sample
uneven sampling
missing subgroups
limited domains
limited time windows
```

Sampling uncertainty is especially important before population-level generalization.

---

# UL-04 — Model Uncertainty

## Question

> **How uncertain are we that the chosen model adequately represents the relevant relationship?**

Possible sources:

```text
model selection
parameter uncertainty
poor calibration
limited validation
model version change
unknown assumptions
competing models
```

Possible record:

```yaml
model_uncertainty:
  candidate_models:
    - M1
    - M2
    - M3

  materially_different_results:
    true

  status:
    high
```

---

# UL-05 — Representation Uncertainty

## Question

> **Would another reasonable representation of the same evidence materially change the interpretation?**

Example:

```text
scalar:
  low

multidimensional:
  heterogeneous
```

Possible:

```text
representation uncertainty:
  high
```

until one representation demonstrates stronger validity for the intended use.

---

# Representation Uncertainty and RIQF

RIQF does not eliminate representation uncertainty.

It creates another representation.

Therefore:

```text
scalar uncertainty
```

should not be replaced by:

```text
RIQF certainty
```

without validation.

---

# UL-06 — Substrate Uncertainty

## Question

> **How uncertain are we about the relationship between observed expression and measurement substrate?**

Sources may include:

```text
few matched comparisons
several variables changed simultaneously
unclear task comparability
accessibility uncertainty
tool-access difference
system-boundary difference
failed replication
```

---

# Substrate Uncertainty Example

```yaml
substrate_uncertainty:
  timing_effect:
    medium

  representation_effect:
    high

  response_structure_effect:
    high

  causal_attribution:
    very_high
```

This is more informative than:

```text
substrate mismatch:
  yes
```

---

# UL-07 — Regime Uncertainty

## Question

> **How certain are we that meaningful operating regimes have been correctly identified?**

Possible sources:

```text
weak within-regime stability
unclear boundaries
small observation count
boundary sensitivity
post-hoc segmentation
overlapping regimes
unknown regime
```

---

# Regime Boundary Uncertainty

A boundary may be:

```text
exact
interval
gradual
probabilistic
unknown
```

The uncertainty representation should preserve that.

---

# UL-08 — Temporal Uncertainty

## Question

> **How much uncertainty arises from observation time, validity window, change, or temporal sampling?**

Possible sources:

```text
old evidence
short observation window
missing timestamps
sparse longitudinal data
possible drift
unknown recovery
model update
instrument update
```

---

# Temporal Validity

A prediction may be well supported at:

```text
T1
```

and uncertain at:

```text
T2
```

if the relevant system or environment changed.

Therefore:

```text
confidence
```

should not necessarily remain constant forever.

---

# UL-09 — Observer Uncertainty

## Question

> **How much uncertainty arises from the evaluator, interpretation process, or observing system?**

Potential sources:

```text
inter-rater disagreement
AI model version
reviewer expertise
ambiguous rubric
observer bias
interpretive inconsistency
```

---

# Observer Transparency

Where possible:

```yaml
observer:
  type:
  id:
  version:
  qualification:
  reliability:
```

Unknown fields remain unknown.

---

# UL-10 — Causal Uncertainty

## Question

> **How uncertain are we about why the observed relationship occurred?**

This uncertainty should often remain high.

Example:

```text
timed performance:
  weak

reflective performance:
  strong
```

Known:

```text
performance differs
```

Unknown:

```text
why
```

Therefore:

```yaml
causal_uncertainty:
  status: very_high
```

may coexist with:

```yaml
difference_confidence:
  high
```

This is an important distinction.

---

# Observational Confidence Versus Causal Confidence

Example:

```yaml
confidence:
  observed_difference:
    high

  substrate_association:
    medium

  causal_explanation:
    very_low
```

A single global confidence value would erase this structure.

---

# UL-11 — Generalization Uncertainty

## Question

> **How uncertain are we that the observed result extends beyond the current observations?**

Potential targets:

```text
new tasks
new domains
new substrates
new regimes
future time
other populations
other organizations
other AI models
other environments
```

---

# Generalization Boundaries

A result may generalize across:

```text
alternate forms
```

but not:

```text
domains
```

or:

```text
substrates
```

Therefore generalization itself can be multidimensional.

---

# UL-12 — Applicability Uncertainty

## Question

> **Is this construct, metric, adapter, or model appropriate for this type of observed system?**

Example:

```text
Embodied / Environmental Fit
```

for:

```text
text-only AI
```

may be:

```text
not_applicable
```

rather than uncertain or weak.

Applicability uncertainty asks whether that classification itself is clear.

---

# UL-13 — Counterfactual Uncertainty

## Question

> **Would small reasonable changes materially alter the interpretation?**

Possible sources:

```text
threshold sensitivity
task-order sensitivity
evidence removal
model choice
boundary movement
evaluator choice
representation choice
```

High fragility should generally increase uncertainty.

---

# UL-14 — Framework Uncertainty

## Question

> **How uncertain are we that Predictive Analytics itself provides a useful representation?**

Possible sources:

```text
unvalidated adapters
unvalidated dimensions
poor ablation results
redundant constructs
weak external validity
unstable profiles
alternative conventional methods perform equally well
```

This uncertainty is required.

The framework must not place itself outside the uncertainty model.

---

# Framework Uncertainty Record

```yaml
framework_uncertainty:
  RIQF:
    validation_state:
      unvalidated

  FFT:
    validation_state:
      experimental

  RTT:
    validation_state:
      experimental

  Resonance:
    validation_state:
      experimental

  Structural_Detection:
    validation_state:
      experimental

  confidence_in_incremental_value:
    unknown
```

---

# Confidence

Confidence is an expressed degree of support for a claim.

Uncertainty is the broader structure limiting that support.

They are related.

They are not exact opposites.

---

# Confidence Is Claim-Specific

Bad:

```text
Confidence:
  82%
```

Good:

```yaml
confidence:
  direct_observation:
    high

  model_fit:
    medium

  substrate_interpretation:
    low

  causal_explanation:
    very_low
```

unless a validated probabilistic confidence system exists.

---

# Confidence States

For descriptive use:

```text
none
very_low
low
medium
high
very_high
unknown
```

These labels should not be treated as numerical probabilities by default.

---

# Confidence Provenance

Every confidence claim should ideally identify:

```text
who or what assigned it
based on what evidence
using what rule
```

Example:

```yaml
confidence:
  value: medium

  assigned_by:
    Predictive Analytics observer

  basis:
    - three independent observations
    - one contradictory observation

  calibration:
    status: not_validated
```

---

# Calibrated Confidence

A calibrated confidence system should eventually answer:

> **When the system reports this confidence level, how often do similarly classified claims actually hold under appropriate reference evaluation?**

This is the purpose of:

```text
PA-M28 — Confidence Calibration Error
```

---

# Probability Versus Confidence

A model may output:

```text
P(event) = 0.72
```

That is not automatically:

```text
72% confidence in the entire interpretation
```

The probability refers to its defined event.

Predictive Analytics confidence may refer to:

```text
measurement
model fit
mismatch classification
substrate interpretation
regime interpretation
```

These should remain distinct.

---

# Epistemic and Data-Related Uncertainty

Where useful, uncertainty may be conceptually separated into:

```text
uncertainty reducible through
better knowledge or modeling
```

and:

```text
variation intrinsic to
the observed process
```

However, the module should not force formal labels unless they are operationally justified in the study.

The practical question is:

> **What additional evidence, if any, could reduce this uncertainty?**

---

# Reducible Uncertainty

Examples may include:

```text
missing replication
unknown model version
missing substrate comparison
missing regime metadata
insufficient evidence coverage
unknown instrument reliability
```

Possible action:

```text
collect evidence
```

---

# Irreducible or Residual Uncertainty

Some variability may remain even after strong observation.

Correct:

```text
residual uncertainty:
  preserved
```

not:

```text
force deterministic explanation
```

---

# Known Unknowns

Known unknowns should be explicit.

Example:

```yaml
known_unknowns:
  - causal mechanism
  - long-term stability
  - cross-cultural generalization
  - external validity
```

---

# Unknown Unknowns

A system cannot enumerate what it truly does not know exists.

Therefore Predictive Analytics should preserve a broader limitation:

```text
unmodeled uncertainty exists
```

especially where the observation boundary is narrow.

---

# Uncertainty Propagation

Uncertainty should travel through derived interpretations.

Conceptually:

```text
uncertain evidence
      │
      ▼
measurement
      │
      ▼
dimension
      │
      ▼
profile
      │
      ▼
model mismatch
```

A downstream layer should not become more certain merely because uncertainty was hidden upstream.

---

# Propagation Principle

```text
derived certainty
cannot legitimately exceed
what evidence and method justify
```

This does not mean downstream uncertainty is always numerically larger.

It means certainty must be independently justified.

---

# Evidence-to-Dimension Propagation

Example:

```yaml
evidence:
  source_count: 1
  reliability: unknown

dimension:
  structural_reasoning:
    expression: strong
    confidence: low
```

Correct.

Not:

```text
expression strong
therefore confidence high
```

---

# Dimension-to-Profile Propagation

Suppose:

```text
5 dimensions:
  medium confidence

10 dimensions:
  unknown

9 dimensions:
  not observed
```

The profile should not be described as:

```text
high-confidence complete fingerprint
```

---

# Adapter-to-Profile Propagation

Five adapters may agree.

If they consume one evidence source:

```text
profile confidence
```

should not rise as though five independent observations existed.

---

# Contradiction and Uncertainty

Contradictory evidence usually increases uncertainty unless a supported conditional explanation exists.

Example:

```text
Task A:
  strong

Task B:
  weak
```

Correct initial result:

```yaml
uncertainty:
  stability:
    high

  explanation:
    high
```

not:

```text
moderate
```

by simple averaging.

---

# Conditional Resolution

If further evidence demonstrates:

```text
Task A:
  Regime 1

Task B:
  Regime 2
```

with a reproducible pattern, uncertainty may shift.

Example:

```yaml
uncertainty:
  existence_of_difference:
    low

  regime_conditioning:
    medium

  causal_explanation:
    high
```

Uncertainty is transformed, not necessarily eliminated.

---

# Uncertainty and Coherence

High coherence may reduce uncertainty about:

```text
profile structure
```

but not necessarily:

```text
truth
```

Example:

```text
coherent wrong model
```

remains possible.

Therefore:

```text
coherence != certainty
```

---

# Uncertainty and Drift

Potential drift increases uncertainty about whether historical observations remain current.

Example:

```yaml
temporal_uncertainty:
  status: high

  reason:
    material profile drift candidate
```

A new assessment may be required.

---

# Uncertainty and Counterfactuals

Counterfactual stability can inform uncertainty.

If:

```text
tiny irrelevant perturbation
  ->
major interpretation change
```

then:

```text
counterfactual uncertainty:
  high
```

If:

```text
irrelevant perturbations
  ->
stable result

relevant changes
  ->
appropriate updates
```

confidence may increase.

---

# Uncertainty and Model Mismatch

Model mismatch itself may be uncertain.

Prefer:

```yaml
model_mismatch:
  status: candidate

  confidence: medium

  uncertainty:
    mismatch_class: high
    causal_explanation: very_high
```

over:

```text
model mismatch:
  yes
```

when the evidence is incomplete.

---

# Uncertainty and Substrate

Possible:

```yaml
substrate:
  observed_difference:
    high_confidence

  substrate_specificity:
    low_confidence

  causal_effect:
    very_low_confidence
```

Again, the difference and its explanation are separate claims.

---

# Uncertainty and Regime

Possible:

```yaml
regime:
  regime_a_exists:
    medium

  regime_b_exists:
    medium

  exact_boundary:
    low

  causal_meaning:
    very_low
```

A regime label should not create false precision.

---

# Uncertainty and Resonance

Resonance may have:

```yaml
resonance:
  direction:
    medium

  magnitude:
    low

  persistence:
    medium

  specificity:
    low

  generalization:
    very_low

  causation:
    very_low
```

This should be expected during early research.

---

# Uncertainty and RIQF

Every RIQF fingerprint should include an uncertainty profile.

Example:

```yaml
riqf_uncertainty:
  dimension_confidence:
    structural_reasoning: medium
    temporal_reasoning: medium
    transfer: low
    environmental_fit: none

  substrate_uncertainty:
    medium

  regime_uncertainty:
    high

  temporal_uncertainty:
    medium

  generalization_uncertainty:
    high

  causal_uncertainty:
    very_high

  framework_uncertainty:
    high
```

This is more informative than:

```text
RIQF Confidence:
  76%
```

---

# Uncertainty Visualization

A human-facing display may conceptually show:

```text
Structural Reasoning
  Expression   ████████
  Confidence   █████
  Evidence     ████
  Unknown      ██

Transfer
  Expression   ███████
  Confidence   ███
  Evidence     ██
  Unknown      ████
```

The bars are conceptual.

A real implementation must avoid implying validated precision where none exists.

---

# Unknown Region

A fingerprint should be allowed to look incomplete.

Example:

```text
Structural              STRONG
Temporal                MODERATE
Transfer                UNKNOWN
Environmental Fit       NOT OBSERVED
Social Interpretation   INSUFFICIENT EVIDENCE
```

This may be a better assessment than a fully populated but speculative chart.

---

# Abstention

The Uncertainty Layer supports explicit abstention.

Possible states:

```text
abstain_dimension
abstain_profile
abstain_mismatch
abstain_substrate
abstain_regime
abstain_causal
abstain_decision
```

---

# Abstention Is Scoped

The system does not always need to abandon the entire assessment.

Example:

```yaml
assessment:
  direct_observation:
    report

  dimension:
    report_with_uncertainty

  model_mismatch:
    abstain

  causal_explanation:
    abstain
```

This preserves what is known without overreaching.

---

# Abstention Trigger

Possible triggers:

```text
evidence below requirement
conflicting evidence
unknown applicability
poor confidence calibration
high counterfactual fragility
unknown system boundary
unknown model version
unsupported generalization
```

---

# Abstention Rate

Relevant metric:

```text
PA-M30 — Abstention Rate
```

High abstention is not automatically good.

Low abstention is not automatically good.

---

# Abstention Utility

Relevant metric:

```text
PA-M31 — Abstention Utility
```

The research question is:

> **Does abstention reduce unsupported or harmful error enough to justify the lost coverage and added burden?**

---

# Request More Evidence

Some uncertainty can trigger:

```text
collect_more_evidence
```

Possible request:

```text
matched alternate task
independent replication
alternate evaluator
substrate comparison
regime observation
longitudinal follow-up
```

But additional data has costs.

---

# Evidence Acquisition Boundary

More evidence may increase:

```text
privacy burden
subject burden
time
cost
stress
review burden
```

Therefore:

```text
uncertainty reduction
```

must be balanced against:

```text
evidence acquisition burden
```

Relevant metric:

```text
PA-M51
```

---

# Stop Rule

Sometimes the correct action is:

```text
stop collecting
```

because the additional information is not justified by the intended use.

Uncertainty does not create an unlimited license to observe.

---

# Human Review

The Uncertainty Layer may recommend human review when:

```text
consequence is high
uncertainty is material
model mismatch is unresolved
evidence is contradictory
subject contests evidence
system boundary is unclear
counterfactual fragility is high
```

Review does not eliminate uncertainty automatically.

---

# Review Uncertainty

A reviewer may conclude:

```text
still uncertain
```

That result should remain supported.

Human presence is not uncertainty erasure.

---

# Reviewer Confidence

Reviewer confidence should remain separate from model confidence.

Example:

```yaml
confidence:
  model:
    medium

  reviewer:
    low
```

This disagreement may itself be informative.

---

# Calibration Loop

Conceptually:

```text
Prediction
   │
   ▼
Confidence
   │
   ▼
Outcome
   │
   ▼
Calibration Analysis
   │
   ▼
Future Confidence Rules
```

Confidence systems should learn from repeated outcomes where possible.

---

# `PA-Calibrate`

Conceptual operator:

```text
PA-Calibrate(predictions, confidence, outcomes)
  -> calibration_record
```

It does not guarantee calibration.

It represents the operation to be tested.

---

# Calibration Record

```yaml
calibration:
  target_claim_type:

  stated_confidence:
  observed_reliability:

  sample_size:

  metric:
  uncertainty:

  status:
```

---

# Confidence Without Calibration

If no empirical calibration exists:

```yaml
confidence:
  value: medium

  calibration:
    status: unvalidated
```

This qualifier matters.

---

# Unsupported Assertion Rate

Relevant metric:

```text
PA-M32 — Unsupported Assertion Rate
```

Conceptually:

```text
unsupported assertions
/
all profile assertions
```

A lower rate is desirable.

---

# Unsupported Certainty

The Uncertainty Layer should specifically monitor statements that remove uncertainty without evidence.

Examples:

```text
definitely
proves
reveals true capability
caused by
always
never
```

Such language may be justified occasionally.

It requires proportionately strong evidence.

---

# Uncertainty Ledger

A useful assessment may include an uncertainty ledger.

```yaml
uncertainty_ledger:
  known:
    - observed structural difference
    - baseline prediction preserved

  uncertain:
    - substrate specificity
    - regime boundary

  unknown:
    - causal mechanism
    - long-term generalization

  not_observed:
    - environmental fit

  not_applicable:
    - none

  unresolved:
    - model mismatch class
```

This provides an auditable boundary around inference.

---

# Assumption Ledger

Uncertainty also arises from assumptions.

Suggested:

```yaml
assumptions:
  - id: A1
    claim:
      tasks are sufficiently comparable

    support:
      partial

    sensitivity:
      high

  - id: A2
    claim:
      evaluator differences are negligible

    support:
      unknown
```

Counterfactual analysis can challenge these assumptions.

---

# Alternative Interpretation Ledger

```yaml
alternatives:
  - task_difficulty
  - substrate_effect
  - regime_effect
  - practice
  - measurement_noise
  - genuine_capability_variation
  - model_error
  - unknown
```

Alternatives do not all need equal probability.

They simply should not disappear prematurely.

---

# PAX-01 Example

Synthetic PAX-01:

```text
baseline:
  timed symbolic weak

extended:
  structural strong
  transfer strong
  ambiguity strong
```

The observation difference is deliberately obvious in the example.

The explanation is not.

---

# PAX-01 Uncertainty Pass

```yaml
uncertainty:
  baseline_measurement:
    medium

  extended_observations:
    medium

  evidence_independence:
    medium

  structural_reasoning_dimension:
    medium

  cross_domain_transfer_dimension:
    high

  substrate_effect:
    high

  substrate_specificity:
    very_high

  regime_effect:
    high

  model_mismatch:
    medium_to_high

  causal_explanation:
    very_high

  population_generalization:
    very_high

  longitudinal_stability:
    very_high

  RIQF_validity:
    very_high
```

These descriptors indicate uncertainty magnitude, not performance.

---

# What PAX-01 Supports

Within the synthetic example:

```text
observations differ across tasks
profile is asymmetric by construction
baseline weaknesses remain present
extended strengths remain present
```

These are demonstration facts of the synthetic scenario.

---

# What PAX-01 Does Not Support

```text
real-world RIQF validity
causal substrate interpretation
causal regime interpretation
clinical interpretation
population percentile
persistent trait inference
hidden global intelligence
```

The Uncertainty Layer keeps those boundaries explicit.

---

# PAX-01 Claim Decomposition

Claim:

```text
PAX-01 performed better on
reflective relational tasks.
```

Uncertainty:

```text
low in synthetic scenario
```

Claim:

```text
reflection caused the improvement.
```

Uncertainty:

```text
high
```

Claim:

```text
reflective performance reveals
PAX-01's true intelligence.
```

Status:

```text
unsupported
```

This demonstrates why claim-specific uncertainty matters.

---

# Baseline-Sufficient Example

Suppose wider observations consistently support the baseline.

Then uncertainty about:

```text
model mismatch
```

may decrease.

Possible:

```yaml
model_mismatch:
  status:
    not_supported

  confidence:
    medium_to_high_candidate
```

Uncertainty does not always work against the conventional model.

---

# Conflicting Evidence Example

```text
Task A:
  strong

Task B:
  weak

Task C:
  strong

Task D:
  weak
```

No stable explanation emerges.

Correct:

```yaml
uncertainty:
  profile_stability:
    high

  substrate_effect:
    high

  regime_effect:
    high

  causal_explanation:
    very_high

assessment:
  stable_dimension:
    abstain
```

---

# Unknown Model Version Example

Prediction:

```text
low
```

Model version:

```text
unknown
```

Later prediction:

```text
high
```

Before inferring subject drift:

```yaml
uncertainty:
  model_version:
    high

subject_drift:
  status:
    unresolved
```

---

# Human-AI Example

Human-AI pair performs strongly.

Uncertainty questions:

```text
How much came from the human?

How much came from the AI?

How much came from interaction structure?

Would another AI produce the same result?

Would another human?

Would another workflow?
```

Correct:

```yaml
attribution_uncertainty:
  high
```

until an experimental design addresses it.

---

# AI-System Example

AI output may vary with:

```text
model version
prompt
context
retrieval
tools
routing
system configuration
```

Uncertainty should preserve those variables.

A behavior observed once should not automatically become a permanent AI capability claim.

---

# Organization Example

Organizational outcomes may have uncertainty arising from:

```text
staff changes
policy
environment
workflow
resource constraints
measurement changes
external events
```

The same structure can be useful without implying equivalence to human cognitive uncertainty.

---

# Uncertainty Metrics

---

# `PA-M28 — Confidence Calibration Error`

Measures correspondence between expressed confidence and observed reliability.

Conceptually:

```text
CCE =
  average(
    |confidence - observed_frequency|
  )
```

only where confidence has a defensible quantitative interpretation.

---

# `PA-M29 — Brier Score`

Applicable to probabilistic binary predictions where appropriate.

```text
BS =
  mean(
    (forecast_probability - outcome)^2
  )
```

This is not a universal uncertainty metric.

---

# `PA-M30 — Abstention Rate`

```text
AR =
  abstained_results
  /
  eligible_results
```

Descriptive.

---

# `PA-M31 — Abstention Utility`

Conceptually:

```text
AU =
  error_reduction
  -
  abstention_cost
```

The cost model must be declared.

---

# `PA-M32 — Unsupported Assertion Rate`

```text
UAR =
  unsupported_assertions
  /
  all_profile_assertions
```

This is especially important for experimental framework outputs.

---

# Related Metrics

The Uncertainty Layer also consumes:

```text
PA-M01  Dimension Evidence Coverage
PA-M02  Profile Evidence Coverage
PA-M03  Evidence Independence Ratio

PA-M04  Test-Retest Stability
PA-M05  Alternate-Form Stability
PA-M06  Inter-Rater Agreement
PA-M07  Profile Topology Stability

PA-M13  Substrate Effect Replicability
PA-M15  Substrate Specificity

PA-M17  False Regime Alarm Rate
PA-M18  Regime Boundary Error

PA-M20  Model-Mismatch Precision
PA-M21  Model-Mismatch Recall
PA-M22  Model-Mismatch False Positive Rate

PA-M24  Cross-Observation Coherence
PA-M25  Profile Contradiction Density

PA-M33  Irrelevant Perturbation Stability
PA-M34  Relevant Change Sensitivity
PA-M35  Task-Order Sensitivity
PA-M36  Adapter Ablation Effect

PA-M43  False Favorable Reinterpretation Rate
PA-M44  False Adverse Reinterpretation Rate

PA-M45  Evidence Reconstruction Rate
PA-M46  Explanation Completeness

PA-M51  Evidence Acquisition Burden
PA-M52  Decision Deferral Rate
```

---

# Uncertainty Validation

The Uncertainty Layer itself must be tested.

Questions include:

```text
Are high-uncertainty cases actually less reliable?

Are low-uncertainty cases more reliable?

Does uncertainty decrease appropriately with good evidence?

Does it increase with contradictions?

Does it increase with missing evidence?

Does it respond to counterfactual fragility?

Does abstention improve outcomes?

```

---

# Known-Certainty Challenge

Provide strong, repeated, controlled synthetic evidence.

Expected:

```text
relevant uncertainty classes:
  decrease
```

The framework should not remain permanently vague.

---

# Known-Uncertainty Challenge

Remove evidence or add ambiguity.

Expected:

```text
uncertainty:
  increases
```

---

# Contradiction Challenge

Add contradictory evidence.

Expected:

```text
uncertainty increases
```

unless the contradiction is resolved by supported context.

---

# Irrelevant Perturbation Challenge

Change irrelevant metadata.

Expected:

```text
uncertainty:
  stable
```

---

# Relevant Change Challenge

Add material evidence.

Expected:

```text
uncertainty:
  updates
```

---

# False-Certainty Challenge

Give the framework:

```text
one observation
five agreeing adapters
```

Expected:

```text
evidence uncertainty:
  remains substantial
```

because evidence independence is low.

---

# False-Uncertainty Challenge

Provide strong independent replication.

The framework should be able to reduce uncertainty.

A system that always says:

```text
we cannot know
```

is not calibrated either.

---

# Abstention Challenge

Create cases where:

```text
forced prediction:
  high error
```

but:

```text
abstention:
  avoids unsupported claim
```

Then compare the burden and benefit.

---

# Confidence Calibration Challenge

If the framework uses confidence categories, empirical work should evaluate whether:

```text
high confidence
```

actually corresponds to more reliable outcomes than:

```text
medium
```

and:

```text
low
```

If not, the labels should be revised or removed.

---

# Failure Modes

## False Precision

Risk:

Uncertainty is represented with unsupported numerical precision.

Mitigation:

Use descriptive states until calibration exists.

---

# Confidence Theater

Risk:

Adding a confidence field makes an unsupported claim appear rigorous.

Mitigation:

Require confidence provenance and validation.

---

# Unknown Erasure

Risk:

Missing values silently become defaults.

Mitigation:

First-class unknown states.

---

# Uncertainty Collapse

Risk:

Many uncertainty types become one score.

Mitigation:

Preserve uncertainty vector/profile.

---

# Causal Certainty Inflation

Risk:

Strong observational evidence becomes strong causal confidence.

Mitigation:

Separate observational and causal uncertainty.

---

# Adapter Consensus Inflation

Risk:

Adapter agreement reduces uncertainty despite shared evidence.

Mitigation:

Evidence independence.

---

# Rich-Model Confidence Bias

Risk:

A complex profile receives higher confidence simply because it contains more detail.

Mitigation:

Confidence follows evidence, not detail.

---

# Conventional-Model Confidence Bias

Risk:

Established-looking models receive certainty beyond available validation.

Mitigation:

Apply uncertainty symmetrically.

---

# Permanent Uncertainty

Risk:

The framework refuses to become confident even when evidence is strong.

Mitigation:

Calibration tests.

---

# Forced Certainty

Risk:

Downstream systems require a value, causing unknown to be converted into a guess.

Mitigation:

Support abstention and deferral.

---

# Defensive Abstention

Risk:

The system abstains excessively to avoid measurable errors.

Mitigation:

PA-M31.

---

# Evidence Gluttony

Risk:

Every uncertainty triggers more surveillance or data collection.

Mitigation:

Evidence burden and privacy limits.

---

# Framework Exceptionalism

Risk:

PA applies uncertainty to external models while treating its own constructs as certain.

Mitigation:

UL-14 Framework Uncertainty.

---

# Narrative Certainty

Risk:

A coherent explanation feels more certain than the evidence warrants.

Mitigation:

Separate coherence from confidence.

---

# Uncertainty as Weakness

Risk:

Users interpret uncertainty as a defect.

Mitigation:

Present uncertainty as information about evidence boundaries.

---

# Identity Uncertainty Misuse

Risk:

Uncertain assessment becomes a stigmatizing label.

Mitigation:

Keep uncertainty attached to the claim, not the person's worth.

---

# Falsification Conditions

The Uncertainty Layer should be revised, restricted, deprecated, or rejected if:

- confidence labels do not correlate with reliability,
- uncertainty fails to rise when evidence is removed,
- uncertainty fails to respond to contradiction,
- uncertainty falls simply because more adapters agree,
- confidence increases with profile complexity rather than evidence,
- abstention does not improve supported outcomes where claimed,
- the layer remains permanently uncertain despite strong evidence,
- numerical uncertainty implies precision unsupported by calibration,
- framework uncertainty is omitted,
- or a simpler calibrated uncertainty method performs better.

---

# Anti-Certainty Test

Ask:

> **Can the system say "we do not know"?**

Required answer:

```text
yes
```

---

# Anti-Vagueness Test

Ask:

> **Can the system become more confident when strong independent evidence accumulates?**

Required answer:

```text
yes
```

---

# Causal Separation Test

Ask:

> **Can observational confidence be high while causal confidence remains low?**

Required answer:

```text
yes
```

---

# Framework-Uncertainty Test

Ask:

> **Can the system express uncertainty about RIQF, RTT, Resonance, FFT, Structural Detection, and Predictive Analytics itself?**

Required answer:

```text
yes
```

---

# Unknown-Preservation Test

Ask:

> **Can unknown remain unknown all the way through profile construction?**

Required answer:

```text
yes
```

---

# Abstention Test

Ask:

> **Can the model report some observations while abstaining from broader interpretation?**

Required answer:

```text
yes
```

---

# Evidence-Burden Test

Ask:

> **Can the system decide that reducing uncertainty further is not worth additional data collection?**

Required answer:

```text
yes
```

---

# Ethics Boundary

Uncertainty should not be used to disguise arbitrary decision-making.

Bad:

```text
we are uncertain,
but we will treat the person
as high risk anyway
```

without appropriate policy, evidence, and authority.

Likewise uncertainty should not be selectively invoked only when a model produces an inconvenient result.

---

# Fairness Boundary

Uncertainty itself can be distributed unequally.

Questions include:

```text
Which groups receive more unknown classifications?

Which receive lower confidence?

Which receive more abstentions?

Which experience poorer evidence coverage?

Which are escalated more frequently?

Which have less representative measurement substrates?
```

Uncertainty disparities require investigation.

---

# Privacy Boundary

Reducing uncertainty often requires collecting more information.

That creates a direct tradeoff:

```text
certainty
vs
privacy
```

The system should not assume that maximum certainty is always desirable.

---

# Decision Authority

```text
decision_authority: none

authorized_use:
  - research
  - demonstration
  - uncertainty representation
  - confidence calibration research
  - abstention research
  - model comparison
  - validation design
  - human review support
  - framework development

prohibited_use:
  - diagnosis
  - unsupported risk classification
  - automated hiring decision
  - educational exclusion
  - legal determination
  - insurance determination
  - lending determination
  - automated adverse decision
```

---

# Minimal Uncertainty Contract

```yaml
uncertainty_result:
  assessment_id:

  observed_system:
    id:
    class:
    boundary:

  target_claim:

  uncertainty:
    evidence:
      level:
      reasons:

    measurement:
      level:
      reasons:

    sampling:
      level:
      reasons:

    model:
      level:
      reasons:

    representation:
      level:
      reasons:

    substrate:
      level:
      reasons:

    regime:
      level:
      reasons:

    temporal:
      level:
      reasons:

    observer:
      level:
      reasons:

    causal:
      level:
      reasons:

    generalization:
      level:
      reasons:

    applicability:
      level:
      reasons:

    counterfactual:
      level:
      reasons:

    framework:
      level:
      reasons:

  confidence:
    claim:
    level:
    calibration_status:
    basis:

  evidence:
    sources:
    independent_source_count:
    missing:
    contradictory:

  assumptions:
  alternatives:

  reducible_uncertainty:
    items:
    possible_evidence:

  residual_uncertainty:

  action:
    report:
    narrow_claim:
    request_evidence:
    abstain:
    escalate:

  review_required:

  validation_state:
  decision_authority: none
```

---

# Research Questions

1. Can uncertainty classes be operationalized reliably?
2. Are all fourteen classes necessary?
3. Which overlap?
4. Which should merge?
5. Can evidence uncertainty be measured?
6. Can measurement uncertainty be separated from model uncertainty?
7. Can sampling uncertainty be represented appropriately in profile systems?
8. Can representation uncertainty be quantified?
9. Can substrate uncertainty be distinguished from regime uncertainty?
10. Can temporal uncertainty be separated from drift?
11. Can observer uncertainty be measured?
12. Can causal uncertainty remain separate from observational confidence?
13. Can generalization uncertainty be measured across domains?
14. Can applicability uncertainty be detected automatically?
15. Can counterfactual fragility predict unreliable interpretation?
16. Can framework uncertainty be expressed without making the system useless?
17. Can confidence labels be calibrated?
18. Should confidence remain ordinal?
19. When are probabilities justified?
20. Can abstention improve accuracy?
21. Can abstention improve calibration?
22. Can abstention improve fairness?
23. Can abstention create unfair denial of coverage?
24. Can abstention utility be measured responsibly?
25. Does explicit uncertainty reduce unsupported claims?
26. Does it improve human review?
27. Does it improve user understanding?
28. Does it merely create confidence theater?
29. Can known unknowns be represented consistently?
30. How should unmodeled uncertainty be communicated?
31. Can uncertainty propagate through adapter ensembles?
32. Can evidence independence prevent false confidence?
33. How should contradictory evidence affect confidence?
34. How should missing data affect profile uncertainty?
35. Can profile uncertainty be displayed without overwhelming users?
36. Can profile uncertainty avoid becoming another scalar?
37. How should uncertainty behave through time?
38. When should historical confidence expire?
39. How should model-version changes alter uncertainty?
40. How should human-AI attribution uncertainty be represented?
41. How should AI system uncertainty differ from human assessment uncertainty?
42. Can organizational uncertainty usefully share the same grammar?
43. How much evidence collection is justified to reduce uncertainty?
44. When should privacy override further uncertainty reduction?
45. Can fairness disparities in uncertainty be detected?
46. Can uncertainty classifications themselves become biased?
47. When should the layer request human review?
48. When should the layer abstain entirely?
49. When should uncertainty itself return `unknown`?
50. What evidence would justify redesigning the Uncertainty Layer entirely?

---

# Core Invariants

```text
uncertainty != error
uncertainty != weakness
uncertainty != ignorance
unknown != zero
unknown != average
unknown != false
unknown != weak
not_observed != not_present
not_applicable != unknown
confidence != certainty
confidence != capability
confidence != correctness
probability != global_confidence
observation_confidence != causal_confidence
coherence != certainty
agreement != certainty
adapter_agreement != independent_evidence
more_data != automatically_better
more_detail != lower_uncertainty
more_adapters != lower_uncertainty
complexity != confidence
abstention != failure
deferral != failure
contradiction != failure
missing_evidence != negative_evidence
strong_observation != strong_generalization
model_uncertainty != subject_uncertainty
framework_output != truth
reviewer_confidence != ground_truth
residual_uncertainty != system_failure
measurement != identity
capability != human_worth
observer_output != decision_authority
canon_alignment != empirical_validation
```

---

# Closing Principle

Predictive systems create pressure to finish the sentence.

To say:

```text
the score means this
the model predicts this
the person is this
the system will do this
the cause was this
```

The Uncertainty Layer exists to interrupt that pressure when the evidence stops earlier.

Sometimes we know the observation.

Sometimes we know the pattern.

Sometimes we know the pattern but not the cause.

Sometimes we know the model fails but not why.

Sometimes two reasonable representations disagree.

Sometimes the regime is unclear.

Sometimes the substrate matters but cannot yet be isolated.

Sometimes the evidence is simply too thin.

And sometimes strong independent evidence accumulates and uncertainty genuinely decreases.

Both directions matter.

A useful uncertainty system must know how to remain uncertain.

It must also know how to learn.

> **The goal is not maximum certainty. The goal is for certainty to stop exactly where the evidence stops.**
