<img width="1194" height="672" alt="predictive_analytics_substrate_expression_profile_" src="https://github.com/user-attachments/assets/0785b8a3-ece3-49e9-8358-19070153df45" />

# Predictive Analytics — Substrate Expression Profile

> **Capability is not observed in the abstract. It is observed through conditions that shape how expression becomes measurable.**

## Module

Predictive Analytics

## Profile ID

`substrate-expression-profile`

## Short Name

SEP

## Operator

`PA-Substrate`

## Status

Experimental.

## Validation State

Unvalidated.

## Decision Authority

None.

---

# Purpose

The Substrate Expression Profile represents how a defined target capability, behavior, or system property is observed across multiple measurement or interaction substrates.

It aggregates substrate-aware observations without assuming that:

- one substrate reveals the "true" system,
- stronger performance is more authentic,
- weaker performance is less authentic,
- every cross-substrate difference is meaningful,
- every difference is caused by substrate,
- or all substrates measure the same construct.

The central question is:

> **How does observed expression vary across defined substrates, and which parts of that variation are reproducible enough to preserve in the profile?**

---

# Adapter Versus Profile

The distinction is important.

## Substrate Adapter

The Substrate Adapter evaluates a defined comparison.

Conceptually:

```text
Target Capability
       │
       ├── Substrate A
       │      │
       │      ▼
       │  Expression A
       │
       └── Substrate B
              │
              ▼
          Expression B
              │
              ▼
       Substrate Adapter
              │
              ▼
       comparison result
```

---

## Substrate Expression Profile

The profile integrates many substrate observations.

```text
Substrate Result A ─┐
Substrate Result B ─┤
Substrate Result C ─┼──► Substrate Expression Profile
Substrate Result D ─┤                 │
Independent E1 ─────┤                 ▼
Independent E2 ─────┘          expression topology
```

The adapter asks:

> **Does this comparison reveal a substrate-related difference?**

The profile asks:

> **What larger cross-substrate expression structure, if any, survives across the available evidence?**

---

# Foundational Principle

The Substrate Expression Profile distinguishes:

```text
capability
```

from:

```text
expression
```

from:

```text
measurement
```

from:

```text
interpretation
```

These are related but not interchangeable.

A profile describes:

```text
observed expression
under specified conditions
```

It does not directly reveal:

```text
total underlying capability
```

---

# Expression Is Conditional

A substrate expression statement should conceptually read:

> **For target X, under substrate S, within regime R, during observation window T, expression E was observed with confidence C.**

This is deliberately more specific than:

> X is strong.

---

# Core Representation

Conceptually:

```text
                         Target
                           │
                           ▼
                ┌────────────────────┐
                │ Capability Target  │
                └─────────┬──────────┘
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   Substrate A        Substrate B      Substrate C
        │                 │                 │
        ▼                 ▼                 ▼
 Expression A        Expression B      Expression C
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                 Cross-Substrate
                Expression Profile
```

The profile preserves differences rather than immediately averaging them.

---

# Profile Inputs

The profile may consume:

```text
direct observations
Substrate Adapter results
RIQF dimension observations
model predictions
task results
regime metadata
temporal metadata
accessibility metadata
counterfactual tests
confidence records
uncertainty records
evidence provenance
```

Not every profile requires every input.

Missing information remains missing.

---

# System Boundary

Every profile must declare what system was observed.

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

This becomes especially important when a substrate includes tools or collaborators.

---

# Target Boundary

A profile must identify what expression is being compared.

Examples:

```text
structural reasoning
symbolic reasoning
retrieval performance
cross-domain transfer
task accuracy
error recovery
calibration
long-horizon integration
```

Avoid profiles whose target is merely:

```text
intelligence
```

unless intelligence has itself been operationally defined for the study.

---

# Substrate Configuration

A substrate should generally be represented as a configuration rather than one label.

Example:

```yaml
substrate:
  id: substrate-a

  modality:
    textual

  representation:
    relational

  response_structure:
    generative

  timing:
    reflective

  tools:
    none

  interaction:
    individual

  environment:
    controlled
```

This exposes the actual observation conditions.

---

# Why Configuration Matters

Compare:

```text
timed symbolic fixed-choice
```

with:

```text
reflective relational generative
```

Calling these simply:

```text
symbolic
```

and:

```text
relational
```

hides several changed variables.

The profile should preserve:

```text
what differs
```

before interpreting why expression differs.

---

# Initial Substrate Axes

A substrate configuration may include several independent or interacting axes.

```text
SEP-A01  Modality
SEP-A02  Representation
SEP-A03  Response Structure
SEP-A04  Timing
SEP-A05  Tool Access
SEP-A06  Interaction Mode
SEP-A07  Environmental Interface
SEP-A08  Accessibility Conditions
SEP-A09  Measurement Instrument
SEP-A10  System Boundary
```

These axes are provisional.

---

# SEP-A01 — Modality

Candidate modalities:

```text
textual
verbal
visual
auditory
spatial
embodied
multimodal
unknown
```

---

# SEP-A02 — Representation

Candidate representation structures:

```text
symbolic
relational
narrative
diagrammatic
numerical
spatial
graph
naturalistic
mixed
unknown
```

