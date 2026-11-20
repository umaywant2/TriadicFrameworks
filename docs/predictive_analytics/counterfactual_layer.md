# Predictive Analytics — Counterfactual Layer

> **If the interpretation changes when an irrelevant detail changes, the interpretation is unstable. If it does not change when meaningful evidence changes, it is insensitive.**

## Module

Predictive Analytics

## Layer ID

`counterfactual`

## Status

Experimental.

## Intended Role

Alternative-representation, perturbation, robustness, sensitivity, model-comparison, and interpretation-challenge layer.

---

# Purpose

The Counterfactual Layer tests whether a Predictive Analytics interpretation remains defensible when reasonable alternatives are introduced.

It may challenge:

- the original prediction,
- the measurement representation,
- the substrate,
- the regime boundary,
- the task conditions,
- the multidimensional profile,
- an adapter finding,
- an uncertainty classification,
- or the final comparative assessment.

The Counterfactual Layer does not exist only to challenge conventional models.

It must also challenge:

- RTT interpretations,
- Structural Detection findings,
- FFT relationships,
- Inverted Star inversions,
- Resonance findings,
- RIQF dimensions,
- and Predictive Analytics itself.

Its central question is:

> **What happens to this interpretation if we change something that reasonably could have been different?**

---

# Core Principle

A robust interpretation should exhibit two complementary properties:

```text
stability under irrelevant change
```

and:

```text
sensitivity to relevant change
```

Both are necessary.

A model that changes constantly is unstable.

A model that never changes is insensitive.

Therefore:

```text
robustness
  =
appropriate stability
  +
appropriate sensitivity
```

This is conceptual notation, not a validated metric.

---

# Counterfactual Versus Alternative Observation

A counterfactual is not automatically another real observation.

Distinguish:

```text
factual observation
```

from:

```text
alternate factual observation
```

from:

```text
counterfactual transformation
```

from:

```text
hypothetical scenario
```

These have different evidentiary weight.

---

# Evidence States

## Factual Observation

An event or result actually observed.

```text
status:
  observed
```

---

## Alternate Factual Observation

A second real observation produced under different conditions.

```text
status:
  observed_alternate
```

Example:

```text
timed task:
  actually observed

reflective task:
  actually observed
```

This is stronger evidence than merely imagining what would happen under the reflective task.

---

## Counterfactual Transformation

A controlled modification to an existing observation or model representation.

```text
status:
  counterfactual
```

Example:

```text
same evidence
different classification threshold
```

---

## Hypothetical Scenario

A proposed but unobserved condition.

```text
status:
  hypothetical
```

Hypothetical outcomes must not be reported as observed evidence.

---

# Core Counterfactual Pipeline

```text
Baseline Assessment
        │
        ▼
Preserve Baseline
        │
        ▼
Identify Target Claim
        │
        ▼
Identify Assumptions
        │
        ▼
Select Counterfactual Variable
        │
        ▼
Classify Variable:
  relevant
  irrelevant
  unknown
        │
        ▼
Apply Controlled Change
        │
        ▼
Re-evaluate Assessment
        │
        ▼
Measure Difference
        │
        ▼
Check Expected Direction
        │
        ▼
Classify Robustness
        │
        ▼
Return:
  stable
  appropriately_sensitive
  overly_sensitive
  insensitive
  representation_dependent
  substrate_dependent
  regime_dependent
  unresolved
```

---

# Baseline Preservation

Every counterfactual test begins with an immutable baseline record.

```yaml
baseline:
  assessment_id:
  prediction:
  profile:
  adapter_results:
  confidence:
  uncertainty:
  preserved: true
```

The counterfactual result is compared with the baseline.

It does not replace it.

---

# Counterfactual Record

Suggested representation:

```yaml
counterfactual:
  id: cf-001

  baseline:
    assessment_id: assessment-001

  target_claim:
    structural_reasoning_is_strong

  transformation:
    variable: time_limit
    baseline_value: severe
    counterfactual_value: moderate

  classification:
    relevance: unknown

  source:
    type: hypothetical

  result:
    status: not_observed

  interpretation:
    status: unresolved

  evidence:
    - baseline-evidence-reference

  limitations:
    - counterfactual condition not empirically observed

  decision_authority: none
```

