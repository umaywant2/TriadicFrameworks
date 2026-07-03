# qCompute — Drift Engine  
**File:** qc_Drift.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Drift Engine computes and enforces **structural drift** for all qCompute sessions.

Drift is a measure of **structural instability** introduced by operators, backends, and environment transitions.  
It is deterministic, rule‑driven, and replay‑verifiable.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Drift Engine:

- computes predicted drift  
- computes measured drift  
- accumulates drift within a frame  
- enforces drift bounds  
- triggers frame closure on overflow  
- emits drift metadata for capture  
- verifies drift during replay  

Drift ensures that structural computation remains **stable**, **bounded**, and **governed**.

---

# 2. Drift Characteristics by Tier

| Tier | Drift Level | Notes |
|------|-------------|-------|
| **r1** | low | primitive operators |
| **r2** | medium | composite operators |
| **r3** | high | pulse operators |
| **measurement** | reset | forces new frame |
| **meta** | zero | barrier, flush |

---

# 3. Environment Drift Bounds

| Environment | Drift Bound | Notes |
|-------------|-------------|-------|
| **sandbox** | relaxed | allows more accumulation |
| **production** | strict | minimal tolerance |
| **archive** | immutable | no operators allowed |

Drift bound is checked **after every operator**.

---

# 4. Drift Accumulation Model

Each operator contributes:

```
drift_predicted: <float>
drift_measured: <float>
drift_total: drift_prev + drift_measured
```

Drift accumulation is:

- monotonic within a frame  
- reset when a new frame opens  
- environment‑bounded  

---

# 5. Drift Overflow

If:

```
drift_total > drift_bound
```

Then:

1. current frame closes  
2. new frame opens  
3. operator is routed into the new frame  
4. drift resets to operator’s measured drift  

Overflow is deterministic and replay‑verifiable.

---

# 6. Frame Interaction

Drift interacts with frames as follows:

- r1: may reuse frame  
- r2: may reuse frame or escalate tier → new frame  
- r3: always opens new frame  
- measurement: always opens new frame  
- meta: always opens new frame  

Drift overflow is an **additional** trigger for new frame creation.

---

# 7. Routing Interaction

Router receives drift metadata:

```
routing:
  backend: "<backend>"
  reason: "<reason>"
  frame_action: "reuse" | "new"
```

Drift Engine may override Router’s frame decision if overflow occurs.

---

# 8. Capture Metadata

Each operator produces drift metadata:

```
drift:
  predicted: <float>
  measured: <float>
  accumulated: <float>
  overflow: true | false
```

Each frame produces a drift summary:

```
frame_drift:
  total: <float>
  max: <float>
  environment_bound: <float>
```

All fields are required.

---

# 9. Replay Verification

Replay recomputes drift:

- predicted drift  
- measured drift  
- accumulated drift  
- overflow events  
- frame boundaries  
- environment bounds  

Replay must confirm:

- drift never exceeds bound  
- overflow events match capture  
- frame boundaries match drift logic  
- drift summaries match operator accumulation  

Replay is deterministic and read‑only.

---

# 10. Invariants

1. drift must not exceed environment bound  
2. overflow must open a new frame  
3. measurement resets drift  
4. meta operators reset drift  
5. r3 operators reset drift  
6. drift accumulation must be monotonic within a frame  
7. drift summaries must match operator accumulation  
8. archive forbids all operators  

---

# 11. Summary

The Drift Engine ensures:

- structural stability  
- deterministic accumulation  
- governed overflow  
- environment‑bounded execution  
- replay‑verifiable correctness  

Drift is a **first‑class structural signal** in qCompute.
