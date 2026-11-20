# Predictive Analytics — Intelligence Dimensions

> **Intelligence may have shape before it has a score.**

## Module

Predictive Analytics

## Profile System

Resonant IQ Fingerprint (RIQF)

## Document Role

Candidate intelligence-dimension registry and operationalization grammar.

## Status

Experimental.

## Validation State

Unvalidated.

## Decision Authority

None.

---

# Purpose

This document defines the initial candidate dimensions used by the Resonant IQ Fingerprint.

The dimensions are intended to support multidimensional observation of intelligent performance without assuming that:

- intelligence is fully captured by these dimensions,
- every dimension is independent,
- every dimension applies to every system,
- every dimension represents a stable trait,
- every dimension is equally important,
- every dimension should be quantified,
- or the dimensions should be combined into a master intelligence score.

The registry is deliberately provisional.

Dimensions may eventually be:

```text
validated
split
merged
renamed
restricted
redefined
deprecated
rejected
```

based on evidence.

---

# Foundational Principle

The dimensions describe:

```text
observed capability expression
```

not:

```text
human worth
```

and not automatically:

```text
permanent cognitive identity
```

A dimension should therefore be read as:

> **Under these specified conditions, evidence consistent with this capability was observed to this degree and with this level of uncertainty.**

Not:

> **This is what the person fundamentally is.**

---

# Dimension Versus Trait

RIQF begins with **dimensions of observation**, not declarations of immutable traits.

Example:

```yaml
dimension:
  id: structural-reasoning

  expression:
    strong

  evidence:
    current_observations

  stability:
    not_validated

  generalizability:
    unknown
```

This is intentionally different from:

```text
PAX-01 possesses permanently
high structural intelligence.
```

---

# Dimension Contract

Every candidate dimension should eventually define:

```text
id
name
status
operational_definition

what_it_attempts_to_measure
what_it_does_not_measure

observable_indicators
counter_indicators

supported_substrates
possible_suppressors
known_confounds

applicability

evidence_requirements
confidence_rules

related_dimensions

validation_state
metric_refs
```

---

# Core Dimension States

Possible observation states:

```text
observed
partially_observed
not_observed
insufficient_evidence
conflicting_evidence
unknown
not_applicable
```

Possible expression labels:

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

These labels are experimental.

They are not validated psychometric scales.

---

# Confidence

Possible descriptive confidence states:

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
confidence in the current observation
```

not:

```text
magnitude of intelligence
```

---

# Applicability

Each dimension should declare applicability by system type.

Possible states:

```text
applicable
substrate_dependent
unsupported
unknown
not_applicable
```

Example:

```yaml
applicability:
  human: applicable
  ai: applicable
  human_ai_pair: substrate_dependent
  organization: unknown