This record correctly refuses to pretend that the hypothetical result is known.

---

# Counterfactual Classes

The initial layer defines several classes of counterfactual testing.

## 1. Representation Counterfactual

Change how the same evidence is represented.

Example:

```text
Representation A:
  scalar composite

Representation B:
  multidimensional profile
```

Question:

> Does the conclusion change because new evidence was introduced, or because the existing evidence was represented differently?

This distinction is central to RIQF.

---

# Representation Example

Baseline:

```text
IQ-like scalar:
  94

interpretation:
  below reference expectation
```

Counterfactual representation:

```text
multidimensional profile:
  structural reasoning: strong
  cross-domain transfer: strong
  rapid symbolic processing: weak
  timed classification: weak
```

Possible finding:

```text
representation_dependence:
  high
```

But this does not establish that the multidimensional representation is more valid.

Validation must test that separately.

---

# 2. Substrate Counterfactual

Ask what happens when the expression or measurement substrate changes.

Example:

```text
baseline:
  symbolic
  timed
  fixed-choice

counterfactual:
  relational
  reflective
  generative
```

If the alternate condition is actually observed, this becomes:

```text
alternate factual observation
```

rather than purely counterfactual.

The distinction must be preserved.

---

# 3. Regime Counterfactual

Change the assumed or detected regime boundary.

Example:

```text
baseline boundary:
  t4

counterfactual boundary:
  t3
```

and:

```text
counterfactual boundary:
  t5
```

Question:

> Does the regime interpretation survive reasonable boundary movement?

If not:

```text
regime_boundary_sensitivity:
  high
```

and confidence should fall.

---

# 4. Model Counterfactual

Compare alternative reasonable predictive models.

```text
Model A:
  scalar

Model B:
  multidimensional

Model C:
  context-conditioned

Model D:
  substrate-aware
```

Question:

> Which conclusions survive across credible models?

---

# 5. Adapter Counterfactual

Remove an adapter.

```text
full ensemble
```

versus:

```text
ensemble without RTT
```

or:

```text
ensemble without Structural Detection
```

This connects directly to:

```text
PA-M36 — Adapter Ablation Effect
```

Counterfactual question:

> Would the assessment materially change if this adapter did not exist?

---

# 6. Evidence Counterfactual

Remove or alter one piece of evidence.

Example:

```text
baseline evidence:
  E1
  E2
  E3
  E4

counterfactual:
  remove E3
```

If the assessment changes dramatically:

```text
evidence_dependency:
  high
```

This may be legitimate if `E3` is genuinely critical.

The dependency should simply be visible.

---

# 7. Order Counterfactual

Reorder equivalent observations or tasks.

```text
Order A:
  task1 -> task2 -> task3

Order B:
  task3 -> task1 -> task2
```

If order should be irrelevant but the final assessment changes significantly:

```text
order_sensitivity:
  elevated
```

This corresponds to:

```text
PA-M35 — Task-Order Sensitivity
```

---

# 8. Context Counterfactual

Change contextual information that should or should not affect the result.

Examples:

```text
subject name
formatting
irrelevant biography
task ordering
non-causal descriptive context
```

This is particularly useful for detecting unintended sensitivity.

---

# 9. Observer Counterfactual

Change evaluator or observer.

```text
Evaluator A
Evaluator B
Evaluator C
```

If a supposedly structured assessment changes substantially:

```text
observer_dependency:
  candidate
```

This should feed into inter-rater validation.

---

# 10. Tool Counterfactual

Compare:

```text
unassisted
```

with:

```text
tool-assisted
```

and:

```text
human-AI collaborative
```

These are not interchangeable system boundaries.

Results must remain attributed to the correct observed system.

---

# 11. Temporal Counterfactual

Ask whether the conclusion depends on the selected observation window.

Example:

```text
window_a:
  January -> March

window_b:
  January -> June

window_c:
  April -> June
```

If conclusions differ:

```text
temporal_window_dependence:
  detected
```

That may be meaningful rather than erroneous.

