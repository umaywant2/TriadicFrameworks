# qCompute — Routing Engine  
**File:** qc_Router.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

The Routing Engine determines:

- backend selection  
- frame reuse vs. new frame  
- tier escalation  
- drift‑overflow routing  
- measurement routing  
- meta routing  
- environment legality  
- token requirements  

Routing is **deterministic**, **governed**, and **replay‑verifiable**.

qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

Router receives a validated operator and decides:

1. **backend**  
2. **frame action** (`reuse` or `new`)  
3. **routing reason**  
4. **environment legality**  
5. **token requirements**  

Router emits routing metadata for capture and replay.

---

# 2. Routing Inputs

Router receives:

```
operator:
  name
  tier
  params

session:
  environment
  token_state
  current_frame

frame:
  tier
  backend
  drift_state

backend_profiles:
  legality
  tier_binding
  drift_envelope
```

All fields are required.

---

# 3. Backend Selection

Backend is determined by **tier binding**:

| Tier | Backend |
|------|----------|
| r1 | local-sim |
| r2 | hybrid-sim |
| r3 | hardware-qpu-2 |

Backend legality is checked against environment:

- sandbox: r1, r2  
- production: r1, r2, r3  
- archive: none  

If illegal:

```
allowed: false
reason: "backend illegal in environment"
```

---

# 4. Frame Reuse vs. New Frame

Router decides whether to reuse the current frame or open a new one.

### 4.1 Reuse Frame

Allowed when:

- tier does not escalate  
- drift does not overflow  
- operator is not measurement  
- operator is not meta  
- operator is not r3  
- environment does not change  

### 4.2 New Frame

Required when:

- **tier escalation** (r1 → r2, r2 → r3)  
- **tier decrease** (measurement)  
- **r3 operator**  
- **meta operator**  
- **drift overflow**  
- **environment transition**  
- **backend change**  

Router must always choose the **strongest trigger**.

---

# 5. Routing Reasons

Router emits one canonical reason:

- `"tier-binding"`  
- `"tier-escalation"`  
- `"tier-decrease"`  
- `"measurement"`  
- `"meta"`  
- `"r3-requires-new-frame"`  
- `"backend-change"`  
- `"environment-transition"`  
- `"drift-overflow"`  
- `"token-required"`  

Only one reason is emitted per operator.

---

# 6. Token Requirements

Token is required for:

- r3 operators  
- sandbox → production transition  
- production → archive transition  

If missing:

```
allowed: false
reason: "token required"
```

---

# 7. Routing Algorithm (Deterministic)

```
1. Determine backend from tier.
2. Check backend legality in environment.
3. Check token requirements.
4. Determine if tier escalates or decreases.
5. Check for measurement or meta operator.
6. Check drift overflow.
7. Check environment transition.
8. Decide frame_action = reuse | new.
9. Emit routing reason.
10. Emit routing metadata.
```

Router never uses heuristics.  
Router never uses randomness.

---

# 8. Routing Metadata (Capture)

Each operator produces:

```
routing:
  backend: "<backend-id>"
  frame_action: "reuse" | "new"
  reason: "<canonical-reason>"
```

Each frame produces:

```
frame_backend:
  id: "<backend-id>"
  tier_support: [...]
  drift_profile: "<low|medium|high>"
```

All fields are required.

---

# 9. Replay Verification

Replay recomputes routing:

- backend selection  
- frame boundaries  
- tier escalation  
- tier decrease  
- drift overflow  
- environment transitions  
- token requirements  

Replay must confirm:

- routing reason matches canonical logic  
- frame boundaries match routing logic  
- backend legality is preserved  
- environment legality is preserved  
- drift overflow is correct  
- token requirements are satisfied  

Replay is deterministic and read‑only.

---

# 10. Invariants

1. r1 → local-sim  
2. r2 → hybrid-sim  
3. r3 → hardware-qpu-2  
4. r3 always opens new frame  
5. measurement always opens new frame  
6. meta always opens new frame  
7. drift overflow always opens new frame  
8. tier may increase but never decrease within a frame  
9. environment transitions always open new frame  
10. archive forbids all operators  

---

# 11. Summary

Router provides:

- deterministic backend selection  
- deterministic frame boundaries  
- deterministic routing reasons  
- deterministic legality enforcement  

Router is the **structural decision engine** of qCompute.