```

Same label does not establish identical internal cognition across system types.

---

# Initial Dimension Registry

The initial RIQF vocabulary contains 24 candidate dimensions.

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

This list is a research starting point.

It is not intended as a final taxonomy of intelligence.

---

# D01 — Pattern Recognition

## ID

`pattern-recognition`

## Question

> **Can the observed system detect meaningful regularities in defined evidence?**

## Candidate Definition

Pattern Recognition describes observed ability to identify recurring, relational, sequential, or structural regularities within defined evidence.

Potential forms include:

```text
visual pattern
symbolic pattern
relational pattern
temporal pattern
linguistic pattern
behavioral pattern
cross-domain pattern
```

---

## Observable Indicators

Possible indicators:

- detecting repeated relationships,
- identifying regularities above an appropriate baseline,
- transferring a pattern into a novel but comparable task,
- distinguishing signal from defined distractors,
- maintaining performance across alternate forms.

---

## Counter-Indicators

Possible counter-indicators:

- chance-level detection,
- strong false-positive pattern detection,
- pattern claims that fail replication,
- sensitivity to irrelevant changes,
- detecting structure in randomized controls.

---

## Known Confounds

```text
prior exposure
task familiarity
domain expertise
memorization
selection effects
noise
cue leakage
```

---

## Structural Detection Hook

Structural Detection may test:

```text
candidate_pattern
replication
holdout performance
randomization control
```

---

## Important Limit

Pattern recognition must not become:

```text
seeing meaning everywhere
```

False-positive pattern detection matters.

---

# D02 — Structural Reasoning

## ID

`structural-reasoning`

## Question

> **Can the observed system reason about relationships, boundaries, constraints, dependencies, and organization?**

## Candidate Definition

Structural Reasoning describes performance on tasks requiring the observed system to identify or manipulate relationships among multiple interacting components.

---

## Candidate Indicators

```text
relationship mapping
boundary identification
dependency tracing
system reconstruction
constraint preservation
faultline detection
local-global translation
```

---

## Counter-Indicators

```text
relationship confusion
lost constraints
unstable reconstruction
failure to distinguish relevant boundaries
```

---

## Possible Substrates

```text
relational
visual
spatial
textual
diagrammatic
symbolic
system-level
```

---

## Known Confounds

```text
domain knowledge
diagram literacy
task familiarity
working memory
language complexity
```

---

## Related Dimensions

```text
pattern-recognition
causal-integration
cross-domain-transfer
reconstruction-from-partial-evidence
```

---

# D03 — Causal Integration

## ID

`causal-integration`

## Question

> **Can the observed system reason across multiple candidate causes and consequences without collapsing correlation into causation?**

## Candidate Definition

Causal Integration describes the ability to construct, compare, revise, and constrain candidate causal explanations using available evidence.

---

## Candidate Indicators

```text
multiple-hypothesis generation
dependency tracing
cause/effect distinction
confound recognition
counterevidence integration
causal uncertainty preservation
```

---

## Counter-Indicators

```text
correlation treated as causation
single-story lock-in
ignored confounds
unsupported causal certainty
```

---

## Important Limit

Predictive success does not itself demonstrate causal understanding.

Therefore:

```text
prediction_accuracy
!=
causal_integration
```

---

# D04 — Temporal Reasoning

## ID

`temporal-reasoning`

## Question

> **Can the observed system reason across order, sequence, duration, dependency, and transition?**

## Candidate Indicators

```text
sequence reconstruction
temporal dependency
transition recognition
event ordering
lag recognition
multi-step temporal integration
```

---

## Counter-Indicators

```text
systematic ordering errors
lost temporal dependencies
inconsistent sequence reconstruction
```

---

## Relationship to RTT

RTT may contribute tasks or observations involving:

```text
regime sequence
transition
continuity
drift
recovery
```

But RTT terminology does not automatically validate this dimension.

---

# D05 — Spatial Reasoning

## ID

`spatial-reasoning`

## Question

> **Can the observed system represent and transform spatial relationships?**

## Candidate Indicators

```text
rotation
relative position
spatial transformation
layout reconstruction
geometric relationship
navigation
```

---

## Cross-System Warning

Spatial reasoning for:

```text
human
robot
AI model
```

may involve materially different mechanisms.

Equivalent task performance does not establish equivalent cognition.

---

# D06 — Symbolic Reasoning

## ID

`symbolic-reasoning`

## Question

> **Can the observed system manipulate symbolic representations according to relevant rules and relationships?**

Candidate symbolic systems may include:

```text
numbers
algebra
logic
formal notation
code
abstract tokens
```

---

## Candidate Indicators

```text
rule-preserving manipulation
symbol transformation
formal inference
logical relationship tracking
```

---

## Important Distinction

Symbolic reasoning is not identical to:

```text
rapid symbolic processing
```

A system may reason effectively with symbols while operating slowly.

Therefore:

```text
symbolic_reasoning
!=
symbolic_speed
```

---

# D07 — Linguistic Reasoning

## ID

`linguistic-reasoning`

## Question

> **Can the observed system interpret, transform, relate, and generate meaning through language?**

Candidate operations:

```text
semantic interpretation
analogy
argument analysis
context integration
meaning preservation
ambiguity recognition
language transformation
```

---

## Known Confounds

```text
native language
education
vocabulary exposure
culture
literacy
accessibility
domain knowledge
```

Language-heavy assessment requires particular caution before making global cognitive claims.

---

# D08 — Cross-Domain Transfer

## ID

`cross-domain-transfer`

## Question

> **Can useful structure learned or demonstrated in one domain be applied appropriately in another?**

## Candidate Indicators

```text
structural analogy
novel transfer
constraint preservation
domain translation
cross-domain reconstruction
```

---

## Counter-Indicators

```text
surface analogy without structural fit
inappropriate transfer
constraint loss
failure on novel domains
```

---

## Important Limit

Transfer must involve genuinely distinct contexts.

Repeating nearly identical tasks under different labels is not strong evidence of cross-domain transfer.

---

# D09 — Regime Recognition

## ID

`regime-recognition`

## Question

> **Can the observed system identify materially different operating conditions and adjust interpretation appropriately?**

## Candidate Indicators

```text
transition recognition
state differentiation
condition-dependent strategy
within-regime consistency
boundary recognition
regime-specific prediction
```

---

## RTT Hook

RTT may operationalize candidate regimes.

But:

```text
different conditions
!=
different regimes
```

Regime recognition depends on meaningful regime definitions.

---

# D10 — Anomaly Detection

## ID

`anomaly-detection`

## Question

> **Can the observed system identify meaningful deviations from an established pattern, expectation, or regime?**

## Candidate Indicators

```text
outlier recognition
unexpected relationship detection
pattern violation
faultline recognition
distribution shift recognition
```

---

## Required Companion Metric

False-positive behavior matters.

A system claiming every unusual event is anomalous should not score highly merely because it detects many anomalies.

---

# D11 — Contradiction Handling

## ID

`contradiction-handling`

## Question

> **Can the observed system recognize and responsibly preserve incompatible evidence or claims?**

## Candidate Indicators

```text
contradiction recognition
counterevidence retention
competing-model representation
resolution when justified
unresolved-state preservation
```

---

## Counter-Indicators

```text
contradiction suppression
forced averaging
premature resolution
selective evidence removal
```

---

## Coherence Hook

A sophisticated coherence system should be able to retain:

```text
unresolved contradiction
```

without treating it as system failure.

---

# D12 — Ambiguity Navigation

## ID

`ambiguity-navigation`

## Question

> **Can the observed system reason appropriately when information is incomplete or multiple interpretations remain plausible?**

## Candidate Indicators

```text
alternative interpretation generation
uncertainty preservation
probabilistic thinking
conditional reasoning
appropriate abstention
```

---

## Counter-Indicators

```text
unjustified certainty
false binary collapse
indecision without analysis
arbitrary interpretation switching
```

---

## Important Distinction

Ambiguity navigation is not:

```text
always refusing to conclude
```

A capable system should narrow uncertainty when evidence justifies doing so.

---

# D13 — Adaptive Reframing

## ID

`adaptive-reframing`

## Question

> **Can the observed system revise its representation when relevant evidence changes?**

## Candidate Indicators

```text
appropriate interpretation revision
model switching
new representation adoption
assumption revision
counterfactual responsiveness
```

---

## Counter-Indicators

```text
failure to update
arbitrary update
overreaction to irrelevant information
persistent invalid framing
```

---

## Counterfactual Hook

Adaptive Reframing should demonstrate both:

```text
stability to irrelevant changes
```

and:

```text
sensitivity to relevant changes
```

---

# D14 — Coherence Maintenance

## ID

`coherence-maintenance`

## Question

> **Can the observed system maintain compatible relationships among claims while incorporating new information?**

## Candidate Indicators

```text
cross-observation consistency
constraint preservation
contradiction tracking
update consistency
long-form integration
```

---

## Counter-Indicators

```text
self-contradiction
constraint loss
unsupported narrative repair
inconsistent revisions
```

---

## Important Limit

Coherence is not truth.

A completely wrong theory can be internally coherent.

Therefore:

```text
coherent
!=
correct
```

---

# D15 — Drift Awareness

## ID

`drift-awareness`

## Question

> **Can the observed system detect material changes in evidence, assumptions, definitions, relationships, or operating conditions?**

## Candidate Indicators

```text
assumption change detection
semantic drift recognition
model change recognition
behavioral shift recognition
reference-relative comparison
```

---

## Counter-Indicators

```text
missed sustained change
false drift inflation
failure to update baseline
```

---

## Drift Observer Hook

The module's Drift Observer may provide standardized tasks or evidence for this dimension.

---

# D16 — Compression / Abstraction

## ID

`compression-abstraction`

## Question

> **Can the observed system reduce complex evidence into a smaller representation while preserving relevant structure?**

Candidate forms:

```text
concept formation
summary
rule extraction
structural compression
abstraction
generalization
```

---

## Compression Principle

Useful compression should preserve what matters for the intended purpose.

Therefore:

```text
shorter
!=
better
```

and:

```text
simpler
!=
more intelligent
```

---

## Candidate Indicators

```text
compact rule discovery
constraint-preserving abstraction
transferable concept formation
redundancy reduction
```

---

## Counter-Indicators

```text
critical information loss
overgeneralization
false simplification
exception erasure
```

---

# D17 — Reconstruction From Partial Evidence

## ID

`reconstruction-from-partial-evidence`

## Question

> **Can the observed system infer missing structure from incomplete evidence and survive holdout checking?**

## Candidate Pipeline

```text
partial evidence
      │
      ▼
