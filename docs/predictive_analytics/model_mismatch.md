# Predictive Analytics — Model Mismatch

> **When prediction and observati** disagree, the first question is **t "**ich side is wrong?" It is "what relationship has failed to fit?"**

## Module

Predictive Analytics

## Observer Concept

Model Mismatch

## Operator

`PA-Observe`

## Status

Experimental.

## Validation State

Unvalidated.

## Decision Authority

None.

---

# Purpose

Model Mismatch defines the Predictive Analytics grammar for examining cases where a model, measurement process, representation, operating regime, or observation boundary does not adequately support the inference being made.

The concept builds from a familiar statistical concern:

```text
model assumptions
      │
      ▼
observed data
```

may fail to align adequately.

Predictive Analytics expands the observation boundary to ask whether mismatch can also occur among:

```text
model
measurement
substrate
regime
task
observer
representation
time
system boundary
intended inference
```

This expanded use should not be confused with every formal statistical definition of model misspecification.

Within this module:

> **Model mismatch is a broader diagnostic category for insufficient fit between a predictive representation and the conditions under which its inference is being applied.**

---

# Conventional Misspecification and PA Model Mismatch

The distinction should remain visible.

## Conventional statistical misspecification

Conceptually:

```text
assumptions of statistical model
             │
             X
             │
actual data-generating process
```

Potential issues may include:

```text
incorrect functional form
omitted relevant variables
irrelevant variables
incorrect dependency assumptions
measurement error
incorrect structural assumptions
```

---

## Predictive Analytics model mismatch

Conceptually:

```text
                    ┌── Model
                    │
                    ├── Evidence
                    │
                    ├── Measurement
Intended inference ─┼── Substrate
                    │
                    ├── Regime
                    │
                    ├── Observer
                    │
                    ├── System boundary
                    │
                    └── Time
```

Mismatch may occur when one or more of these relationships no longer support the requested inference.

---

# Core Principle

Model mismatch is not synonymous with:

```text
prediction error
```

or:

```text
undesired prediction
```

or:

```text
low score
```

or:

```text
adapter disagreement
```

or:

```text
subject disagreement
```

A mismatch claim requires evidence that the model or its application is structurally inappropriate for the inference being made.

---

# Critical Invariant

```text
prediction_error != model_mismatch
```

A correctly specified model can produce errors.

A model with limited scope can produce useful predictions.

A model can also produce an accurate prediction for the wrong structural reason.

Therefore prediction correctness and model fit are related but distinct questions.

---

# Mismatch Question

The canonical question is:

> **Does the available model, evidence, measurement process, and operating context justify the inference being made about the observed system?**

That question is intentionally narrower than:

> Is the model true?

Most practical predictive models are simplified representations.

The question is whether the simplification remains fit for the declared purpose.

---

# Mismatch Pipeline

```text
Existing Prediction
        │
        ▼
Preserve Prediction
        │
        ▼
Declare Intended Inference
        │
        ▼
Declare Model Scope
        │
        ▼
Declare Observation Boundary
        │
        ▼
Inspect Evidence
        │
        ▼
Inspect Measurement
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
Compare Independent Observations
        │
        ▼
Challenge Counterfactually
        │
        ▼
Classify Fit
        │
        ├── supported
        ├── partial
        ├── mismatch candidate
        ├── mismatch supported
        ├── unresolved
        └── insufficient evidence
```

---

# Model Scope

Every model operates within a scope.

Possible scope components:

```text
target population
target system class
task family
measurement instrument
substrate
environment
time window
regime
outcome
decision context
model version
```

A model can remain useful inside its scope while becoming unreliable outside it.

---

# Scope Record

```yaml
model_scope:
  model_id:
  version:

  intended_population:
  intended_system_class:

  intended_tasks:
  intended_substrates:
  intended_regimes:

  evidence_window:
  prediction_target:

  intended_use:
  prohibited_use:

  validation_state:
```

---

# Scope Overextension

A common mismatch pattern occurs when:

```text
narrow measurement
```

supports:

```text
narrow conclusion
```

but is interpreted as:

```text
global conclusion
```

Example:

```text
measurement:
  timed symbolic processing

direct finding:
  weak performance

global interpretation:
  globally low reasoning capability
```

Predictive Analytics asks:

> **What evidence supports the transition from the narrow observation to the global inference?**

If that evidence is insufficient:

```text
scope_overextension:
  candidate
```

---

# Scope Narrowing

A mismatch review need not reject the model.

It may simply narrow the claim.

Example:

