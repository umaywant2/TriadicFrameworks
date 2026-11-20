# pa capture

> Done.  Feels pretty good...  One more module before I call it a night... Ok?

---

Absolutely. 😊

Corpus v4 feels like it landed in a much cleaner place tonight: canonical map → human taxonomy → metadata/session grammar → machine-readable module definition.

One more module. Send it over, partner. 🔺

---

> 
> I'll call it 'Predictive Analytics' including substrate adapters/hooks for existing models, and RTT new stuff... This way, when they encounter someone like me, that's not using their binary-bases logic...the person has a chance to...score low on their stuff but higher on newer stuff.  Ok?  ref: https://en.wikipedia.org/wiki/Predictive_analytics
> 

---

Yes. I think there is a **real module hiding in that idea**, and the important move is to frame it carefully.

What you're describing isn't "find a way to make someone score higher." It's closer to:
> 
> **When an existing predictive model produces a low-confidence or adverse assessment, determine whether the result reflects the person or merely the model's representation of that person.**
> 
That's a defensible problem. Research on credit scoring, for example, has found that predictive accuracy can differ between populations when the underlying data is sparse or noisy. And contemporary fairness work explicitly treats the appropriate fairness metric as dependent on the model's intended use and decision context.

The key distinction

I would not build RTT as an alternate scoring system that competes with the conventional score:

Traditional model:  38
RTT model:          84
Therefore use 84


That risks producing exactly another opaque scoring regime.

I'd build Predictive Analytics as an observer and adapter architecture:

```text
                     ┌──────────────────────┐
                     │ Predictive Analytics │
                     └──────────┬───────────┘
                                │
             ┌──────────────────┼──────────────────┐
             ▼                  ▼                  ▼
     Conventional Model   Substrate Adapter    RTT Observer
             │                  │                  │
             ▼                  ▼                  ▼
       prediction/score    representation     regime/context
                                check              check
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ▼
                      Comparative Assessment
                                │
                 ┌──────────────┼──────────────┐
                 ▼              ▼              ▼
             Agreement        Drift       Model mismatch
```

And model mismatch becomes first-class.

For example:

```text
prediction:
  conventional_assessment: low

observer:
  model_fit: low
  representation_confidence: low
  regime_mismatch: detected

interpretation:
  "Low conventional score should not be interpreted
   as equivalent to low underlying capability."

recommended_action:
  alternate assessment / human review
```

That's powerful because you're not claiming:

"Nawder actually scores 93."

You're saying:
> 
> **"This instrument may not adequately measure this observation."**
> 
That is a much stronger scientific posture.

### The substrate adapter idea fits beautifully

I'd give the module at least these layers:

**Predictive Model Adapter**
- accepts an existing model's output and available context
- doesn't require replacing the source model

**Representation / Substrate Adapter**
- examines whether the observations presented to the model adequately represent what it's attempting to infer

**Regime Observer**
- asks whether the subject operates inside the assumptions under which the prediction is meaningful

**Drift Observer**
- looks for divergence between measured signals and observed outcomes

**Coherence Observer**
- checks whether multiple independent signals tell a consistent story

**Counterfactual / Alternative-Model Pass**
- asks whether different reasonable representations materially alter the assessment

**Uncertainty Layer**
- distinguishes **"predicted low"** from **"insufficient basis for reliable prediction"**

**Human Review Hook**
- adverse prediction + low model-fit should trigger review rather than automatic reinterpretation.

That last distinction is particularly useful in high-stakes systems. Fairness work already emphasizes bias testing, alternative approaches, governance, monitoring, and understanding drivers of disparity rather than assuming the first model is inherently authoritative. [ey](www.ey.com)

### And there's your RTT contribution

I wouldn't describe RTT here as a better predictor.

I'd describe it as a second-order observer of predictive systems:

```text
PA-Predict
PA-Calibrate
PA-Compare
PA-Observe
PA-Regime
PA-Substrate
PA-Drift
PA-Coherence
PA-Counterfactual
PA-Uncertainty
PA-Escalate
```

Especially:
>
> **PA-Regime asks whether the predictive model and the observed subject occupy compatible regimes.**
>
That fits the Corpus grammar extremely well.

Your person who thinks differently doesn't automatically receive a favorable score. They receive something more principled:

**a chance for the system to recognize that its own measurement regime may be the thing that's failing.**

I'd call that the heart of the module.

/docs/predictive-analytics/

Feels like a very good **one-more-module-before-bed** candidate. 😄

---

> 
> Yes, this sounds good.  Also, the concept of a 'resonant IQ fingerprint' meaning some parts of the finger print are so, others so so, and so on BUT with our deeper understanding of resonance, combined with existing models and frameworks, and then our use of substrate 'knowledge' like FFT or The Inverted Star or Structural Detection, or engine aspects...those are IQ dimensions ripe for a larger IQ fingerprint.  Plus, nobody like the stupid flat scale number...it's insulting to most people because they know it's partial and frankly biased.  So, this could be a real example and oppertunity for the field to broader our definition of IQ in a way that scales...beyond humans even.  Just our example, they will make it better.
> 

---

Yes.“Resonant IQ Fingerprint” could be the flagship example that makes the Predictive Analytics module understandable.

