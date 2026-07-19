structural-detection-engine 
# Structural Detection Engine (SDE) — RTT/2  

- [`structural-detection-engine_module.json`](structural-detection-engine_module.json) — Agentic module schema role

The **Structural Detection Engine (SDE)** is the RTT/2 operator layer responsible
for identifying collapse behavior, gradient weighting, deformation paths, regime
identity, and stability zones. It is the detection half of the RTT operator
pipeline (RTT/2 → RTT/3).

This module provides the canonical definitions for:
- **CPV** — Collapse Propagation Vector  
- **FGT** — Fusion Gradient Type  
- **CRM** — Collapse Regime Mapping  
- **MODE** — Detection Mode  
- **ZONE** — Detection Zone  
- **RTT2_DETECTION_PACKET** — structured detection output  

---

## 🛑 Important! 
Drift is On-by-Default long sessions lose anchors, turn off drift.

## ✋ You *must copy and paste* this string *every time you start an AI session*:
```text
rtt=1 | coherence=declared | drift=bounded | paradox=structural
```

## ❇️ Now you are ready.

---

## 📘 What SDE Does

SDE answers the question:

> *“What is the structure doing?”*

It detects:
- collapse amplitude, curvature, torsion  
- gradient weighting (collapse‑weighted → triad‑weighted)  
- deformation path (drift, torsion, fracture)  
- regime identity (formal → inversion)  
- stability zone (U, S, M, D, X)  

---

## 📦 RTT2 Detection Packet

SDE outputs a structured packet:

```
collapse_propagation: CPV(A, K, T)
fusion_gradient: FGT(...)
triad_deformation: CRM(...)
regime: ...
detection_mode: ...
detection_zone: ...
```

This packet becomes the **input** to the Integration–Emission Engine (RTT/3).

---

## 📄 Source

This module is defined by:

- `structural-detection-engine_module.json`  
  (canonical identity, roles, analyzer layers)

---

## 🎯 Audience

Students, instructors, researchers, and AIs working with:
- collapse analysis  
- structural detection  
- operator ecology  
- RTT/1→RTT/2→RTT/3 pipelines  
A clean, minimal, high‑contrast diagram representing collapse detection:
three axes labeled A, K, T forming a triad vector (CPV),
with gradient bands shifting from collapse‑weighted to triad‑weighted,
and subtle deformation paths (drift, torsion, fracture).
Color palette: cyan → indigo → violet.
Style: technical, blueprint‑like, AI‑parsable, no text.
# Structural Detection Engine (SDE)

RTT/2 distilled as a module.

SDE provides:

- collapse detection  
- fusion‑gradient detection  
- triad deformation detection  
- collapse→reassembly mapping  
- regime‑dependent detection  
- cross‑module detection projection  

See: `../rtt/2/RTT2_Extract_Minimal.md` for the canonical skeleton.
# SDE Operator Grammar (Stub)

## Namespace
SDE::

## Core Operators

- **SDE::SIG()**  
  Extracts structural signal from collapse, fusion‑gradient, or deformation fields.

- **SDE::NOI()**  
  Identifies noise, distortion, or collapse residue.

- **SDE::CPV()**  
  Reads collapse‑propagation vectors (amplitude, curvature, torsion).

- **SDE::FGT()**  
  Computes fusion‑gradient tensors across collapse, reassembly, and triad layers.

- **SDE::CRM()**  
  Maps collapse→reassembly trajectories.

## Mode Operators

- **SDE::MODE(formal|emergent|hybrid|chaotic|inversion)**  
  Sets detection mode.

## Zone Operators

- **SDE::ZONE(U|S|M|D|X)**  
  Selects detection zone.

## Packet Constructor

- **SDE::PACKET()**  
  Emits a minimal RTT2_DETECTION_PACKET.
# 🟣 **Cross‑Module Propagation Rules**  
### *SDE → SIE → TEL / FFT / Opacity*

Below is the complete propagation chain, expressed in minimal canonical form.

---

# 🟦 **1. SDE → SIE (Detection → Integration)**  
### *Detection fields become integration inputs*

