<img width="1194" height="672" alt="predictive_analytics_example_resonant_iq_fingerprint_" src="https://github.com/user-attachments/assets/0eaa4968-1721-4d0e-9507-64dad1c5a4d2" />

# Example — Resonant IQ Fingerprint

> **The purpose of the fingerprint is not to find a better number. It is to preserve the shape that a number compresses away.**

## Module

Predictive Analytics

## Example ID

`PAX-01`

## Example Type

Resonant IQ Fingerprint

## Status

Synthetic demonstration.

## Validation State

Unvalidated.

## Decision Authority

None.

---

# Important Notice

`PAX-01` is a fictional subject created solely to demonstrate the Predictive Analytics and Resonant IQ Fingerprint representation grammar.

This example is **not**:

- a psychological diagnosis,
- a validated intelligence assessment,
- an educational placement instrument,
- an employment assessment,
- a medical assessment,
- a clinical assessment,
- a legal assessment,
- or an assessment of any real person.

All values, observations, task results, confidence labels, and profile shapes in this document are illustrative.

They are synthetic.

They must not be interpreted as empirical results.

---

# Example Objective

This example demonstrates a simple problem.

Suppose an existing assessment produces a relatively low composite result.

Additional observations later reveal that the subject performs quite differently across other tasks and contexts.

What should happen?

A naive response might be:

```text
Original score:
  low

New framework:
  high

Therefore:
  original assessment was wrong
```

Predictive Analytics rejects that shortcut.

Instead:

```text
Original observation
      │
      ▼
Preserve it
      │
      ▼
Collect additional evidence
      │
      ▼
Identify dimensions
      │
      ▼
Compare substrates
      │
      ▼
Apply relevant adapters
      │
      ▼
Check coherence
      │
      ▼
Challenge counterfactually
      │
      ▼
Preserve uncertainty
      │
      ▼
Produce profile
```

The goal is not rescue.

The goal is better observation.

---

# Scenario

Synthetic subject `PAX-01` participates in a conventional assessment emphasizing:

- timed symbolic reasoning,
- fixed-choice classification,
- short-context problem solving,
- rapid selection among predefined alternatives.

The simplified conventional result is:

```text
Composite:
  94
```

For purposes of this fictional example, assume the originating system describes that result as:

```text
below reference expectation
```

No claim is made here that a real instrument would use this exact score, interpretation, or task structure.

They are demonstration values.

---

# Baseline Observation

```yaml
baseline_assessment:
  subject: PAX-01
  synthetic: true

  representation:
    type: scalar_composite

  composite:
    value: 94
    status: synthetic_demo_value

  directly_observed:
    rapid_symbolic_processing: weak
    timed_classification: weak
    short_context_recall: moderate

  global_interpretation:
    broad_reasoning_capability: low

  confidence:
    direct_task_observations: medium
    global_interpretation: unknown
```

The crucial distinction is immediately visible.

The assessment directly observed:

```text
rapid symbolic processing
timed classification
short-context performance
```

But the broad interpretation claims:

```text
reasoning capability generally
```

Predictive Analytics asks whether the evidence warrants that larger inference.

It does not assume the answer is no.

---

# Baseline Preservation

The original result remains part of the record.

```yaml
baseline:
  preserved: true

  composite: 94

  direct_observations:
    rapid_symbolic_processing: weak
    timed_classification: weak
    short_context_recall: moderate

  rejected: false
  overridden: false
```

Nothing later in the example is allowed to erase these observations merely because another representation becomes more flattering.

---

# Additional Observation Program

PAX-01 then completes a broader synthetic task set.

The new tasks intentionally sample different forms of observable performance.

They include:

```text
T01  Pattern Completion
T02  Structural Mapping
T03  Causal System Reconstruction
T04  Temporal Sequence Reasoning
T05  Spatial Transformation
T06  Symbolic Manipulation
T07  Linguistic Reasoning
T08  Cross-Domain Transfer
T09  Regime Change Recognition
T10  Anomaly Detection
T11  Contradiction Handling
T12  Ambiguity Navigation
T13  Adaptive Reframing
T14  Coherence Maintenance
T15  Drift Recognition
T16  Abstraction / Compression
T17  Partial-Evidence Reconstruction
T18  Novelty Response
T19  Confidence Calibration
T20  Tool Collaboration
T21  Social Interpretation
T22  Environmental Adaptation
T23  Long-Horizon Integration
T24  Recovery / Recalibration
```

These task names are illustrative.

They are not validated psychometric instruments.

---

# Evidence Boundary

Several forms of evidence are deliberately separated.

