# qCompute — Structural Pipeline Flow  
**File:** qc_Flow.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document provides a **narrative walkthrough** of the qCompute structural pipeline.

The pipeline is:

```
operator → validator → router → frame manager → drift engine → transitions → capture → replay
```

qCompute computes **structure**, not amplitudes.

---

# 1. Operator Entry

A structural operator enters the system:

```python
session.h(q=0)
session.cx(q1=0, q2=1)
session.pulse(q=0, duration=20, amplitude=0.5)
session.measure(q=0)
```

Operators carry:

- name  
- parameters  
- resonance tier (r1 / r2 / r3)  
- drift characteristic  
- backend requirements  

The operator is passed to the **Validator**.

---

# 2. Validator

Validator enforces:

- grammar correctness  
- argument correctness  
- environment legality  
- tier legality  
- backend legality  
- token requirements  
- archive terminality  

If invalid:

```
allowed: false
reason: "<canonical reason>"
```

Invalid operators are captured but not executed.

If valid, the operator proceeds to the **Router**.

---

# 3. Router

Router selects:

- backend  
- frame reuse vs. new frame  
- routing reason  

Routing rules:

- r1 → `local-sim`  
- r2 → `hybrid-sim`  
- r3 → `hardware-qpu-2` (token required)  

Router may:

- reuse current frame  
- escalate tier → open new frame  
- detect drift overflow → open new frame  
- detect measurement → open new frame  

Router emits routing metadata and passes the operator to the **Frame Manager**.

---

# 4. Frame Manager

A **frame** is a structural container with:

- environment  
- backend  
- resonance profile  
- drift bound  
- drift summary  
- operator list  

Frame Manager:

- opens frames  
- closes frames  
- enforces tier monotonicity  
- enforces backend consistency  
- enforces environment legality  

Triggers for new frame:

- first operator  
- tier escalation  
- tier decrease (measurement)  
- r3 operator  
- drift overflow  
- meta operator  
- environment transition  

The operator is appended to the active frame and passed to the **Drift Engine**.

---

# 5. Drift Engine

Drift Engine computes:

- predicted drift  
- measured drift  
- accumulated drift  

Drift bounds:

| Environment | Drift Bound |
|-------------|-------------|
| sandbox     | relaxed     |
| production  | strict      |
| archive     | immutable   |

If drift exceeds bound:

- frame closes  
- new frame opens  
- operator is routed into new frame  

Drift metadata is appended and the operator proceeds to **Transitions**.

---

# 6. Transition Engine

Transitions are explicit:

```python
session.transition("production")
session.transition("archive")
```

Rules:

- sandbox → production (token required)  
- production → archive (token required)  
- archive → (forbidden)  

Transition Engine:

- closes current frame  
- updates environment  
- updates drift bound  
- updates backend legality  
- appends lineage  

Transition events are passed to **Capture**.

---

# 7. Capture Engine

Capture writes an append‑only `.qtrace` ledger.

Each operator produces:

- operator entry  
- validation metadata  
- routing metadata  
- drift metadata  
- timestamp  
- hash_prev / hash_self  

Each frame produces:

- frame summary  
- drift summary  
- operator list  
- timestamps  

Each transition produces:

- from / to  
- token used  
- timestamp  

Capture writes:

1. header  
2. operator entries  
3. frame summaries  
4. transitions  
5. footer  
6. hash chain root  

The `.qtrace` file is the **source of truth**.

---

# 8. Replay Engine

Replay reconstructs:

- session  
- frames  
- operators  
- transitions  
- lineage  
- drift accumulation  
- backend binding  
- tier monotonicity  

Replay verifies:

- hash chain integrity  
- environment legality  
- drift bounds  
- transition correctness  
- archive terminality  
- canonical field presence  

Replay is deterministic and read‑only.

---

# 9. Full Pipeline Diagram (Textual)

```
┌──────────────────────────────────────────────────────────────┐
│                        Operator Entry                         │
└───────────────┬──────────────────────────────────────────────┘
                ▼
        ┌──────────────┐
        │   Validator   │  grammar, args, env, tier, backend, token
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │    Router     │  backend, frame reuse/new, tier escalation
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │ Frame Manager │  open/close frames, tier monotonicity
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │ Drift Engine  │  predicted/measured drift, overflow
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │  Transitions  │  env changes, lineage, token use
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │   Capture     │  append-only .qtrace ledger
        └───────┬──────┘
                ▼
        ┌──────────────┐
        │    Replay     │  reconstruct + verify invariants
        └──────────────┘
```

---

# 10. Summary

The qCompute pipeline:

- validates  
- routes  
- frames  
- accumulates drift  
- transitions environments  
- captures a ledger  
- replays and verifies  

qCompute is the **structural compute harness** of RTT‑Inside.