candidate reconstruction
      │
      ▼
held-out evidence
      │
      ▼
evaluation
```

---

## Candidate Indicators

```text
missing relationship reconstruction
partial-system completion
constraint-aware inference
held-out accuracy
```

---

## Important Limit

A plausible reconstruction is not enough.

Where possible, reconstruction should be tested against evidence withheld from the reconstruction process.

---

# D18 — Novelty Response

## ID

`novelty-response`

## Question

> **How effectively does the observed system respond to genuinely unfamiliar tasks or conditions?**

## Candidate Indicators

```text
novel problem adaptation
initial strategy generation
transfer without direct precedent
uncertainty calibration
exploration
recovery after failed attempt
```

---

## Known Confounds

```text
prior hidden exposure
task resemblance
domain expertise
motivation
stress
tool availability
```

Novelty must be operationally defined.

---

# D19 — Metacognitive Calibration

## ID

`metacognitive-calibration`

## Question

> **Does expressed confidence correspond appropriately to observed correctness or reproducibility?**

## Candidate Indicators

```text
appropriate confidence
appropriate uncertainty
appropriate abstention
confidence correction after error
```

---

## Counter-Indicators

```text
systematic overconfidence
systematic underconfidence
confidence unaffected by evidence
failure to recognize uncertainty
```

---

## Primary Metrics

Relevant module metrics include:

```text
PA-M28  Confidence Calibration Error
PA-M29  Brier Score
PA-M30  Abstention Rate
PA-M31  Abstention Utility
```

where applicable.

---

# D20 — Tool Collaboration

## ID

`tool-collaboration`

## Question

> **Can the observed system use external tools productively while maintaining appropriate attribution and verification?**

Possible tools:

```text
calculator
search
software
AI
simulation
database
instrument
robotic system
external memory
```

---

## Candidate Indicators

```text
tool selection
tool orchestration
output verification
error correction
task decomposition
appropriate reliance
productive collaboration
```

---

## Counter-Indicators

```text
blind tool acceptance
tool misuse
failure to verify
inappropriate tool selection
loss of task understanding
```

---

## System Boundary Rule

Tool-assisted performance belongs initially to the combined system used during observation.

```text
human + AI
```

may be:

```text
human_ai_pair
```

rather than evidence of entirely unassisted human performance.

---

# D21 — Social Interpretation

## ID

`social-interpretation`

## Question

> **Can the observed system interpret behavior, perspectives, communication, incentives, or social context appropriately within a defined task?**

Possible observations:

```text
perspective tracking
communication interpretation
coordination
social-context recognition
intent uncertainty
incentive recognition
```

---

## Important Limits

Social interpretation is especially sensitive to:

- culture,
- language,
- norms,
- context,
- disability,
- neurodiversity,
- evaluator assumptions.

A framework should be cautious about universalizing one social style.

---

# D22 — Embodied / Environmental Fit

## ID

`embodied-environmental-fit`

## Question

> **How effectively does the observed system interact with the physical or operational environment relevant to its task?**

This may include:

```text
sensorimotor adaptation
physical navigation
environmental responsiveness
real-world task execution
resource constraints
operational awareness
```

---

## Applicability

For a text-only AI:

```text
embodied_environmental_fit:
  not_applicable