```yaml
evidence_sources:
  E1:
    source: conventional_assessment
    independent: true

  E2:
    source: structural_task_family
    independent: true

  E3:
    source: transfer_task_family
    independent: true

  E4:
    source: temporal_task_family
    independent: true

  E5:
    source: ambiguity_task_family
    independent: true

  E6:
    source: longitudinal_task_family
    independent: true

  E7:
    source: tool_collaboration_task
    independent: true
```

If multiple adapters interpret `E2`, that remains:

```text
one independent evidence source
```

not:

```text
one evidence source per adapter
```

---

# Synthetic Observations

Illustrative observations:

```text
Pattern Recognition             strong
Structural Reasoning            strong
Causal Integration              strong
Temporal Reasoning              moderate-strong
Spatial Reasoning               moderate
Symbolic Reasoning              moderate
Linguistic Reasoning            moderate-strong
Cross-Domain Transfer           strong
Regime Recognition              strong
Anomaly Detection               strong
Contradiction Handling          strong
Ambiguity Navigation            strong
Adaptive Reframing              strong
Coherence Maintenance           moderate-strong
Drift Awareness                 strong
Compression / Abstraction       strong
Partial-Evidence Reconstruction strong
Novelty Response                strong
Metacognitive Calibration       moderate
Tool Collaboration              strong
Social Interpretation           moderate
Embodied / Environmental Fit    unknown
Long-Horizon Integration        strong
Recovery / Recalibration        moderate-strong

Rapid Symbolic Processing       weak-moderate
Timed Classification            weak
Short-Context Recall            moderate
```

Again:

```text
strong
moderate
weak
```

are illustrative ordinal labels.

They are not IQ scores.

---

# Initial RIQF Profile

A first profile might appear:

```text
                      PAX-01

Pattern Recognition             ████████░░
Structural Reasoning            █████████░
Causal Integration              ████████░░
Temporal Reasoning              ███████░░░
Spatial Reasoning               ██████░░░░
Symbolic Reasoning              ██████░░░░
Linguistic Reasoning            ███████░░░
Cross-Domain Transfer           █████████░
Regime Recognition              ████████░░
Anomaly Detection               █████████░
Contradiction Handling          ████████░░
Ambiguity Navigation            █████████░
Adaptive Reframing              ████████░░
Coherence Maintenance           ███████░░░
Drift Awareness                 ████████░░
Compression / Abstraction       ████████░░
Partial-Evidence Reconstruction █████████░
Novelty Response                ████████░░
Metacognitive Calibration       ██████░░░░
Tool Collaboration              ████████░░
Social Interpretation           ██████░░░░
Environmental Fit               ??????????
Long-Horizon Integration        █████████░
Recovery / Recalibration        ███████░░░

Rapid Symbolic Processing       ████░░░░░░
Timed Classification            ███░░░░░░░
Short-Context Recall            █████░░░░░
```

The bars are visual demonstration aids only.

They do not represent validated intervals or population percentiles.

---

# First Important Result

The profile is:

```text
asymmetric
```

This alone establishes very little.

It does **not** establish:

```text
hidden genius
```

or:

```text
conventional assessment invalid
```

It establishes:

> **The synthetic observation set is heterogeneous enough that a single scalar does not preserve all observed variation.**

That is the first meaningful finding.

---

# RIQF Layer 1 — Capability

The capability layer records what was directly observed.

```yaml
capability_profile:
  structural_reasoning:
    expression: strong
    confidence: medium

  cross_domain_transfer:
    expression: strong
    confidence: medium

  ambiguity_navigation:
    expression: strong
    confidence: medium

  regime_recognition:
    expression: strong
    confidence: medium

  long_horizon_integration:
    expression: strong
    confidence: medium

  rapid_symbolic_processing:
    expression: weak
    confidence: medium

  timed_classification:
    expression: weak
    confidence: medium

  environmental_fit:
    expression: unknown
    confidence: none
```

Unknown remains unknown.

---

# RIQF Layer 2 — Expression Substrate

PAX-01 is then observed under several synthetic substrates.

```text
Reflective textual              strong
Relational mapping              strong
System-level visual             strong
Open generative                 strong
Cross-domain conversational     strong
Tool-assisted                   strong
Human-AI collaborative          strong

Fixed-choice                    moderate
Isolated symbolic               moderate
Short-context                   moderate

Severely timed symbolic         weak
Severely timed classification   weak
```

This produces a candidate:

```text
substrate sensitivity:
  observed
```

But not yet:

```text
substrate causation:
  established
```

---

# Substrate Expression Profile

