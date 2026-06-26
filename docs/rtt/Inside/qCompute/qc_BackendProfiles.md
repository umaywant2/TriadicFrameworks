# qCompute — Backend Metadata Profiles  
**File:** qc_BackendProfiles.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

This document defines the **deep metadata profiles** for all qCompute backends.

Backends are **structural abstractions**, not hardware interfaces.  
They define legality, drift envelopes, tier support, and routing behavior.

qCompute computes **structure**, not amplitudes.

---

# 1. Metadata Schema

Each backend profile follows this schema:

```
backend_id: "<string>"
display_name: "<string>"

tier_support:
  - r1 | r2 | r3

environment_legal:
  - sandbox | production

drift_envelope:
  predicted: "<low|medium|high>"
  measured: "<low|medium|high>"
  max_accumulated: <float>

frame_behavior:
  reuse: true|false
  always_new: true|false

transition_behavior:
  sandbox_to_production: "allowed" | "token-required" | "forbidden"
  production_to_archive: "allowed" | "token-required" | "forbidden"

routing_constraints:
  tier_binding: "<r1|r2|r3>"
  environment_required: "<sandbox|production>"
  token_required: true|false

notes: "<freeform>"
```

All fields are required.

---

# 2. Backend Profiles

## 2.1 local-sim

```
backend_id: "local-sim"
display_name: "Local Structural Simulator"

tier_support:
  - r1

environment_legal:
  - sandbox
  - production

drift_envelope:
  predicted: "low"
  measured: "low"
  max_accumulated: 1.0

frame_behavior:
  reuse: true
  always_new: false

transition_behavior:
  sandbox_to_production: "allowed"
  production_to_archive: "forbidden"

routing_constraints:
  tier_binding: "r1"
  environment_required: "sandbox-or-production"
  token_required: false

notes: "Used for primitive operators. Stable, low drift, frame reuse preferred."
```

---

## 2.2 hybrid-sim

```
backend_id: "hybrid-sim"
display_name: "Hybrid Structural Simulator"

tier_support:
  - r1
  - r2

environment_legal:
  - sandbox
  - production

drift_envelope:
  predicted: "medium"
  measured: "medium"
  max_accumulated: 3.0

frame_behavior:
  reuse: true
  always_new: false

transition_behavior:
  sandbox_to_production: "allowed"
  production_to_archive: "forbidden"

routing_constraints:
  tier_binding: "r2"
  environment_required: "sandbox-or-production"
  token_required: false

notes: "Used for composite operators. Medium drift. May reuse or open new frame depending on tier escalation or drift overflow."
```

---

## 2.3 hardware-qpu-2

```
backend_id: "hardware-qpu-2"
display_name: "Hardware Pulse Tier (Structural)"

tier_support:
  - r3

environment_legal:
  - production

drift_envelope:
  predicted: "high"
  measured: "high"
  max_accumulated: 0.5

frame_behavior:
  reuse: false
  always_new: true

transition_behavior:
  sandbox_to_production: "token-required"
  production_to_archive: "token-required"

routing_constraints:
  tier_binding: "r3"
  environment_required: "production"
  token_required: true

notes: "Used for pulse operators. High drift. Always opens new frame. Token-gated. Forbidden in sandbox and archive."
```

---

# 3. Cross‑Backend Comparison

| Property | local-sim | hybrid-sim | hardware-qpu-2 |
|----------|-----------|------------|-----------------|
| Tier Support | r1 | r1, r2 | r3 |
| Drift | low | medium | high |
| Frame Reuse | yes | yes | no |
| Always New Frame | no | no | yes |
| Sandbox Legal | yes | yes | no |
| Production Legal | yes | yes | yes |
| Token Required | no | no | yes |
| Max Drift | 1.0 | 3.0 | 0.5 |

---

# 4. Routing Integration

Router uses backend profiles to determine:

- backend legality  
- tier binding  
- environment legality  
- token requirements  
- frame reuse vs. new frame  
- drift overflow thresholds  

Routing reasons include:

- `"tier-escalation"`  
- `"tier-binding"`  
- `"environment-requirement"`  
- `"token-required"`  
- `"drift-overflow"`  
- `"measurement"`  
- `"meta"`  

---

# 5. Capture Metadata

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
  drift_profile: "<low|medium|high>"
  tier_support: [...]
```

All fields are required.

---

# 6. Replay Verification

Replay verifies:

- backend legality  
- tier binding  
- environment legality  
- drift envelope  
- frame boundaries  
- transition correctness  
- token requirements  
- hash chain integrity  

Replay is deterministic and read‑only.

---

# 7. Invariants

1. r1 → local-sim  
2. r2 → hybrid-sim  
3. r3 → hardware-qpu-2  
4. hardware-qpu-2 requires production  
5. hardware-qpu-2 requires token  
6. drift must not exceed envelope  
7. frame behavior must match backend profile  
8. archive forbids all backends  

---

# 8. Summary

Backend Profiles define:

- identity  
- tier support  
- drift envelopes  
- environment legality  
- frame behavior  
- transition behavior  
- routing constraints  

They are the **deep structural metadata layer** of qCompute.
