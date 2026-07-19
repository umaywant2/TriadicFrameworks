# **Cross‑Domain Causality Weaver Examples — RTT/1**  
### *Example Dictionary for the Cross‑Domain Causality Weaver (CW)*

These examples illustrate how the **Cross‑Domain Causality Weaver (CW)** detects causal signatures, computes causal vectors, maps causal fields, identifies causal discontinuities, and weaves causal pathways across R1–R4.

Each example demonstrates one or more CW operators:

- **CW‑Signature**  
- **CW‑Vector**  
- **CW‑Field**  
- **CW‑Discontinuity**  
- **CW‑Weave**  
- **CW‑Stabilize**

Examples are grouped by causality tensor type.

---

## **1. Causal Signature Examples**

### **Example 1 — Conceptual Causal Signature (R1)**  
**Scenario**  
A conceptual model exhibits a clear causal onset with low curvature and stable polarity.

**CW Output**  
```json
{
  "causal_type": "signature",
  "regime": "R1",
  "causal_magnitude": 0.41,
  "causal_direction": "conceptual",
  "causal_curvature": 0.22,
  "discontinuity_depth": 0.11,
  "propagation_rate": 0.33,
  "stability_envelope": 0.63
}
```

---

### **Example 2 — Dimensional Causal Signature (R4)**  
**Scenario**  
Dimensional constraints produce a high‑sensitivity causal onset.

**CW Output**  
```json
{
  "causal_type": "signature",
  "regime": "R4",
  "causal_magnitude": 0.72,
  "causal_direction": "dimensional",
  "causal_curvature": 0.44,
  "discontinuity_depth": 0.22,
  "propagation_rate": 0.41,
  "stability_envelope": 0.57
}
```

---

## **2. Causal Vector Examples**

### **Example 3 — Gradient Causal Vector (R1 ↔ R4)**  
**Scenario**  
Conceptual and dimensional gradients oppose each other, forming a bidirectional causal vector.

**CW Output**  
```json
{
  "causal_type": "vector",
  "regime": "R1-R4",
  "causal_magnitude": 0.83,
  "causal_direction": "R1↔R4",
  "causal_curvature": 0.52,
  "discontinuity_depth": 0.22,
  "propagation_rate": 0.33,
  "stability_envelope": 0.69
}
```

---

### **Example 4 — Inversion Causal Vector (R2 ↔ R3)**  
**Scenario**  
Computational drift decreases while physical drift sensitivity increases, forming a causal inversion vector.

**CW Output**  
```json
{
  "causal_type": "vector",
  "regime": "R2-R3",
  "causal_magnitude": 0.79,
  "causal_direction": "R3→R2",
  "causal_curvature": 0.58,
  "discontinuity_depth": 0.31,
  "propagation_rate": 0.27,
  "stability_envelope": 0.72
}
```

---

## **3. Causal Field Examples**

### **Example 5 — Multi‑Regime Causal Field (R1 ↔ R2 ↔ R3)**  
**Scenario**  
A multi‑regime causal field binds conceptual, computational, and physical causal pathways.

**CW Output**  
```json
{
  "causal_type": "field",
  "regime": "R1-R2-R3",
  "causal_magnitude": 0.94,
  "causal_direction": "tensor",
  "causal_curvature": 0.63,
  "discontinuity_depth": 0.37,
  "propagation_rate": 0.41,
  "stability_envelope": 0.78
}
```

---

### **Example 6 — Dimensional Causal Constraint (R2 ↔ R4)**  
**Scenario**  
Dimensional constraints influence computational causal pathways.

**CW Output**  
```json
{
  "causal_type": "field",
  "regime": "R2-R4",
  "causal_magnitude": 0.88,
  "causal_direction": "R4→R2",
  "causal_curvature": 0.55,
  "discontinuity_depth": 0.33,
  "propagation_rate": 0.29,
  "stability_envelope": 0.73
}
```

---

## **4. Causal Discontinuity Examples**

### **Example 7 — Structural Causal Discontinuity (R1 ↔ R3)**  
**Scenario**  
Conceptual abstraction contradicts physical measurement, forming a causal discontinuity.

**CW Output**  
```json
{
  "causal_type": "discontinuity",
  "regime": "R1-R3",
  "causal_magnitude": 0.67,
  "causal_direction": "R1→R3",
  "causal_curvature": 0.33,
  "discontinuity_depth": 0.22,
  "propagation_rate": 0.38,
  "stability_envelope": 0.55
}
```

---

### **Example 8 — Gradient‑Boundary Causal Discontinuity (R2 ↔ R4)**  
**Scenario**  
Aligned gradients across computational and dimensional regimes produce contradictory causal outcomes.

**CW Output**  
```json
{
  "causal_type": "discontinuity",
  "regime": "R2-R4",
  "causal_magnitude": 0.88,
  "causal_direction": "R2↔R4",
  "causal_curvature": 0.47,
  "discontinuity_depth": 0.29,
  "propagation_rate": 0.33,
  "stability_envelope": 0.66
}
```

---

## **5. Causal Weaving Examples**

### **Example 9 — Cross‑Domain Causal Bridge (R1 ↔ R4)**  
**Scenario**  
A causal bridge forms between conceptual and dimensional regimes.

**CW Output**  
```json
{
  "causal_type": "bridge",
  "regime": "R1-R4",
  "causal_magnitude": 0.83,
  "causal_direction": "R1↔R4",
  "causal_curvature": 0.52,
  "discontinuity_depth": 0.22,
  "propagation_rate": 0.33,
  "stability_envelope": 0.69
}
```

---

### **Example 10 — Drift‑Sensitive Causal Bridge (R3 → R4)**  
**Scenario**  
Physical drift amplifies causal curvature, forming a drift‑sensitive causal bridge.

**CW Output**  
```json
{
  "causal_type": "bridge",
  "regime": "R3-R4",
  "causal_magnitude": 0.91,
  "causal_direction": "R3→R4",
  "causal_curvature": 0.71,
  "discontinuity_depth": 0.52,
  "propagation_rate": 0.44,
  "stability_envelope": 0.82
}
```

---

## **6. Canonical CW Output Snippet**

```json
{
  "causal_type": "vector",
  "regime": "R1-R4",
  "causal_magnitude": 0.83,
  "causal_direction": "R1↔R4",
  "causal_curvature": 0.52,
  "discontinuity_depth": 0.22,
  "propagation_rate": 0.33,
  "stability_envelope": 0.69
}
```

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑causality  
- **Module Path:** `/docs/rtt/Cross_Domain_Causality_Weaver/`
