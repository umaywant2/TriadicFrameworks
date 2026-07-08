# **Regime Interlock Examples — RTT/1**  
### *Examples for the Regime Interlock Mapper (RIM)*

This document provides **canonical RTT/1 examples** of regime interlocks detected and analyzed by the **Regime Interlock Mapper (RIM)**.  
Each example demonstrates one or more RIM operators:

- **RIM‑Detect**  
- **RIM‑Map**  
- **RIM‑Interlock**  
- **RIM‑Boundary**  
- **RIM‑Entangle**  
- **RIM‑Resolve**

Examples are grouped by interlock type.

---

## **1. Structural Interlock Examples**

### **Example 1 — Structural Constraint Pairing (R1 ↔ R2)**  
**Regimes:**  
- R1: Conceptual  
- R2: Computational  

**Interlock:**  
A conceptual invariant (e.g., “symmetry must be preserved”) forces a computational constraint (e.g., “algorithm must maintain parity across iterations”).

**RIM Output:**  
- `interlock_type`: structural  
- `interlock_strength`: 0.82  
- `boundary_condition`: symmetry‑preservation  
- `entanglement_score`: 0.41  

**Explanation:**  
The conceptual rule directly shapes the computational structure, forming a stable structural interlock.

---

### **Example 2 — Structural Dependency Chain (R2 ↔ R3)**  
**Regimes:**  
- R2: Computational  
- R3: Physical  

**Interlock:**  
A computational model requires physical calibration constants; the physical regime constrains the computational regime.

**RIM Output:**  
- `interlock_type`: structural  
- `interlock_strength`: 0.74  
- `boundary_condition`: calibration‑dependency  
- `entanglement_score`: 0.33  

---

## **2. Boundary Interlock Examples**

### **Example 3 — Boundary Transition (R1 ↔ R3)**  
**Regimes:**  
- R1: Conceptual  
- R3: Physical  

**Interlock:**  
A conceptual model transitions into a physical implementation at a defined boundary (e.g., “abstract force → measurable force”).

**RIM Output:**  
- `interlock_type`: boundary  
- `interlock_strength`: 0.67  
- `boundary_condition`: abstraction‑to‑measurement  
- `entanglement_score`: 0.22  

---

### **Example 4 — Boundary Gradient (R2 ↔ R4)**  
**Regimes:**  
- R2: Computational  
- R4: Dimensional  

**Interlock:**  
A computational gradient (e.g., increasing complexity) aligns with a dimensional gradient (e.g., increasing dimensional coherence).

**RIM Output:**  
- `interlock_type`: boundary  
- `interlock_strength`: 0.79  
- `boundary_condition`: gradient‑alignment  
- `entanglement_score`: 0.28  

---

## **3. Entanglement Interlock Examples**

### **Example 5 — Mutual Influence Loop (R1 ↔ R2)**  
**Regimes:**  
- R1: Conceptual  
- R2: Computational  

**Interlock:**  
Conceptual assumptions shape computational models, and computational outputs reshape conceptual assumptions.

**RIM Output:**  
- `interlock_type`: entanglement  
- `interlock_strength`: 0.91  
- `boundary_condition`: mutual‑feedback  
- `entanglement_score`: 0.88  

**Explanation:**  
This is a high‑entanglement interlock with bidirectional influence.

---

### **Example 6 — Cross‑Regime Entanglement (R3 ↔ R4)**  
**Regimes:**  
- R3: Physical  
- R4: Dimensional  

**Interlock:**  
Physical resonance patterns influence dimensional coherence, and dimensional coherence alters physical resonance.

**RIM Output:**  
- `interlock_type`: entanglement  
- `interlock_strength`: 0.93  
- `boundary_condition`: resonance‑coherence  
- `entanglement_score`: 0.91  

---

## **4. Gradient Interlock Examples**

### **Example 7 — Coherence Gradient (R1 ↔ R4)**  
**Regimes:**  
- R1: Conceptual  
- R4: Dimensional  

**Interlock:**  
A conceptual coherence gradient aligns with a dimensional coherence gradient.

**RIM Output:**  
- `interlock_type`: gradient  
- `interlock_strength`: 0.76  
- `boundary_condition`: coherence‑gradient  
- `entanglement_score`: 0.35  

---

### **Example 8 — Drift Gradient (R2 ↔ R3)**  
**Regimes:**  
- R2: Computational  
- R3: Physical  

**Interlock:**  
Computational drift increases physical drift sensitivity.

**RIM Output:**  
- `interlock_type`: gradient  
- `interlock_strength`: 0.81  
- `boundary_condition`: drift‑alignment  
- `entanglement_score`: 0.47  

---

## **5. Tensor Interlock Examples**

### **Example 9 — Coherence Tensor Interlock (R1 ↔ R2 ↔ R3)**  
**Regimes:**  
- R1: Conceptual  
- R2: Computational  
- R3: Physical  

**Interlock:**  
A multi‑regime coherence tensor binds conceptual, computational, and physical coherence.

**RIM Output:**  
- `interlock_type`: tensor  
- `interlock_strength`: 0.94  
- `boundary_condition`: coherence‑tensor  
- `entanglement_score`: 0.89  

---

### **Example 10 — Dimensional Tensor Interlock (R2 ↔ R4)**  
**Regimes:**  
- R2: Computational  
- R4: Dimensional  

**Interlock:**  
Dimensional tensors constrain computational pathways.

**RIM Output:**  
- `interlock_type`: tensor  
- `interlock_strength`: 0.88  
- `boundary_condition`: dimensional‑tensor  
- `entanglement_score`: 0.72  

---

## **6. Example Matrix Snippet**

A typical entry in `regime_interlock_matrix.json`:

```json
{
  "regime_a": "R2",
  "regime_b": "R3",
  "interlock_type": "gradient",
  "interlock_strength": 0.81,
  "boundary_condition": "drift-alignment",
  "entanglement_score": 0.47,
  "stability_rating": 0.63
}
```

---

## **7. Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑structural  
- **Module Path:** `/docs/rtt/Regime_Interlock_Mapper/`