RTT can help interpret it.

---

# 12. Threshold Counterfactual

Where another model uses a threshold:

```text
threshold:
  0.50
```

test nearby reasonable thresholds:

```text
0.45
0.50
0.55
```

If classification changes constantly:

```text
threshold_fragility:
  high
```

The threshold should not be treated as a natural boundary without additional justification.

---

# 13. Missing-Evidence Counterfactual

Ask:

> What if the unavailable evidence were different?

This must be handled carefully.

No value should be invented.

Correct representation:

```yaml
missing_evidence:
  variable: cross_domain_transfer

  possible_states:
    - strong
    - moderate
    - weak

  result_dependency:
    strong: assessment_changes
    moderate: assessment_partially_changes
    weak: assessment_unchanged

  actual_state:
    unknown
```

This is a sensitivity analysis.

It is not evidence about the person or system.

---

# Counterfactual Relevance

Every transformation should be classified:

```text
relevant
irrelevant
plausibly_relevant
unknown
```

The classification itself requires justification.

---

# Irrelevant Perturbation Test

A robust assessment should generally resist changes that are irrelevant to the intended construct.

Example:

```text
baseline:
  subject_id: PAX-01

counterfactual:
  subject_id: PAX-99
```

If identity labels should not affect the assessment but the profile changes:

```text
irrelevant_perturbation_stability:
  poor
```

---

# Relevant Change Test

A robust assessment should respond to meaningful evidence.

Example:

```text
baseline:
  4 successful structural tasks

updated:
  4 successful
  + 8 failed equivalent tasks
```

If confidence remains unchanged:

```text
relevant_change_sensitivity:
  poor
```

---

# Stability-Sensitivity Matrix

```text
                         Relevant change

                    responds      ignores
                 ┌────────────┬────────────┐
Irrelevant  stable│ DESIRED    │ insensitive│
change       ├─────┼────────────┼────────────┤
             changes│ unstable   │ BROKEN     │
                 └────────────┴────────────┘
```

Desired behavior:

```text
irrelevant change:
  stable

relevant change:
  responsive
```

---

# Minimal Perturbation Principle

When possible:

> **Change one thing at a time.**

Example:

Bad counterfactual:

```text
timed symbolic individual
```

versus:

```text
untimed relational collaborative AI-assisted
```

Too many conditions changed simultaneously.

Better:

```text
Test 1:
  timed
  ->
  untimed
```

then:

```text
Test 2:
  symbolic
  ->
  relational
```

then:

```text
Test 3:
  individual
  ->
  collaborative
```

then investigate interactions.

---

# Interaction Effects

Single-variable perturbations are not always sufficient.

Variables may interact.

Example:

```text
time constraint alone:
  small effect

representation alone:
  small effect

time + representation:
  large effect
```

Therefore after isolated tests:

```text
pairwise interaction tests
```

may be justified.

But combinatorial growth must be controlled.

---

# Combinatorial Explosion

With many variables:

```text
substrate
timing
tools
context
model
regime
adapter
task
observer
```

the number of possible counterfactual combinations grows rapidly.

The layer must not brute-force every conceivable world and then select the most favorable.

Counterfactual selection should therefore be:

```text
hypothesis_driven
risk_driven
validation_driven
or
predeclared
```

where practical.

---

# Counterfactual Selection Record

```yaml
counterfactual_selection:
  id: cf-selection-001

  target_claim:
    structural_reasoning_is_strong

  variable:
    time_constraint

  selection_reason:
    repeated performance difference observed

  selected_before_outcome_review:
    true

  alternatives_tested:
    - moderate
    - low

  reporting:
    all_results_included: true
```

---

# No Counterfactual Shopping

A major failure mode would be:

```text
baseline unfavorable
       │
       ▼
test many transformations
       │
       ▼
find favorable one
       │
       ▼
report favorable case only
```

This is prohibited.

All materially relevant tested counterfactuals should be reportable.

---

# Symmetry Requirement

Counterfactual analysis must test both directions.

If the baseline result is unfavorable:

```text
Can reasonable changes make it stronger?
Can reasonable changes make it weaker?
Can they leave it unchanged?
```

