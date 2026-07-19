# qCompute — Resonance Frame Manager  
**File:** qc_ResonanceFrame.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

A **ResonanceFrame** is the fundamental structural container of qCompute.

Frames bind:

- environment  
- backend  
- resonance tier  
- drift envelope  
- operator list  
- timestamps  
- lineage  

Frames ensure that structural computation remains **stable**, **bounded**, and **governed**.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

The Frame Manager:

- opens frames  
- closes frames  
- enforces tier monotonicity  
- enforces backend consistency  
- enforces drift bounds  
- enforces environment legality  
- segments structural computation  
- emits frame metadata for capture  
- reconstructs frames during replay  

Frames are **append‑only** and **immutable after closure**.

---

# 2. Frame Identity

Each frame has:

```
frame_id: <int>
environment: "sandbox" | "production" | "archive"
backend: "<backend-id>"
tier: "r1" | "r2" | "r3"
drift:
  accumulated: <float>
  max: <float>
operators: [ ... ]
timestamp_open: "<iso8601>"
timestamp_close: "<iso8601>"
```

All fields are required.

---

# 3. When Frames Open

A new frame opens when:

1. **first operator**  
2. **tier escalation** (r1 → r2, r2 → r3)  
3. **tier decrease** (measurement)  
4. **r3 operator**  
5. **meta operator**  
6. **drift overflow**  
7. **environment transition**  
8. **backend change**  

Router determines the trigger; Frame Manager enforces it.

---

# 4. When Frames Close

A frame closes when:

- a new frame opens  
- an environment transition occurs  
- session ends  
- archive is entered  

Closed frames are immutable.

---

# 5. Tier Semantics Inside Frames

Tier monotonicity:

```
r1 → r2 → r3 (allowed)
r3 → r2 → r1 (forbidden)
```

If a tier decrease is attempted:

- measurement forces a new frame  
- other decreases are illegal  

If illegal:

```
allowed: false
reason: "tier decrease inside frame"
```

---

# 6. Backend Semantics Inside Frames

Backend must remain consistent within a frame.

If backend changes:

- frame closes  
- new frame opens  

Backend changes occur due to:

- tier escalation  
- r3 operator  
- environment transition  

---

# 7. Drift Semantics Inside Frames

Drift accumulates monotonically:

```
drift_total = drift_prev + drift_measured
```

If drift exceeds environment bound:

- frame closes  
- new frame opens  
- operator routed into new frame  

Drift resets when:

- new frame opens  
- measurement occurs  
- meta operator occurs  
- r3 operator occurs  

---

# 8. Environment Semantics Inside Frames

Environment must remain consistent within a frame.

If environment changes:

- frame closes  
- new frame opens  
- drift resets  
- backend legality rechecked  

Environment transitions:

- sandbox → production (token required)  
- production → archive (token required)  
- archive → (forbidden)  

---

# 9. Operator Interaction

Operators appended to a frame must satisfy:

- grammar validity  
- argument validity  
- environment legality  
- backend legality  
- tier monotonicity  
- drift bounds  

Operators carry:

- tier  
- backend  
- drift  
- routing reason  

---

# 10. Capture Metadata

Each frame produces:

```
frame:
  frame_id: <int>
  environment: "<env>"
  backend: "<backend-id>"
  tier: "<tier>"
  drift:
    accumulated: <float>
    max: <float>
  operators: [op_ids...]
  timestamp_open: "<iso8601>"
  timestamp_close: "<iso8601>"
```

All fields are required.

---

# 11. Replay Reconstruction

Replay reconstructs frames by:

1. reading operator stream  
2. applying routing logic  
3. applying drift logic  
4. applying tier monotonicity  
5. applying backend legality  
6. applying environment transitions  
7. opening/closing frames deterministically  

Replay must confirm:

- frame boundaries match routing + drift logic  
- backend consistency  
- tier monotonicity  
- drift bounds  
- environment legality  
- hash chain integrity  

Replay is deterministic and read‑only.

---

# 12. Invariants

1. frames are append‑only  
2. frames are immutable after closure  
3. tier must not decrease inside a frame  
4. backend must remain consistent inside a frame  
5. drift must not exceed bound  
6. r3 always opens a new frame  
7. measurement always opens a new frame  
8. meta always opens a new frame  
9. environment transitions always open a new frame  
10. archive forbids all operators  

---

# 13. Summary

ResonanceFrames provide:

- structural segmentation  
- stability envelopes  
- deterministic boundaries  
- drift‑bounded execution  
- environment‑aware computation  
- replay‑verifiable correctness  

Frames are the **structural heartbeat** of qCompute.