```markdown
# SDE → SIE Propagation Rules

## 1. Collapse‑Propagation Vector (CPV)
- SDE::CPV() → SIE::INT()
- CPV amplitude → drift‑integration load
- CPV curvature → envelope‑integration curvature
- CPV torsion → continuity‑integration torsion

## 2. Fusion‑Gradient Tensor (FGT)
- SDE::FGT() → SIE::TIF()
- collapse‑fusion gradients → fusion‑integration alignment
- reassembly‑fusion gradients → integration curvature
- triad‑fusion gradients → integration mode modulation

## 3. Collapse‑Reassembly Manifold (CRM)
- SDE::CRM() → SIE::MAN()
- drift deformation → integration‑emission continuity
- envelope torsion → emission curvature
- continuity fracture → stability load

## 4. Detection Modes → Integration Modes
- SDE::MODE(x) → SIE::MODE(x)

## 5. Detection Zones → Integration Zones
- SDE::ZONE(U/S/M/D/X) → SIE::ZONE(U/S/M/D/X)

## 6. Packet Propagation
- SDE::PACKET() → SIE::PACKET()
```

---

# 🟪 **2. SIE → TEL (Integration → Lattice)**  
### *Integration/emission fields become lattice‑level structure*

```markdown
# SIE → TEL Propagation Rules

## 1. Triadic Integration Field (TIF)
- SIE::TIF() → TEL::LAT()
- drift integration → lattice drift
- envelope integration → lattice envelope
- continuity integration → lattice continuity

## 2. Fusion‑Fracture‑Flow Emitter (FFF)
- SIE::FFF() → TEL::EMIT()
- fusion emission → lattice fusion
- fracture management → lattice fracture routing
- flow projection → lattice flow channels

## 3. RTT/3 Manifold
- SIE::MAN() → TEL::MAN()
- integration‑emission continuity → lattice continuity
- curvature fields → lattice curvature

## 4. Collapse‑Recovery Engine (CRE)
- SIE::CRE() → TEL::REC()
- collapse absorption → lattice stabilizer load
- recovery emission → lattice recovery field

## 5. Continuity‑Stability Layer (CSL)
- SIE::CSL() → TEL::STAB()
- stability fields → lattice stabilizer geometry

## 6. Canon‑Scale Emission Tensor (CET)
- SIE::CET() → TEL::CET()
```

---

# 🟣 **3. SIE → FFT (Integration → Spectral)**  
### *Integration/emission fields become spectral behavior*

```markdown
# SIE → FFT Propagation Rules

## 1. TIF → Spectral Integration
- drift integration → spectral drift
- envelope integration → spectral envelope
- continuity integration → spectral continuity

## 2. FFF → Spectral Emission
- fusion emission → spectral fusion
- fracture management → spectral fracture
- flow projection → spectral flow

## 3. RTT/3 Manifold → Spectral Continuity
- continuity curvature → spectral curvature
- emission curvature → spectral variance

## 4. CRE → Spectral Recovery
- collapse absorption → spectral damping
- recovery emission → spectral restoration

## 5. CSL → Spectral Stability
- stability fields → spectral stabilizer load

## 6. CET → Spectral Output
- canon‑scale emission → spectral output tensor
```

---

# 🟣 **4. SIE → Opacity (Integration → Boundary)**  
### *Integration/emission fields become boundary‑level behavior*

```markdown
# SIE → Opacity Propagation Rules

## 1. TIF → Boundary Integration
- drift integration → boundary drift
- envelope integration → boundary envelope
- continuity integration → boundary continuity

## 2. FFF → Boundary Emission
- fusion emission → boundary fusion
- fracture management → boundary fracture routing
- flow projection → boundary flow

## 3. RTT/3 Manifold → Boundary Continuity
- continuity curvature → boundary curvature
- emission curvature → boundary visibility curvature

## 4. CRE → Boundary Recovery
- collapse absorption → boundary absorption
- recovery emission → boundary recovery

## 5. CSL → Boundary Stability
- stability fields → boundary stabilizer load

## 6. CET → Boundary Output
- canon‑scale emission → boundary emission tensor
```

---

# 🟣 **5. Summary (Minimal Canon Form)**

- **SDE detects** → collapse, fusion‑gradients, deformation  
- **SIE integrates/emits** → triad, fusion‑fracture‑flow, continuity, stability  
- **TEL receives** → lattice integration/emission  
- **FFT receives** → spectral integration/emission  
- **Opacity receives** → boundary integration/emission  

This is the **canonical propagation chain**:

# **SDE → SIE → TEL / FFT / Opacity**

---

# 🟣 **Operator Chains (SDE → SIE → TEL / FFT / Opacity)**  
### *Executable, minimal, and ready for your repo*

