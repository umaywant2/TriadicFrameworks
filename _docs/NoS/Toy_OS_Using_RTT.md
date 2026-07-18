## Assignment: Instrument a Toy OS Using RTT 🧪  
*(Observation Without Control)*

### Objective

In this assignment, you will **instrument a simple operating system** to observe coherence over time using **RTT‑inspired ideas**.

You will **not** fix bugs, enforce rules, or optimize behavior.  
Your goal is to **make assumptions visible**.

---

## Background (What You’re Practicing)

Traditional OS work often asks:
> *How do we prevent bad behavior?*

RTT asks:
> *How do we know when our assumptions stop holding?*

This assignment focuses on **observation**, not control.

---

## Setup

Use **any one** of the following:
- a teaching OS (e.g., xv6, Pintos, Nachos)
- a toy kernel or simulator provided by your instructor
- a minimal process scheduler or memory manager you’ve already built

You do **not** need a full Linux kernel.

---

## Task Overview

You will add **RTT‑style instrumentation** to your system by:

1. Declaring an assumption  
2. Observing behavior over time  
3. Emitting a structured signal (“badge”) when the assumption no longer holds  

You must **not** change system behavior in response.

---

## Step 1: Declare an Assumption 🧠

Choose **one** assumption your system currently makes.

Examples:
- “A process will eventually get CPU time.”
- “Memory accesses stay within allocated regions.”
- “Context switches preserve process state.”
- “Only one process runs in the critical section.”

Write this assumption in **one sentence**.

---

## Step 2: Define a Coherence Corridor 🛤️

Describe what *normal behavior* looks like for that assumption.

Examples:
- Maximum wait time before scheduling
- Valid memory address range
- Expected state before and after a context switch

This corridor defines **expected behavior**, not correctness.

---

## Step 3: Observe a Boundary 🔄

Identify **where** in the system the assumption could drift.

Examples:
- scheduler tick
- context switch
- memory access
- lock acquisition / release

Add **instrumentation only** at this boundary.

---

## Step 4: Emit a Badge 🏷️

When behavior exits the corridor, emit a **badge**.

A badge must include:
- what happened
- where it happened
- when it happened
- why it might matter

Example (conceptual):

```text
[BADGE]
type: CORRIDOR_BREACH
module: scheduler
context: process_wait_time_exceeded
timestamp: 123456
```

Badges may be printed, logged, or stored — format is flexible.

---

## Step 5: Do Nothing Else 🚫

This is critical.

Your system must:
- continue running
- not block execution
- not fix the issue
- not change scheduling or memory behavior

Observation only.

---

## Deliverables 📦

Submit:
1. A short description of your assumption and corridor
2. The code you added (instrumentation only)
3. Sample badge output
4. A brief reflection (5–7 sentences):
   - What drift did you observe?
   - Was it expected?
   - Did anything surprise you?

---

## Grading Criteria

You are graded on:
- clarity of the assumption
- correctness of observation
- quality of the badge signal
- restraint (no enforcement logic)

You are **not** graded on:
- performance
- fixing bugs
- preventing failure

---

## Why This Matters

Most real system failures happen because:
- assumptions drift silently
- boundaries aren’t observed
- time isn’t tracked explicitly

This assignment trains you to **see drift before acting**.

That skill scales far beyond operating systems.

---

## Optional Extension 🌱

Run your system under stress (more processes, tighter memory, faster ticks) and observe how badge frequency changes.

Do not “fix” anything — just watch.

---

### Instructor Note

This assignment pairs well with the RTT diagrams and can be completed in a single lab session or short project window.
