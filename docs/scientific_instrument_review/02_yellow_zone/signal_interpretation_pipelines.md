# **signal_interpretation_pipelines.md**  
*(Yellow‑zone draft)*

## **Signal Interpretation Pipelines**  
Pipelines that convert raw sensor data into interpreted quantities (e.g., mass‑to‑charge, resonance frequency, field strength). They are powerful but inference‑dependent.

### **Dimensional Core (SET)**  
- **Spin:** relevant for magnetic or quantum systems  
- **Elec:** digital processing  
- **Temp:** affects drift and noise  

### **Why Yellow‑Zone**  
Interpretation pipelines introduce **multi‑stage inference**.  
Each stage (filtering, normalization, feature extraction) adds assumptions that influence the final output.

### **Regime Notes**  
- **pos‑regime:** clean signals, stable hardware  
- **Q‑regime:** mixed signals, partial overlap  
- **neg‑regime:** ambiguous data, unstable baselines  

### **Alignment Notes**  
Needs explicit notes on pipeline stages and assumption stacking.