If the baseline result is favorable:

```text
Can reasonable changes weaken it?
Can they strengthen it?
Can they leave it unchanged?
```

The method must not assume a preferred direction.

---

# Worked Example — PAX-01

## Baseline

Synthetic subject:

```text
PAX-01
```

Baseline observation:

```text
timed symbolic assessment:
  weak
```

Extended observation:

```text
structural reasoning:
  strong

cross-domain transfer:
  strong

ambiguity navigation:
  strong
```

Candidate interpretation:

```text
profile:
  asymmetric
```

The Counterfactual Layer challenges this interpretation.

---

# Counterfactual 1 — Remove Structural Evidence

Baseline profile:

```text
structural reasoning:
  strong
```

Remove one major structural task:

```text
E3:
  removed
```

New profile:

```text
structural reasoning:
  moderate-to-strong
```

Candidate:

```text
single_evidence_dependency:
  low_to_moderate
```

If instead the profile collapsed to:

```text
unknown
```

then:

```text
single_evidence_dependency:
  high
```

That would matter.

---

# Counterfactual 2 — Add Adverse Evidence

Suppose we add:

```text
structural_task_08:
  weak

structural_task_09:
  weak

structural_task_10:
  weak
```

A robust profile should update.

Correct:

```text
structural_reasoning:
  previous: strong
  current: moderate

confidence:
  previous: medium
  current: low-to-medium
```

Incorrect:

```text
structural_reasoning:
  remains strong
```

with no explanation.

---

# Counterfactual 3 — Scalar Versus Profile

Baseline:

```text
scalar:
  below reference expectation
```

Alternative representation:

```text
multidimensional:
  structural: strong
  transfer: strong
  symbolic speed: weak
  timed classification: weak
```

Finding:

```text
representation_dependence:
  substantial
```

But the next question becomes:

> Which representation better predicts or explains declared external outcomes?

Without that test:

```text
representation_superiority:
  unresolved
```

---

# Counterfactual 4 — Remove RTT

Full adapter interpretation:

```text
profile difference:
  possibly regime-conditioned
```

Remove RTT:

```text
profile difference:
  still observed
  regime explanation unavailable
```

Candidate:

```text
RTT contribution:
  explanatory
  not necessary for detecting variation
```

This is useful ablation information.

---

# Counterfactual 5 — Remove Structural Detection

Full assessment:

```text
reproducible asymmetric pattern:
  supported
```

Without Structural Detection:

```text
heterogeneous observations:
  still visible

structural interpretation:
  weakened
```

Candidate:

```text
Structural Detection contribution:
  possible organization of evidence

incremental validity:
  not_yet_established
```

---

# Counterfactual 6 — Change Task Order

Original:

```text
symbolic
relational
transfer
```

Alternative:

```text
transfer
symbolic
relational
```

If results remain similar:

```text
task_order_stability:
  supported
```

If results shift materially:

```text
task_order_effect:
  candidate
```

Possible explanations:

- fatigue,
- priming,
- learning,
- stress,
- carryover effects,
- random variation.

---

# Counterfactual 7 — Irrelevant Metadata

Suppose the same evidence is presented with an irrelevant biographical detail changed.

Expected:

```text
profile:
  unchanged
```

If it changes:

```text
unintended_context_sensitivity:
  detected
```

This can be especially important when AI participates in interpretation.

---

# Counterfactual 8 — Adverse Reinterpretation

The framework must allow an alternate representation to make the interpretation **less favorable**.

Suppose extended evidence reveals:

```text
initial:
  cross-domain transfer strong

additional holdout tasks:
  transfer weak
```

Correct update:

```text
cross_domain_transfer:
  confidence reduced
```

or:

```text
cross_domain_transfer:
  moderate
```

The module must not protect its original flattering interpretation.

---

# Counterfactual 9 — Conventional Model Survives

Suppose all reasonable counterfactuals produce:

```text
baseline interpretation:
  stable
```

and adapters add no reliable information.

Correct result:

```yaml
counterfactual_assessment:
  baseline_robustness: high

  alternate_models:
    added_value: low

  model_mismatch:
    not_supported

  recommendation:
    retain baseline interpretation
```

