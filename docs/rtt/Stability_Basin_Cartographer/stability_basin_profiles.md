# **Stability Basin Profiles — RTT/1**  
### *Profile Dictionary for the Stability Basin Cartographer (SBC)*

Stability basin profiles define the **canonical shapes, behaviors, collapse geometries, gradient flows, and stability‑field interactions** across conceptual, computational, physical, and dimensional regimes.

These profiles are used by:

- **SBC‑Map**  
- **SBC‑Basin**  
- **SBC‑Gradient**  
- **SBC‑Field**  
- **SBC‑Collapse**  
- **SBC‑Stabilize**

Each profile includes:

- **definition**  
- **basin signature**  
- **field behavior**  
- **gradient behavior**  
- **collapse geometry**  
- **stability envelope**  
- **canonical SBC output pattern**

---

## **1. Stability Basin Profiles**

### **Profile: Conceptual Stability Basin**
**Definition**  
A stability basin formed by conceptual coherence and low‑curvature conceptual structures.

**Basin Signature**
- low magnitude  
- stable direction  
- shallow curvature  

**Field Behavior**
- narrow stability field  
- shallow ridge  

**Gradient Behavior**
- low gradient sensitivity  

**Collapse Geometry**
- shallow collapse zone  

**Stability Envelope**
- high stability  

---

### **Profile: Computational Stability Basin**
**Definition**  
A basin formed by computational consistency, calibration, and structural predictability.

**Basin Signature**
- medium magnitude  
- stable computational direction  
- medium curvature  

**Field Behavior**
- moderate field width  
- calibration ridge  

**Gradient Behavior**
- medium gradient sensitivity  

**Collapse Geometry**
- medium collapse zone  

**Stability Envelope**
- medium stability  

---

## **2. Gradient Basin Profiles**

### **Profile: Gradient Basin Opposition**
**Definition**  
A basin formed when gradients across regimes oppose each other.

**Basin Signature**
- high magnitude  
- bidirectional vector  
- high curvature  

**Field Behavior**
- wide stability field  
- ridge inversion  

**Gradient Behavior**
- medium‑high gradient sensitivity  

**Collapse Geometry**
- deep collapse zone  

**Stability Envelope**
- medium stability  

---

### **Profile: Gradient Inversion Basin**
**Definition**  
A basin formed when stability decreases in one regime while increasing in another.

**Basin Signature**
- medium‑high magnitude  
- inversion vector  
- polarity flip  

**Field Behavior**
- medium field width  
- inversion curvature  

**Gradient Behavior**
- high gradient sensitivity  

**Collapse Geometry**
- medium‑deep collapse zone  

**Stability Envelope**
- medium‑low stability  

---

## **3. Boundary Basin Profiles**

### **Profile: Abstraction‑Measurement Basin**
**Definition**  
A basin formed at the boundary between conceptual abstraction and physical measurement.

**Basin Signature**
- medium magnitude  
- abstraction → measurement direction  
- boundary curvature  

**Field Behavior**
- narrow field  
- boundary ridge  

**Gradient Behavior**
- low gradient sensitivity  

**Collapse Geometry**
- shallow collapse zone  

**Stability Envelope**
- medium‑high stability  

---

### **Profile: Gradient‑Boundary Basin**
**Definition**  
Aligned gradients across regimes produce contradictory stability outcomes.

**Basin Signature**
- high magnitude  
- aligned direction  
- medium curvature  

**Field Behavior**
- wide field  
- alignment trough  

**Gradient Behavior**
- medium gradient sensitivity  

**Collapse Geometry**
- medium‑deep collapse zone  

**Stability Envelope**
- medium stability  

---

## **4. Stability‑Field Profiles**

### **Profile: Multi‑Regime Stability Field**
**Definition**  
A multi‑regime stability tensor binding stability basins across R1–R3 or R1–R4.

**Basin Signature**
- very high magnitude  
- tensor direction  
- high curvature  

**Field Behavior**
- wide stability field  
- tensor topology  

**Gradient Behavior**
- high gradient sensitivity  

**Collapse Geometry**
- deep collapse zone  

**Stability Envelope**
- medium‑high stability  

---

### **Profile: Dimensional Stability Constraint**
**Definition**  
Dimensional constraints influence computational stability pathways.

**Basin Signature**
- high magnitude  
- dimensional → computational direction  
- medium‑high curvature  

**Field Behavior**
- medium‑wide field  
- tensor trough  

**Gradient Behavior**
- medium gradient sensitivity  

**Collapse Geometry**
- medium‑deep collapse zone  

**Stability Envelope**
- medium stability  

---

## **5. Collapse‑Zone Profiles**

### **Profile: Stability Collapse Basin**
**Definition**  
A collapse basin formed when stability collapses into dimensional instability.

**Basin Signature**
- very high magnitude  
- collapse‑aligned direction  
- high curvature  

**Field Behavior**
- wide collapse field  
- collapse basin  

**Gradient Behavior**
- very high gradient sensitivity  

**Collapse Geometry**
- deep collapse seam  
- instability ridge  

**Stability Envelope**
- low stability  

---

### **Profile: Stability‑Coherence Collapse Ridge**
**Definition**  
Stability reduces coherence while physical stability increases coherence sensitivity.

**Basin Signature**
- medium‑high magnitude  
- coherence‑aligned direction  
- medium‑high curvature  

**Field Behavior**
- medium field  
- collapse ridge  

**Gradient Behavior**
- high gradient sensitivity  

**Collapse Geometry**
- medium‑deep collapse zone  

**Stability Envelope**
- medium‑low stability  

---

## **6. Canonical SBC Output Pattern**

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