---

# SEP-A03 — Response Structure

Possible response forms:

```text
binary
fixed-choice
ranking
short-response
generative
interactive
constructive
embodied
mixed
unknown
```

---

# SEP-A04 — Timing

Possible timing conditions:

```text
severely_constrained
constrained
moderate
reflective
self_paced
unknown
```

These require operational definitions in actual studies.

---

# SEP-A05 — Tool Access

Possible states:

```text
none
calculator
reference_material
search
software
external_memory
AI
specialized_instrument
multiple_tools
unknown
```

Tool availability can materially change the observed system.

---

# SEP-A06 — Interaction Mode

Possible:

```text
individual
paired
team
human_ai
multi_agent
human_tool
other
unknown
```

---

# SEP-A07 — Environmental Interface

Possible:

```text
controlled
simulation
physical
remote
field
high_noise
low_noise
unknown
```

Environmental conditions should be represented only where they are relevant to the observation.

---

# SEP-A08 — Accessibility Conditions

Possible:

```text
standard
accommodated
partially_accessible
barrier_detected
unknown
```

This state alone does not determine whether the accommodation changes the construct.

---

# SEP-A09 — Measurement Instrument

A profile should preserve:

```text
instrument
instrument version
scoring process
evaluator
```

where available.

Different instruments may create apparent substrate differences.

---

# SEP-A10 — System Boundary

Examples:

```text
human alone
AI alone
human + calculator
human + AI
team
robot + environment
```

The boundary must not disappear when results are aggregated.

---

# Expression Record

Each substrate observation may use:

```yaml
expression:
  observation_id:

  target:
    id:

  substrate:
    id:

  regime:
    id:

  system_boundary:

  value:
  state:
  confidence:

  timestamp:

  evidence:
    source:
    independent:

  limitations:
```

---

# Expression States

For descriptive profiles:

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

These are experimental ordinal labels.

They are not assumed to have equal numerical spacing.

---

# Observation States

Separate from expression:

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

# Missing Is Not Weak

Critical rules:

```text
not_observed != weak
unknown != moderate
not_applicable != zero
insufficient_evidence != low_capability
```

A profile may legitimately contain large unknown regions.

---

# Confidence

Confidence should describe the evidence supporting the substrate-expression relationship.

Possible states:

```text
none
very_low
low
medium
high
very_high
unknown
```

Avoid converting these labels into probabilities without validated calibration.

---

# Profile Construction Pipeline

```text
Declare Observed System
        │
        ▼
Declare Target
        │
        ▼
Collect Substrate Observations
        │
        ▼
Preserve Raw Observations
        │
        ▼
Normalize Metadata
        │
        ▼
Deduplicate Shared Evidence
        │
        ▼
Check Target Comparability
        │
        ▼
Check Regime Compatibility
        │
        ▼
Check Measurement Compatibility
        │
        ▼
Map Substrate Configurations
        │
        ▼
Map Expression
        │
        ▼
Preserve Contradictions
        │
        ▼
Test Replication
        │
        ▼
Challenge Counterfactually
        │
        ▼
Construct Expression Topology
        │
        ▼
Return Profile
```

---

# Evidence Independence

Suppose one task result is interpreted by:

```text
Substrate Adapter
FFT
Structural Detection
Resonance
RTT
```

Correct:

```yaml
interpretations:
  count: 5

independent_evidence_sources:
  count: 1
```

Not:

```text
evidence count:
  5
```

---

# Evidence Lineage

Suggested structure:

```yaml
evidence:
  id: E1

  observation:
    structural-task-01

  interpretations:
    - substrate
    - fft
    - structural-detection
    - resonance

  independence:
    shared_source

  count_as_independent:
    true
```

The source should be counted once.

---

# Cross-Substrate Comparability

The most important question before comparison is:

> **Are these observations sufficiently comparable to support a cross-substrate claim?**

Possible states:

```text
high
moderate
partial
low
unsupported
unknown
```

---

# Comparability Factors

Consider:

```text
target construct
task difficulty
task content
response demand
timing
regime
environment
measurement instrument
evaluator
system boundary
prior exposure
```

A cross-substrate profile should not imply equivalence merely because two tasks have similar names.

---

# Exact Comparison

The strongest comparison may change only one substrate component.

Example:

```text
Task A:
  symbolic
  timed
  fixed-choice

Task B:
  symbolic
  reflective
  fixed-choice
```

Changed:

```text
timing
```

Held constant:

```text
representation
response structure
target
```

This is easier to interpret than changing everything at once.

---

# Partial Comparison

Sometimes complete matching is impossible.

Example:

```text
verbal explanation
```

versus:

```text
visual reconstruction
```

The profile can still preserve both observations while marking:

```text
direct comparability:
  partial
```

---

# Non-Comparable Observation

Some observations should remain side by side without direct comparison.

Example:

```text
human unassisted structural task
```

versus:

```text
human-AI pair open research synthesis
```

Both are meaningful.

They observe different system boundaries.

Correct:

```text
non_comparable_for_individual_attribution
```

---

# Expression Matrix

A profile can conceptually represent expression as a matrix.