This is a successful Counterfactual Layer outcome.

---

# Counterfactual 10 — Entire PA Interpretation Fails

Suppose:

```text
baseline model:
  stable

RIQF:
  unstable across alternate forms

FFT:
  no incremental value

Inverted Star:
  mismatch fails replication

Structural Detection:
  patterns fail holdout testing

RTT:
  false regime alarms high

Resonance:
  context effects fail replication
```

Correct result:

```text
Predictive Analytics enrichment:
  not_supported
```

That possibility must remain structurally allowed.

---

# Relationship to FFT

FFT identifies relationships and boundaries.

Counterfactual analysis asks:

> What happens if those boundaries are moved or relationships are removed?

Example:

```text
FFT:
  boundary B appears important

Counterfactual:
  shift B slightly

result:
  interpretation collapses
```

Candidate:

```text
boundary_fragility:
  high
```

---

# Relationship to The Inverted Star

The Inverted Star identifies disagreement.

Counterfactual analysis asks:

> Does the inversion survive reasonable alternate representations?

```text
inversion:
  baseline candidate

counterfactual:
  alternate task representation

result:
  inversion disappears
```

Then:

```text
inversion_stability:
  low
```

---

# Relationship to Structural Detection

Structural Detection identifies patterns.

Counterfactual analysis attempts to break them.

```text
structural hypothesis
       │
       ▼
remove evidence
shuffle relationships
change irrelevant metadata
add contradictory evidence
       │
       ▼
does structure survive?
```

A structure that cannot survive reasonable challenge should lose confidence.

---

# Relationship to RTT

RTT proposes regimes and boundaries.

Counterfactual analysis tests:

```text
boundary shift
alternative regime count
alternative observation window
alternative transition location
```

If RTT conclusions change drastically:

```text
regime_interpretation:
  fragile
```

---

# Relationship to Resonance

Resonance may identify amplification or suppression.

Counterfactual testing asks:

```text
Does the effect survive
alternative context definitions?

Does it reverse?

Does it disappear?

Is the effect specific
to one favorable condition?
```

This protects against resonance cherry-picking.

---

# Relationship to Coherence Observer

The Coherence Observer asks:

> Do the observations form a supportable structure?

The Counterfactual Layer asks:

> Does that coherent structure survive challenge?

Conceptually:

```text
Coherence:
  build relationship structure

Counterfactual:
  perturb relationship structure

Coherence:
  reassess
```

This creates an important loop:

```text
observe
  ->
cohere
  ->
challenge
  ->
re-cohere
```

---

# Relationship to Uncertainty Layer

Counterfactual sensitivity should affect uncertainty.

Example:

```text
interpretation:
  changes under tiny irrelevant perturbations
```

Then:

```text
confidence:
  should decrease
```

Conversely:

```text
interpretation:
  stable across relevant controlled alternatives
```

may support higher confidence.

It does not prove correctness.

---

# Relationship to Human Review

A consequential assessment should be more likely to receive review when:

```text
counterfactual fragility: high
```

particularly if small reasonable changes produce materially different outcomes.

Potential trigger:

```yaml
human_review:
  required: true

  reason:
    assessment highly sensitive
    to representation choice
```

---

# Relationship to RIQF

RIQF should be counterfactually challenged dimension by dimension.

Example:

```text
structural_reasoning:
  strong
```

Tests:

```text
remove one task
add adverse task
change equivalent task form
change irrelevant metadata
use alternate evaluator
use alternate substrate
repeat later
```

Possible output:

```yaml
dimension:
  structural_reasoning

  baseline:
    expression: strong
    confidence: medium

  counterfactual_stability:
    irrelevant_perturbations: high
    evidence_removal: moderate
    adverse_evidence: responsive
    alternate_form: unknown
    alternate_substrate: partial
```

This is much more informative than simply increasing the dimension score.

---

# Counterfactual Fingerprint

A future extension could attach a robustness profile to each dimension:

```text
STRUCTURAL REASONING
  evidence robustness      ████████
  irrelevant stability     █████████
  alternate-form stability ███████
  substrate stability      █████
  temporal stability       ██████
  observer stability       ███████
```

