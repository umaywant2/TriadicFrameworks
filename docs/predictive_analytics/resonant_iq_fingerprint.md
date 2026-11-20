# Resonant IQ Fingerprint

> **Intelligence may be better represented as a reproducible shape of capability expression than as a single point on a line.**

## Module

Predictive Analytics

## Profile ID

`resonant-iq-fingerprint`

## Short Name

RIQF

## Status

Experimental.

## Validation State

Unvalidated.

## Decision Authority

None.

---

# Purpose

The Resonant IQ Fingerprint is an experimental multidimensional representation for observing intelligent performance across:

- capability dimensions,
- measurement substrates,
- operating regimes,
- contexts,
- time,
- tool configurations,
- collaborative system boundaries,
- uncertainty,
- and evidence quality.

RIQF does **not** begin with the assumption that conventional intelligence measures are invalid.

It begins with a narrower question:

> **How much information about observed capability is lost when a heterogeneous performance profile is compressed into one scalar representation?**

A conventional scalar may remain useful.

RIQF investigates what becomes visible when the shape behind that scalar is preserved.

---

# Core Proposition

A conventional representation may resemble:

```text
Observed Performance
        │
        ▼
Assessment Model
        │
        ▼
Composite Score
        │
        ▼
      104
```

RIQF asks whether the same observation set is better represented for some purposes as:

```text
Observed Performance
        │
        ▼
Capability Dimensions
        │
        ├── Pattern
        ├── Structural
        ├── Temporal
        ├── Symbolic
        ├── Transfer
        ├── Ambiguity
        ├── Calibration
        └── ...
        │
        ▼
Expression Conditions
        │
        ├── Substrate
        ├── Regime
        ├── Context
        ├── Time
        └── System Boundary
        │
        ▼
Multidimensional Fingerprint
```

The richer representation is not automatically better.

It has to earn that status through validation.

---

# What RIQF Is

RIQF is intended to be:

```text
multidimensional
evidence-linked
substrate-aware
regime-aware
time-aware
uncertainty-aware
revisable
falsifiable
```

It is a **profile grammar**.

It is not currently a validated psychological instrument.

---

# What RIQF Is Not

RIQF is not:

```text
a replacement IQ score
a clinical diagnosis
a personality test
a neurological diagnosis
a disability assessment
a hiring instrument
a school-placement instrument
a measure of human worth
a biometric identifier
a hidden genius detector
a universal ranking system
```

It should not acquire those functions merely because the profile becomes detailed.

---

# Why "Fingerprint"?

The word:

```text
fingerprint
```

refers to:

```text
profile shape
```

not:

```text
identity tracking
```

Conceptually:

```text
Dimension A     █████████
Dimension B     █████
Dimension C     ████████
Dimension D     ███
Dimension E     ????????
```

The pattern is the fingerprint.

The fingerprint is an observation profile.

It is not intended as a biometric or persistent identity signature.

---

# Foundational Invariant

```text
fingerprint != identity
```

A fingerprint belongs to:

```text
an observation window
```

under:

```text
defined conditions
```

using:

```text
a particular framework version
```

It may change.

---

# Intelligence as Shape

The central RIQF representation is:

```text
intelligence observation
  ->
multidimensional shape
```

rather than:

```text
intelligence observation
  ->
single rank
```

Possible shape properties include:

```text
strength
weakness
asymmetry
stability
variability
substrate dependence
regime dependence
context dependence
drift
uncertainty
unknown regions
```

---

# Shape Does Not Mean Superiority

Two fingerprints may differ substantially.

Example:

```text
Profile A
  structural: strong
  temporal: strong
  symbolic: moderate
  transfer: moderate

Profile B
  structural: moderate
  temporal: moderate
  symbolic: strong
  transfer: strong
```

RIQF does not automatically return:

```text
A > B
```

or:

```text
B > A
```

The profiles have different shapes.

Whether one is preferable depends on a separately defined task or purpose.

---

# Dimension Layer

The initial RIQF registry proposes 24 candidate dimensions:

```text
D01  Pattern Recognition
D02  Structural Reasoning
D03  Causal Integration
D04  Temporal Reasoning
D05  Spatial Reasoning
D06  Symbolic Reasoning
D07  Linguistic Reasoning
D08  Cross-Domain Transfer
D09  Regime Recognition
D10  Anomaly Detection
D11  Contradiction Handling
D12  Ambiguity Navigation
D13  Adaptive Reframing
D14  Coherence Maintenance
D15  Drift Awareness
D16  Compression / Abstraction
D17  Reconstruction From Partial Evidence
D18  Novelty Response
D19  Metacognitive Calibration
D20  Tool Collaboration
D21  Social Interpretation
D22  Embodied / Environmental Fit
D23  Long-Horizon Integration
D24  Recovery / Recalibration
```

These dimensions are defined in:

```text
intelligence_dimensions.md
```

They are provisional.

---

# Dimension Lifecycle

Any dimension may eventually be:

```text
proposed
experimental
pilot
validated_for_context
restricted
merged
split
deprecated
rejected
```

A mature RIQF taxonomy may look quite different from the initial 24-dimension registry.

