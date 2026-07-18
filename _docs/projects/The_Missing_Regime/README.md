# The Missing Regime

**Project Type:** Student Lab — Regime-Layer Audit & Context Recovery  
**Canon Alignment:** RTT-12 · Regime Analyzer · FFT Analyzer Suite  
**Difficulty:** Introductory → Intermediate  
**Estimated Time:** 2–4 hours per exercise cycle  

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## Purpose

Every system operates inside a regime — a bounded set of rules, assumptions, and constraints that define what the system *can* do, what it *cannot* do, and what it *does not know it is missing*.

Most frameworks never name their regime. Most analyses never audit it. The result is **regime blindness**: decisions made inside a frame that no one has tested, boundaries no one has mapped, and contradictions no one has surfaced.

**The Missing Regime** is a hands-on student project that teaches you to find, name, and stress-test the regime layer of any system, framework, or domain — using the diagnostic tools of the RTT Regime Analyzer.

You will learn to ask the question most analyses skip:

> *"What regime is this system operating in — and what does that regime make invisible?"*

---

## RTT Framing

This project is grounded in **Resonance Triad Theory (RTT)**, a twelve-layer harmonic framework for analyzing systems across domains. Within RTT, the **regime layer** is the structural context that governs how a system stabilizes, adapts, or collapses.

### Regime Levels

| Level | Name | Behavioral State |
|-------|------|------------------|
| **R0** | Pre-Regime | No stable governing structure; behavior is emergent or chaotic |
| **R1** | Stabilized | Rules are fixed; boundaries are rigid; the system resists change |
| **R2** | Adaptive | The system adjusts its rules in response to drift or external pressure |
| **R3** | Generative | The system produces new regimes; it is self-authoring |

Your job in every exercise is to **classify where the target system sits on this scale** — and then to probe what that classification reveals and conceals.

### Core Diagnostic Dimensions

The Regime Analyzer measures six dimensions. Each becomes a step in your audit:

1. **Regime Identification** — What regime is active? Can you name it?
2. **Regime Boundaries** — Where does this regime end? What lies outside it?
3. **Regime Contradictions** — Does the regime contain internal conflicts it cannot resolve?
4. **Regime Drift** — Is the regime shifting? In what direction? At what rate?
5. **Operator–Regime Coupling** — Which operators (forces, functions, actors) are locked to this regime? Which are decoupled?
6. **Regime Blindness** — What can this regime structurally not see about itself?

---

## What You Will Learn

By completing this project, you will be able to:

- **Identify** the governing regime of a system, even when it is unnamed or implicit
- **Map** regime boundaries and distinguish internal structure from external context
- **Detect** contradictions that a regime cannot resolve from within its own frame
- **Track** drift vectors — the slow, often invisible movement of a regime toward transition or collapse
- **Assess** how tightly operators (actors, functions, rules) are coupled to the current regime
- **Surface** regime blindness — the structural gaps a regime creates by its own design
- **Generate** a regime signature: a compact, portable summary of a system's regime state
- **Recover** missing context that a regime-blind analysis would have overlooked

---

## Reproducible Workflow

Each exercise follows the same seven-step audit cycle. This pattern is designed to be **repeatable across any domain** — you can apply it to an economic policy, a software architecture, a classroom curriculum, a scientific model, or a personal decision framework.

### Step 0 — Select a Target

Choose a system, framework, policy, or domain to audit. It can be anything with structure:

- A grading policy at your school
- A software development methodology (e.g., Agile, Waterfall)
- A diet or fitness plan
- A business model
- A scientific theory
- A social media platform's content algorithm

Write a one-paragraph description of the target. Name what it does and who it serves.

> **Output:** `target_description.md`

---

### Step 1 — Identify the Regime

Ask: *What regime is this system operating in?*

- Can you name the regime? If not, describe its behavior.
- Classify it: **R0**, **R1**, **R2**, or **R3**.
- What evidence supports your classification?

> **Output:** `regime_identification.md`

---

### Step 2 — Map the Boundaries

Ask: *Where does this regime end?*

- What is inside the regime? What is explicitly outside?
- Are boundaries sharp or fuzzy?
- Are there contested zones — areas that different stakeholders would draw differently?

> **Output:** `regime_boundaries.md`

---

### Step 3 — Detect Contradictions

Ask: *Does this regime contain conflicts it cannot resolve from within?*

- List any internal contradictions you observe.
- For each contradiction, explain why the regime cannot resolve it using only its own rules.
- Are any contradictions load-bearing (i.e., the regime depends on them)?