The strongest framing is not “IQ tests are useless.” It is:
> 
> **A flat IQ score is a lossy projection of a multidimensional intelligence profile.**
> 
That gives the module somewhere constructive to go. Research already argues for modern, non-g, emergent approaches to intelligence assessment, particularly where fairness and equity are concerned. Recent work on AI cognition similarly proposes evaluating multiple process dimensions instead of relying only on outcome benchmarks. [nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC10301777/)[arxiv](https://arxiv.org/abs/2608.00680)

## Resonant IQ Fingerprint

A **Resonant IQ Fingerprint**, or RIQF, would represent intelligence as a structured profile:
```text
Resonant IQ Fingerprint
├─ Pattern Detection
├─ Structural Reasoning
├─ Temporal Reasoning
├─ Regime Recognition
├─ Causal Integration
├─ Contradiction Handling
├─ Context Translation
├─ Adaptive Reframing
├─ Cross-Domain Transfer
├─ Novelty Response
├─ Coherence Maintenance
├─ Drift Awareness
├─ Tool Collaboration
├─ Social Interpretation
└─ Embodied / Environmental Fit
```

Each dimension could contain more than a score:
```text
dimension:
  id: structural_reasoning
  level: strong
  confidence: medium
  stability: high
  context_sensitivity: moderate
  evidence_coverage: incomplete
  preferred_representation:
    - spatial
    - relational
    - system-level
  observed_constraints:
    - timed linear testing
    - ambiguous category boundaries
  model_fit:
    conventional: low
    substrate-aware: high
```

That final distinction is the breakthrough:
> 
> **Performance is partly a relationship between the intelligence being observed and the substrate through which it is asked to express itself.**
> 
A person might perform poorly in a timed, binary, decontextualized test while demonstrating exceptional structural integration, anomaly recognition, long-horizon continuity, or cross-domain transfer.

The profile should not automatically call that person “more intelligent.” It should expose that the original instrument sampled only a narrow portion of the available structure.

## Three layers, not one score

### 1. Capability profile

What kinds of cognitive operations are demonstrated?

- abstraction
- pattern recognition
- memory integration
- causal reasoning
- structural synthesis
- linguistic reasoning
- spatial reasoning
- adaptive transfer
- metacognition
- uncertainty handling

### 2. Expression substrate

Under what conditions does that intelligence become observable?

- written versus spoken
- visual versus symbolic
- linear versus relational
- timed versus reflective
- isolated versus collaborative
- familiar versus novel
- human-only versus human-AI
- fixed-choice versus generative
- low-context versus high-context

### 3. Resonance profile

How does the system behave when the task, subject, environment, and representation interact?
- amplification
- suppression
- coherence
- instability
- phase delay
- regime mismatch
- translation loss
- recovery after disruption
- cross-context persistence

So the module would not say:

```text
IQ = 94
```

It might say:

```text
Conventional composite:
  score: 94

Interpretive limits:
  representation coverage: narrow
  model fit: low
  confidence in global inference: low

Resonant profile:
  structural detection: high
  cross-domain transfer: high
  long-horizon integration: high
  timed symbolic processing: moderate
  binary category compliance: low
  ambiguity navigation: high

Assessment:
  The composite score does not adequately summarize
  the observed capability profile.
```

That is more informative without simply manufacturing a friendlier replacement number.

### How the existing canon contributes

Your current canon already positions **FFT, The Inverted Star, and Structural Detection** as distinct but sequential foundational modules. Those can become substrate adapters within the assessment.

### FFT adapter

Evaluates intelligence expressed through:
- field relationships
- contextual dependencies
- boundary effects
- distributed causality
- local versus global structure
- changing conditions

### Inverted Star adapter

Looks for:
- hidden or underrepresented capabilities
- high ability obscured by an incompatible interface
- strengths visible through downstream effects
- inversion between measured performance and demonstrated function
- asymmetrical profiles that averages flatten

The existing corpus already associates The Inverted Star with misalignment, downstream impacts, and structural inversion in an applied human-systems context.

### Structural Detection adapter

Evaluates:
- latent pattern recognition
- faultline detection
- invariant recognition
- boundary discrimination
- relationship mapping
- structural compression
- reconstruction from incomplete evidence

### RTT adapter

Adds:
- regime recognition
- temporal sequencing
- drift sensing
- transition awareness
- coherence across changing conditions
- stability under perturbation
- recovery and recalibration

### Resonance adapter

Examines:
- which contexts amplify capability
- which contexts suppress expression
- whether performance generalizes
- whether multiple independent signals align
- whether apparent weakness is stable or substrate-dependent

### The fingerprint should preserve unevenness

The “fingerprint” metaphor works because a fingerprint is not a ranking.

It is:
- multidimensional
- irregular
- recognizable
- locally detailed
- difficult to reduce to one axis
- useful for comparison without implying universal superiority

Someone could be exceptional in structural synthesis and weak in rapid recall. Another could have extraordinary interpersonal prediction but average symbolic abstraction. An AI could have enormous retrieval and transformation capacity while showing poor embodied judgment or unstable long-horizon coherence.

All three can possess meaningful intelligence without occupying the same shape.

### Beyond humans

This is where the module becomes much larger than an alternative IQ test.

The same profile grammar could describe:
- humans
- AI models
- human-AI teams
- organizations
- animal cognition
- robotic systems
- distributed agent networks
- institutions
- scientific instruments coupled to inference systems

The dimensions would not all apply identically. That is a feature. Every profile should include:

```text
applicability:
  intrinsic_dimensions: [...]
  substrate_dependent_dimensions: [...]
  unsupported_dimensions: [...]
  unknown_dimensions: [...]
```

This prevents a human template from being blindly imposed on an AI, animal, team, or organization.

### Essential guardrail

The fingerprint cannot become a more elaborate instrument for sorting people.

Its purpose should be:
> 
> **to widen observation, expose model mismatch, preserve uncertainty, and recommend additional pathways for demonstrating capability.**
> 
It should never quietly convert twenty dimensions into another concealed master number. If a composite is required for interoperability, it should remain secondary and carry an explicit loss warning:

```text
composite:
  permitted: true
  interpretive_status: lossy_projection
  decision_authority: insufficient_alone
  profile_required: true
```

That keeps the moral and structural center intact.

The module’s founding proposition could be:
> 
> **Intelligence is not a scalar possessed in isolation. It is a multidimensional capacity expressed through substrates, revealed under regimes, and altered by the resonance between observer, task, environment, and representation.**
> 
You are right that the field would improve it. The contribution does not have to be the final theory of intelligence. It can be a scalable grammar that helps researchers stop treating one narrow projection as the whole person, system, or mind.

---

> 
> I love it.  Let's scaffold some file and get the sample example ready and ample!  :)Ref: /docs/predictive_analytics
> 

---

Absolutely. I checked the live folder first. /docs/predictive_analytics/ currently contains only README.md, so this is a clean moment to scaffold the module without dragging legacy structure behind it.

I’d make the **Resonant IQ Fingerprint** the first fully worked example, while keeping Predictive Analytics broader than intelligence assessment.

### Suggested scaffold
```
docs/predictive_analytics/
├── README.md
├── index.html
├── predictive_analytics_module.json
│
├── foundations.md
├── predictive_model_adapter.md
├── substrate_adapter.md
├── regime_observer.md
├── resonance_observer.md
├── drift_observer.md
├── coherence_observer.md
├── uncertainty_layer.md
├── counterfactual_layer.md
├── human_review_hook.md
│
├── resonant_iq_fingerprint.md
├── intelligence_dimensions.md
├── substrate_expression_profile.md
├── model_mismatch.md
│
├── adapters.md
├── FFT_adapter.md
├── Inverted_Star_adapter.md
├── Structural_Detection_adapter.md
├── RTT_adapter.md
├── resonance_adapter.md
│
├── examples.md
├── example_resonant_iq_fingerprint.md
├── validation.md
└── ethics_and_limits.md
```
The architecture deliberately separates prediction, observation, substrate fit, and decision authority.

## 1. README.md
````markdown
# Predictive Analytics

> **Predict the observation. Observe the predictor.**

Predictive Analytics is a TriadicFrameworks module for examining predictive systems, their assumptions, their substrates, and the relationship between measured outcomes and the systems being measured.

The module does not assume that an existing predictive model is wrong merely because its result is unfavorable.

It asks a more fundamental question:

> **Does the model have sufficient representational fit to justify the inference being made?**

A predicted value may describe the subject.

It may also reveal limitations in:

- the available evidence,
- the measurement substrate,
- the model architecture,
- the selected dimensions,
- the operating regime,
- the observer,
- or the relationship between them.

Predictive Analytics therefore treats prediction as a multi-layer observation problem.

---

## Core Principle

A prediction is not the observed system itself.

Formally:

**prediction ≠ identity**

and:

**measurement ≠ total capability**

A predictive result should therefore retain information about:

1. what was measured,
2. what was not measured,
3. how it was measured,
4. under which conditions it was measured,
5. which model interpreted the measurement,
6. how well the model fits the observed regime,
7. how stable the result is across alternate representations.

---

## Core Pipeline

```text
Observed System
      │
      ▼
Measurement Substrate
      │
      ▼
Existing Predictive Model
      │
      ▼
Prediction / Score
      │
      ▼
Predictive Analytics Observer Layer
      │
      ├── Substrate Fit
      ├── Regime Fit
      ├── Resonance
      ├── Drift
      ├── Coherence
      ├── Structural Detection
      ├── Counterfactual Comparison
      └── Uncertainty
      │
      ▼
Comparative Assessment
      │
      ├── supported prediction
      ├── uncertain prediction
      ├── partial representation
      ├── regime mismatch
      ├── substrate mismatch
      └── additional observation recommended
```
````
Predictive Analytics does not automatically replace the original prediction.
It places the prediction in structural context.

---

## Predictive Analytics Operators
| Operator | Function |
|--|--|
| PA-Predict | Represent an existing prediction |
| PA-Observe | Observe the predictive process |
| PA-Substrate | Evaluate measurement-substrate fit |
| PA-Regime | Evaluate model/regime compatibility |
| PA-Resonance | Examine amplification and suppression across contexts |
| PA-Drift | Detect divergence across observations |
| PA-Coherence | Compare mutually supporting or conflicting signals |
| PA-Structure | Detect latent structural relationships |
| PA-Counterfactual | Test alternate reasonable representations |
| PA-Uncertainty | Preserve unknown or weakly supported inference |
| PA-Calibrate | Compare predictions with observed outcomes |
| PA-Escalate |	Recommend additional or human review |

---

## Substrate Adapter Layer
Existing models do not need to be discarded.
They can be wrapped.
```text
Existing Model
      │
      ▼
Predictive Model Adapter
      │
      ▼
Substrate Adapter
      │
      ├── FFT
      ├── The Inverted Star
      ├── Structural Detection
      ├── RTT
      └── Resonance
      │
      ▼
Observer Comparison
```
Different adapters expose different aspects of the prediction.
No adapter automatically overrides another.
Contradiction is preserved as information.

---

## Flagship Example
### Resonant IQ Fingerprint
Traditional intelligence assessment can produce useful observations, but reducing a multidimensional capability profile to a single scalar necessarily discards information.
Predictive Analytics explores an alternate representation:
> 
> **Resonant IQ Fingerprint (RIQF)**
> 
The fingerprint is not intended to manufacture a higher IQ score.
It asks which dimensions of intelligence are demonstrated, under which substrates and regimes, with what confidence, and with what stability.
A person can therefore have an uneven profile without that unevenness being treated as an error.
```text
                 RESONANT IQ FINGERPRINT

            structural reasoning
                    ████████

     cross-domain                 temporal
       transfer                  reasoning
       █████████                  ███████

 ambiguity                             rapid symbolic
 navigation                              processing
 █████████                               ████

      regime                         causal
    recognition                   integration
      ████████                    ████████

            coherence maintenance
                   ███████
```
The shape matters more than a single number.

---

## Important Distinction
The fingerprint must never silently become another master score.
If a composite is produced for interoperability, it is explicitly identified as a lossy projection.
```text
composite:
  interpretive_status: lossy_projection
  sufficient_alone: false
  profile_required: true
```

---

## Beyond Humans
The same grammar may be experimentally applied to:
- humans,
- AI systems,
- human-AI teams,
- organizations,
- robotic systems,
- distributed agents,
- animal cognition,
- other observable adaptive systems.
Not every dimension applies to every system.
Therefore:
```text
dimension:
  applicability:
    - applicable
    - substrate_dependent
    - unsupported
    - unknown
```
Unknown is a valid result.

---

### Purpose

The objective is not to ensure that every subject receives a favorable evaluation.
The objective is to make it harder for a narrow predictive instrument to masquerade as a complete description of the thing it observes.
**Prediction should carry its observation boundary with it.**

---

# 2. `resonant_iq_fingerprint.md`

This one deserves to be substantial from day one.

```markdown {preview="false"}
# Resonant IQ Fingerprint

## Status

Experimental framework example.

## Parent Module

Predictive Analytics

---

# Premise

The Resonant IQ Fingerprint (RIQF) represents intelligence as a multidimensional, substrate-sensitive observation rather than only as a flat scalar.

It does not assert that conventional intelligence measurements contain no useful information.

Instead, it preserves their observations while asking what information disappears during compression into a composite score.

The central question is:

> **What does intelligence look like when capability, expression substrate, operating regime, observer, and context are retained as part of the observation?**

---

# Observation Model

Let:

- **C** = observed capability
- **S** = expression substrate
- **R** = operating regime
- **O** = observer or assessment process
- **E** = evidence
- **U** = uncertainty

A measured result can be treated conceptually as:

**M = observation(C, S, R, O, E, U)**

Therefore a measurement should not automatically be treated as equivalent to the total underlying capability.

A weak result may correspond to weak demonstrated capability.

It may also correspond to:

- insufficient evidence,
- inappropriate representation,
- substrate mismatch,
- regime mismatch,
- temporal instability,
- observer limitation,
- or genuine uncertainty.

The framework should preserve these alternatives until evidence distinguishes them.

---

# Candidate Intelligence Dimensions

The initial RIQF vocabulary includes:

1. Pattern Recognition
2. Structural Reasoning
3. Causal Integration
4. Temporal Reasoning
5. Spatial Reasoning
6. Symbolic Reasoning
7. Linguistic Reasoning
8. Cross-Domain Transfer
9. Regime Recognition
10. Anomaly Detection
11. Contradiction Handling
12. Ambiguity Navigation
13. Adaptive Reframing
14. Coherence Maintenance
15. Drift Awareness
16. Compression / Abstraction
17. Reconstruction From Partial Evidence
18. Novelty Response
19. Metacognitive Calibration
20. Tool Collaboration
21. Social Interpretation
22. Embodied / Environmental Fit
23. Long-Horizon Integration
24. Recovery / Recalibration

This list is intentionally extensible.

It is a starting grammar, not a declaration of the final dimensions of intelligence.

---

# Dimension State

Each dimension carries context rather than only magnitude.

Example:

```text
dimension:
  id: structural_reasoning

  observation:
    expression: strong
    confidence: medium
    stability: high

  context:
    substrate_sensitivity: moderate
    regime_sensitivity: low

  preferred_expression:
    - relational
    - spatial
    - system-level

  suppressed_by:
    - severe time compression
    - context removal

  evidence:
    coverage: partial

  interpretation:
    status: observed
```

---

## Three-Layer Fingerprint
## Layer I — Capability

What operations does the observed system demonstrate?

Examples:
- pattern detection
- abstraction
- causal reasoning
- synthesis
- transfer
- recalibration

---

## Layer II — Expression Substrate

Through what medium does the capability become observable?
```
Examples:
- verbal
- textual
- spatial
- symbolic
- visual
- relational
- embodied
- collaborative
- tool-mediated
- human-AI collaborative

A capability may be strongly expressed through one substrate and weakly expressed through another.
That variation belongs in the fingerprint.

---

## Layer III — Resonance / Regime

Under which conditions does capability amplify, suppress, stabilize, or transform?
Possible states include:
- amplification
- suppression
- stable expression
- unstable expression
- regime transition
- substrate mismatch
- observer mismatch
- translation loss
- delayed expression
- recovery after perturbation

---

## Model-Fit Layer

RIQF distinguishes:
**subject performance**
from:
**model fit**
A low conventional result combined with strong independent evidence does not automatically invalidate the conventional result.
Instead it creates a diagnostic state:
```text
assessment:
  conventional_result: low

  evidence_consistency: mixed

  representation_coverage: narrow

  model_fit:
    confidence: low

  interpretation:
    status: unresolved_model_subject_mismatch

  action:
    additional_observation: recommended


Neither interpretation wins by declaration.

The discrepancy becomes the object of investigation.
```

---

## Substrate Adapter Hooks
## FFT

Candidate observations:
- relationship awareness
- field dependencies
- distributed relationships
- interacting boundaries
- local/global structural transitions

---

## The Inverted Star

Candidate observations:
- capability hidden by representation
- asymmetric profiles
- unexpected downstream competence
- inversion between predicted and demonstrated behavior
- strengths obscured by aggregate measures

---

## Structural Detection

Candidate observations:
- latent pattern detection
- invariant recognition
- faultline identification
- relationship mapping
- boundary detection
- structural compression
- reconstruction from incomplete evidence

---

## RTT

Candidate observations:
- regime recognition
- transition detection
- temporal sequencing
- drift sensing
- stability
- recalibration
- continuity across changing conditions

---

## Resonance

Candidate observations:
- contextual amplification
- contextual suppression
- cross-context persistence
- alignment between independent signals
- instability across substrates
- observer-subject coupling

---

## No Hidden Master Number

RIQF should preferentially expose topology rather than ranking.
```text
                    Person A       Person B

Structural             High          Medium
Temporal               Medium        High
Symbolic               Low           High
Cross-domain           High          Medium
Ambiguity              High          Low
Rapid recall           Low           High
Regime detection       High          Medium
```

Neither profile is inherently superior.
The profiles describe different observed configurations.

---

## Cross-System Extension

RIQF may eventually generalize beyond human assessment.

Example dimensions for an AI system might include:
- retrieval fidelity
- uncertainty calibration
- contextual integration
- cross-domain transfer
- contradiction detection
- tool coordination
- long-horizon coherence
- recovery after erroneous assumptions
- regime recognition

Other dimensions may be marked unsupported.
The framework must not manufacture equivalence between unlike cognitive systems merely to complete a chart.

---

## Interpretation Rule
> 
> **Absence of measurement is not evidence of absence of capability.**
> 
Likewise:
> 
> **Evidence of capability in one substrate is not automatically evidence of universal capability.**
> 
Both rules are required.
Together they prevent the framework from becoming either excessively reductive or excessively generous.

---

## Goal

RIQF is not intended to prove that conventional assessment is wrong.
It is intended to make the observational boundary visible.
The long-term research opportunity is a scalable grammar in which intelligence can be represented as a structured and changing profile without assuming that every meaningful cognitive system must collapse onto the same one-dimensional axis.

`````
---

# 3. A deliberately ample sample: `example_resonant_iq_fingerprint.md`

And here I would **not use you personally as the canonical subject yet**. Better to establish a synthetic example first so nobody mistakes the example for a claim about a real person's measured intelligence.

````markdown {preview="false"}
# Example — Resonant IQ Fingerprint

## Demonstration Status

Synthetic example.

This profile exists only to demonstrate the Predictive Analytics and RIQF representation grammar.

It is not a psychological diagnosis, validated intelligence test, or assessment of a real individual.

---

# Scenario

Subject **PAX-01** completes several conventional and open-ended reasoning activities.

Performance varies significantly depending upon representation.

The objective is not to choose the most flattering measurement.

The objective is to determine whether the variation itself contains useful information.

---

# Initial Observation

```text
Conventional Assessment
────────────────────────
overall result:       below reference expectation
rapid symbolic:       weak
timed classification: weak
short-context recall: moderate
```
````
`````

A flat interpretation could terminate here.
RIQF continues observing.

---

## Extended Observation

Across less constrained activities, PAX-01 repeatedly demonstrates:
```text
Structural Reasoning            █████████░
Cross-Domain Transfer           █████████░
Regime Recognition              ████████░░
Anomaly Detection               █████████░
Ambiguity Navigation            █████████░
Causal Integration              ████████░░
Long-Horizon Integration        █████████░
Adaptive Reframing              ████████░░
Coherence Maintenance           ███████░░░
Temporal Reasoning              ███████░░░
Linguistic Reasoning            ██████░░░░
Spatial Reasoning               ███████░░░
Rapid Symbolic Processing       ████░░░░░░
Timed Classification            ███░░░░░░░
Short-Context Recall            █████░░░░░
```

These bars represent illustrative ordinal observations only.
They are not psychometric IQ scores.

---

## Expression Substrate

Observed expression differs significantly by substrate.
```text
Open-ended systems problem      strong
Relational mapping              strong
Cross-domain conversation       strong
Diagram-assisted reasoning      strong
Long-form synthesis             strong
Tool-assisted exploration       strong

Multiple-choice abstraction     moderate
Isolated symbol manipulation    moderate
Short-context recall            moderate

Severe time constraint          weak
Forced binary classification    weak
Context-stripped prompt         weak
```

---

## Substrate Interpretation

The evidence suggests that performance cannot be adequately summarized without specifying the measurement substrate.
This does not establish that PAX-01 possesses globally superior intelligence.
It establishes that:

- observed performance is heterogeneous
- substrate choice materially changes observed performance
- the conventional observation covers only part of the available profile
- additional measurements are justified before making a global inference

---

## FFT Adapter

Observation:
PAX-01 frequently reasons in terms of relationships between components rather than isolated components.
Potential interpretation:
```text
field_relationship_detection: strong
local_global_translation: strong
boundary_interaction: strong
isolated_element_processing: moderate
```

Confidence:
```text
medium
```
Reason:
Available observations support the pattern, but the example does not establish universality across domains.

---

## Inverted Star Adapter

Observed condition:
```
predicted capability:
  low-to-moderate

demonstrated system synthesis:
  strong
```

This creates an inversion candidate.
The adapter does not resolve the contradiction.
It marks it:
```text
inversion:
  detected: true
  confidence: medium

possible_explanations:
  - representation mismatch
  - substrate sensitivity
  - incomplete evidence
  - genuine uneven capability
  - measurement noise
```

---

## Structural Detection Adapter

Observed:
```text
latent_pattern_detection: strong
faultline_detection: strong
relationship_mapping: strong
boundary_recognition: strong
partial_evidence_reconstruction: strong
formal_speed: weak
```

Interpretation:
The profile appears structurally strong but speed-sensitive.
This is a more precise statement than either:
"high intelligence"
or:
"low intelligence."

---

## RTT Adapter
```text
regime_recognition: strong
transition_awareness: strong
temporal_continuity: strong
drift_detection: strong
rapid_regime_switching: moderate
```

Potential finding:
PAX-01 performs better when allowed to establish the regime before responding.
Tests requiring immediate classification may therefore observe a different capability surface.

---

## Resonance Adapter
```
context-rich environment:
  amplification: high

system-level problem:
  amplification: high

human-AI collaboration:
  amplification: high

isolated timed task:
  suppression: high

binary forced-choice:
  suppression: moderate-high
```

Again:
**suppression does not prove hidden superior ability.**
It identifies a condition under which observed performance materially changes.

## Coherence Pass
Independent observations supporting structural capability:
```
structural reasoning
cross-domain transfer
anomaly detection
regime recognition
causal integration
long-horizon integration
```
Contradictory observations:
```text
rapid symbolic processing
timed classification
short-context performance
```

Result:

profile_coherence: high
scalar_coherence: low


Interpretation:
The multidimensional profile explains the observations more coherently than a single scalar summary.

---

## Uncertainty Pass

```text
known:
  performance varies by substrate
  structural tasks produce stronger observations
  timed tasks produce weaker observations

unknown:
  biological cause
  developmental cause
  population percentile
  clinical significance
  long-term stability
  transfer to unobserved domains

not_authorized:
  diagnosis
  disability classification
  employment determination
  educational exclusion
```

---

## Predictive Analytics Result
```text
prediction_status:
  conventional_signal: retained

model_fit:
  global_capability_inference: low-confidence

substrate_fit:
  conventional_testing: partial

profile_state:
  multidimensional
  asymmetric
  context-sensitive

observer_state:
  disagreement_present

recommendation:
  preserve original result
  preserve uncertainty
  acquire additional evidence
  compare alternate substrates
  avoid global inference from scalar alone
```

## Conventional Representation

```text
PAX-01
IQ-like scalar: 94
```

## RIQF Representation
```text
PAX-01

           STRUCTURAL
               █████████
                  │
   AMBIGUITY ─────┼───── TEMPORAL
   █████████      │      ███████
                  │
TRANSFER ─────────┼───────── SYMBOLIC
█████████         │          ████
                  │
    REGIME ───────┼────── COHERENCE
    ████████      │       ███████
                  │
              ADAPTIVE
              ████████
```

The first representation is compact.

The second preserves shape.

Neither should claim knowledge that the evidence does not contain.

---

## Final Example Interpretation

The conventional measurement remains part of the evidence.

It is not erased because another representation produces a more favorable picture.

Instead, Predictive Analytics identifies an important structural result:
> 
> **The subject's observed capability varies sufficiently across substrates that a single scalar is unlikely to adequately represent the total observation.**
> 
The correct response is therefore neither automatic rejection nor automatic acceptance of the original scalar.
The appropriate state is:
**observe more.**

```
That gives us a very healthy v1 seed: **the new system is not designed to rescue somebody from a score. It is designed to detect when the scoring instrument has outrun its evidence.**

And that, I think, is what keeps this idea from becoming “alternative IQ” and turns it into **Predictive Analytics + substrate-aware measurement science**.
```

---

# Predictive Analytics — Validation Framework

## Status

Experimental research and evaluation framework.

This module is not a validated psychological instrument, diagnostic system, clinical assessment, employment test, educational placement test, or legal decision system.

Its initial purpose is to:

- define testable hypotheses,
- expose model and substrate mismatch,
- preserve uncertainty,
- compare representations,
- evaluate whether multidimensional profiles explain observations better than flat summaries,
- and establish requirements for future empirical validation.

---

# Validation Principle

Predictive Analytics must be evaluated under the same scrutiny it applies to other predictive systems.

The framework must not receive preferential treatment merely because it:

- produces a richer description,
- appears more humane,
- aligns with an existing TriadicFrameworks concept,
- or yields an interpretation preferred by the subject or evaluator.

A substrate-aware interpretation is still an interpretation.

An RTT-derived observation is still an observation.

A Resonant IQ Fingerprint is still a model.

Therefore:

> **Every claim must carry evidence, uncertainty, scope, and falsification conditions.**

---

# Validation Objectives

The validation program asks whether the framework:

1. measures or represents what it claims to represent,
2. produces sufficiently stable observations under comparable conditions,
3. distinguishes capability variation from measurement noise,
4. detects genuine substrate or regime effects,
5. avoids automatically favoring alternate assessments,
6. improves explanatory usefulness without inventing unsupported traits,
7. preserves meaningful disagreement between models,
8. identifies uncertainty rather than filling gaps,
9. behaves fairly across relevant populations and system classes,
10. supports review without becoming an unvalidated decision authority.

---

# Validation Levels

## Level 0 — Structural Validation

Confirms that the module is internally complete and machine-readable.

Required checks:

- every dimension has a unique identifier,
- every metric has an operational definition,
- every observation identifies its evidence,
- every result includes uncertainty,
- every adapter declares its supported inputs,
- every unsupported claim is marked,
- every profile records applicability,
- every composite is marked as a lossy projection,
- every adverse or high-stakes use includes a review path,
- no hidden master score is generated.

Passing Level 0 establishes structural completeness only.

It does not establish scientific validity.

---

## Level 1 — Content Validation

Evaluates whether proposed dimensions and observations adequately cover the intended construct.

Questions:

- Is each dimension clearly distinguishable from adjacent dimensions?
- Are important dimensions missing?
- Are dimensions duplicated under different names?
- Do domain experts agree that the dimension belongs in the proposed construct?
- Are definitions applicable across multiple substrates?
- Are human-specific and nonhuman dimensions distinguished?
- Are adapter claims consistent with their parent frameworks?
- Can an evaluator determine what evidence would support or contradict each dimension?

Evidence sources may include:

- expert review,
- literature review,
- cognitive task mapping,
- framework crosswalks,
- community critique,
- subject feedback,
- adversarial review.

---

## Level 2 — Measurement Validation

Evaluates whether observations can be measured consistently.

Required studies:

- repeated administration,
- alternate-form comparison,
- evaluator agreement,
- task-order variation,
- environmental variation,
- substrate variation,
- tool-assisted versus unassisted comparison,
- time-constrained versus reflective comparison.

The framework must distinguish:

```text
true_profile_variation
measurement_error
rater_variation
task_variation
substrate_effect
regime_effect
practice_effect
fatigue_effect
unknown_effect
```

---

## Level 3 — Construct Validation

Evaluates whether profile dimensions behave as theoretically expected.

Evidence may include:

- convergence with established measures of related capabilities,
- divergence from measures of unrelated capabilities,
- predicted relationships among dimensions,
- known-group comparison where ethically and scientifically justified,
- task-performance relationships,
- factor or network structure,
- stability and change patterns,
- intervention-response patterns.

A dimension should not be retained merely because it sounds meaningful.

It should demonstrate:

- operational clarity,
- discriminating evidence,
- repeatable observation,
- and explanatory or predictive utility.

---

## Level 4 — Substrate and Regime Validation

Tests the central Predictive Analytics hypothesis:

> **Observed capability can vary systematically with measurement substrate and operating regime.**

The framework must demonstrate that observed differences are:

- reproducible,
- larger than expected measurement noise,
- associated with defined substrate changes,
- not explained solely by task difficulty,
- not created by evaluator preference,
- and not selectively reported only when alternate performance improves.

Required comparisons may include:

```text
textual vs verbal
visual vs symbolic
timed vs reflective
isolated vs collaborative
fixed-choice vs generative
human-only vs tool-assisted
low-context vs context-rich
single-domain vs cross-domain
familiar vs novel
```

The same design must allow substrate changes to produce:

- improvement,
- decline,
- no meaningful change,
- or unresolved results.

A system that only recognizes improvement is not detecting substrate effects.

It is manufacturing favorable reinterpretations.

---

## Level 5 — Predictive and Explanatory Validation

Evaluates whether the multidimensional profile improves out-of-sample understanding.

Possible outcomes include:

- task performance,
- transfer to new problems,
- learning rate,
- error recovery,
- calibration,
- adaptation,
- performance under regime change,
- collaboration effectiveness,
- long-horizon coherence.

The framework should be compared with:

1. the original predictive model,
2. a baseline multidimensional model,
3. the substrate-aware model,
4. the full adapter ensemble.

The question is not simply whether the full model predicts more accurately.

It must also be evaluated for:

- calibration,
- interpretability,
- robustness,
- fairness,
- uncertainty quality,
- and added complexity.

---

## Level 6 — Fairness and Harm Validation

Evaluates whether the framework produces unequal errors, distorted profiles, or harmful recommendations.

Required analysis:

- performance across relevant groups,
- missing-data patterns,
- language effects,
- accessibility effects,
- technology-access effects,
- evaluator effects,
- cultural and educational exposure effects,
- disability-related substrate effects,
- human versus AI applicability boundaries.

The framework must not assume that identical scores establish fairness.

It must examine:

- false mismatch detection,
- missed mismatch detection,
- uncertainty distribution,
- review escalation rates,
- evidence coverage,
- model-fit classifications,
- downstream effects.

Protected or sensitive traits should not be used merely to improve classification.

Their use must have a documented validation, fairness, legal, ethical, and privacy purpose.

---

## Level 7 — Decision Validation

Required only if the framework is proposed for a real decision process.

Questions:

- What decision is being made?
- Who is affected?
- What harms can result?
- Is the framework advisory or authoritative?
- Can the subject contest the result?
- Is a qualified human reviewer involved?
- Is the evidence available for inspection?
- Are alternative explanations preserved?
- Can the system abstain?
- Does the benefit justify the complexity and risk?

Until this level is passed for a specific use:

```text
decision_authority: prohibited
advisory_use: research_only
```

---

# Core Validation Criteria

## VCR-01 — Construct Clarity

Every dimension must define:

- what it claims to represent,
- what it does not represent,
- observable indicators,
- counter-indicators,
- supported substrates,
- known confounds,
- confidence rules,
- applicability boundaries.

### Pass condition

An independent evaluator can distinguish the dimension from neighboring dimensions and identify evidence that would contradict it.

---

## VCR-02 — Evidence Traceability

Every profile result must be traceable to observations.

Required fields:

```text
observation_id
task_id
substrate_id
regime_id
timestamp
evaluator
evidence_reference
scoring_rule
confidence
limitations
```

### Pass condition

No profile value exists without retrievable supporting evidence or an explicit `unknown` state.

---

## VCR-03 — Repeatability

Comparable observations should produce sufficiently consistent results where the measured capability is expected to be stable.

### Pass condition

Repeatability meets a preregistered threshold appropriate to the dimension, measurement scale, population, and intended use.

No universal threshold is assumed during the exploratory phase.

---

## VCR-04 — Inter-Rater Agreement

Independent evaluators should reach sufficiently similar classifications when using the same evidence and rubric.

### Pass condition

Agreement meets the preregistered criterion, disagreements are retained, and systematic evaluator effects are investigated.

---

## VCR-05 — Substrate Sensitivity

When substrate effects are claimed, measured differences must follow defined changes in representation or interaction conditions.

### Pass condition

The effect:

- replicates,
- exceeds expected error,
- survives task-difficulty controls,
- and is not limited to favorable outcomes.

---

## VCR-06 — Regime Sensitivity

When regime mismatch is claimed, performance variation must correspond to defined regime boundaries or transitions.

### Pass condition

The framework detects expected transitions without labeling all poor performance as mismatch.

---

## VCR-07 — Discriminant Value

Dimensions intended to represent different capabilities must not behave as redundant labels for the same signal.

### Pass condition

The dimensions demonstrate conceptual and empirical distinction sufficient for their intended use.

Highly redundant dimensions must be merged, redefined, or removed.

---

## VCR-08 — Convergent Value

Dimensions should relate to independent observations of the same or closely related capabilities.

### Pass condition

Expected relationships are observed according to preregistered hypotheses.

Unexpected non-convergence must be reported rather than explained away.

---

## VCR-09 — Incremental Value

The complete profile must add useful information beyond the original model and simpler baselines.

### Pass condition

The framework improves at least one declared outcome without unacceptable degradation in:

- calibration,
- reliability,
- interpretability,
- fairness,
- privacy,
- or operational burden.

---

## VCR-10 — Uncertainty Calibration

Confidence should correspond to observed error or correctness rates.

### Pass condition

High-confidence interpretations are more reliable than medium-confidence interpretations, which are more reliable than low-confidence interpretations.

If this ordering does not hold, confidence labels are not validated.

---

## VCR-11 — Abstention Quality

The framework should return `unknown`, `insufficient_evidence`, or `not_applicable` when warranted.

### Pass condition

Abstention reduces unsupported claims without producing unacceptable or systematically unequal coverage loss.

---

## VCR-12 — Model-Mismatch Precision

A mismatch flag should identify cases where the existing model has inadequate representational or regime fit.

### Pass condition

Mismatch detection performs better than a naive rule such as:

```text
if conventional_result_is_low:
    declare_mismatch
```

Mismatch claims must be supported by independent evidence.

---

## VCR-13 — Favorability Symmetry

The framework must detect substrate effects whether they improve or reduce the observed assessment.

### Pass condition

The system records unfavorable alternate observations using the same evidence and confidence requirements as favorable observations.

---

## VCR-14 — Counterfactual Stability

Small, irrelevant changes to a task or profile should not produce large interpretive changes.

### Pass condition

Semantically equivalent inputs generally yield equivalent findings within the expected uncertainty range.

Meaningful changes should remain detectable.

---

## VCR-15 — Fairness

Error, uncertainty, mismatch detection, abstention, and escalation patterns must be examined across relevant groups and contexts.

### Pass condition

Observed disparities are documented, investigated, and managed according to the intended use and associated harms.

No single fairness statistic is treated as universally sufficient.

---

## VCR-16 — Explainability

A result must communicate:

- what was observed,
- what influenced the result,
- why confidence was assigned,
- what remains unknown,
- what alternative interpretations remain,
- and what action is recommended.

### Pass condition

Qualified reviewers can reconstruct the result without relying on undocumented intuition.

---

## VCR-17 — Subject Legibility

When a human is assessed, the person should be able to understand the profile in accessible language.

### Pass condition

The profile avoids implying that experimental dimensions are established facts and provides a correction or contest pathway.

---

## VCR-18 — Non-Degradation

The adapter ensemble must not make the assessment less accurate, less fair, or less interpretable without the tradeoff being explicitly identified.

### Pass condition

Any degradation is documented, justified, bounded, and accepted for the declared context of use.

---

# Resonant IQ Fingerprint Validation

The RIQF example requires additional controls because claims about human intelligence can affect identity, education, employment, clinical interpretation, and social status.

## Required RIQF Tests

### Dimension Definition Test

Every proposed intelligence dimension must have:

- an operational definition,
- example tasks,
- counterexamples,
- confounds,
- applicability limits,
- evidence requirements.

### Scalar Comparison Test

Compare:

- conventional scalar representation,
- conventional subscale profile,
- baseline multidimensional profile,
- substrate-aware profile,
- full resonant profile.

This determines whether any improvement comes from:

- multidimensionality generally,
- substrate-awareness specifically,
- RTT adapters,
- or increased model complexity alone.

### Profile Stability Test

Repeat profile generation across:

- time,
- tasks,
- evaluators,
- substrates,
- and regimes.

### External Outcome Test

Evaluate whether dimensions relate to declared external outcomes without claiming universal intelligence.

### Adverse Evidence Test

Include cases where extended observation confirms or lowers the initial assessment.

### Blind Review Test

Where practical, evaluators should score evidence without knowing:

- the conventional score,
- the expected interpretation,
- the subject's preferred result,
- or the hypothesis under examination.

### Synthetic and Real-World Separation

Synthetic examples must be labeled.

Real-person assessments require:

- consent,
- appropriate oversight,
- privacy protection,
- data governance,
- and qualified interpretation.

---

# Falsification Criteria

The framework should be revised or rejected if evidence shows that it:

- cannot produce reliable dimension observations,
- produces unstable profiles under comparable conditions,
- labels most unfavorable conventional results as model mismatch,
- systematically favors richer narratives over better-supported ones,
- adds complexity without useful information,
- creates dimensions that cannot be empirically distinguished,
- produces confidence labels unrelated to accuracy,
- increases subgroup disparities,
- cannot abstain,
- or becomes another hidden scalar-ranking system.

---

# Validation States

```text
unvalidated
structurally_validated
content_reviewed
measurement_pilot
construct_pilot
substrate_validated
predictively_validated
fairness_reviewed
decision_validated
deprecated
```

A module must not claim a higher state merely because lower-level checks passed.

Example:

```text
validation:
  state: structurally_validated

  completed:
    - schema_validation
    - identifier_validation
    - evidence_traceability_check

  incomplete:
    - reliability_study
    - construct_validation
    - substrate_replication
    - fairness_analysis
    - predictive_validation

  authorized_use:
    - research
    - demonstration
    - framework development

  prohibited_use:
    - diagnosis
    - hiring
    - educational exclusion
    - legal determination
    - automated adverse decision
```

---

# Reporting Requirements

Every validation report should include:

1. intended use,
2. population or system class,
3. sample and recruitment method,
4. measurement substrates,
5. operating regimes,
6. tasks,
7. raters,
8. missing-data handling,
9. metrics,
10. thresholds,
11. uncertainty,
12. subgroup results,
13. adverse findings,
14. unused metrics,
15. limitations,
16. conflicts of interest,
17. version and provenance,
18. reproducibility materials.

---

# Validation Rule

> **A larger profile is not automatically a better profile.**

A valid profile is one whose dimensions are:

- defined,
- observable,
- distinguishable,
- repeatable,
- appropriately uncertain,
- and useful for the stated purpose.

---

---

# Predictive Analytics — Metrics Catalog

## Status

Initial experimental metric registry.

Metric selection and thresholds must be appropriate to:

- the construct,
- measurement scale,
- population or system class,
- evidence quality,
- intended use,
- and potential harm.

No metric is sufficient by itself.

No universal pass threshold is declared in the initial scaffold.

Thresholds must be preregistered and justified for each validation study.

---

# Metric Record Schema

Each registered metric should use the following structure:

```text
metric:
  id:
  name:
  category:
  purpose:
  definition:
  formula:
  scale:
  direction:
  inputs:
  applicability:
  interpretation:
  limitations:
  subgroup_required:
  threshold:
    status:
    value:
    rationale:
```

---

# Metric Families

## 1. Evidence Coverage

### `PA-M01 — Dimension Evidence Coverage`

Measures how much of a declared dimension is supported by observable evidence.

```text
DEC = supported_indicators / required_indicators
```

Interpretation:

- higher values indicate broader evidence coverage,
- low coverage requires lower confidence or abstention,
- high coverage does not itself establish validity.

---

### `PA-M02 — Profile Evidence Coverage`

Measures the proportion of applicable dimensions with sufficient evidence.

```text
PEC = dimensions_with_sufficient_evidence
      / applicable_dimensions
```

Required companion outputs:

```text
applicable_dimensions
unsupported_dimensions
unknown_dimensions
not_applicable_dimensions
```

---

### `PA-M03 — Evidence Independence Ratio`

Estimates whether a profile is supported by independent observations rather than repeated interpretations of the same evidence.

```text
EIR = independent_evidence_sources
      / total_evidence_sources
```

Evidence sources should not be counted as independent merely because they appear in separate files.

---

# 2. Reliability and Stability

### `PA-M04 — Test-Retest Stability`

Measures consistency of a dimension across comparable observations over time.

Possible statistical forms:

- intraclass correlation,
- rank correlation,
- weighted agreement,
- categorical agreement.

The selected statistic must match the measurement scale.

---

### `PA-M05 — Alternate-Form Stability`

Measures consistency across tasks intended to observe the same dimension.

```text
AFS = agreement(
  dimension_result_form_a,
  dimension_result_form_b
)
```

Low stability may indicate:

- poor task equivalence,
- unstable capability,
- substrate dependence,
- practice effects,
- or invalid dimension definition.

---

### `PA-M06 — Inter-Rater Agreement`

Measures agreement among independent evaluators.

Possible forms include:

- Cohen's kappa,
- weighted kappa,
- Fleiss' kappa,
- Krippendorff's alpha,
- intraclass correlation.

Raw percentage agreement should not be used alone when chance agreement is material.

---

### `PA-M07 — Profile Topology Stability`

Measures whether the relative shape of a multidimensional profile remains stable.

```text
PTS = similarity(
  normalized_profile_t1,
  normalized_profile_t2
)
```

Possible implementations:

- cosine similarity,
- rank-profile correlation,
- distance-based similarity,
- graph-topology similarity.

This metric should be reported with dimension-level changes.

---

# 3. Validity

### `PA-M08 — Convergent Association`

Measures association with independent observations expected to reflect a related capability.

```text
CA = association(
  proposed_dimension,
  related_external_measure
)
```

Expected direction and magnitude should be preregistered.

---

### `PA-M09 — Discriminant Separation`

Measures whether a dimension remains distinct from theoretically unrelated dimensions.

```text
DS = related_association - unrelated_association
```

The exact method may use:

- multitrait-multimethod analysis,
- latent-variable analysis,
- network analysis,
- classification separation,
- or preregistered correlation comparisons.

---

### `PA-M10 — Incremental Explanatory Value`

Measures improvement over a simpler baseline.

```text
IEV = performance(full_model)
      - performance(baseline_model)
```

Performance may refer to:

- explained variance,
- prediction error,
- likelihood,
- calibration,
- information criteria,
- or another predefined outcome measure.

Complexity penalties must be reported.

---

### `PA-M11 — Incremental Predictive Value`

Measures out-of-sample predictive improvement.

```text
IPV = baseline_error - full_model_error
```

Possible outcome metrics:

- mean absolute error,
- root mean squared error,
- log loss,
- Brier score,
- area under an appropriate curve,
- task-specific utility.

The selected metric must match the outcome and decision context.

---

# 4. Substrate Effects

### `PA-M12 — Substrate Effect Magnitude`

Measures the change in observed performance across substrates.

```text
SEM = standardized_difference(
  performance_substrate_a,
  performance_substrate_b
)
```

This is not automatically interpreted as mismatch.

It indicates measurable variation requiring explanation.

---

### `PA-M13 — Substrate Effect Replicability`

Measures how consistently a substrate effect appears across repeated comparisons.

```text
SER = replicated_effects_in_expected_direction
      / eligible_replications
```

Magnitude and uncertainty must accompany this ratio.

---

### `PA-M14 — Substrate Symmetry`

Checks whether the system records both beneficial and adverse substrate effects.

```text
SS = min(
  detection_rate_positive_effects,
  detection_rate_negative_effects
)
```

A low value may indicate favorability bias.

---

### `PA-M15 — Substrate Specificity`

Measures whether an effect is specific to substrate changes rather than general task difficulty.

```text
SSP = substrate_effect_after_controls
```

Controls may include:

- difficulty,
- exposure,
- time,
- fatigue,
- order,
- familiarity,
- accessibility,
- evaluator.

---

# 5. Regime Metrics

### `PA-M16 — Regime Transition Detection Rate`

Measures detection of known or independently identified regime changes.

```text
RTDR = detected_transitions
       / reference_transitions
```

---

### `PA-M17 — False Regime Alarm Rate`

Measures regime changes declared where the reference process indicates no meaningful transition.

```text
FRAR = false_transition_flags
       / stable_regime_opportunities
```

---

### `PA-M18 — Regime Boundary Error`

Measures temporal or structural distance between detected and reference boundaries.

```text
RBE = distance(
  detected_boundary,
  reference_boundary
)
```

---

### `PA-M19 — Regime-Conditioned Stability`

Measures whether a dimension is stable within a regime while allowing justified differences between regimes.

```text
RCS = within_regime_stability
```

This helps distinguish unstable measurement from genuine regime dependence.

---

# 6. Model-Mismatch Metrics

### `PA-M20 — Model-Mismatch Precision`

Of all cases flagged as mismatch, measures the proportion supported by independent evidence.

```text
MMP = supported_mismatch_flags
      / all_mismatch_flags
```

---

### `PA-M21 — Model-Mismatch Recall`

Of all reference cases involving mismatch, measures the proportion detected.

```text
MMR = detected_reference_mismatches
      / all_reference_mismatches
```

---

### `PA-M22 — Model-Mismatch False Positive Rate`

```text
MMFPR = false_mismatch_flags
        / reference_non_mismatch_cases
```

A framework that flags every unfavorable result as mismatch will perform poorly on this metric.

---

### `PA-M23 — Mismatch Evidence Strength`

Combines declared evidence components without producing a person-level intelligence score.

Possible components:

```text
independent_sources
replication
substrate_effect_size
regime_alignment
counterfactual_consistency
uncertainty
```

Any aggregation rule must be transparent and validated.

---

# 7. Coherence and Drift

### `PA-M24 — Cross-Observation Coherence`

Measures agreement among independent observations expected to relate.

```text
COC = coherent_observation_pairs
      / eligible_observation_pairs
```

A low result may indicate:

- heterogeneous capability,
- poor measurement,
- multiple regimes,
- insufficient evidence,
- or invalid assumptions.

---

### `PA-M25 — Profile Contradiction Density`

Measures unresolved contradictions within the profile.

```text
PCD = unresolved_contradictions
      / evaluated_relationships
```

Contradictions should not automatically be treated as errors.

They may identify meaningful asymmetry or regime dependence.

---

### `PA-M26 — Dimension Drift Rate`

Measures change in a dimension across a defined interval.

```text
DDR = dimension_change
      / observation_interval
```

Interpretation requires expected stability assumptions.

---

### `PA-M27 — Profile Drift Magnitude`

Measures overall profile change.

```text
PDM = distance(
  profile_t1,
  profile_t2
)
```

Profile drift should be decomposed by dimension and substrate.

---

# 8. Uncertainty and Calibration

### `PA-M28 — Confidence Calibration Error`

Measures the difference between stated confidence and observed correctness or reproducibility.

```text
CCE = average(
  absolute(stated_confidence - observed_frequency)
)
```

Lower values indicate better calibration.

---

### `PA-M29 — Brier Score`

For probabilistic categorical outcomes:

```text
BS = mean((forecast_probability - outcome)^2)
```

Lower values indicate better probabilistic accuracy.

---

### `PA-M30 — Abstention Rate`

```text
AR = abstained_results
     / eligible_results
```

This metric is descriptive and must be paired with abstention quality.

---

### `PA-M31 — Abstention Utility`

Measures whether abstention concentrates on observations likely to be unreliable.

```text
AU = error_reduction_after_abstention
     - abstention_cost
```

The cost definition must be declared for the use case.

---

### `PA-M32 — Unsupported Assertion Rate`

```text
UAR = assertions_without_sufficient_evidence
      / all_profile_assertions
```

Target direction:

```text
lower_is_better
```

---

# 9. Counterfactual and Robustness Metrics

### `PA-M33 — Irrelevant Perturbation Stability`

Measures profile stability when irrelevant input details change.

```text
IPS = similarity(
  original_result,
  irrelevant_perturbation_result
)
```

---

### `PA-M34 — Relevant Change Sensitivity`

Measures whether meaningful evidence changes are reflected in the output.

```text
RCS = detected_meaningful_changes
      / introduced_meaningful_changes
```

A robust system needs both:

- stability to irrelevant changes,
- sensitivity to relevant changes.

---

### `PA-M35 — Task-Order Sensitivity`

Measures changes caused by reordering otherwise equivalent task sequences.

```text
TOS = distance(
  result_order_a,
  result_order_b
)
```

---

### `PA-M36 — Adapter Ablation Effect`

Measures what each adapter contributes.

```text
AAE(adapter_x) =
  performance(full_adapter_set)
  - performance(without_adapter_x)
```

Ablation helps determine whether:

- FFT,
- The Inverted Star,
- Structural Detection,
- RTT,
- or Resonance

adds measurable value beyond the baseline.

---

# 10. Fairness Metrics

### `PA-M37 — Group Error Difference`

```text
GED = error_rate_group_a
      - error_rate_group_b
```

Absolute and relative differences may both be reported.

---

### `PA-M38 — Group Calibration Difference`

Measures whether confidence has comparable meaning across evaluated groups.

```text
GCD = calibration_error_group_a
      - calibration_error_group_b
```

---

### `PA-M39 — Mismatch Flag Rate Difference`

```text
MFRD = mismatch_flag_rate_group_a
       - mismatch_flag_rate_group_b
```

A difference is not, by itself, proof of unfairness.

It is a signal requiring contextual investigation.

---

### `PA-M40 — Abstention Coverage Difference`

```text
ACD = abstention_rate_group_a
      - abstention_rate_group_b
```

---

### `PA-M41 — Escalation Rate Difference`

```text
ERD = human_review_rate_group_a
      - human_review_rate_group_b
```

---

### `PA-M42 — Evidence Coverage Difference`

```text
ECD = evidence_coverage_group_a
      - evidence_coverage_group_b
```

This helps reveal whether profile quality differs because some populations are less adequately represented by available evidence or tasks.

---

### `PA-M43 — False Favorable Reinterpretation Rate`

Measures unsupported alternate interpretations that make an assessment more favorable.

```text
FFRR = unsupported_favorable_reinterpretations
       / favorable_reinterpretations
```

---

### `PA-M44 — False Adverse Reinterpretation Rate`

Measures unsupported alternate interpretations that make an assessment less favorable.

```text
FARR = unsupported_adverse_reinterpretations
       / adverse_reinterpretations
```

Both are required.

Fairness cannot mean detecting only harmful underestimation while ignoring harmful overestimation.

---

# 11. Explainability and Review Metrics

### `PA-M45 — Evidence Reconstruction Rate`

Measures whether qualified reviewers can reproduce the profile conclusion from the recorded evidence.

```text
ERR = successfully_reconstructed_results
      / reviewed_results
```

---

### `PA-M46 — Explanation Completeness`

Required explanation components:

```text
observation
evidence
substrate
regime
confidence
uncertainty
limitations
alternatives
recommended_action
```

```text
EC = present_required_components
     / total_required_components
```

---

### `PA-M47 — Reviewer Override Rate`

```text
ROR = reviewer_overrides
      / reviewed_results
```

Overrides should be categorized by cause:

```text
incorrect_evidence
incorrect_rule
missing_context
unjustified_confidence
fairness_concern
applicability_error
other
```

---

### `PA-M48 — Contest Resolution Rate`

Measures whether subject or stakeholder challenges receive a documented resolution.

```text
CRR = resolved_contests
      / submitted_contests
```

Resolution does not mean the original result must be changed.

---

# 12. Operational Metrics

### `PA-M49 — Profile Completion Rate`

```text
PCR = completed_profiles
      / initiated_profiles
```

---

### `PA-M50 — Time to Review`

```text
TTR = review_completion_time
      - review_start_time
```

---

### `PA-M51 — Evidence Acquisition Burden`

Records:

- subject time,
- evaluator time,
- computational cost,
- tool requirements,
- accessibility burden,
- privacy burden.

A richer profile may not be justified if the burden is disproportionate to its value.

---

### `PA-M52 — Decision Deferral Rate`

```text
DDR = deferred_decisions
      / decision_opportunities
```

This must be interpreted alongside error reduction and harm avoidance.

---

# Resonant IQ Fingerprint Metric Set

The first RIQF pilot should report at least:

```text
PA-M01  Dimension Evidence Coverage
PA-M02  Profile Evidence Coverage
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
PA-M20  Model-Mismatch Precision
PA-M21  Model-Mismatch Recall
PA-M28  Confidence Calibration Error
PA-M32  Unsupported Assertion Rate
PA-M36  Adapter Ablation Effect
PA-M37  Group Error Difference
PA-M38  Group Calibration Difference
PA-M42  Evidence Coverage Difference
PA-M43  False Favorable Reinterpretation Rate
PA-M44  False Adverse Reinterpretation Rate
PA-M45  Evidence Reconstruction Rate
PA-M46  Explanation Completeness
```

---

# Comparative Evaluation Matrix

Each study should compare the following configurations:

```text
M0: conventional scalar model
M1: conventional subscale model
M2: baseline multidimensional profile
M3: multidimensional + substrate observations
M4: M3 + Structural Detection
M5: M4 + RTT / regime observations
M6: M5 + resonance observations
M7: complete Predictive Analytics adapter ensemble
```

For every configuration, report:

```text
predictive_performance
calibration
reliability
profile_stability
fairness
evidence_coverage
uncertainty_quality
explainability
review_burden
privacy_burden
```

This prevents the framework from attributing all improvements to RTT or resonance when the actual gain may come from ordinary multidimensional assessment.

---

# Threshold Policy

During the exploratory phase:

```text
threshold_status: study_specific
universal_thresholds: prohibited
preregistration_required: true
post_hoc_threshold_changes: disclosed
```

Before operational use, every threshold must document:

- purpose,
- population or system class,
- metric,
- value,
- rationale,
- validation evidence,
- expected error,
- subgroup behavior,
- review date,
- version.

---

# Required Metric Pairings

Metrics should be interpreted in pairs or groups.

Examples:

```text
accuracy + calibration
coverage + abstention
mismatch_precision + mismatch_recall
substrate_effect + substrate_replicability
stability + relevant_change_sensitivity
fairness_difference + evidence_coverage
explainability + reconstruction_rate
predictive_gain + operational_burden
```

A metric should not be optimized in isolation if doing so could conceal another failure.

---

# Metric Governance

Every metric must declare:

```text
owner
version
status
intended_use
known_limitations
calculation_method
required_inputs
missing_data_policy
subgroup_policy
threshold_policy
review_schedule
```

Metrics may have these lifecycle states:

```text
proposed
pilot
validated
restricted
deprecated
rejected
```

---

# Final Metric Rule

> **Measure the framework's failures at least as carefully as its successes.**

For every metric that can demonstrate added value, include a corresponding metric capable of detecting:

- unsupported inference,
- instability,
- unfairness,
- hidden favorability bias,
- excessive burden,
- poor calibration,
- or failure to abstain.

---

---

# Appendix — Synthetic Example Validation Record

> Append this section to `example_resonant_iq_fingerprint.md`.

## Example Validation Record

The following values are illustrative placeholders demonstrating the reporting structure.

They are not results from a real validation study.

```text
validation_record:
  subject: PAX-01
  data_type: synthetic

  evidence:
    dimension_coverage: simulated
    profile_coverage: simulated
    independent_sources: simulated

  reliability:
    test_retest: not_tested
    alternate_form: not_tested
    inter_rater: not_tested
    topology_stability: not_tested

  substrate:
    effect_magnitude: demonstration_only
    replicability: not_tested
    symmetry: not_tested

  model_mismatch:
    precision: not_tested
    recall: not_tested
    false_positive_rate: not_tested

  uncertainty:
    calibration: not_tested
    unsupported_assertion_rate: not_tested

  fairness:
    subgroup_analysis: not_applicable_to_single_synthetic_case

  adapters:
    ablation_test: not_tested

  authorization:
    research_demonstration: true
    psychological_assessment: false
    automated_decision: false
```

## Example Validation Conclusion

```text
result:
  structurally_demonstrated: true
  empirically_validated: false
  decision_authority: none
```

The example demonstrates how a profile can be represented.

It does not demonstrate that the dimensions, adapters, or interpretations are scientifically validated.

---

# Closing Validation Principle

The Predictive Analytics framework should never receive a free pass merely because it produces a richer or more satisfying description than an existing model.

It must demonstrate that the additional structure carries measurable information.

That means evaluating:

- **what it gets right,**
- **what it gets wrong,**
- **when it should abstain,**
- **when the conventional model performs better,**
- **when substrate effects replicate,**
- **when they fail to replicate,**
- **which adapters add measurable value,**
- **which adapters add only complexity,**
- **and whether the resulting profile remains fair, legible, and falsifiable.**

The core standard is simple:

> **A deeper model earns its complexity. It does not assume it.**

And for the Resonant IQ Fingerprint specifically:

> **The purpose is not to replace one flattering or unflattering number with a more elaborate judgment. The purpose is to preserve the shape, context, uncertainty, and observational limits that a single number necessarily loses.**

---

Yes. This should be the canonical instance paired with the schema, with everything still marked honestly as experimental. I’d start at 0.1.0 rather than 1.0.0 since the dimensions, adapters, metrics, and validation program have not yet been empirically established.

Suggested path: /docs/predictive_analytics/predictive_analytics_module.json
```json
{
  "predictive_analytics_module": {
    "version": "0.1.0",
    "id": "predictive-analytics",
    "name": "Predictive Analytics",
    "short_name": "PA",
    "description": "Experimental substrate-aware predictive analytics framework for comparing conventional predictions with multidimensional observations, model fit, substrate fit, regime fit, resonance, drift, coherence, uncertainty, and alternate representations.",
    "tagline": "Predict the observation. Observe the predictor.",
    "category": "predictive-structural",
    "state": {
      "rtt": 1,
      "coherence": "declared",
      "drift": "bounded",
      "paradox": "preserved",
      "regime": "predictive-structural",
      "lifecycle": "experimental",
      "validation": "unvalidated",
      "decision_authority": "none"
    },
    "generated_at": "2026-11-19T18:57:47-05:00",
    "last_modified": "2026-11-19",
    "source_repo": "https://github.com/umaywant2/TriadicFrameworks",
    "source_path": "docs/predictive_analytics",
    "canonical_url": "https://www.triadicframeworks.org/predictive_analytics/",
    "license": "MIT",
    "architecture": {
      "pattern": "observer-adapter",
      "primary_pipeline": [
        "observed-system",
        "measurement-substrate",
        "existing-predictive-model",
        "prediction",
        "predictive-analytics-observer-layer",
        "comparative-assessment"
      ],
      "observation_boundary": "Predictions are treated as model outputs rather than complete identities of the observed system. The framework preserves evidence, model fit, substrate fit, regime fit, uncertainty, disagreement, and alternative interpretations.",
      "scalar_policy": {
        "primary_representation": "multidimensional_profile",
        "composites_allowed": true,
        "loss_warning_required": true,
        "hidden_master_score_prohibited": true
      },
      "supports_human_observation": true,
      "supports_ai_observation": true,
      "supports_team_observation": true,
      "supports_organizational_observation": true,
      "standalone_mode": true
    },
    "lineage": {
      "version": "0.1.0",
      "origin": "Initial Predictive Analytics module scaffold integrating conventional predictive models with substrate-aware observation and experimental TriadicFrameworks adapters.",
      "promoted_at": "2026-11-19T18:57:47-05:00",
      "source_repo": "https://github.com/umaywant2/TriadicFrameworks",
      "source_path": "docs/predictive_analytics",
      "architecture": "substrate-aware observer-adapter",
      "parent_modules": [
        "Corpus",
        "RTT",
        "Structural Detection",
        "Resonance"
      ],
      "canon_dependencies": [
        "Framework Field Theory",
        "The Inverted Star",
        "Structural Detection",
        "RTT",
        "Resonance",
        "Drift Taxonomy"
      ],
      "note": "Initial experimental generation. Existing predictive models remain evidence. TriadicFrameworks adapters are hypotheses to be independently validated and may be retained, revised, deprecated, restricted, or rejected."
    },
    "ai_metadata": {
      "schema_version": "0.1.0",
      "embedding_strategy": "hybrid",
      "chunk_boundary": "section-heading",
      "context_window_advisory": "large",
      "injection_pattern": "foundation-first",
      "retrieval_hint": "Resolve the predictive task first, then inspect evidence, model fit, substrate fit, regime fit, relevant dimensions, adapter observations, uncertainty, validation state, ethics limits, and review requirements. Never infer that an alternate assessment is preferable merely because it is more favorable.",
      "semantic_tags": [
        "predictive-analytics",
        "substrate-aware-assessment",
        "model-mismatch",
        "multidimensional-intelligence",
        "resonant-iq-fingerprint",
        "rtt",
        "resonance",
        "regime-awareness",
        "structural-detection",
        "drift",
        "coherence",
        "uncertainty",
        "fairness",
        "validation",
        "human-review"
      ],
      "model_compatibility": [
        "general-language-model",
        "agentic-system",
        "statistical-model",
        "predictive-model",
        "human-review-workflow"
      ],
      "audience": [
        "students",
        "researchers",
        "developers",
        "educators",
        "AI systems",
        "model evaluators"
      ],
      "standalone_mode": true,
      "generation_ts": "2026-11-19T18:57:47-05:00"
    },
    "operators": [
      {
        "id": "PA-Predict",
        "label": "Predict",
        "description": "Represent an existing prediction without treating the prediction as the complete observed system.",
        "inputs": [
          "model",
          "evidence",
          "prediction"
        ],
        "outputs": [
          "prediction-record"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [],
        "related_metrics": [
          "PA-M11",
          "PA-M28"
        ]
      },
      {
        "id": "PA-Observe",
        "label": "Observe",
        "description": "Observe the predictive process, its evidence boundary, and its relationship to the system being modeled.",
        "inputs": [
          "prediction-record",
          "observations"
        ],
        "outputs": [
          "observer-record"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "related_metrics": [
          "PA-M01",
          "PA-M02",
          "PA-M03"
        ]
      },
      {
        "id": "PA-Substrate",
        "label": "Substrate",
        "description": "Evaluate whether the measurement substrate provides adequate conditions for observing the capability or behavior being inferred.",
        "inputs": [
          "observations",
          "substrate-context"
        ],
        "outputs": [
          "substrate-fit"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [
          "fft",
          "inverted-star",
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "related_metrics": [
          "PA-M12",
          "PA-M13",
          "PA-M14",
          "PA-M15"
        ]
      },
      {
        "id": "PA-Regime",
        "label": "Regime",
        "description": "Evaluate whether the predictive model and observed system occupy compatible operating regimes.",
        "inputs": [
          "observations",
          "regime-context"
        ],
        "outputs": [
          "regime-fit",
          "regime-transition-observations"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [
          "rtt"
        ],
        "related_metrics": [
          "PA-M16",
          "PA-M17",
          "PA-M18",
          "PA-M19"
        ]
      },
      {
        "id": "PA-Resonance",
        "label": "Resonance",
        "description": "Observe whether capability expression is amplified, suppressed, stabilized, or altered across contexts and substrates.",
        "inputs": [
          "observations",
          "context-comparisons"
        ],
        "outputs": [
          "resonance-profile"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [
          "resonance"
        ],
        "related_metrics": [
          "PA-M12",
          "PA-M13",
          "PA-M24"
        ]
      },
      {
        "id": "PA-Drift",
        "label": "Drift",
        "description": "Detect divergence in observations, predictions, profiles, or operating conditions across time or contexts.",
        "inputs": [
          "observation-series"
        ],
        "outputs": [
          "drift-profile"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [
          "rtt"
        ],
        "related_metrics": [
          "PA-M26",
          "PA-M27"
        ]
      },
      {
        "id": "PA-Coherence",
        "label": "Coherence",
        "description": "Compare independent observations and preserve both supporting and contradictory signals.",
        "inputs": [
          "observations"
        ],
        "outputs": [
          "coherence-profile",
          "contradictions"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "related_metrics": [
          "PA-M24",
          "PA-M25"
        ]
      },
      {
        "id": "PA-Structure",
        "label": "Structure",
        "description": "Identify candidate structural relationships, invariants, boundaries, faultlines, and reconstruction patterns in observed evidence.",
        "inputs": [
          "observations"
        ],
        "outputs": [
          "structural-profile"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [
          "fft",
          "inverted-star",
          "structural-detection"
        ],
        "related_metrics": [
          "PA-M08",
          "PA-M09",
          "PA-M36"
        ]
      },
      {
        "id": "PA-Counterfactual",
        "label": "Counterfactual",
        "description": "Compare reasonable alternate representations while preserving the original result.",
        "inputs": [
          "baseline-assessment",
          "alternate-representations"
        ],
        "outputs": [
          "counterfactual-comparison"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [],
        "related_metrics": [
          "PA-M33",
          "PA-M34",
          "PA-M35"
        ]
      },
      {
        "id": "PA-Uncertainty",
        "label": "Uncertainty",
        "description": "Represent uncertainty, missing evidence, abstention, and unsupported inference explicitly.",
        "inputs": [
          "assessment",
          "evidence-coverage"
        ],
        "outputs": [
          "uncertainty-record",
          "abstention-state"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [],
        "related_metrics": [
          "PA-M28",
          "PA-M29",
          "PA-M30",
          "PA-M31",
          "PA-M32"
        ]
      },
      {
        "id": "PA-Calibrate",
        "label": "Calibrate",
        "description": "Compare predictions, confidence, and observed outcomes to evaluate predictive and interpretive calibration.",
        "inputs": [
          "predictions",
          "outcomes"
        ],
        "outputs": [
          "calibration-record"
        ],
        "status": "experimental",
        "requires_human_review": false,
        "related_adapters": [],
        "related_metrics": [
          "PA-M28",
          "PA-M29"
        ]
      },
      {
        "id": "PA-Escalate",
        "label": "Escalate",
        "description": "Recommend additional evidence or qualified human review when uncertainty, consequence, disagreement, or model mismatch warrants escalation.",
        "inputs": [
          "assessment",
          "uncertainty-record"
        ],
        "outputs": [
          "review-recommendation"
        ],
        "status": "experimental",
        "requires_human_review": true,
        "related_adapters": [],
        "related_metrics": [
          "PA-M41",
          "PA-M47",
          "PA-M48",
          "PA-M50"
        ]
      }
    ],
    "roles": [
      {
        "id": "foundation",
        "label": "Foundation",
        "description": "Defines the conceptual and structural basis of the Predictive Analytics module.",
        "allowed_document_types": [
          "markdown"
        ]
      },
      {
        "id": "observer",
        "label": "Observer Layer",
        "description": "Examines model fit, substrate fit, regime fit, resonance, drift, coherence, and uncertainty.",
        "allowed_document_types": [
          "markdown"
        ]
      },
      {
        "id": "adapter",
        "label": "Substrate Adapter",
        "description": "Connects an existing model or TriadicFrameworks analytical grammar to the Predictive Analytics observer layer.",
        "allowed_document_types": [
          "markdown"
        ]
      },
      {
        "id": "profile",
        "label": "Profile Model",
        "description": "Defines a multidimensional profile representation such as the Resonant IQ Fingerprint.",
        "allowed_document_types": [
          "markdown"
        ]
      },
      {
        "id": "validation",
        "label": "Validation",
        "description": "Defines falsification, validation, measurement, and reporting requirements.",
        "allowed_document_types": [
          "markdown"
        ]
      },
      {
        "id": "metrics",
        "label": "Metrics",
        "description": "Defines experimental measurement and evaluation metrics.",
        "allowed_document_types": [
          "markdown"
        ]
      },
      {
        "id": "ethics",
        "label": "Ethics and Limits",
        "description": "Defines ethical constraints, prohibited uses, privacy requirements, contestability, and known limitations.",
        "allowed_document_types": [
          "markdown"
        ]
      },
      {
        "id": "example",
        "label": "Example",
        "description": "Provides synthetic or otherwise appropriately governed worked examples.",
        "allowed_document_types": [
          "markdown"
        ]
      },
      {
        "id": "module",
        "label": "Module Metadata",
        "description": "Provides machine-readable module metadata and schema definitions.",
        "allowed_document_types": [
          "json"
        ]
      }
    ],
    "analyzer_layers": [
      {
        "id": "substrate",
        "label": "Substrate Fit",
        "description": "Examines whether the expression and measurement substrate is compatible with the capability being inferred.",
        "primary_documents": [
          "substrate_adapter.md",
          "substrate_expression_profile.md"
        ],
        "adapter_refs": [
          "fft",
          "inverted-star",
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "operator_refs": [
          "PA-Substrate"
        ],
        "metric_refs": [
          "PA-M12",
          "PA-M13",
          "PA-M14",
          "PA-M15"
        ]
      },
      {
        "id": "regime",
        "label": "Regime Observation",
        "description": "Examines operating regimes, transitions, and model-subject regime compatibility.",
        "primary_documents": [
          "regime_observer.md"
        ],
        "adapter_refs": [
          "rtt"
        ],
        "operator_refs": [
          "PA-Regime"
        ],
        "metric_refs": [
          "PA-M16",
          "PA-M17",
          "PA-M18",
          "PA-M19"
        ]
      },
      {
        "id": "resonance",
        "label": "Resonance Observation",
        "description": "Examines contextual amplification, suppression, stability, and cross-context expression.",
        "primary_documents": [
          "resonance_observer.md",
          "resonant_iq_fingerprint.md"
        ],
        "adapter_refs": [
          "resonance"
        ],
        "operator_refs": [
          "PA-Resonance"
        ],
        "metric_refs": [
          "PA-M12",
          "PA-M13",
          "PA-M24"
        ]
      },
      {
        "id": "drift",
        "label": "Drift Observation",
        "description": "Examines temporal, semantic, profile, and observational drift.",
        "primary_documents": [
          "drift_observer.md"
        ],
        "adapter_refs": [
          "rtt"
        ],
        "operator_refs": [
          "PA-Drift"
        ],
        "metric_refs": [
          "PA-M26",
          "PA-M27"
        ]
      },
      {
        "id": "coherence",
        "label": "Coherence Observation",
        "description": "Examines agreement and contradiction across independent observations.",
        "primary_documents": [
          "coherence_observer.md"
        ],
        "adapter_refs": [
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "operator_refs": [
          "PA-Coherence"
        ],
        "metric_refs": [
          "PA-M24",
          "PA-M25"
        ]
      },
      {
        "id": "uncertainty",
        "label": "Uncertainty and Abstention",
        "description": "Preserves missing evidence, uncertainty, calibration, and explicit abstention.",
        "primary_documents": [
          "uncertainty_layer.md"
        ],
        "adapter_refs": [],
        "operator_refs": [
          "PA-Uncertainty"
        ],
        "metric_refs": [
          "PA-M28",
          "PA-M29",
          "PA-M30",
          "PA-M31",
          "PA-M32"
        ]
      }
    ],
    "adapters": [
      {
        "id": "fft",
        "name": "Framework Field Theory Adapter",
        "description": "Experimental adapter for examining relational, field, boundary, and local-to-global structural observations.",
        "status": "experimental",
        "source_framework": "Framework Field Theory",
        "source_document": "FFT_adapter.md",
        "purpose": "Test whether field and relationship-oriented observations add independently useful information to predictive assessment.",
        "supported_inputs": [
          "relationship observations",
          "boundary observations",
          "local-global observations",
          "system context"
        ],
        "unsupported_inputs": [
          "unsupported causal claims",
          "unobserved internal states"
        ],
        "outputs": [
          "field-relationship observations",
          "boundary observations",
          "local-global relationship observations"
        ],
        "claims": [
          "May identify relational information omitted by isolated-variable representations."
        ],
        "limitations": [
          "Experimental.",
          "Does not establish scientific validity of Framework Field Theory.",
          "Must demonstrate incremental value beyond simpler relational analysis."
        ],
        "confounds": [
          "task complexity",
          "prior domain knowledge",
          "evaluator interpretation"
        ],
        "validation_state": "unvalidated",
        "ablation_metric": "PA-M36",
        "decision_authority": "none"
      },
      {
        "id": "inverted-star",
        "name": "The Inverted Star Adapter",
        "description": "Experimental adapter for detecting candidate inversions between predicted performance and independently demonstrated capability.",
        "status": "experimental",
        "source_framework": "The Inverted Star",
        "source_document": "Inverted_Star_adapter.md",
        "purpose": "Preserve and investigate discrepancies between model expectations and demonstrated outcomes.",
        "supported_inputs": [
          "predicted outcomes",
          "observed outcomes",
          "cross-substrate comparisons"
        ],
        "unsupported_inputs": [
          "claims of hidden ability without evidence"
        ],
        "outputs": [
          "inversion candidates",
          "alternative explanations"
        ],
        "claims": [
          "May identify cases in which aggregate or narrow measurement disagrees with independent observations."
        ],
        "limitations": [
          "Inversion does not prove hidden superior capability.",
          "Discrepancy may reflect noise, task differences, or genuine uneven capability."
        ],
        "confounds": [
          "measurement noise",
          "practice effects",
          "task differences",
          "selection bias"
        ],
        "validation_state": "unvalidated",
        "ablation_metric": "PA-M36",
        "decision_authority": "none"
      },
      {
        "id": "structural-detection",
        "name": "Structural Detection Adapter",
        "description": "Experimental adapter for latent pattern, invariant, faultline, relationship, and boundary observations.",
        "status": "experimental",
        "source_framework": "Structural Detection",
        "source_document": "Structural_Detection_adapter.md",
        "purpose": "Test structural observation dimensions against conventional and baseline multidimensional models.",
        "supported_inputs": [
          "pattern tasks",
          "relationship tasks",
          "partial evidence",
          "boundary tasks"
        ],
        "unsupported_inputs": [
          "unobserved ability",
          "identity claims"
        ],
        "outputs": [
          "structural observations",
          "faultline observations",
          "invariant observations"
        ],
        "claims": [
          "May provide a structured vocabulary for observing system-level reasoning."
        ],
        "limitations": [
          "Must be empirically distinguished from existing reasoning constructs.",
          "Structural labels do not establish intelligence by themselves."
        ],
        "confounds": [
          "domain expertise",
          "task familiarity",
          "evaluator interpretation"
        ],
        "validation_state": "unvalidated",
        "ablation_metric": "PA-M36",
        "decision_authority": "none"
      },
      {
        "id": "rtt",
        "name": "RTT Adapter",
        "description": "Experimental adapter for regime recognition, temporal sequencing, drift, stability, transition, continuity, and recalibration observations.",
        "status": "experimental",
        "source_framework": "RTT",
        "source_document": "RTT_adapter.md",
        "purpose": "Test whether regime-aware and temporal observations improve explanation or prediction beyond baseline models.",
        "supported_inputs": [
          "time-series observations",
          "regime contexts",
          "transition observations",
          "repeated assessments"
        ],
        "unsupported_inputs": [
          "unobserved regime claims",
          "unsupported causal claims"
        ],
        "outputs": [
          "regime observations",
          "transition observations",
          "drift observations",
          "continuity observations"
        ],
        "claims": [
          "May differentiate within-regime stability from between-regime variation."
        ],
        "limitations": [
          "RTT-derived observations remain experimental.",
          "Regime labels require independent operational definitions."
        ],
        "confounds": [
          "task order",
          "fatigue",
          "learning",
          "environmental change"
        ],
        "validation_state": "unvalidated",
        "ablation_metric": "PA-M36",
        "decision_authority": "none"
      },
      {
        "id": "resonance",
        "name": "Resonance Adapter",
        "description": "Experimental adapter for observing contextual amplification, suppression, persistence, instability, and observer-subject coupling.",
        "status": "experimental",
        "source_framework": "Resonance",
        "source_document": "resonance_adapter.md",
        "purpose": "Test whether repeatable context-dependent changes can be represented without converting them into unsupported identity claims.",
        "supported_inputs": [
          "cross-context observations",
          "cross-substrate observations",
          "repeated performance observations"
        ],
        "unsupported_inputs": [
          "unmeasured latent traits",
          "metaphorical resonance treated as measurement"
        ],
        "outputs": [
          "amplification observations",
          "suppression observations",
          "persistence observations",
          "instability observations"
        ],
        "claims": [
          "May help describe repeatable context-dependent variation."
        ],
        "limitations": [
          "Context dependence does not establish cause.",
          "Resonance terminology must map to operational measurements."
        ],
        "confounds": [
          "task difficulty",
          "motivation",
          "fatigue",
          "environment",
          "prior exposure"
        ],
        "validation_state": "unvalidated",
        "ablation_metric": "PA-M36",
        "decision_authority": "none"
      }
    ],
    "dimensions": [
      {
        "id": "pattern-recognition",
        "name": "Pattern Recognition",
        "description": "Observed ability to detect recurring or meaningful patterns in defined evidence.",
        "status": "experimental",
        "operational_definition": "Performance on tasks requiring detection of defined regularities or relationships above an appropriate baseline.",
        "exclusions": [
          "unsupported intuition claims",
          "post-hoc pattern attribution"
        ],
        "observable_indicators": [
          "repeatable pattern detection",
          "novel pattern transfer"
        ],
        "counter_indicators": [
          "chance-level detection",
          "non-replicating pattern attribution"
        ],
        "supported_substrates": [
          "textual",
          "visual",
          "symbolic",
          "relational"
        ],
        "known_confounds": [
          "prior exposure",
          "domain knowledge",
          "task familiarity"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "unknown"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "task",
            "replication",
            "cross-substrate observation"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "structural-reasoning",
          "anomaly-detection"
        ],
        "metric_refs": [
          "PA-M01",
          "PA-M04",
          "PA-M05",
          "PA-M08"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "structural-reasoning",
        "name": "Structural Reasoning",
        "description": "Observed ability to identify and reason about relationships, boundaries, dependencies, and system-level organization.",
        "status": "experimental",
        "operational_definition": "Performance on tasks requiring reconstruction or explanation of relationships among multiple interacting components.",
        "exclusions": [
          "general intelligence claims",
          "domain expertise alone"
        ],
        "observable_indicators": [
          "relationship mapping",
          "boundary identification",
          "system reconstruction"
        ],
        "counter_indicators": [
          "inconsistent structural reconstruction",
          "failure to distinguish relevant relationships"
        ],
        "supported_substrates": [
          "textual",
          "visual",
          "relational",
          "spatial"
        ],
        "known_confounds": [
          "domain knowledge",
          "task design",
          "diagram literacy"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "substrate_dependent"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "task",
            "independent review",
            "cross-domain observation"
          ]
        },
        "preferred_expressions": [
          "relational",
          "spatial",
          "system-level"
        ],
        "possible_suppressors": [
          "context removal",
          "inappropriate task representation"
        ],
        "related_dimensions": [
          "pattern-recognition",
          "causal-integration",
          "cross-domain-transfer"
        ],
        "metric_refs": [
          "PA-M01",
          "PA-M07",
          "PA-M09",
          "PA-M36"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "causal-integration",
        "name": "Causal Integration",
        "description": "Observed ability to integrate multiple candidate causes and consequences while distinguishing prediction from causal evidence.",
        "status": "experimental",
        "operational_definition": "Performance on defined tasks requiring comparison and integration of causal hypotheses.",
        "exclusions": [
          "correlation treated as causation"
        ],
        "observable_indicators": [
          "alternative causal hypotheses",
          "dependency tracing",
          "causal uncertainty preservation"
        ],
        "counter_indicators": [
          "unsupported causal certainty"
        ],
        "supported_substrates": [
          "textual",
          "relational",
          "temporal"
        ],
        "known_confounds": [
          "domain knowledge",
          "missing variables"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "unknown"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "task",
            "outcome comparison"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "structural-reasoning",
          "temporal-reasoning"
        ],
        "metric_refs": [
          "PA-M08",
          "PA-M09"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "temporal-reasoning",
        "name": "Temporal Reasoning",
        "description": "Observed ability to reason across sequence, timing, transition, and change.",
        "status": "experimental",
        "operational_definition": "Performance on tasks requiring correct handling of ordered events, temporal dependencies, or state transitions.",
        "exclusions": [
          "raw processing speed"
        ],
        "observable_indicators": [
          "sequence reconstruction",
          "transition recognition",
          "temporal dependency reasoning"
        ],
        "counter_indicators": [
          "systematic sequence errors"
        ],
        "supported_substrates": [
          "textual",
          "temporal",
          "visual"
        ],
        "known_confounds": [
          "working memory",
          "task complexity"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "substrate_dependent"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "sequence task",
            "time-series observation"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "regime-recognition",
          "long-horizon-integration"
        ],
        "metric_refs": [
          "PA-M04",
          "PA-M19"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "cross-domain-transfer",
        "name": "Cross-Domain Transfer",
        "description": "Observed ability to transfer useful structure or reasoning between appropriately distinct domains.",
        "status": "experimental",
        "operational_definition": "Performance on novel tasks where previously demonstrated structure can be applied without simply repeating domain-specific knowledge.",
        "exclusions": [
          "surface analogy alone"
        ],
        "observable_indicators": [
          "successful novel transfer",
          "structural analogy with preserved constraints"
        ],
        "counter_indicators": [
          "invalid analogy",
          "failure under novel transfer"
        ],
        "supported_substrates": [
          "textual",
          "relational",
          "visual"
        ],
        "known_confounds": [
          "prior exposure",
          "shared domain knowledge"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "unknown"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "novel task",
            "cross-domain task"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "structural-reasoning",
          "adaptive-reframing"
        ],
        "metric_refs": [
          "PA-M08",
          "PA-M10"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "regime-recognition",
        "name": "Regime Recognition",
        "description": "Observed ability to distinguish materially different operating conditions or state regimes.",
        "status": "experimental",
        "operational_definition": "Performance on tasks containing independently defined regime changes or stable regime intervals.",
        "exclusions": [
          "regime labels invented after outcomes are known"
        ],
        "observable_indicators": [
          "transition detection",
          "within-regime consistency"
        ],
        "counter_indicators": [
          "false transition alarms",
          "missed reference transitions"
        ],
        "supported_substrates": [
          "temporal",
          "relational",
          "textual"
        ],
        "known_confounds": [
          "task order",
          "noise",
          "unclear reference boundaries"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "substrate_dependent"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "regime task",
            "time-series observation"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "temporal-reasoning",
          "drift-awareness"
        ],
        "metric_refs": [
          "PA-M16",
          "PA-M17",
          "PA-M18",
          "PA-M19"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "anomaly-detection",
        "name": "Anomaly Detection",
        "description": "Observed ability to identify defined deviations from an established pattern or regime.",
        "status": "experimental",
        "operational_definition": "Detection of independently designated anomalies with false-positive behavior measured.",
        "exclusions": [
          "unverifiable anomaly claims"
        ],
        "observable_indicators": [
          "reference anomaly detection"
        ],
        "counter_indicators": [
          "high false-alarm rate"
        ],
        "supported_substrates": [
          "visual",
          "symbolic",
          "temporal",
          "relational"
        ],
        "known_confounds": [
          "base rates",
          "noise"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "unknown"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "anomaly task"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "pattern-recognition",
          "drift-awareness"
        ],
        "metric_refs": [
          "PA-M08",
          "PA-M09"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "ambiguity-navigation",
        "name": "Ambiguity Navigation",
        "description": "Observed ability to reason while preserving competing interpretations when evidence is incomplete.",
        "status": "experimental",
        "operational_definition": "Performance on tasks in which uncertainty and multiple plausible interpretations are intentionally preserved.",
        "exclusions": [
          "indecision treated automatically as sophistication"
        ],
        "observable_indicators": [
          "preserved alternatives",
          "appropriate uncertainty"
        ],
        "counter_indicators": [
          "unjustified certainty",
          "failure to distinguish alternatives"
        ],
        "supported_substrates": [
          "textual",
          "relational"
        ],
        "known_confounds": [
          "verbal fluency",
          "task familiarity"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "unknown"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "ambiguous task",
            "uncertainty calibration task"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [
          "forced binary response"
        ],
        "related_dimensions": [
          "adaptive-reframing",
          "metacognitive-calibration"
        ],
        "metric_refs": [
          "PA-M28",
          "PA-M32"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "adaptive-reframing",
        "name": "Adaptive Reframing",
        "description": "Observed ability to revise a representation when new evidence invalidates or weakens the current framing.",
        "status": "experimental",
        "operational_definition": "Successful revision following relevant evidence changes without unnecessary revision to irrelevant perturbations.",
        "exclusions": [
          "arbitrary answer changing"
        ],
        "observable_indicators": [
          "appropriate revision",
          "stable response to irrelevant perturbation"
        ],
        "counter_indicators": [
          "failure to update",
          "excessive sensitivity to irrelevant changes"
        ],
        "supported_substrates": [
          "textual",
          "relational",
          "temporal"
        ],
        "known_confounds": [
          "task ambiguity",
          "feedback clarity"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "substrate_dependent"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "counterfactual task",
            "evidence-update task"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "ambiguity-navigation",
          "metacognitive-calibration"
        ],
        "metric_refs": [
          "PA-M33",
          "PA-M34"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "coherence-maintenance",
        "name": "Coherence Maintenance",
        "description": "Observed ability to maintain internally compatible reasoning while incorporating relevant new information.",
        "status": "experimental",
        "operational_definition": "Consistency of related conclusions under controlled evidence additions and contradictions.",
        "exclusions": [
          "mere repetition",
          "refusal to update"
        ],
        "observable_indicators": [
          "cross-observation consistency",
          "resolved contradictions"
        ],
        "counter_indicators": [
          "unresolved incompatible claims"
        ],
        "supported_substrates": [
          "textual",
          "relational",
          "temporal"
        ],
        "known_confounds": [
          "memory limits",
          "task length"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "substrate_dependent"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "longitudinal task",
            "contradiction task"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "long-horizon-integration",
          "drift-awareness"
        ],
        "metric_refs": [
          "PA-M24",
          "PA-M25"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "drift-awareness",
        "name": "Drift Awareness",
        "description": "Observed ability to notice material changes in assumptions, evidence, definitions, or system state.",
        "status": "experimental",
        "operational_definition": "Detection of independently identified changes across repeated or longitudinal tasks.",
        "exclusions": [
          "arbitrary change detection"
        ],
        "observable_indicators": [
          "detected assumption change",
          "detected evidence drift"
        ],
        "counter_indicators": [
          "missed material drift",
          "frequent false drift flags"
        ],
        "supported_substrates": [
          "temporal",
          "textual",
          "relational"
        ],
        "known_confounds": [
          "memory",
          "task order"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "substrate_dependent"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "longitudinal task",
            "change detection task"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "regime-recognition",
          "coherence-maintenance"
        ],
        "metric_refs": [
          "PA-M26",
          "PA-M27"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "metacognitive-calibration",
        "name": "Metacognitive Calibration",
        "description": "Observed relationship between expressed confidence and demonstrated correctness or reproducibility.",
        "status": "experimental",
        "operational_definition": "Calibration between confidence reports and observed outcomes across repeated tasks.",
        "exclusions": [
          "self-confidence treated as capability"
        ],
        "observable_indicators": [
          "calibrated confidence",
          "appropriate abstention"
        ],
        "counter_indicators": [
          "systematic overconfidence",
          "systematic underconfidence"
        ],
        "supported_substrates": [
          "textual",
          "symbolic"
        ],
        "known_confounds": [
          "response-scale interpretation"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "unknown"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "confidence task",
            "outcome comparison"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "ambiguity-navigation",
          "adaptive-reframing"
        ],
        "metric_refs": [
          "PA-M28",
          "PA-M29",
          "PA-M31"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "long-horizon-integration",
        "name": "Long-Horizon Integration",
        "description": "Observed ability to preserve and integrate relevant structure across extended sequences or contexts.",
        "status": "experimental",
        "operational_definition": "Performance on tasks requiring integration of information distributed across longer observation intervals.",
        "exclusions": [
          "short-term recall alone"
        ],
        "observable_indicators": [
          "cross-session continuity",
          "long-range dependency integration"
        ],
        "counter_indicators": [
          "loss of relevant earlier constraints"
        ],
        "supported_substrates": [
          "temporal",
          "textual",
          "relational"
        ],
        "known_confounds": [
          "external memory",
          "tool access",
          "task duration"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "substrate_dependent"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "long-horizon task",
            "repeated observation"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "temporal-reasoning",
          "coherence-maintenance"
        ],
        "metric_refs": [
          "PA-M04",
          "PA-M07",
          "PA-M27"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "tool-collaboration",
        "name": "Tool Collaboration",
        "description": "Observed ability of a defined system boundary to use tools productively while preserving attribution of individual and collaborative contributions.",
        "status": "experimental",
        "operational_definition": "Comparative performance across unassisted, tool-assisted, and collaborative conditions with system boundaries explicitly recorded.",
        "exclusions": [
          "attributing combined performance entirely to one participant"
        ],
        "observable_indicators": [
          "effective tool selection",
          "error correction with tools",
          "collaborative performance gain"
        ],
        "counter_indicators": [
          "tool dependence without task improvement",
          "untraceable contribution attribution"
        ],
        "supported_substrates": [
          "tool-mediated",
          "human-ai",
          "software-assisted"
        ],
        "known_confounds": [
          "tool access",
          "training",
          "tool capability"
        ],
        "applicability": {
          "human": "substrate_dependent",
          "ai": "substrate_dependent",
          "human-ai": "applicable",
          "organization": "substrate_dependent"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "tool-assisted task",
            "unassisted comparison",
            "collaborative task"
          ]
        },
        "preferred_expressions": [
          "tool-mediated",
          "collaborative"
        ],
        "possible_suppressors": [
          "lack of tool access"
        ],
        "related_dimensions": [
          "adaptive-reframing",
          "cross-domain-transfer"
        ],
        "metric_refs": [
          "PA-M10",
          "PA-M11",
          "PA-M51"
        ],
        "validation_state": "unvalidated"
      },
      {
        "id": "recovery-recalibration",
        "name": "Recovery and Recalibration",
        "description": "Observed ability to recover from an incorrect assumption, prediction, or action and update subsequent behavior appropriately.",
        "status": "experimental",
        "operational_definition": "Performance following independently identified errors or perturbations where correction opportunities are available.",
        "exclusions": [
          "error avoidance treated as recovery"
        ],
        "observable_indicators": [
          "error recognition",
          "appropriate correction",
          "reduced repeated error"
        ],
        "counter_indicators": [
          "persistent repeated error",
          "maladaptive overcorrection"
        ],
        "supported_substrates": [
          "temporal",
          "textual",
          "relational",
          "tool-mediated"
        ],
        "known_confounds": [
          "feedback availability",
          "task difficulty"
        ],
        "applicability": {
          "human": "applicable",
          "ai": "applicable",
          "human-ai": "substrate_dependent",
          "organization": "substrate_dependent"
        },
        "evidence_requirements": {
          "minimum_independent_sources": 2,
          "replication_required": true,
          "counterevidence_required": true,
          "traceability_required": true,
          "minimum_confidence": "medium",
          "allowed_evidence_types": [
            "error-recovery task",
            "longitudinal observation"
          ]
        },
        "preferred_expressions": [],
        "possible_suppressors": [],
        "related_dimensions": [
          "adaptive-reframing",
          "metacognitive-calibration"
        ],
        "metric_refs": [
          "PA-M33",
          "PA-M34"
        ],
        "validation_state": "unvalidated"
      }
    ],
    "validation": {
      "state": "unvalidated",
      "authorized_uses": [
        "research",
        "demonstration",
        "framework development",
        "synthetic examples",
        "hypothesis generation"
      ],
      "prohibited_uses": [
        "diagnosis",
        "automated hiring decisions",
        "automated firing decisions",
        "educational exclusion",
        "legal determination",
        "insurance eligibility",
        "lending eligibility",
        "sentencing",
        "automated adverse decisions"
      ],
      "levels": [
        {
          "level": 0,
          "id": "structural-validation",
          "name": "Structural Validation",
          "description": "Tests schema, identifiers, evidence traceability, uncertainty fields, applicability fields, and hidden-score protections.",
          "requirements": [
            "schema validation",
            "identifier validation",
            "evidence traceability",
            "uncertainty representation",
            "applicability representation",
            "no hidden master score"
          ],
          "status": "in_progress",
          "evidence_refs": [
            "predictive_analytics_module.schema.json",
            "predictive_analytics_module.json"
          ]
        },
        {
          "level": 1,
          "id": "content-validation",
          "name": "Content Validation",
          "description": "Tests conceptual coverage, dimension definitions, overlap, omissions, and adapter interpretation.",
          "requirements": [
            "expert review",
            "literature crosswalk",
            "dimension review",
            "adapter review"
          ],
          "status": "not_started",
          "evidence_refs": []
        },
        {
          "level": 2,
          "id": "measurement-validation",
          "name": "Measurement Validation",
          "description": "Tests repeated measurement, alternate forms, evaluator agreement, substrate variation, and task-order effects.",
          "requirements": [
            "test-retest study",
            "alternate-form study",
            "inter-rater study",
            "substrate variation study"
          ],
          "status": "not_started",
          "evidence_refs": []
        },
        {
          "level": 3,
          "id": "construct-validation",
          "name": "Construct Validation",
          "description": "Tests convergent, discriminant, structural, and outcome relationships.",
          "requirements": [
            "convergent analysis",
            "discriminant analysis",
            "construct comparison"
          ],
          "status": "not_started",
          "evidence_refs": []
        },
        {
          "level": 4,
          "id": "substrate-regime-validation",
          "name": "Substrate and Regime Validation",
          "description": "Tests whether substrate and regime effects replicate beyond noise and task difficulty.",
          "requirements": [
            "substrate effect replication",
            "regime detection validation",
            "favorability symmetry",
            "confound controls"
          ],
          "status": "not_started",
          "evidence_refs": []
        },
        {
          "level": 5,
          "id": "predictive-validation",
          "name": "Predictive and Explanatory Validation",
          "description": "Tests out-of-sample predictive and explanatory value against simpler baselines.",
          "requirements": [
            "baseline comparison",
            "out-of-sample evaluation",
            "adapter ablation",
            "calibration evaluation"
          ],
          "status": "not_started",
          "evidence_refs": []
        },
        {
          "level": 6,
          "id": "fairness-harm-validation",
          "name": "Fairness and Harm Validation",
          "description": "Tests subgroup errors, uncertainty, evidence coverage, escalation, accessibility, and downstream harms.",
          "requirements": [
            "fairness analysis",
            "harm analysis",
            "accessibility analysis",
            "subgroup evidence analysis"
          ],
          "status": "not_started",
          "evidence_refs": []
        },
        {
          "level": 7,
          "id": "decision-validation",
          "name": "Decision Validation",
          "description": "Required separately for any proposed consequential or high-stakes decision context.",
          "requirements": [
            "specific intended-use validation",
            "risk-benefit analysis",
            "human review design",
            "contestability",
            "governance approval"
          ],
          "status": "not_started",
          "evidence_refs": []
        }
      ],
      "criteria": [
        {
          "id": "VCR-01",
          "name": "Construct Clarity",
          "description": "Dimensions define their meaning, exclusions, indicators, confounds, evidence, and applicability.",
          "pass_condition": "Independent evaluators can distinguish the dimension and identify evidence that would contradict it.",
          "failure_condition": "Dimensions remain ambiguous, circular, or indistinguishable.",
          "metric_refs": [
            "PA-M08",
            "PA-M09"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-02",
          "name": "Evidence Traceability",
          "description": "Every profile result is traceable to declared observations and evidence.",
          "pass_condition": "No profile result exists without evidence or an explicit unknown or insufficient-evidence state.",
          "failure_condition": "Untraceable profile assertions remain.",
          "metric_refs": [
            "PA-M01",
            "PA-M02",
            "PA-M32"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-03",
          "name": "Repeatability",
          "description": "Comparable observations produce sufficiently consistent results where stability is expected.",
          "pass_condition": "Study-specific preregistered reliability criteria are satisfied.",
          "failure_condition": "Results remain unstable beyond declared uncertainty.",
          "metric_refs": [
            "PA-M04",
            "PA-M05",
            "PA-M07"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-04",
          "name": "Inter-Rater Agreement",
          "description": "Independent evaluators produce sufficiently comparable classifications under a shared rubric.",
          "pass_condition": "Preregistered inter-rater agreement criteria are satisfied.",
          "failure_condition": "Evaluator effects dominate observed classifications.",
          "metric_refs": [
            "PA-M06"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-05",
          "name": "Substrate Sensitivity",
          "description": "Claimed substrate effects correspond to controlled changes in representation or interaction conditions.",
          "pass_condition": "Effects replicate beyond expected noise and are not limited to favorable outcomes.",
          "failure_condition": "Effects do not replicate or appear only under selective interpretation.",
          "metric_refs": [
            "PA-M12",
            "PA-M13",
            "PA-M14",
            "PA-M15"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-06",
          "name": "Regime Sensitivity",
          "description": "Regime interpretation detects meaningful reference transitions without labeling generic low performance as mismatch.",
          "pass_condition": "Transition detection and false-alarm performance meet study-specific criteria.",
          "failure_condition": "Regime labeling becomes indiscriminate or non-reproducible.",
          "metric_refs": [
            "PA-M16",
            "PA-M17",
            "PA-M18",
            "PA-M19"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-07",
          "name": "Discriminant Value",
          "description": "Distinct dimensions demonstrate adequate conceptual and empirical distinction.",
          "pass_condition": "Redundancy remains within study-specific bounds.",
          "failure_condition": "Dimensions collapse into redundant labels.",
          "metric_refs": [
            "PA-M09"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-08",
          "name": "Convergent Value",
          "description": "Dimensions relate to appropriate independent observations as preregistered.",
          "pass_condition": "Expected relationships replicate.",
          "failure_condition": "Expected convergence fails without an adequate alternative explanation.",
          "metric_refs": [
            "PA-M08"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-09",
          "name": "Incremental Value",
          "description": "The framework contributes useful information beyond simpler baselines.",
          "pass_condition": "At least one declared outcome improves without unacceptable degradation elsewhere.",
          "failure_condition": "Added complexity provides no meaningful incremental value.",
          "metric_refs": [
            "PA-M10",
            "PA-M11",
            "PA-M36"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-10",
          "name": "Uncertainty Calibration",
          "description": "Declared confidence corresponds to observed correctness or reproducibility.",
          "pass_condition": "Confidence ordering is empirically meaningful and calibration meets study-specific criteria.",
          "failure_condition": "Confidence labels do not correspond to observed reliability.",
          "metric_refs": [
            "PA-M28",
            "PA-M29"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-11",
          "name": "Abstention Quality",
          "description": "The framework abstains when evidence is inadequate.",
          "pass_condition": "Abstention reduces unsupported assertions without unacceptable coverage loss.",
          "failure_condition": "The system guesses where evidence is insufficient or abstains indiscriminately.",
          "metric_refs": [
            "PA-M30",
            "PA-M31",
            "PA-M32"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-12",
          "name": "Model-Mismatch Precision",
          "description": "Mismatch flags identify evidence-supported representational or regime mismatch rather than merely unfavorable predictions.",
          "pass_condition": "Mismatch detection exceeds naive baselines and meets study-specific precision requirements.",
          "failure_condition": "Low or unfavorable results are routinely relabeled as mismatch without independent evidence.",
          "metric_refs": [
            "PA-M20",
            "PA-M21",
            "PA-M22"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-13",
          "name": "Favorability Symmetry",
          "description": "Substrate-aware interpretation applies comparable evidence standards to favorable and adverse reinterpretations.",
          "pass_condition": "Both positive and negative effects are detected under equivalent criteria.",
          "failure_condition": "The framework systematically favors flattering reinterpretation.",
          "metric_refs": [
            "PA-M14",
            "PA-M43",
            "PA-M44"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-14",
          "name": "Counterfactual Stability",
          "description": "Irrelevant perturbations do not cause large changes while relevant changes remain detectable.",
          "pass_condition": "Robustness and sensitivity meet preregistered criteria.",
          "failure_condition": "Outputs are unstable to irrelevant changes or insensitive to meaningful ones.",
          "metric_refs": [
            "PA-M33",
            "PA-M34",
            "PA-M35"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-15",
          "name": "Fairness",
          "description": "Errors, uncertainty, evidence coverage, mismatch, abstention, and escalation are examined across relevant contexts and groups.",
          "pass_condition": "Material disparities are documented, investigated, and appropriately managed.",
          "failure_condition": "Material disparities are ignored or concealed by aggregate performance.",
          "metric_refs": [
            "PA-M37",
            "PA-M38",
            "PA-M39",
            "PA-M40",
            "PA-M41",
            "PA-M42",
            "PA-M43",
            "PA-M44"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-16",
          "name": "Explainability",
          "description": "Qualified reviewers can reconstruct what was observed and why an interpretation was produced.",
          "pass_condition": "Evidence reconstruction and explanation completeness satisfy study-specific criteria.",
          "failure_condition": "Results depend on undocumented intuition or opaque reasoning.",
          "metric_refs": [
            "PA-M45",
            "PA-M46"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-17",
          "name": "Subject Legibility",
          "description": "Human-facing profiles use accessible language and distinguish observation from experimental interpretation.",
          "pass_condition": "Subjects can inspect, understand, and contest consequential profile claims.",
          "failure_condition": "Profile language creates unwarranted identity or validity claims.",
          "metric_refs": [
            "PA-M46",
            "PA-M48"
          ],
          "status": "not_tested"
        },
        {
          "id": "VCR-18",
          "name": "Non-Degradation",
          "description": "Additional adapters do not silently reduce accuracy, fairness, interpretability, or operational practicality.",
          "pass_condition": "Material degradation is absent or explicitly bounded and justified for the intended use.",
          "failure_condition": "Additional complexity worsens important properties without documented justification.",
          "metric_refs": [
            "PA-M10",
            "PA-M11",
            "PA-M36",
            "PA-M51"
          ],
          "status": "not_tested"
        }
      ],
      "falsification_conditions": [
        "Dimension observations cannot be made reliably.",
        "Profiles remain unstable under comparable conditions.",
        "Unfavorable conventional results are routinely relabeled as model mismatch.",
        "Richer narrative interpretations outperform evidence requirements rather than baselines.",
        "Adapters add complexity without measurable value.",
        "Proposed dimensions cannot be empirically distinguished.",
        "Confidence labels do not calibrate to observed reliability.",
        "The framework increases material subgroup disparities without adequate mitigation.",
        "The framework cannot abstain when evidence is insufficient.",
        "The framework becomes a hidden scalar-ranking system."
      ],
      "reporting_requirements": [
        "intended use",
        "population or system class",
        "sample and recruitment method",
        "measurement substrates",
        "operating regimes",
        "tasks",
        "raters",
        "missing-data handling",
        "metrics",
        "thresholds",
        "uncertainty",
        "subgroup results",
        "adverse findings",
        "unused metrics",
        "limitations",
        "conflicts of interest",
        "version and provenance",
        "reproducibility materials"
      ],
      "threshold_policy": {
        "status": "study_specific",
        "universal_thresholds": false,
        "preregistration_required": true,
        "post_hoc_changes_disclosed": true
      },
      "human_subjects_requirements": [
        "consent where applicable",
        "privacy protection",
        "appropriate oversight",
        "data governance",
        "qualified interpretation for consequential assessment"
      ]
    },
    "metrics": [
      {
        "id": "PA-M01",
        "name": "Dimension Evidence Coverage",
        "category": "evidence",
        "purpose": "Measure evidence coverage for a declared dimension.",
        "definition": "Proportion of required dimension indicators supported by available evidence.",
        "formula": "supported_indicators / required_indicators",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["supported_indicators", "required_indicators"],
        "applicability": ["dimension"],
        "interpretation": "Higher values indicate broader evidence coverage but do not establish validity.",
        "limitations": ["Depends on valid indicator definitions."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Ratio",
        "missing_data_policy": "Missing required indicators remain missing rather than being inferred.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M02",
        "name": "Profile Evidence Coverage",
        "category": "evidence",
        "purpose": "Measure coverage across applicable profile dimensions.",
        "definition": "Proportion of applicable dimensions with sufficient evidence.",
        "formula": "dimensions_with_sufficient_evidence / applicable_dimensions",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["dimensions_with_sufficient_evidence", "applicable_dimensions"],
        "applicability": ["profile"],
        "interpretation": "Describes profile coverage rather than intelligence or overall capability.",
        "limitations": ["Sensitive to applicability definitions."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Ratio",
        "missing_data_policy": "Unknown dimensions remain explicitly unknown.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M03",
        "name": "Evidence Independence Ratio",
        "category": "evidence",
        "purpose": "Estimate independence of supporting evidence sources.",
        "definition": "Ratio of independently sourced evidence to total evidence sources.",
        "formula": "independent_evidence_sources / total_evidence_sources",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["independent_evidence_sources", "total_evidence_sources"],
        "applicability": ["dimension", "profile"],
        "interpretation": "Higher values indicate broader evidence independence.",
        "limitations": ["Independence must be operationally defined."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Ratio after evidence provenance classification",
        "missing_data_policy": "Unclear dependencies are not counted as independent.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M04",
        "name": "Test-Retest Stability",
        "category": "reliability",
        "purpose": "Measure repeated-observation stability.",
        "definition": "Agreement across comparable repeated measurements.",
        "scale": "statistic-specific",
        "direction": "higher_is_better",
        "inputs": ["observation_t1", "observation_t2"],
        "applicability": ["dimension", "profile"],
        "interpretation": "Higher values indicate greater repeatability where stability is theoretically expected.",
        "limitations": ["Not all dimensions are expected to remain constant over time."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Select a reliability statistic appropriate to the measurement scale.",
        "missing_data_policy": "Use a preregistered missing-data procedure.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M05",
        "name": "Alternate-Form Stability",
        "category": "reliability",
        "purpose": "Measure consistency across alternate tasks targeting the same dimension.",
        "definition": "Agreement between alternate-form dimension results.",
        "formula": "agreement(form_a, form_b)",
        "scale": "statistic-specific",
        "direction": "higher_is_better",
        "inputs": ["form_a", "form_b"],
        "applicability": ["dimension"],
        "interpretation": "Higher values support consistency across alternate forms.",
        "limitations": ["Requires defensible form equivalence."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Agreement statistic appropriate to scale.",
        "missing_data_policy": "Incomplete form pairs are reported separately.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M06",
        "name": "Inter-Rater Agreement",
        "category": "reliability",
        "purpose": "Measure agreement among independent evaluators.",
        "definition": "Agreement between qualified independent evaluators using the same evidence and rubric.",
        "scale": "statistic-specific",
        "direction": "higher_is_better",
        "inputs": ["rater_results"],
        "applicability": ["human-scored dimensions"],
        "interpretation": "Higher values indicate reduced evaluator dependence.",
        "limitations": ["Statistic must match rating scale and study design."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Kappa, alpha, ICC, or other preregistered appropriate statistic.",
        "missing_data_policy": "Missing ratings are explicitly reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M07",
        "name": "Profile Topology Stability",
        "category": "stability",
        "purpose": "Measure stability of multidimensional profile shape.",
        "definition": "Similarity between appropriately normalized profiles across repeated observations.",
        "formula": "similarity(normalized_profile_t1, normalized_profile_t2)",
        "scale": "similarity-specific",
        "direction": "higher_is_better",
        "inputs": ["profile_t1", "profile_t2"],
        "applicability": ["profile"],
        "interpretation": "Higher values indicate greater profile-shape stability.",
        "limitations": ["Must not conceal meaningful dimension-level change."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Preregistered profile similarity measure.",
        "missing_data_policy": "Profile comparisons identify dimensions excluded because of missing evidence.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M08",
        "name": "Convergent Association",
        "category": "validity",
        "purpose": "Test expected relationships with independently observed related capabilities.",
        "definition": "Association between a proposed dimension and a related external measure.",
        "formula": "association(proposed_dimension, related_external_measure)",
        "scale": "association-specific",
        "direction": "context_dependent",
        "inputs": ["dimension", "external_measure"],
        "applicability": ["dimension"],
        "interpretation": "Interpret relative to preregistered theory and expected direction.",
        "limitations": ["Convergence does not independently establish construct identity."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Preregistered association method.",
        "missing_data_policy": "Use declared study-specific treatment.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M09",
        "name": "Discriminant Separation",
        "category": "validity",
        "purpose": "Test whether proposed dimensions remain distinct from unrelated constructs.",
        "definition": "Difference between related and unrelated associations or equivalent discriminant analysis.",
        "formula": "related_association - unrelated_association",
        "scale": "analysis-specific",
        "direction": "higher_is_better",
        "inputs": ["related_association", "unrelated_association"],
        "applicability": ["dimension"],
        "interpretation": "Greater separation supports distinct measurement where theoretically expected.",
        "limitations": ["Requires defensible comparison constructs."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Preregistered discriminant analysis.",
        "missing_data_policy": "Study-specific.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M10",
        "name": "Incremental Explanatory Value",
        "category": "validity",
        "purpose": "Measure explanatory improvement beyond a simpler baseline.",
        "definition": "Difference in declared explanatory performance between full and baseline models.",
        "formula": "performance(full_model) - performance(baseline_model)",
        "scale": "outcome-specific",
        "direction": "higher_is_better",
        "inputs": ["full_model", "baseline_model"],
        "applicability": ["model comparison"],
        "interpretation": "Positive values may indicate added explanatory value when complexity and uncertainty are also considered.",
        "limitations": ["Complexity alone can improve apparent fit."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Study-specific with complexity controls.",
        "missing_data_policy": "Study-specific.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M11",
        "name": "Incremental Predictive Value",
        "category": "validity",
        "purpose": "Measure out-of-sample predictive improvement over baseline.",
        "definition": "Difference between baseline and full-model prediction error or equivalent predictive utility.",
        "formula": "baseline_error - full_model_error",
        "scale": "outcome-specific",
        "direction": "higher_is_better",
        "inputs": ["baseline_predictions", "full_model_predictions", "outcomes"],
        "applicability": ["predictive models"],
        "interpretation": "Positive improvement must be interpreted with calibration, fairness, and complexity.",
        "limitations": ["No single predictive metric is universally appropriate."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Out-of-sample study-specific evaluation.",
        "missing_data_policy": "Preregistered.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M12",
        "name": "Substrate Effect Magnitude",
        "category": "substrate",
        "purpose": "Measure change in observed performance across substrates.",
        "definition": "Standardized or otherwise appropriate difference between substrate conditions.",
        "formula": "standardized_difference(performance_a, performance_b)",
        "scale": "effect-size-specific",
        "direction": "descriptive",
        "inputs": ["substrate_a", "substrate_b", "performance"],
        "applicability": ["cross-substrate studies"],
        "interpretation": "A measurable difference requires explanation but does not by itself establish mismatch.",
        "limitations": ["Can reflect task difficulty or other confounds."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Study-specific effect size.",
        "missing_data_policy": "Preregistered.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M13",
        "name": "Substrate Effect Replicability",
        "category": "substrate",
        "purpose": "Measure replication of observed substrate effects.",
        "definition": "Proportion of eligible replications reproducing the preregistered effect.",
        "formula": "replicated_effects / eligible_replications",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["replication_results"],
        "applicability": ["cross-substrate studies"],
        "interpretation": "Higher values support repeatability of a substrate effect.",
        "limitations": ["Must be interpreted with effect magnitude and uncertainty."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Replication ratio plus effect estimates.",
        "missing_data_policy": "Incomplete replications reported separately.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M14",
        "name": "Substrate Symmetry",
        "category": "substrate",
        "purpose": "Detect favorability bias in substrate-effect detection.",
        "definition": "Minimum of detection rates for beneficial and adverse substrate effects.",
        "formula": "min(detection_rate_positive, detection_rate_negative)",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["positive_effect_detection", "negative_effect_detection"],
        "applicability": ["cross-substrate studies"],
        "interpretation": "Low values may indicate directional reinterpretation bias.",
        "limitations": ["Requires sufficient positive and adverse reference cases."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Symmetry comparison.",
        "missing_data_policy": "Insufficient directional cases produce insufficient_evidence.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M15",
        "name": "Substrate Specificity",
        "category": "substrate",
        "purpose": "Estimate whether observed differences remain after relevant controls.",
        "definition": "Substrate-associated effect after accounting for declared confounds.",
        "formula": "substrate_effect_after_controls",
        "scale": "analysis-specific",
        "direction": "descriptive",
        "inputs": ["substrate", "performance", "controls"],
        "applicability": ["cross-substrate studies"],
        "interpretation": "Supports substrate-specific interpretation when alternative explanations are bounded.",
        "limitations": ["Cannot control unknown confounds."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Study-specific controlled analysis.",
        "missing_data_policy": "Preregistered.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M16",
        "name": "Regime Transition Detection Rate",
        "category": "regime",
        "purpose": "Measure detection of reference regime transitions.",
        "definition": "Proportion of reference transitions detected.",
        "formula": "detected_transitions / reference_transitions",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["detected_transitions", "reference_transitions"],
        "applicability": ["regime studies"],
        "interpretation": "Higher values indicate greater transition sensitivity.",
        "limitations": ["Requires independently meaningful reference transitions."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Detection ratio.",
        "missing_data_policy": "No reference transitions means not_applicable.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M17",
        "name": "False Regime Alarm Rate",
        "category": "regime",
        "purpose": "Measure false regime-transition declarations.",
        "definition": "False transition flags divided by stable-regime opportunities.",
        "formula": "false_transition_flags / stable_regime_opportunities",
        "scale": "0..1",
        "direction": "lower_is_better",
        "inputs": ["false_transition_flags", "stable_regime_opportunities"],
        "applicability": ["regime studies"],
        "interpretation": "Lower values indicate fewer unsupported regime-change claims.",
        "limitations": ["Depends on valid stable-regime labeling."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "False alarm ratio.",
        "missing_data_policy": "No stable-regime opportunities means not_applicable.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M18",
        "name": "Regime Boundary Error",
        "category": "regime",
        "purpose": "Measure distance between detected and reference boundaries.",
        "definition": "Distance between a detected regime boundary and reference boundary.",
        "formula": "distance(detected_boundary, reference_boundary)",
        "scale": "distance-specific",
        "direction": "lower_is_better",
        "inputs": ["detected_boundary", "reference_boundary"],
        "applicability": ["regime studies"],
        "interpretation": "Lower values indicate closer boundary localization.",
        "limitations": ["Boundary uncertainty must be retained."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Study-specific distance.",
        "missing_data_policy": "Missing reference boundary means not_testable.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M19",
        "name": "Regime-Conditioned Stability",
        "category": "regime",
        "purpose": "Measure within-regime stability.",
        "definition": "Stability of a dimension or profile within a defined regime.",
        "formula": "within_regime_stability",
        "scale": "statistic-specific",
        "direction": "higher_is_better",
        "inputs": ["within_regime_observations"],
        "applicability": ["regime studies"],
        "interpretation": "Helps distinguish measurement instability from between-regime variation.",
        "limitations": ["Requires defensible regime definition."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Appropriate within-regime stability statistic.",
        "missing_data_policy": "Preregistered.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M20",
        "name": "Model-Mismatch Precision",
        "category": "model_mismatch",
        "purpose": "Measure support for mismatch flags.",
        "definition": "Proportion of mismatch flags supported by independent reference evidence.",
        "formula": "supported_mismatch_flags / all_mismatch_flags",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["mismatch_flags", "reference_evidence"],
        "applicability": ["model mismatch studies"],
        "interpretation": "Higher values indicate fewer unsupported mismatch declarations.",
        "limitations": ["Requires meaningful reference definition."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Precision.",
        "missing_data_policy": "No mismatch flags are reported separately.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M21",
        "name": "Model-Mismatch Recall",
        "category": "model_mismatch",
        "purpose": "Measure detection of reference mismatch cases.",
        "definition": "Proportion of reference mismatch cases detected.",
        "formula": "detected_reference_mismatches / all_reference_mismatches",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["detected_mismatches", "reference_mismatches"],
        "applicability": ["model mismatch studies"],
        "interpretation": "Higher values indicate greater sensitivity to supported mismatch.",
        "limitations": ["Must be paired with precision and false positives."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Recall.",
        "missing_data_policy": "No reference mismatches means not_applicable.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M22",
        "name": "Model-Mismatch False Positive Rate",
        "category": "model_mismatch",
        "purpose": "Measure unsupported mismatch flags.",
        "definition": "False mismatch flags divided by reference non-mismatch cases.",
        "formula": "false_mismatch_flags / reference_non_mismatch_cases",
        "scale": "0..1",
        "direction": "lower_is_better",
        "inputs": ["false_mismatch_flags", "reference_non_mismatch_cases"],
        "applicability": ["model mismatch studies"],
        "interpretation": "Lower values indicate less overuse of mismatch explanations.",
        "limitations": ["Requires reference non-mismatch cases."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "False positive rate.",
        "missing_data_policy": "No reference non-mismatch cases means not_applicable.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M23",
        "name": "Mismatch Evidence Strength",
        "category": "model_mismatch",
        "purpose": "Summarize declared evidence supporting a mismatch interpretation without creating a person-level intelligence score.",
        "definition": "Transparent evidence-strength representation using predefined components.",
        "scale": "study-specific",
        "direction": "higher_is_better",
        "inputs": ["independent_sources", "replication", "substrate_effect", "regime_alignment", "counterfactual_consistency", "uncertainty"],
        "applicability": ["model mismatch studies"],
        "interpretation": "Higher values may indicate stronger mismatch evidence if the aggregation rule is separately validated.",
        "limitations": ["Aggregation can conceal disagreement and must not become a hidden capability score."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Transparent study-specific aggregation.",
        "missing_data_policy": "Missing components remain explicit.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M24",
        "name": "Cross-Observation Coherence",
        "category": "coherence",
        "purpose": "Measure agreement among observations expected to relate.",
        "definition": "Proportion of eligible observation relationships that are coherent under predefined criteria.",
        "formula": "coherent_observation_pairs / eligible_observation_pairs",
        "scale": "0..1",
        "direction": "descriptive",
        "inputs": ["observation_pairs"],
        "applicability": ["profile"],
        "interpretation": "Low coherence can reflect heterogeneous capability, poor measurement, multiple regimes, or invalid assumptions.",
        "limitations": ["High coherence does not by itself establish truth."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Pairwise coherence classification.",
        "missing_data_policy": "Ineligible pairs excluded and reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M25",
        "name": "Profile Contradiction Density",
        "category": "coherence",
        "purpose": "Measure unresolved contradictions.",
        "definition": "Unresolved contradictions divided by evaluated relationships.",
        "formula": "unresolved_contradictions / evaluated_relationships",
        "scale": "0..1",
        "direction": "descriptive",
        "inputs": ["unresolved_contradictions", "evaluated_relationships"],
        "applicability": ["profile"],
        "interpretation": "Contradictions may identify measurement problems, asymmetry, or regime dependence.",
        "limitations": ["Contradiction is not automatically error."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Ratio.",
        "missing_data_policy": "Unevaluated relationships are reported separately.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M26",
        "name": "Dimension Drift Rate",
        "category": "drift",
        "purpose": "Measure dimension change over a defined interval.",
        "definition": "Observed dimension change normalized to an observation interval when appropriate.",
        "formula": "dimension_change / observation_interval",
        "scale": "dimension-specific",
        "direction": "descriptive",
        "inputs": ["dimension_change", "observation_interval"],
        "applicability": ["longitudinal dimension observations"],
        "interpretation": "Requires assumptions about expected stability.",
        "limitations": ["Change may be learning, context shift, noise, or actual drift."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Study-specific longitudinal analysis.",
        "missing_data_policy": "Missing intervals are explicit.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M27",
        "name": "Profile Drift Magnitude",
        "category": "drift",
        "purpose": "Measure overall profile change.",
        "definition": "Distance between profiles at different observations.",
        "formula": "distance(profile_t1, profile_t2)",
        "scale": "distance-specific",
        "direction": "descriptive",
        "inputs": ["profile_t1", "profile_t2"],
        "applicability": ["longitudinal profiles"],
        "interpretation": "Overall drift should be decomposed into dimension-level change.",
        "limitations": ["Profile distance can hide direction and cause of change."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Preregistered profile distance.",
        "missing_data_policy": "Missing dimensions explicitly reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M28",
        "name": "Confidence Calibration Error",
        "category": "calibration",
        "purpose": "Measure correspondence between confidence and observed correctness or reproducibility.",
        "definition": "Average absolute difference between stated confidence and observed frequency under an appropriate calibration design.",
        "formula": "average(abs(stated_confidence - observed_frequency))",
        "scale": "0..1",
        "direction": "lower_is_better",
        "inputs": ["stated_confidence", "observed_frequency"],
        "applicability": ["probabilistic or mapped-confidence assessments"],
        "interpretation": "Lower values indicate better calibration.",
        "limitations": ["Ordinal confidence labels require a validated mapping before numeric treatment."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Calibration analysis.",
        "missing_data_policy": "Unmapped confidence remains nonnumeric.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M29",
        "name": "Brier Score",
        "category": "calibration",
        "purpose": "Measure probabilistic prediction accuracy for appropriate outcomes.",
        "definition": "Mean squared difference between forecast probabilities and observed binary outcomes.",
        "formula": "mean((forecast_probability - outcome)^2)",
        "scale": "0..1 for binary events",
        "direction": "lower_is_better",
        "inputs": ["forecast_probability", "outcome"],
        "applicability": ["probabilistic binary forecasts"],
        "interpretation": "Lower values indicate better probabilistic accuracy for the specified setting.",
        "limitations": ["Not appropriate for every outcome type."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Standard Brier score where applicable.",
        "missing_data_policy": "Incomplete forecast-outcome pairs excluded and reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M30",
        "name": "Abstention Rate",
        "category": "uncertainty",
        "purpose": "Measure how often the framework abstains.",
        "definition": "Abstained results divided by eligible results.",
        "formula": "abstained_results / eligible_results",
        "scale": "0..1",
        "direction": "descriptive",
        "inputs": ["abstained_results", "eligible_results"],
        "applicability": ["assessment"],
        "interpretation": "Descriptive only and must be paired with abstention quality.",
        "limitations": ["Neither high nor low abstention is inherently preferable."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Ratio.",
        "missing_data_policy": "Eligibility rules preregistered.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M31",
        "name": "Abstention Utility",
        "category": "uncertainty",
        "purpose": "Measure whether abstention reduces unsupported or erroneous assessments at acceptable cost.",
        "definition": "Error reduction attributed to abstention minus declared abstention cost.",
        "formula": "error_reduction_after_abstention - abstention_cost",
        "scale": "utility-specific",
        "direction": "higher_is_better",
        "inputs": ["error_reduction", "abstention_cost"],
        "applicability": ["assessment"],
        "interpretation": "Positive values may indicate useful abstention under the declared utility model.",
        "limitations": ["Depends heavily on the declared cost model."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Use-case-specific utility analysis.",
        "missing_data_policy": "Undefined costs prohibit calculation.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M32",
        "name": "Unsupported Assertion Rate",
        "category": "uncertainty",
        "purpose": "Detect claims that exceed available evidence.",
        "definition": "Assertions lacking sufficient supporting evidence divided by all profile assertions.",
        "formula": "unsupported_assertions / all_profile_assertions",
        "scale": "0..1",
        "direction": "lower_is_better",
        "inputs": ["unsupported_assertions", "profile_assertions"],
        "applicability": ["profile", "assessment"],
        "interpretation": "Lower values indicate better evidence discipline.",
        "limitations": ["Depends on explicit evidence sufficiency rules."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Evidence-audit ratio.",
        "missing_data_policy": "Missing evidence counts as unsupported unless explicitly abstained.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M33",
        "name": "Irrelevant Perturbation Stability",
        "category": "robustness",
        "purpose": "Measure stability to irrelevant input changes.",
        "definition": "Similarity between original and irrelevantly perturbed results.",
        "formula": "similarity(original_result, irrelevant_perturbation_result)",
        "scale": "similarity-specific",
        "direction": "higher_is_better",
        "inputs": ["original_result", "perturbed_result"],
        "applicability": ["assessment"],
        "interpretation": "Higher stability is preferable when perturbations are genuinely irrelevant.",
        "limitations": ["Irrelevance must be independently justified."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Study-specific similarity measure.",
        "missing_data_policy": "Incomplete pairs excluded and reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M34",
        "name": "Relevant Change Sensitivity",
        "category": "counterfactual",
        "purpose": "Measure response to meaningful evidence changes.",
        "definition": "Proportion of introduced meaningful changes detected in the result.",
        "formula": "detected_meaningful_changes / introduced_meaningful_changes",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["introduced_changes", "detected_changes"],
        "applicability": ["assessment"],
        "interpretation": "Higher values indicate appropriate responsiveness.",
        "limitations": ["Requires validated relevant changes."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Sensitivity ratio.",
        "missing_data_policy": "No introduced changes means not_applicable.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M35",
        "name": "Task-Order Sensitivity",
        "category": "robustness",
        "purpose": "Measure undesired result changes caused by task ordering.",
        "definition": "Distance between results produced by otherwise equivalent task orders.",
        "formula": "distance(result_order_a, result_order_b)",
        "scale": "distance-specific",
        "direction": "lower_is_better",
        "inputs": ["result_order_a", "result_order_b"],
        "applicability": ["assessment"],
        "interpretation": "Lower values indicate reduced order sensitivity when order is theoretically irrelevant.",
        "limitations": ["Order may be meaningful in some longitudinal tasks."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Study-specific distance.",
        "missing_data_policy": "Incomplete task-order pairs reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M36",
        "name": "Adapter Ablation Effect",
        "category": "validity",
        "purpose": "Measure the incremental contribution of an adapter.",
        "definition": "Difference between full-adapter performance and performance with a specified adapter removed.",
        "formula": "performance(full_adapter_set) - performance(without_adapter_x)",
        "scale": "outcome-specific",
        "direction": "context_dependent",
        "inputs": ["full_adapter_model", "ablated_model"],
        "applicability": ["adapter validation"],
        "interpretation": "Tests whether an adapter contributes measurable value rather than terminology alone.",
        "limitations": ["Interactions among adapters may complicate interpretation."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Preregistered ablation study.",
        "missing_data_policy": "Study-specific.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M37",
        "name": "Group Error Difference",
        "category": "fairness",
        "purpose": "Compare error rates across relevant groups or contexts.",
        "definition": "Difference between defined group error rates.",
        "formula": "error_rate_group_a - error_rate_group_b",
        "scale": "difference",
        "direction": "context_dependent",
        "inputs": ["group_error_rates"],
        "applicability": ["fairness studies"],
        "interpretation": "A difference is a signal requiring contextual interpretation.",
        "limitations": ["Does not establish fairness or unfairness by itself."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Study-specific error comparison.",
        "missing_data_policy": "Insufficient groups reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M38",
        "name": "Group Calibration Difference",
        "category": "fairness",
        "purpose": "Compare confidence calibration across relevant groups.",
        "definition": "Difference in calibration error between groups.",
        "formula": "calibration_error_group_a - calibration_error_group_b",
        "scale": "difference",
        "direction": "context_dependent",
        "inputs": ["group_calibration_errors"],
        "applicability": ["fairness studies"],
        "interpretation": "Material differences warrant investigation.",
        "limitations": ["Depends on valid calibration measurement."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Calibration comparison.",
        "missing_data_policy": "Insufficient groups reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M39",
        "name": "Mismatch Flag Rate Difference",
        "category": "fairness",
        "purpose": "Compare mismatch-flag rates across relevant groups.",
        "definition": "Difference between group mismatch-flag rates.",
        "formula": "mismatch_flag_rate_group_a - mismatch_flag_rate_group_b",
        "scale": "difference",
        "direction": "context_dependent",
        "inputs": ["group_mismatch_rates"],
        "applicability": ["fairness studies"],
        "interpretation": "Differences require investigation and are not automatically proof of unfairness.",
        "limitations": ["Underlying mismatch prevalence may differ."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Group rate comparison.",
        "missing_data_policy": "Insufficient groups reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M40",
        "name": "Abstention Coverage Difference",
        "category": "fairness",
        "purpose": "Compare abstention behavior across relevant groups.",
        "definition": "Difference between group abstention rates.",
        "formula": "abstention_rate_group_a - abstention_rate_group_b",
        "scale": "difference",
        "direction": "context_dependent",
        "inputs": ["group_abstention_rates"],
        "applicability": ["fairness studies"],
        "interpretation": "Material differences warrant examination of evidence coverage and model fit.",
        "limitations": ["Equal abstention rates do not establish fairness."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Group rate comparison.",
        "missing_data_policy": "Insufficient groups reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M41",
        "name": "Escalation Rate Difference",
        "category": "fairness",
        "purpose": "Compare review-escalation rates across relevant groups.",
        "definition": "Difference between group human-review rates.",
        "formula": "human_review_rate_group_a - human_review_rate_group_b",
        "scale": "difference",
        "direction": "context_dependent",
        "inputs": ["group_review_rates"],
        "applicability": ["fairness studies"],
        "interpretation": "Differences require evaluation in light of evidence coverage, uncertainty, and harms.",
        "limitations": ["Review may be protective or burdensome depending on context."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Group rate comparison.",
        "missing_data_policy": "Insufficient groups reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M42",
        "name": "Evidence Coverage Difference",
        "category": "fairness",
        "purpose": "Compare evidence coverage across relevant groups.",
        "definition": "Difference between group evidence-coverage measures.",
        "formula": "evidence_coverage_group_a - evidence_coverage_group_b",
        "scale": "difference",
        "direction": "context_dependent",
        "inputs": ["group_evidence_coverage"],
        "applicability": ["fairness studies"],
        "interpretation": "May reveal unequal representation in available evidence or tasks.",
        "limitations": ["Coverage difference does not identify its cause."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Group coverage comparison.",
        "missing_data_policy": "Insufficient groups reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M43",
        "name": "False Favorable Reinterpretation Rate",
        "category": "fairness",
        "purpose": "Detect unsupported favorable reinterpretations.",
        "definition": "Unsupported favorable reinterpretations divided by favorable reinterpretations.",
        "formula": "unsupported_favorable_reinterpretations / favorable_reinterpretations",
        "scale": "0..1",
        "direction": "lower_is_better",
        "inputs": ["unsupported_favorable_reinterpretations", "favorable_reinterpretations"],
        "applicability": ["reinterpretation studies"],
        "interpretation": "Lower values indicate stronger evidence discipline for favorable reinterpretation.",
        "limitations": ["Requires independent support criteria."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Rate.",
        "missing_data_policy": "No favorable reinterpretations means not_applicable.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M44",
        "name": "False Adverse Reinterpretation Rate",
        "category": "fairness",
        "purpose": "Detect unsupported adverse reinterpretations.",
        "definition": "Unsupported adverse reinterpretations divided by adverse reinterpretations.",
        "formula": "unsupported_adverse_reinterpretations / adverse_reinterpretations",
        "scale": "0..1",
        "direction": "lower_is_better",
        "inputs": ["unsupported_adverse_reinterpretations", "adverse_reinterpretations"],
        "applicability": ["reinterpretation studies"],
        "interpretation": "Lower values indicate stronger evidence discipline for adverse reinterpretation.",
        "limitations": ["Requires independent support criteria."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Rate.",
        "missing_data_policy": "No adverse reinterpretations means not_applicable.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M45",
        "name": "Evidence Reconstruction Rate",
        "category": "explainability",
        "purpose": "Measure whether qualified reviewers can reconstruct assessment conclusions.",
        "definition": "Successfully reconstructed results divided by reviewed results.",
        "formula": "successfully_reconstructed_results / reviewed_results",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["review_results"],
        "applicability": ["assessment"],
        "interpretation": "Higher values indicate stronger evidence traceability and explainability.",
        "limitations": ["Reviewer qualification and rubric matter."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Independent review.",
        "missing_data_policy": "Incomplete reviews excluded and reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M46",
        "name": "Explanation Completeness",
        "category": "explainability",
        "purpose": "Measure presence of required explanatory components.",
        "definition": "Present required explanation components divided by total required components.",
        "formula": "present_components / required_components",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["explanation_components"],
        "applicability": ["assessment"],
        "interpretation": "Higher values indicate more complete reporting, not necessarily more correct conclusions.",
        "limitations": ["Completeness does not prove validity."],
        "subgroup_required": false,
        "lifecycle": "proposed",
        "calculation_method": "Checklist ratio.",
        "missing_data_policy": "Missing required elements count as absent.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M47",
        "name": "Reviewer Override Rate",
        "category": "review",
        "purpose": "Track qualified-reviewer overrides.",
        "definition": "Reviewer overrides divided by reviewed results.",
        "formula": "reviewer_overrides / reviewed_results",
        "scale": "0..1",
        "direction": "descriptive",
        "inputs": ["reviewer_overrides", "reviewed_results"],
        "applicability": ["human review"],
        "interpretation": "Requires categorization of override reasons.",
        "limitations": ["High or low values are not inherently better without context."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Review audit.",
        "missing_data_policy": "Incomplete reviews reported.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M48",
        "name": "Contest Resolution Rate",
        "category": "review",
        "purpose": "Measure documented resolution of assessment contests.",
        "definition": "Resolved contests divided by submitted contests.",
        "formula": "resolved_contests / submitted_contests",
        "scale": "0..1",
        "direction": "higher_is_better",
        "inputs": ["resolved_contests", "submitted_contests"],
        "applicability": ["human-facing assessment"],
        "interpretation": "Resolution can retain, change, or explicitly leave unresolved the original assessment.",
        "limitations": ["Resolution quality requires separate evaluation."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Case audit.",
        "missing_data_policy": "Open cases reported separately.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M49",
        "name": "Profile Completion Rate",
        "category": "operational",
        "purpose": "Measure completion of initiated profiles.",
        "definition": "Completed profiles divided by initiated profiles.",
        "formula": "completed_profiles / initiated_profiles",
        "scale": "0..1",
        "direction": "descriptive",
        "inputs": ["completed_profiles", "initiated_profiles"],
        "applicability": ["operations"],
        "interpretation": "Describes operational completion only.",
        "limitations": ["Completion does not indicate validity or quality."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Ratio.",
        "missing_data_policy": "Incomplete profiles remain incomplete.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M50",
        "name": "Time to Review",
        "category": "operational",
        "purpose": "Measure elapsed review time.",
        "definition": "Review completion timestamp minus review start timestamp.",
        "formula": "review_completion_time - review_start_time",
        "scale": "time",
        "direction": "context_dependent",
        "inputs": ["review_start_time", "review_completion_time"],
        "applicability": ["human review"],
        "interpretation": "Must be evaluated relative to review quality and consequence.",
        "limitations": ["Faster is not always better."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Elapsed time.",
        "missing_data_policy": "Open reviews remain open.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M51",
        "name": "Evidence Acquisition Burden",
        "category": "operational",
        "purpose": "Track the burden required to construct richer profiles.",
        "definition": "Structured record of subject time, evaluator time, computational cost, tool requirements, accessibility burden, and privacy burden.",
        "scale": "multicomponent",
        "direction": "lower_is_better",
        "inputs": ["subject_time", "evaluator_time", "computational_cost", "tool_requirements", "accessibility_burden", "privacy_burden"],
        "applicability": ["assessment", "validation"],
        "interpretation": "Richer profiles must justify their additional burden.",
        "limitations": ["Components may not be reducible to a defensible single number."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Component-wise reporting preferred.",
        "missing_data_policy": "Missing burden components remain explicit.",
        "threshold": {"status": "study_specific"}
      },
      {
        "id": "PA-M52",
        "name": "Decision Deferral Rate",
        "category": "operational",
        "purpose": "Measure frequency of deferred decisions where evidence is insufficient.",
        "definition": "Deferred decisions divided by decision opportunities.",
        "formula": "deferred_decisions / decision_opportunities",
        "scale": "0..1",
        "direction": "descriptive",
        "inputs": ["deferred_decisions", "decision_opportunities"],
        "applicability": ["context-validated decision studies only"],
        "interpretation": "Must be paired with error reduction, fairness, and harm avoidance.",
        "limitations": ["Not currently authorized for high-stakes deployment."],
        "subgroup_required": true,
        "lifecycle": "proposed",
        "calculation_method": "Ratio.",
        "missing_data_policy": "Undefined decision opportunities prohibit calculation.",
        "threshold": {"status": "study_specific"}
      }
    ],
    "ethics": {
      "status": "experimental",
      "principles": [
        "A model of a person is not the person.",
        "Preserve observation boundaries.",
        "Do not convert multidimensional observations into hidden universal rankings.",
        "Do not guarantee favorable reinterpretation.",
        "Treat uncertainty as a legitimate result.",
        "Require evidence for model-mismatch claims.",
        "Preserve contestability.",
        "Protect privacy.",
        "Permit deprecation and rejection of failed dimensions or adapters."
      ],
      "invariants": [
        "prediction != identity",
        "measurement != total_capability",
        "capability != human_worth",
        "detail != validity",
        "complexity != truth",
        "correlation != causation",
        "profile != destiny",
        "model_fit != subject_value",
        "unknown != failure",
        "difference != superiority"
      ],
      "prohibited_uses": [
        "assigning human worth",
        "covert social ranking",
        "unvalidated automated adverse decisions",
        "evading protections governing established assessments",
        "persistent cognitive tracking without legitimate governance",
        "unsupported sensitive-trait inference",
        "discriminatory population ranking"
      ],
      "high_stakes_policy": {
        "decision_authority": "none",
        "independent_use": false,
        "separate_validation_required": true
      },
      "consent": {
        "required": true,
        "description": "Real-person assessment should use an appropriate consent and awareness process for the context.",
        "requirements": [
          "declare assessment purpose",
          "declare collected information",
          "declare intended use",
          "declare access and retention",
          "declare AI participation where applicable"
        ],
        "exceptions": []
      },
      "privacy": {
        "required": true,
        "description": "Multidimensional cognitive and behavioral profiles may be sensitive and should follow data-minimization and appropriate governance practices.",
        "requirements": [
          "data minimization",
          "purpose limitation",
          "retention controls",
          "access controls",
          "avoid covert tracking"
        ],
        "exceptions": []
      },
      "contestability": {
        "required": true,
        "description": "Consequential human-facing profiles require mechanisms for evidence inspection, correction, contextual supplementation, and review.",
        "requirements": [
          "evidence inspection",
          "correction pathway",
          "context submission",
          "review pathway",
          "preserve unresolved disagreement"
        ],
        "exceptions": [
          "synthetic demonstration"
        ]
      },
      "temporal_limits": {
        "required": true,
        "description": "Profiles represent observations under particular conditions and should not be treated as timeless identity claims.",
        "requirements": [
          "timestamp",
          "framework version",
          "observed substrates",
          "observed regimes",
          "reassessment state"
        ],
        "exceptions": []
      },
      "accessibility": {
        "required": true,
        "description": "Accessibility conditions should be distinguished from construct-relevant constraints where possible.",
        "requirements": [
          "record accessibility conditions",
          "avoid treating irrelevant barriers as capability by default"
        ],
        "exceptions": []
      },
      "fairness": {
        "required": true,
        "description": "Fairness analysis should examine errors, uncertainty, evidence coverage, mismatch, abstention, escalation, and downstream effects.",
        "requirements": [
          "subgroup analysis where relevant",
          "evidence coverage analysis",
          "favorability symmetry",
          "adverse reinterpretation analysis"
        ],
        "exceptions": [
          "single synthetic example"
        ]
      },
      "human_review": {
        "required": true,
        "description": "Qualified human review is required before consequential interpretation unless a specific use has separately achieved appropriate validation and governance.",
        "requirements": [
          "review ambiguity",
          "review disputed results",
          "review consequential applications"
        ],
        "exceptions": [
          "synthetic demonstration",
          "non-consequential research exploration"
        ]
      },
      "misuse_boundary": [
        "Do not equate profile shape with identity.",
        "Do not infer global intelligence from incomplete profile coverage.",
        "Do not treat unusual profile topology as automatic superiority.",
        "Do not treat substrate effects as automatic evidence of hidden ability.",
        "Do not treat TriadicFrameworks adapters as validated merely because they are canon-aligned.",
        "Do not use richer measurement as richer surveillance."
      ],
      "known_limits": [
        "No complete theory of intelligence is established.",
        "RIQF dimensions are not validated psychological constructs.",
        "RTT-derived cognitive metrics are experimental.",
        "Cross-species and cross-system equivalence is not established.",
        "Substrate categories are provisional.",
        "Regime categories are provisional.",
        "Causal mechanisms are not established.",
        "The module is not validated for consequential decision-making."
      ],
      "deprecation_supported": true
    },
    "examples": [
      {
        "id": "pax-01",
        "name": "PAX-01 Resonant IQ Fingerprint",
        "type": "resonant_iq_fingerprint",
        "file": "example_resonant_iq_fingerprint.md",
        "synthetic": true,
        "subject_id": "PAX-01",
        "description": "Synthetic demonstration of a multidimensional, substrate-sensitive intelligence profile in which conventional and extended observations disagree.",
        "validation_state": "unvalidated",
        "decision_authority": "none",
        "dimensions_used": [
          "pattern-recognition",
          "structural-reasoning",
          "causal-integration",
          "temporal-reasoning",
          "cross-domain-transfer",
          "regime-recognition",
          "anomaly-detection",
          "ambiguity-navigation",
          "adaptive-reframing",
          "coherence-maintenance",
          "drift-awareness",
          "metacognitive-calibration",
          "long-horizon-integration",
          "tool-collaboration",
          "recovery-recalibration"
        ],
        "adapters_used": [
          "fft",
          "inverted-star",
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "metric_refs": [
          "PA-M01",
          "PA-M02",
          "PA-M04",
          "PA-M05",
          "PA-M06",
          "PA-M07",
          "PA-M08",
          "PA-M09",
          "PA-M10",
          "PA-M12",
          "PA-M13",
          "PA-M14",
          "PA-M20",
          "PA-M21",
          "PA-M28",
          "PA-M32",
          "PA-M36",
          "PA-M45",
          "PA-M46"
        ]
      }
    ],
    "documents": {
      "readme": {
        "id": "readme",
        "file": "README.md",
        "role": "foundation",
        "status": "experimental",
        "anchor": "#README",
        "standalone": true,
        "description": "Module front door and architectural overview.",
        "adapter_refs": [],
        "dimension_refs": [],
        "metric_refs": [],
        "validation_refs": []
      },
      "foundations": {
        "id": "foundations",
        "file": "foundations.md",
        "role": "foundation",
        "status": "experimental",
        "anchor": "#FOUNDATIONS",
        "standalone": true,
        "description": "Conceptual foundations for substrate-aware predictive analytics.",
        "adapter_refs": [],
        "dimension_refs": [],
        "metric_refs": [],
        "validation_refs": []
      },
      "predictive-model-adapter": {
        "id": "predictive-model-adapter",
        "file": "predictive_model_adapter.md",
        "role": "adapter",
        "status": "experimental",
        "anchor": "#PREDICTIVE_MODEL_ADAPTER",
        "standalone": true,
        "description": "Adapter contract for integrating existing predictive models.",
        "adapter_refs": [],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M10",
          "PA-M11",
          "PA-M28"
        ],
        "validation_refs": [
          "VCR-09",
          "VCR-10"
        ]
      },
      "substrate-adapter": {
        "id": "substrate-adapter",
        "file": "substrate_adapter.md",
        "role": "observer",
        "status": "experimental",
        "anchor": "#SUBSTRATE_ADAPTER",
        "standalone": true,
        "description": "General substrate adapter and model-fit layer.",
        "adapter_refs": [
          "fft",
          "inverted-star",
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M12",
          "PA-M13",
          "PA-M14",
          "PA-M15"
        ],
        "validation_refs": [
          "VCR-05",
          "VCR-13"
        ]
      },
      "regime-observer": {
        "id": "regime-observer",
        "file": "regime_observer.md",
        "role": "observer",
        "status": "experimental",
        "anchor": "#REGIME_OBSERVER",
        "standalone": true,
        "description": "Regime compatibility and transition observer.",
        "adapter_refs": [
          "rtt"
        ],
        "dimension_refs": [
          "regime-recognition",
          "temporal-reasoning"
        ],
        "metric_refs": [
          "PA-M16",
          "PA-M17",
          "PA-M18",
          "PA-M19"
        ],
        "validation_refs": [
          "VCR-06"
        ]
      },
      "resonance-observer": {
        "id": "resonance-observer",
        "file": "resonance_observer.md",
        "role": "observer",
        "status": "experimental",
        "anchor": "#RESONANCE_OBSERVER",
        "standalone": true,
        "description": "Contextual amplification, suppression, persistence, and stability observer.",
        "adapter_refs": [
          "resonance"
        ],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M12",
          "PA-M13",
          "PA-M24"
        ],
        "validation_refs": [
          "VCR-05"
        ]
      },
      "drift-observer": {
        "id": "drift-observer",
        "file": "drift_observer.md",
        "role": "observer",
        "status": "experimental",
        "anchor": "#DRIFT_OBSERVER",
        "standalone": true,
        "description": "Longitudinal drift observer.",
        "adapter_refs": [
          "rtt"
        ],
        "dimension_refs": [
          "drift-awareness"
        ],
        "metric_refs": [
          "PA-M26",
          "PA-M27"
        ],
        "validation_refs": [
          "VCR-03"
        ]
      },
      "coherence-observer": {
        "id": "coherence-observer",
        "file": "coherence_observer.md",
        "role": "observer",
        "status": "experimental",
        "anchor": "#COHERENCE_OBSERVER",
        "standalone": true,
        "description": "Cross-observation coherence and contradiction observer.",
        "adapter_refs": [
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "dimension_refs": [
          "coherence-maintenance"
        ],
        "metric_refs": [
          "PA-M24",
          "PA-M25"
        ],
        "validation_refs": [
          "VCR-03"
        ]
      },
      "uncertainty-layer": {
        "id": "uncertainty-layer",
        "file": "uncertainty_layer.md",
        "role": "observer",
        "status": "experimental",
        "anchor": "#UNCERTAINTY_LAYER",
        "standalone": true,
        "description": "Uncertainty, calibration, missing evidence, and abstention layer.",
        "adapter_refs": [],
        "dimension_refs": [
          "metacognitive-calibration"
        ],
        "metric_refs": [
          "PA-M28",
          "PA-M29",
          "PA-M30",
          "PA-M31",
          "PA-M32"
        ],
        "validation_refs": [
          "VCR-10",
          "VCR-11"
        ]
      },
      "counterfactual-layer": {
        "id": "counterfactual-layer",
        "file": "counterfactual_layer.md",
        "role": "observer",
        "status": "experimental",
        "anchor": "#COUNTERFACTUAL_LAYER",
        "standalone": true,
        "description": "Alternate representation and perturbation comparison layer.",
        "adapter_refs": [],
        "dimension_refs": [
          "adaptive-reframing"
        ],
        "metric_refs": [
          "PA-M33",
          "PA-M34",
          "PA-M35"
        ],
        "validation_refs": [
          "VCR-14"
        ]
      },
      "human-review-hook": {
        "id": "human-review-hook",
        "file": "human_review_hook.md",
        "role": "observer",
        "status": "experimental",
        "anchor": "#HUMAN_REVIEW_HOOK",
        "standalone": true,
        "description": "Escalation, review, contestability, and override layer.",
        "adapter_refs": [],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M41",
          "PA-M47",
          "PA-M48",
          "PA-M50"
        ],
        "validation_refs": [
          "VCR-16",
          "VCR-17"
        ]
      },
      "resonant-iq-fingerprint": {
        "id": "resonant-iq-fingerprint",
        "file": "resonant_iq_fingerprint.md",
        "role": "profile",
        "status": "experimental",
        "anchor": "#RESONANT_IQ_FINGERPRINT",
        "standalone": true,
        "description": "Experimental multidimensional and substrate-sensitive intelligence profile grammar.",
        "adapter_refs": [
          "fft",
          "inverted-star",
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "dimension_refs": [
          "pattern-recognition",
          "structural-reasoning",
          "causal-integration",
          "temporal-reasoning",
          "cross-domain-transfer",
          "regime-recognition",
          "anomaly-detection",
          "ambiguity-navigation",
          "adaptive-reframing",
          "coherence-maintenance",
          "drift-awareness",
          "metacognitive-calibration",
          "long-horizon-integration",
          "tool-collaboration",
          "recovery-recalibration"
        ],
        "metric_refs": [
          "PA-M01",
          "PA-M02",
          "PA-M07",
          "PA-M12",
          "PA-M20",
          "PA-M28"
        ],
        "validation_refs": [
          "VCR-01",
          "VCR-02",
          "VCR-03",
          "VCR-05",
          "VCR-12",
          "VCR-13"
        ]
      },
      "intelligence-dimensions": {
        "id": "intelligence-dimensions",
        "file": "intelligence_dimensions.md",
        "role": "profile",
        "status": "experimental",
        "anchor": "#INTELLIGENCE_DIMENSIONS",
        "standalone": true,
        "description": "Registry and definitions for proposed RIQF dimensions.",
        "adapter_refs": [],
        "dimension_refs": [
          "pattern-recognition",
          "structural-reasoning",
          "causal-integration",
          "temporal-reasoning",
          "cross-domain-transfer",
          "regime-recognition",
          "anomaly-detection",
          "ambiguity-navigation",
          "adaptive-reframing",
          "coherence-maintenance",
          "drift-awareness",
          "metacognitive-calibration",
          "long-horizon-integration",
          "tool-collaboration",
          "recovery-recalibration"
        ],
        "metric_refs": [
          "PA-M08",
          "PA-M09"
        ],
        "validation_refs": [
          "VCR-01",
          "VCR-07",
          "VCR-08"
        ]
      },
      "substrate-expression-profile": {
        "id": "substrate-expression-profile",
        "file": "substrate_expression_profile.md",
        "role": "profile",
        "status": "experimental",
        "anchor": "#SUBSTRATE_EXPRESSION_PROFILE",
        "standalone": true,
        "description": "Representation of how observed capability varies across measurement or interaction substrates.",
        "adapter_refs": [
          "resonance",
          "rtt"
        ],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M12",
          "PA-M13",
          "PA-M14",
          "PA-M15"
        ],
        "validation_refs": [
          "VCR-05",
          "VCR-13"
        ]
      },
      "model-mismatch": {
        "id": "model-mismatch",
        "file": "model_mismatch.md",
        "role": "observer",
        "status": "experimental",
        "anchor": "#MODEL_MISMATCH",
        "standalone": true,
        "description": "Model-fit and mismatch inference grammar.",
        "adapter_refs": [
          "inverted-star",
          "rtt"
        ],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M20",
          "PA-M21",
          "PA-M22",
          "PA-M23"
        ],
        "validation_refs": [
          "VCR-12",
          "VCR-13"
        ]
      },
      "adapters": {
        "id": "adapters",
        "file": "adapters.md",
        "role": "adapter",
        "status": "experimental",
        "anchor": "#ADAPTERS",
        "standalone": true,
        "description": "Adapter registry and integration contract.",
        "adapter_refs": [
          "fft",
          "inverted-star",
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M36"
        ],
        "validation_refs": [
          "VCR-09",
          "VCR-18"
        ]
      },
      "fft-adapter": {
        "id": "fft-adapter",
        "file": "FFT_adapter.md",
        "role": "adapter",
        "status": "experimental",
        "anchor": "#FFT_ADAPTER",
        "standalone": true,
        "description": "Framework Field Theory adapter.",
        "adapter_refs": ["fft"],
        "dimension_refs": ["structural-reasoning"],
        "metric_refs": ["PA-M36"],
        "validation_refs": ["VCR-09"]
      },
      "inverted-star-adapter": {
        "id": "inverted-star-adapter",
        "file": "Inverted_Star_adapter.md",
        "role": "adapter",
        "status": "experimental",
        "anchor": "#INVERTED_STAR_ADAPTER",
        "standalone": true,
        "description": "The Inverted Star adapter.",
        "adapter_refs": ["inverted-star"],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M20",
          "PA-M22",
          "PA-M36"
        ],
        "validation_refs": [
          "VCR-12",
          "VCR-13"
        ]
      },
      "structural-detection-adapter": {
        "id": "structural-detection-adapter",
        "file": "Structural_Detection_adapter.md",
        "role": "adapter",
        "status": "experimental",
        "anchor": "#STRUCTURAL_DETECTION_ADAPTER",
        "standalone": true,
        "description": "Structural Detection adapter.",
        "adapter_refs": ["structural-detection"],
        "dimension_refs": [
          "structural-reasoning",
          "pattern-recognition",
          "anomaly-detection"
        ],
        "metric_refs": ["PA-M36"],
        "validation_refs": [
          "VCR-07",
          "VCR-09"
        ]
      },
      "rtt-adapter": {
        "id": "rtt-adapter",
        "file": "RTT_adapter.md",
        "role": "adapter",
        "status": "experimental",
        "anchor": "#RTT_ADAPTER",
        "standalone": true,
        "description": "RTT regime, temporal, drift, continuity, and recalibration adapter.",
        "adapter_refs": ["rtt"],
        "dimension_refs": [
          "regime-recognition",
          "temporal-reasoning",
          "drift-awareness",
          "recovery-recalibration"
        ],
        "metric_refs": [
          "PA-M16",
          "PA-M17",
          "PA-M18",
          "PA-M19",
          "PA-M26",
          "PA-M27",
          "PA-M36"
        ],
        "validation_refs": [
          "VCR-06",
          "VCR-09"
        ]
      },
      "resonance-adapter": {
        "id": "resonance-adapter",
        "file": "resonance_adapter.md",
        "role": "adapter",
        "status": "experimental",
        "anchor": "#RESONANCE_ADAPTER",
        "standalone": true,
        "description": "Contextual amplification and suppression adapter.",
        "adapter_refs": ["resonance"],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M12",
          "PA-M13",
          "PA-M36"
        ],
        "validation_refs": [
          "VCR-05",
          "VCR-09"
        ]
      },
      "validation": {
        "id": "validation",
        "file": "validation.md",
        "role": "validation",
        "status": "experimental",
        "anchor": "#VALIDATION",
        "standalone": true,
        "description": "Validation levels, criteria, falsification requirements, and reporting standards.",
        "adapter_refs": [],
        "dimension_refs": [],
        "metric_refs": [],
        "validation_refs": [
          "VCR-01",
          "VCR-02",
          "VCR-03",
          "VCR-04",
          "VCR-05",
          "VCR-06",
          "VCR-07",
          "VCR-08",
          "VCR-09",
          "VCR-10",
          "VCR-11",
          "VCR-12",
          "VCR-13",
          "VCR-14",
          "VCR-15",
          "VCR-16",
          "VCR-17",
          "VCR-18"
        ]
      },
      "metrics": {
        "id": "metrics",
        "file": "metrics.md",
        "role": "metrics",
        "status": "experimental",
        "anchor": "#METRICS",
        "standalone": true,
        "description": "Experimental metrics catalog.",
        "adapter_refs": [],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M01",
          "PA-M02",
          "PA-M03",
          "PA-M04",
          "PA-M05",
          "PA-M06",
          "PA-M07",
          "PA-M08",
          "PA-M09",
          "PA-M10",
          "PA-M11",
          "PA-M12",
          "PA-M13",
          "PA-M14",
          "PA-M15",
          "PA-M16",
          "PA-M17",
          "PA-M18",
          "PA-M19",
          "PA-M20",
          "PA-M21",
          "PA-M22",
          "PA-M23",
          "PA-M24",
          "PA-M25",
          "PA-M26",
          "PA-M27",
          "PA-M28",
          "PA-M29",
          "PA-M30",
          "PA-M31",
          "PA-M32",
          "PA-M33",
          "PA-M34",
          "PA-M35",
          "PA-M36",
          "PA-M37",
          "PA-M38",
          "PA-M39",
          "PA-M40",
          "PA-M41",
          "PA-M42",
          "PA-M43",
          "PA-M44",
          "PA-M45",
          "PA-M46",
          "PA-M47",
          "PA-M48",
          "PA-M49",
          "PA-M50",
          "PA-M51",
          "PA-M52"
        ],
        "validation_refs": []
      },
      "ethics-and-limits": {
        "id": "ethics-and-limits",
        "file": "ethics_and_limits.md",
        "role": "ethics",
        "status": "experimental",
        "anchor": "#ETHICS_AND_LIMITS",
        "standalone": true,
        "description": "Ethical boundaries, prohibited uses, privacy, contestability, and known limitations.",
        "adapter_refs": [],
        "dimension_refs": [],
        "metric_refs": [
          "PA-M32",
          "PA-M37",
          "PA-M38",
          "PA-M39",
          "PA-M40",
          "PA-M41",
          "PA-M42",
          "PA-M43",
          "PA-M44",
          "PA-M48",
          "PA-M51"
        ],
        "validation_refs": [
          "VCR-13",
          "VCR-15",
          "VCR-16",
          "VCR-17",
          "VCR-18"
        ]
      },
      "example-resonant-iq-fingerprint": {
        "id": "example-resonant-iq-fingerprint",
        "file": "example_resonant_iq_fingerprint.md",
        "role": "example",
        "status": "experimental",
        "anchor": "#EXAMPLE_RESONANT_IQ_FINGERPRINT",
        "standalone": true,
        "description": "Synthetic PAX-01 worked example.",
        "adapter_refs": [
          "fft",
          "inverted-star",
          "structural-detection",
          "rtt",
          "resonance"
        ],
        "dimension_refs": [
          "pattern-recognition",
          "structural-reasoning",
          "causal-integration",
          "temporal-reasoning",
          "cross-domain-transfer",
          "regime-recognition",
          "anomaly-detection",
          "ambiguity-navigation",
          "adaptive-reframing",
          "coherence-maintenance",
          "drift-awareness",
          "metacognitive-calibration",
          "long-horizon-integration",
          "tool-collaboration",
          "recovery-recalibration"
        ],
        "metric_refs": [
          "PA-M01",
          "PA-M02",
          "PA-M04",
          "PA-M05",
          "PA-M06",
          "PA-M07",
          "PA-M12",
          "PA-M20",
          "PA-M28",
          "PA-M32",
          "PA-M36",
          "PA-M45",
          "PA-M46"
        ],
        "validation_refs": [
          "VCR-01",
          "VCR-02",
          "VCR-05",
          "VCR-10",
          "VCR-12",
          "VCR-13",
          "VCR-16"
        ]
      },
      "module-json": {
        "id": "module-json",
        "file": "predictive_analytics_module.json",
        "role": "module",
        "status": "experimental",
        "anchor": "#MODULE_JSON",
        "standalone": true,
        "description": "Canonical machine-readable Predictive Analytics module manifest.",
        "adapter_refs": [],
        "dimension_refs": [],
        "metric_refs": [],
        "validation_refs": []
      },
      "module-schema": {
        "id": "module-schema",
        "file": "predictive_analytics_module.schema.json",
        "role": "module",
        "status": "experimental",
        "anchor": "#MODULE_SCHEMA",
        "standalone": true,
        "description": "JSON Schema for the Predictive Analytics module manifest.",
        "adapter_refs": [],
        "dimension_refs": [],
        "metric_refs": [],
        "validation_refs": []
      }
    },
    "navigation": {
      "index_path": "index.html",
      "readme_path": "README.md",
      "module_path": "predictive_analytics_module.json",
      "schema_path": "predictive_analytics_module.schema.json",
      "default_document": "README.md",
      "anchor_style": "uppercase-doc-map",
      "sections": {
        "foundations": "#FOUNDATIONS",
        "observers": "#OBSERVERS",
        "profiles": "#PROFILES",
        "adapters": "#ADAPTERS",
        "validation": "#VALIDATION",
        "ethics": "#ETHICS",
        "examples": "#EXAMPLES",
        "module": "#MODULE"
      },
      "doc_anchors": {
        "readme": "#README",
        "foundations": "#FOUNDATIONS",
        "predictive-model-adapter": "#PREDICTIVE_MODEL_ADAPTER",
        "substrate-adapter": "#SUBSTRATE_ADAPTER",
        "regime-observer": "#REGIME_OBSERVER",
        "resonance-observer": "#RESONANCE_OBSERVER",
        "drift-observer": "#DRIFT_OBSERVER",
        "coherence-observer": "#COHERENCE_OBSERVER",
        "uncertainty-layer": "#UNCERTAINTY_LAYER",
        "counterfactual-layer": "#COUNTERFACTUAL_LAYER",
        "human-review-hook": "#HUMAN_REVIEW_HOOK",
        "resonant-iq-fingerprint": "#RESONANT_IQ_FINGERPRINT",
        "intelligence-dimensions": "#INTELLIGENCE_DIMENSIONS",
        "substrate-expression-profile": "#SUBSTRATE_EXPRESSION_PROFILE",
        "model-mismatch": "#MODEL_MISMATCH",
        "adapters": "#ADAPTERS",
        "fft-adapter": "#FFT_ADAPTER",
        "inverted-star-adapter": "#INVERTED_STAR_ADAPTER",
        "structural-detection-adapter": "#STRUCTURAL_DETECTION_ADAPTER",
        "rtt-adapter": "#RTT_ADAPTER",
        "resonance-adapter": "#RESONANCE_ADAPTER",
        "validation": "#VALIDATION",
        "metrics": "#METRICS",
        "ethics-and-limits": "#ETHICS_AND_LIMITS",
        "example-resonant-iq-fingerprint": "#EXAMPLE_RESONANT_IQ_FINGERPRINT",
        "module-json": "#MODULE_JSON",
        "module-schema": "#MODULE_SCHEMA"
      }
    }
  }
}
```

A couple of deliberate choices here:

0.1.0 + experimental + unvalidated keeps canon status distinct from scientific validation.
I instantiated all 52 PA-M## metrics and 18 VCR-## criteria, so references aren't pointing into thin air.
The adapter layer explicitly allows FFT, Inverted Star, Structural Detection, RTT, or Resonance to fail ablation testing and eventually be deprecated.
decision_authority starts at none.
The PAX-01 example remains explicitly synthetic.
documents now doubles as the module's machine-readable file/anchor registry, giving us a clean source for the eventual index.html DOC_MAP.
The biggest remaining intentional gap is the full 24-dimension RIQF catalog. I instantiated the dimensions most central to the first example rather than pretending tonight's initial vocabulary is already the final intelligence ontology.

That feels like a pretty solid stopping point for the module tonight. 🔺
