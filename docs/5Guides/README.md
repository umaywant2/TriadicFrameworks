<img width="1194" height="672" alt="5Guides_" src="https://github.com/user-attachments/assets/c6cb8a28-46a6-4fd1-b224-9cd1e63d64dc" />

- [`5G_module.json`](5G_module.json) — Agentic module schema role assignments

# 5Guides

> **Awareness → Alignment → Coherenc**→ Clarity → Continu**y**

**5Guides** is a student-facing learning path for practicing five structural questions:

1. **Awareness:** What am I observing?
2. **Alignment:** What corresponds?
3. **Coherence:** Does this hold together?
4. **Clarity:** Can it be understood and inspected?
5. **Continuity:** What persists through change?

The goal is not to memorize five definitions.

The goal is to **practice five habits**f inspection**, use them on increasingly unfamiliar problems, and eventually take them somewhere we did not choose for you.

---

## Start Here

You do **not** need:

- prior knowledge of TriadicFrameworks;
- mathematics beyond the exercises you choose;
- programming experience;
- Lean 4;
- an AI assistant;
- or an account simply to understand and practice the Guides.

Start with ordinary observation.

Move at your own pace.

Ask questions.

Change your mind when the evidence gives you a reason.

And remember:

> **"I don't know yet" is a usef** answer when**ou genuinely don't know yet.**

---

# The Five Guides

| Guide | Question | Practice |
|---|---|---|
| **Awareness** | What am I observing? | Separate observation, interpretation, assumption, uncertainty, and boundary |
| **Alignment** | What corresponds? | Find, test, qualify, or reject mappings |
| **Coherence** | Does this hold together? | Inspect relationships, gaps, contradictions, and assumptions |
| **Clarity** | Can it be understood and inspected? | Make important structure visible without silently changing its meaning |
| **Continuity** | What persists through change? | Follow state, structure, drift, breaks, and persistence over time |

The intended progression is:

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

Each Guide builds on skills practiced earlier, but the questions remain useful on their own.

---

# How Each Guide Works

Each Guide follows the same general learning rhythm:

> **Experience → Notice → Inspect → Apply → Demonstrate → Reflect → Continue**

That rhythm is divided into four sections.

## Explore

Meet the idea through approachable examples, games, observations, and small challenges.

No need to begin with formal vocabulary.

First, experience the problem.

## Practice

Use the idea deliberately.

Examples may move through three levels:

### Everyday

Familiar situations such as:

- objects;
- conversations;
- maps;
- puzzles;
- study habits;
- directions;
- and ordinary decisions.

### Systems

Apply the same question to:

- software;
- signals;
- states;
- mappings;
- failures;
- drift;
- transitions;
- and recurring patterns.

### Formal

For interested students, optional **Lean 4** examples show how selected ideas can be made precise enough for a proof checker to inspect.

Lean is an optional branch, not a requirement for completing the Guides.

## Mastery

Try the skill on a fresh problem without being walked through every step.

If something doesn't work, that isn't the end of the exercise.

It tells you what may deserve another look.

> **Retry is part of learning.**

## Reflect

Pause long enough to ask:

> **What changed about how I approached the problem?**

Then continue when you're ready.

---

# Guide 1 — Awareness

> ## **What am I observing?**

Awareness begins before explanation.

You'll practice noticing the difference between:

- what you observe;
- what you infer;
- what you assume;
- what remains uncertain;
- what information may be missing;
- and where you're observing from.

You'll also experiment with:

- observation games;
- grounding and imagination;
- observer perspective;
- blind spots;
- multiple viewpoints;
- and how systems can represent observations.

The first goal is simple:

> **Notice before you decide.**

**Start:** `awareness/index.md`

---

# Guide 2 — Alignment

> ## **What corresponds?**

Once you can inspect observations, you can begin comparing them.

You'll practice finding:

- meaningful correspondences;
- partial matches;
- conditional matches;
- mismatches;
- missing relationships;
- and unsupported mappings.

You'll also explore a surprisingly important skill:

> **Knowing when not to make things align.**

A mismatch can carry valuable information.

**Continue:** `alignment/index.md`

---

# Guide 3 — Coherence

> ## **Does this hold together?**

Individual pieces can look perfectly reasonable while the complete structure does not.

You'll practice spotting:

- contradictions;
- missing connections;
- incompatible assumptions;
- unsupported conclusions;
- and situations where locally reasonable pieces work against each other.

The goal is not to immediately repair every problem.

First:

> **Find where the structure stops holding together.**

**Continue:** `coherence/index.md`

---

# Guide 4 — Clarity

> ## **Can this be understood well enough to inspect?**

Something can be coherent and still be difficult for another person to examine.

You'll practice exposing:

- definitions;
- relationships;
- assumptions;
- missing steps;
- ambiguity;
- uncertainty;
- and important structure.

But there's a catch:

> **Making something easier to understand should not silently change what it means.**

Clarity is not merely simplification.

It is making structure visible enough to inspect.

**Continue:** `clarity/index.md`

---

# Guide 5 — Continuity

> ## **What persists through change?**

Systems move.

Understanding changes.

Evidence accumulates.

States transition.

Patterns repeat, drift, and sometimes break.

You'll practice asking:

- What changed?
- What persisted?
- What returned?
- What drifted?
- What broke?
- Can I trace how the system got here?

Continuity brings the earlier Guides together.

**Continue:** `continuity/index.md`

---

# Your Five Student Records

Each Guide produces a small reusable artifact:

```text
Awareness Record
      ↓
Alignment Record
      ↓
Coherence Record
      ↓
Clarity Record
      ↓
Continuity Record
```

These are not paperwork for the sake of paperwork.

They are thinking tools.

By the end of the Five Guides, you should have more than five completed lessons.

You should have a small toolkit you can use elsewhere.

---

# Awareness Check vs. Mastery

The Guides distinguish between two kinds of learning checks.

## Awareness Check

An optional first-pass question:

> **What stuck after my first encounter?**

This isn't about punishment or ranking.

It helps reveal what you already noticed and what may deserve another look.

## Mastery Checkpoint

A practical question:

> **Can I use this on a fresh problem?**

Mastery is retryable.

An incomplete attempt is information:

> **Here's something worth inspecting again.**

---

# AI Assistance

AI is optional throughout 5Guides.

If you use an AI assistant, treat it as a **thinking partner**, not an answer key.

Try prompts such as:

> **Challenge my assumption.**

> **What might I be missing?**

> **Give me another possible interpretation.**

> **Find the strongest mismatch in my mapping.**

> **What would make this explanation fail?**

> **Help me make this clearer without changing its meaning.**

And remember:

> **AI output is also something you can inspect.**

You remain responsible for deciding what the available evidence supports.

---

# Optional Lean 4 Path

For learners interested in formal reasoning, 5Guides includes a small Lean 4 strand.

The first five examples correspond to the Guides:

```text
01_awareness.lean
02_alignment.lean
03_coherence.lean
04_clarity.lean
05_continuity.lean
```

Additional examples examine selected structures from the project's lineage:

```text
06_tft_origin.lean
07_nawderian_theorem.lean
08_nawderian_set_theorem.lean
09_temperature_engine_theorem.lean
10_unified_resonance_theorem.lean
11_rtt_origin.lean
```

The complete `01–11` set was compiler-checked using:

```text
Lean 4.36.0
x86_64-w64-windows-gnu
```

Compiler acceptance means Lean accepted the formal definitions and proofs under that environment.

It does **not** automatically establish that a broader model accurately describes nature.

Keep these questions separate:

> **Did Lean verify the formal proof?**

and:

> **Did we formalize the claim we intended to make?**

That distinction is part of the lesson.

---

# Where Did 5Guides Come From?

The Five Guides emerged from a longer line of work within TriadicFrameworks.

A compact project-lineage view is:

```text
TFT
 ↓
Triads
 ↓
Theorems
 ↓
RTT
 ↓
AACCC / 5Guides
```

This is a **project-lineage interpretation**.

It does not mean the earlier materials originally defined the Five Guides exactly as they appear here.

Instead, 5Guides draws recurring structural habits from that work and turns them into a student-facing learning sequence.

The Origins section is optional.

You do not need to understand that history before using the Guides.

**Explore later:** `origins/index.md`

---

# Privacy

The Guides begin with a simple principle:

> **Learning does not grant us permission to observe the learner.**

Participation should not require surveillance.

Learning, mastery, badges, and voluntary feedback should remain separate.

You should be able to learn without leaving an unnecessary identifying footprint.

---

# Optional Student Footprint

After completing a Guide, you may eventually be invited to leave something small behind.

For example:

**Where are you learning from?**

`[ Optional country ]`

**One thought about your experience**

`[ Optional short reflection ]`

No name is required.

No email is required.

No public profile is required simply to leave feedback.

Choosing not to leave a footprint does not change what you accomplished.

---

# Badges

Each completed Guide can award a learning milestone:

- **Awareness Badge**
- **Alignment Badge**
- **Coherence Badge**
- **Clarity Badge**
- **Continuity Badge**

These are not professional certifications or accreditation.

They mean:

> **You completed the learning journey and demonstrated the skill defined by that Guide.**

Completing all five opens the final step:

> **Independent Application**

---

# Where This Is Going

The destination isn't:

> **Now memorize TriadicFrameworks.**

It isn't:

> **Now agree with us.**

And it isn't:

> **Now ask AI what to think.**

The destination is much simpler.

Choose something we didn't choose for you:

- something you're learning;
- a technical problem;
- a disagreement;
- a research claim;
- a model;
- a piece of software;
- a system;
- or something from everyday life.

Then ask:

> **What am I observing?**

> **What corresponds?**

> **Does this hold together?**

> **Can I make it clear enough to inspect?**

> **What persists when it changes?**

If you can carry those questions into your own problems, the Guides have done their job.

---

# Begin

Start with:

# **Awareness**

> **What am I actually observing?**

Proceed to:

`awareness/index.md`

---

## Module Structure

```text
5Guides/
├── README.md
├── 5g_capture.md
│
├── awareness/
├── alignment/
├── coherence/
├── clarity/
├── continuity/
│
├── origins/
├── lean/
└── shared/
```

`5g_capture.md` remains the development workshop where the Five Guides were shaped.

The student-facing files become the place where the Guides are experienced.

> **Experience → Notice → Inspect → Apply → Demonstrate → Reflect → Continue**
