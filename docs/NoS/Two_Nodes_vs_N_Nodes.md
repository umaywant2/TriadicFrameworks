## Lab: RTT Instrumentation — Two Nodes vs N Nodes 🌐  
*(Seeing Coherence Collapse as Scale Increases)*

### Objective

In this lab, you will instrument a distributed system using **RTT‑style observation** and compare system behavior in:

- a **two‑node configuration**
- an **N‑node configuration** (N ≥ 5)

You will observe how **coherence drift changes with scale**, without adding coordination, retries, or enforcement.

---

## Core Question

> *What assumptions hold at two nodes that quietly fail at N nodes?*

RTT helps you see the answer.

---

## System Setup

Use any distributed system you already have access to:
- message‑passing nodes
- replicated key‑value store
- leader‑based service
- consensus simulator (without enforcing consensus)

You may simulate all nodes on one machine.

---

## Phase 1: Two‑Node Instrumentation 🔁

### Step 1: Declare an Assumption

Choose **one distributed assumption**.

Examples:
- “Both nodes eventually agree on the latest value.”
- “Messages arrive within a bounded time.”
- “Only one node believes it is leader.”

Write it in **one sentence**.

---

### Step 2: Define a Coherence Corridor

Define what *normal behavior* looks like **between two nodes**.

Examples:
- Maximum message delay
- Allowed version divergence
- Heartbeat interval

This corridor defines *expected coherence*, not correctness.

---

### Step 3: Observe a Boundary

Instrument **one boundary**:
- message send / receive
- state update
- timeout
- leadership change

Add **observation only**.

---

### Step 4: Emit Badges

When behavior exits the corridor, emit a badge:

```text
[BADGE]
type: COHERENCE_DRIFT
node: node_A
context: version_lag_exceeded
timestamp: 10234
```

Run the system and collect badge output.

---

## Phase 2: N‑Node Instrumentation 🔗

Now scale the **same system** to **N nodes (≥5)**.

Do **not**:
- change logic
- add coordination
- tighten timeouts
- fix anything

Only scale the node count.

---

### Observe and Record

Run the system under similar load and record:

- badge frequency
- badge symmetry (which nodes emit)
- time to first drift
- whether drift stabilizes or cascades

---

## Comparison Analysis 📊

Create a short comparison table:

| Aspect | Two Nodes | N Nodes |
|------|-----------|---------|
| First drift observed | | |
| Badge frequency | | |
| Drift symmetry | | |
| Time sensitivity | | |

---

## Reflection Questions 🧠

Answer briefly:

1. Which assumptions held at two nodes but failed at N?
2. Did drift appear gradually or suddenly?
3. Did time matter more than state?
4. Did any node “know” the system was incoherent?
5. Would enforcement have helped — or hidden the problem?

---

## Key Insight (What You Should Notice)

At two nodes:
- assumptions feel stable
- drift is rare and symmetric
- time feels manageable

At N nodes:
- drift appears earlier
- assumptions fragment
- time dominates behavior
- coherence becomes *emergent*, not guaranteed

RTT makes this visible **without fixing anything**.

---

## What You Must Not Do 🚫

- No retries
- No leader re‑election
- No resynchronization
- No consistency enforcement

Observation only.

---

## Deliverables 📦

Submit:
1. Assumption and corridor definition
2. Instrumentation code
3. Badge samples from two‑node and N‑node runs
4. Comparison table
5. Short reflection (8–10 sentences)

---

## Why This Lab Matters

Most distributed systems are designed at small scale and **fail at large scale** — not because logic breaks, but because **assumptions stop holding silently**.

RTT trains you to:
- see that moment
- name it
- reason about it

Before you try to fix it.

---

### Instructor Note

This lab pairs well with lectures on:
- CAP theorem
- failure detectors
- eventual consistency
- clock skew and partial order

Students often report that this is the first time they *see* scale as a coherence problem, not just a performance one.