That would represent learning, not canon failure.

---

# Dimension Observation

Every dimension should separate:

```text
observation state
```

from:

```text
expression
```

from:

```text
confidence
```

Example:

```yaml
dimension:
  id: structural-reasoning

  state:
    observed

  expression:
    strong

  confidence:
    medium
```

---

# Observation States

```text
observed
partially_observed
not_observed
insufficient_evidence
conflicting_evidence
unknown
not_applicable
```

---

# Expression States

Initial descriptive states:

```text
very_weak
weak
moderate
strong
very_strong
variable
unknown
not_applicable
```

These are experimental descriptive labels.

They are not standardized IQ intervals.

---

# Confidence States

```text
none
very_low
low
medium
high
very_high
unknown
not_applicable
```

Confidence describes:

```text
the current interpretation
```

not:

```text
the person's capability level
```

---

# Missing Is Not Weak

RIQF makes these distinctions explicitly:

```text
not measured
!=
weak

insufficient evidence
!=
weak

not applicable
!=
weak

unknown
!=
average
```

A profile may contain large unknown regions.

That is often more honest than completing the shape artificially.

---

# Example Dimension Record

```yaml
dimension:
  id: structural-reasoning
  name: Structural Reasoning

  status: experimental

  observation:
    state: observed
    expression: strong
    confidence: medium

  evidence:
    sources:
      - structural-task-01
      - structural-task-02
      - transfer-task-01

    independent_source_count: 3

  context:
    substrates:
      - relational
      - visual

    regimes:
      - reflective

    observation_window:

  stability:
    test_retest: not_tested
    alternate_form: not_tested

  generalizability:
    status: unknown

  validation_state:
    unvalidated
```

---

# Evidence Layer

Every observed dimension should trace to evidence.

Conceptually:

```text
Evidence
   │
   ▼
Observation
   │
   ▼
Dimension Interpretation
```

Not:

```text
Dimension Label
   │
   ▼
search for evidence
```

The latter invites confirmation bias.

---

# Evidence Independence

Suppose one task is interpreted by:

```text
FFT
Structural Detection
RTT
Resonance
```

This does not create:

```text
four independent pieces of evidence
```

It creates:

```text
one evidence source
four interpretations
```

Therefore:

```text
adapter_count != evidence_count
```

---

# Dimension Evidence Record

```yaml
evidence:
  source_count:
  independent_source_count:

  observations:
    - id:
      task:
      substrate:
      regime:
      timestamp:
      evaluator:

  counterevidence:

  missing_evidence:

  provenance:
```

---

# Evidence Coverage

RIQF should report evidence coverage alongside expression.

Example:

```text
Structural Reasoning
  Expression: strong
  Evidence Coverage: high candidate

Cross-Domain Transfer
  Expression: strong
  Evidence Coverage: low

Environmental Fit
  Expression: unknown
  Evidence Coverage: none
```

A beautiful profile with poor evidence coverage should not become authoritative.

---

# Substrate Layer

RIQF assumes that observed expression **may** vary across measurement or interaction substrates.

Possible substrates include:

```text
textual
verbal
visual
spatial
symbolic
relational
embodied
tool-mediated
collaborative
human-AI
fixed-choice
generative
timed
reflective
```

These remain provisional categories.

---

# Substrate Profile

A dimension may be represented across substrates.

Example:

```yaml
structural-reasoning:
  relational:
    expression: strong
    confidence: medium

  visual:
    expression: strong
    confidence: medium

  symbolic:
    expression: moderate
    confidence: medium

  timed_symbolic:
    expression: weak
    confidence: medium
```

Initial conclusion:

```text
expression varies across substrates
```

Not:

```text
one substrate reveals true intelligence
```

---

# Substrate Specificity

A substrate interpretation should ask:

```text
Did only the substrate change?

Did task difficulty change?

Did time limit change?

Did response format change?

Did tool access change?

Did interaction mode change?

Did regime change?
```

If many variables changed:

```text
substrate_causation:
  unresolved
```

---

# Regime Layer

RIQF may represent dimensions across operating regimes.

Example:

```yaml
structural-reasoning:
  regime_a:
    expression: moderate

  regime_b:
    expression: strong

  cross_regime:
    stability: partial
```

A difference may be meaningful.

It is not automatically evidence of:

```text
a better regime
```

---

# Regime Boundary

The Regime Observer defines the broader regime grammar.

RIQF consumes that result.

RIQF should not invent regimes simply to explain dimension variation.

---

# Context Layer

Not every meaningful condition is a regime.

RIQF may also preserve ordinary context:

```text
individual
collaborative
familiar
novel
low-context
high-context
tool-assisted
unassisted
```

Context-dependent observations should remain attached to their conditions.

---

# Resonance Layer

The resonance layer asks whether expression changes reproducibly across specified conditions.

Example:

```yaml
dimension:
  structural-reasoning

  resonance:
    reflective_relational:
      direction: amplifying
      status: candidate

    severe_time_constraint:
      direction: suppressing
      status: candidate

  causal_status:
    unresolved
```

