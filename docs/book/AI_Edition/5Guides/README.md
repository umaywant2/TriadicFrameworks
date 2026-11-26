<img width="1194" height="672" alt="book_AI_Edition_5Guides_README_" src="https://github.com/user-attachments/assets/265d84aa-da81-44d5-bd58-a41ad0f30f42" />

# 5Guides — AI Edition

> Machine-oriented structural learning materials for Awareness, Alignment, Coherence, Clarity, and Continuity.

This directory contains the AI-facing edition of the 5Guides learning module.

The human-facing source material lives at:

```text
/docs/5Guides/
```

The AI Edition lives at:

```text
/docs/book/AI_Edition/5Guides/
```

The two editions serve different purposes.

The human edition is designed to be read, explored, practiced, and experienced by learners.

The AI Edition is designed to expose the same educational structure in explicit machine-readable JSON.

---

# Core Framework

5Guides is organized around AACCC:

```text
Awareness
    ↓
Alignment
    ↓
Coherence
    ↓
Clarity
    ↓
Continuity
    ↓
Independent Application
```

The five questions are:

```text
Awareness
What am I observing?

Alignment
What corresponds?

Coherence
Does this hold together?

Clarity
Can this be understood and inspected?

Continuity
What persists through change?
```

These questions form a developmental sequence.

They are not isolated stages.

A later question may reveal a problem that requires returning to an earlier one.

For example:

```text
Coherence problem
      ↓
inspect Alignment
      ↓
discover observation boundary problem
      ↓
return to Awareness
```

AACCC should therefore be treated as both:

```text
a learning progression
```

and:

```text
a reusable inspection loop
```

---

# Purpose of the AI Edition

The AI Edition is not intended to be a Markdown-to-JSON transcription.

Its purpose is structural transformation.

The human edition may express a Guide across:

```text
index.md
explore.md
practice.md
mastery.md
```

The AI Edition combines those materials into one structured Guide object:

```text
guides/awareness.json
guides/alignment.json
guides/coherence.json
guides/clarity.json
guides/continuity.json
```

The transformation is:

```text
Human Learning Experience
        ↓
Structural Extraction
        ↓
Machine-Readable Learning Object
```

The educational meaning should persist.

The presentation format may change.

---

# Human Edition vs. AI Edition

## Human Edition

The human-facing materials emphasize:

- pacing;
- examples;
- games;
- student questions;
- reflection;
- narrative transitions;
- approachable explanations;
- optional formal exploration.

Typical structure:

```text
Guide
├── index.md
├── explore.md
├── practice.md
└── mastery.md
```

## AI Edition

The AI-facing materials emphasize:

- explicit structure;
- semantic roles;
- learning objectives;
- distinctions;
- boundaries;
- mastery criteria;
- student artifacts;
- provenance;
- formal companions;
- machine navigation.

Typical structure:

```text
Guide Object
├── identity
├── core_question
├── purpose
├── learning_objectives
├── key_distinctions
├── explore
├── practice
├── mastery
├── student_record
├── assessment
├── badge
├── ai_companion
├── formal_companion
├── boundaries
├── provenance
└── next_guide
```

---

# Directory Structure

```text
docs/book/AI_Edition/5Guides/
│
├── README.md
├── module.json
├── index.json
│
├── guides/
│   ├── awareness.json
│   ├── alignment.json
│   ├── coherence.json
│   ├── clarity.json
│   └── continuity.json
│
├── shared/
│   ├── ai_companion.json
│   ├── assessment.json
│   ├── badges.json
│   ├── privacy.json
│   └── student_footprint.json
│
├── origins/
│   ├── index.json
│   ├── tft.json
│   ├── theorems.json
│   ├── rtt.json
│   └── formalization.json
│
└── lean/
    ├── index.json
    ├── 01_awareness.json
    ├── 02_alignment.json
    ├── 03_coherence.json
    ├── 04_clarity.json
    ├── 05_continuity.json
    ├── 06_tft_origin.json
    ├── 07_nawderian_theorem.json
    ├── 08_nawderian_set_theorem.json
    ├── 09_temperature_engine_theorem.json
    ├── 10_unified_resonance_theorem.json
    └── 11_rtt_origin.json
```

The README documents the edition.

The machine-facing learning corpus itself is JSON.

---

# Root Files

## `module.json`

`module.json` defines the module contract.

It describes:

- module identity;
- AACCC sequence;
- learning rhythm;
- Guide-object expectations;
- assessment contract;
- badge contract;
- AI Companion contract;
- privacy contract;
- formalization contract;
- Lean validation boundary;
- Origins boundary;
- provenance rules;
- file registry.

Think of it as:

```text
What rules govern this module?
```

---

# `index.json`

`index.json` is the AI-facing front door.

