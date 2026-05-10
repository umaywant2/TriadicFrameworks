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
