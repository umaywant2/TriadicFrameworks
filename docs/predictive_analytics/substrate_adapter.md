<img width="1194" height="672" alt="predictive_analytics_substrate_adapter_" src="https://github.com/user-attachments/assets/2225aa2f-9d7f-4c6f-b55e-4a136dc801cc" />

# Predictive Analytics — Substrate Adapter

> **What becomes observable depends partly on how observation is made.**

## Module

Predictive Analytics

## Adapter ID

`substrate`

## Operator

`PA-Substrate`

## Status

Experimental.

## Validation State

Unvalidated.

## Intended Role

Measurement-substrate, expression-substrate, accessibility, cross-substrate comparison, and substrate-fit adapter.

## Decision Authority

None.

---

# Purpose

The Substrate Adapter examines whether observed performance changes across the medium, representation, interface, interaction structure, or measurement conditions through which capability becomes observable.

Its purpose is to ask:

> **Does the measurement substrate provide an adequate opportunity to observe the capability or behavior being inferred?**

The adapter may compare observations across:

- textual substrates,
- verbal substrates,
- visual substrates,
- spatial substrates,
- symbolic substrates,
- relational substrates,
- embodied substrates,
- tool-mediated substrates,
- collaborative substrates,
- human-AI substrates,
- fixed-choice formats,
- generative formats,
- timed formats,
- reflective formats.

These categories are provisional.

They require operational definition and validation.

---

# Core Principle

The adapter distinguishes:

```text
observed performance
```

from:

```text
underlying capability
```

and both from:

```text
measurement substrate
```

Conceptually:

```text
Observed Expression
       │
       ▼
interaction of
       │
       ├── capability
       ├── substrate
       ├── task
       ├── regime
       ├── environment
       ├── observer
       └── measurement process
```

Therefore:

```text
performance_difference
!=
substrate_effect
```

and:

```text
substrate_effect
!=
substrate_mismatch
```

---

# Working Definition

Within Predictive Analytics:

> **A substrate is the medium or interaction structure through which a target behavior, capability, or system state becomes observable.**

A substrate may affect:

- what information is available,
- how information is represented,
- how the observed system interacts with it,
- what responses are possible,
- which tools are available,
- how much time is available,
- and what the measurement process records.

---

# Substrate Is Not Just Hardware

In this module, substrate is broader than:

```text
physical material
```

or:

```text
computing hardware
```

A predictive observation may have substrates such as:

```text
spoken language
written language
symbolic notation
visual diagram
physical environment
multiple-choice interface
open-response interface
human-AI collaboration
tool-mediated interaction
```

These are functional observation substrates.

---

# Substrate Is Not Automatically Regime

A substrate describes:

```text
the medium or interaction structure
through which expression is observed
```

A regime describes:

```text
the broader operating conditions
under which relevant relationships remain sufficiently stable
```

Therefore:

```text
substrate != regime
```

A single substrate can occur inside multiple regimes.

A regime can contain multiple substrates.

---

# Substrate Is Not Context

Context may include:

```text
social setting
task framing
domain
history
environment
instructions
available information
```

Substrate may be one component of context.

Therefore:

```text
context_difference
!=
substrate_difference
```

---

# Substrate Pipeline

```text
Observed System
       │
       ▼
Declare Target Capability
       │
       ▼
Declare Baseline Substrate
       │
       ▼
Measure Baseline Expression
       │
       ▼
Declare Comparison Substrate
       │
       ▼
Measure Comparison Expression
       │
       ▼
Check Task Comparability
       │
       ▼
Check Regime
       │
       ▼
Check Time
       │
       ▼
Check Accessibility
       │
       ▼
Estimate Expected Variation
       │
       ▼
Test Replication
       │
       ▼
Control Alternative Explanations
       │
       ▼
Challenge Counterfactually
       │
       ▼
Classify Substrate Relationship
       │
       ▼
Return:
  comparable
  effect_candidate
  effect_supported
  mismatch_candidate
  partial_fit
  no_detectable_effect
  unresolved
  insufficient_evidence
```

---

# Substrate Record

Suggested representation:

```yaml
substrate:
  id: substrate-001

  name:
    reflective-relational-text

  class:
    relational

  modality:
    textual

  response_structure:
    generative

  timing:
    reflective

  interaction:
    individual

  tools:
    none

  accessibility:
    status: unknown

  measurement:
    instrument:
    version:

  evidence:
    - observation-reference

  validation_state:
    unvalidated
```

---

# Substrate Classes

The initial module may use:

```text
SA-01  Textual
SA-02  Verbal
SA-03  Visual
SA-04  Spatial
SA-05  Symbolic
SA-06  Relational
SA-07  Embodied
SA-08  Fixed Choice
SA-09  Generative
SA-10  Timed
SA-11  Reflective
SA-12  Tool-Mediated
SA-13  Collaborative
SA-14  Human-AI
SA-15  Multimodal
SA-16  Unknown / Mixed
```

These classes can overlap.

Example:

```text
reflective
+
relational
+
textual
+
generative
```

