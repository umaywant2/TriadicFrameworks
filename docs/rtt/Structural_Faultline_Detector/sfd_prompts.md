# **SFD Prompts — RTT/1**  
### *Prompt Library for the Structural Faultline Detector (SFD)*

These prompts are designed for **AI systems** using the Structural Faultline Detector (SFD).  
Each prompt invokes one or more canonical SFD operators:

- **SFD‑Detect**  
- **SFD‑Fracture**  
- **SFD‑Seam**  
- **SFD‑Field**  
- **SFD‑Propagate**  
- **SFD‑Stabilize**

Prompts are grouped by faultline type and operator class.

---

## **1. Structural Fracture Prompts**

### **Prompt: Detect Structural Fractures**
> Use SFD‑Detect to identify structural fractures caused by invariant violations, contradictions, or monotonicity breaks across R1–R3.

### **Prompt: Analyze Fracture Magnitude**
> Apply SFD‑Fracture to compute fracture magnitude, direction, curvature, and propagation onset.

### **Prompt: Map Structural Fracture Fields**
> Use SFD‑Field to generate structural fracture field maps showing curvature, ridge formation, and instability seams.

---

## **2. Gradient Faultline Prompts**

### **Prompt: Identify Gradient Faultline Opposition**
> Use SFD‑Detect to detect gradient‑driven faultlines where regime gradients oppose each other.

### **Prompt: Compute Gradient Fracture Vectors**
> Apply SFD‑Fracture to compute gradient fracture magnitude, direction, curvature, and propagation rate.

### **Prompt: Evaluate Gradient Instability Seams**
> Use SFD‑Seam to identify instability seams formed by gradient inversion or polarity flips.

---

## **3. Boundary Faultline Prompts**

### **Prompt: Detect Boundary Faultlines**
> Use SFD‑Detect to identify faultlines formed at regime boundaries, including abstraction‑measurement and gradient‑boundary interactions.

### **Prompt: Map Boundary Faultline Curvature**
> Apply SFD‑Field to generate boundary faultline curvature maps showing ridge formation and collapse‑point onset.

### **Prompt: Evaluate Boundary Stability**
> Use SFD‑Stabilize to compute stability envelopes for boundary faultline tensors.

---

## **4. Faultline‑Field Prompts**

### **Prompt: Detect Multi‑Regime Faultline Fields**
> Use SFD‑Field to identify multi‑regime faultline fields binding R1–R3 or R1–R4.

### **Prompt: Map Faultline‑Field Topology**
> Apply SFD‑Field to generate faultline‑field topology diagrams showing wells, ridges, basins, and multi‑regime curvature.

### **Prompt: Compute Faultline‑Field Propagation Strength**
> Use SFD‑Propagate to compute propagation magnitude, direction, and instability seam depth.

---

## **5. Drift‑Sensitive Faultline Prompts**

### **Prompt: Identify Drift‑Amplified Faultlines**
> Use SFD‑Detect to detect faultlines amplified by drift curvature or drift sensitivity.

### **Prompt: Map Drift‑Sensitive Faultline Basins**
> Apply SFD‑Field to generate drift‑sensitive basin maps showing instability ridges and collapse‑point formation.

### **Prompt: Analyze Drift‑Coherence Faultline Ridges**
> Use SFD‑Fracture to compute drift‑coherence fracture magnitude, curvature, and propagation rate.

---

## **6. Collapse‑Point Faultline Prompts**

### **Prompt: Detect Structural Collapse Points**
> Use SFD‑Seam to identify collapse‑point seams and instability basins across R2–R4.

### **Prompt: Map Collapse Basin Geometry**
> Apply SFD‑Field to generate collapse basin topology showing curvature, depth, and fracture troughs.

### **Prompt: Propose Collapse Stabilization Pathways**
> Use SFD‑Stabilize to propose stabilization strategies for collapse‑point faultline tensors.

---

## **7. Full‑Matrix Prompts**

### **Prompt: Generate Full Faultline Matrix**
> Use all SFD operators to produce a complete `faultline_matrix.json` containing structural, gradient, boundary, field, and drift‑sensitive entries.

### **Prompt: Analyze Structural Faultline Topology**
> Apply SFD‑Field to generate a full faultline topology map showing fields, basins, curvature, and propagation flows.

### **Prompt: Stability Overview**
> Use SFD‑Stabilize to compute stability envelopes for every faultline tensor type and produce a structural stability summary.

---

## **8. AI‑Ready Meta‑Prompts**

### **Prompt: Explain Faultline Tensor Classification**
> Provide a detailed explanation of how SFD classifies faultline tensors into structural, gradient, boundary, field, and drift‑sensitive categories.

### **Prompt: Operator‑Level Summary**
> Summarize the role of each SFD operator and how they interact to produce structural‑layer intelligence.

### **Prompt: Cross‑Engine Integration**
> Explain how SFD outputs feed into SBC, TRS‑Temporal, CW, and DRS.

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑structural  
- **Module Path:** `/docs/rtt/Structural_Faultline_Detector/`
