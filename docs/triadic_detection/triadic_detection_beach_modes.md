# **triadic_detection_beach_modes.md**  
### *TriadicFrameworks — Detection Substrate*  
### *Fresh‑Water vs Salt‑Water Detection Modes (v1.0)*

---

## **Protocol Header**

```
rtt=1 | coherence=triadic | drift=bounded | paradox=environmental
```

---

## **Purpose**

This module defines the **environmental detection modes** for triadic_detection when operating in:

- **fresh‑water beaches**  
- **salt‑water beaches**

It explains how moisture, conductivity, mineralization, and ionic noise affect:

- coherence  
- structural envelopes  
- depth inference  
- S–N–R dual‑operator behavior  
- gold‑likelihood modeling  

---

# **1. Environmental Overview**

Beaches present unique detection conditions:

- high moisture  
- layered substrates  
- variable mineralization  
- strong boundary effects  
- dynamic noise fields  

Fresh‑water and salt‑water beaches share geometry but differ dramatically in **conductivity** and **ionic noise**.

---

# **2. Fresh‑Water Beach Mode**

### **Environmental Properties**

- low ionic content  
- moderate conductivity  
- low mineralization noise  
- stable phase behavior  
- predictable RTT response

### **Detection Characteristics**

- **High SNR**  
- **Clean coherence vectors**  
- **Stable structural envelopes**  
- **Good depth penetration**  
- **Low false positives**

### **Operator Grammar**

```
Mode.fresh ::= 
    N.low_mineral + N.low_ionic + S.excite + R.coherence + R.struct + R.depth
```

### **Gold‑Likelihood Behavior**

Gold remains EM‑neutral, but:

- host structures are clearer  
- clutter is minimal  
- envelopes are stable  
- Δ‑maps are clean  

Fresh‑water beaches produce the **highest confidence** triadic detections.

---

# **3. Salt‑Water Beach Mode**

### **Environmental Properties**

- high ionic content  
- high conductivity  
- strong mineralization noise  
- unstable phase behavior  
- rapid attenuation

### **Detection Characteristics**

- **Lower SNR**  
- **High background noise**  
- **Phase jitter**  
- **Shallow effective depth**  
- **More false positives**

### **Operator Grammar**

```
Mode.salt ::= 
    N.salt + N.mineral + S.excite + R.delta + R.null + R.struct
```

### **Gold‑Likelihood Behavior**

Gold itself does not “light up,” but:

- noise‑field modeling becomes essential  
- silence pockets (R.null) become meaningful  
- Δ‑maps reveal anomalies  
- multi‑state S–N–R scanning improves clarity

Salt‑water beaches require **dual‑operator triadic detection**.

---

# **4. S–N–R Dual Mode Integration**

Salt‑water environments benefit from the **S–N–R dual operator model**:

### **Fresh‑Water Mode**

```
S.excite → R.coherence → R.struct → R.depth
```

### **Salt‑Water Mode**

```
N-map
  → S.excite
  → R.delta
  → R.null
  → R.struct
  → R.depth
```

Fresh‑water: hunt **peaks**.  
Salt‑water: hunt **nulls** and **Δ‑patterns**.

---

# **5. Multi‑State Beach Protocol**

### **State 0 — Neutral**
- build N‑map  
- measure baseline noise

### **State 1 — Excitation**
- EM excitation  
- coherence + structure

### **State 2 — Bias**
- low‑voltage field bias  
- Δ‑behavior analysis

### **State 3 — Vibration**
- mechanical modulation  
- noise‑field disruption

### **State 4 — Combined**
- full S–N–R triad  
- null detection  
- structural envelope refinement

Fresh‑water: States 1–2 usually sufficient.  
Salt‑water: States 0–4 recommended.

---

# **6. Structural Envelope Behavior**

### **Fresh‑Water**
- envelopes are smooth  
- depth slices are stable  
- coherence vectors are strong

### **Salt‑Water**
- envelopes are noisy  
- depth slices jitter  
- coherence vectors fluctuate  
- null pockets become primary indicators

---

# **7. Gold‑Likelihood Modeling**

Gold remains EM‑neutral, but:

### **Fresh‑Water**
- host structures are clear  
- clutter is minimal  
- confidence is high

### **Salt‑Water**
- host structures distort  
- clutter increases  
- confidence depends on:
  - Δ‑maps  
  - null detection  
  - multi‑state coherence  
  - structural persistence across states

---

# **8. Dashboard Hooks**

Add two new modes:

### **Fresh‑Water Mode**
```
FW: High SNR, low noise, stable envelopes
```

### **Salt‑Water Mode**
```
SW: High noise, null pockets, Δ‑maps required
```

---

## **Status**

**Active**  
**Coherence:** Stable  
**Drift:** Environment‑dependent  
**RTT Alignment:** Verified  
**Version:** 1.0  