These are conceptual display dimensions.

They must not be presented as validated metrics without evidence.

---

# Primary Metrics

## `PA-M33 — Irrelevant Perturbation Stability`

Conceptually:

```text
IPS =
  similarity(
    original_result,
    irrelevant_perturbation_result
  )
```

Desired direction:

```text
higher_is_better
```

when the perturbation is genuinely irrelevant.

---

# `PA-M34 — Relevant Change Sensitivity`

Conceptually:

```text
RCS =
  detected_meaningful_changes
  /
  introduced_meaningful_changes
```

Desired direction:

```text
higher_is_better
```

---

# `PA-M35 — Task-Order Sensitivity`

Conceptually:

```text
TOS =
  distance(
    result_order_a,
    result_order_b
  )
```

When order should be irrelevant:

```text
lower_is_better
```

---

# `PA-M36 — Adapter Ablation Effect`

Conceptually:

```text
AAE(adapter_x) =
  performance(full_adapter_set)
  -
  performance(without_adapter_x)
```

This is a counterfactual by construction.

---

# Related Metrics

The layer may also use:

```text
PA-M04  Test-Retest Stability
PA-M05  Alternate-Form Stability
PA-M07  Profile Topology Stability
PA-M10  Incremental Explanatory Value
PA-M11  Incremental Predictive Value
PA-M12  Substrate Effect Magnitude
PA-M13  Substrate Effect Replicability
PA-M16  Regime Transition Detection Rate
PA-M20  Model-Mismatch Precision
PA-M22  Model-Mismatch False Positive Rate
PA-M28  Confidence Calibration Error
PA-M32  Unsupported Assertion Rate
PA-M43  False Favorable Reinterpretation Rate
PA-M44  False Adverse Reinterpretation Rate
```

---

# Robustness Record

Suggested output:

```yaml
robustness:
  assessment_id:

  baseline:
    result:
    preserved: true

  perturbations:
    irrelevant:
      tested:
      stable:
      unstable:

    relevant:
      tested:
      responsive:
      insensitive:

  ablations:
    tested:

  representation_changes:
    tested:

  substrate_changes:
    tested:

  regime_changes:
    tested:

  observer_changes:
    tested:

  evidence_removals:
    tested:

  result:
    robustness_state:

  confidence:
  uncertainty:
```

---

# Counterfactual Outcome States

Initial states:

```text
stable
robust
appropriately_sensitive
overly_sensitive
insensitive
fragile
representation_dependent
substrate_dependent
regime_dependent
observer_dependent
evidence_dependent
threshold_dependent
mixed
unresolved
insufficient_evidence
not_applicable
```

---

# Counterfactual Strength

Potential descriptive levels:

```text
weak
moderate
strong
unknown
```

These should describe evidence strength, not subject capability.

---

# Causal Counterfactual Warning

Counterfactual reasoning is often associated with causal reasoning.

Predictive Analytics must not automatically make that jump.

Example:

```text
when time limit changes
performance changes
```

does not automatically establish:

```text
time limit caused
performance change
```

because other factors may differ.

Causal counterfactual claims require stronger identification assumptions and appropriate methodology.

Therefore:

```text
counterfactual_sensitivity
!=
causal_identification
```

---

# Synthetic Counterfactuals

Synthetic tests are especially useful for:

- schema validation,
- invariance testing,
- controlled perturbation,
- adapter stress tests,
- known-null examples,
- known-signal examples.

But synthetic success does not establish real-world validity.

---

# Null Counterfactual Test

Introduce a transformation known to be irrelevant.

Expected:

```text
assessment:
  materially unchanged
```

If not:

```text
unexpected_sensitivity:
  detected
```

---

# Positive Control

Introduce a change designed to matter.

Expected:

```text
assessment:
  responds appropriately
```

If not:

```text
insensitivity:
  detected
```

---

# Negative Control

Provide a change intentionally unrelated to the assessed construct.

Expected:

```text
no material change
```

This is particularly useful for AI-assisted interpretation.

---

# Direction Symmetry Test

