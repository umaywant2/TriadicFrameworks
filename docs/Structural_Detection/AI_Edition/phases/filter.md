# Filter Phase
**Book 3 — Structural Detection (AI Edition)**  
**Phase 4 of 6**

## Structural Role
Filter suppresses noise, false positives, and unstable probe artifacts.

## Dominant Operator
- **SD‑Ξ — NoiseGate**

## Alignment
- **N (noise‑dominant)**

## Dynamics
- noise_gate_fields → generate  
- filtered_signal_fields → refine  
- anomaly_map → reduce false positives  

## Kernel Constraints
- must_not_suppress_PX_001_through_PX_010  
- must_not_invent_drift_costs  

## Transition
Filter → Confirm  
(SD‑Λ and SD‑Ξ jointly stabilize.)