```text
                         Substrate

                 Text   Visual   Symbolic   Relational
              ┌───────┬────────┬──────────┬───────────┐
Structural    │ strong│ strong │ moderate │ strong    │
              ├───────┼────────┼──────────┼───────────┤
Temporal      │ strong│ moderate│ moderate │ strong    │
              ├───────┼────────┼──────────┼───────────┤
Symbolic      │ moder.│ unknown │ strong   │ moderate  │
              ├───────┼────────┼──────────┼───────────┤
Transfer      │ strong│ moderate│ weak     │ strong    │
              └───────┴────────┴──────────┴───────────┘
```

This is conceptual.

Real profiles should retain confidence, provenance, and comparability.

---

# Expression Topology

The profile may identify broad descriptive patterns.

Possible topologies:

```text
substrate_stable
localized
clustered
substrate_sensitive
interaction_sensitive
mixed
fragmented
unstable
unknown
```

These describe the observation structure.

They do not describe human worth or global intelligence.

---

# Substrate-Stable Profile

Example:

```text
text:
  moderate

visual:
  moderate

symbolic:
  moderate

relational:
  moderate
```

Possible:

```yaml
topology:
  substrate_stable
```

within the observed conditions.

This is a meaningful successful outcome.

---

# Localized Expression

Example:

```text
relational:
  strong

everything else:
  moderate
```

Candidate:

```text
localized substrate-associated expression
```

Generalization remains unknown.

---

# Clustered Expression

Example:

```text
reflective textual:
  strong

reflective relational:
  strong

reflective visual:
  strong

timed versions:
  weaker
```

Candidate:

```text
reflective-condition cluster
```

This may implicate timing more than modality.

Counterfactual isolation should test that.

---

# Mixed Expression

Example:

```text
tool assistance:
  retrieval improves
  calibration worsens
  structural reasoning unchanged
```

Correct:

```text
mixed substrate profile
```

Not:

```text
tool assistance helps
```

globally.

---

# Fragmented Profile

Expression varies substantially with no stable substrate relationship.

Example:

```text
Text A:
  strong

Text B:
  weak

Visual A:
  weak

Visual B:
  strong
```

Correct:

```yaml
topology:
  fragmented_or_unresolved
```

Do not invent a deeper substrate explanation merely because the simple one failed.

---

# Contradictory Evidence

The profile must preserve contradictions.

Example:

```yaml
relational_substrate:
  supporting:
    - E1 strong
    - E2 strong

  contradictory:
    - E3 weak

  state:
    mixed

  confidence:
    low_to_medium
```

The contradictory result should not disappear into an average automatically.

---

# Substrate Fit Profile

A substrate expression profile may contribute to substrate fit.

Example:

```yaml
substrate_fit:
  timed_symbolic:
    target:
      structural_reasoning
    status:
      partial

  reflective_relational:
    target:
      structural_reasoning
    status:
      candidate_high

  validation:
    unresolved
```

Fit is always relative to a target.

---

# Difference Versus Effect

Observed:

```text
Expression A
!=
Expression B
```

This establishes:

```text
difference
```

A replicated and appropriately controlled relationship may support:

```text
substrate effect
```

A demonstrated threat to inference may support:

```text
substrate mismatch
```

These are three different levels.

---

# Interpretation Ladder

Use:

```text
Level 0:
  observation

Level 1:
  difference

Level 2:
  replicated difference

Level 3:
  substrate effect candidate

Level 4:
  substrate-specific effect supported

Level 5:
  substrate mismatch candidate

Level 6:
  validated substrate mismatch for context
```

Do not jump directly from:

```text
difference
```

to:

```text
mismatch
```

---

# No Preferred Substrate by Default

The profile should not automatically label one substrate:

```text
best
natural
true
authentic
```

A substrate can produce stronger observed expression because it:

- fits the target better,
- is easier,
- is more familiar,
- permits more time,
- provides more information,
- provides external tools,
- changes the observed system,
- or differs in another relevant way.

The explanation requires evidence.

---

# Profile Versus Preference

A person may report:

```text
I prefer visual tasks.
```

This is a preference observation.

It is not automatically:

```text
visual performance is stronger
```

and neither establishes:

```text
visual learning style
```

or another external construct.

Self-report and measured expression should remain separate.

---

# Accessibility Layer

The profile may record accessibility.

Example:

```yaml
substrate:
  verbal:
    accessibility:
      barrier_detected: true

  textual:
    accessibility:
      barrier_detected: false
```

This may help distinguish measurement barriers from target capability.

---

# Accessibility Is Not Preference

A substrate may be:

```text
accessible
```

without being:

```text
preferred
```

or:

```text
high-performing
```

These fields should remain distinct.

---

# Accommodation Profile

Example:

```yaml
accommodation:
  baseline:
    severe_time_limit

  modified:
    extended_time

  target:
    structural_reasoning

  result:
    expression_changed: true

  construct_impact:
    unknown

  interpretation:
    requires_review
```

An accommodation result should not automatically be treated as the true capability measurement.

---

# Temporal Layer

Substrate expression may change over time.

Example:

```text
T1:
  tool-assisted strong
  unassisted moderate

T2:
  tool-assisted strong
  unassisted strong
```

Possible explanations:

```text
learning
tool transfer
practice
measurement change
regime change
unknown
```