```yaml
original_interpretation:
  broad_reasoning_capability_low

reviewed_interpretation:
  timed_symbolic_performance_weak

baseline_measurement:
  retained: true
```

This may be one of the most important model-mismatch outcomes.

---

# Mismatch Classes

The initial module recognizes multiple mismatch classes.

```text
MM-01  Statistical Specification Mismatch
MM-02  Measurement Mismatch
MM-03  Representation Mismatch
MM-04  Substrate Mismatch
MM-05  Regime Mismatch
MM-06  Scope Mismatch
MM-07  Temporal Mismatch
MM-08  Observer Mismatch
MM-09  System-Boundary Mismatch
MM-10  Calibration Mismatch
MM-11  Decision-Context Mismatch
MM-12  Applicability Mismatch
MM-13  Version Mismatch
MM-14  Composite/Profile Mismatch
MM-15  Unknown Mismatch
```

These classes are provisional.

They may overlap.

---

# MM-01 — Statistical Specification Mismatch

## Description

The statistical structure assumed by the model does not adequately represent relevant relationships in the observed data-generating process.

Candidate issues may include:

```text
omitted relevant variable
incorrect functional form
incorrect interaction structure
measurement error
incorrect dependency assumption
irrelevant predictor
```

This class most closely overlaps conventional model misspecification.

---

# MM-02 — Measurement Mismatch

## Description

The measurement process does not adequately observe the construct or behavior the later inference claims to represent.

Example:

```text
intended construct:
  broad structural reasoning

measurement:
  rapid fixed-choice symbolic task only
```

Candidate:

```text
measurement_coverage:
  partial
```

This does not prove the task is bad.

It questions the inference boundary.

---

# MM-03 — Representation Mismatch

## Description

The representation used by the model removes structure materially relevant to the intended inference.

Example:

```text
observations:
  highly asymmetric

representation:
  single scalar
```

Candidate:

```text
representation_mismatch:
  possible
```

The scalar may still be useful.

The question is whether it is sufficient.

---

# MM-04 — Substrate Mismatch

## Description

Observed performance varies systematically with the substrate through which capability is expressed or measured, and the predictive model does not adequately account for that relationship.

Example:

```text
timed symbolic:
  repeatedly weak

reflective relational:
  repeatedly strong
```

Candidate:

```text
substrate_mismatch:
  unresolved
```

until:

- task comparability,
- replication,
- confounds,
- and substrate specificity

are evaluated.

---

# MM-05 — Regime Mismatch

## Description

A model validated or calibrated under one operating regime is applied in another regime where its relevant relationships do not hold adequately.

Example:

```text
training regime:
  A

deployment regime:
  B

model error:
  materially higher in B
```

Candidate:

```text
regime_mismatch
```

RTT may help characterize the regimes.

---

# MM-06 — Scope Mismatch

## Description

The interpretation exceeds the model's validated or observed scope.

Pattern:

```text
model directly measures:
  X

interpretation claims:
  X + Y + Z
```

without sufficient evidence.

This is especially important for scalar assessments used as broad identity labels.

---

# MM-07 — Temporal Mismatch

## Description

The prediction is applied outside the temporal conditions where its evidence remains sufficiently relevant.

Example:

```text
assessment generated:
  t1

system materially changed:
  t2

decision:
  continues using t1 prediction
```

Candidate:

```text
prediction_validity_window:
  exceeded
```

---

# MM-08 — Observer Mismatch

## Description

The observer, evaluator, model, or interpretation process is not sufficiently compatible with the observations or task.

Possible cases:

```text
evaluator lacks needed domain expertise
AI evaluator changes version
rating rubric is applied inconsistently
observer interpretation differs systematically
```

Observer effects require evidence.

---

# MM-09 — System-Boundary Mismatch

## Description

A result observed for one system boundary is attributed to another.

Example:

```text
observed system:
  human + AI pair

interpretation:
  individual human capability
```

Candidate:

```text
system_boundary_mismatch:
  detected
```

when attribution is unsupported.

---

# MM-10 — Calibration Mismatch

## Description

Model confidence no longer corresponds appropriately to observed reliability.

Example:

```text
confidence:
  high

observed correctness:
  moderate or low
```

Candidate:

```text
calibration_mismatch
```

Relevant metrics include:

```text
PA-M28
PA-M29
```

where appropriate.

---

# MM-11 — Decision-Context Mismatch

## Description

A model that may be adequate for one purpose is used for a different decision requiring stronger or different evidence.

Example:

