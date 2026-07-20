# Interoperability Contracts

This document defines informal contracts
for interoperating CSM with RSM and RTT systems.

---

## Contract: Non‑Intrusion

CSM components must not:
- alter external substrate assumptions
- override existing control logic
- impose RTT interpretations

---

## Contract: Boundary Respect

All integrations must:
- preserve WR‑SADC core boundaries
- respect regime definitions
- avoid cross‑model leakage

---

## Contract: Optional Interpretation

RTT lenses may be applied
without affecting system operation.

Interpretation remains optional.
Operation remains primary.

---

## Final Note

Interoperability is achieved through alignment,
not enforcement.
