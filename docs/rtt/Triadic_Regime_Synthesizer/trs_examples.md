# **Triadic Regime Synthesizer Examples — RTT/1**  
### *Example Dictionary for the Triadic Regime Synthesizer (TRS)*

These examples illustrate how the **Triadic Regime Synthesizer (TRS)** detects regime interlocks, merges boundaries, computes synthesis tensors, identifies fusion points, evaluates coherence ridges, and resolves regime conflicts.

Each example demonstrates one or more TRS operators:

- **TRS‑Synthesize**  
- **TRS‑Merge**  
- **TRS‑Harmonize**  
- **TRS‑Boundary**  
- **TRS‑Tensor**  
- **TRS‑Resolve**

Examples are grouped by regime tensor type.

---

## **1. Regime Signature Examples**

### **Example 1 — Conceptual Regime Signature (R1)**  
**Scenario**  
A conceptual model exhibits a low‑curvature regime onset with stable polarity.

**TRS Output**  
```json
{
  "regime_type": "signature",
  "regime": "R1",
  "synthesis_magnitude": 0.41,
  "synthesis_direction": "conceptual",
  "synthesis_curvature": 0.22,
  "fusion_depth": 0.11,
  "coherence_field": 0.63,
  "boundary_stability": 0.44
}
```

---

### **Example 2 — Dimensional Regime Signature (R4)**  
**Scenario**  
Dimensional constraints produce a high‑sensitivity regime onset.

**TRS Output**  
```json
{
  "regime_type": "signature",
  "regime": "R4",
  "synthesis_magnitude": 0.72,
  "synthesis_direction": "dimensional",
  "synthesis_curvature": 0.44,
  "fusion_depth": 0.22,
  "coherence_field": 0.57,
  "boundary_stability": 0.41
}
```

---

## **2. Regime Boundary Examples**

### **Example 3 — Boundary Stability (R2)**  
**Scenario**  
A computational structure exhibits stable boundary curvature with low drift sensitivity.

**TRS Output**  
```json
{
  "regime_type": "boundary",
  "regime": "R2",
  "synthesis_magnitude": 0.52,
  "synthesis_direction": "computational",
  "synthesis_curvature": 0.33,
  "fusion_depth": 0.27,
  "coherence_field": 0.57,
  "boundary_stability": 0.41
}
```

---

### **Example 4 — Boundary Inversion (R2 ↔ R3)**  
**Scenario**  
Computational boundary stability decreases while physical boundary sensitivity increases.

**TRS Output**  
```json
{
  "regime_type": "boundary",
  "regime": "R2-R3",
  "synthesis_magnitude": 0.79,
  "synthesis_direction": "R3→R2",
  "synthesis_curvature": 0.58,
  "fusion_depth": 0.31,
  "coherence_field": 0.72,
  "boundary_stability": 0.41
}
```

---

## **3. Regime Interlock Examples**

### **Example 5 — Multi‑Regime Interlock (R1 ↔ R2 ↔ R3)**  
**Scenario**  
A multi‑regime interlock binds conceptual, computational, and physical regime pathways.

**TRS Output**  
```json
{
  "regime_type": "interlock",
  "regime": "R1-R2-R3",
  "synthesis_magnitude": 0.94,
  "synthesis_direction": "tensor",
  "synthesis_curvature": 0.63,
  "fusion_depth": 0.37,
  "coherence_field": 0.78,
  "boundary_stability": 0.57
}
```

---

### **Example 6 — Dimensional Interlock Constraint (R2 ↔ R4)**  
**Scenario**  
Dimensional constraints influence computational regime pathways.

**TRS Output**  
```json
{
  "regime_type": "interlock",
  "regime": "R2-R4",
  "synthesis_magnitude": 0.88,
  "synthesis_direction": "R4→R2",
  "synthesis_curvature": 0.55,
  "fusion_depth": 0.33,
  "coherence_field": 0.73,
  "boundary_stability": 0.63
}
```

---

## **4. Regime Synthesis Examples**

### **Example 7 — Regime Synthesis (R1 ↔ R3)**  
**Scenario**  
Conceptual abstraction amplifies physical regime curvature, forming a synthesis zone.

**TRS Output**  
```json
{
  "regime_type": "synthesis",
  "regime": "R1-R3",
  "synthesis_magnitude": 0.67,
  "synthesis_direction": "R1→R3",
  "synthesis_curvature": 0.33,
  "fusion_depth": 0.22,
  "coherence_field": 0.55,
  "boundary_stability": 0.38
}
```

---

### **Example 8 — Dimensional Synthesis (R2 ↔ R4)**  
**Scenario**  
Dimensional constraints amplify computational regime synthesis.

**TRS Output**  
```json
{
  "regime_type": "synthesis",
  "regime": "R2-R4",
  "synthesis_magnitude": 0.88,
  "synthesis_direction": "R2↔R4",
  "synthesis_curvature": 0.47,
  "fusion_depth": 0.29,
  "coherence_field": 0.66,
  "boundary_stability": 0.58
}
```

---

## **5. Regime Coherence Examples**

### **Example 9 — Coherence Ridge (R1 ↔ R4)**  
**Scenario**  
A coherence ridge forms between conceptual and dimensional regimes.

**TRS Output**  
```json
{
  "regime_type": "coherence",
  "regime": "R1-R4",
  "synthesis_magnitude": 0.83,
  "synthesis_direction": "R1↔R4",
  "synthesis_curvature": 0.52,
  "fusion_depth": 0.22,
  "coherence_field": 0.69,
  "boundary_stability": 0.46
}
```

---

### **Example 10 — Drift‑Sensitive Coherence (R3 → R4)**  
**Scenario**  
Physical drift amplifies coherence curvature, forming a drift‑sensitive coherence zone.

**TRS Output**  
```json
{
  "regime_type": "coherence",
  "regime": "R3-R4",
  "synthesis_magnitude": 0.91,
  "synthesis_direction": "R3→R4",
  "synthesis_curvature": 0.71,
  "fusion_depth": 0.52,
  "coherence_field": 0.82,
  "boundary_stability": 0.44
}
```

---

## **6. Canonical TRS Output Snippet**

```json
{
  "regime_type": "synthesis",
  "regime": "R1-R4",
  "synthesis_magnitude": 0.83,
  "synthesis_direction": "R1↔R4",
  "synthesis_curvature": 0.52,
  "fusion_depth": 0.22,
  "coherence_field": 0.69,
  "boundary_stability": 0.46
}
```

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑regime  
- **Module Path:** `/docs/rtt/Triadic_Regime_Synthesizer/`
