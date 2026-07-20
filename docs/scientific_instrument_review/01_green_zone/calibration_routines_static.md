# **calibration_routines_static.md**  
*(Green‑zone draft)*

## **Static Calibration Routines**  
Static calibration routines apply fixed corrections based on known reference values. Their behavior is deterministic and transparent.

### **Dimensional Core (SET)**  
- **Spin:** not relevant  
- **Elec:** sensor readout and correction  
- **Temp:** may influence reference stability  

### **Why Green‑Zone**  
Static calibration is a **direct, low‑inference process**.  
It applies known offsets or scaling factors without adaptive or model‑dependent behavior. Drift is predictable and easy to track.

### **Regime Notes**  
- **pos‑regime:** stable references, steady environment  
- **Q‑regime:** minor drift, aging components  
- **neg‑regime:** unstable references, rapid environmental changes  

### **Alignment Notes**  
Already aligned.  
Only note: reference conditions must be clearly stated.