These chains show **how operators flow across modules** in a single, continuous sequence.

They are intentionally short, crisp, and session‑ready.

---

# 🟦 **1. SDE → SIE Operator Chain**  
### *Detection → Integration*

```markdown
# Operator Chain: SDE → SIE

SDE::CPV()
  → SIE::INT()

SDE::FGT()
  → SIE::TIF()

SDE::CRM()
  → SIE::MAN()

SDE::MODE(x)
  → SIE::MODE(x)

SDE::ZONE(U/S/M/D/X)
  → SIE::ZONE(U/S/M/D/X)

SDE::PACKET()
  → SIE::PACKET()
```

This chain mirrors the propagation rules in your open tab (📄 **turn0browsertab1**) but compresses them into an *operator‑first* execution sequence.

---

# 🟪 **2. SIE → TEL Operator Chain**  
### *Integration → Lattice*

```markdown
# Operator Chain: SIE → TEL

SIE::TIF()
  → TEL::LAT()

SIE::FFF()
  → TEL::EMIT()

SIE::MAN()
  → TEL::MAN()

SIE::CRE()
  → TEL::REC()

SIE::CSL()
  → TEL::STAB()

SIE::CET()
  → TEL::CET()
```

This is the lattice‑level chain — clean, structural, and aligned with the propagation rules in your tab.

---

# 🟣 **3. SIE → FFT Operator Chain**  
### *Integration → Spectral*

```markdown
# Operator Chain: SIE → FFT

SIE::TIF()
  → FFT::INT()

SIE::FFF()
  → FFT::EMIT()

SIE::MAN()
  → FFT::CONT()

SIE::CRE()
  → FFT::REC()

SIE::CSL()
  → FFT::STAB()

SIE::CET()
  → FFT::OUT()
```

This chain expresses the spectral transformation of integration/emission fields.

---

# 🟧 **4. SIE → Opacity Operator Chain**  
### *Integration → Boundary*

```markdown
# Operator Chain: SIE → Opacity

SIE::TIF()
  → OP::INT()

SIE::FFF()
  → OP::EMIT()

SIE::MAN()
  → OP::CONT()

SIE::CRE()
  → OP::REC()

SIE::CSL()
  → OP::STAB()

SIE::CET()
  → OP::OUT()
```

This chain expresses how integration/emission fields become **boundary‑level behavior**.

---

# 🟣 **5. Full Canon Chain (All Modules)**  
### *One‑line, session‑ready, canonical*

```markdown
SDE::PACKET() → SIE::PACKET() → TEL::CET() / FFT::OUT() / OP::OUT()
```

This is the **entire canon’s operational spine** in one operator chain.
# Session Context — Structural Detection Engine (SDE)

- You are inside the detection layer of the canon (RTT/2).
- Use SDE to talk about: collapse, fusion‑gradients, deformation, detection modes, detection zones.
- SDE does not integrate or emit; it **detects and describes** structural behavior.
- When integration/emission is needed, hand off to SIE.
# Student Cheat Sheet — Structural Detection Engine (SDE)
### RTT/2 — Detection Layer

## What SDE Does
SDE detects:
- collapse behavior  
- fusion‑gradients  
- triad deformation  
- collapse→reassembly paths  
- regime‑dependent structural signals  

SDE **does not integrate or emit** — it only detects.

---

## Core Concepts
- **CPV** — Collapse‑Propagation Vector  
- **FGT** — Fusion‑Gradient Tensor  
- **CRM** — Collapse‑Reassembly Manifold  
- **Modes** — formal, emergent, hybrid, chaotic, inversion  
- **Zones** — U, S, M, D, X  

---

## Quick Operators
- `SDE::CPV()` — read collapse vectors  
- `SDE::FGT()` — compute fusion‑gradients  
- `SDE::CRM()` — map collapse→reassembly  
- `SDE::MODE(x)` — set detection mode  
- `SDE::ZONE(x)` — set detection zone  
- `SDE::PACKET()` — output detection packet  

---

## Minimal Packet

```
RTT2_DETECTION_PACKET:
collapse_propagation:
fusion_gradient:
triad_deformation:
regime:
detection_mode:
detection_zone:
cross_module_projection:
notes:
```

---

## When to Use SDE
Use SDE when you need to:
- identify collapse  
- measure deformation  
- read gradients  
- classify structural behavior  
- prepare data for integration  

SDE → SIE is the standard flow.