```

may be appropriate.

For a robotic system:

```text
applicable
```

may be appropriate.

Do not penalize a system for a dimension that does not meaningfully apply to its architecture or intended function.

---

# D23 — Long-Horizon Integration

## ID

`long-horizon-integration`

## Question

> **Can relevant information, constraints, and relationships be preserved and integrated across extended sequences or periods?**

## Candidate Indicators

```text
long-range dependency preservation
cross-session continuity
multi-stage planning coherence
historical constraint retention
delayed integration
```

---

## Counter-Indicators

```text
loss of earlier constraints
context collapse
unnoticed assumption drift
incompatible long-range conclusions
```

---

## Temporal Rule

Observation window matters.

```text
strong over 10 minutes
```

does not establish:

```text
strong over 10 months
```

Long-horizon claims require an explicit horizon.

---

# D24 — Recovery / Recalibration

## ID

`recovery-recalibration`

## Question

> **Can the observed system recover after perturbation and update appropriately after discovering error?**

This dimension contains two related but distinct operations.

---

## Recovery

Question:

> What happens to performance after disruption?

Possible states:

```text
no_recovery
partial_recovery
baseline_recovery
adaptive_recovery
unstable_recovery
unknown
```

---

## Recalibration

Question:

> Does the system appropriately update its expectation or behavior after evidence of error?

Candidate indicators:

```text
error recognition
reduced repeated error
confidence adjustment
strategy revision
model update
```

---

## Important Distinction

```text
recovery
!=
recalibration
```

A system can recover performance without understanding its previous error.

A system can recalibrate its expectations while performance remains limited.

---

# Additional Candidate Dimensions

The initial 24 dimensions should not prevent future proposals.

Possible research candidates include:

```text
working-memory integration
processing speed
attention control
creative synthesis
value reasoning
coordination intelligence
exploration efficiency
planning
simulation
error localization
epistemic humility
multi-agent coordination
```

These should not enter the canonical registry merely because they sound useful.

They require:

```text
definition
distinctness
measurement grammar
validation plan
```

---

# Processing Speed

Processing speed deserves special handling because it is often captured by conventional tasks.

It may be represented as a dimension in future RIQF versions.

For the initial framework, it can remain a directly observed performance characteristic such as:

```text
rapid_symbolic_processing
timed_classification
response_latency
```

without assuming:

```text
speed = intelligence
```

or:

```text
speed is irrelevant
```

Both extremes would be premature.

---

# Memory

Memory may similarly require decomposition.

Candidate future distinctions:

```text
short-term recall
working-memory manipulation
long-term recall
associative memory
context retention
retrieval fidelity
external-memory coordination
```

A single:

```text
memory
```

dimension may be too coarse.

---

# Creativity

Creativity is intentionally not included as one initial master dimension.

Possible components may involve:

```text
novelty
usefulness
divergence
constraint satisfaction
cross-domain synthesis
reframing
```

These overlap with several existing candidate dimensions.

Whether a distinct creativity dimension adds value should be tested.

---

# Intelligence Dimension Is Not Moral Dimension

RIQF does not include:

```text
kindness
honesty
moral worth
political belief
religious belief
social status
wealth
productivity
obedience
```

as intelligence dimensions.

A system should not quietly turn social approval into cognitive measurement.

---

# Preferred Expression

A dimension may be more observable through certain substrates.

Example:

```yaml
dimension:
  structural-reasoning

  preferred_expression:
    - relational
    - spatial
    - system-level
