# **Temporal Regime Sequencer Examples — RTT/1**  
### *Example Dictionary for the Temporal Regime Sequencer (TRS‑Temporal)*

These examples illustrate how the **Temporal Regime Sequencer (TRS‑Temporal)** detects temporal signatures, computes temporal gradients, maps temporal fields, identifies instability zones, and sequences regime transitions.

Each example demonstrates one or more TRS‑Temporal operators:

- **TRS‑Seq**  
- **TRS‑Gradient**  
- **TRS‑Field**  
- **TRS‑Instability**  
- **TRS‑Transition**  
- **TRS‑Stabilize**

Examples are grouped by temporal tensor type.

---

## **1. Temporal Signature Examples**

### **Example 1 — Conceptual Temporal Signature (R1)**  
**Scenario**  
A conceptual model exhibits a low‑curvature temporal onset with stable polarity.

**TRS Output**  
```json
{
  "temporal_type": "signature",
  "regime": "R1",
  "temporal_magnitude": 0.41,
  "temporal_direction": "conceptual",
  "temporal_curvature": 0.22,
  "instability_depth": 0.11,
  "temporal_field": 0.63,
  "transition_boundary": 0.44
}
```

---

### **Example 2 — Dimensional Temporal Signature (R4)**  
**Scenario**  
Dimensional constraints produce a high‑sensitivity temporal onset.

**TRS Output**  
```json
{
  "temporal_type": "signature",
  "regime": "R4",
  "temporal_magnitude": 0.72,
  "temporal_direction": "dimensional",
  "temporal_curvature": 0.44,
  "instability_depth": 0.22,
  "temporal_field": 0.57,
  "transition_boundary": 0.41
}
```

---

## **2. Temporal Gradient Examples**

### **Example 3 — Harmonic Temporal Gradient (R2)**  
**Scenario**  
A computational structure exhibits a stable temporal gradient with low drift sensitivity.

**TRS Output**  
```json
{
  "temporal_type": "gradient",
  "regime": "R2",
  "temporal_magnitude": 0.52,
  "temporal_direction": "computational",
  "temporal_curvature": 0.33,
  "instability_depth": 0.27,
  "temporal_field": 0.57,
  "transition_boundary": 0.41
}
```

---

### **Example 4 — Gradient Inversion (R2 ↔ R3)**  
**Scenario**  
Computational temporal stability decreases while physical temporal sensitivity increases.

**TRS Output**  
```json
{
  "temporal_type": "gradient",
  "regime": "R2-R3",
  "temporal_magnitude": 0.79,
  "temporal_direction": "R3→R2",
  "temporal_curvature": 0.58,
  "instability_depth": 0.31,
  "temporal_field": 0.72,
  "transition_boundary": 0.41
}
```

---

## **3. Temporal Field Examples**

### **Example 5 — Multi‑Regime Temporal Field (R1 ↔ R2 ↔ R3)**  
**Scenario**  
A multi‑regime temporal field binds conceptual, computational, and physical temporal pathways.

**TRS Output**  
```json
{
  "temporal_type": "field",
  "regime": "R1-R2-R3",
  "temporal_magnitude": 0.94,
  "temporal_direction": "tensor",
  "temporal_curvature": 0.63,
  "instability_depth": 0.37,
  "temporal_field": 0.78,
  "transition_boundary": 0.57
}
```

---

### **Example 6 — Dimensional Temporal Constraint (R2 ↔ R4)**  
**Scenario**  
Dimensional constraints influence computational temporal pathways.

**TRS Output**  
```json
{
  "temporal_type": "field",
  "regime": "R2-R4",
  "temporal_magnitude": 0.88,
  "temporal_direction": "R4→R2",
  "temporal_curvature": 0.55,
  "instability_depth": 0.33,
  "temporal_field": 0.73,
  "transition_boundary": 0.63
}
```

---

## **4. Temporal Instability Examples**

### **Example 7 — Temporal Instability Zone (R3 → R4)**  
**Scenario**  
Physical drift amplifies temporal curvature, forming a temporal instability zone.

**TRS Output**  
```json
{
  "temporal_type": "instability",
  "regime": "R3-R4",
  "temporal_magnitude": 0.91,
  "temporal_direction": "R3→R4",
  "temporal_curvature": 0.71,
  "instability_depth": 0.52,
  "temporal_field": 0.82,
  "transition_boundary": 0.44
}
```

---

### **Example 8 — Stability‑Coherence Temporal Ridge (R2 ↔ R3)**  
**Scenario**  
Computational stability reduces coherence while physical stability increases temporal sensitivity.

**TRS Output**  
```json
{
  "temporal_type": "instability",
  "regime": "R2-R3",
  "temporal_magnitude": 0.86,
  "temporal_direction": "R2↔R3",
  "temporal_curvature": 0.62,
  "instability_depth": 0.49,
  "temporal_field": 0.77,
  "transition_boundary": 0.48
}
```

---

## **5. Temporal Transition Examples**

### **Example 9 — Cross‑Domain Temporal Transition (R1 ↔ R4)**  
**Scenario**  
A temporal transition forms between conceptual and dimensional regimes.

**TRS Output**  
```json
{
  "temporal_type": "transition",
  "regime": "R1-R4",
  "temporal_magnitude": 0.83,
  "temporal_direction": "R1↔R4",
  "temporal_curvature": 0.52,
  "instability_depth": 0.22,
  "temporal_field": 0.69,
  "transition_boundary": 0.46
}
```

---

### **Example 10 — Drift‑Sensitive Temporal Transition (R3 → R4)**  
**Scenario**  
Physical drift amplifies temporal curvature, forming a drift‑sensitive temporal transition.

**TRS Output**  
```json
{
  "temporal_type": "transition",
  "regime": "R3-R4",
  "temporal_magnitude": 0.91,
  "temporal_direction": "R3→R4",
  "temporal_curvature": 0.71,
  "instability_depth": 0.52,
  "temporal_field": 0.82,
  "transition_boundary": 0.44
}
```

---

## **6. Canonical TRS‑Temporal Output Snippet**

```json
{
  "temporal_type": "transition",
  "regime": "R1-R4",
  "temporal_magnitude": 0.83,
  "temporal_direction": "R1↔R4",
  "temporal_curvature": 0.52,
  "instability_depth": 0.22,
  "temporal_field": 0.69,
  "transition_boundary": 0.46
}
```

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑temporal  
- **Module Path:** `/docs/rtt/Temporal_Regime_Sequencer/`
