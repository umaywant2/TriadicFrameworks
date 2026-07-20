# **SBC Prompts — RTT/1**  
### *Prompt Library for the Stability Basin Cartographer (SBC)*

These prompts are designed for **AI systems** using the Stability Basin Cartographer (SBC).  
Each prompt invokes one or more canonical SBC operators:

- **SBC‑Map**  
- **SBC‑Basin**  
- **SBC‑Gradient**  
- **SBC‑Field**  
- **SBC‑Collapse**  
- **SBC‑Stabilize**

Prompts are grouped by basin type and operator class.

---

## **1. Stability Basin Prompts**

### **Prompt: Map Stability Basins**
> Use SBC‑Map to identify stability basins, basin boundaries, stability fields, and collapse zones across R1–R4.

### **Prompt: Analyze Basin Magnitude**
> Apply SBC‑Basin to compute basin magnitude, direction, curvature, and envelope boundaries.

### **Prompt: Evaluate Basin Stability**
> Use SBC‑Stabilize to compute stability envelopes and propose reinforcement pathways.

---

## **2. Gradient Basin Prompts**

### **Prompt: Detect Gradient Basin Opposition**
> Use SBC‑Map to detect gradient‑driven basins where regime gradients oppose each other.

### **Prompt: Compute Gradient Flow**
> Apply SBC‑Gradient to compute basin gradient magnitude, direction, curvature, and stability flow.

### **Prompt: Evaluate Gradient Collapse Zones**
> Use SBC‑Collapse to identify collapse zones formed by gradient inversion or polarity flips.

---

## **3. Boundary Basin Prompts**

### **Prompt: Detect Boundary Stability Basins**
> Use SBC‑Map to identify stability basins formed at regime boundaries, including abstraction‑measurement and gradient‑boundary interactions.

### **Prompt: Map Boundary Basin Curvature**
> Apply SBC‑Field to generate boundary basin curvature maps showing ridge formation and collapse‑point onset.

### **Prompt: Evaluate Boundary Stability**
> Use SBC‑Stabilize to compute stability envelopes for boundary basin tensors.

---

## **4. Stability‑Field Prompts**

### **Prompt: Detect Multi‑Regime Stability Fields**
> Use SBC‑Field to identify multi‑regime stability fields binding R1–R3 or R1–R4.

### **Prompt: Map Stability‑Field Topology**
> Apply SBC‑Field to generate stability‑field topology diagrams showing wells, ridges, basins, and multi‑regime curvature.

### **Prompt: Compute Stability‑Field Collapse Strength**
> Use SBC‑Collapse to compute collapse magnitude, direction, and collapse‑zone depth.

---

## **5. Collapse‑Zone Prompts**

### **Prompt: Detect Stability Collapse Points**
> Use SBC‑Collapse to identify collapse‑point seams and instability basins across R2–R4.

### **Prompt: Map Collapse Basin Geometry**
> Apply SBC‑Field to generate collapse basin topology showing curvature, depth, and fracture troughs.

### **Prompt: Propose Collapse Stabilization Pathways**
> Use SBC‑Stabilize to propose stabilization strategies for collapse‑point stability tensors.

---

## **6. Full‑Matrix Prompts**

### **Prompt: Generate Full Stability Basin Matrix**
> Use all SBC operators to produce a complete `stability_basin_matrix.json` containing stability, gradient, boundary, field, and collapse‑zone entries.

### **Prompt: Analyze Stability Topology**
> Apply SBC‑Field to generate a full stability topology map showing fields, basins, curvature, and collapse flows.

### **Prompt: Stability Overview**
> Use SBC‑Stabilize to compute stability envelopes for every basin tensor type and produce a stability summary.

---

## **7. AI‑Ready Meta‑Prompts**

### **Prompt: Explain Basin Tensor Classification**
> Provide a detailed explanation of how SBC classifies basin tensors into stability, gradient, boundary, field, and collapse‑zone categories.

### **Prompt: Operator‑Level Summary**
> Summarize the role of each SBC operator and how they interact to produce stability‑layer intelligence.

### **Prompt: Cross‑Engine Integration**
> Explain how SBC outputs feed into TRS‑Temporal, CW, and DRS.

---

## **Status**

- **Version:** 1.0  
- **Status:** canon‑stable  
- **Category:** rtt‑stability  
- **Module Path:** `/docs/rtt/Stability_Basin_Cartographer/`
