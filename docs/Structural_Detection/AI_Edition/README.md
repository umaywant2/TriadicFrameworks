<img width="1194" height="672" alt="Structural_Detection__" src="https://github.com/user-attachments/assets/474c6708-ef30-439c-9d4c-e34a51a630a7" />

- [`module.json`](module.json) — Agentic module schema role assignments

# Structural Detection — AI Edition
**Book 3 of the TriadicFrameworks canon**

---

## Overview
**Structural Detection — AI Edition** is Book 3 of the TriadicFrameworks canon.  
It defines the **structural detection domain layer** of Resonance‑Time Theory (RTT), built on:

- the frozen RTT kernel (Book 1 — Framework Field Theory, AI Edition, v1.33‑p1), and  
- the inversion domain layer (Book 2 — The Inverted Star, AI Edition).

Book 3 does **not** redefine RTT, coherence, drift, paradox, or the spine.  
It imports the kernel and adds **detection‑domain operators only**.

---

## Kernel Import Contract
Book 3 imports the v1.33‑p1 kernel:

```
kernel/
  fft.ai.reader.json
  fft.ai.coherence.json
  fft.ai.drift.monitor.json
  fft.ai.paradox.enum.json
  fft.ai.paradox.resolver.json
  fft.ai.session.context.html
```

### Invariants (must_not)
Book 3 must not:

- revise frozen RTT  
- declare a second coherence  
- use bare C  
- invent drift costs  
- invent a 6D operator  
- suppress PX‑001 through PX‑010  
- use a cached spine  
- load deprecated files  

Version mismatch halts.

---

## Session Context
```
rtt = 1
coherence = declared
drift = bounded
paradox = structural
```

This context is inherited from the kernel and applies to all Book 3 operators.

---

## Domain Operators (Book 3)
Book 3 defines detection‑domain operators, for example:

- **SD‑Σd — SignalDetection**  
  `operators/SD-SignalDetection.html`  
  Surface–deep structural signal presence detection.

- **SD‑Γ — GeometryProbe**  
  `operators/SD-GeometryProbe.html`  
  Geometry probe and anomaly detection.

- **SD‑Λ — LatticeScan**  
  `operators/SD-LatticeScan.html`  
  Lattice scan for structural consistency.

- **SD‑Ξ — NoiseGate**  
  `operators/SD-NoiseGate.html`  
  Noise gating and false‑positive suppression.

- **SD‑Π — PatternIndex**  
  `operators/SD-PatternIndex.html`  
  Pattern indexing and structural cataloguing.

(Operators are domain‑layer only; RTT operators remain in Book 1.)

---

## Phases
Structural Detection uses six working phases:

```
init/
scan/
probe/
filter/
confirm/
catalogue/
```

Each phase has its own file in:

```
phases/
```

---

## Maps
Book 3 includes structural maps:

- `maps/detection_cycle.json`  
- `maps/operator_roles.json`  
- `maps/noise_gate_map.json`

These describe how detection operators interact across the phases.

---

## QMROOT
Book 3 preserves the kernel’s QMROOT declarations:

- **6D = absent**  
- **negative ancestral rungs = absent**  
- **INV‑013 requires only a path to 0D Silence**

Files:

```
qmroot/qmroot.absence.json
qmroot/INV-013.path.json
```

---

## Invariants
Book 3’s invariants file:

```
invariants/structural_detection.invariants.json
```

This file enforces the detection‑domain rules and kernel boundaries.

---

## Directory Structure
```text
AI_Edition/
  index.html
  README.md
  module.json

  kernel/
  operators/
  phases/
  maps/
  invariants/
  qmroot/
  examples/
  assets/
```

---

## Purpose
Book 3 provides the **structural detection domain layer** of RTT.  
Together with:

- **Book 1:** Frozen RTT kernel  
- **Book 2:** Inversion domain layer  

Book 3 completes the AI Edition trilogy of TriadicFrameworks.