```yaml
substrate_expression:
  reflective_textual:
    expression: strong

  relational:
    expression: strong

  system_level_visual:
    expression: strong

  generative:
    expression: strong

  tool_assisted:
    expression: strong

  human_ai_collaborative:
    expression: strong

  fixed_choice:
    expression: moderate

  symbolic:
    expression: moderate

  severe_time_constraint:
    expression: weak

  causal_status:
    unresolved
```

---

# Important Boundary

Tool-assisted performance belongs to a different observational boundary.

```text
PAX-01 alone
```

is not identical to:

```text
PAX-01 + AI
```

Therefore:

```yaml
system_boundaries:
  individual_human:
    id: PAX-01

  human_ai_pair:
    id: PAX-01-AI

attribution:
  collaborative_result:
    belongs_to: PAX-01-AI

  individual_credit:
    status: partial
```

The collaborative result may be meaningful.

It is not automatically an individual-human score.

---

# RIQF Layer 3 — Resonance / Context

The example next asks whether performance changes systematically across contexts.

Illustrative patterns:

```text
context-rich:
  amplification candidate

system-level:
  amplification candidate

reflective:
  amplification candidate

tool-collaborative:
  amplification candidate

severely time-constrained:
  suppression candidate

fixed binary-choice:
  suppression candidate
```

These remain candidate observations until replication.

---

# Existing Model Interpretation

The conventional model says, in simplified demonstration form:

```text
composite:
  94

broad interpretation:
  low reasoning capability
```

The richer observation set says:

```text
profile:
  highly uneven

strong:
  structural
  transfer
  ambiguity
  anomaly
  regime
  long-horizon

weak:
  rapid symbolic
  timed classification
```

This creates a disagreement.

---

# Model Mismatch Question

The question is **not**:

> Which result do we like better?

The question is:

> **Does the conventional representation have sufficient scope to justify the global interpretation being made?**

Candidate model-fit record:

```yaml
model_fit:
  direct_task_fit:
    status: supported

  global_profile_fit:
    status: low

  reason:
    baseline directly reflects several observed
    weaknesses but does not explain the larger
    heterogeneous observation profile

  confidence:
    low_to_medium
```

The conventional task observations remain supported.

The global inference becomes less certain.

---

# FFT Adapter Pass

The Framework Field Theory adapter asks:

> What relationships and boundaries surround the prediction?

It finds:

```text
local observation:
  timed symbolic performance weak

broader observations:
  structural and relational tasks strong
```

Candidate field relationships:

```text
task representation
     ↕
observed performance

time constraint
     ↕
observed performance

interaction mode
     ↕
observed performance
```

Correct result:

```yaml
fft:
  relationships:
    status: candidate

  boundary_difference:
    status: supported_in_example

  causal_interpretation:
    status: unresolved

  added_information:
    broader observation boundary matters
```

FFT does not declare PAX-01 globally more intelligent.

---

# Inverted Star Adapter Pass

The Inverted Star asks whether prediction and independent observations materially disagree.

```text
baseline:
  broad_reasoning: low

extended:
  structural_reasoning: strong
  transfer: strong
  ambiguity_navigation: strong
  long_horizon_integration: strong
```

Candidate:

```yaml
inverted_star:
  inversion:
    detected: true

  class:
    - prediction-performance
    - local-global
    - representation

  direction:
    prediction_lower_than_broader_observation

  confidence:
    medium

  cause:
    unresolved
```

Importantly:

```text
inversion
!=
proof of hidden superior intelligence
```

---

# Structural Detection Adapter Pass

Structural Detection looks for reproducible structure in the variation.

Candidate pattern:

```text
rapid / constrained / fixed:
  weaker

relational / structural / generative:
  stronger
```

Synthetic repeated observations support:

```text
heterogeneous but structured profile
```

Candidate:

```yaml
structural_detection:
  pattern:
    status: replicated_in_demo

  structural_reasoning:
    status: supported_in_demo

  boundary:
    candidate: task_representation

  invariant:
    candidate: relational_structure_preservation

  generalizability:
    unknown
```

Again:

```text
demo replication
!=
empirical validation
```

---

# RTT Adapter Pass

RTT asks whether the observations organize into meaningful operating regimes.

Candidate Regime A:

```text
timed
symbolic
fixed-choice
individual
```

Candidate Regime B:

```text
reflective
relational
generative
individual or collaborative
```

Synthetic performance:

```text
Regime A:
  repeatedly weaker

Regime B:
  repeatedly stronger
```

Candidate:

```yaml
rtt:
  regime_difference:
    status: candidate

  within_regime_stability:
    status: demonstration_only

  model_fit:
    regime_a: plausible
    regime_b: weaker

  causal_interpretation:
    unresolved
```

