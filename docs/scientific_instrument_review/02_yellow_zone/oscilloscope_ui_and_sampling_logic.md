# **oscilloscope_ui_and_sampling_logic.md**  
*(Yellow‑zone draft)*

## **Oscilloscope UI & Sampling Logic**  
Oscilloscope software manages sampling, triggering, visualization, and measurement extraction. It is stable but sensitive to sampling assumptions.

### **Dimensional Core (SET)**  
- **Spin:** not relevant  
- **Elec:** primary axis  
- **Temp:** affects noise and drift  

### **Why Yellow‑Zone**  
Oscilloscope software relies on **sampling and grounding assumptions**.  
Aliasing, probe loading, and trigger logic introduce mixed‑regime behavior.

### **Regime Notes**  
- **pos‑regime:** clean signals, proper grounding  
- **Q‑regime:** noise, jitter, aliasing  
- **neg‑regime:** unstable references, saturation  

### **Alignment Notes**  
Needs explicit sampling‑rate, grounding, and bandwidth boundaries.
