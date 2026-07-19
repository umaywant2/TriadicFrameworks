# **real_time_filtering_firmware.md**  
*(Yellow‑zone draft)*

## **Real‑Time Filtering Firmware**  
Adaptive filters (e.g., Kalman, LMS) adjust their behavior based on incoming data. They stabilize signals but introduce assumption‑heavy dynamics.

### **Dimensional Core (SET)**  
- **Spin:** not relevant  
- **Elec:** digital filtering  
- **Temp:** minor influence on timing  

### **Why Yellow‑Zone**  
Adaptive filtering is **mixed‑regime** by nature.  
It blends direct measurement with prediction, and performance depends on noise models, tuning parameters, and environmental stability.

### **Regime Notes**  
- **pos‑regime:** stable noise characteristics  
- **Q‑regime:** drifting noise, changing dynamics  
- **neg‑regime:** unstable feedback, divergence  

### **Alignment Notes**  
Needs explicit notes on tuning parameters and noise‑model assumptions.