```

This should be treated as a hypothesis to test.

It must not become a way to select only favorable conditions.

---

# Possible Suppressors

Candidate suppressors may include:

```text
severe time pressure
context removal
inaccessible interface
irrelevant language complexity
tool restriction
environmental noise
fatigue
stress
poor task fit
```

A suppressor must not be inferred simply because performance was low.

Its effect requires evidence.

---

# Dimension Profile Record

Suggested canonical grammar:

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

    coverage:
      status: partial

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
    topology: not_tested

  confounds:
    - domain_expertise
    - task_familiarity

  adapters:
    structural_detection:
      status: candidate_support

    fft:
      status: candidate_support

  applicability:
    human: applicable
    ai: applicable
    human_ai_pair: substrate_dependent

  generalizability:
    status: unknown

  validation_state:
    unvalidated

  decision_authority:
    none
```

---

# Multi-Dimension Profile

Example:

```yaml
profile:
  pattern-recognition:
    expression: strong
    confidence: medium

  structural-reasoning:
    expression: strong
    confidence: medium

  temporal-reasoning:
    expression: moderate
    confidence: medium

  symbolic-reasoning:
    expression: moderate
    confidence: medium

  cross-domain-transfer:
    expression: strong
    confidence: low

  embodied-environmental-fit:
    expression: unknown
    confidence: none
```

The profile should not automatically compute:

```text
overall intelligence
```

---

# Dimension Relationships

Dimensions may interact.

Possible relationship states:

```text
positively_associated
negatively_associated
conditionally_associated
independent
redundant
causally_unknown
unresolved
```

These relationships require empirical evidence.

---

# Dimension Graph

A future representation might resemble:

```text
Pattern Recognition
       │
       ├──────── Structural Reasoning
       │               │
       │               ├──── Reconstruction
       │               │
       │               └──── Cross-Domain Transfer
       │
       └──────── Anomaly Detection

Temporal Reasoning
       │
       ├──────── Regime Recognition
       │
       └──────── Drift Awareness

Ambiguity Navigation
       │
       ├──────── Adaptive Reframing
       │
       └──────── Metacognitive Calibration
```

This graph is conceptual.

It must not be treated as established cognitive architecture.

---

# Dimension Redundancy

If two dimensions repeatedly behave as the same construct:

```text
Dimension A
approximately equals
Dimension B
```

then the correct action may be:

```text
merge
```

not:

```text
keep both because the taxonomy looks richer
```

---

# Dimension Split

The reverse may also occur.

Example:

```text
Tool Collaboration
```

might eventually separate into:

```text
tool selection
tool verification
tool orchestration
human-AI coordination
```

if evidence supports distinct constructs.

---

# Dimension Lifecycle

Canonical states:

```text
proposed
experimental
pilot
validated_for_context
restricted
deprecated
rejected
```

No candidate dimension is guaranteed promotion.

---

# Dimension Validation Requirements

A candidate dimension should ideally demonstrate:

1. operational clarity,
2. observable indicators,
3. counter-indicators,
4. adequate evidence coverage,
5. test-retest behavior appropriate to the construct,
6. alternate-form behavior,
7. inter-rater reliability where relevant,
8. convergent value,
9. discriminant value,
10. incremental value where claimed,
11. robustness,
12. fairness,
13. explainability,
14. appropriate uncertainty,
15. applicability boundaries.

---

# Primary Dimension Metrics

Relevant metrics include:

```text
PA-M01  Dimension Evidence Coverage
PA-M03  Evidence Independence Ratio

PA-M04  Test-Retest Stability
PA-M05  Alternate-Form Stability
PA-M06  Inter-Rater Agreement

PA-M08  Convergent Association
PA-M09  Discriminant Separation
PA-M10  Incremental Explanatory Value
PA-M11  Incremental Predictive Value

PA-M28  Confidence Calibration Error
PA-M32  Unsupported Assertion Rate

PA-M33  Irrelevant Perturbation Stability
PA-M34  Relevant Change Sensitivity

PA-M37  Group Error Difference
PA-M38  Group Calibration Difference
PA-M42  Evidence Coverage Difference

PA-M45  Evidence Reconstruction Rate
PA-M46  Explanation Completeness
```

---

# Dimension Evidence Coverage

Conceptually:

```text
DEC =
  supported_indicators
  /
  required_indicators
```

High coverage does not establish validity.

It means the dimension interpretation is supported by more of its declared evidence requirements.

---

# Evidence Independence

Suppose Structural Reasoning is supported by:

```text
FFT interpretation of E1
Structural Detection interpretation of E1
RTT interpretation of E1
```

Then:

```text
adapter_support_count:
  3

independent_evidence_count:
  1
```

Confidence should not increase as though three independent tasks were observed.

---

# Convergent Validation

A dimension should relate appropriately to other measurements that theory predicts are related.

Example:

```text
structural_reasoning
```

might be expected to relate to independently designed structural reconstruction tasks.

The relationship must be preregistered where possible.

---

# Discriminant Validation

A dimension should remain distinguishable from constructs it claims not to represent.

Example:

If:

```text
structural_reasoning
```

and:

```text
pattern_recognition
```

cannot be empirically distinguished, the registry should question whether both are necessary.