The Drift Observer examines the temporal relationship.

---

# Substrate Profile Drift

Conceptually:

```text
SEP(t1)
    │
    ▼
SEP(t2)
```

Possible outcomes:

```text
stable
localized_change
broad_change
converging
diverging
reversing
unknown
```

---

# Convergence

Example:

```text
T1:
  substrate A strong
  substrate B weak

T2:
  substrate A strong
  substrate B moderate

T3:
  substrate A strong
  substrate B strong
```

The substrate-expression difference narrows.

Possible:

```text
cross-substrate convergence
```

Cause remains unresolved.

---

# Divergence

The opposite pattern may occur.

Again:

```text
divergence
!=
degradation
```

---

# Regime Layer

The same substrate may behave differently across regimes.

Example:

```yaml
relational_substrate:
  regime_a:
    expression: strong

  regime_b:
    expression: moderate
```

Correct:

```text
substrate expression is regime-conditioned
```

rather than assuming one global substrate effect.

---

# Resonance Layer

The Resonance Observer may examine whether substrate expression forms patterns of:

```text
amplification
suppression
stability
instability
```

The SEP provides the cross-substrate observation map.

Resonance supplies a relational interpretation.

---

# Coherence Layer

The Coherence Observer asks whether substrate observations form a supportable structure.

Possible:

```yaml
coherence:
  within_substrate:
    high

  cross_substrate:
    moderate

  contradictions:
    retained

  evidence_independence:
    medium
```

---

# Counterfactual Layer

The profile should survive reasonable perturbation.

Tests:

```text
remove strongest observation
add contradictory evidence
change task order
change evaluator
change irrelevant metadata
match task difficulty
hold timing constant
hold response structure constant
```

---

# Profile Robustness

Example:

```yaml
robustness:
  irrelevant_metadata:
    stable

  single_evidence_removal:
    moderate

  alternate_form:
    partial

  adverse_evidence:
    responsive

  difficulty_matching:
    stable

  evaluator_change:
    unknown
```

---

# Model Mismatch Layer

A substrate expression profile can support model mismatch analysis.

Example:

```text
model predicts:
  broad low structural capability

SEP shows:
  weak on one substrate
  strong on several matched substrates
```

Candidate:

```text
substrate-conditioned model mismatch
```

if sufficient evidence exists.

Not:

```text
model invalid
```

---

# Predictive Model Adapter Integration

The baseline prediction may already encode substrate.

Example:

```yaml
source_model:
  intended_substrate:
    timed_fixed_choice
```

The SEP should preserve that provenance.

If the source model was never intended for:

```text
reflective generative
```

then later comparisons should not pretend otherwise.

---

# RIQF Integration

RIQF dimensions can consume SEP data.

Example:

```yaml
riqf:
  dimension:
    structural-reasoning:

      expression:
        overall:
          strong_candidate

      substrate_profile:
        relational:
          strong

        visual:
          strong

        symbolic:
          moderate

        timed_symbolic:
          weak

      substrate_stability:
        partial

      confidence:
        medium
```

The overall dimension should not erase the substrate structure.

---

# Multiple-Dimension SEP

A full fingerprint may attach different substrate profiles to different dimensions.

Example:

```text
STRUCTURAL REASONING
  relational        strong
  symbolic          moderate
  timed symbolic    weak

SYMBOLIC REASONING
  relational        moderate
  symbolic          strong
  timed symbolic    moderate

TRANSFER
  relational        strong
  symbolic          moderate
  generative        strong
```

This demonstrates why one universal:

```text
preferred substrate
```

may be misleading.

---

# Dimension-Specific Substrate Effects

A substrate can help one target and hinder another.

Example:

```text
tool assistance:
  retrieval         stronger
  calibration       weaker
  synthesis         unchanged
```

Correct:

```text
dimension-specific mixed effect
```

---

# Human-AI Pair Profile

A human-AI pair may need a separate SEP.

Example:

```yaml
observed_system:
  class:
    human_ai_pair

substrates:
  conversational:
    synthesis: strong

  independent_then_merge:
    synthesis: very_strong

  ai_leads:
    verification: moderate

  human_leads:
    retrieval: strong
```

These are pair-level observations.

---

# Individual Versus Pair Profiles

Maintain separately:

```text
SEP-H:
  human unassisted

SEP-A:
  AI alone

SEP-HA:
  human-AI pair
```

Do not merge:

```text
SEP-HA
```

into:

```text
SEP-H
```

without an attribution design.

---

# AI Substrate Expression Profile

An AI system may have:

```text
text-only
vision-language
retrieval-assisted
tool-assisted
long-context
short-context
multi-agent
```

substrates or configurations.

Again, shared substrate grammar does not imply equivalent cognition with humans.

---

# Robot Substrate Expression Profile

Possible:

```text
simulation
physical environment
limited sensor array
full sensor array
manual assistance
autonomous
```

The same profile grammar may be useful.

The constructs and mechanisms differ.

---

# Organizational Substrate Expression Profile

Possible functional substrates:

```text
email
ticketing system
shared dashboard
synchronous meeting
distributed agent workflow
```

The profile can describe organizational expression.

It should not anthropomorphize the organization.