may describe one actual substrate configuration.

---

# SA-01 — Textual

Expression occurs primarily through written language.

Possible forms:

```text
reading
writing
text interpretation
text generation
structured textual reasoning
```

Potential confounds:

```text
literacy
language familiarity
typing
reading accessibility
domain vocabulary
```

---

# SA-02 — Verbal

Expression occurs primarily through spoken language.

Possible influences include:

```text
speech production
hearing
language fluency
social interaction
response latency
```

A verbal result should not automatically be compared directly with a written result without considering these differences.

---

# SA-03 — Visual

The task principally communicates or receives information visually.

Examples:

```text
images
graphs
diagrams
patterns
visual maps
```

Possible confounds:

```text
vision
visual literacy
display quality
color accessibility
diagram familiarity
```

---

# SA-04 — Spatial

The task requires interaction with spatial relationships.

Examples:

```text
rotation
placement
navigation
relative position
physical layout
```

Spatial and visual substrates may overlap.

They should not be treated as identical by default.

---

# SA-05 — Symbolic

Information is represented primarily using formal or abstract symbols.

Examples:

```text
numbers
logic notation
algebra
code
abstract token systems
```

Important distinction:

```text
symbolic reasoning
!=
symbolic processing speed
```

---

# SA-06 — Relational

The task foregrounds relationships among components.

Examples:

```text
graphs
systems
dependency maps
network relations
causal diagrams
structured comparisons
```

The FFT and Structural Detection adapters may be especially relevant here.

---

# SA-07 — Embodied

Expression depends materially on interaction with a physical environment.

Examples may include:

```text
navigation
physical manipulation
sensorimotor coordination
robotic interaction
real-world task execution
```

Applicability varies strongly by system class.

---

# SA-08 — Fixed Choice

The response space is predefined.

Example:

```text
A
B
C
D
```

Advantages may include:

```text
standardization
easy scoring
controlled comparison
```

Potential limitation:

```text
expression constrained to predefined options
```

The limitation must not be assumed to matter unless evidence supports it.

---

# SA-09 — Generative

The response is constructed rather than selected.

Examples:

```text
free response
system reconstruction
explanation
design
open problem solving
```

Generative tasks may reveal additional information.

They may also introduce:

```text
scoring complexity
language confounds
evaluator variability
```

More expressive does not automatically mean more valid.

---

# SA-10 — Timed

Available response time is deliberately constrained.

Timing may itself be construct-relevant.

Example:

```text
processing speed assessment
```

In that case:

```text
time constraint
```

is not necessarily a substrate defect.

---

# Timed-Task Principle

If the target is:

```text
rapid processing under time constraint
```

then removing the time limit may change the construct.

Correct:

```text
different measurement target
```

possibly.

Not automatically:

```text
better substrate
```

---

# SA-11 — Reflective

The task allows a longer or less constrained response interval.

A reflective substrate may reveal capabilities suppressed by speed requirements.

Or it may simply measure different capabilities.

This must be tested.

---

# SA-12 — Tool-Mediated

The observed system is allowed to use external tools.

Examples:

```text
calculator
search
database
software
AI
simulation
external memory
```

Tool-mediated performance is meaningful.

Its attribution depends on the declared system boundary.

---

# SA-13 — Collaborative

Multiple participants contribute to the observed result.

Possible systems:

```text
human pair
team
human-tool system
human-AI pair
multi-agent system
```

Collaborative performance must not automatically become individual capability.

---

# SA-14 — Human-AI

The observed system includes both human and AI participation.

Correct boundary:

```yaml
observed_system:
  class:
    human_ai_pair
```

unless an experimental design separately isolates component contributions.

---

# SA-15 — Multimodal

Multiple modalities contribute materially.

Example:

```text
text + image + speech
```

or:

```text
vision + sensor + language
```

A multimodal substrate may not be cleanly reducible to its components.

---

# SA-16 — Unknown / Mixed

Where substrate structure cannot be adequately specified:

```text
unknown
```

or:

```text
mixed
```

should remain available.

Do not force classification.

---

# Substrate Configuration

A real observation may use multiple substrate descriptors.

Example:

```yaml
substrate_configuration:
  modality:
    textual

  representation:
    relational

  response:
    generative

  timing:
    reflective

  tool_access:
    none

  interaction:
    individual
```

This is generally more informative than a single label:

```text
text
```

---

# Target Capability

Substrate analysis must declare what capability is being observed.

Example:

```yaml
target:
  id:
    structural_reasoning

  operational_definition:
    ability to reconstruct
    defined system relationships
```

Without a target, substrate fit becomes vague.

---

# Baseline Substrate

Substrate analysis requires a comparison reference.

Example:

```yaml
baseline_substrate:
  modality: symbolic
  response: fixed_choice
  timing: timed
```

---

# Comparison Substrate

Example:

```yaml
comparison_substrate:
  modality: textual
  representation: relational
  response: generative
  timing: reflective
```

Several variables changed.

The adapter must expose that.

---

# Changed Variables

Suggested record:

```yaml
substrate_comparison:
  changed:
    - modality
    - representation
    - response_structure
    - timing

  held_constant:
    - target
    - evaluator

  unknown:
    - difficulty_equivalence
```

This prevents false causal simplification.

---

# Minimal-Change Principle

Where possible:

> **Change one substrate dimension at a time before evaluating interactions.**

Example:

```text
Test 1:
  timed
  ->
  reflective

Test 2:
  fixed-choice
  ->
  generative

Test 3:
  symbolic
  ->
  relational
```

Then investigate interactions.

---

# Factorial Substrate Analysis

Some effects may arise only from combinations.

Example:

```text
timing alone:
  small effect

representation alone:
  small effect

timing + representation:
  large effect
```

Therefore:

```text
one-variable tests
```

may be followed by:

```text
interaction tests
```

where appropriate.

---

# Substrate Fit

Substrate fit asks:

> **Does this measurement configuration provide an adequate basis for the intended inference?**

Possible states:

```text
high
moderate
low
partial
mismatch_candidate
mismatch_supported
unknown
not_applicable
```

---

# Fit Is Purpose-Dependent

A substrate may be excellent for:

```text
rapid classification
```

and poor for:

```text
open structural synthesis
```

Neither fact makes the substrate universally good or bad.

Therefore:

```text
substrate_fit
```

must always refer to:

```text
target + intended inference
```

---

# Substrate Mismatch

A mismatch candidate occurs when evidence suggests:

```text
measurement substrate
```

systematically obscures, distorts, constrains, or differently samples the target in a way that makes the intended inference unreliable or overbroad.

This is stronger than:

```text
performance differs
```

---

# Mismatch Requirements

A substrate mismatch claim should ideally include:

```text
defined target
baseline substrate
comparison substrate
matched observations
replication
effect magnitude
alternative explanations
counterevidence
specificity
appropriate regime controls
```

---

# Example — Difference Without Mismatch

```text
Task target:
  rapid symbolic processing

Timed symbolic:
  strong

Untimed relational:
  strong
```

Different substrates.

No mismatch is apparent.

---

# Example — Different Construct

```text
Timed symbolic:
  weak

Untimed creative writing:
  strong
```

These observations differ greatly.

But the tasks may not observe the same construct.

Correct:

```text
direct comparison:
  unsupported
```

Not:

```text
substrate mismatch
```

---

# Example — Candidate Mismatch

```text
Target:
  structural reconstruction

Fixed-choice structural representation:
  repeatedly weak

Generative structural reconstruction:
  repeatedly strong
```

with matched difficulty and replicated tasks.

Candidate:

```yaml
substrate_mismatch:
  status:
    candidate
```

Further validation remains necessary.

---

# Substrate Effect

A substrate effect describes a reproducible performance difference.

Conceptually:

```text
Effect(Sa, Sb)
  =
Expression(Sa)
-
Expression(Sb)
```

This notation is conceptual.

The actual metric should fit the measurement scale.

---

# Effect Direction

Possible states:

```text
higher_in_a
higher_in_b
equivalent
mixed
unknown
```

Avoid:

```text
better substrate
```

unless a declared objective defines what better means.

---

# Effect Magnitude

Possible descriptive states:

```text
negligible
small
moderate
large
unknown
```

Empirical work should use appropriate effect-size methods.

---

# Effect Replication

Possible states:

```text
single
partial
replicated
failed_replication
mixed
unknown
```

A candidate mismatch should weaken when replication fails.

---

# Substrate Symmetry

A strong safeguard:

> **The adapter must detect both favorable and adverse substrate effects.**

If:

```text
substrate B
```

produces stronger performance:

```text
record it
```

If it produces weaker performance:

```text
record that too
```

---

# Favorability Symmetry

The adapter fails if it becomes:

```text
unfavorable score
  ->
search for better substrate
  ->
report only improvement
```

Instead:

```text
all declared substrate comparisons
  ->
report complete results
```

---

# Accessibility

Accessibility deserves explicit representation.

A measurement difficulty may originate from:

```text
construct-relevant demand
```

or:

```text
construct-irrelevant accessibility barrier
```

or:

```text
unknown relationship
```

---

# Accessibility Record

```yaml
accessibility:
  condition:

  relationship_to_construct:
    relevant
    irrelevant
    unknown

  accommodation:
  evidence:

  interpretation:
```

A barrier should not automatically be removed from the assessment if it is part of the construct being measured.

Likewise it should not automatically be treated as capability if it is irrelevant to the intended construct.

---

# Accommodation Versus Substrate Change

An accommodation may alter the substrate.

Question:

> **Does the accommodation remove an irrelevant barrier or alter the target construct?**

That determination may require specialist judgment.

The adapter should preserve the change without pretending to resolve it automatically.

---

# Measurement Accessibility Principle

```text
accessible measurement
!=
easier measurement
```

and:

```text
harder measurement
!=
more valid measurement
```

Validity depends on the construct.

---

# Substrate and Model Fit

A predictive model trained under one substrate may perform differently under another.

Example:

```text
model training:
  fixed-choice

deployment:
  generative

prediction error:
  increases
```

Candidate:

```text
substrate-conditioned model fit
```

---

# Substrate and Model Mismatch

The Model Mismatch layer may classify:

```text
substrate_mismatch
```

when the substrate relationship threatens the model's intended inference.

The Substrate Adapter supplies the evidence.

It does not make the final mismatch claim alone.

---

# Substrate and FFT

FFT may map:

```text
relationships
boundaries
constraints
local/global context
```

that surround substrate changes.

Example:

```text
tool availability
```

changes the relationship structure of the task.

FFT may make that structural change explicit.

---

# Substrate and Inverted Star

Inverted Star may detect:

```text
prediction low
```

but:

```text
performance stronger
under another substrate
```

This produces:

```text
substrate inversion candidate
```

The Substrate Adapter asks whether the difference itself is reliable.

---

# Substrate and Structural Detection

Structural Detection asks whether performance variation across substrates has reproducible structure.

Example:

```text
relational:
  strong
  strong
  strong

symbolic:
  weak
  weak
  moderate
```

Candidate:

```text
structured substrate dependence
```

---

# Substrate and RTT

RTT asks whether substrate differences align with:

```text
regime
time
transition
continuity
drift
```

Substrate change can coincide with regime transition.

They should not be conflated automatically.

---

# Substrate and Resonance

The Resonance Adapter asks whether a substrate relationship behaves like:

```text
amplification
suppression
stabilization
```

The Substrate Adapter should establish the cross-substrate difference first.

---

# Substrate and Coherence

The Coherence Observer can ask:

```text
are within-substrate observations coherent?

are cross-substrate differences coherent?

do observations contradict one another?

are they conditionally compatible?
```

---

# Substrate and Drift

A substrate may change through time.

Example:

```text
T1:
  unassisted

T2:
  calculator-assisted

T3:
  AI-assisted
```

Performance movement may reflect:

```text
substrate drift
```

rather than underlying capability drift alone.

---

# Substrate and Counterfactuals

Substrate claims should be challenged.

Examples:

```text
match task difficulty
change only timing
change only response format
change only modality
change evaluator
change task order
remove one favorable observation
add adverse observation
```

If the effect disappears:

```text
substrate_interpretation:
  weakened
```

---

# Substrate and Uncertainty

Confidence should fall when:

```text
many substrate variables changed simultaneously
few observations exist
difficulty matching is weak
regime changed
system boundary changed
measurement changed
observer changed
replication failed
```

---

# Substrate and Human Review

Review may be appropriate when a consequential interpretation depends heavily on substrate mismatch.

Review questions:

1. What exactly was measured?
2. What changed between substrates?
3. Were tasks comparable?
4. Was difficulty comparable?
5. Did timing change?
6. Did response structure change?
7. Did accessibility change?
8. Did regime change?
9. Did the observed system boundary change?
10. Did tool availability change?
11. Did the effect replicate?
12. Were adverse comparisons retained?
13. Could a simpler interaction model explain the finding?

---

# Substrate and RIQF

RIQF can attach substrate expression to each candidate dimension.

Example:

```yaml
dimension:
  structural-reasoning

  substrates:
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

  substrate_effect:
    status: candidate

  causal_status:
    unresolved
```

This preserves the structure without defining a "true" substrate.

---

# Worked Example — PAX-01

## Baseline

Synthetic PAX-01 baseline:

```text
timed
symbolic
fixed-choice
individual
```

Observed:

```text
rapid symbolic:
  weak

timed classification:
  weak
```

Extended tasks:

```text
reflective relational:
  strong

generative structural:
  strong

context-rich synthesis:
  strong
```

The initial result is:

```text
performance differs across measurement conditions
```

Nothing more.

---

# Pass 1 — Declare Targets

Baseline directly targets:

```text
rapid symbolic processing
timed classification
```

Extended tasks target:

```text
structural reasoning
cross-domain transfer
synthesis
```

These are not fully equivalent constructs.

Therefore:

```text
direct global cross-substrate comparison:
  limited
```

This is important.

---

# Pass 2 — Create Matched Structural Tasks

Synthetic matched target:

```text
structural reconstruction
```

Task A:

```text
symbolic
fixed-choice
timed
```

Task B:

```text
relational
generative
reflective
```

Observed:

```text
A:
  weak

B:
  strong
```

Candidate:

```text
condition effect
```

---

# Pass 3 — Identify Changed Variables

```yaml
changed:
  - representation
  - response_structure
  - timing

held_constant:
  - target

unknown:
  - exact difficulty equivalence
```

Therefore:

```text
substrate cause:
  underdetermined
```

---

# Pass 4 — Isolate Timing

Create matched tasks:

```text
symbolic fixed-choice timed
```

versus:

```text
symbolic fixed-choice reflective
```

Synthetic observation:

```text
timed:
  weak

reflective:
  moderate
```

Candidate:

```text
timing contribution
```

---

# Pass 5 — Isolate Response Structure

```text
reflective fixed-choice:
  moderate

reflective generative:
  moderate-strong
```

