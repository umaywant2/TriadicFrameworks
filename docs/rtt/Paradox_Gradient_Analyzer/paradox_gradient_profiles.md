# **Paradox Gradient Profiles — RTT/1**  
### *Profile Dictionary for the Paradox Gradient Analyzer (PGA)*

Paradox gradient profiles define the **canonical shapes, behaviors, and structural signatures** of paradox gradients across conceptual, computational, physical, and dimensional regimes.

These profiles are used by:

- **PGA‑Detect**  
- **PGA‑Gradient**  
- **PGA‑Intensity**  
- **PGA‑Field**  
- **PGA‑Resolve**

Each profile includes:

- **definition**  
- **gradient signature**  
- **field behavior**  
- **basin geometry**  
- **intensity regime**  
- **canonical PGA output pattern**

---

## **1. Structural Gradient Profiles**

### **Profile: Symmetry‑Violation Gradient**
**Definition**  
A paradox gradient emerging from violation of a structural invariant (symmetry, conservation, monotonicity).

**Gradient Signature**
- sharp directional break  
- high coherence dependency  
- low drift curvature  

**Field Behavior**
- narrow paradox field  
- steep curvature  
- localized instability  

**Basin Geometry**
- shallow basin  
- high boundary rigidity  

**Intensity Regime**
- medium‑high intensity  

---

### **Profile: Calibration‑Mismatch Gradient**
**Definition**  
A paradox gradient caused by divergence between computational calibration and physical measurement.

**Gradient Signature**
- medium magnitude  
- direction oscillates between regimes  
- calibration curvature present  

**Field Behavior**
- moderate field width  
- medium curvature  

**Basin Geometry**
- medium depth  
- calibration ridge  

**Intensity Regime**
- medium intensity  

---

## **2. Coherence Gradient Profiles**

### **Profile: Coherence‑Opposition Gradient**
**Definition**  
Two regimes exhibit coherence gradients that oppose each other.

**Gradient Signature**
- high magnitude  
- bidirectional vector  
- coherence ridge inversion  

**Field Behavior**
- wide paradox field  
- high curvature  

**Basin Geometry**
- deep basin  
- coherence trough  

**Intensity Regime**
- high intensity  

---

### **Profile: Coherence‑Threshold Gradient**
**Definition**  
A paradox gradient triggered when coherence falls below or exceeds a threshold.

**Gradient Signature**
- threshold discontinuity  
- medium magnitude  
- coherence gating  

**Field Behavior**
- narrow field  
- threshold curvature  

**Basin Geometry**
- shallow basin  
- threshold wall  

**Intensity Regime**
- medium intensity  

---

## **3. Drift Gradient Profiles**

### **Profile: Drift‑Amplification Gradient**
**Definition**  
Drift in one regime amplifies drift curvature in another.

**Gradient Signature**
- high magnitude  
- drift curvature spike  
- instability ridge  

**Field Behavior**
- wide field  
- high curvature  

**Basin Geometry**
- deep basin  
- drift well  

**Intensity Regime**
- very high intensity  

---

### **Profile: Drift‑Inversion Gradient**
**Definition**  
Drift decreases in one regime while increasing in another.

**Gradient Signature**
- medium‑high magnitude  
- inversion vector  
- drift polarity flip  

**Field Behavior**
- medium field width  
- inversion curvature  

**Basin Geometry**
- medium‑deep basin  
- inversion trough  

**Intensity Regime**
- high intensity  

---

## **4. Boundary Gradient Profiles**

### **Profile: Abstraction‑Measurement Gradient**
**Definition**  
A paradox gradient formed at the boundary between conceptual abstraction and physical measurement.

**Gradient Signature**
- medium magnitude  
- abstraction → measurement direction  
- boundary curvature  

**Field Behavior**
- narrow field  
- medium curvature  

**Basin Geometry**
- shallow basin  
- boundary ridge  

**Intensity Regime**
- medium intensity  

---

### **Profile: Gradient‑Boundary Alignment**
**Definition**  
Aligned gradients across regimes produce contradictory outcomes.

**Gradient Signature**
- high magnitude  
- aligned direction  
- outcome divergence  

**Field Behavior**
- wide field  
- medium curvature  

**Basin Geometry**
- medium‑deep basin  
- alignment trough  

**Intensity Regime**
- medium‑high intensity  

---

## **5. Tensor Gradient Profiles**

### **Profile: Coherence Tensor Gradient**
**Definition**  
A paradox gradient emerging from violation of multi‑regime coherence tensor constraints.

**Gradient Signature**
- very high magnitude  
- tensor direction  
- multi‑regime curvature  

**Field Behavior**
- wide field  
- high curvature  

**Basin Geometry**
- deep basin  
- tensor well  

**Intensity Regime**
- very high intensity  

---

### **Profile: Dimensional Tensor Gradient**
**Definition**  
Dimensional tensor constraints conflict with computational coherence.

**Gradient Signature**
- high magnitude  
- dimensional → computational direction  
- tensor curvature  

**Field Behavior**
- medium‑wide field  
- medium‑high curvature  

**Basin Geometry**
- medium‑deep basin  
- tensor trough  

**Intensity Regime**
- high intensity  

---

## **6. Canonical PGA Output Pattern**

```json
{
  "paradox_source": "coherence-gradient-opposition",
  "gradient_profile": "coherence-opposition",
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