RTT does not establish which changed variable caused the difference.

---

# Resonance Adapter Pass

Resonance asks whether expression repeatedly amplifies or suppresses under particular contexts.

Candidate:

```yaml
resonance:
  amplification:
    - reflective
    - relational
    - context-rich

  suppression:
    - severe_time_constraint
    - forced_fixed_choice

  replication:
    status: demonstration_only

  cause:
    unresolved
```

The vocabulary is useful only if future work can operationalize it.

---

# Coherence Observer Pass

The Coherence Observer compares the observations.

Supporting cluster:

```text
structural reasoning
cross-domain transfer
anomaly detection
regime recognition
long-horizon integration
ambiguity navigation
```

Contrasting cluster:

```text
rapid symbolic processing
timed classification
```

Candidate:

```yaml
coherence:
  profile_coherence:
    status: moderate_to_high

  scalar_coherence:
    status: low

  cross_substrate_coherence:
    status: conditional

  cross_regime_coherence:
    status: unresolved

  adapter_coherence:
    status: moderate

  evidence_independence:
    status: medium
```

This does not mean the richer model is true.

It means it organizes the synthetic evidence with fewer unresolved contradictions.

---

# Scalar Coherence

The scalar compresses:

```text
strong structural performance
strong transfer
strong ambiguity navigation
weak timed symbolic performance
weak fixed-choice performance
```

into:

```text
94
```

That may be useful for some purposes.

But for this synthetic observation set:

```text
information_loss:
  substantial
```

Therefore:

```yaml
composite:
  permitted: true

  value: 94

  interpretive_status:
    lossy_projection

  sufficient_alone:
    false

  profile_required:
    true
```

---

# Counterfactual Challenge 1 — Remove Favorable Evidence

Remove one strong structural task.

Original:

```text
structural_reasoning:
  strong
```

After removal:

```text
structural_reasoning:
  still strong
  confidence reduced
```

Candidate:

```text
single_favorable_evidence_dependency:
  low
```

---

# Counterfactual Challenge 2 — Add Adverse Evidence

Add several weak structural tasks.

New synthetic results:

```text
structural_task_08:
  weak

structural_task_09:
  weak

structural_task_10:
  moderate
```

Updated profile:

```text
structural_reasoning:
  moderate
```

Confidence changes.

This is required behavior.

The profile is not protected from adverse evidence.

---

# Counterfactual Challenge 3 — Remove RTT

Without RTT:

```text
performance variation:
  still present

regime explanation:
  unavailable
```

Candidate:

```text
RTT:
  explanatory contribution possible

variation detection:
  not dependent on RTT
```

This prevents RTT from taking credit for evidence that existed before it was applied.

---

# Counterfactual Challenge 4 — Remove Structural Detection

Without Structural Detection:

```text
heterogeneous observations:
  still present

structured pattern interpretation:
  reduced
```

Candidate:

```text
Structural Detection:
  organizational contribution possible

incremental validity:
  unresolved
```

---

# Counterfactual Challenge 5 — Remove Resonance

Without Resonance:

```text
context variation:
  still visible

amplification / suppression vocabulary:
  absent
```

This asks whether resonance adds measurable information or merely terminology.

---

# Counterfactual Challenge 6 — Restore Scalar Only

Use only:

```text
composite:
  94
```

Question:

> Does the scalar explain the held-out structural and transfer tasks?

Synthetic answer for this example:

```text
poorly
```

That makes scalar-only representation less explanatory **within the demonstration**.

It does not establish the same result empirically.

---

# Counterfactual Challenge 7 — Baseline Model Wins

Now deliberately modify the synthetic evidence.

Suppose additional observations instead show:

```text
structural reasoning:
  weak

cross-domain transfer:
  weak

ambiguity navigation:
  weak

long-horizon integration:
  weak
```

Then:

```text
baseline prediction:
  increasingly coherent

model mismatch:
  not supported

RIQF:
  no rescue
```

This counterexample is essential.

If the module could not produce this outcome, it would be biased by design.

---

# Drift Observer Pass

The example now introduces fictional repeated observations.

At `T1`:

```text
structural reasoning:
  strong

cross-domain transfer:
  strong

rapid symbolic:
  weak
```

At `T2`:

```text
structural reasoning:
  strong

cross-domain transfer:
  moderate

rapid symbolic:
  moderate
```

At `T3`:

```text
structural reasoning:
  strong

cross-domain transfer:
  moderate

rapid symbolic:
  moderate
```

Candidate:

```yaml
drift:
  structural_reasoning:
    status: stable

  cross_domain_transfer:
    status: repeated_change
    direction: decreasing

  rapid_symbolic_processing:
    status: repeated_change
    direction: increasing

  global_drift:
    status: inappropriate_summary

  cause:
    unresolved
```

The fingerprint changes shape.

That is allowed.

---

# Profile Topology

Instead of asking:

```text
Did IQ go up or down?
```

the richer question becomes:

> **How did the observed capability topology change?**

Conceptually:

```text
T1
  structural      █████████
  transfer        █████████
  symbolic        ████

T3
  structural      █████████
  transfer        ██████
  symbolic        ██████
```

The change is multidirectional.

A single drift number would conceal that.

---

# Uncertainty Layer

The framework now asks what it **does not know**.

```yaml
uncertainty:
  biological_cause:
    status: unknown

  developmental_cause:
    status: unknown

  clinical_significance:
    status: unknown

  population_percentile:
    status: unknown

  cross_cultural_generalization:
    status: unknown

  long_term_stability:
    status: unvalidated

  transfer_to_unobserved_domains:
    status: unknown

  causal_substrate_effect:
    status: unresolved

  causal_regime_effect:
    status: unresolved
```

This may be one of the most important sections of the entire fingerprint.

---

# Known

Within the synthetic example:

```text
performance varies across tasks
performance varies across substrates
profile is asymmetric
several patterns repeat by construction
conventional task weaknesses remain present
broader observations include strengths not represented by baseline scalar
```

---

# Unknown

```text
why the variation exists
whether the dimensions correspond to stable real constructs
whether effects replicate in real populations
whether RTT adds predictive value
whether resonance adds predictive value
whether FFT adds predictive value
whether Structural Detection adds predictive value
whether the profile predicts real external outcomes
whether the profile is culturally portable
whether the profile is fair across groups
```

---

# Not Authorized

```text
diagnosis
clinical interpretation
disability classification
employment decision
educational exclusion
legal determination
insurance decision
lending decision
automated adverse action
```

---

# Human Review Hook

Suppose this were someday a validated, appropriately governed consequential context.

A discrepancy such as:

```text
broad adverse scalar inference
+
strong contradictory multidimensional evidence
```

might trigger:

```yaml
review:
  required: true

  reasons:
    - model_scope_question
    - profile_asymmetry
    - prediction_observation_disagreement
    - substrate_dependence_candidate
```

The review action would **not** be:

```text
replace 94 with higher score
```

It would be:

```text
inspect evidence
inspect intended use
inspect model scope
inspect alternative observations
preserve uncertainty
determine whether additional assessment is justified
```

---

# Resonant IQ Fingerprint Summary

```text
PAX-01 — SYNTHETIC

CAPABILITY SHAPE
────────────────────────────────────────

Structural Reasoning            █████████░
Cross-Domain Transfer           █████████░
Pattern Recognition             ████████░░
Anomaly Detection               █████████░
Regime Recognition              ████████░░
Ambiguity Navigation            █████████░
Adaptive Reframing              ████████░░
Long-Horizon Integration        █████████░
Causal Integration              ████████░░
Coherence Maintenance           ███████░░░
Temporal Reasoning              ███████░░░
Linguistic Reasoning            ███████░░░
Spatial Reasoning               ██████░░░░
Metacognitive Calibration       ██████░░░░
Social Interpretation           ██████░░░░

Rapid Symbolic Processing       ████░░░░░░
Timed Classification            ███░░░░░░░
Short-Context Recall            █████░░░░░

Environmental Fit               UNKNOWN
```

---

# Substrate Profile

```text
Reflective textual              ████████
Relational                      █████████
System-level                    █████████
Generative                      ████████
Context-rich                    █████████
Tool-assisted                   ████████
Human-AI pair                   █████████

Fixed-choice                    █████
Isolated symbolic               █████

Severely timed                  ███
```

Again:

```text
these bars are illustrative
```

They are not validated scores.

---

# Model-Fit Profile

```yaml
model_fit:
  conventional_direct_tasks:
    status: supported

  conventional_global_inference:
    status: low_confidence

  multidimensional_profile:
    status: better_fit_in_demo

  substrate_aware_profile:
    status: candidate

  regime_aware_profile:
    status: candidate

  final:
    status: unresolved_without_empirical_validation
```

This preserves a subtle but crucial distinction:

> The original measurement can be accurate about what it measured while still being too narrow for a global claim.

---

# Adapter Summary

