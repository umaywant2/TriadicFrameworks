# qCompute — Backend Overview  
**File:** qc_Backends.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

Backends define the **structural execution substrate** for qCompute.

They do not simulate amplitudes.  
They do not compute physics.  
They provide **structural legality**, **tier binding**, and **environment constraints**.

qCompute computes **structure**, not amplitudes.

---

# 1. Backend List

qCompute defines **three canonical backends**:

| Backend | Tier Support | Environments | Drift | Notes |
|---------|--------------|--------------|--------|-------|
| **local-sim** | r1 | sandbox, production | low | primitive structural execution |
| **hybrid-sim** | r1, r2 | sandbox, production | medium | composite structural execution |
| **hardware-qpu-2** | r3 | production only | high | pulse‑tier structural execution |

These backends are **structural abstractions**, not hardware interfaces.

---

# 2. Backend Identity

Each backend has:

```
backend_id: "<id>"
tier_support: [r1 | r2 | r3]
environment_legal: ["sandbox" | "production"]
drift_profile: "low" | "medium" | "high"
frame_behavior: "reuse" | "new"
transition_behavior: "allowed" | "forbidden"
```

All fields are required.

---

# 3. Backend Descriptions

## 3.1 local-sim

```
backend_id: "local-sim"
tier_support: ["r1"]
environment_legal: ["sandbox", "production"]
drift_profile: "low"
frame_behavior: "reuse"
transition_behavior: "allowed"
```

Used for:

- primitive operators (r1)  
- low‑drift structural steps  
- stable frames  

---

## 3.2 hybrid-sim

```
backend_id: "hybrid-sim"
tier_support: ["r1", "r2"]
environment_legal: ["sandbox", "production"]
drift_profile: "medium"
frame_behavior: "reuse-or-new"
transition_behavior: "allowed"
```

Used for:

- composite operators (r2)  
- tier escalation  
- medium drift accumulation  

Router may reuse or open a new frame depending on:

- tier escalation  
- drift overflow  
- measurement events  

---

## 3.3 hardware-qpu-2

```
backend_id: "hardware-qpu-2"
tier_support: ["r3"]
environment_legal: ["production"]
drift_profile: "high"
frame_behavior: "new"
transition_behavior: "allowed"
```

Used for:

- pulse operators (r3)  
- high‑drift structural steps  
- token‑gated operations  

Always opens a new frame.

Forbidden in:

- sandbox  
- archive  

---

# 4. Environment Legality

| Environment | local-sim | hybrid-sim | hardware-qpu-2 |
|-------------|-----------|------------|-----------------|
| sandbox | ✓ | ✓ | ✗ |
| production | ✓ | ✓ | ✓ |
| archive | ✗ | ✗ | ✗ |

Archive is terminal and forbids all operators.

---

# 5. Tier Binding

| Tier | Backend |
|------|----------|
| r1 | local-sim |
| r2 | hybrid-sim |
| r3 | hardware-qpu-2 |

Tier binding is deterministic and replay‑verifiable.

---

# 6. Frame Interaction

Backends influence frame behavior:

- **local-sim**: may reuse frame  
- **hybrid-sim**: may reuse or open new frame  
- **hardware-qpu-2**: always opens new frame  

Frame boundaries are also influenced by:

- tier escalation  
- tier decrease  
- drift overflow  
- meta operators  
- environment transitions  

---

# 7. Transition Interaction

Backends must remain legal across transitions:

- sandbox → production: all backends legal  
- production → archive: no backends legal  
- archive → (forbidden)  

Transitions close the current frame and open a new one.

---

# 8. Capture Metadata

Each operator includes backend metadata:

```
routing:
  backend: "<backend-id>"
  reason: "<routing-reason>"
  frame_action: "reuse" | "new"
```

Each frame includes backend summary:

```
frame_backend:
  id: "<backend-id>"
  tier_support: [...]
  drift_profile: "<profile>"
```

All fields are required.

---

# 9. Replay Verification

Replay verifies:

- backend legality  
- tier binding  
- environment legality  
- frame boundaries  
- drift consistency  
- transition correctness  

Replay is deterministic and read‑only.

---

# 10. Summary

Backends define:

- tier support  
- environment legality  
- drift profile  
- frame behavior  
- transition behavior  

They are the **structural substrate** of qCompute.