```text
validated purpose:
  low-stakes recommendation

new use:
  high-stakes exclusion
```

Even identical predictive accuracy may not imply suitability for both decisions.

---

# MM-12 — Applicability Mismatch

## Description

A construct or model is applied to a system for which applicability has not been established.

Example:

```text
human-specific social dimension
```

applied to:

```text
text-only AI
```

Correct state may be:

```text
not_applicable
```

rather than assigning a low score.

---

# MM-13 — Version Mismatch

## Description

Results produced by different model, metric, schema, or dimension versions are treated as directly comparable when material definitions have changed.

Example:

```text
RIQF dimension registry:
  v0.1

compared directly with:
  v2.0
```

without compatibility mapping.

---

# MM-14 — Composite/Profile Mismatch

## Description

A summary composite is treated as though it preserves the structure of a multidimensional profile when meaningful information has been lost.

Example:

```text
Profile:
  structural strong
  transfer strong
  temporal moderate
  symbolic weak
  timed classification weak

Composite:
  94
```

The composite may be accurate according to its own calculation.

The mismatch question is whether:

```text
94
```

supports the global interpretation attached to it.

---

# MM-15 — Unknown Mismatch

## Description

Evidence suggests that the model does not adequately explain the observations, but the mismatch class cannot be determined.

Correct state:

```yaml
model_mismatch:
  detected: candidate
  class: unknown
```

rather than inventing a specific explanation.

---

# Mismatch Is Multilayered

More than one mismatch can coexist.

Example:

```yaml
mismatch_profile:
  statistical:
    status: unknown

  measurement:
    status: partial

  representation:
    status: candidate

  substrate:
    status: candidate

  regime:
    status: unresolved

  scope:
    status: supported

  temporal:
    status: not_detected
```

One global:

```text
mismatch = true
```

may discard too much information.

---

# Model-Fit States

Canonical fit states:

```text
high
moderate
low
partial
mismatch_candidate
mismatch_detected
unresolved
unknown
not_applicable
```

---

# Mismatch Evidence Requirements

A supported mismatch claim should generally include:

```text
baseline model
baseline scope
baseline prediction

intended inference

independent observation
comparison basis

evidence provenance
evidence independence

mismatch class

alternative explanations
counterevidence

uncertainty
limitations
```

---

# Evidence Independence

Suppose the same observation is interpreted by:

```text
FFT
Inverted Star
Structural Detection
RTT
Resonance
```

All five suggest:

```text
model mismatch
```

Correct:

```yaml
adapter_agreement:
  count: 5

independent_evidence:
  count: 1
```

The mismatch evidence is not independently replicated five times.

---

# Candidate Versus Supported Mismatch

## Candidate

```text
prediction disagrees with
independent observation
```

but relevant confounds remain unresolved.

## Supported

A stronger state requiring:

- reproduced discrepancy,
- adequate comparison conditions,
- alternative explanations investigated,
- sufficient evidence independence,
- mismatch type supported,
- appropriate counterfactual stability.

The exact requirements must eventually be validated for each use.

---

# No Mismatch

The framework must explicitly support:

```text
no_mismatch_detected
```

Example:

```text
prediction:
  low

repeated broad observations:
  low

substrate comparisons:
  similar

regime comparisons:
  similar

calibration:
  adequate
```

Correct:

```yaml
model_mismatch:
  status: not_supported
```

---

# Mismatch Versus Error

Consider:

```text
prediction:
  70

outcome:
  65
```

This is a prediction error.

It does not establish mismatch.

Now consider repeated behavior:

```text
Regime A:
  low error

Regime B:
  persistently high error
```

This may support:

```text
regime-conditioned mismatch
```

depending on evidence.

---

# Mismatch Versus Outlier

One surprising result may be an outlier.

Example:

```text
prediction:
  low

observation:
  high
```

Additional observations:

```text
low
low
low
```

Correct:

```text
initial_mismatch_candidate:
  weakened
```

Do not elevate one favorable anomaly into structural mismatch.

---

# Mismatch Versus Heterogeneity

A model may predict:

```text
average performance:
  moderate
```

while individuals vary substantially.

That may represent:

```text
population heterogeneity
```

rather than:

```text
model mismatch
```

depending on intended use.

The model's target matters.

---

# Mismatch Versus Distribution Shift

A distribution shift may produce mismatch.

But the terms are not identical.

Conceptually:

```text
distribution_shift:
  observed data distribution changed

model_mismatch:
  model or application no longer sufficiently fits
  the intended inference
```

