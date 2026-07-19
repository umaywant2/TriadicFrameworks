# Reference Architecture

This document presents a minimal reference architecture
for an autonomous form using a WR‑SADC core.

---

## Core Placement

- One WR‑SADC core per autonomous form
- Core isolated behind wrapper interfaces
- No direct external mutation of core state

---

## Surrounding Systems

The reference architecture assumes the presence of:
- sensing or input subsystems
- control, planning, or learning components
- actuation or output subsystems

These systems interact with the core
only through defined wrappers.

---

## Data Flow

- External signals enter through wrappers
- Core evaluates resonance and validity
- Signals indicating misalignment or transition
  are emitted outward

The core informs.
Other systems act.
