# **Dimensional Resonance Scanner Examples — RTT/1**  
### *Example Dictionary for the Dimensional Resonance Scanner (DRS)*

These examples illustrate how the **Dimensional Resonance Scanner (DRS)** detects resonance signatures, computes resonance frequencies, maps resonance fields, identifies amplification zones, and evaluates multi‑regime resonance gradients.

Each example demonstrates one or more DRS operators:

- **DRS‑Scan**  
- **DRS‑Frequency**  
- **DRS‑Field**  
- **DRS‑Vector**  
- **DRS‑Amplify**  
- **DRS‑Stabilize**

Examples are grouped by resonance tensor type.

---

## **1. Resonance Signature Examples**

### **Example 1 — Conceptual Resonance Signature (R1)**  
**Scenario**  
A conceptual model exhibits a low‑frequency resonance onset with shallow curvature.

**DRS Output**  
```json
{
  "resonance_type": "signature",
  "regime": "R1",
  "resonance_magnitude": 0.41,
  "resonance_direction": "conceptual",
  "resonance_curvature": 0.22,
  "amplification_zone": 0.11,
  "resonance_field": 0.63,
  "envelope_boundary": 0.44
}
```

---

### **Example 2 — Dimensional Resonance Signature (R4)**  
**Scenario**  
Dimensional constraints produce a high‑sensitivity resonance onset.

**DRS Output**  
```json
{
  "resonance_type": "signature",
  "regime": "R4",
  "resonance_magnitude": 0.72,
  "resonance_direction": "dimensional",
  "resonance_curvature": 0.44,
  "amplification_zone": 0.22,
  "resonance_field": 0.57,
  "envelope_boundary": 0.41
}
```

---

## **2. Resonance Frequency Examples**

### **Example 3 — Harmonic Resonance Frequency (R2)**  
**Scenario**  
A computational structure exhibits a stable harmonic resonance frequency.

**DRS Output**  
```json
{
  "resonance_type": "frequency",
  "regime": "R2",
  "resonance_magnitude": 0.52,
  "resonance_direction": "computational",
  "resonance_curvature": 0.33,
  "amplification_zone": 0.27,
  "resonance_field": 0.57,
  "envelope_boundary": 0.41
}
```

---

### **Example 4 — Frequency Inversion (R2 ↔ R3)**  
**Scenario**  
Computational resonance decreases while physical resonance sensitivity increases.

**DRS Output**  
```json
{
  "resonance_type": "frequency",
  "regime": "R2-R3",
  "resonance_magnitude": 0.79,
  "resonance_direction": "R3→R2",
  "resonance_curvature": 0.58,
  "amplification_zone": 0.31,
  "resonance_field": 0.72,
  "envelope_boundary": 0.41
}
```

---

## **3. Resonance Field Examples**

### **Example 5 — Multi‑Regime Resonance Field (R1 ↔ R2 ↔ R3)**  
**Scenario**  
A multi‑regime resonance field binds conceptual, computational, and physical resonance pathways.

**DRS Output**  
```json
{
  "resonance_type": "field",
  "regime": "R1-R2-R3",
  "resonance_magnitude": 0.94,
  "resonance_direction": "tensor",
  "resonance_curvature": 0.63,
  "amplification_zone": 0.37,
  "resonance_field": 0.78,
  "envelope_boundary": 0.57
}
```

---

### **Example 6 — Dimensional Resonance Constraint (R2 ↔ R4)**  
**Scenario**  
Dimensional constraints influence computational resonance pathways.

**DRS Output**  
```json
{
  "resonance_type": "field",
  "regime": "R2-R4",
  "resonance_magnitude": 0.88,
  "resonance_direction": "R4→R2",
  "resonance_curvature": 0.55,
  "amplification_zone": 0.33,
  "resonance_field": 0.73,
  "envelope_boundary": 0.63
}
```

---

## **4. Resonance Amplification Examples**

### **Example 7 — Amplification Zone (R3 → R4)**  
**Scenario**  
Physical drift amplifies resonance curvature, forming a resonance amplification zone.

**DRS Output**  
```json
{
  "resonance_type": "amplification",
  "regime": "R3-R4",
  "resonance_magnitude": 0.91,
  "resonance_direction": "R3→R4",
  "resonance_curvature": 0.71,
  "amplification_zone": 0.52,
  "resonance_field": 0.82,
  "envelope_boundary": 0.44
}
```

---

### **Example 8 — Stability‑Coherence Resonance Ridge (R2 ↔ R3)**  
**Scenario**  
Computational stability reduces coherence while physical stability increases resonance sensitivity.

**DRS Output**  
```json
{
  "resonance_type": "amplification",
  "regime": "R2-R3",
  "resonance_magnitude": 0.86,
  "resonance_direction": "R2↔R3",
  "resonance_curvature": 0.62,
  "amplification_zone": 0.49,
  "resonance_field": 0.77,
  "envelope_boundary": 0.48
}
```

---

## **5. Resonance Vector Examples**

### **Example 9 — Cross‑Domain Resonance Vector (R1 ↔ R4)**  
**Scenario**  
A resonance vector forms between conceptual and dimensional regimes.

**DRS Output**  
```json
{
  "resonance_type": "vector",
  "regime": "R1-R4",
  "resonance_magnitude": 0.83,
  "resonance_direction": "R1↔R4",
  "resonance_curvature": 0.52,
  "amplification_zone": 0.22,
  "resonance_field": 0.69,
  "envelope_boundary": 0.46
}
```

---

### **Example 10 — Drift‑Sensitive Resonance Vector (R3 → R4)**  
**Scenario**  
Physical drift amplifies resonance curvature, forming a drift‑sensitive resonance vector.

**DRS Output**  
```json
{
  "resonance_type": "vector",
  "regime": "R3-R4",
  "resonance_magnitude": 0.91,
  "resonance_direction": "R3→R4",
  "resonance_curvature": 0.71,
  "amplification_zone": 0.52,
  "resonance_field": 0.82,
  "envelope_boundary": 0.44
}
```

---

## **6. Canonical DRS Output Snippet**

```json
{
  "resonance_type": "vector",
  "regime": "R1-R4",
  "resonance_magnitude": 0.83,
  "resonance_direction": "R1↔R4",
  "resonance_curvature": 0.52,
  "amplification_zone": 0.22,
  "resonance_field": 0.69,
  "envelope_boundary": 0.46
}
```

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑resonance  
- **Module Path:** `/docs/rtt/Dimensional_Resonance_Scanner/`
