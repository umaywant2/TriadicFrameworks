## Assignment: Instrument a Distributed System Using RTT 🌐  
*(Observing Coherence Without Coordination)*

### Objective

In this assignment, you will **instrument a distributed system** to observe **coherence over time** using **RTT‑inspired ideas**.

You will **not**:
- enforce consistency
- fix failures
- add coordination protocols
- optimize performance

Your goal is to **make assumptions visible across nodes**.

---

## Background (Why RTT Fits Distributed Systems)

Distributed systems fail not because rules are missing, but because:
- time is inconsistent
- assumptions diverge across nodes
- boundaries are crossed silently

RTT treats these as **coherence problems**, not control problems.

---

## Setup

Use **any one** of the following:
- a key‑value store (toy or real)
- a message‑passing system
- a replicated service
- a consensus simulator
- a distributed lab framework provided by your instructor

You may simulate nodes on a single machine.

---

## Task Overview

You will:
1. Declare a **distributed assumption**
2. Define a **coherence corridor**
3. Observe **boundary events**
4. Emit **badges** when assumptions drift
5. Do nothing else

---

## Step 1: Declare a Distributed Assumption 🧠

Choose **one assumption** your system implicitly makes.

Examples:
- “All replicas eventually see the same value.”
- “Messages are delivered within a bounded time.”
- “Leaders are unique at any moment.”
- “Clocks are close enough to compare timestamps.”
- “Requests are processed in causal order.”

Write this assumption in **one sentence**.

---

## Step 2: Define a Coherence Corridor 🛤️

Describe what *normal behavior* looks like **over time and across nodes**.

Examples:
- Maximum acceptable message delay
- Allowed divergence window between replicas
- Expected heartbeat interval
- Acceptable clock skew

This corridor defines **expected coherence**, not correctness.

---

## Step 3: Observe a Boundary 🔄

Identify **where the assumption could drift**.

Examples:
- message send / receive
- replica update
- leader election
- timeout expiration
- state synchronization

Add instrumentation **only at this boundary**.

---

## Step 4: Emit a Badge 🏷️

When behavior exits the corridor, emit a **badge**.

A badge must include:
- what happened
- which node observed it
- when it was observed (local time is fine)
- relevant context (IDs, versions, delays)

Example (conceptual):

```text
[BADGE]
type: COHERENCE_DRIFT
module: replication
node: replica_3
context: version_lag_exceeded
timestamp: 48291
```

Badges may be logged locally or collected centrally.

---

## Step 5: Do Not Coordinate 🚫

This is critical.

Your system must:
- not retry
- not re‑elect
- not resynchronize
- not block progress

Observation only.

---

## Deliverables 📦

Submit:
1. Your declared assumption and corridor
2. Instrumentation code
3. Sample badge output from multiple nodes
4. A short reflection (5–7 sentences):
   - Did drift occur?
   - Was it symmetric across nodes?
   - Did time matter more than state?

---

## Grading Criteria

You are graded on:
- clarity of the assumption
- correctness of observation
- usefulness of badge context
- restraint (no control logic)

You are **not** graded on:
- consistency guarantees
- fault tolerance
- performance

---

## Why This Matters

Most distributed failures are not bugs — they are **unobserved divergence**.

RTT trains you to:
- see drift before coordination
- separate observation from agreement
- reason about time explicitly

These skills apply to:
- databases
- consensus systems
- microservices
- distributed AI systems

---

## Optional Extension 🌱

Introduce:
- network delay
- message loss
- clock skew

Observe how badge patterns change.

Do not “fix” anything.

---

### Instructor Note

This assignment pairs well with lectures on:
- eventual consistency
- CAP tradeoffs
- failure detectors
- logical vs physical time

Students often discover that **time**, not logic, is the hardest part.
