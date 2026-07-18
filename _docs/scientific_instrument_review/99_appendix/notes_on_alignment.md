# **notes_on_alignment.md**  
*(draft)*

## **Notes on Alignment**

This appendix collects short observations about how scientific instruments behave across regimes.  
These notes help contributors understand why an instrument lands in Green, Yellow, or Red.

### **1. Green‑Zone Patterns**
Instruments that land in Green typically show:

- a clear dimensional core  
- stable, substrate‑agnostic behavior  
- predictable response curves  
- minimal calibration drift  
- well‑defined operational envelopes  

Examples: accelerometer, interferometer, thermometer.

These tools already “speak” the language of coherence.

---

### **2. Yellow‑Zone Patterns**
Yellow instruments usually work well but reveal:

- hidden assumptions in their models  
- calibration practices that mask drift  
- mixed‑regime behavior  
- sensitivity to environmental or substrate changes  
- reliance on inference rather than direct measurement  

Examples: DNA sequencer, mass spectrometer, oscilloscope.

These tools benefit from RTT alignment and explicit regime boundaries.

---

### **3. Red‑Zone Patterns**
Red instruments are not unsafe — they are **regime‑fragile**.  
They often show:

- high substrate sensitivity  
- indirect or inference‑heavy measurement  
- unstable or narrow operational regimes  
- strong dependence on environmental conditions  
- ambiguous signals without coherence checks  

Examples: electrostatic analyzer, magnetic tweezers, thermocouple.

These tools require containment: clear context, careful interpretation, and explicit limits.

---

### **4. Why Alignment Matters**
Modern science uses powerful instruments, but often without acknowledging:

- regime shifts  
- substrate dependence  
- coherence loss  
- isotropic assumptions applied to anisotropic systems  

Alignment doesn’t replace existing knowledge — it **clarifies** it.

> **Everything students already know becomes easier to understand  
> when the regime is explicit and the dimensional core is respected.**