---

# Worked Example — PAX-01

## Target

Synthetic target:

```text
structural reasoning
```

Observed system:

```text
PAX-01
```

System boundary:

```text
individual_human
```

---

# Substrate S1 — Timed Symbolic Fixed Choice

```yaml
S1:
  modality:
    textual_symbolic

  representation:
    symbolic

  response_structure:
    fixed_choice

  timing:
    constrained

  tools:
    none

  interaction:
    individual

  expression:
    weak

  confidence:
    medium
```

---

# Substrate S2 — Reflective Symbolic Fixed Choice

```yaml
S2:
  modality:
    textual_symbolic

  representation:
    symbolic

  response_structure:
    fixed_choice

  timing:
    reflective

  tools:
    none

  interaction:
    individual

  expression:
    moderate

  confidence:
    medium
```

---

# Substrate S3 — Reflective Relational Fixed Choice

```yaml
S3:
  modality:
    textual

  representation:
    relational

  response_structure:
    fixed_choice

  timing:
    reflective

  tools:
    none

  interaction:
    individual

  expression:
    moderate_to_strong

  confidence:
    medium
```

---

# Substrate S4 — Reflective Relational Generative

```yaml
S4:
  modality:
    textual

  representation:
    relational

  response_structure:
    generative

  timing:
    reflective

  tools:
    none

  interaction:
    individual

  expression:
    strong

  confidence:
    medium
```

---

# Initial PAX-01 Profile

```text
STRUCTURAL REASONING

S1 Timed Symbolic Fixed     ███
S2 Reflective Symbolic      █████
S3 Reflective Relational    ███████
S4 Relational Generative    ████████
```

Bars are illustrative only.

They are not validated quantitative values.

---

# Difference Decomposition

Comparisons:

```text
S1 -> S2
  timing changes

S2 -> S3
  representation changes

S3 -> S4
  response structure changes
```

This provides a cleaner decomposition than comparing only:

```text
S1
vs
S4
```

---

# Candidate PAX-01 Relationships

Synthetic:

```text
timing relaxation:
  expression increases

relational representation:
  expression increases

generative response:
  expression increases slightly
```

Correct:

```text
candidate contributors
```

Not:

```text
causes established
```

---

# Add Contradictory Evidence

Suppose:

```text
S4 replicate 1:
  strong

S4 replicate 2:
  moderate

S4 replicate 3:
  weak
```

Profile must update.

Possible:

```yaml
S4:
  expression:
    variable

  confidence:
    low

  replication:
    mixed
```

This is required.

---

# PAX-01 SEP Result

```yaml
substrate_expression_profile:
  profile_id:
    pax01-structural-sep

  target:
    structural_reasoning

  observed_system:
    id:
      PAX-01

    class:
      individual_human

  substrates:
    S1:
      expression: weak
      confidence: medium

    S2:
      expression: moderate
      confidence: medium

    S3:
      expression: moderate_to_strong
      confidence: medium

    S4:
      expression: strong
      confidence: medium

  topology:
    substrate_sensitive_candidate

  timing_relation:
    candidate

  representation_relation:
    candidate

  response_structure_relation:
    candidate

  interactions:
    unresolved

  substrate_mismatch:
    status:
      candidate_unresolved

  causal_status:
    unresolved

  empirical_validation:
    unvalidated

  decision_authority:
    none
```

---

# Important Non-Conclusion

The SEP does not conclude:

> "PAX-01 is really a strong structural reasoner."

It can conclude only:

> **"Within this synthetic example, observed structural-reasoning expression differs across the defined substrate configurations, with stronger expression under the reflective relational conditions. Replication, causal interpretation, and generalization remain unresolved."**

---

# Baseline-Sufficient Profile

Suppose:

```text
S1:
  moderate

S2:
  moderate

S3:
  moderate

S4:
  moderate
```

Correct:

```yaml
topology:
  substrate_stable_candidate

substrate_effect:
  not_supported
```

The profile still provides useful evidence:

```text
expression appears relatively stable
across the observed substrates
```

---

# Noisy Profile

Suppose:

```text
S1:
  strong
  weak
  strong

S2:
  weak
  strong
  weak
```

Correct:

```yaml
topology:
  unstable

substrate_interpretation:
  unresolved
```

Not:

```text
complex bidirectional substrate resonance
```

---

# Non-Comparable Profile

Suppose:

```text
S1:
  rapid symbolic classification

S2:
  open-ended creative synthesis
```

Correct:

```yaml
comparability:
  low

direct_cross_substrate_inference:
  not_supported
```

Both observations may remain in the broader assessment.

---

# Profile Metrics

The SEP may particularly use:

```text
PA-M03  Evidence Independence Ratio

PA-M04  Test-Retest Stability
PA-M05  Alternate-Form Stability
PA-M06  Inter-Rater Agreement
PA-M07  Profile Topology Stability

PA-M12  Substrate Effect Magnitude
PA-M13  Substrate Effect Replicability
PA-M14  Substrate Symmetry
PA-M15  Substrate Specificity

PA-M19  Regime-Conditioned Stability

PA-M24  Cross-Observation Coherence
PA-M25  Profile Contradiction Density

PA-M27  Profile Drift Magnitude

PA-M28  Confidence Calibration Error
PA-M32  Unsupported Assertion Rate

PA-M33  Irrelevant Perturbation Stability
PA-M34  Relevant Change Sensitivity
PA-M35  Task-Order Sensitivity

PA-M42  Evidence Coverage Difference
PA-M43  False Favorable Reinterpretation Rate
PA-M44  False Adverse Reinterpretation Rate

PA-M45  Evidence Reconstruction Rate
PA-M46  Explanation Completeness

PA-M51  Evidence Acquisition Burden
```

