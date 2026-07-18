# **Fracture Cases — RTT/1**  
### *Case Studies for the Structural Faultline Detector (SFD)*

Structural fractures represent **breaks, discontinuities, instability seams, and propagation pathways** across conceptual, computational, physical, and dimensional regimes.  
These case studies illustrate how the Structural Faultline Detector (SFD) evaluates:

- fracture magnitude  
- fracture direction  
- faultline curvature  
- propagation rate  
- instability seam depth  
- stability envelope  
- collapse‑point formation  

Each case demonstrates one or more SFD operators:

- **SFD‑Detect**  
- **SFD‑Fracture**  
- **SFD‑Seam**  
- **SFD‑Field**  
- **SFD‑Propagate**  
- **SFD‑Stabilize**

---

## **1. Structural Fracture Cases**

### **Case 1 — Structural Invariant Fracture (R1 → R2)**  
**Scenario**  
A conceptual invariant is violated by a computational structure, producing a structural fracture.

**SFD Output**  
```json
{
  "regime": "R1-R2",
  "fracture_magnitude": 0.72,
  "fracture_direction": "R1→R2",
  "faultline_curvature": 0.33,
  "propagation_rate": 0.22,
  "instability_seam": 0.41,
  "stability_envelope": 0.63
}
```

---

### **Case 2 — Calibration‑Mismatch Fracture (R2 → R3)**  
**Scenario**  
A computational calibration mismatch produces a structural fracture across physical measurement.

**SFD Output**  
```json
{
  "regime": "R2-R3",
  "fracture_magnitude": 0.68,
  "fracture_direction": "R3→R2",
  "faultline_curvature": 0.39,
  "propagation_rate": 0.27,
  "instability_seam": 0.38,
  "stability_envelope": 0.57
}
```

---

## **2. Gradient Fracture Cases**

### **Case 3 — Gradient Fracture Opposition (R1 ↔ R4)**  
**Scenario**  
Conceptual and dimensional gradients oppose each other, forming a gradient fracture.

**SFD Output**  
```json
{
  "regime": "R1-R4",
  "fracture_magnitude": 0.83,
  "fracture_direction": "R1↔R4",
  "faultline_curvature": 0.52,
  "propagation_rate": 0.33,
  "instability_seam": 0.47,
  "stability_envelope": 0.69
}
```

---

### **Case 4 — Gradient Inversion Fracture (R2 ↔ R3)**  
**Scenario**  
Computational drift decreases while physical drift sensitivity increases, forming a gradient fracture.

**SFD Output**  
```json
{
  "regime": "R2-R3",
  "fracture_magnitude": 0.79,
  "fracture_direction": "R3→R2",
  "faultline_curvature": 0.58,
  "propagation_rate": 0.31,
  "instability_seam": 0.44,
  "stability_envelope": 0.72
}
```

---

## **3. Boundary Fracture Cases**

### **Case 5 — Abstraction‑Measurement Fracture (R1 → R3)**  
**Scenario**  
Conceptual abstraction predicts behavior that contradicts physical measurement, forming a boundary fracture.

**SFD Output**  
```json
{
  "regime": "R1-R3",
  "fracture_magnitude": 0.67,
  "fracture_direction": "R1→R3",
  "faultline_curvature": 0.33,
  "propagation_rate": 0.22,
  "instability_seam": 0.38,
  "stability_envelope": 0.55
}
```

---

### **Case 6 — Gradient‑Boundary Fracture (R2 ↔ R4)**  
**Scenario**  
Aligned gradients across computational and dimensional regimes produce contradictory structural outcomes.

**SFD Output**  
```json
{
  "regime": "R2-R4",
  "fracture_magnitude": 0.88,
  "fracture_direction": "R2↔R4",
  "faultline_curvature": 0.47,
  "propagation_rate": 0.29,
  "instability_seam": 0.58,
  "stability_envelope": 0.66
}
```

---

## **4. Faultline‑Field Fracture Cases**

### **Case 7 — Multi‑Regime Fracture Field (R1 ↔ R2 ↔ R3)**  
**Scenario**  
A multi‑regime fracture binds conceptual, computational, and physical structural pathways.

**SFD Output**  
```json
{
  "regime": "R1-R2-R3",
  "fracture_magnitude": 0.94,
  "fracture_direction": "tensor",
  "faultline_curvature": 0.63,
  "propagation_rate": 0.37,
  "instability_seam": 0.57,
  "stability_envelope": 0.78
}
```

---

### **Case 8 — Dimensional Fracture Constraint (R2 ↔ R4)**  
**Scenario**  
Dimensional constraints influence computational structural pathways.

**SFD Output**  
```json
{
  "regime": "R2-R4",
  "fracture_magnitude": 0.88,
  "fracture_direction": "R4→R2",
  "faultline_curvature": 0.55,
  "propagation_rate": 0.33,
  "instability_seam": 0.63,
  "stability_envelope": 0.73
}
```

---

## **5. Drift‑Sensitive Fracture Cases**

### **Case 9 — Drift‑Amplified Fracture Basin (R3 → R4)**  
**Scenario**  
Physical drift amplifies structural curvature, forming a drift‑sensitive fracture basin.

**SFD Output**  
```json
{
  "regime": "R3-R4",
  "fracture_magnitude": 0.91,
  "fracture_direction": "R3→R4",
  "faultline_curvature": 0.71,
  "propagation_rate": 0.52,
  "instability_seam": 0.44,
  "stability_envelope": 0.82
}
```

---

### **Case 10 — Drift‑Coherence Fracture Ridge (R2 ↔ R3)**  
**Scenario**  
Computational drift reduces coherence while physical drift increases coherence sensitivity, forming a drift‑coherence fracture ridge.

**SFD Output**  
```json
{
  "regime": "R2-R3",
  "fracture_magnitude": 0.86,
  "fracture_direction": "R2↔R3",
  "faultline_curvature": 0.62,
  "propagation_rate": 0.49,
  "instability_seam": 0.48,
  "stability_envelope": 0.77
}
```

---

## **6. Canonical SFD Fracture Snippet**

```json
{
  "regime": "R1-R4",
  "fracture_magnitude": 0.83,
  "fracture_direction": "R1↔R4",
  "faultline_curvature": 0.52,
  "propagation_rate": 0.33,
  "instability_seam": 0.47,
  "stability_envelope": 0.69
}
```

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑structural  
- **Module Path:** `/docs/rtt/Structural_Faultline_Detector/`