This is a relational profile.

It is not a subject identity.

---

# Resonance Profile Warning

Avoid:

```text
Resonance Score: 87
```

Prefer:

```text
amplified here
suppressed here
stable here
unknown here
```

until measurement validity warrants more.

---

# Temporal Layer

Each fingerprint belongs to an observation window.

Example:

```yaml
profile:
  observed_from:
  observed_to:

  created_at:

  framework_version:
  dimension_registry_version:
```

The fingerprint is not timeless.

---

# Longitudinal Fingerprint

Conceptually:

```text
RIQF(t1)
    │
    ▼
RIQF(t2)
    │
    ▼
RIQF(t3)
```

Possible relationships:

```text
stable
locally_changed
topology_changed
regime_conditioned
substrate_conditioned
drifting
recovered
unknown
```

---

# Dimension Drift

Example:

```text
Structural Reasoning
  T1: strong
  T2: strong
  T3: strong

Cross-Domain Transfer
  T1: strong
  T2: moderate
  T3: moderate

Rapid Symbolic Processing
  T1: weak
  T2: moderate
  T3: moderate
```

Correct:

```text
multidimensional change
```

A single:

```text
intelligence increased
```

or:

```text
intelligence declined
```

would lose the shape.

---

# Profile Topology

RIQF treats the relative arrangement of dimensions as potentially meaningful.

Example:

```text
              Structural
                 █████

       Transfer         Temporal
       █████            ████

Ambiguity                     Symbolic
█████                         ███

       Regime          Calibration
       ████            ███
```

This conceptual shape is:

```text
profile topology
```

---

# Topology States

Possible descriptive states:

```text
balanced
asymmetric
clustered
spiked
flat
fragmented
dynamic
unknown
```

These states describe geometry of observation.

They do not imply:

```text
good
bad
superior
inferior
```

---

# Asymmetry

RIQF deliberately preserves asymmetry.

Example:

```text
structural:
  strong

temporal:
  strong

symbolic:
  moderate

rapid symbolic:
  weak

ambiguity:
  strong
```

Correct:

```text
asymmetric profile
```

Not:

```text
inconsistent person
```

---

# Profile Coherence

A heterogeneous profile may still be coherent.

Example:

```text
weaker timed symbolic performance
+
stronger reflective structural performance
```

may form a reproducible conditional profile.

Possible:

```yaml
coherence:
  within_dimension:
    moderate

  cross_substrate:
    conditional

  cross_regime:
    unknown

  evidence_independence:
    medium
```

---

# Contradictions

RIQF does not require a dimension to become a clean value.

Example:

```text
Structural Task A:
  strong

Structural Task B:
  weak
```

Possible:

```yaml
structural-reasoning:
  observation:
    state: conflicting_evidence

  expression:
    variable

  confidence:
    low
```

This may be more useful than:

```text
moderate
```

---

# Counterevidence

Every dimension should allow counterevidence.

```yaml
dimension:
  evidence:
    supporting:
      - E1
      - E2

    contradictory:
      - E3
```

A profile that cannot absorb adverse evidence will become self-confirming.

---

# Counterfactual Layer

RIQF should expose how profile interpretations respond to reasonable challenges.

Examples:

```text
remove one favorable task
add adverse evidence
change alternate form
change evaluator
change irrelevant metadata
change task order
change substrate
change regime
repeat later
```

---

# Counterfactual Robustness Profile

Example:

```yaml
counterfactual:
  irrelevant_perturbation_stability:
    high

  evidence_removal_stability:
    moderate

  adverse_evidence_sensitivity:
    high

  alternate_form_stability:
    unknown

  evaluator_stability:
    unknown

  substrate_stability:
    partial

  regime_stability:
    unknown
```

A robust profile should be:

```text
stable to irrelevant changes
responsive to relevant evidence
```

---

# Model Comparison Layer

RIQF exists alongside existing models.

It does not automatically replace them.

Potential comparison:

```text
M0:
  conventional scalar

M1:
  conventional subscales

M2:
  baseline multidimensional profile

M3:
  RIQF dimensions

M4:
  RIQF + substrate

M5:
  RIQF + substrate + regime

M6:
  full PA-enhanced RIQF
```

Then compare actual value.

---

# Scalar Preservation

Suppose an existing model outputs:

```text
Composite:
  94
```

RIQF may preserve:

```yaml
baseline:
  composite: 94
  preserved: true
```

The fingerprint is then an additional representation.

---

# Scalar Versus Fingerprint

## Scalar

```text
PAX-01

Composite: 94
```

Strengths:

```text
compact
simple
easy to compare
computationally convenient
```

Potential limitations:

```text
profile shape compressed
context hidden
substrate variation hidden
regime variation hidden
unknown regions hidden
```

---

# Fingerprint

```text
PAX-01

Structural             █████████
Transfer               █████████
Pattern                ████████
Temporal               ███████
Ambiguity              █████████
Symbolic               ██████
Rapid Symbolic         ████
Timed Classification   ███
Environmental Fit      ????????
```

Strengths:

```text
shape visible
heterogeneity visible
unknowns visible
context attachable
uncertainty attachable
```