It describes:

- where to begin;
- how to traverse AACCC;
- how Guide skills accumulate;
- when to return to an earlier Guide;
- where Shared resources live;
- where Lean companions live;
- where Origins materials live;
- how to reach Independent Application.

Think of it as:

```text
How should an AI navigate this module?
```

---

# The Five Guide Objects

The primary learning objects are:

```text
guides/awareness.json
guides/alignment.json
guides/coherence.json
guides/clarity.json
guides/continuity.json
```

Each combines the corresponding human-facing:

```text
index.md
explore.md
practice.md
mastery.md
```

into one machine-oriented structure.

---

# Awareness

Path:

```text
guides/awareness.json
```

Core question:

> What am I observing?

Primary distinctions include:

```text
Observation

Interpretation

Assumption

Unknown

Observer Position

Boundary

Blind Spot
```

Student artifact:

```text
Awareness Record
```

Formal companion:

```text
lean/01_awareness.json
```

---

# Alignment

Path:

```text
guides/alignment.json
```

Core question:

> What corresponds?

Primary distinctions include:

```text
Correspondence

Identity

Similarity

Mapping

Mismatch

Partial Alignment

Conditional Alignment

Unmapped Element

Provenance
```

Student artifact:

```text
Alignment Record
```

Formal companion:

```text
lean/02_alignment.json
```

---

# Coherence

Path:

```text
guides/coherence.json
```

Core question:

> Does this hold together?

Primary distinctions include:

```text
Supported Relationship

Contradiction

Constraint

Missing Relationship

Unsupported Conclusion

Hidden Assumption

Local Coherence

Global Coherence
```

Student artifact:

```text
Coherence Record
```

Formal companion:

```text
lean/03_coherence.json
```

---

# Clarity

Path:

```text
guides/clarity.json
```

Core question:

> Can this be understood and inspected?

Primary distinctions include:

```text
Meaning

Definition

Ambiguity

Missing Step

Representation

Qualification

Uncertainty

Meaning Drift
```

Student artifact:

```text
Clarity Record
```

Formal companion:

```text
lean/04_clarity.json
```

---

# Continuity

Path:

```text
guides/continuity.json
```

Core question:

> What persists through change?

Primary distinctions include:

```text
State

Transition

Persistence

Drift

Recurrence

Pattern Break

History

Provenance

Invariant
```

Student artifact:

```text
Continuity Record
```

Formal companion:

```text
lean/05_continuity.json
```

---

# Learning Rhythm

The shared educational rhythm is:

```text
Experience
    ↓
Notice
    ↓
Inspect
    ↓
Apply
    ↓
Demonstrate
    ↓
Reflect
    ↓
Continue
```

Each Guide expresses this through three major phases:

```text
Explore
   ↓
Practice
   ↓
Mastery
```

The AI Edition should preserve the distinction among those phases.

---

# Explore

Explore introduces the structural idea through approachable examples.

The AI should treat Explore as:

```text
experience-building
```

rather than:

```text
final assessment
```

Useful behavior includes:

- asking questions;
- offering another example;
- changing perspective;
- changing scale;
- exposing a distinction;
- allowing uncertainty.

---

# Practice

Practice makes the structural skill deliberate.

The AI should help the learner:

- apply the Guide question;
- use the Guide's record structure;
- identify assumptions;
- distinguish evidence from interpretation;
- preserve mismatch;
- expose missing information;
- revise reasoning.

Practice may include AI assistance.

Practice is not equivalent to mastery.

---

# Mastery

Mastery uses a fresh problem.

The purpose is transfer.

The learner should demonstrate that the skill can be used without having every step supplied in advance.

A mastery interaction should therefore avoid:

```text
AI solves problem
      ↓
learner copies answer
      ↓
badge
```

Prefer:

```text
learner attempts
      ↓
structural feedback
      ↓
revisit if needed
      ↓
fresh attempt
      ↓
demonstrated skill
```

Retry is part of learning.

---

# Shared Resources

The Shared directory contains learning contracts that apply across all five Guides.

```text
shared/
├── ai_companion.json
├── assessment.json
├── badges.json
├── privacy.json
└── student_footprint.json
```

---

# AI Companion

Path:

```text
shared/ai_companion.json
```

The AI Companion is optional.

Its role is:

```text
thinking companion
```

not:

```text
final authority
```

Useful actions include:

- ask questions;
- generate practice;
- challenge assumptions;
- offer counter-mappings;
- expose missing steps;
- compare versions;
- preserve uncertainty;
- help explain formal structures.

The learner retains judgment.

---

# Assessment

Path:

```text
shared/assessment.json
```

Assessment distinguishes:

```text
Awareness Check
```

from:

```text
Mastery Checkpoint
```