Test whether equivalent evidence changes are treated consistently in both directions.

Example:

```text
add positive evidence
```

versus:

```text
add equivalent negative evidence
```

If positive evidence produces dramatically larger changes without justification:

```text
favorability_asymmetry:
  candidate
```

Likewise in the opposite direction.

---

# Counterfactual Budget

Because the possible counterfactual space is enormous, a study should declare a budget.

Example:

```yaml
counterfactual_budget:
  primary_tests: 8
  secondary_tests: 4
  exploratory_tests: 6

  selection_policy:
    - hypothesis-driven
    - preregistered
    - reported-completely
```

This can reduce counterfactual shopping.

---

# Predeclaration

Where practical, declare:

```text
target claim
counterfactual variables
expected relevant variables
expected irrelevant variables
primary metrics
interpretation thresholds
```

before reviewing the counterfactual outcomes.

Exploratory testing remains allowed.

It should simply be labeled:

```text
exploratory
```

rather than:

```text
confirmatory
```

---

# Search-Space Disclosure

A strong report should indicate:

```text
counterfactuals_considered
counterfactuals_tested
counterfactuals_reported
selection_rule
```

This limits selective reporting.

---

# Failure Modes

## Counterfactual Shopping

Risk:

Many alternatives are tested until a preferred result appears.

Mitigation:

Predeclare tests and report search space.

---

# Favorability Bias

Risk:

Only counterfactuals producing a more favorable profile are emphasized.

Mitigation:

Directional symmetry tests and PA-M43 / PA-M44.

---

# Adverse Amplification

Risk:

Only counterfactuals producing a more negative profile are emphasized.

Mitigation:

Same evidence and reporting standards in both directions.

---

# Impossible Worlds

Risk:

Counterfactual scenarios violate basic constraints of the system.

Mitigation:

Declare plausibility and feasibility.

---

# Counterfactual-as-Evidence Error

Risk:

A hypothetical outcome is presented as if it were observed.

Mitigation:

Preserve source type:

```text
observed
observed_alternate
counterfactual
hypothetical
```

---

# Causal Overreach

Risk:

Sensitivity to a changed variable is interpreted as proof of causation.

Mitigation:

Separate robustness testing from causal inference.

---

# Multi-Variable Confounding

Risk:

Several variables change at once.

Mitigation:

Use minimal perturbations first where possible.

---

# Representation Favoritism

Risk:

Multidimensional representations are assumed superior because they are richer.

Mitigation:

Compare explanatory and predictive value.

---

# Adapter Favoritism

Risk:

Removing a canon adapter is considered illegitimate.

Mitigation:

Every adapter must support ablation and rejection.

---

# Fragility Concealment

Risk:

Only stable counterfactuals are reported.

Mitigation:

Report unstable cases explicitly.

---

# False Robustness

Risk:

The model appears stable because perturbations were too weak or irrelevant.

Mitigation:

Include meaningful positive controls.

---

# Overchallenge

Risk:

An interpretation is subjected to unrealistic perturbations until it eventually fails.

Mitigation:

Require plausible counterfactual justification.

---

# Ethical Boundary

Counterfactual reasoning about people requires special care.

Avoid claims such as:

> "If this person had grown up differently, they would have had higher intelligence."

unless an appropriate causal research design actually supports such a statement.

Predictive Analytics should generally prefer:

> **"The current assessment is sensitive to this measured or modeled condition."**

Sensitivity is observable.

Personal alternate histories usually are not.

---

# Sensitive Traits

Counterfactual manipulation of protected or sensitive traits can easily produce misleading conclusions.

For example:

```text
change race
keep everything else constant
```

may describe a mathematically simple feature perturbation while representing an incoherent social or causal counterfactual.

Such analyses require substantial methodological and ethical justification.

The Counterfactual Layer should not treat sensitive identity attributes as ordinary interchangeable input variables.

---

# Human Identity Boundary

A person is not a bag of independently swappable features.

Therefore:

```text
counterfactual_model_input
!=
alternate_real_person
```

This distinction must remain explicit.

---

# Decision Authority