Candidate:

```text
response-structure contribution
```

---

# Pass 6 — Isolate Representation

```text
reflective symbolic:
  moderate

reflective relational:
  strong
```

Candidate:

```text
representation contribution
```

---

# Pass 7 — Interaction

The strongest difference occurs when:

```text
reflective
+
relational
+
generative
```

appear together.

Possible:

```text
interaction effect
```

This requires further testing.

---

# Pass 8 — Replication

Suppose matched tasks show:

```text
Relational:
  strong
  strong
  moderate-strong

Symbolic:
  moderate
  moderate
  weak-moderate
```

Synthetic result:

```text
cross-substrate pattern:
  demonstration candidate
```

Still not empirical validation.

---

# Pass 9 — Counterevidence

Add:

```text
relational task:
  weak
```

Correct behavior:

```text
substrate confidence:
  decreases
```

The adapter must retain the contradictory observation.

---

# PAX-01 Substrate Result

```yaml
substrate_result:
  target:
    structural_reasoning

  baseline:
    symbolic_timed_fixed:
      expression: weak

  comparisons:
    symbolic_reflective:
      expression: moderate

    relational_reflective:
      expression: strong

    relational_generative_reflective:
      expression: strong

  effect:
    status: candidate

  timing_contribution:
    candidate

  representation_contribution:
    candidate

  response_structure_contribution:
    candidate

  interaction:
    possible

  mismatch:
    status: unresolved_candidate

  causal_status:
    unresolved

  validation_state:
    unvalidated

  decision_authority:
    none
```

---

# Important Non-Conclusion

The adapter does **not** conclude:

> "PAX-01's true intelligence appears only on relational tasks."

It may conclude:

> **"In this synthetic example, observed structural-reasoning performance varies across the defined measurement conditions. Timing, representation, and response structure are candidate contributors, but their causal roles and generalizability remain unresolved."**

That is the intended level of interpretation.

---

# Baseline-Sufficient Example

Suppose matched tasks produce:

```text
timed symbolic:
  moderate

reflective symbolic:
  moderate

reflective relational:
  moderate

generative relational:
  moderate
```

Correct:

```yaml
substrate_effect:
  status: not_supported

baseline_model:
  substrate_robustness:
    supported_candidate
```

The adapter added no substantive information.

---

# False Substrate Effect

Initial:

```text
visual:
  strong

textual:
  weak
```

Later matched observations:

```text
visual:
  weak
  moderate

textual:
  strong
  moderate
```

Correct:

```yaml
initial_substrate_effect:
  failed_replication: true

current_status:
  unresolved_or_not_supported
```

---

# Favorable Effect Failure

Baseline:

```text
weak
```

New substrate:

```text
strong
```

Replications:

```text
weak
moderate
weak
```

Correct:

```text
favorable_substrate_interpretation:
  rejected_or_weakened
```

---

# Adverse Effect Failure

Baseline:

```text
strong
```

New substrate:

```text
weak
```

Replications:

```text
strong
moderate
strong
```

Correct:

```text
adverse_substrate_interpretation:
  rejected_or_weakened
```

Same evidentiary standard.

---

# Human-AI Example

Human alone:

```text
structural synthesis:
  moderate
```

AI alone:

```text
structural synthesis:
  moderate
```

Human-AI pair:

```text
structural synthesis:
  strong
```

Correct:

```yaml
substrate_or_system_change:
  human_ai_pair:
    observed: true

system_boundary:
  changed: true

individual_human_inference:
  unsupported
```

Human-AI collaboration is more than a simple substrate shift because the observed system itself changes.

---

# Tool-Mediated Example

Human:

```text
unassisted:
  moderate

calculator-assisted:
  strong
```

If the target is:

```text
real-world quantitative problem solving
```

the tool-assisted condition may be relevant.

If the target is:

```text
unaided calculation
```

the tool changes the construct.

Substrate fit depends on intended use.

---

# AI-System Example

AI model:

```text
text-only:
  moderate

text + image:
  strong
```

Correct:

```text
multimodal performance difference
```

before:

```text
multimodal substrate mismatch
```

is claimed.

Possible causes:

```text
model architecture
training
task design
information availability
representation
unknown
```

---

# Robotic Example

Robot:

```text
simulation:
  strong

physical environment:
  weak
```

Candidate:

```text
simulation-to-embodied substrate difference
```

This may be operationally important.

It does not establish the causal source of the gap.

---

# Organizational Example

Organization:

```text
email-only coordination:
  slow

shared operational dashboard:
  faster
```

Possible:

```text
coordination substrate effect
```

But workflow, process, training, and incentives may also differ.

The analogy is functional.

---

# Substrate Fit Matrix

A future representation may compare:

```text
                 Target Capability

                A      B      C      D
            ┌──────┬──────┬──────┬──────┐
Textual     │ high │ mod. │ high │ unk. │
            ├──────┼──────┼──────┼──────┤
Visual      │ mod. │ high │ mod. │ high │
            ├──────┼──────┼──────┼──────┤
Symbolic    │ high │ low  │ mod. │ low  │
            ├──────┼──────┼──────┼──────┤
Relational  │ mod. │ high │ high │ mod. │
            └──────┴──────┴──────┴──────┘
```