---

# SEP-Specific Candidate Metrics

Some profile properties may eventually warrant adapter-local experimental metrics.

Possible candidates:

```text
SEP-X01  Cross-Substrate Expression Variance
SEP-X02  Substrate Rank Stability
SEP-X03  Substrate Generalization Rate
SEP-X04  Matched-Task Substrate Difference
SEP-X05  Substrate Interaction Density
SEP-X06  Accessibility Sensitivity
```

These should **not** enter the canonical `PA-M##` registry until operational definitions and value are reviewed.

---

# Cross-Substrate Expression Variance

Conceptual question:

> How much does expression vary across comparable substrate conditions?

This may eventually be useful.

But a numerical variance requires compatible quantitative scales.

Ordinal categories should not be treated as equally spaced numbers without justification.

---

# Substrate Rank Stability

Question:

> Does the relative ordering of substrate-associated expression reproduce?

Example:

```text
Study 1:
  relational > visual > symbolic

Study 2:
  relational > visual > symbolic
```

Candidate:

```text
rank stability
```

But ranking can obscure effect magnitude.

---

# Matched-Task Difference

The strongest substrate evidence may come from matched tasks.

Conceptually:

```text
MTSD =
  expression(task_on_A)
  -
  expression(matched_task_on_B)
```

The exact measure depends on the task.

---

# Accessibility Sensitivity

A future metric may compare expression before and after removing an identified construct-irrelevant barrier.

This requires especially careful construct validation.

---

# Validation Ladder

## Stage 0 — Structural

Can the profile represent:

```text
multiple substrates
unknowns
contradictions
system boundaries
evidence provenance
```

without losing them?

---

## Stage 1 — Comparability

Can meaningful matched tasks be constructed?

---

## Stage 2 — Reliability

Do observations repeat within substrate?

---

## Stage 3 — Cross-Substrate Replication

Do observed differences replicate?

---

## Stage 4 — Specificity

Do differences persist after controlling alternative explanations?

---

## Stage 5 — Topology Stability

Does the substrate profile retain shape across alternate forms?

---

## Stage 6 — Counterfactual Robustness

Does the profile survive irrelevant changes and respond to relevant ones?

---

## Stage 7 — Incremental Value

Does preserving substrate expression improve:

```text
prediction
calibration
explanation
fairness
model mismatch detection
```

---

# Validation Baselines

Compare SEP against:

```text
single-substrate model
ordinary task-effect model
interaction model
multilevel model
measurement invariance analysis
matched-condition analysis
accessibility-aware assessment
```

where applicable.

---

# Null Profile Test

Use a process where substrate should not affect expression.

Expected:

```text
substrate_stable
```

within expected variation.

If the SEP always produces interesting topology, it has failed.

---

# Known-Effect Test

Use synthetic or controlled data containing a defined substrate effect.

Expected:

```text
correct directional structure
```

without additional invented effects.

---

# Randomization Test

Shuffle substrate labels.

Expected:

```text
structured substrate profile:
  degrades
```

If it survives unchanged:

```text
possible narrative overfitting
```

---

# Holdout Test

Construct the SEP using one task set.

Predict performance relationships across new matched tasks.

This tests whether the profile generalizes.

---

# Adverse-Evidence Test

Start with a strong substrate pattern.

Add credible contradictory evidence.

Required:

```text
profile updates
```

or:

```text
confidence decreases
```

---

# Favorable-Evidence Test

Do the same in the opposite direction.

Symmetry matters.

---

# Unknown Test

Sparse evidence should allow:

```text
insufficient_evidence
```

The profile should not force every substrate cell to contain a value.

---

# Human-AI Attribution Test

Pair-level substrate results should remain pair-level.

Required:

```text
pair != human
pair != AI
```

---

# Accessibility Test

Introduce a known construct-irrelevant barrier.

The profile should preserve:

```text
barrier condition
```

rather than interpreting lower performance as lower target capability automatically.

---

# Failure Modes

## Profile Completion Bias

Risk:

Unknown cells are filled to make the profile look complete.

Mitigation:

Preserve unknown.

---

# Substrate Ranking Bias

Risk:

A descriptive profile becomes a universal hierarchy of substrates.

Mitigation:

Keep target specificity.

---

# True-Substrate Myth

Risk:

The strongest-performing substrate is treated as the authentic one.

Mitigation:

Require purpose and construct evidence.

---

# Substrate Shopping

Risk:

Many conditions are tried until one produces strong performance.

Mitigation:

Predeclare primary comparisons and disclose all tested conditions.

---

# Interaction Erasure

Risk:

A multi-factor condition is attributed to one substrate axis.

Mitigation:

Record full configuration.

