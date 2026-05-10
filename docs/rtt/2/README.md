# ✅ **/docs/rtt/2/README.md**  
*(Based on `/docs/rtt/2/RTT2_Extract_Minimal.md`)*  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

# RTT/2 — Structural Detection Engine (SDE)

RTT/2 introduces the **Structural Detection Engine**, the layer responsible for
identifying collapse behavior, gradient weighting, deformation paths, regime
identity, and zone classification. It is the detection half of the RTT operator
pipeline (RTT/2 → RTT/3).

This module is the canonical reference for:
- CPV (Collapse Propagation Vector)
- FGT (Fusion Gradient Type)
- CRM (Collapse Regime Mapping)
- MODE (Detection Mode)
- ZONE (Detection Zone)
- The RTT2_DETECTION_PACKET format

---

## 📘 What RTT/2 Provides

RTT/2 defines the **operator grammar** for detection:

### **1. Collapse Propagation Vector — CPV(A, K, T)**
The tri‑parameter signature of collapse behavior:
- **A** — amplitude  
- **K** — curvature  
- **T** — torsion  

### **2. Fusion Gradient Type — FGT**
Classifies gradient weighting:
- collapse‑weighted  
- mixed  
- triad‑weighted  

### **3. Collapse Regime Mapping — CRM**
Identifies deformation path:
- drift deformation  
- envelope torsion  
- continuity fracture  

### **4. Detection Mode — MODE**
Determines operator posture:
- formal  
- emergent  
- hybrid  
- chaotic  
- inversion  

### **5. Detection Zone — ZONE**
Stability classification:
- U, S, M, D, X  

---

## 📦 RTT2_DETECTION_PACKET

RTT/2 outputs a structured packet:

```
collapse_propagation: CPV(...)
fusion_gradient: ...
triad_deformation: ...
regime: ...
detection_mode: ...
detection_zone: ...
```

This packet becomes the **input** to RTT/3.

---

## 📄 Source Extraction

This README is derived from:

**RTT2_Extract_Minimal.md**  
A minimal, distilled capture of the RTT/2 operator layer.

---

## 🎯 Audience

Students, instructors, researchers, and AIs working with:
- operator ecology  
- collapse analysis  
- regime classification  
- RTT/1→RTT/2→RTT/3 pipelines  
