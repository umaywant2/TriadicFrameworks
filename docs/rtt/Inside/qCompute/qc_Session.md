# qCompute — Session Engine  
**File:** qc_Session.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

A **qSession** is the structural container for all qCompute activity.

It governs:

- environment  
- drift bound  
- backend legality  
- resonance frames  
- tokens  
- lineage  
- transitions  
- capture lifecycle  

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Session Engine:

- initializes structural context  
- manages environment  
- manages tokens  
- manages frames  
- manages drift envelope  
- orchestrates routing  
- orchestrates transitions  
- orchestrates capture  
- provides replay‑verifiable structure  

A session is the **root of structural truth**.

---

# 2. Session Identity

A session has:

```
session_id: "<uuid>"
environment: "sandbox" | "production" | "archive"
drift_bound: "<float>"
backend_legal: [...]
frames: []
lineage: ["sandbox", ...]
tokens: { deployed: [...] }
timestamp_open: "<iso8601>"
timestamp_close: "<iso8601>"
```

All fields are required.

---

# 3. Session Construction

```python
session = qSession(env="sandbox", backend="auto")
```

Arguments:

- `env`: `"sandbox" | "production" | "archive"`
- `backend`: `"auto"` or explicit backend ID

Defaults:

- environment = sandbox  
- backend = auto (tier‑bound)  

---

# 4. Environment Model

Environments define legality:

| Environment | Allowed Tiers | Drift Bound | Notes |
|-------------|---------------|-------------|-------|
| sandbox | r1, r2 | relaxed | development |
| production | r1, r2, r3 | strict | governed |
| archive | none | immutable | terminal |

Environment is updated only through transitions.

---

# 5. Token Model

Tokens are required for:

- sandbox → production  
- production → archive  
- r3 operators  

Deploy token:

```python
session.deploy_token("token-id")
```

Token state:

```
tokens:
  deployed: ["t1", "t2", ...]
```

---

# 6. Frame Model

A session contains **ResonanceFrames**.

Frame lifecycle:

- open on first operator  
- open on tier escalation  
- open on tier decrease  
- open on r3 operator  
- open on meta operator  
- open on drift overflow  
- open on environment transition  
- close when new frame opens  
- close when session ends  

Frames are append‑only and immutable after closure.

---

# 7. Drift Model

Session maintains drift envelope:

```
drift:
  accumulated: <float>
  bound: <float>
```

Drift resets when:

- new frame opens  
- measurement occurs  
- meta operator occurs  
- r3 operator occurs  
- environment transitions  

Drift must never exceed bound.

---

# 8. Operator Lifecycle

Operator flow inside a session:

```
operator → validator → router → frame manager → drift engine → capture
```

Session orchestrates:

- legality  
- routing  
- frame boundaries  
- drift accumulation  
- transition enforcement  
- capture ledger updates  

Operators are appended to the active frame.

---

# 9. Transition Lifecycle

Transitions are invoked via:

```python
session.transition("production")
session.transition("archive")
```

Transitions:

- require tokens  
- close current frame  
- update environment  
- reset drift  
- open new frame  
- update lineage  
- update backend legality  
- emit transition metadata  

Archive is terminal.

---

# 10. Capture Lifecycle

Save trace:

```python
session.save_trace("example.qtrace")
```

Capture writes:

- header  
- operator entries  
- frame summaries  
- transitions  
- footer  
- hash chain root  

Capture is append‑only and immutable.

---

# 11. Replay Integration

Replay reconstructs:

- session  
- frames  
- operators  
- transitions  
- drift  
- routing  
- backend legality  
- environment sequence  
- hash chain integrity  

Replay is deterministic and read‑only.

---

# 12. Invariants

1. environment must be legal  
2. backend must be legal  
3. drift must not exceed bound  
4. tier must not decrease inside a frame  
5. r3 requires token  
6. transitions require token  
7. transitions always open new frames  
8. archive is terminal  
9. capture must maintain valid hash chain  
10. frames are immutable after closure  

---

# 13. Summary

The Session Engine provides:

- structural context  
- environment governance  
- drift envelope  
- frame lifecycle  
- routing orchestration  
- transition orchestration  
- capture lifecycle  
- replay‑verifiable structure  

A session is the **governed container** for all qCompute computation.