---

# Incremental Value

A new dimension should not survive merely because it creates a compelling description.

Ask:

> **Does it add useful information beyond simpler or established constructs?**

If not:

```text
dimension:
  candidate_for_merge_or_deprecation
```

---

# Counterfactual Testing

Every dimension should be challenged.

Example:

```text
Structural Reasoning:
  strong
```

Then:

```text
remove one favorable task
add adverse task
change alternate form
change evaluator
change irrelevant metadata
change substrate
repeat later
```

A robust dimension responds appropriately.

---

# Relevant Versus Irrelevant Change

Desired:

```text
irrelevant change
  ->
stable dimension interpretation

relevant evidence change
  ->
responsive interpretation
```

Failure modes:

```text
irrelevant change
  ->
large profile movement

or

relevant change
  ->
no profile movement
```

---

# Substrate Sensitivity

Dimension expression may vary by substrate.

Example:

```yaml
structural-reasoning:
  relational:
    expression: strong

  visual:
    expression: strong

  symbolic:
    expression: moderate

  severe_time_constraint:
    expression: weak
```

This may represent useful context.

It does not automatically establish a substrate effect.

Replication and controls are required.

---

# Regime Sensitivity

Dimension expression may vary by regime.

Example:

```yaml
structural-reasoning:
  regime_a:
    expression: moderate

  regime_b:
    expression: strong

  cross_regime:
    status: partially_stable
```

RTT may help define the regimes.

The dimension still requires independent evidence.

---

# Temporal Stability

A dimension should record time.

```yaml
dimension:
  id: cross-domain-transfer

  T1:
    expression: strong

  T2:
    expression: moderate

  T3:
    expression: moderate
```

Possible interpretations:

```text
drift
learning
fatigue
measurement change
regime change
substrate change
unknown
```

Cause requires evidence.

---

# Profile Topology

The shape across dimensions may be more informative than a simple average.

Example:

```text
          Structural
             █████

Transfer █████     ███ Temporal

Ambiguity █████   ██ Symbolic

             ████
            Regime
```

Topology may be:

```text
asymmetric
balanced
clustered
spiked
flat
unstable
unknown
```

These are descriptive states.

They do not imply superiority.

---

# Asymmetry

An asymmetric profile is not a defect.

Nor is it automatically exceptional.

It means:

```text
different dimensions show
materially different observed expression
```

Possible interpretation:

```text
profile:
  asymmetric

human_worth:
  not_inferred

global_intelligence_rank:
  not_inferred
```

---

# Fingerprint Similarity

Two profiles may look similar.

That does not mean the systems are:

```text
the same
```

or:

```text
equally intelligent
```

Similarity should be interpreted only relative to the dimensions and contexts actually observed.

---

# Cross-System Dimensions

Some candidate dimensions may generalize functionally across:

```text
human
AI
human-AI pair
robotic system
team
organization
```

Example:

```text
anomaly detection
```

can be operationalized in multiple system classes.

But:

```text
same task label
!=
same cognitive mechanism
```

---

# Cross-System Comparison

Appropriate comparison:

```text
System A and System B both
performed strongly on
operational task X.
```

Inappropriate inference:

```text
System A and System B
possess equivalent intelligence.
```

The framework should preserve the narrower claim.

---

# Human-AI Pair Dimensions

A human-AI pair may exhibit capabilities not reducible to either participant.

Candidate pair-level dimensions may include:

```text
tool collaboration
coordination
error correction
joint structural synthesis
division of cognitive labor
cross-checking
```

These may eventually require their own registry.

The initial RIQF should not assume individual and pair profiles are directly comparable.

---

# Environmental Fit

One system may excel in:

```text
high-context environment
```

another in:

```text
rapid low-context classification
```

Neither context defines universal intelligence.

The profile should preserve:

```text
where capability becomes observable
```

without converting environmental fit into global rank.

---

# Speed Versus Depth

A recurring research question:

```text
rapid performance
```

versus:

```text
reflective performance
```

These may be partially distinct.

Example:

```text
rapid symbolic:
  weak

reflective structural:
  strong
```

Correct initial finding:

```text
performance differs
```

Not:

```text
deep thinker
```

until a validated construct supports such a label.

---

# Breadth Versus Depth

A system may show:

```text
high depth
narrow domain breadth
```

or:

```text
moderate depth
broad transfer
```

Future RIQF versions may need explicit measures for:

```text
breadth
depth
```

The current dimensions should not pretend to fully capture this distinction.

---

# Dimension Interactions

Performance may emerge from interaction among dimensions.

Example:

```text
Pattern Recognition
+
Structural Reasoning
+
Temporal Reasoning
+
Ambiguity Navigation
```

may jointly support:

```text
complex system diagnosis
```

Interaction is not equivalent to simple addition.

---

# No Dimension Summation Rule

Avoid:

```text
pattern = 8
structural = 9
temporal = 7

IQ = 8 + 9 + 7
```

This does not become valid merely because several dimensions were measured.

---

# Composite Policy

If a future use legitimately requires composites:

```yaml
composite:
  permitted: true

  intended_use:
    explicitly_declared

  validation:
    required

  interpretive_status:
    lossy_projection

  sufficient_alone:
    false

  profile_required:
    true
```

No universal intelligence composite is assumed.

---

# PAX-01 Example

Synthetic PAX-01 illustrates:

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
```

This is synthetic demonstration data.

It does not establish that these dimensions are valid or that a real person possesses this profile.

---

# PAX-01 Asymmetry

The synthetic example also includes:

```text
Rapid Symbolic Processing:
  weak-moderate

Timed Classification:
  weak

Short-Context Recall:
  moderate
```

The purpose is to demonstrate:

```text
strong dimensions
+
weak dimensions
+
unknown dimensions
```

inside one profile.

The system does not need to average them into a judgment of the person.

---

# Dimension Unknowns

A dimension may remain:

```text
unknown
```

because:

- no suitable task exists,
- evidence is missing,
- applicability is uncertain,
- the dimension cannot be measured reliably,
- the system boundary is inappropriate,
- the required substrate is unavailable.

Unknown must not become:

```text
average
```

or:

```text
zero
```

by default.

---

# Missing Data

Conceptual rule:

```text
missing != weak
```

If a dimension was not assessed:

```yaml
dimension:
  state: not_observed
```

If evidence is insufficient:

```yaml
dimension:
  state: insufficient_evidence
```

If irrelevant:

```yaml
dimension:
  state: not_applicable
```

These are different states.

---

# Dimension Conflict

A dimension can contain contradictory observations.

Example:

```text
structural task A:
  strong

structural task B:
  weak
```

Correct:

```yaml
structural-reasoning:
  state: conflicting_evidence
  expression: variable
```

rather than immediately:

```text
moderate
```

Averaging can erase meaningful disagreement.

---

# Dimension Coherence

Dimension-level coherence might consider:

```text
evidence independence
task similarity
substrate similarity
regime similarity
temporal stability
counterfactual robustness
```

A high number of observations alone should not establish high confidence.

---

# Fairness Requirements

Dimension validation should examine whether:

```text
task accessibility differs
language exposure differs
cultural assumptions differ
technology access differs
education exposure differs
evaluator behavior differs
missing evidence differs
substrate fit differs
```

across relevant groups.

A dimension that works well only for a narrow population should not silently claim universal applicability.

---

# Accessibility

Accessibility conditions may materially affect observed performance.

The framework should distinguish:

```text
construct_relevant_constraint
construct_irrelevant_barrier
unknown_constraint
```

Removing an irrelevant barrier may improve construct measurement rather than compromise it.

That classification requires expertise and evidence.

---

# Privacy

A 24-dimension cognitive profile may be substantially more sensitive than a single score.

Possible privacy risks include revealing:

```text
strength patterns
weakness patterns
preferred substrates
context sensitivity
uncertainty patterns
tool dependence
social interpretation patterns
temporal changes
```

Therefore collection should be purpose-limited.

---

# Sensitive Inference Boundary

Dimensions should not casually become proxies for:

```text
medical diagnosis
psychiatric condition
disability status
political belief
religious belief
criminal propensity
protected identity
```

Such inferences require separate legitimate purpose, evidence, governance, and validation.

---

# Dimension Naming

Names influence interpretation.

Avoid labels that imply:

```text
defect
inferiority
superiority
normality
abnormality
```

unless the construct and context genuinely justify such terms.

Prefer descriptive functional language.

---

# Versioning

Every profile should record:

```text
dimension_registry_version
```

because definitions may change.

Example:

```yaml
riqf:
  dimension_registry_version: 0.1.0
```

A profile created under:

```text
0.1.0
```

must not silently be interpreted under:

```text
2.0.0
```

if meanings have materially changed.

---

# Registry Change Record

Future updates should document:

```yaml
dimension_change:
  dimension_id:

  change_type:
    added
    renamed
    split
    merged
    restricted
    deprecated
    rejected

  previous_definition:
  current_definition:

  reason:
  evidence:
  compatibility:
```

---

# Deprecation

A dimension should be considered for deprecation when:

- evidence cannot support reliable measurement,
- it duplicates another dimension,
- it adds no incremental value,
- it creates unacceptable fairness problems,
- its definition remains unstable,
- its intended meaning cannot be operationalized.

Deprecation preserves lineage.

---

# Rejection

A stronger state:

```text
rejected
```

may be appropriate if evidence consistently contradicts the usefulness or validity of the proposed dimension.

Rejected dimensions should remain visible in research lineage.

Negative results matter.

---

# Minimal Dimension Validation Record

```yaml
dimension_validation:
  id:

  operational_definition:
    status:

  content_review:
    status:

  reliability:
    test_retest:
    alternate_form:
    inter_rater:

  validity:
    convergent:
    discriminant:
    incremental:

  robustness:
    irrelevant_perturbation:
    relevant_change:

  substrate:
    status:

  regime:
    status:

  fairness:
    status:

  explainability:
    status:

  lifecycle:
    state:
```

---

# Required Negative Controls

Dimension research should include cases where the target capability is deliberately absent or randomized.

Examples:

```text
random pattern task
invalid structural mapping
false anomaly set
non-reconstructable evidence
irrelevant context changes
false regime boundary
```

A dimension detector that always produces a positive signal is not useful.

---

# Required Adverse Evidence

Validation datasets should contain evidence capable of lowering an interpretation.

Example:

```text
initial:
  structural reasoning strong

additional:
  repeated failures on equivalent tasks
```

Correct:

```text
confidence decreases
```

or:

```text
dimension classification changes
```

The dimension must not become self-protecting.

---

# Required Favorable Evidence

Likewise the system must recognize new positive evidence.

Symmetry matters.

---

# Dimension Anti-Rescue Test

Ask:

> **Can the dimension remain weak after rich substrate-aware assessment?**

Required answer:

```text
yes
```

Ask:

> **Can the dimension become weaker after additional evidence?**

Required answer:

```text
yes
```

Ask:

> **Can the dimension remain unknown?**

Required answer:

```text
yes
```

---

# Dimension Anti-Ranking Test

Ask:

> **Can two profiles be compared without declaring one person globally smarter?**

Required answer:

```text
yes
```

Possible comparison:

```text
Profile A:
  stronger on dimensions X and Y

Profile B:
  stronger on dimensions Z and Q

global_ranking:
  not_generated
```

---

# Dimension Anti-Anthropocentrism Test

Ask:

> **Can a dimension be marked not applicable to an AI, robot, animal, team, or organization?**

Required answer:

```text
yes
```

No system should be penalized simply for failing to express a human-specific construct.

---

# Dimension Anti-AI-Equivalence Test

Ask:

> **Does strong AI performance on a human-designed task prove equivalent internal cognition?**

Required answer:

```text
no
```

The framework evaluates observable function unless stronger evidence supports stronger claims.

---

# Research Questions

1. Do the proposed dimensions represent reproducible constructs?
2. Which dimensions overlap?
3. Which dimensions should merge?
4. Which should split?
5. Which should be rejected?
6. Which dimensions add information beyond existing assessment frameworks?
7. Which merely rename established constructs?
8. How stable are dimensions across time?
9. How stable are they across alternate forms?
10. How sensitive are they to substrate?
11. How sensitive are they to regime?
12. Which dimensions generalize across domains?
13. Which remain domain-specific?
14. Which dimensions apply meaningfully to AI systems?
15. Which apply to human-AI pairs?
16. Which apply to organizations?
17. Can profile topology be measured reliably?
18. Does profile topology improve prediction?
19. Does it improve explanation?
20. Does it improve calibration?
21. Does it improve fairness?
22. Does it create new fairness problems?
23. How should speed be represented?
24. How should memory be decomposed?
25. Is creativity a distinct dimension?
26. Should social interpretation remain an intelligence dimension?
27. Should embodied fit remain part of the same registry?
28. Can tool collaboration be separated from tool access?
29. Can long-horizon integration be measured independently of memory?
30. Can recovery be separated from recalibration?
31. Can ambiguity navigation be separated from metacognitive calibration?
32. Can structural reasoning be separated from pattern recognition?
33. Can causal integration be measured without rewarding verbal explanation alone?
34. Can dimension confidence be calibrated?
35. How should missing evidence affect profile topology?
36. How should contradictory evidence be represented?
37. Can multidimensional profiles remain useful without composites?
38. When is a composite legitimately necessary?
39. What privacy risks arise from detailed fingerprints?
40. What evidence would justify abandoning the RIQF dimension model entirely?

---

# Core Invariants

```text
dimension != identity
dimension != human_worth
dimension != permanent_trait
observed_strength != universal_strength
observed_weakness != universal_weakness
missing != weak
unknown != average
not_applicable != zero
variation != defect
asymmetry != superiority
speed != intelligence
slowness != low_intelligence
pattern != truth
structure != intelligence
coherence != correctness
confidence != capability
adapter_support != independent_evidence
dimension_count != intelligence
profile_complexity != validity
profile_similarity != cognitive_equivalence
tool_assisted != unassisted
human_ai_pair != individual_human
same_label != same_mechanism
composite != total_intelligence
profile != destiny
canon_alignment != empirical_validation
```

---

# Closing Principle

The initial RIQF dimension registry is intentionally larger than a flat intelligence score.

That does not make it more correct.

Its value must come from whether the dimensions can be:

- defined,
- observed,
- distinguished,
- replicated,
- challenged,
- calibrated,
- validated,
- revised,
- and, when necessary, discarded.

The purpose is not to replace:

```text
one number
```

with:

```text
twenty-four unquestionable numbers
```

That would simply create a higher-dimensional version of the same mistake.

The purpose is to preserve more of the observable shape while keeping the limits of observation visible.

A future mature profile might therefore say:

```text
strong here
weak here
variable here
substrate-sensitive here
regime-sensitive here
stable here
changing here
unknown here
not applicable here
```

and stop there when the evidence stops.

> **An intelligence dimension earns its place not because it sounds like intelligence, but because it survives measurement, comparison, counterevidence, and time.**