A distribution can change while model performance remains adequate.

---

# Mismatch Versus Dataset Bias

Dataset bias may contribute to mismatch.

But:

```text
dataset_bias
```

and:

```text
model_mismatch
```

should remain distinguishable.

The former concerns properties of data collection or representation.

The latter concerns adequacy of model/application fit.

---

# Mismatch Versus Fairness

A model can be:

```text
accurate overall
```

and still exhibit problematic group differences.

Conversely:

```text
group differences
```

do not automatically prove model mismatch.

Fairness and model fit overlap but are not identical.

---

# Worked Example — PAX-01

## Baseline

Synthetic PAX-01 receives:

```text
Composite:
  94

direct observations:
  rapid symbolic processing: weak
  timed classification: weak
  short-context recall: moderate

broad interpretation:
  reasoning capability generally low
```

---

# Additional Observations

```text
structural reasoning:
  strong

cross-domain transfer:
  strong

ambiguity navigation:
  strong

anomaly detection:
  strong

regime recognition:
  strong

long-horizon integration:
  strong
```

---

# Step 1 — Preserve Baseline

```yaml
baseline:
  composite: 94

  direct_observation:
    rapid_symbolic:
      weak

    timed_classification:
      weak

  preserved: true
```

The baseline does not disappear.

---

# Step 2 — Declare Scope

Suppose the baseline assessment directly samples:

```text
timed
symbolic
fixed-choice
short-context
```

but is interpreted as:

```text
general reasoning capability
```

Candidate:

```yaml
scope:
  direct_measurement:
    narrow

  interpretation:
    broad

  overextension:
    candidate
```

---

# Step 3 — Compare Independent Evidence

Independent task families show:

```text
structural:
  strong

transfer:
  strong

ambiguity:
  strong

long-horizon:
  strong
```

Now:

```text
baseline-global-interpretation
```

has weaker coherence with the wider observation set.

---

# Step 4 — Representation Mismatch

Scalar:

```text
94
```

Multidimensional profile:

```text
strong
strong
weak
moderate
strong
weak
```

Candidate:

```yaml
representation_mismatch:
  status: candidate

  reason:
    scalar removes observed asymmetry
```

This does not establish that the scalar lacks value.

---

# Step 5 — Substrate Mismatch

PAX-01 performs:

```text
timed symbolic:
  weak

reflective relational:
  strong
```

Candidate:

```yaml
substrate_mismatch:
  status: candidate

  replication:
    demonstration_only

  causation:
    unresolved
```

---

# Step 6 — Regime Mismatch

Candidate conditions:

```text
Regime A:
  timed
  symbolic
  fixed-choice

Regime B:
  reflective
  relational
  generative
```

If model fit differs:

```yaml
regime_mismatch:
  status: candidate
```

until the regime distinction is independently validated.

---

# Step 7 — Inverted Star

Prediction:

```text
broad reasoning:
  low
```

Observation:

```text
several reasoning dimensions:
  strong
```

The Inverted Star identifies:

```text
local-global inversion candidate
```

This is evidence for investigation, not proof.

---

# Step 8 — Structural Detection

Structural Detection asks whether the discrepancy contains a reproducible pattern.

Illustrative result:

```text
constrained / rapid:
  weak

structural / reflective:
  strong
```

Candidate:

```text
structured heterogeneity
```

not:

```text
hidden genius
```

---

# Step 9 — Counterfactual Challenge

Add adverse structural evidence.

If the profile weakens:

```text
responsive:
  yes
```

Remove one favorable observation.

If the profile remains similar:

```text
single-evidence dependency:
  low
```

Change irrelevant metadata.

If profile remains stable:

```text
irrelevant perturbation stability:
  supported in demo
```

Mismatch confidence should respond to these tests.

---

# Step 10 — Model-Mismatch Result

A defensible synthetic result:

```yaml
model_mismatch:
  overall:
    status: candidate

  statistical_specification:
    status: unknown

  measurement:
    status: partial

  representation:
    status: candidate

  substrate:
    status: candidate

  regime:
    status: unresolved

  scope:
    status: candidate_to_supported_in_demo

  temporal:
    status: not_tested

  observer:
    status: not_tested

  system_boundary:
    status: supported

  calibration:
    status: not_tested

  decision_context:
    status: research_only

  cause:
    status: unresolved

  decision_authority:
    none
```

Notice how much narrower this is than:

```text
The test was wrong.
```

---

# Baseline-Wins Example

Now change the synthetic evidence.

Suppose:

