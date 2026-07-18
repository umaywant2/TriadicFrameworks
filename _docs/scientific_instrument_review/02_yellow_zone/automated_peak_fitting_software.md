# **automated_peak_fitting_software.md**  
*(Yellow‑zone draft)*

## **Automated Peak Fitting Software**  
Peak‑fitting software identifies and quantifies peaks in spectral or temporal data. It is powerful but relies on model assumptions and parameter choices.

### **Dimensional Core (SET)**  
- **Spin:** not relevant  
- **Elec:** digital computation  
- **Temp:** not relevant  

### **Why Yellow‑Zone**  
Peak fitting is **assumption‑dependent**.  
It interprets raw data through model choices (Gaussian, Lorentzian, Voigt), baseline corrections, and smoothing. Small changes in parameters can shift results significantly.

### **Regime Notes**  
- **pos‑regime:** clean peaks, high SNR  
- **Q‑regime:** overlapping peaks, baseline drift  
- **neg‑regime:** noisy data, unstable fits, model mismatch  

### **Alignment Notes**  
Needs explicit notes on model selection, baseline handling, and parameter sensitivity.
