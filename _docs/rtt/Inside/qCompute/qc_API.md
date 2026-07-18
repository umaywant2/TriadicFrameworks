# qCompute — Public API  
**File:** qc_API.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **public API surface** for qCompute.

The API is:

- structural  
- deterministic  
- environment‑aware  
- drift‑bounded  
- replay‑safe  

The API does **not** simulate amplitudes or physical states.

---

# 1. Session API

### Create a session

```python
session = qSession(env="sandbox", backend="auto")
```

Arguments:

- `env`: `"sandbox" | "production" | "archive"`
- `backend`: `"auto"` or explicit backend ID

### Deploy a token

```python
session.deploy_token("token-id")
```

Tokens are required for:

- sandbox → production  
- production → archive  
- r3 operators  

### Transition environment

```python
session.transition("production")
session.transition("archive")
```

Rules:

- sandbox → production (token required)  
- production → archive (token required)  
- archive → (forbidden)  

### Save trace

```python
session.save_trace("example.qtrace")
```

Produces an append‑only `.qtrace` ledger.

---

# 2. Operator API

Operators are invoked directly on the session:

```python
session.h(q=0)
session.cx(q1=0, q2=1)
session.measure(q=0)
session.pulse(q=0, duration=20, amplitude=0.5)
```

Operator families:

- **r1**: primitive  
- **r2**: composite  
- **r3**: pulse  
- **measurement**  
- **meta**  

All operators pass through:

1. Validator  
2. Router  
3. Frame Manager  
4. Drift Engine  
5. Capture  

---

# 3. r1 Operators (Primitive)

```python
session.x(q=0)
session.y(q=0)
session.z(q=0)
session.h(q=0)
session.s(q=0)
session.t(q=0)
```

Rules:

- allowed in sandbox + production  
- low drift  
- backend: `local-sim`  

---

# 4. r2 Operators (Composite)

```python
session.cx(q1=0, q2=1)
session.cz(q1=0, q2=1)
session.swap(q1=0, q2=1)
```

Rules:

- allowed in sandbox + production  
- medium drift  
- backend: `hybrid-sim`  
- tier escalation opens new frame  

---

# 5. r3 Operators (Pulse)

```python
session.pulse(q=0, duration=20, amplitude=0.5)
```

Rules:

- production only  
- token required  
- backend: `hardware-qpu-2`  
- always opens new frame  
- high drift  

---

# 6. Measurement Operators

```python
session.measure(q=0)
```

Rules:

- allowed in sandbox + production  
- forces tier decrease  
- forces new frame  

---

# 7. Meta Operators

```python
session.barrier()
session.flush()
```

Rules:

- allowed in sandbox + production  
- always open new frame  
- zero drift  

---

# 8. Replay API

Load a trace:

```python
replay = qReplay("example.qtrace")
```

Access reconstructed structures:

```python
replay.session
replay.frames
replay.operators
replay.transitions
```

Replay is:

- deterministic  
- read‑only  
- invariant‑checking  
- hash‑verified  

---

# 9. Error Model

All structural errors raise:

```python
qComputeError("<canonical reason>")
```

Canonical reasons:

- `"invalid grammar"`
- `"invalid arguments"`
- `"illegal in environment"`
- `"backend mismatch"`
- `"backend illegal in environment"`
- `"tier decrease inside frame"`
- `"token required"`
- `"archive terminal"`
- `"illegal transition"`
- `"drift bound exceeded"`
- `"hash chain invalid"`

No other strings are permitted.

---

# 10. Summary

The qCompute API provides:

- session creation  
- environment transitions  
- token deployment  
- operator invocation  
- trace capture  
- replay verification  

The API is **structural**, **deterministic**, and **governed**.
