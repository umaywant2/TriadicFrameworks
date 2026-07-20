# **environmental_compensation_modules.md**  
*(Yellow‑zone draft)*

## **Environmental Compensation Modules**  
These modules correct for temperature, humidity, pressure, or vibration effects. They stabilize readings but rely on environmental models.

### **Dimensional Core (SET)**  
- **Spin:** not relevant  
- **Elec:** sensor readout  
- **Temp:** primary compensation axis  

### **Why Yellow‑Zone**  
Compensation modules are **assumption‑heavy**.  
They depend on environmental models that may not match real‑world conditions, creating mixed‑regime behavior.

### **Regime Notes**  
- **pos‑regime:** stable environment, accurate models  
- **Q‑regime:** partial compensation, drifting conditions  
- **neg‑regime:** rapid changes, model breakdown  

### **Alignment Notes**  
Needs explicit environmental boundaries and model‑validity notes.