The Awareness Check asks:

> What did the learner notice after first exposure?

The Mastery Checkpoint asks:

> Can the learner use the skill on a fresh problem?

Mastery is retryable.

The assessment model is criterion-based rather than competitive.

---

# Badges

Path:

```text
shared/badges.json
```

The five Guide milestones are:

```text
Awareness Badge

Alignment Badge

Coherence Badge

Clarity Badge

Continuity Badge
```

Completion of the sequence may produce:

```text
Five Guides Completion
```

These represent learning milestones.

They are not:

- professional certification;
- accreditation;
- ranking;
- authority;
- artificial scarcity.

---

# Privacy

Path:

```text
shared/privacy.json
```

The governing principle is:

> Learning does not grant us permission to observe the learner.

The following should remain separate:

```text
Learning

Mastery

Badge

Optional Feedback
```

Identity is not required merely to learn.

AI is not required.

Lean is not required.

A Student Footprint is not required.

---

# Student Footprint

Path:

```text
shared/student_footprint.json
```

The Student Footprint is an optional minimal feedback mechanism.

Possible voluntary fields are:

```text
Country

Short Reflection
```

The Footprint should not become:

- a learner profile;
- surveillance;
- a leaderboard;
- an engagement score;
- a requirement for completion.

Silence should remain silence.

---

# Lean 4 Lab

The AI Edition contains machine-oriented companions for the validated Lean examples.

```text
lean/
├── index.json
├── 01_awareness.json
├── 02_alignment.json
├── 03_coherence.json
├── 04_clarity.json
├── 05_continuity.json
├── 06_tft_origin.json
├── 07_nawderian_theorem.json
├── 08_nawderian_set_theorem.json
├── 09_temperature_engine_theorem.json
├── 10_unified_resonance_theorem.json
└── 11_rtt_origin.json
```

The human source Lean files live at:

```text
/docs/5Guides/lean/
```

---

# Lean Validation

The human-source Lean teaching set `01–11` was compiler-checked using:

```text
Lean 4.36.0

x86_64-w64-windows-gnu
```

The AI Edition should preserve that compiler provenance.

It should also preserve the validation boundary.

Compiler acceptance means:

> The formal artifact was accepted under the stated Lean environment.

It does not mean:

> The broader source framework was empirically validated.

---

# Lean JSON Objects

Each Lean JSON artifact should expose more than source code.

Recommended structure includes:

```text
identity

source_file

role

purpose

definitions

assumptions

theorems

verified_consequences

compiler_validation

formalization_boundary

student_questions

lean_source

provenance
```

This helps prevent an AI from confusing:

```text
formal consequence
```

with:

```text
source interpretation
```

or:

```text
empirical claim
```

---

# Origins

The Origins directory preserves project lineage.

```text
origins/
├── index.json
├── tft.json
├── theorems.json
├── rtt.json
└── formalization.json
```

The simplified lineage is:

```text
TFT
 ↓
Triads
 ↓
Theorems
 ↓
RTT
 ↓
AACCC
 ↓
5Guides
```

The arrows indicate project development.

They do not represent a strict proof chain.

---

# Origins Boundary

The Origins materials should not be interpreted as claiming:

```text
TFT proved the Theorems.

The Theorems proved RTT.

RTT proved AACCC.

AACCC proves 5Guides scientifically valid.
```

That is not the purpose of the lineage.

The useful question is:

> What persisted, changed, became more explicit, was abandoned, or became teachable?

---

# Formalization

Path:

```text
origins/formalization.json
```

The AI Edition should preserve three distinct questions.

## Formal Verification

```text
Given these definitions and assumptions,
does the conclusion follow?
```

## Modeling

```text
Do these definitions and assumptions represent
what we intended to describe?
```

## Empirical Validation

```text
Does the model adequately describe the relevant
real-world evidence?
```

These questions may support one another.

They are not interchangeable.

---

# Provenance Chain

For formalized origin material, preserve a chain such as:

```text
Source
  ↓
Interpretation
  ↓
Teaching Abstraction
  ↓
Formal Definition
  ↓
Added Assumptions
  ↓
Lean Theorem
  ↓
Verified Consequence
  ↓
Formalization Boundary
```

An AI should not collapse these layers.

---

# Core Reasoning Boundaries

The AI Edition should preserve the following distinctions.

```text
Observation
≠
Interpretation
```

```text
Interpretation
≠
Source Statement
```

```text
Similarity
≠
Identity
```

```text
Similarity
≠
Historical Influence
```

```text
Mismatch
≠
Automatic Error
```

```text
Recurrence
≠
Causation
```

```text
Formal Verification
≠
Empirical Validation
```

```text
Compiler Acceptance
≠
Physical Validation
```