```yaml
adapters:
  fft:
    finding:
      broader field relationships matter
    validation:
      unvalidated

  inverted_star:
    finding:
      prediction-observation inversion candidate
    validation:
      unvalidated

  structural_detection:
    finding:
      asymmetric structural pattern candidate
    validation:
      unvalidated

  rtt:
    finding:
      regime-conditioned expression candidate
    validation:
      unvalidated

  resonance:
    finding:
      contextual amplification/suppression candidate
    validation:
      unvalidated
```

---

# Adapter Agreement Warning

All five adapters agreeing does not imply five independent confirmations.

Example:

```yaml
adapter_agreement:
  count: 5

independent_evidence_sources:
  count: 7

interpretation:
  adapter coherence and evidence independence
  are reported separately
```

That distinction must remain explicit.

---

# Validation Record

The values below describe **validation status**, not synthetic performance numbers.

```yaml
validation_record:
  subject: PAX-01

  data_type:
    synthetic

  empirical_subject:
    false

  framework_validation:
    state: unvalidated

  evidence:
    dimension_coverage:
      status: demonstration_only

    profile_coverage:
      status: demonstration_only

    evidence_independence:
      status: structurally_demonstrated

  reliability:
    test_retest:
      status: not_tested

    alternate_form:
      status: not_tested

    inter_rater:
      status: not_tested

    topology_stability:
      status: not_tested

  validity:
    convergent:
      status: not_tested

    discriminant:
      status: not_tested

    incremental_explanatory:
      status: not_tested

    incremental_predictive:
      status: not_tested

  substrate:
    effect_magnitude:
      status: demonstration_only

    replicability:
      status: not_tested

    symmetry:
      status: structurally_demonstrated

    specificity:
      status: not_tested

  regime:
    transition_detection:
      status: not_tested

    false_alarm_rate:
      status: not_tested

    regime_conditioned_stability:
      status: demonstration_only

  model_mismatch:
    precision:
      status: not_tested

    recall:
      status: not_tested

    false_positive_rate:
      status: not_tested

  uncertainty:
    calibration:
      status: not_tested

    unsupported_assertion_rate:
      status: not_tested

  adapters:
    ablation:
      status: demonstration_only

  fairness:
    subgroup_analysis:
      status: not_applicable_to_single_synthetic_case

  explainability:
    evidence_reconstruction:
      status: demonstration_only

    explanation_completeness:
      status: demonstration_only

  decision:
    authority: none
```

---

# Selected Metric Mapping

The first real RIQF pilot should consider at least:

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
PA-M11  Incremental Predictive Value

PA-M12  Substrate Effect Magnitude
PA-M13  Substrate Effect Replicability
PA-M14  Substrate Symmetry
PA-M15  Substrate Specificity

PA-M16  Regime Transition Detection Rate
PA-M17  False Regime Alarm Rate
PA-M19  Regime-Conditioned Stability

PA-M20  Model-Mismatch Precision
PA-M21  Model-Mismatch Recall
PA-M22  Model-Mismatch False Positive Rate

PA-M24  Cross-Observation Coherence
PA-M25  Profile Contradiction Density

PA-M26  Dimension Drift Rate
PA-M27  Profile Drift Magnitude

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

---

# Comparative Evaluation Matrix

A real validation program should avoid comparing only:

```text
traditional IQ
vs
RIQF
```

That comparison is too crude.

A better progression:

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
  + RTT / regime observation

M6:
  M5
  + resonance observation

M7:
  full Predictive Analytics ensemble
```

Then ask:

```text
Which layer actually adds value?
```

---

# What Would Count as Success?

RIQF should not be considered successful merely because users like the resulting profiles better.

Success could eventually include evidence that it:

- improves explanatory value,
- predicts relevant external outcomes,
- improves calibration,
- detects model mismatch reliably,
- preserves meaningful asymmetry,
- exposes uncertainty,
- survives alternate forms,
- survives irrelevant perturbations,
- responds to relevant evidence changes,
- reduces unsupported global inference,
- and behaves acceptably across relevant groups.

---

# What Would Count as Failure?

RIQF should be revised or rejected if it:

- produces unstable profiles,
- cannot distinguish dimensions,
- merely redescribes conventional subscales,
- systematically generates flattering narratives,
- labels most unfavorable assessments as mismatches,
- produces poor inter-rater agreement,
- adds complexity without predictive or explanatory value,
- fails counterfactual tests,
- creates new fairness problems,
- cannot abstain,
- or secretly recreates a master intelligence score.

---

# Falsification Example

Suppose a future study finds:

```text
RIQF dimensions:
  low test-retest reliability

adapter outputs:
  poor inter-rater agreement

substrate effects:
  fail replication

RTT contribution:
  no ablation effect

resonance contribution:
  no ablation effect

Structural Detection:
  equivalent to simpler methods

predictive value:
  no improvement