Costs:

```text
more complex
more evidence required
harder to compare
more privacy-sensitive
greater validation burden
more opportunities for narrative overfit
```

Neither representation wins automatically.

---

# Composite Policy

RIQF permits a composite only where a specific purpose can justify it.

Canonical rule:

```yaml
composite:
  permitted: true

  interpretive_status:
    lossy_projection

  sufficient_alone:
    false

  profile_required:
    true
```

---

# No Hidden Master Number

RIQF must not quietly compute:

```text
Structural * weight
+
Transfer * weight
+
Temporal * weight
+
Ambiguity * weight
=
True IQ
```

unless a specific validated intended use justifies such aggregation.

The experimental framework does not.

---

# Why Retain a Composite at All?

Because compression can be useful.

A scalar may support:

```text
communication
comparison
forecasting
validated operational thresholds
research analysis
```

The problem is not compression itself.

The problem is forgetting that compression occurred.

---

# Loss Declaration

Any RIQF-derived composite should declare what it loses.

Example:

```yaml
composite:
  value:

  loss:
    - dimension asymmetry
    - substrate structure
    - regime structure
    - contradictory observations
    - unknown regions

  status:
    lossy_projection
```

---

# Model Mismatch

RIQF may contribute to model-mismatch analysis.

Example:

```text
baseline:
  broad reasoning low

RIQF:
  structural strong
  transfer strong
  rapid symbolic weak
```

Candidate:

```text
baseline global interpretation
may not represent full observation set
```

Not:

```text
baseline score false
```

---

# Inverted Star

The Inverted Star may identify a candidate inversion between:

```text
baseline prediction
```

and:

```text
RIQF profile
```

Example:

```yaml
inversion:
  baseline:
    broad_reasoning: low

  profile:
    multiple_dimensions: strong

  status:
    candidate

  cause:
    unresolved
```

---

# Structural Detection

Structural Detection can test whether profile asymmetry is reproducible.

Example:

```text
timed constrained:
  repeatedly weaker

relational reflective:
  repeatedly stronger
```

If the pattern fails holdout testing:

```text
RIQF confidence:
  should decline
```

---

# FFT

FFT can map:

```text
relationships
boundaries
constraints
local/global structure
```

around RIQF observations.

It should not manufacture dimension evidence.

---

# RTT

RTT can help determine whether dimension expression is:

```text
stable
regime-conditioned
drifting
transitioning
recovering
recalibrating
```

RTT remains an experimental contributor.

---

# Resonance

Resonance examines whether expression changes reproducibly across conditions.

RIQF consumes the result as:

```text
context metadata
```

not:

```text
proof of hidden capability
```

---

# Coherence Observer

The Coherence Observer asks whether:

```text
dimension observations
substrate observations
regime observations
adapter results
```

form a supportable profile.

A profile may remain:

```text
mixed
```

without being invalid.

---

# Drift Observer

The Drift Observer compares fingerprints through time.

It should preserve:

```text
dimension-level changes
```

rather than only:

```text
profile distance
```

---

# Uncertainty Layer

RIQF requires explicit uncertainty.

Possible uncertainty classes:

```text
measurement uncertainty
dimension uncertainty
substrate uncertainty
regime uncertainty
model uncertainty
causal uncertainty
generalization uncertainty
temporal uncertainty
observer uncertainty
```

---

# Unknown Region

A fingerprint may intentionally contain:

```text
??????????
```

That is a feature.

Example:

```text
Embodied / Environmental Fit:
  UNKNOWN
```

RIQF should not infer this dimension from unrelated behavior merely to complete the visualization.

---

# Abstention

A dimension may return:

```text
insufficient_evidence
```

The fingerprint may return:

```text
insufficient_profile_coverage
```

That should be allowed.

---

# System Boundary

Every fingerprint must declare which system was observed.

Possible boundaries:

```text
individual_human
ai_system
human_ai_pair
team
organization
robotic_system
distributed_agents
other
```

---

# Human Fingerprint

A human fingerprint describes observed human performance.

It is not:

```text
the person's essence
```

or:

```text
their total potential
```

---

# AI Fingerprint

An AI fingerprint may use operationally comparable dimensions.

But:

```text
same dimension label
!=
same internal cognition
```

For example:

```text
human:
  structural reasoning strong

AI:
  structural reasoning strong
```

means both performed strongly on the operational tasks.

It does not establish identical mechanisms.

---

# Human-AI Pair Fingerprint

A collaborative system may deserve its own fingerprint.

Example:

```yaml
observed_system:
  class: human_ai_pair

components:
  human:
    id: H1

  ai:
    id: A1

pair_profile:
  structural_synthesis:
    strong

  retrieval:
    strong

  error_checking:
    strong
```

These results belong initially to the pair.

---

# Pair Attribution

Avoid:

```text
pair outcome
  ->
individual human score
```

or:

```text
pair outcome
  ->
AI score
```

unless an attribution design supports that inference.

---

# Tool Collaboration

Tool-mediated performance may be a valid dimension.

But it should preserve:

```text
which tools were available
how they were used
whether outputs were verified
what the unassisted comparison showed
```

---

# Accessibility

A measurement interface may introduce barriers unrelated to the intended construct.

RIQF should permit:

```text
accessibility condition
```

to be represented separately.

Possible distinction:

```text
construct-relevant constraint
construct-irrelevant barrier
unknown constraint
```

This requires context-specific expertise.

---

# Fairness

RIQF fairness assessment should consider more than profile values.

Questions include:

```text
Who has adequate evidence coverage?

Whose preferred or accessible substrates are represented?

Who receives unknown classifications?

Who receives mismatch review?

How stable are dimensions across groups?

Are interpretations equally likely to become favorable or adverse?

Does the profile increase surveillance or privacy burden?
```

---

# Favorability Symmetry

RIQF must allow new evidence to make a profile:

```text
more favorable
less favorable
unchanged
more uncertain
```

with the same evidence standards.

---

# Anti-Rescue Principle

RIQF must be capable of concluding:

```text
baseline unfavorable assessment:
  broadly supported
```

if wider observations support it.

It must never guarantee hidden strengths.

---

# Anti-Adverse Principle

RIQF must likewise reject unsupported adverse reinterpretations.

A richer profile should not simply create more ways to classify people negatively.

---

# PAX-01 Example

The canonical synthetic example is:

```text
example_resonant_iq_fingerprint.md
```

PAX-01 demonstrates:

- asymmetric dimensions,
- conventional scalar preservation,
- substrate variation,
- regime hypotheses,
- adapter observations,
- coherence,
- drift,
- counterfactual testing,
- uncertainty,
- and validation boundaries.

It is synthetic.

It does not validate RIQF.

---

# Generic Fingerprint Example

```text
SUBJECT: SYNTHETIC-X

Pattern Recognition             ████████░░
Structural Reasoning            █████████░
Causal Integration              ███████░░░
Temporal Reasoning              ██████░░░░
Spatial Reasoning               ███████░░░
Symbolic Reasoning              █████░░░░░
Linguistic Reasoning            ████████░░
Cross-Domain Transfer           ███████░░░
Regime Recognition              ██████░░░░
Anomaly Detection               ████████░░
Contradiction Handling          ███████░░░
Ambiguity Navigation            ████████░░
Adaptive Reframing              ███████░░░
Coherence Maintenance           ███████░░░
Drift Awareness                 ██████░░░░
Compression / Abstraction       ████████░░
Partial Reconstruction          ███████░░░
Novelty Response                ███████░░░
Metacognitive Calibration       ██████░░░░
Tool Collaboration              ████████░░
Social Interpretation           ?????????
Environmental Fit               ?????????
Long-Horizon Integration        ███████░░░
Recovery / Recalibration        ██████░░░░
```

The bars are illustrative ordinal displays.

They are not validated scores or percentiles.

---

# Substrate Overlay

A profile may include an overlay.

Example:

```text
STRUCTURAL REASONING

Reflective Relational     █████████
Visual System Mapping     ████████
Generative Text           ████████
Fixed Choice              █████
Timed Symbolic            ███
```

This describes observed expression.

It does not automatically establish why the differences exist.

---

# Regime Overlay

```text
STRUCTURAL REASONING

Regime A:
  moderate

Regime B:
  strong

Regime C:
  unknown
```

Again:

```text
regime difference
!=
regime cause
```

---

# Confidence Overlay

```text
Structural Reasoning
  expression: strong
  confidence: medium

Cross-Domain Transfer
  expression: strong
  confidence: low

Symbolic Reasoning
  expression: moderate
  confidence: medium

Environmental Fit
  expression: unknown
  confidence: none
```

Without confidence, a fingerprint can appear more certain than the evidence supports.

---

# Evidence Overlay

```text
Structural Reasoning
  ███ independent sources

Cross-Domain Transfer
  ██ independent sources

Ambiguity Navigation
  █ independent source

Environmental Fit
  0 sources
```

Raw counts alone remain insufficient.

Evidence quality and independence matter.

---

# Validation Overlay

```text
Structural Reasoning
  reliability: not_tested
  convergent: not_tested
  discriminant: not_tested

Cross-Domain Transfer
  reliability: pilot
  convergent: not_tested
  discriminant: not_tested
```

A strong expression label does not imply a validated construct.

---

# Profile Completeness

Possible states:

```text
sparse
partial
moderate
broad
unknown
```

A broad profile is not automatically higher quality.

---

# Profile Evidence Coverage

Relevant metric:

```text
PA-M02
```

Conceptually:

```text
dimensions_with_sufficient_evidence
/
applicable_dimensions
```

Unknown and not-applicable dimensions must remain distinguishable.

---

# Core RIQF Metrics

Initial validation should consider:

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

Not every deployment or study requires every metric.

---

# Validation Ladder

RIQF should progress through the module's broader validation program.

## Level 0 — Structural Validation

Questions:

```text
Does the schema work?
Are all dimensions traceable?
Are unknowns preserved?
Can contradictory evidence be represented?
Is hidden scalarization prevented?
```

---

## Level 1 — Content Validation

