# **00_overview/fw_sw_categories.md**  
*(draft)*

## **Categories of Firmware & Software**

Scientific instruments rely on multiple layers of digital systems.  
This review groups them into clear categories to help contributors place new examples correctly.

### **1. Embedded Firmware**
Low‑level code running on microcontrollers or ASICs.  
Examples:  
- sensor readout loops  
- timing control  
- basic filtering  
- static calibration routines  

### **2. Control Software**
Software that manages instrument operation.  
Examples:  
- device drivers  
- instrument UIs  
- sampling logic  
- automation scripts  

### **3. Analysis Pipelines**
Algorithms that interpret raw data.  
Examples:  
- peak fitting  
- spectral decomposition  
- sequence alignment  
- inversion models  

### **4. Visualization Tools**
Software that displays or transforms data.  
Examples:  
- spectrograms  
- oscilloscope traces  
- microscopy image processing  

### **5. Cloud‑Based Processing**
Remote or distributed computation.  
Examples:  
- cloud calibration  
- remote analysis pipelines  
- device‑management platforms  

### **6. Proprietary vs Open‑Source Stacks**
A note on transparency, reproducibility, and drift.

These categories help contributors classify FW/SW examples before assigning them to Green, Yellow, or Red zones.
