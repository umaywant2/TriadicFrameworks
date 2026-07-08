# **Structural Faultline Detector Examples — RTT/1**  
### *Example Dictionary for the Structural Faultline Detector (SFD)*

These examples illustrate how the **Structural Faultline Detector (SFD)** detects structural fractures, maps faultlines, identifies instability seams, evaluates faultline propagation, and computes structural stability envelopes across R1–R4.

Each example demonstrates one or more SFD operators:

- **SFD‑Detect**  
- **SFD‑Fracture**  
- **SFD‑Seam**  
- **SFD‑Field**  
- **SFD‑Propagate**  
- **SFD‑Stabilize**

Examples are grouped by faultline type.

---

## **1. Structural Fracture Examples**

### **Example 1 — Structural Invariant Fracture (R1 ↔ R2)**  
**Scenario**  
A conceptual invariant is violated by a computational structure, producing a structural fracture.

**SFD Output**  
```json
{
  "faultline_type": "structural-fracture",
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

### **Example 2 — Calibration‑Driven Structural Fracture (R2 ↔ R3)**  
**Scenario**  
A computational calibration mismatch produces a structural fracture across physical measurement.

**SFD Output**  
```json
{
  "faultline_type": "structural-fracture",
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

## **2. Gradient Faultline Examples**

### **Example 3 — Gradient Faultline Opposition (R1 ↔ R4)**  
**Scenario**  
Conceptual and dimensional gradients oppose each other, forming a gradient faultline.

**SFD Output**  
```json
{
  "faultline_type": "gradient",
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

### **Example 4 — Gradient Inversion Faultline (R2 ↔ R3)**  
**Scenario**  
Computational drift decreases while physical drift sensitivity increases, forming a gradient faultline.

**SFD Output**  
```json
{
  "faultline_type": "gradient",
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

## **3. Boundary Faultline Examples**

### **Example 5 — Abstraction‑Measurement Faultline (R1 ↔ R3)**  
**Scenario**  
Conceptual abstraction predicts behavior that contradicts physical measurement, forming a boundary faultline.

**SFD Output**  
```json
{
  "faultline_type": "boundary",
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

### **Example 6 — Gradient‑Boundary Faultline (R2 ↔ R4)**  
**Scenario**  
Aligned gradients across computational and dimensional regimes produce contradictory structural outcomes.

**SFD Output**  
```json
{
  "faultline_type": "boundary",
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

## **4. Faultline‑Field Examples**

### **Example 7 — Multi‑Regime Faultline Field (R1 ↔ R2 ↔ R3)**  
**Scenario**  
A multi‑regime faultline binds conceptual, computational, and physical structural fractures.

**SFD Output**  
```json
{
  "faultline_type": "field",
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

### **Example 8 — Dimensional Faultline Constraint (R2 ↔ R4)**  
**Scenario**  
Dimensional constraints influence computational structural pathways.

**SFD Output**  
```json
{
  "faultline_type": "field",
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

## **5. Drift‑Sensitive Faultline Examples**

### **Example 9 — Drift‑Amplified Faultline Basin (R3 ↔ R4)**  
**Scenario**  
Physical drift amplifies structural curvature, forming a drift‑sensitive faultline basin.

**SFD Output**  
```json
{
  "faultline_type": "drift-sensitive",
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

### **Example 10 — Drift‑Coherence Faultline Ridge (R2 ↔ R3)**  
**Scenario**  
Computational drift reduces coherence while physical drift increases coherence sensitivity, forming a drift‑coherence faultline ridge.

**SFD Output**  
```json
{
  "faultline_type": "drift-sensitive",
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

## **6. Canonical SFD Output Snippet**

```json
{
  "faultline_type": "gradient",
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