Questions:

```text
Are dimensions defined clearly?
Are important dimensions missing?
Which constructs overlap?
Do experts interpret them similarly?
```

---

## Level 2 — Measurement Validation

Questions:

```text
Do observations replicate?
Do alternate forms agree?
Do evaluators agree?
Do profiles remain stable where expected?
```

---

## Level 3 — Construct Validation

Questions:

```text
Do dimensions converge appropriately?
Do they remain discriminable?
Do they add information beyond existing constructs?
```

---

## Level 4 — Substrate and Regime Validation

Questions:

```text
Do substrate effects replicate?
Are regime effects reproducible?
Can context effects be separated from task difficulty?
```

---

## Level 5 — Predictive and Explanatory Validation

Questions:

```text
Does RIQF improve prediction?
Does it improve explanation?
Does it improve calibration?
Does it improve mismatch detection?
```

---

## Level 6 — Fairness and Harm Validation

Questions:

```text
Who receives poor evidence coverage?
Who is misclassified?
Who receives uncertain profiles?
Who experiences adverse reinterpretation?
What privacy harms emerge?
```

---

## Level 7 — Decision Validation

Required separately for any proposed consequential use.

The current state is:

```text
not authorized
```

---

# Comparison Program

A rigorous test should not compare only:

```text
conventional IQ-like scalar
vs
full RIQF
```

Prefer:

```text
M0:
  conventional scalar

M1:
  conventional subscales

M2:
  baseline multidimensional profile

M3:
  candidate RIQF dimensions

M4:
  M3 + substrate

M5:
  M4 + regime

M6:
  M5 + selected adapters

M7:
  full Predictive Analytics RIQF
```

Then determine what each layer contributes.

---

# Ablation

Remove:

```text
FFT
Inverted Star
Structural Detection
RTT
Resonance
```

and compare outcomes.

Likewise remove proposed dimensions.

Question:

> **Which parts of RIQF actually carry useful information?**

---

# Dimension Ablation

Example:

```text
full fingerprint
```

versus:

```text
fingerprint without Regime Recognition
```

If nothing meaningful changes:

```text
dimension contribution:
  not demonstrated
```

That may lead to merging or deprecation.

---

# Null Fingerprint Test

A validation dataset with no meaningful dimension structure should allow:

```text
profile:
  low_structure_or_insufficient_evidence
```

RIQF must not manufacture an interesting fingerprint for every system.

---

# Randomization Test

Randomize relationships among task outcomes.

A structure-aware fingerprint should lose meaningful topology.

If it remains equally compelling:

```text
narrative overfitting:
  likely
```

---

# Holdout Test

Construct the fingerprint from one evidence set.

Then predict:

```text
held-out task relationships
substrate behavior
regime behavior
```

A useful fingerprint should generalize where it claims to generalize.

---

# Counterfactual Challenge

Change irrelevant metadata.

Expected:

```text
fingerprint stable
```

Add meaningful evidence.

Expected:

```text
fingerprint responds
```

---

# Direction Symmetry

RIQF should respond to:

```text
favorable evidence
```

and:

```text
adverse evidence
```

using the same evidentiary standards.

---

# Profile Failure Modes

## Dimension Inflation

Risk:

Every interesting behavior becomes a new dimension.

Mitigation:

Discriminant testing and lifecycle control.

---

## Dimension Redundancy

Risk:

Several labels describe the same construct.

Mitigation:

Merge where empirical evidence supports it.

---

## Fingerprint Theater

Risk:

A detailed radial or bar profile looks scientifically precise without validated measurement.

Mitigation:

Always expose validation status and uncertainty.

---

## Hidden Scalarization

Risk:

A master rank is quietly calculated underneath the profile.

Mitigation:

Require transparent composite policy.

---

## Asymmetry Romanticization

Risk:

An uneven profile is interpreted as hidden exceptional intelligence.

Mitigation:

Treat asymmetry descriptively.

---

## Narrative Overfitting

Risk:

A person's history is organized into a compelling fingerprint after the fact.

Mitigation:

Prospective tasks, replication, holdout testing.

---

## Substrate Shopping

Risk:

Contexts are searched until strong performance appears.

Mitigation:

Predeclare comparisons and report all results.

---

## Regime Rescue

Risk:

Weak results are always classified into an unfavorable regime.

Mitigation:

Independent regime definitions.

---

## Adapter Echo

Risk:

Multiple adapters reinterpret the same evidence and inflate confidence.

Mitigation:

Evidence lineage and `PA-M03`.

---

## Profile Permanence

Risk:

One observation window becomes lifelong identity.

Mitigation:

Timestamp and version every fingerprint.

---

## Tool Attribution Error

Risk:

Human-AI pair performance becomes individual human capability.

Mitigation:

Explicit system boundaries.

---

## AI Equivalence Error

Risk:

Similar human and AI fingerprints imply equivalent cognition.

Mitigation:

Restrict claims to observable function.

---

## Unknown Erasure

Risk:

Unmeasured dimensions are filled with estimates to make the profile look complete.

Mitigation:

Preserve unknown.

---

