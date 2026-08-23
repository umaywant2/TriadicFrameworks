# qCompute — Advanced Structural Examples  
**File:** qc_Examples_Advanced.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

These examples demonstrate **full‑pipeline**, **multi‑frame**, **multi‑backend**, and **multi‑transition** structural behavior in qCompute.

They show:

- tier escalation (r1 → r2 → r3)
- tier decrease (measurement)
- drift overflow
- backend switching
- environment transitions
- token usage
- meta‑operators
- capture + replay
- full structural lifecycle

No amplitudes.  
No simulation.  
Structure only.

---

# 1. Advanced Multi‑Frame Example (r1 → r2 → r1)

```python
session = qSession(env="sandbox")

session.h(q=0)            # r1 → frame 1
session.cx(q1=0, q2=1)    # r2 → new frame
session.measure(q=0)      # measurement → tier decrease → new frame
session.x(q=1)            # r1 → same frame

session.save_trace("adv_multiframe.qtrace")
```

**Demonstrates**

- r1 → r2 tier escalation  
- measurement forcing tier decrease  
- frame 1 (r1), frame 2 (r2), frame 3 (measurement + r1)  
- backend sequence: local-sim → hybrid-sim → local-sim  

---

# 2. Advanced Drift Overflow Example

```python
session = qSession(env="sandbox")

# r2 operators accumulate medium drift
session.cx(q1=0, q2=1)  
session.cx(q1=1, q2=2)
session.cx(q1=2, q2=3)

# drift overflow → new frame
session.cx(q1=3, q2=4)

session.save_trace("adv_drift_overflow.qtrace")
```

**Demonstrates**

- drift accumulation  
- drift overflow forcing new frame  
- backend = hybrid-sim  
- two frames with identical tier but different drift summaries  

---

# 3. Advanced Transition Example (Sandbox → Production → Archive)

```python
session = qSession(env="sandbox")
session.deploy_token("t1")
session.deploy_token("t2")

session.h(q=0)                 # sandbox
session.transition("production")  # token t1

session.pulse(q=0, duration=20, amplitude=0.5)  # r3 → production only

session.transition("archive")  # token t2

session.save_trace("adv_transitions.qtrace")
```

**Demonstrates**

- sandbox → production → archive  
- token usage  
- r3 operator allowed only in production  
- archive terminality  
- lineage: ["sandbox", "production", "archive"]  

---

# 4. Advanced Backend Switching Example

```python
session = qSession(env="production")
session.deploy_token("t1")

session.h(q=0)                    # r1 → local-sim
session.cx(q1=0, q2=1)            # r2 → hybrid-sim
session.pulse(q=1, duration=10, amplitude=0.4)  # r3 → hardware-qpu-2

session.save_trace("adv_backend_switch.qtrace")
```

**Demonstrates**

- backend progression: local-sim → hybrid-sim → hardware-qpu-2  
- tier escalation across three levels  
- r3 token requirement  

---

# 5. Advanced Meta‑Operator Example (Barrier + Flush)

```python
session = qSession(env="sandbox")

session.h(q=0)
session.barrier()                 # meta → new frame
session.cx(q1=0, q2=1)
session.flush()                   # meta → new frame

session.save_trace("adv_meta.qtrace")
```

**Demonstrates**

- meta‑operators always open new frames  
- zero drift  
- structural segmentation  

---

# 6. Advanced Mixed Pipeline Example (Full System)

```python
session = qSession(env="sandbox")
session.deploy_token("t1")
session.deploy_token("t2")

# Frame 1: r1
session.h(q=0)

# Frame 2: r2
session.cx(q1=0, q2=1)

# Transition to production
session.transition("production")   # token t1

# Frame 3: r3
session.pulse(q=0, duration=15, amplitude=0.3)

# Frame 4: measurement → tier decrease
session.measure(q=0)

# Transition to archive
session.transition("archive")      # token t2

session.save_trace("adv_full_pipeline.qtrace")
```

**Demonstrates**

- r1 → r2 → transition → r3 → measurement → transition  
- four frames  
- backend sequence: local-sim → hybrid-sim → hardware-qpu-2 → local-sim  
- drift progression  
- lineage: ["sandbox", "production", "archive"]  
- archive terminality  

---

# 7. Advanced Replay Example

```python
replay = qReplay("adv_full_pipeline.qtrace")

for frame in replay.frames:
    print(frame.frame_id, frame.backend, frame.resonance_profile)

for op in replay.operators:
    print(op.op_id, op.routing["reason"])
```

**Demonstrates**

- frame reconstruction  
- backend reconstruction  
- routing reasons  
- deterministic replay  
- invariant verification  

---

# Summary

These advanced examples demonstrate:

- multi‑tier execution  
- multi‑backend routing  
- drift overflow  
- environment transitions  
- token usage  
- meta‑operators  
- capture + replay  
- full structural lifecycle  

Use these examples to understand **complex qCompute behavior**.