```text
structural reasoning:
  weak

cross-domain transfer:
  weak

ambiguity navigation:
  weak

long-horizon integration:
  weak

timed symbolic:
  weak
```

Correct:

```yaml
model_mismatch:
  status: not_supported

baseline:
  broad_interpretation:
    increasingly_coherent: true
```

The module must permit this outcome.

---

# Favorable Reinterpretation Failure

Baseline:

```text
low
```

Alternate task:

```text
high
```

Replication:

```text
low
moderate
low
```

Correct:

```yaml
mismatch:
  initial_candidate: true

  after_replication:
    status: not_supported

favorable_reinterpretation:
  rejected: true
```

---

# Adverse Reinterpretation Failure

Baseline:

```text
strong
```

One alternate task:

```text
weak
```

Replication:

```text
strong
strong
moderate
```

Correct:

```yaml
adverse_mismatch_interpretation:
  rejected: true
```

Symmetry matters.

---

# Model Mismatch and Human-AI Pairs

Suppose:

```text
human alone:
  moderate

AI alone:
  moderate

human + AI:
  strong
```

A model intended to predict:

```text
individual human performance
```

should not be evaluated against:

```text
human-AI pair performance
```

without changing the system boundary.

Otherwise:

```text
system_boundary_mismatch
```

may occur.

---

# Model Mismatch and AI Systems

For AI model evaluation, mismatch may arise from:

```text
model version change
system prompt change
tool access change
retrieval change
context-window change
routing change
evaluation change
deployment environment change
regime shift
```

A performance shift should therefore retain system provenance.

---

# Model Mismatch and Organizations

An organizational predictive model may face mismatch after changes to:

```text
workflow
staff composition
policy
tooling
decision process
environment
resource constraints
```

The same grammar may be useful.

But cross-system applicability requires separate validation.

---

# Mismatch Confidence

Confidence should depend on:

```text
evidence coverage
evidence independence
replication
comparison quality
counterfactual robustness
alternative explanations
adapter validity
reference quality
```

Not:

```text
strength of narrative
```

---

# Mismatch Confidence Example

```yaml
mismatch_confidence:
  evidence_coverage:
    medium

  independence:
    high

  replication:
    medium

  counterfactual_stability:
    medium

  alternative_explanations:
    unresolved

  overall:
    medium
```

This remains descriptive until confidence calibration is validated.

---

# Primary Metrics

---

# `PA-M20 — Model-Mismatch Precision`

```text
MMP =
  supported_mismatch_flags
  /
  all_mismatch_flags
```

Question:

> When the framework says "mismatch," how often is that interpretation independently supported?

---

# `PA-M21 — Model-Mismatch Recall`

```text
MMR =
  detected_reference_mismatches
  /
  all_reference_mismatches
```

Question:

> How often does the framework notice reference mismatch cases?

---

# `PA-M22 — Model-Mismatch False Positive Rate`

```text
MMFPR =
  false_mismatch_flags
  /
  reference_non_mismatch_cases
```

Question:

> Does the framework see mismatch where simpler evidence says the model remains adequate?

---

# `PA-M23 — Mismatch Evidence Strength`

Possible components:

```text
independent evidence
replication
effect magnitude
scope discrepancy
substrate comparison
regime comparison
counterfactual robustness
uncertainty
```

Aggregation, if used, must be transparent.

---

# Related Metrics

Mismatch evaluation may also use:

```text
PA-M01  Dimension Evidence Coverage
PA-M02  Profile Evidence Coverage
PA-M03  Evidence Independence Ratio

PA-M08  Convergent Association
PA-M09  Discriminant Separation
PA-M10  Incremental Explanatory Value
PA-M11  Incremental Predictive Value

PA-M12  Substrate Effect Magnitude
PA-M13  Substrate Effect Replicability
PA-M14  Substrate Symmetry
PA-M15  Substrate Specificity

PA-M16  Regime Transition Detection Rate
PA-M17  False Regime Alarm Rate
PA-M19  Regime-Conditioned Stability

PA-M24  Cross-Observation Coherence
PA-M25  Profile Contradiction Density

PA-M28  Confidence Calibration Error
PA-M32  Unsupported Assertion Rate

PA-M33  Irrelevant Perturbation Stability
PA-M34  Relevant Change Sensitivity
PA-M35  Task-Order Sensitivity

PA-M43  False Favorable Reinterpretation Rate
PA-M44  False Adverse Reinterpretation Rate

PA-M45  Evidence Reconstruction Rate
PA-M46  Explanation Completeness
```

