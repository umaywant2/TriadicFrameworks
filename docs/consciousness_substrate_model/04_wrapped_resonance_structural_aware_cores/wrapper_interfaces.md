# Wrapper Interfaces

Wrappers define how a WR‑SADC core interfaces
with external systems.

---

## Wrapper Purpose

Wrappers exist to:
- isolate the core from direct external manipulation
- translate signals without altering internal structure
- enforce boundary conditions

Wrappers are replaceable.
Cores are not.

---

## Interface Characteristics

A valid wrapper interface must:
- preserve internal state integrity
- avoid direct mutation of core primitives
- expose only bounded signals
- support graceful degradation

Wrappers may be layered.
No wrapper may bypass core boundaries.
