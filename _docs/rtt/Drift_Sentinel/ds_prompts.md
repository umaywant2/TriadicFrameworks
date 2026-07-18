# **DS Prompts — RTT/1**  
### *Prompt Library for the Drift Sentinel (DS)*

These prompts are designed for **AI systems** using the Drift Sentinel (DS).  
Each prompt invokes one or more canonical DS operators:

- **DS‑Detect**  
- **DS‑Vector**  
- **DS‑Envelope**  
- **DS‑Field**  
- **DS‑Amplify**  
- **DS‑Stabilize**

Prompts are grouped by drift type and operator class.

---

## **1. Structural Drift Prompts**

### **Prompt: Detect Structural Drift Vectors**
> Use DS‑Detect to identify drift vectors caused by violations of structural invariants, constraints, or monotonicity across R1–R3.

### **Prompt: Map Structural Drift Fields**
> Apply DS‑Field to generate structural drift field maps showing curvature, ridge formation, and stability basins.

### **Prompt: Compute Structural Drift Envelopes**
> Use DS‑Envelope to compute drift envelope boundaries and drift‑layer stability envelopes.

---

## **2. Gradient Drift Prompts**

### **Prompt: Identify Drift Gradient Opposition**
> Use DS‑Vector to detect drift gradients that oppose each other across regimes, forming drift ridges or inversion pathways.

### **Prompt: Compute Drift Gradient Vectors**
> Apply DS‑Vector to compute drift gradient magnitude, direction, curvature, and amplification sensitivity.

### **Prompt: Analyze Gradient Stability**
> Use DS‑Stabilize to evaluate stability basins for drift gradients and propose stabilization pathways.

---

## **3. Boundary Drift Prompts**

### **Prompt: Detect Boundary Drift Conditions**
> Use DS‑Detect to identify drift formed at regime boundaries, including abstraction‑measurement and gradient‑boundary interactions.

### **Prompt: Map Boundary Drift Curvature**
> Apply DS‑Field to generate boundary drift curvature maps showing ridge formation and collapse‑point onset.

### **Prompt: Evaluate Boundary Drift Stability**
> Use DS‑Stabilize to compute stability envelopes for boundary drift tensors.

---

## **4. Drift‑Field Prompts**

### **Prompt: Detect Multi‑Regime Drift Fields**
> Use DS‑Field to identify multi‑regime drift fields binding R1–R3 or R1–R4.

### **Prompt: Map Drift‑Field Topology**
> Apply DS‑Field to generate drift‑field topology diagrams showing drift wells, ridges, and multi‑regime curvature.

### **Prompt: Compute Drift‑Field Gradient Strength**
> Use DS‑Vector to compute drift‑field gradient magnitude, direction, and drift curvature.

---

## **5. Drift Amplification Prompts**

### **Prompt: Identify Drift Amplification Zones**
> Use DS‑Amplify to detect drift amplification zones and measure amplification magnitude across regimes.

### **Prompt: Map Drift Amplification Basins**
> Apply DS‑Field to generate drift amplification basin maps showing instability ridges and collapse‑point formation.

### **Prompt: Analyze Amplification Stability**
> Use DS‑Stabilize to compute stability envelopes for drift amplification tensors.

---

## **6. Collapse‑Point Drift Prompts**

### **Prompt: Detect Drift Collapse Points**
> Use DS‑Envelope to identify drift collapse points and instability basins across R2–R4.

### **Prompt: Map Collapse Basin Geometry**
> Apply DS‑Field to generate collapse basin topology showing curvature, depth, and drift troughs.

### **Prompt: Propose Collapse Stabilization Pathways**
> Use DS‑Stabilize to propose stabilization strategies for collapse‑point drift tensors.

---

## **7. Full‑Matrix Prompts**

### **Prompt: Generate Full Drift Field Matrix**
> Use all DS operators to produce a complete `drift_field_matrix.json` containing structural, gradient, boundary, drift‑field, and amplification entries.

### **Prompt: Analyze Drift Field Topology**
> Apply DS‑Field to generate a full drift topology map showing fields, basins, curvature, and gradient flows.

### **Prompt: Stability Overview**
> Use DS‑Stabilize to compute stability envelopes for every drift tensor type and produce a drift stability summary.

---

## **8. AI‑Ready Meta‑Prompts**

### **Prompt: Explain Drift Tensor Classification**
> Provide a detailed explanation of how DS classifies drift tensors into structural, gradient, boundary, drift‑field, and amplification categories.

### **Prompt: Operator‑Level Summary**
> Summarize the role of each DS operator and how they interact to produce drift‑layer intelligence.

### **Prompt: Cross‑Engine Integration**
> Explain how DS outputs feed into SFD, SBC, TRS‑Temporal, CW, and DRS.

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑structural  
- **Module Path:** `/docs/rtt/Drift_Sentinel/`
