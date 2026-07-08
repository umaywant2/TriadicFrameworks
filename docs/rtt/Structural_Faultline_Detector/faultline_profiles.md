# **Faultline Profiles — RTT/1**  
### *Profile Dictionary for the Structural Faultline Detector (SFD)*

Faultline profiles define the **canonical shapes, behaviors, propagation patterns, instability seams, and collapse geometries** of structural faultlines across conceptual, computational, physical, and dimensional regimes.

These profiles are used by:

- **SFD‑Detect**  
- **SFD‑Fracture**  
- **SFD‑Seam**  
- **SFD‑Field**  
- **SFD‑Propagate**  
- **SFD‑Stabilize**

Each profile includes:

- **definition**  
- **faultline signature**  
- **field behavior**  
- **propagation behavior**  
- **instability seam geometry**  
- **stability envelope**  
- **canonical SFD output pattern**

---

## **1. Structural Fracture Profiles**

### **Profile: Structural Invariant Fracture**
**Definition**  
Fracture emerging from violation of structural invariants (symmetry, conservation, monotonicity).

**Faultline Signature**
- medium‑high magnitude  
- stable direction  
- low curvature  

**Field Behavior**
- narrow faultline field  
- shallow ridge  

**Propagation Behavior**
- low propagation rate  

**Instability Seam Geometry**
- shallow seam  
- rigid boundary  

**Stability Envelope**
- high stability  

---

### **Profile: Calibration‑Mismatch Fracture**
**Definition**  
Fracture caused by divergence between computational calibration and physical measurement.

**Faultline Signature**
- medium magnitude  
- oscillating direction  
- calibration curvature  

**Field Behavior**
- moderate field width  
- calibration ridge  

**Propagation Behavior**
- medium propagation rate  

**Instability Seam Geometry**
- medium depth  

**Stability Envelope**
- medium stability  

---

## **2. Gradient Faultline Profiles**

### **Profile: Gradient Faultline Opposition**
**Definition**  
Faultlines formed when gradients across regimes oppose each other.

**Faultline Signature**
- high magnitude  
- bidirectional vector  
- high curvature  

**Field Behavior**
- wide faultline field  
- ridge inversion  

**Propagation Behavior**
- medium‑high propagation  

**Instability Seam Geometry**
- deep seam  

**Stability Envelope**
- medium stability  

---

### **Profile: Gradient Inversion Faultline**
**Definition**  
Faultline formed when drift decreases in one regime while increasing in another.

**Faultline Signature**
- medium‑high magnitude  
- inversion vector  
- polarity flip  

**Field Behavior**
- medium field width  
- inversion curvature  

**Propagation Behavior**
- high propagation sensitivity  

**Instability Seam Geometry**
- medium‑deep seam  

**Stability Envelope**
- medium‑low stability  

---

## **3. Boundary Faultline Profiles**

### **Profile: Abstraction‑Measurement Faultline**
**Definition**  
Faultline formed at the boundary between conceptual abstraction and physical measurement.

**Faultline Signature**
- medium magnitude  
- abstraction → measurement direction  
- boundary curvature  

**Field Behavior**
- narrow field  
- boundary ridge  

**Propagation Behavior**
- low propagation  

**Instability Seam Geometry**
- shallow seam  

**Stability Envelope**
- medium‑high stability  

---

### **Profile: Gradient‑Boundary Faultline**
**Definition**  
Aligned gradients across regimes produce contradictory structural outcomes.

**Faultline Signature**
- high magnitude  
- aligned direction  
- medium curvature  

**Field Behavior**
- wide field  
- alignment trough  

**Propagation Behavior**
- medium propagation  

**Instability Seam Geometry**
- medium‑deep seam  

**Stability Envelope**
- medium stability  

---

## **4. Faultline‑Field Profiles**

### **Profile: Multi‑Regime Faultline Field**
**Definition**  
A multi‑regime faultline tensor binds structural fractures across R1–R3 or R1–R4.

**Faultline Signature**
- very high magnitude  
- tensor direction  
- high curvature  

**Field Behavior**
- wide faultline field  
- tensor topology  

**Propagation Behavior**
- high propagation  

**Instability Seam Geometry**
- deep seam  

**Stability Envelope**
- medium‑high stability  

---

### **Profile: Dimensional Faultline Constraint**
**Definition**  
Dimensional constraints influence computational structural pathways.

**Faultline Signature**
- high magnitude  
- dimensional → computational direction  
- medium‑high curvature  

**Field Behavior**
- medium‑wide field  
- tensor trough  

**Propagation Behavior**
- medium propagation  

**Instability Seam Geometry**
- medium‑deep seam  

**Stability Envelope**
- medium stability  

---

## **5. Drift‑Sensitive Faultline Profiles**

### **Profile: Drift‑Amplified Faultline Basin**
**Definition**  
Drift amplification increases structural curvature, forming a drift‑sensitive faultline basin.

**Faultline Signature**
- very high magnitude  
- amplification‑aligned direction  
- high curvature  

**Field Behavior**
- wide field  
- amplification basin  

**Propagation Behavior**
- very high propagation  

**Instability Seam Geometry**
- deep collapse seam  
- instability ridge  

**Stability Envelope**
- low stability  

---

### **Profile: Drift‑Coherence Faultline Ridge**
**Definition**  
Drift increases coherence sensitivity, amplifying structural curvature.

**Faultline Signature**
- medium‑high magnitude  
- coherence‑aligned direction  
- medium‑high curvature  

**Field Behavior**
- medium field  
- amplification ridge  

**Propagation Behavior**
- high propagation  

**Instability Seam Geometry**
- medium‑deep seam  

**Stability Envelope**
- medium‑low stability  

---

## **6. Canonical SFD Output Pattern**

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
