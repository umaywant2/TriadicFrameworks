# Diagram Spec — Collapse→Recovery Engine (CRE)

diagram:
  type: bidirectional-flow
  components:
    - CAV: Collapse‑Absorption Vector
    - REV: Recovery‑Emission Vector
    - CSV: Continuity‑Stabilization Vector

tensor:
  name: Collapse‑Recovery Tensor
  formula: T_CR = α·CAV + β·REV + γ·CSV + δ·R

flow:
  collapse:
    inputs:
      - collapse amplitude
      - collapse curvature
      - collapse torsion
    path:
      - CAV → CSV → REV
    outputs:
      - recovery emission
      - restored continuity

modes:
  - Formal Recovery
  - Emergent Recovery
  - Hybrid Recovery
  - Chaotic Recovery
  - Inversion Recovery

zones:
  - U: unified recovery
  - S: stable recovery
  - M: mixed recovery
  - D: divergent recovery
  - X: inversion recovery

notes:
  - CRE is the stabilization core of RTT/3
  - Collapse always flows CAV → CSV → REV