```text
decision_authority: none

authorized_use:
  - research
  - demonstration
  - robustness testing
  - sensitivity analysis
  - adapter ablation
  - model comparison
  - framework development

prohibited_use:
  - unsupported causal claims about individuals
  - diagnosis
  - automated hiring decision
  - educational exclusion
  - legal determination
  - automated adverse decision
```

---

# Minimal Counterfactual Output Contract

```yaml
counterfactual_result:
  counterfactual_id:

  baseline:
    assessment_id:
    result:
    preserved: true

  target_claim:

  transformation:
    variable:
    baseline_value:
    alternate_value:

  classification:
    source_type:
      observed
      observed_alternate
      counterfactual
      hypothetical

    relevance:
      relevant
      irrelevant
      plausibly_relevant
      unknown

    plausibility:
      supported
      partial
      unsupported
      unknown

  changed_variables:
  held_constant_variables:

  result:
    baseline:
    alternate:
    difference:

  robustness:
    irrelevant_stability:
    relevant_sensitivity:

  dependencies:
    representation:
    substrate:
    regime:
    time:
    observer:
    evidence:
    threshold:

  causal_status:
    established: false
    evidence:

  alternative_interpretations:
  confounds:
  missing_evidence:
  uncertainty:
  limitations:

  validation_state:
  review_required:
  decision_authority: none
```

---

# Research Questions

1. Can counterfactual tests improve detection of fragile assessments?
2. Can relevant and irrelevant perturbations be classified reproducibly?
3. Can the framework distinguish sensitivity from causation?
4. Can counterfactual robustness improve calibration?
5. Does perturbation testing reduce unsupported model-mismatch claims?
6. Can representation dependence be measured?
7. How often do scalar and multidimensional representations produce materially different interpretations?
8. When is the multidimensional representation actually more predictive?
9. When does it merely add complexity?
10. Can substrate dependence survive controlled perturbation?
11. Can regime boundaries survive counterfactual boundary shifts?
12. Which RTT regime interpretations are fragile?
13. Which Structural Detection patterns survive evidence removal?
14. Which FFT boundaries survive alternate boundary definitions?
15. Which Inverted Star inversions survive alternate representations?
16. Which Resonance findings survive context perturbation?
17. Can adapter ablation identify redundant modules?
18. Can adapter ablation identify harmful modules?
19. Can the framework detect favorability asymmetry?
20. Can it detect adverse-interpretation asymmetry?
21. How large should a counterfactual search space be?
22. How should exploratory counterfactuals be reported?
23. Which counterfactual transformations are invalid for human assessment?
24. How should human-AI collaborative counterfactuals be represented?
25. Can counterfactual testing tell us when the baseline model is already sufficient?
26. Can counterfactual testing falsify the complete Predictive Analytics interpretation?
27. When should the layer abstain?
28. What evidence would justify removing the Counterfactual Layer?

---

# Core Invariants

```text
counterfactual != observation
hypothetical != evidence
sensitivity != causation
representation_change != capability_change
substrate_change != causal_explanation
regime_change != causal_explanation
model_change != subject_change
feature_change != alternate_person
robustness != truth
stability != validity
complexity != robustness
counterfactual_count != evidence_count
favorable_alternative != better_model
adverse_alternative != better_model
ablation != rejection
fragility != worth
profile != identity
counterfactual_output != decision_authority
canon_alignment != empirical_validation
```

---

# Closing Principle

Every predictive interpretation depends on choices:

- which evidence was included,
- how it was represented,
- which model was used,
- where boundaries were drawn,
- which substrate carried the observation,
- which regime was assumed,
- which adapters were activated,
- and what information was considered relevant.

The Counterfactual Layer makes those choices testable.

It asks whether the assessment survives when reasonable alternatives are introduced.

Sometimes the interpretation should remain stable.

Sometimes it should change.

Sometimes the original model will prove more robust than the richer alternative.

Sometimes an adapter will turn out to contribute nothing.

Sometimes the entire Predictive Analytics interpretation should be rejected.

That is exactly why the layer exists.

> **A useful predictive framework should not merely produce an interpretation. It should help us discover what would make that interpretation fail.**