explanatory value:
  no improvement
```

Correct conclusion:

```text
RIQF:
  not_supported_in_current_form
```

Not:

```text
researchers did not understand the framework
```

unless evidence independently supports that explanation.

---

# No Hidden Master Number

The example deliberately refuses:

```text
Resonant IQ:
  143
```

or:

```text
RIQF Score:
  91%
```

because that would immediately recreate the reduction the profile was designed to investigate.

Preferred:

```yaml
profile:
  dimensions:
    multidimensional

  topology:
    asymmetric

  evidence:
    variable

  uncertainty:
    explicit

  composite:
    permitted: true
    interpretive_status: lossy_projection
    sufficient_alone: false
```

---

# Why Keep the Conventional Scalar?

Because compression is sometimes useful.

A scalar can be:

- easy to communicate,
- easy to compare,
- computationally convenient,
- operationally useful for a validated purpose.

The error is not necessarily producing a scalar.

The error is silently transforming:

```text
useful compressed observation
```

into:

```text
complete description of intelligence
```

The RIQF example preserves both.

---

# Flat Number Versus Fingerprint

## Flat representation

```text
PAX-01

Composite: 94
```

Advantages:

```text
compact
simple
comparable
```

Limitations:

```text
high information compression
profile shape lost
substrate effects lost
regime effects lost
uncertainty often hidden
```

---

# Fingerprint Representation

```text
PAX-01

Structural             █████████
Transfer               █████████
Pattern                ████████
Regime                 ████████
Ambiguity              █████████
Anomaly                █████████
Temporal               ███████
Symbolic               ██████
Rapid Symbolic         ████
Timed Classification   ███
```

Advantages:

```text
shape preserved
heterogeneity visible
context can be attached
uncertainty can be attached
```

Limitations:

```text
higher complexity
higher evidence burden
harder comparison
higher privacy risk
greater validation burden
greater narrative-overfit risk
```

Neither representation is inherently superior for every purpose.

---

# Beyond Humans

The same grammar might eventually describe other systems.

Example AI profile:

```text
retrieval fidelity
structural reasoning
uncertainty calibration
cross-domain transfer
contradiction detection
tool collaboration
long-horizon coherence
error recovery
regime recognition
```

But this does **not** imply that AI intelligence and human intelligence are internally equivalent.

It means the same high-level observation grammar may sometimes be useful across different system classes.

That claim itself requires validation.

---

# Human-AI Pair Example

A collaborative profile may look different from both components.

```text
Human:
  structural synthesis        strong
  retrieval                   moderate
  long-context recall         moderate

AI:
  structural synthesis        moderate
  retrieval                   strong
  long-context recall         strong

Human-AI Pair:
  structural synthesis        strong
  retrieval                   strong
  long-context integration    strong
```

The pair may be the meaningful system.

Do not automatically redistribute the pair result back onto the components.

---

# Long-Term Opportunity

The larger possibility is not merely:

```text
better IQ testing
```

It is a scalable grammar for representing intelligent performance as:

```text
multidimensional
substrate-sensitive
regime-sensitive
temporal
uncertain
contextual
revisable
```

That could potentially support comparisons within:

- humans,
- AI systems,
- teams,
- human-AI collaborations,
- organizations,
- robotic systems,
- other adaptive systems.

Cross-system comparisons require separate validation.

---

# Ethical Boundary

The fingerprint must never become:

```text
a new caste system
a covert ranking
a hiring shortcut
a school exclusion mechanism
a diagnostic substitute
a behavioral surveillance identifier
```

A richer profile can produce richer harm if treated as authority before validation.

---

# Privacy Boundary

A multidimensional cognitive profile may be more sensitive than a single conventional score.

It could reveal:

- observed strengths,
- observed weaknesses,
- preferred substrates,
- context sensitivities,
- uncertainty patterns,
- collaboration patterns,
- temporal change.

Therefore:

```text
more information
  =
more privacy responsibility
```

The fingerprint should not silently become an identity-tracking fingerprint.

---

# Contestability

If a future real-person PAX-style profile had consequential use, the subject should be able to:

- inspect relevant evidence,
- identify factual errors,
- challenge interpretation,
- provide contextual information,
- request review,
- add appropriate evidence,
- preserve unresolved disagreement.

The profile should not trap a person inside its own previous observations.

---

# Temporal Boundary

A future real profile should carry:

```yaml
profile:
  observed_at:
  evidence_window:
  framework_version:
  dimension_registry_version:
  adapter_versions:
  substrates_observed:
  regimes_observed:
  model_versions:
  reassessment_status:
```

The profile is a snapshot of observations.

It is not timeless identity.

---

# Minimal RIQF Example Record

```yaml
resonant_iq_fingerprint:
  subject:
    id: PAX-01
    synthetic: true

  assessment:
    status: demonstration
    validation_state: unvalidated
    decision_authority: none

  baseline:
    model: synthetic_conventional_model
    composite: 94
    preserved: true

  dimensions:
    pattern_recognition:
      expression: strong
      confidence: medium

    structural_reasoning:
      expression: strong
      confidence: medium

    cross_domain_transfer:
      expression: strong
      confidence: medium

    regime_recognition:
      expression: strong
      confidence: medium

    ambiguity_navigation:
      expression: strong
      confidence: medium

    long_horizon_integration:
      expression: strong
      confidence: medium

    rapid_symbolic_processing:
      expression: weak
      confidence: medium

    timed_classification:
      expression: weak
      confidence: medium

    environmental_fit:
      expression: unknown
      confidence: none

  substrate_profile:
    reflective:
      expression: strong

    relational:
      expression: strong

    severe_time_constraint:
      expression: weak

  adapters:
    fft:
      status: candidate

    inverted_star:
      status: candidate

    structural_detection:
      status: candidate

    rtt:
      status: candidate

    resonance:
      status: candidate

  coherence:
    profile: moderate_to_high
    scalar: low
    adapter: moderate

  drift:
    status: multidimensional

  uncertainty:
    causal_explanation: unresolved
    external_validity: unvalidated
    population_generalization: unknown

  composite:
    permitted: true
    interpretive_status: lossy_projection
    sufficient_alone: false
    profile_required: true
```

---

# Example Final Assessment

A defensible conclusion for this **synthetic example** is:

> **PAX-01 demonstrates an asymmetric synthetic capability profile in which performance varies materially across task types and measurement conditions. The fictional conventional assessment accurately preserves several observed weaknesses, particularly rapid symbolic and timed classification performance, but its broad scalar interpretation does not adequately represent the full constructed observation set. The multidimensional profile provides a more complete representation of this synthetic evidence, while the causal meaning, population validity, and scientific validity of the proposed RIQF dimensions and adapters remain unestablished.**

That is intentionally narrower than:

> "PAX-01 is actually highly intelligent."

The latter is exactly the kind of unsupported identity claim this module is designed to avoid.

---

# What the Example Demonstrates

The example demonstrates:

```text
how to preserve a baseline
how to add multidimensional observations
how to represent substrate variation
how adapters can contribute
how adapter agreement differs from evidence independence
how coherence can be multidimensional
how drift can change profile shape
how counterfactual tests can challenge the profile
how uncertainty remains explicit
how validation status remains separate from representation
how a composite can remain without becoming identity
```

---

# What the Example Does Not Demonstrate

The example does **not** establish:

```text
RIQF validity
RIQF reliability
a new theory of intelligence
the validity of FFT for intelligence assessment
the validity of The Inverted Star for intelligence assessment
the validity of Structural Detection for intelligence assessment
the validity of RTT for intelligence assessment
the validity of Resonance for intelligence assessment
real substrate effects
real regime effects
real cognitive dimensions
population norms
clinical significance
employment validity
educational validity
cross-cultural validity
human-AI cognitive equivalence
```

Those are research questions.

---

# Core Invariants

```text
scalar != identity
profile != identity
measurement != total_capability
weak_dimension != low_human_worth
strong_dimension != high_human_worth
asymmetry != superiority
difference != disorder
substrate_effect != causal_explanation
regime_effect != causal_explanation
adapter_agreement != independent_evidence
coherence != truth
counterfactual != observation
drift != degradation
collaborative_performance != individual_performance
synthetic_example != validation
richer_profile != better_model
experimental_dimension != established_construct
composite != total_intelligence
unknown != failure
```

---

# Closing Principle

The simplest version of the example is:

```text
94
```

The richer version says:

```text
strong here
moderate here
weak here
unknown here

strong under these conditions
weak under these conditions

stable here
changing here

supported here
uncertain here

prediction fits here
prediction fits poorly here
```

The richer representation is unquestionably larger.

Whether it is scientifically **better** is something the module must earn through validation.

That is the opportunity.

Not to manufacture a more flattering intelligence score.

Not to prove that every person misunderstood by one system is secretly exceptional.

But to create a grammar capable of asking a better question:

> **What if intelligence is not best represented as where a system lands on one line, but as the reproducible shape of what it can do, under which conditions, across which substrates and regimes, with what stability, evidence, and uncertainty?**

`PAX-01` is only a synthetic example.

The field gets to decide, through evidence, whether the larger idea survives.
