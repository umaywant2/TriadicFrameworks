# **00_overview/method_fw_sw.md**  
*(draft)*

## **Method: How FW/SW Is Evaluated**

Firmware and software are evaluated using the same triadic principles as hardware instruments, with emphasis on:

### **1. Directness of Measurement**  
Does the FW/SW operate on raw signals, or does it infer hidden quantities?

### **2. Inference Layers**  
How many steps separate the raw data from the final output?  
Are these steps stable, transparent, or opaque?

### **3. Substrate Sensitivity**  
Does the FW/SW depend heavily on:  
- sample composition  
- environmental conditions  
- hardware quirks  
- versioning or patch levels  

### **4. Drift & Versioning**  
Does behavior change across:  
- firmware updates  
- library versions  
- calibration cycles  
- OS or driver changes  

### **5. Regime Behavior (pos / Q / neg)**  
- **pos‑regime:** stable algorithms, predictable outputs  
- **Q‑regime:** assumption‑heavy or adaptive behavior  
- **neg‑regime:** fragile, nonlinear, or unstable pipelines  

This method keeps the review coherent across hardware and software layers.