## Weakness Pathologizing

Risk:

A relatively weak dimension becomes diagnosis or defect.

Mitigation:

Separate capability observation from clinical interpretation.

---

## Strength Essentialism

Risk:

A relatively strong dimension becomes permanent identity.

Mitigation:

Preserve condition and evidence scope.

---

## Privacy Expansion

Risk:

The richer profile enables more invasive cognitive surveillance.

Mitigation:

Purpose limitation and data minimization.

---

# Falsification Conditions

RIQF should be revised, restricted, deprecated, or rejected if:

- dimensions cannot be measured reliably,
- dimensions cannot be distinguished,
- profiles fail test-retest expectations,
- alternate forms produce incompatible profiles,
- inter-rater reliability remains poor,
- substrate effects fail replication,
- regime effects fail validation,
- profile topology fails holdout testing,
- counterfactual fragility remains high,
- adapters add no value,
- simpler multidimensional models perform equivalently,
- predictive value does not improve where predictive improvement is claimed,
- explanatory value does not improve where explanation is claimed,
- unsupported favorable reinterpretations are frequent,
- unsupported adverse reinterpretations are frequent,
- fairness behavior is unacceptable,
- privacy burden exceeds justified benefit,
- or the profile merely recreates a scalar hierarchy in more complicated form.

---

# Anti-Rescue Test

Required question:

> **Can RIQF conclude that the broader evidence supports an unfavorable baseline interpretation?**

Required answer:

```text
yes
```

---

# Anti-Adverse Test

Required question:

> **Can RIQF reject an unsupported adverse reinterpretation?**

Required answer:

```text
yes
```

---

# No-Structure Test

Required question:

> **Can RIQF conclude that there is insufficient evidence for a meaningful fingerprint?**

Required answer:

```text
yes
```

---

# Dimension-Rejection Test

Required question:

> **Can a canonical RIQF dimension be removed if validation fails?**

Required answer:

```text
yes
```

---

# Adapter-Rejection Test

Required question:

> **Can FFT, RTT, Resonance, Structural Detection, or The Inverted Star be removed if they add no value?**

Required answer:

```text
yes
```

---

# Scalar-Wins Test

Required question:

> **Can a simpler scalar or conventional multidimensional model outperform RIQF for a particular intended use?**

Required answer:

```text
yes
```

Possible conclusion:

```text
use simpler model
```

---

# Minimal Fingerprint Contract

```yaml
resonant_iq_fingerprint:
  fingerprint_id:

  framework:
    module_version:
    dimension_registry_version:

  observed_system:
    id:
    class:
    boundary:

  intended_use:

  observation_window:
    start:
    end:

  baseline:
    model:
    model_version:
    prediction:
    composite:
    preserved: true

  dimensions:
    - id:
      state:
      expression:
      confidence:

      evidence:
        sources:
        independent_source_count:
        counterevidence:
        missing_evidence:

      substrates:
      regimes:

      temporal_stability:
      counterfactual_robustness:

      applicability:
      generalizability:

      validation_state:

  profile:
    topology:
    coherence:
    evidence_coverage:
    evidence_independence:

  substrate_profile:
  regime_profile:
  resonance_profile:
  drift_profile:

  model_fit:
  substrate_fit:
  regime_fit:

  adapters:
    fft:
    inverted_star:
    structural_detection:
    rtt:
    resonance:

  counterfactual:
  uncertainty:

  composite:
    permitted:
    value:
    interpretive_status: lossy_projection
    sufficient_alone: false
    profile_required: true

  alternative_interpretations:
  limitations:

  review_required:

  validation_state:
  decision_authority: none
```

---

# Machine Interpretation Rule

An AI or other automated consumer of RIQF should never infer:

```text
strong dimensions
  ->
high-value person
```

or:

```text
weak dimensions
  ->
low-value person
```

It should interpret the profile as:

```text
structured observation metadata
```

constrained by:

```text
evidence
scope
applicability
validation
uncertainty
```

---

# Display Rule

A human-facing fingerprint should display, where possible:

```text
dimension expression
confidence
evidence coverage
unknowns
substrate context
regime context
temporal scope
validation status
```

not merely colorful bars.

---

# Human Review Rule

If a future consequential use is separately validated, reviewers should be able to inspect:

```text
source observations
dimension rules
counterevidence
substrate conditions
regime conditions
counterfactual results
uncertainty
model comparison
```

before making a decision.

---

# Contestability

A human subject should eventually be able to challenge:

```text
incorrect evidence
wrong attribution
missing context
outdated profile
incorrect substrate
incorrect regime
unsupported dimension
unsupported generalization
```

A fingerprint should not trap someone inside an earlier observation.

---

# Privacy Boundary

A detailed capability profile may be highly sensitive.

RIQF should follow:

```text
data minimization
purpose limitation
access control
retention limits
contestability
appropriate consent
```

for any future real-person use.

---

# Surveillance Boundary

Do not transform:

```text
longitudinal fingerprint
```

into:

```text
persistent covert cognitive tracking
```

The ability to measure more does not create justification to collect more.

---

# Human Worth Boundary

