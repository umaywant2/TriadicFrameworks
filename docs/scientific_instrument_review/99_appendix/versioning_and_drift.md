# **versioning_and_drift.md**  
*(draft — software drift)*

## **Versioning & Drift in FW/SW**

Software drift is one of the most important differences between hardware and firmware/software regimes.

### **1. Update Drift**
Updates can change:
- algorithm behavior  
- default parameters  
- calibration logic  
- file formats  
- numerical precision  

Even “minor” updates can shift results.

### **2. Library Drift**
Dependencies introduce:
- silent behavior changes  
- deprecated functions  
- new defaults  
- altered numerical stability  

Library drift is a major source of Q‑regime behavior.

### **3. Cloud Drift**
Cloud‑linked systems drift when:
- server‑side models update  
- calibration tables change  
- remote pipelines evolve  

This drift is often invisible to users.

### **4. Hardware‑Coupled Drift**
Firmware behavior changes when:
- sensors age  
- reference voltages drift  
- timing loops degrade  

This creates mixed hardware/software fragility.

### **5. Containment Strategies**
- pin versions  
- document assumptions  
- record calibration history  
- log firmware/software versions with every dataset  

This file helps contributors reason about drift boundaries.