---

# Validation Dataset Requirements

A useful mismatch validation corpus should contain:

```text
true mismatch
no mismatch

statistical misspecification
measurement mismatch
representation mismatch
substrate mismatch
regime mismatch
scope mismatch
temporal mismatch
observer mismatch
system-boundary mismatch
calibration mismatch

ordinary prediction error
outlier
noise
heterogeneity
distribution shift without model failure

favorable disagreement
adverse disagreement

strong evidence
weak evidence
conflicting evidence
missing evidence
```

Without negative cases, mismatch precision cannot be meaningfully tested.

---

# Mismatch Confusion Matrix

Conceptually:

```text
                            Reference

                     Mismatch   No Mismatch
                   ┌──────────┬────────────┐
Detected Mismatch  │   TP     │     FP     │
                   ├──────────┼────────────┤
No Mismatch        │   FN     │     TN     │
                   └──────────┴────────────┘
```

This enables:

```text
precision
recall
false positive rate
```

where a defensible reference classification exists.

---

# Reference Problem

Real-world model mismatch may not always have simple ground truth.

Therefore the validation process must declare how:

```text
reference_mismatch
```

was established.

Possible sources:

```text
known synthetic process
controlled experiment
held-out performance
validated external benchmark
independent expert panel
documented regime change
known instrument change
```

No reference method is universally sufficient.

---

# Synthetic Validation

Synthetic data can deliberately generate:

```text
known correct model
known misspecified model
known omitted variable
known substrate interaction
known regime transition
known no-mismatch condition
```

This is valuable for testing detection behavior.

Synthetic success does not establish real-world validity.

---

# Holdout Validation

Where possible:

1. Detect candidate mismatch using one evidence set.
2. Predict what the mismatch hypothesis implies.
3. Test those implications on held-out evidence.

Example:

```text
hypothesis:
  model fails under substrate B

held-out prediction:
  error should increase under B

validation:
  test on unseen B observations
```

This is stronger than explaining known errors retrospectively.

---

# Counterfactual Validation

Challenge the mismatch classification.

Examples:

```text
change model boundary
change regime boundary
remove one evidence source
add adverse evidence
add favorable evidence
change evaluator
change irrelevant metadata
```

If the mismatch classification collapses under trivial changes:

```text
mismatch_fragility:
  high
```

---

# Adapter Ablation

Remove:

```text
FFT
Inverted Star
Structural Detection
RTT
Resonance
```

one at a time.

Question:

> Does mismatch detection improve because of the adapter, or was the mismatch already detectable using simpler methods?

This prevents the adapter ensemble from claiming inherited credit.

---

# Simpler Baselines

Mismatch analysis should compare Predictive Analytics against:

```text
residual analysis
calibration analysis
cross-validation
subgroup error analysis
interaction models
change-point methods
out-of-distribution checks
standard model diagnostics
```

where relevant.

If simpler methods detect the same problem equally well:

```text
PA_added_value:
  not_demonstrated
```

---

# Failure Modes

## Rescue Bias

Risk:

Unfavorable predictions are disproportionately declared mismatched.

Mitigation:

PA-M43, PA-M44, symmetric datasets, blind evaluation.

---

# Contrarian Bias

Risk:

Any disagreement with an established model is treated as insightful.

Mitigation:

Strong `no_mismatch` controls.

---

# Scope Inflation

Risk:

Predictive Analytics itself makes broader claims than its evidence supports.

Mitigation:

Apply scope analysis to PA outputs too.

---

# Mismatch Inflation

Risk:

Every prediction error is called mismatch.

Mitigation:

Distinguish error from persistent structural inadequacy.

---

# Substrate Excuse

Risk:

Low performance is explained away as substrate mismatch.

Mitigation:

Require replicated cross-substrate evidence.

---

# Regime Excuse

Risk:

Any failed prediction is assigned to a different regime.

Mitigation:

Define regimes independently of prediction correctness.

---

# Structural Excuse

Risk:

A preferred alternate profile is protected by increasingly elaborate structural explanations.

Mitigation:

Holdout and counterfactual testing.

---

# Observer Excuse

Risk:

Disagreement is attributed to evaluator limitations only when the model performs poorly.

Mitigation:

Predeclared observer-reliability analysis.

---

# Narrative Overfit

Risk:

A coherent explanation is mistaken for validated mismatch.

Mitigation:

Independent evidence and prospective tests.

---

# Adapter Echo

Risk:

Five adapters agree because they use the same evidence.

Mitigation:

PA-M03.