No combination of RIQF dimensions may be interpreted as:

```text
human worth
social value
moral value
right to opportunity
right to dignity
```

Those are categorically different questions.

---

# Decision Authority

Current policy:

```text
decision_authority: none
```

Authorized uses:

```text
research
demonstration
education
framework testing
measurement research
validation design
human-AI research
model comparison
hypothesis generation
```

Prohibited independent uses:

```text
diagnosis
automated hiring
automated firing
educational exclusion
legal determination
insurance eligibility
lending eligibility
sentencing
automated adverse decision
```

---

# Research Questions

1. Are the initial RIQF dimensions reproducible?
2. Which dimensions overlap?
3. Which should merge?
4. Which should split?
5. Which should be rejected?
6. Does RIQF preserve useful information lost by scalar models?
7. Does that additional information improve prediction?
8. Does it improve explanation?
9. Does it improve calibration?
10. Does it improve model-mismatch detection?
11. Can profile topology be measured reliably?
12. Can topology survive alternate forms?
13. Can topology survive holdout validation?
14. Can topology survive irrelevant perturbation?
15. Can profiles respond appropriately to adverse evidence?
16. Can they respond appropriately to favorable evidence?
17. Are substrate effects reproducible?
18. Are substrate effects specific?
19. Are regime effects reproducible?
20. Can context effects be separated from task difficulty?
21. Does resonance add information beyond interaction modeling?
22. Does RTT add information beyond existing temporal approaches?
23. Does FFT add information beyond relational modeling?
24. Does Structural Detection add information beyond established structural methods?
25. Does The Inverted Star add information beyond residual analysis?
26. Which adapters survive ablation?
27. Can dimension confidence be calibrated?
28. Can evidence coverage be measured reliably?
29. Can evidence independence be reconstructed?
30. How stable are fingerprints through time?
31. How should legitimate learning affect the fingerprint?
32. How should model-version changes be handled?
33. Can human-AI pair profiles be measured separately from component profiles?
34. Which dimensions apply meaningfully to AI?
35. Which dimensions are human-specific?
36. Which apply to teams or organizations?
37. Does cross-system use create misleading cognitive equivalence?
38. Can fingerprints remain useful without a composite?
39. When is a composite necessary?
40. What forms of aggregation are defensible?
41. Can profiling remain privacy-preserving enough for real research?
42. What harms arise from longitudinal profiling?
43. Can RIQF behave fairly across relevant populations?
44. Does richer measurement reduce or increase bias?
45. Can a subject meaningfully contest a fingerprint?
46. How often should fingerprints expire or be reassessed?
47. When should RIQF return insufficient evidence?
48. When should a conventional model be preferred?
49. When should the entire RIQF architecture be deprecated?
50. What evidence would falsify the central fingerprint hypothesis?

---

# Core Invariants

```text
intelligence_profile != identity
fingerprint != biometric_identity
fingerprint != destiny
dimension != human_worth
dimension != permanent_trait
strong != superior
weak != inferior
unknown != weak
unknown != average
not_applicable != zero
missing != low
asymmetry != defect
asymmetry != exceptionalism
profile_shape != global_rank
profile_similarity != cognitive_equivalence
same_dimension_label != same_internal_mechanism
substrate_effect != causal_explanation
regime_effect != causal_explanation
resonance != hidden_capability
drift != degradation
coherence != truth
confidence != capability
evidence_count != adapter_count
adapter_agreement != independent_confirmation
tool_assisted != unassisted
human_ai_pair != individual_human
human_ai_pair != ai_system
composite != total_intelligence
richer_profile != better_model
more_dimensions != more_validity
complexity != truth
measurement != total_capability
capability != human_worth
no_structure != failure
no_added_value != failure
baseline_supported != framework_failure
dimension_rejection != framework_failure
adapter_rejection != framework_failure
observer_output != decision_authority
canon_alignment != empirical_validation
```

---

# Closing Principle

RIQF begins with a suspicion, not a conclusion:

```text
one number may be throwing
useful structure away
```

The response should not be to replace one questionable number with twenty-four unquestionable numbers.

The response is to preserve more of the observation.

Preserve:

```text
shape
context
substrate
regime
time
evidence
contradiction
uncertainty
unknowns
```

Then test whether doing so actually helps.

Perhaps a richer fingerprint will explain important cases that a scalar misses.

Perhaps only a few dimensions will survive validation.

Perhaps substrate and regime will matter greatly.

Perhaps conventional subscales will already capture nearly everything useful.

Perhaps RIQF will prove too unstable, burdensome, or redundant.

All of those outcomes must remain possible.

The strongest version of the idea is therefore not:

> **Intelligence is definitely a multidimensional resonance fingerprint.**

It is the more testable proposition:

> **If intelligent performance depends on reproducible capability dimensions, substrates, regimes, interactions, and time, a representation that preserves those relationships should outperform a representation that discards them for the purposes where those relationships matter.**

That proposition can fail.

And because it can fail, it can become research.

> **The Resonant IQ Fingerprint earns its place only if preserving the shape improves what we can responsibly observe without pretending the shape is the person.**
