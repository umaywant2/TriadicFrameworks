# Grading Rubric: RTT Two‑Node vs N‑Node Lab 📊  
*(Insight Over Correctness)*

**Total: 100 points**

This rubric emphasizes **observational quality, reasoning, and reflection**.  
Students are **not** graded on system correctness, performance, or stability.

---

## 1️⃣ Assumption & Coherence Corridor (20 points)

**What we’re looking for:**  
A clear, honest statement of what the system *believes* to be true.

| Level | Description |
|------|-------------|
| **Excellent (18–20)** | Assumption is precise, realistic, and clearly time‑dependent. Corridor is well‑defined and measurable. |
| **Good (14–17)** | Assumption is clear but corridor is loosely defined or partially implicit. |
| **Adequate (10–13)** | Assumption is vague or corridor is underspecified. |
| **Needs Work (0–9)** | Assumption is unclear, trivial, or not related to distributed behavior. |

---

## 2️⃣ Instrumentation Quality (20 points)

**What we’re looking for:**  
Observation without interference.

| Level | Description |
|------|-------------|
| **Excellent (18–20)** | Instrumentation is minimal, well‑placed, and does not alter system behavior. |
| **Good (14–17)** | Instrumentation is correct but slightly intrusive or overly broad. |
| **Adequate (10–13)** | Observation works but mixes in unnecessary logic. |
| **Needs Work (0–9)** | Instrumentation changes system behavior or enforces outcomes. |

---

## 3️⃣ Badge Design & Signal Clarity (20 points)

**What we’re looking for:**  
Badges that make drift legible.

| Level | Description |
|------|-------------|
| **Excellent (18–20)** | Badges clearly communicate what happened, where, when, and why it matters. |
| **Good (14–17)** | Badges are useful but missing some contextual detail. |
| **Adequate (10–13)** | Badges exist but are hard to interpret. |
| **Needs Work (0–9)** | Badges are unclear, inconsistent, or absent. |

---

## 4️⃣ Two‑Node vs N‑Node Comparison (20 points)

**What we’re looking for:**  
Recognition of **non‑linear coherence effects**.

| Level | Description |
|------|-------------|
| **Excellent (18–20)** | Clear, thoughtful comparison showing how scale changes drift behavior. |
| **Good (14–17)** | Differences are identified but not deeply analyzed. |
| **Adequate (10–13)** | Comparison is mostly descriptive with limited insight. |
| **Needs Work (0–9)** | Little or no meaningful comparison. |

---

## 5️⃣ Reflection & Insight (20 points)

**What we’re looking for:**  
Understanding, not solutions.

| Level | Description |
|------|-------------|
| **Excellent (18–20)** | Reflection shows deep insight into time, drift, and assumptions. Avoids “fixing” mindset. |
| **Good (14–17)** | Reflection is thoughtful but leans toward solution‑thinking. |
| **Adequate (10–13)** | Reflection summarizes results without deeper reasoning. |
| **Needs Work (0–9)** | Reflection focuses on correctness or performance. |

---

## Bonus: Restraint Award (+5 points)

Awarded if the student:
- explicitly notes the temptation to “fix” the system
- explains why they chose not to
- demonstrates RTT’s separation of observation and control

---

## What Will *Not* Affect Your Grade 🚫

- Whether the system “works”
- Whether drift is eliminated
- Whether consistency is achieved
- Whether performance improves

Failure is acceptable.  
**Unobserved failure is not.**

---

## Instructor Summary

A strong submission answers:
> *What changed as the system scaled — and how did time make it visible?*

A weak submission answers:
> *How could we fix this?*

This rubric rewards the former.