This is conceptual.

No such universal matrix is currently validated.

---

# Substrate Metrics

## `PA-M12 — Substrate Effect Magnitude`

Conceptually:

```text
SEM =
  standardized_difference(
    performance_a,
    performance_b
  )
```

The statistical form must match the measurement.

---

# `PA-M13 — Substrate Effect Replicability`

```text
SER =
  replicated_effects_in_expected_direction
  /
  eligible_replications
```

---

# `PA-M14 — Substrate Symmetry`

Tests whether favorable and adverse effects are detected under comparable evidence standards.

---

# `PA-M15 — Substrate Specificity`

Tests whether the apparent substrate effect survives control for relevant alternatives.

---

# Related Metrics

Substrate analysis may also use:

```text
PA-M01  Dimension Evidence Coverage
PA-M03  Evidence Independence Ratio

PA-M04  Test-Retest Stability
PA-M05  Alternate-Form Stability
PA-M06  Inter-Rater Agreement

PA-M10  Incremental Explanatory Value
PA-M11  Incremental Predictive Value

PA-M19  Regime-Conditioned Stability

PA-M20  Model-Mismatch Precision
PA-M21  Model-Mismatch Recall
PA-M22  Model-Mismatch False Positive Rate

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

# Substrate Validation Ladder

## Stage 0 — Define Target

What capability or behavior is being observed?

---

## Stage 1 — Define Substrates

What precisely differs between the substrate conditions?

---

## Stage 2 — Establish Comparability

Are the tasks sufficiently comparable?

---

## Stage 3 — Observe Difference

Does performance differ?

---

## Stage 4 — Replicate

Does the difference repeat?

---

## Stage 5 — Isolate Variables

Can timing, modality, response structure, tool access, and other components be separated?

---

## Stage 6 — Test Specificity

Does the effect survive controls?

---

## Stage 7 — Counterfactual Challenge

Does the interpretation survive reasonable perturbations?

---

## Stage 8 — Incremental Value

Does substrate awareness improve:

```text
prediction
calibration
explanation
fairness
model-mismatch detection
```

---

# Validation Baselines

Compare substrate-aware interpretation against:

```text
ordinary task-effect models
interaction models
matched task comparisons
mixed-effects models
multilevel models
accessibility-aware assessment approaches
measurement invariance methods
```

where appropriate.

The Substrate Adapter earns its role only if it contributes useful information beyond credible baselines.

---

# Null Substrate Test

Provide matched substrate conditions that should not affect the target.

Expected:

```text
substrate_effect:
  not_detected
```

A system finding mismatch regardless has failed.

---

# Known Effect Test

Use a controlled process where substrate affects observable performance.

Expected:

```text
effect:
  detected
```

without overclaiming cause beyond the design.

---

# Difficulty-Matching Test

Create apparent substrate differences using unequal task difficulty.

Then match difficulty.

If effect disappears:

```text
substrate_effect:
  not_supported