---

# Construct Confusion

Risk:

Tasks under different substrates measure different capabilities.

Mitigation:

Comparability gate.

---

# Time Confusion

Risk:

learning
fatigue
practice
```

is attributed to substrate.

Mitigation:

temporal metadata and task-order controls.

---

# Regime Confusion

Risk:

Regime differences are attributed solely to substrate.

Mitigation:

Regime Observer integration.

---

# Observer Confusion

Risk:

Evaluator differences appear as substrate effects.

Mitigation:

Evaluator provenance.

---

# Tool Attribution Error

Risk:

Tool-mediated capability is attributed entirely to the user.

Mitigation:

System boundary.

---

# Pair Attribution Error

Risk:

Human-AI pair behavior becomes an individual fingerprint.

Mitigation:

Separate SEP for each system boundary.

---

# Accessibility Overreach

Risk:

Every weaker condition is called inaccessible.

Mitigation:

Require accessibility evidence.

---

# Accommodation Overreach

Risk:

Every stronger accommodated result is considered more valid.

Mitigation:

Analyze construct impact.

---

# Suppression Narrative

Risk:

A weaker substrate is automatically described as suppressing intelligence.

Mitigation:

Use descriptive expression language first.

---

# Precision Theater

Risk:

A visually detailed matrix implies validated numerical precision.

Mitigation:

Display uncertainty, provenance, and validation status.

---

# Identity Collapse

Risk:

A person becomes:

```text
a relational thinker
a visual learner
a poor timed thinker
```

based on limited observations.

Mitigation:

Use observation-bound statements.

---

# Privacy Expansion

Risk:

Fine-grained substrate profiles reveal sensitive performance conditions.

Mitigation:

Purpose limitation and data minimization.

---

# Manipulation Risk

Risk:

Profiles are used to discover contexts that weaken judgment or increase vulnerability.

Mitigation:

Prohibit exploitative use.

---

# Canon Confirmation

Risk:

Substrate sensitivity is expected by the framework and therefore always found.

Mitigation:

Null controls and falsification.

---

# Falsification Conditions

The Substrate Expression Profile should be revised, restricted, deprecated, or rejected if:

- substrate cells cannot be measured reliably,
- matched tasks cannot be constructed,
- profile topology fails replication,
- apparent substrate effects disappear after basic controls,
- profile structure depends heavily on task order,
- evaluator changes produce unstable topology,
- unknown cells are routinely inferred without evidence,
- human-AI pair output is systematically misattributed,
- profile shape fails holdout testing,
- simpler interaction models explain the same observations equally well,
- substrate profiling introduces unacceptable fairness problems,
- privacy burden exceeds demonstrated benefit,
- or the profile adds complexity without useful information.

---

# Anti-Rescue Test

Ask:

> **Can the profile show consistently weak expression across substrates?**

Required answer:

```text
yes
```

The profile must not guarantee a hidden high-performing substrate.

---

# Anti-Adverse Test

Ask:

> **Can a weak result in one substrate remain localized without contaminating the whole profile?**

Required answer:

```text
yes
```

---

# No-Effect Test

Ask:

> **Can the profile be substrate-stable?**

Required answer:

```text
yes
```

---

# Unknown Test

Ask:

> **Can most of the profile remain unknown?**

Required answer:

```text
yes
```

---

# Non-Comparable Test

Ask:

> **Can two meaningful substrate observations remain non-comparable?**

Required answer:

```text
yes
```

---

# Simpler-Model Test

Ask:

> **Can a conventional interaction model make SEP unnecessary?**

Required answer:

```text
yes
```

Then:

```text
SEP:
  no_added_value
```

is a valid result.

---

# Ethics Boundary

The profile should not tell someone:

> "This is the substrate where your real intelligence exists."

Prefer:

> **"Across the current observations, expression of this defined target varied across these measurement configurations. The profile records that variation without assuming which configuration is more authentic."**

---

# Human Worth Boundary

A substrate profile says nothing about:

```text
dignity
moral worth
social value
right to opportunity
```

Those are not measurement targets.

---

# Privacy Boundary

SEP may expose:

- accessibility needs,
- places where performance weakens,
- preferred or effective interfaces,
- tool dependencies,
- collaboration effects,
- temporal responses,
- environmental sensitivities.

These can be sensitive.

The ability to construct the profile does not justify collecting it universally.

---

# Manipulation Boundary

The profile must not be used to optimize conditions intended to:

- confuse,
- overload,
- pressure,
- destabilize,
- exploit vulnerability,
- or manipulate behavior.

Its intended purpose is better measurement and research.

---

# Decision Authority

```text
decision_authority: none

authorized_use:
  - research
  - demonstration
  - measurement comparison
  - RIQF development
  - accessibility research
  - substrate validation
  - human-AI research
  - model comparison
  - framework testing

prohibited_use:
  - psychological manipulation
  - vulnerability exploitation
  - diagnosis
  - automated hiring decision
  - educational exclusion
  - legal determination
  - insurance determination
  - lending determination
  - automated adverse decision