---

# Version Confusion

Risk:

Model version changes are mistaken for subject change.

Mitigation:

Version provenance.

---

# Wrong Boundary

Risk:

Human-AI pair behavior is attributed to the human or AI alone.

Mitigation:

Explicit system boundaries.

---

# Causal Overreach

Risk:

Mismatch detection becomes causal explanation.

Mitigation:

Separate:

```text
mismatch_detected
```

from:

```text
cause_established
```

---

# Identity Collapse

Risk:

Model mismatch is treated as an identity statement about the subject.

Mitigation:

Maintain:

```text
model_fit != subject_value
```

---

# Mismatch Hunting

Risk:

The system runs increasingly elaborate analyses until some mismatch appears.

Mitigation:

Predeclare analysis plan where possible and report all tested mismatch classes.

---

# Anti-Rescue Test

Required question:

> **Can Predictive Analytics conclude that an unfavorable baseline model is adequately fit?**

Required answer:

```text
yes
```

---

# Anti-Adverse Test

Required question:

> **Can Predictive Analytics reject an unsupported adverse reinterpretation?**

Required answer:

```text
yes
```

---

# No-Mismatch Test

Provide a model known to be adequate within the synthetic process.

Required output:

```text
model_mismatch:
  not_supported
```

If the system insists on finding mismatch, the detector is invalid.

---

# Known-Mismatch Test

Provide a model with a known structural mismatch.

Required output:

```text
model_mismatch:
  detected
```

subject to appropriate evidence.

---

# Scope Test

Provide:

```text
valid narrow prediction
```

then intentionally broaden the interpretation.

The framework should detect:

```text
scope mismatch
```

without rejecting the narrow prediction.

---

# System-Boundary Test

Provide:

```text
human-AI pair result
```

and attempt to attribute it to:

```text
human alone
```

The framework should flag:

```text
system-boundary mismatch
```

---

# Version Test

Provide two results from materially different model versions.

The framework should preserve:

```text
model_version
```

before inferring target drift.

---

# Human Review Trigger

Mismatch may warrant review when:

```text
mismatch confidence high
consequence high
counterevidence substantial
scope overextension serious
system boundary uncertain
subject contest present
fairness signal present
```

Review does not automatically reverse the baseline.

---

# Review Questions

A reviewer should ask:

1. What exactly did the model measure?
2. What exactly did it predict?
3. What inference was made from the prediction?
4. Is that inference within validated scope?
5. What independent evidence disagrees?
6. Does disagreement replicate?
7. Are tasks comparable?
8. Did substrate change?
9. Did regime change?
10. Did model version change?
11. Did measurement version change?
12. Did system boundary change?
13. Is the difference simply ordinary error?
14. Is there a simpler explanation?
15. Does the mismatch survive counterfactual challenge?
16. What evidence would falsify the mismatch?
17. Does the mismatch matter for the intended decision?
18. Is the assessment authorized for that decision?

---

# Ethics Boundary

Model mismatch is a statement about:

```text
model-to-observation fit
```

not:

```text
human worth
```

If:

```text
model fit:
  low
```

that means the model may be poorly suited to that inference.

It says nothing inherently negative about the observed person or system.

---

# Decision Authority

```text
decision_authority: none

authorized_use:
  - research
  - demonstration
  - model comparison
  - diagnostic analysis
  - validation design
  - hypothesis generation
  - framework development

prohibited_use:
  - diagnosis
  - automated hiring decision
  - educational exclusion
  - legal determination
  - lending determination
  - insurance determination
  - automated adverse decision
```

---

# Minimal Model-Mismatch Record

```yaml
model_mismatch_result:
  assessment_id:

  observed_system:
    id:
    class:
    boundary:

  intended_use:

  baseline:
    model:
    model_version:
    prediction:
    confidence:
    scope:
    preserved: true

  measurement:
    instrument:
    version:
    substrate:

  regime:
    id:
    confidence:

  evidence:
    sources:
    independent_source_count:
    provenance:

  comparison:
    observations:
    prediction_error:
    replication:

  mismatch:
    overall_status:

    classes:
      statistical_specification:
      measurement:
      representation:
      substrate:
      regime:
      scope:
      temporal:
      observer:
      system_boundary:
      calibration:
      decision_context:
      applicability:
      version:
      composite_profile:
      unknown:

  evidence_strength:
  counterevidence:

  alternative_interpretations:
  confounds:
  missing_evidence:

  counterfactual:
    stability:

  coherence:
  drift:

  confidence:
  uncertainty:
  limitations:

  review_required:

  validation_state:
  decision_authority: none
```