```

---

# Accessibility Test

Introduce an interface barrier unrelated to the target.

An appropriate measurement process should detect:

```text
accessibility issue
```

rather than:

```text
low target capability
```

where the construct definition supports that distinction.

---

# Construct-Relevance Test

Conversely, if timing is explicitly part of the target:

```text
rapid response under time constraint
```

removing timing should not automatically be called an accessibility correction.

It may change the construct.

---

# Randomization Test

Randomize substrate labels.

A true substrate-dependent pattern should weaken substantially.

If it persists:

```text
possible leakage
overfitting
or unrelated structure
```

---

# Holdout Test

Discover a substrate effect on one set.

Predict:

```text
which substrate should produce
different expression
```

on held-out observations.

This is stronger than retrospective interpretation.

---

# Counterfactual Test

Change:

```text
irrelevant metadata
```

while holding the substrate fixed.

The interpretation should remain stable.

Change:

```text
relevant substrate component
```

where the synthetic process makes it meaningful.

The system should respond.

---

# Symmetry Test

Include:

```text
substrate improves performance
substrate worsens performance
substrate has no effect
```

The adapter must represent all three.

---

# Human-AI Boundary Test

Move from:

```text
human alone
```

to:

```text
human-AI pair
```

The adapter should detect:

```text
system boundary changed
```

and avoid treating the result as merely an individual-level substrate effect.

---

# Failure Modes

## Substrate Rescue

Risk:

After an unfavorable result, substrates are searched until stronger performance appears.

Mitigation:

Predeclare comparisons and report all outcomes.

---

# Substrate Blame

Risk:

Weak performance is always attributed to substrate.

Mitigation:

Permit baseline-supported results.

---

# Favorability Bias

Risk:

Stronger alternate performance gets more interpretive weight than weaker alternate performance.

Mitigation:

PA-M14, PA-M43, PA-M44.

---

# Adverse Bias

Risk:

Poor performance on one substrate receives disproportionate global interpretation.

Mitigation:

Scope conclusions to conditions.

---

# Construct Substitution

Risk:

Different tasks actually measure different constructs.

Mitigation:

Declare target and comparability.

---

# Difficulty Confounding

Risk:

One substrate condition is simply easier.

Mitigation:

Matched difficulty and appropriate controls.

---

# Multi-Variable Confounding

Risk:

Timing, modality, response structure, and tools change simultaneously.

Mitigation:

Minimal-change testing.

---

# Accessibility Confusion

Risk:

A construct-irrelevant barrier is treated as capability.

Mitigation:

Accessibility review.

---

# Accommodation Inflation

Risk:

Every stronger accommodated result is called the true capability.

Mitigation:

Require construct analysis.

---

# Tool Attribution Error

Risk:

Tool-assisted performance is attributed entirely to the individual.

Mitigation:

Explicit system boundary.

---

# Human-AI Boundary Collapse

Risk:

Pair-level performance becomes human or AI individual performance.

Mitigation:

Separate pair profile.

---

# Regime Confusion

Risk:

A regime change is mislabeled purely as substrate effect.

Mitigation:

Regime Observer integration.

---

# Time Confusion

Risk:

Later performance improvement is attributed to substrate when learning occurred.

Mitigation:

Temporal controls.

---

# Observer Confusion

Risk:

Different evaluators create apparent substrate differences.

Mitigation:

Evaluator provenance.

---

# Precision Theater

Risk:

Substrate fit receives a precise numeric score without validated scale.

Mitigation:

Use descriptive states until measurement supports precision.

---

# Causal Overreach

Risk:

Substrate association becomes causal claim.

Mitigation:

Preserve:

```text
effect detected
cause unresolved
```

---

# Canon Confirmation

Risk:

Substrate sensitivity is assumed because PA expects it.

Mitigation:

Null controls and baseline comparison.

---

# Falsification Conditions

The Substrate Adapter should be revised, restricted, deprecated, or rejected if:

- null substrate comparisons routinely produce effects,
- candidate effects fail replication,
- effects disappear after basic difficulty controls,
- effects depend heavily on evaluator choice,
- substrate categories cannot be operationalized,
- favorable and adverse effects are treated asymmetrically,
- system-boundary changes are misclassified as individual substrate effects,
- matched tasks do not support cross-substrate differences,
- simpler interaction models explain the same results equally well,
- substrate-aware analysis does not improve any claimed outcome,
- or ablation shows negligible contribution.

---

# Anti-Rescue Test

Ask:

> **Can the adapter conclude that an unfavorable result remains valid across appropriate substrates?**

Required answer:

```text
yes
```

---

# Anti-Adverse Test

Ask:

> **Can the adapter reject an unsupported adverse substrate interpretation?**

Required answer:

```text
yes
```

---

# No-Effect Test

Ask:

> **Can the adapter conclude that substrate had no detectable effect?**

Required answer:

```text
yes
```

---

# Different-Construct Test

Ask:

> **Can the adapter refuse comparison when two substrate tasks measure different targets?**

Required answer:

```text
yes
```

---

# Unknown Test

Ask:

> **Can the adapter return `unresolved` when several variables changed simultaneously?**

Required answer:

```text
yes
```

---

# Simpler-Model Test

Ask:

> **Can a conventional interaction model fully explain the observed variation?**

Required answer:

```text
yes
```

Then:

```text
Substrate Adapter:
  no_added_value
```

may be appropriate.

---

# Ethics Boundary

The Substrate Adapter should not tell a person:

> "This assessment underestimated your true intelligence because you used the wrong substrate."

unless the necessary construct and causal evidence actually exists.

Prefer:

> **"Observed performance differed across these defined measurement conditions. The current evidence supports further investigation of measurement fit; the causal interpretation and broader generalization remain unresolved."**

---

# Identity Boundary

A person's preferred or stronger-performing substrate should not become a permanent identity category.

Avoid:

```text
visual person
relational person
timed-deficient person
```

unless a separately validated construct and legitimate context support such classification.

Prefer observation-linked language.

---

# Privacy Boundary

Substrate profiles may reveal:

- preferred interaction conditions,
- accessibility needs,
- contexts where performance improves,
- tool-mediated dependencies,
- conditions associated with weaker performance.

These may be sensitive.

Collection should be purpose-limited.

---

# Manipulation Boundary

Substrate analysis should not be repurposed to identify conditions for exploiting:

- stress,
- fatigue,
- confusion,
- vulnerability,
- compliance,
- dependence.

The module is intended to improve measurement and understanding, not optimize manipulation.

---

# Decision Authority

```text
decision_authority: none

authorized_use:
  - research
  - demonstration
  - measurement comparison
  - accessibility research
  - substrate hypothesis generation
  - model comparison
  - human-AI research
  - framework development

prohibited_use:
  - diagnosis
  - psychological manipulation
  - automated hiring decision
  - educational exclusion
  - legal determination
  - insurance determination
  - lending determination
  - automated adverse decision