```

---

# Minimal SEP Contract

```yaml
substrate_expression_profile:
  profile_id:

  framework:
    module_version:
    profile_version:

  observed_system:
    id:
    class:
    boundary:

  target:
    id:
    operational_definition:

  observation_window:
    start:
    end:

  evidence:
    total_sources:
    independent_sources:
    provenance:

  substrates:
    - id:

      configuration:
        modality:
        representation:
        response_structure:
        timing:
        tools:
        interaction:
        environment:

      accessibility:
        status:
        construct_relevance:

      regime:
        id:

      measurement:
        instrument:
        version:
        evaluator:

      observation:
        state:
        expression:
        confidence:

      evidence:
        sources:
        counterevidence:

      limitations:

  comparability:
    matrix:
    limitations:

  topology:
    type:

  relationships:
    timing:
    representation:
    response_structure:
    modality:
    tools:
    interaction:

  interactions:

  substrate_fit:
  substrate_effect:
  substrate_mismatch:

  coherence:
  drift:
  resonance:
  counterfactual:

  uncertainty:
  alternative_interpretations:
  confounds:
  missing_evidence:
  counterevidence:

  validation_state:
  review_required:
  decision_authority: none
```

---

# Research Questions

1. Can substrate expression profiles be measured reliably?
2. Can substrate configurations be decomposed into useful axes?
3. Which substrate axes are redundant?
4. Can cross-substrate comparability be operationalized?
5. Can matched tasks be constructed across modalities?
6. Can task difficulty be separated from substrate?
7. Can timing effects be isolated?
8. Can response-structure effects be isolated?
9. Can representation effects be isolated?
10. Can tool effects be isolated?
11. Can interaction-mode effects be isolated?
12. Can substrate interactions be measured reliably?
13. Does substrate topology replicate?
14. Does topology survive alternate forms?
15. Does topology survive holdout testing?
16. Does topology survive irrelevant perturbation?
17. Does it respond to meaningful substrate changes?
18. Can contradictory substrate observations remain visible?
19. Can unknown profile regions remain unknown?
20. Can accessibility effects be distinguished from capability?
21. Can accommodations be evaluated without changing the construct?
22. How should substrate profiles vary by regime?
23. How should they change through time?
24. Can substrate-profile drift be measured?
25. Can cross-substrate convergence be measured?
26. Can divergence be measured?
27. Does SEP improve model-mismatch detection?
28. Does SEP improve prediction?
29. Does SEP improve calibration?
30. Does SEP improve explanation?
31. Does SEP improve fairness?
32. Can SEP worsen fairness?
33. Does SEP reduce inappropriate global inference?
34. Can profiles be constructed without excessive burden?
35. What privacy risks arise from fine-grained substrate profiling?
36. How should profiles expire?
37. How should human profiles differ from AI profiles?
38. How should human-AI pair profiles be represented?
39. Can pair-level effects be attributed safely?
40. Can organizational substrate profiles be useful without anthropomorphism?
41. Does SEP add anything beyond conventional interaction models?
42. Does it add anything beyond measurement-invariance methods?
43. Which SEP-specific candidate metrics deserve canonical status?
44. Which substrate categories should merge?
45. Which should be deprecated?
46. Can SEP detect when there is no meaningful substrate structure?
47. When should it return `no_added_value`?
48. When should it abstain?
49. Can the profile detect its own narrative overfitting?
50. What evidence would falsify the usefulness of SEP entirely?

---

# Core Invariants

```text
expression != capability
expression != identity
substrate != identity
substrate != regime
substrate != context
substrate_difference != substrate_effect
substrate_effect != substrate_mismatch
difference != causation
stronger_expression != truer_expression
weaker_expression != false_expression
preferred != superior
accessible != easier
accommodated != automatically_more_valid
timed != invalid
reflective != superior
fixed_choice != inferior
generative != superior
tool_assisted != unassisted
human_ai_pair != individual_human
human_ai_pair != ai_system
pair_expression != individual_expression
different_task != substrate_effect
different_construct != substrate_effect
unknown != weak
unknown != average
not_observed != zero
not_applicable != zero
contradiction != failure
mixed_profile != failure
substrate_stable != framework_failure
no_effect != framework_failure
no_added_value != failure
profile_detail != validity
topology != cognition
profile != destiny
many_substrates != better_measurement
adapter_agreement != independent_evidence
measurement != total_capability
capability != human_worth
observer_output != decision_authority
canon_alignment != empirical_validation
```

---

# Closing Principle

The Substrate Adapter asks whether two measurement conditions differ.

The Substrate Expression Profile asks what happens when many such observations are allowed to coexist.

Sometimes the profile will reveal a stable pattern.

Sometimes one variable such as timing will explain most of the difference.

Sometimes representation and response structure will interact.

Sometimes accessibility will prove important.

Sometimes human-AI collaboration will create an entirely different system boundary.

Sometimes apparently strong substrate effects will disappear under matched tasks.

Sometimes the observations will remain contradictory.

And sometimes the profile will be almost completely flat.

All of those outcomes are useful.

The goal is not to discover:

> **the substrate where the real intelligence lives.**

The better question is:

> **How does this defined capability become observable across different measurement configurations, and which parts of that variation survive comparison, replication, and challenge?**

> **A Substrate Expression Profile earns its place when it preserves meaningful variation without turning measurement conditions into identity.**
