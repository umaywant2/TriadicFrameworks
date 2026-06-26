# qCompute — Minimal Structural Examples  
**File:** qc_Examples_Minimal.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

These examples demonstrate the **smallest possible** structural flows in qCompute.

They show:

- operator entry  
- validation  
- routing  
- frame creation  
- drift accumulation  
- transitions  
- capture  
- replay  

No amplitudes.  
No simulation.  
Structure only.

---

# 1. Minimal r1 Example (Sandbox)

```python
from qcompute import qSession

session = qSession(env="sandbox")

session.h(q=0)
session.x(q=0)

session.save_trace("r1_minimal.qtrace")
```

**What this demonstrates**

- sandbox environment  
- r1 operators  
- single frame  
- low drift  
- backend = local-sim  
- simple `.qtrace` with one frame  

---

# 2. Minimal r2 Example (Tier Escalation)

```python
session = qSession(env="sandbox")

session.h(q=0)          # r1 → frame 1
session.cx(q1=0, q2=1)  # r2 → new frame

session.save_trace("r2_minimal.qtrace")
```

**What this demonstrates**

- r1 → r2 tier escalation  
- automatic new frame  
- backend shift: local-sim → hybrid-sim  
- drift increase  
- two-frame `.qtrace`  

---

# 3. Minimal Measurement Example (Tier Decrease)

```python
session = qSession(env="sandbox")

session.cx(q1=0, q2=1)  # r2 → frame 1
session.measure(q=0)    # measurement → new frame

session.save_trace("measure_minimal.qtrace")
```

**What this demonstrates**

- r2 operator  
- measurement forces tier decrease  
- measurement forces new frame  
- drift reset  

---

# 4. Minimal r3 Example (Pulse Operator)

```python
session = qSession(env="production")
session.deploy_token("t1")

session.pulse(q=0, duration=20, amplitude=0.5)

session.save_trace("r3_minimal.qtrace")
```

**What this demonstrates**

- production environment  
- r3 operator  
- token requirement  
- backend = hardware-qpu-2  
- high drift  
- single-frame `.qtrace`  

---

# 5. Minimal Transition Example (Sandbox → Production)

```python
session = qSession(env="sandbox")
session.deploy_token("t1")

session.h(q=0)
session.transition("production")

session.save_trace("transition_minimal.qtrace")
```

**What this demonstrates**

- sandbox → production transition  
- token usage  
- frame closure on transition  
- lineage update  

---

# 6. Minimal Replay Example

```python
from qcompute import qReplay

replay = qReplay("r1_minimal.qtrace")

print(replay.session.env)
print(replay.frames[0].backend)
print(replay.operators[0].routing)
```

**What this demonstrates**

- loading a `.qtrace`  
- reconstructing session  
- accessing frames  
- accessing routing metadata  

---

# 7. Minimal Full Pipeline Example

```python
session = qSession(env="sandbox")
session.deploy_token("t1")

session.h(q=0)          # r1
session.cx(q1=0, q2=1)  # r2 → new frame
session.transition("production")
session.pulse(q=0, duration=10, amplitude=0.3)

session.save_trace("pipeline_minimal.qtrace")
```

**What this demonstrates**

- r1 → r2 → transition → r3  
- three frames  
- backend progression  
- drift progression  
- lineage: ["sandbox", "production"]  
- complete structural pipeline  

---

# Summary

These minimal examples show:

- r1, r2, r3 operators  
- tier escalation + tier decrease  
- drift behavior  
- environment transitions  
- capture + replay  
- the full structural pipeline in the smallest possible form  

Use these as the **entry point** for learning qCompute.