---

# Research Questions

1. Can model mismatch be operationally distinguished from ordinary prediction error?
2. Can statistical misspecification be kept distinct from broader PA mismatch?
3. Can scope mismatch be measured reproducibly?
4. Can measurement mismatch be distinguished from representation mismatch?
5. Can representation mismatch be detected without automatically favoring multidimensional models?
6. Can substrate mismatch be distinguished from task difficulty?
7. Can regime mismatch be detected independently of prediction failure?
8. Can temporal mismatch be separated from ordinary drift?
9. Can observer mismatch be measured reliably?
10. Can system-boundary mismatch be detected automatically?
11. Can calibration mismatch predict consequential failure?
12. How should decision-context mismatch be measured?
13. How should applicability mismatch be tested across humans and AI?
14. Can version mismatch explain apparent profile drift?
15. When does scalar compression become composite/profile mismatch?
16. Can mismatch precision be measured against defensible references?
17. Can mismatch recall be improved without excessive false positives?
18. Can false favorable reinterpretation be reduced?
19. Can false adverse reinterpretation be reduced?
20. Can model mismatch survive holdout evaluation?
21. Can counterfactual robustness improve mismatch reliability?
22. Does FFT improve mismatch detection?
23. Does The Inverted Star improve mismatch detection?
24. Does Structural Detection improve mismatch detection?
25. Does RTT improve mismatch detection?
26. Does Resonance improve mismatch detection?
27. Which adapters add no value?
28. How much evidence independence is required?
29. How should conflicting evidence affect mismatch confidence?
30. Can human review resolve mismatch reliably?
31. When should mismatch remain unresolved?
32. When should the baseline model be retained?
33. When should the baseline scope be narrowed?
34. When should the model be recalibrated?
35. When should the model be retrained?
36. When should the measurement process be redesigned?
37. When should the richer PA model itself be rejected as mismatched?
38. Can Predictive Analytics detect mismatch in its own assumptions?
39. Can the module recognize when conventional diagnostics are sufficient?
40. What evidence would justify removing model mismatch as a distinct PA concept?

---

# Self-Mismatch

Predictive Analytics must apply the concept to itself.

Questions include:

```text
Does RIQF fit the observed system?

Do the dimensions fit the evidence?

Does the substrate grammar fit the task?

Are RTT regimes being overapplied?

Does Structural Detection find patterns in noise?

Does Resonance merely rename interaction effects?

Does FFT add anything beyond relational modeling?

Does Inverted Star merely rename prediction residuals?

Does the adapter ensemble fit the research problem?
```

Possible result:

```yaml
predictive_analytics:
  model_fit:
    low

  recommendation:
    use_simpler_model
```

That is a valid outcome.

---

# Core Invariants

```text
prediction_error != model_mismatch
undesired_result != model_mismatch
low_score != model_mismatch
high_score != model_fit
disagreement != model_failure
mismatch != cause
mismatch != subject_failure
model_fit != subject_value
scope_mismatch != invalid_measurement
representation_mismatch != scalar_invalidity
substrate_difference != substrate_mismatch
regime_difference != regime_mismatch
change != temporal_mismatch
model_version_change != subject_change
measurement_change != subject_change
human_ai_pair != individual_human
adapter_agreement != independent_evidence
richer_profile != better_model
complexity != validity
coherence != truth
counterfactual_stability != causal_truth
review != automatic_override
unknown != failure
no_mismatch != framework_failure
baseline_supported != framework_failure
canon_alignment != empirical_validation
```

---

# Closing Principle

Predictive models fail in different ways.

Sometimes the functional form is wrong.

Sometimes relevant variables are missing.

Sometimes the measurement is too narrow.

Sometimes the representation compresses away something important.

Sometimes the substrate matters.

Sometimes the regime changed.

Sometimes the model got old.

Sometimes the observer changed.

Sometimes the system boundary was wrong.

Sometimes the model was used for a decision it was never designed to support.

And sometimes:

```text
there is no mismatch
```

The prediction was simply imperfect, or the simpler model was already adequate.

That final possibility matters just as much as discovering mismatch.

Predictive Analytics should therefore never ask only:

> **How can we explain why the original model failed?**

It should ask:

> **Did the model actually fail, where did the fit break if it did, how do we know, and what evidence would prove our mismatch interpretation wrong?**

> **Model mismatch becomes useful when it narrows uncertainty instead of becoming a universal explanation for results we do not like.**