```text
Clearer Wording
≠
Permission to Strengthen a Claim
```

```text
Continuity
≠
Preventing Change
```

```text
AI Assistance
≠
Learner Judgment
```

```text
Badge
≠
Professional Certification
```

These distinctions are part of the module architecture.

They are not optional editorial notes.

---

# Preserve Uncertainty

Uncertainty is a valid representational state.

The AI Edition should preserve states such as:

```text
unknown

uncertain

partial

conditional

unmapped

not established

insufficient information
```

Do not automatically convert them into conclusions.

For example:

```text
Relationship:
unknown
```

should not become:

```text
Relationship:
probably X
```

without evidence.

---

# Preserve Mismatch

A mismatch can be useful information.

If:

```text
Expected:
A

Observed:
B
```

the default response should not be:

```text
change B to A
```

or:

```text
reinterpret A until B fits
```

Preserve:

```text
Expected:
A

Observed:
B

Relationship:
mismatch
```

Then investigate.

---

# Preserve Missing Relationships

If the available material supports:

```text
A
 ↓
?
 ↓
C
```

do not invent B merely because the sequence looks incomplete.

The missing relationship is itself information.

This principle applies to:

- educational examples;
- provenance;
- theorem interpretation;
- source mapping;
- causal explanation;
- formalization.

---

# AI Navigation

The normal student-facing traversal is:

```text
guides/awareness.json
        ↓
guides/alignment.json
        ↓
guides/coherence.json
        ↓
guides/clarity.json
        ↓
guides/continuity.json
        ↓
Independent Application
```

But the AI should permit return paths.

For example:

```text
Coherence
   ↓
Alignment problem detected
   ↓
Alignment
```

or:

```text
Continuity
   ↓
Meaning drift detected
   ↓
Clarity
```

or:

```text
Alignment
   ↓
Observation boundary unclear
   ↓
Awareness
```

The sequence teaches accumulation.

It does not prohibit recursion.

---

# Optional Branches

At any suitable point, the learner may branch into:

```text
Shared Resources
```

```text
Lean 4 Lab
```

```text
Origins
```

These branches should remain optional.

Do not require knowledge of project lineage before allowing student-facing learning.

Do not require formal proof experience before awarding normal Guide mastery.

---

# Independent Application

The destination of 5Guides is not more 5Guides.

It is:

```text
Independent Application
```

The learner selects a problem not chosen by the module.

Possible domains include:

- learning;
- technical problems;
- repair;
- research claims;
- disagreements;
- models;
- documents;
- software;
- changing systems;
- everyday situations.

Then the learner asks:

```text
What am I observing?

What corresponds?

Does this hold together?

Can I make it clear enough to inspect?

What persists when it changes?
```

---

# Independent AACCC Record

A reusable final structure is:

```text
Problem:
...

Awareness:
...

Alignment:
...

Coherence:
...

Clarity:
...

Continuity:
...

Assumptions:
...

Uncertainty:
...

Evidence:
...

What I Would Test Next:
...

Current Judgment:
...
```

There is no supplied universal answer key.

That is intentional.

The module is designed to produce transfer rather than dependency.

---

# Machine-Use Guidance

An AI consuming this edition should prefer:

```text
inspect
```

before:

```text
conclude
```

Prefer:

```text
ask
```

before:

```text
assume
```

Prefer:

```text
preserve mismatch
```

before:

```text
force mapping
```

Prefer:

```text
show uncertainty
```

before:

```text
manufacture certainty
```

Prefer:

```text
expose assumptions
```

before:

```text
hide them
```

Prefer:

```text
trace provenance
```

before:

```text
infer lineage
```

Prefer:

```text
learner demonstration
```

before:

```text
AI substitution
```

---

# Start Here

For machine navigation:

```text
index.json
```

For the module contract:

```text
module.json
```

For the first Guide:

```text
guides/awareness.json
```

For optional formal companions:

```text
lean/index.json
```

For project lineage:

```text
origins/index.json
```

For shared learning contracts:

```text
shared/
```

---

# Final AI Edition Principle

The human 5Guides edition teaches through experience.

The AI Edition should preserve the structure underneath that experience.

Its purpose is not merely to tell an AI:

```text
what the Guides say
```

but to make explicit:

```text
what each Guide is for

how the Guides relate

what distinctions must survive

what evidence supports a relationship

where uncertainty belongs

where formalization begins and ends

how provenance is preserved

when learner judgment must remain primary

and where the learner should eventually go next
```

That final destination is not dependence on the framework.

It is:

```text
Observe carefully.

Map honestly.

Test the structure.

Make it inspectable.

Follow what changes.

Then carry the questions somewhere new.
```

---

> The AI Edition exposes the structure. The learner still does the learning.
