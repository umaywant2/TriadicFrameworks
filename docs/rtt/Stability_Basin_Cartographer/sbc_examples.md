# **Stability Basin Cartographer Examples — RTT/1**  
### *Example Dictionary for the Stability Basin Cartographer (SBC)*

These examples illustrate how the **Stability Basin Cartographer (SBC)** maps stability basins, computes basin gradients, identifies stability fields, detects collapse zones, and evaluates stability topology across R1–R4.

Each example demonstrates one or more SBC operators:

- **SBC‑Map**  
- **SBC‑Basin**  
- **SBC‑Gradient**  
- **SBC‑Field**  
- **SBC‑Collapse**  
- **SBC‑Stabilize**

Examples are grouped by basin type.

---

## **1. Stability Basin Examples**

### **Example 1 — Conceptual Stability Basin (R1)**  
**Scenario**  
A conceptual model exhibits a stable region with low curvature and shallow collapse potential.

**SBC Output**  
```json
{
  "basin_type": "stability",
  "regime": "R1",
  "basin_magnitude": 0.41,
  "basin_direction": "conceptual",
  "basin_curvature": 0.22,
  "collapse_zone": 0.11,
  "stability_field": 0.63,
  "envelope_boundary": 0.44
}
```

---

### **Example 2 — Computational Stability Basin (R2)**  
**Scenario**  
A computational structure forms a stability basin with moderate curvature and medium collapse sensitivity.

**SBC Output**  
```json
{
  "basin_type": "stability",
  "regime": "R2",
  "basin_magnitude": 0.52,
  "basin_direction": "computational",
  "basin_curvature": 0.33,
  "collapse_zone": 0.27,
  "stability_field": 0.57,
  "envelope_boundary": 0.41
}
```

---

## **2. Gradient Basin Examples**

### **Example 3 — Gradient Basin Opposition (R1 ↔ R4)**  
**Scenario**  
Conceptual and dimensional gradients oppose each other, forming a gradient basin with high curvature.

**SBC Output**  
```json
{
  "basin_type": "gradient",
  "regime": "R1-R4",
  "basin_magnitude": 0.83,
  "basin_direction": "R1↔R4",
  "basin_curvature": 0.51,
  "collapse_zone": 0.22,
  "stability_field": 0.69,
  "envelope_boundary": 0.46
}
```

---

### **Example 4 — Gradient Inversion Basin (R2 ↔ R3)**  
**Scenario**  
Computational stability decreases while physical stability increases, forming a gradient inversion basin.

**SBC Output**  
```json
{
  "basin_type": "gradient",
  "regime": "R2-R3",
  "basin_magnitude": 0.79,
  "basin_direction": "R3→R2",
  "basin_curvature": 0.58,
  "collapse_zone": 0.31,
  "stability_field": 0.72,
  "envelope_boundary": 0.41
}
```

---

## **3. Boundary Basin Examples**

### **Example 5 — Abstraction‑Measurement Stability Basin (R1 ↔ R3)**  
**Scenario**  
Conceptual abstraction predicts behavior that contradicts physical measurement, forming a boundary stability basin.

**SBC Output**  
```json
{
  "basin_type": "boundary",
  "regime": "R1-R3",
  "basin_magnitude": 0.67,
  "basin_direction": "R1→R3",
  "basin_curvature": 0.33,
  "collapse_zone": 0.22,
  "stability_field": 0.55,
  "envelope_boundary": 0.38
}
```

---

### **Example 6 — Gradient‑Boundary Stability Basin (R2 ↔ R4)**  
**Scenario**  
Aligned gradients across computational and dimensional regimes produce contradictory stability outcomes.

**SBC Output**  
```json
{
  "basin_type": "boundary",
  "regime": "R2-R4",
  "basin_magnitude": 0.88,
  "basin_direction": "R2↔R4",
  "basin_curvature": 0.47,
  "collapse_zone": 0.29,
  "stability_field": 0.66,
  "envelope_boundary": 0.58
}
```

---

## **4. Stability‑Field Examples**

### **Example 7 — Multi‑Regime Stability Field (R1 ↔ R2 ↔ R3)**  
**Scenario**  
A multi‑regime stability field binds conceptual, computational, and physical stability basins.

**SBC Output**  
```json
{
  "basin_type": "field",
  "regime": "R1-R2-R3",
  "basin_magnitude": 0.94,
  "basin_direction": "tensor",
  "basin_curvature": 0.63,
  "collapse_zone": 0.37,
  "stability_field": 0.78,
  "envelope_boundary": 0.57
}
```

---

### **Example 8 — Dimensional Stability Constraint (R2 ↔ R4)**  
**Scenario**  
Dimensional constraints influence computational stability pathways.

**SBC Output**  
```json
{
  "basin_type": "field",
  "regime": "R2-R4",
  "basin_magnitude": 0.88,
  "basin_direction": "R4→R2",
  "basin_curvature": 0.55,
  "collapse_zone": 0.33,
  "stability_field": 0.73,
  "envelope_boundary": 0.63
}
```

---

## **5. Collapse‑Zone Examples**

### **Example 9 — Stability Collapse Basin (R3 → R4)**  
**Scenario**  
Physical stability collapses into dimensional instability, forming a collapse basin.

**SBC Output**  
```json
{
  "basin_type": "collapse",
  "regime": "R3-R4",
  "basin_magnitude": 0.91,
  "basin_direction": "R3→R4",
  "basin_curvature": 0.71,
  "collapse_zone": 0.52,
  "stability_field": 0.82,
  "envelope_boundary": 0.44
}
```

---

### **Example 10 — Stability‑Coherence Collapse Ridge (R2 ↔ R3)**  
**Scenario**  
Computational stability reduces coherence while physical stability increases coherence sensitivity, forming a collapse ridge.

**SBC Output**  
```json
{
  "basin_type": "collapse",
  "regime": "R2-R3",
  "basin_magnitude": 0.86,
  "basin_direction": "R2↔R3",
  "basin_curvature": 0.62,
  "collapse_zone": 0.49,
  "stability_field": 0.77,
  "envelope_boundary": 0.48
}
```

---

## **6. Canonical SBC Output Snippet**

```json
{
  "basin_type": "gradient",
  "regime": "R1-R4",
  "basin_magnitude": 0.83,
  "basin_direction": "R1↔R4",
  "basin_curvature": 0.51,
  "collapse_zone": 0.22,
  "stability_field": 0.69,
  "envelope_boundary": 0.46
}
```

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑stability  
- **Module Path:** `/docs/rtt/Stability_Basin_Cartographer/`
