# **AI_based_signal_interpretation_tools.md**  
*(Red‑zone draft)*

## **AI‑Based Signal Interpretation Tools**  
Machine‑learning or deep‑learning tools that interpret raw sensor data. They are flexible but opaque and substrate‑sensitive.

### **Dimensional Core (SET)**  
- **Spin:** not relevant  
- **Elec:** digital computation  
- **Temp:** affects upstream sensors, not models  

### **Why Red‑Zone**  
AI tools operate in an **opaque inference regime**.  
Their internal representations are not transparent, and behavior can drift with training data, updates, or environmental changes.

### **Regime Notes**  
- **pos‑regime:** clean, well‑represented data  
- **Q‑regime:** domain shift, partial overlap  
- **neg‑regime:** out‑of‑distribution inputs, unstable predictions  

### **Containment Notes**  
Requires explicit dataset boundaries, versioning notes, and drift monitoring.