> **Output:** `regime_contradictions.md`

---

### Step 4 — Map Drift Vectors

Ask: *Is this regime changing? In what direction?*

- Identify any drift: slow shifts in rules, norms, metrics, or behavior.
- Is drift moving toward a higher regime level (R0→R1, R1→R2) or toward collapse?
- What is driving the drift? Internal pressure, external shock, or neglect?

> **Output:** `regime_drift.md`

---

### Step 5 — Assess Operator–Regime Coupling

Ask: *Which operators are locked to this regime?*

- List the key operators (actors, functions, rules, metrics) in the system.
- For each, classify coupling: **tight** (cannot function outside this regime), **loose** (adaptable), or **decoupled** (regime-independent).
- What happens to tightly coupled operators if the regime shifts?

> **Output:** `operator_coupling.md`

---

### Step 6 — Run Blindness Checks

Ask: *What can this regime not see about itself?*

This is the heart of the project. Use the Regime Blindness Checklist:

- [ ] **Regime mismatch** — Is the system using rules from a different regime than the one it occupies?
- [ ] **Outdated observer frame** — Are stakeholders evaluating the system using metrics from a prior era?
- [ ] **Legacy metrics** — Are success measures inherited rather than chosen?
- [ ] **Structural contradictions** — Are there contradictions the regime treats as features rather than bugs?
- [ ] **Missing feedback loops** — Are there signals the regime structurally cannot receive?
- [ ] **Invisible alternatives** — Does the regime make competing approaches impossible to evaluate fairly?

For every box you check, write one paragraph explaining *what is missing and why the regime cannot see it*.

> **Output:** `blindness_checks.md`

---

### Step 7 — Generate the Regime Signature

Compile your findings into a compact regime signature — a portable summary another analyst could use to understand the system's regime state at a glance.

**Signature Template:**

```
Target:        [name of system]
Regime Level:  [R0 / R1 / R2 / R3]
Boundaries:    [sharp / fuzzy / contested]
Contradictions:[count] — [load-bearing? yes/no]
Drift Vector:  [direction] at [rate: slow / moderate / rapid]
Coupling:      [dominant pattern: tight / loose / mixed]
Blindness:     [count of checks flagged] — [most critical gap]
Recovery Note: [one sentence: what context was missing before this audit?]
```

> **Output:** `regime_signature.md`

---

## Context Recovery

After completing the seven-step audit, write a short reflection (200–500 words):

1. **What did you know about this system before the audit?**
2. **What did the audit reveal that you could not have seen without regime-layer analysis?**
3. **If you had to advise someone making a decision about this system, what one thing would you tell them that a regime-blind analysis would have missed?**

This reflection is the *context recovery* — the act of naming what was structurally invisible and making it available for future decisions.

> **Output:** `context_recovery.md`

---

## Folder Structure

Your completed project should contain:

```
The_Missing_Regime/
├── README.md                  ← this file
├── target_description.md      ← Step 0
├── regime_identification.md   ← Step 1
├── regime_boundaries.md       ← Step 2
├── regime_contradictions.md   ← Step 3
├── regime_drift.md            ← Step 4
├── operator_coupling.md       ← Step 5
├── blindness_checks.md        ← Step 6
├── regime_signature.md        ← Step 7
└── context_recovery.md        ← Reflection
```

---

## Repeat & Compare

This workflow is designed for reuse. Run it on multiple targets and compare:

- Which regime level is most common in your chosen domain?
- Do certain domains cluster at R1 (rigid) while others reach R2 (adaptive)?
- Are there patterns in what regimes make blind — do similar blind spots recur?
- Can you find a system at R3 (generative)? What makes it different?

The more targets you audit, the sharper your regime-layer intuition becomes.

---

## Prerequisites

- No prior RTT knowledge required — this project teaches the concepts as you use them.
- Familiarity with writing structured observations in Markdown is helpful but not required.
- A willingness to question assumptions is essential.

---

## Credits & Lineage

**The Missing Regime** is a student project within the **TriadicFrameworks** canon.  
It draws directly on the **Regime Analyzer** module of the **FFT Analyzer Suite** and the **Regime Blindness Checklist**.

Framework: **Resonance Triad Theory (RTT)** — Nawder Loswin, 2025  
Canon: [TriadicFrameworks](https://triadicframeworks.com)

---

*Find the regime. Name it. Map what it hides. Recover the context.*