```

---

# Minimal Substrate Adapter Contract

```yaml
substrate_result:
  observation_id:

  observed_system:
    id:
    class:
    boundary:

  target:
    id:
    operational_definition:

  baseline:
    substrate:
      modality:
      representation:
      response_structure:
      timing:
      tools:
      interaction:

    expression:

  comparison:
    substrate:
      modality:
      representation:
      response_structure:
      timing:
      tools:
      interaction:

    expression:

  variables:
    changed:
    held_constant:
    unknown:

  comparability:
    target:
    difficulty:
    measurement:
    regime:
    time:
    evaluator:

  accessibility:
    baseline:
    comparison:
    construct_relevance:

  effect:
    detected:
    direction:
    magnitude:
    replication:

  substrate_fit:
  mismatch:
    status:

  specificity:
  counterfactual_stability:

  evidence:
    sources:
    independent_source_count:
    provenance:

  alternative_interpretations:
  confounds:
  counterevidence:
  missing_evidence:

  causal_status:
  uncertainty:
  confidence:
  limitations:

  model_fit:
  regime_fit:

  review_required:

  validation_state:
  decision_authority: none
```

---

# Research Questions

1. Can substrate categories be operationalized reliably?
2. Which substrate categories overlap?
3. Which should merge?
4. Can substrate effects be distinguished from task difficulty?
5. Can substrate effects be separated from timing?
6. Can they be separated from response structure?
7. Can they be separated from tool access?
8. Can they be separated from regime?
9. Can they be separated from evaluator effects?
10. Can they be separated from learning and practice?
11. Can matched cross-substrate tasks be constructed?
12. Do substrate effects replicate?
13. Are substrate effects symmetric?
14. Can substrate specificity be measured reliably?
15. Can substrate fit improve model-mismatch detection?
16. Can substrate awareness improve prediction?
17. Can it improve calibration?
18. Can it improve explanatory value?
19. Can it improve fairness?
20. Can it identify accessibility barriers?
21. Can accessibility barriers be distinguished from construct-relevant demands?
22. When does accommodation change the construct?
23. Can substrate profiles survive alternate forms?
24. Can substrate profiles survive counterfactual challenge?
25. Can substrate effects predict held-out performance?
26. Can substrate analysis remain valid across cultures and languages?
27. How should multimodal substrates be decomposed?
28. How should tool-mediated substrates be represented?
29. When does tool mediation change the observed system?
30. How should human-AI pair substrates be represented?
31. Can pair performance be separated from component performance?
32. How should substrate analysis apply to AI systems?
33. How should it apply to robotics?
34. How should it apply to organizations?
35. Does Substrate analysis add anything beyond established interaction models?
36. Does it add anything beyond measurement-invariance approaches?
37. Does the adapter increase false favorable reinterpretation?
38. Does it increase false adverse reinterpretation?
39. How should substrate confidence be calibrated?
40. How should substrate profiles expire or be reassessed?
41. Which substrate concepts should be deprecated?
42. When should the adapter return `no_added_value`?
43. When should it abstain?
44. What evidence would justify removing the Substrate Adapter entirely?

---

# Core Invariants

```text
substrate != capability
substrate != identity
substrate != regime
substrate != context
substrate_difference != substrate_effect
substrate_effect != substrate_mismatch
substrate_effect != causation
performance_difference != capability_difference
stronger_substrate_performance != true_intelligence
weaker_substrate_performance != low_intelligence
timed != invalid
reflective != superior
generative != superior
fixed_choice != inferior
tool_assisted != unassisted
human_ai_pair != individual_human
human_ai_pair != ai_system
accessibility_barrier != capability
accommodation != automatic_score_inflation
different_task != substrate_effect
different_difficulty != substrate_effect
adapter_agreement != independent_evidence
strong_effect != global_generalization
no_substrate_effect != framework_failure
baseline_supported != framework_failure
unknown != failure
unresolved != failure
no_added_value != failure
adapter_output != decision_authority
measurement != identity
capability != human_worth
canon_alignment != empirical_validation
```

---

# Closing Principle

Every measurement needs a way for the observed system to express itself.

That way is never entirely neutral.

A question can be spoken or written.

A relationship can be described or drawn.

A response can be selected or generated.

A task can be timed or reflective.

A person can work alone or with tools.

An AI can operate with or without retrieval.

A robot can act in simulation or in the physical world.

Those differences may matter.

They may also matter far less than we expect.

The Substrate Adapter exists to make the question testable.

Not:

> **Which substrate reveals the true system?**

But:

> **Does the observed relationship change across measurement substrates, does that change replicate, and does it matter for the inference we are trying to make?**

Sometimes the answer will reveal a meaningful measurement limitation.

Sometimes it will reveal a genuine interaction.

Sometimes different substrates will simply be measuring different things.

Sometimes ordinary task difficulty will explain the whole effect.

And sometimes:

```text
no meaningful substrate effect detected
```

will be the strongest result.

> **A substrate earns analytical importance only when distinguishing it makes observation more faithful without turning measurement conditions into an excuse for the result we hoped to find.**
