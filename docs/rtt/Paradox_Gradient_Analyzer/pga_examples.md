# **Paradox Gradient Examples — RTT/1**  
### *Example Dictionary for the Paradox Gradient Analyzer (PGA)*

These examples illustrate how the **Paradox Gradient Analyzer (PGA)** detects, computes, and maps paradox gradients across conceptual, computational, physical, and dimensional regimes.

Each example demonstrates one or more PGA operators:

- **PGA‑Detect**  
- **PGA‑Gradient**  
- **PGA‑Intensity**  
- **PGA‑Source**  
- **PGA‑Field**  
- **PGA‑Resolve**

Examples are grouped by paradox type.

---

## **1. Structural Paradox Examples**

### **Example 1 — Structural Constraint Contradiction (R1 ↔ R2)**  
**Paradox:**  
A conceptual invariant (“symmetry must be preserved”) conflicts with a computational algorithm that introduces asymmetry during iteration.

**PGA Output:**  
```json
{
  "paradox_source": "symmetry-violation",
  "regime": "R1-R2",
  "gradient_magnitude": 0.72,
  "gradient_direction": "R1→R2",
  "intensity": 0.81,
  "field_curvature": 0.44,
  "basin_depth": 0.63,
  "stability_rating": 0.52
}
```

---

### **Example 2 — Structural Calibration Paradox (R2 ↔ R3)**  
**Paradox:**  
A computational model requires calibration constants that contradict physical measurements.

**PGA Output:**  
```json
{
  "paradox_source": "calibration-contradiction",
  "regime": "R2-R3",
  "gradient_magnitude": 0.68,
  "gradient_direction": "R3→R2",
  "intensity": 0.74,
  "field_curvature": 0.39,
  "basin_depth": 0.57,
  "stability_rating": 0.49
}
```

---

## **2. Gradient Paradox Examples**

### **Example 3 — Opposing Coherence Gradients (R1 ↔ R4)**  
**Paradox:**  
Conceptual coherence increases while dimensional coherence decreases.

**PGA Output:**  
```json
{
  "paradox_source": "coherence-gradient-opposition",
  "regime": "R1-R4",
  "gradient_magnitude": 0.83,
  "gradient_direction": "R1↔R4",
  "intensity": 0.77,
  "field_curvature": 0.51,
  "basin_depth": 0.69,
  "stability_rating": 0.46
}
```

---

### **Example 4 — Drift Gradient Inversion (R2 ↔ R3)**  
**Paradox:**  
Computational drift decreases while physical drift sensitivity increases.

**PGA Output:**  
```json
{
  "paradox_source": "drift-gradient-inversion",
  "regime": "R2-R3",
  "gradient_magnitude": 0.79,
  "gradient_direction": "R3→R2",
  "intensity": 0.82,
  "field_curvature": 0.58,
  "basin_depth": 0.72,
  "stability_rating": 0.41
}
```

---

## **3. Boundary Paradox Examples**

### **Example 5 — Abstraction‑Measurement Paradox (R1 ↔ R3)**  
**Paradox:**  
An abstract conceptual model predicts behavior that contradicts physical measurement.

**PGA Output:**  
```json
{
  "paradox_source": "abstraction-measurement",
  "regime": "R1-R3",
  "gradient_magnitude": 0.67,
  "gradient_direction": "R1→R3",
  "intensity": 0.71,
  "field_curvature": 0.33,
  "basin_depth": 0.55,
  "stability_rating": 0.62
}
```

---

### **Example 6 — Gradient‑Boundary Paradox (R2 ↔ R4)**  
**Paradox:**  
A computational gradient aligns with a dimensional gradient but produces contradictory outcomes.

**PGA Output:**  
```json
{
  "paradox_source": "gradient-boundary",
  "regime": "R2-R4",
  "gradient_magnitude": 0.88,
  "gradient_direction": "R2↔R4",
  "intensity": 0.79,
  "field_curvature": 0.47,
  "basin_depth": 0.66,
  "stability_rating": 0.58
}
```

---

## **4. Tensor Paradox Examples**

### **Example 7 — Coherence Tensor Paradox (R1 ↔ R2 ↔ R3)**  
**Paradox:**  
A multi‑regime coherence tensor binds conceptual, computational, and physical coherence, but one regime violates tensor constraints.

**PGA Output:**  
```json
{
  "paradox_source": "coherence-tensor",
  "regime": "R1-R2-R3",
  "gradient_magnitude": 0.94,
  "gradient_direction": "tensor",
  "intensity": 0.91,
  "field_curvature": 0.63,
  "basin_depth": 0.78,
  "stability_rating": 0.57
}
```

---

### **Example 8 — Dimensional Tensor Paradox (R2 ↔ R4)**  
**Paradox:**  
Dimensional tensors constrain computational pathways, but computational coherence violates tensor alignment.

**PGA Output:**  
```json
{
  "paradox_source": "dimensional-tensor",
  "regime": "R2-R4",
  "gradient_magnitude": 0.88,
  "gradient_direction": "R4→R2",
  "intensity": 0.84,
  "field_curvature": 0.55,
  "basin_depth": 0.73,
  "stability_rating": 0.63
}
```

---

## **5. Drift‑Induced Paradox Examples**

### **Example 9 — Drift Amplification Paradox (R3 ↔ R4)**  
**Paradox:**  
Physical drift amplifies dimensional drift curvature, creating a paradox basin.

**PGA Output:**  
```json
{
  "paradox_source": "drift-amplification",
  "regime": "R3-R4",
  "gradient_magnitude": 0.91,
  "gradient_direction": "R3→R4",
  "intensity": 0.89,
  "field_curvature": 0.71,
  "basin_depth": 0.82,
  "stability_rating": 0.44
}
```

---

### **Example 10 — Drift‑Coherence Paradox (R2 ↔ R3)**  
**Paradox:**  
Computational drift reduces coherence while physical drift increases coherence sensitivity.

**PGA Output:**  
```json
{
  "paradox_source": "drift-coherence",
  "regime": "R2-R3",
  "gradient_magnitude": 0.86,
  "gradient_direction": "R2↔R3",
  "intensity": 0.83,
  "field_curvature": 0.62,
  "basin_depth": 0.77,
  "stability_rating": 0.48
}
```

---

## **6. Example Matrix Snippet**

```json
{
  "paradox_source": "coherence-gradient-opposition",
  "regime": "R1-R4",
  "gradient_magnitude": 0.83,
  "gradient_direction": "R1↔R4",
  "intensity": 0.77,
  "field_curvature": 0.51,
  "basin_depth": 0.69,
  "stability_rating": 0.46
}
```

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑structural  
- **Module Path:** `/docs/rtt/Paradox_Gradient_Analyzer/`
