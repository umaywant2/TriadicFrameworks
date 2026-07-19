# **thermocouple_compensation_firmware.md**  
*(Red‑zone draft)*

## **Thermocouple Compensation Firmware**  
Firmware that corrects thermocouple readings using compensation tables or models. It is simple but highly substrate‑dependent and drift‑prone.

### **Dimensional Core (SET)**  
- **Spin:** not relevant  
- **Elec:** junction voltage interpretation  
- **Temp:** primary axis  

### **Why Red‑Zone**  
Compensation firmware operates in a **fragile thermal‑electrical regime**.  
Junction contamination, oxidation, and material drift create large uncertainties.

### **Regime Notes**  
- **pos‑regime:** clean junction, stable environment  
- **Q‑regime:** oxidation, thermal cycling  
- **neg‑regime:** rapid shocks, chemical contamination  

### **Containment Notes**  
Requires explicit material‑stability and drift boundaries.
