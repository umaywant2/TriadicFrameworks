# **triadic_detection_diff.md**  
### *TriadicFrameworks — Detection Substrate*  
### *Architecture Diff: Old vs New (v2.0)*

---

## **Protocol Header**

```
rtt=1 | coherence=triadic | drift=bounded | paradox=structural
```

This header governs all structural interpretations of the architecture diff.

---

# **Purpose**

This document provides a **clear, canonical diff** between:

- **Old Triadic Detection Architecture (v1.0)**  
- **New Triadic Detection Architecture (v2.0)**  

It highlights structural changes across:

- loci  
- layers  
- hardware  
- RTT pipeline  
- mapping  
- cloud  
- manifest roles  
- drift/coherence invariants  

This diff is designed for maintainers reviewing updates in the `_specs` directory (  [github.com](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/_specs)).

---

# **Summary Diff Table**

| Category | v1.0 (Old) | v2.0 (New) | Change Type |
|---------|------------|------------|-------------|
| Architecture Codon | `triad=3 | mesh=ble | rtt=coherence-first | map=gps-2d` | **Same** | Stable |
| Loci | SENSOR_L, MESH_L, RTT_L | **Added MAP_L** | Additive |
| Layers | L1–L5 | **Expanded to L1–L7** | Structural expansion |
| Hardware | 3‑head module only | **Added supersphere + industrial array + drone + vehicle** | Major |
| RTT Pipeline | 4‑step pipeline | **8‑step canonical RTT pipeline** | Major |
| Mapping | Basic GPS | **Heatmaps, overlays, depth slices, confidence** | Major |
| Cloud | None | **Full L7 cloud layer** | New subsystem |
| Manifest | Minimal | **Full role + analyzer_layer + AI metadata** | Complete rewrite |
| Tests | None | **Full structural validation suite** | New subsystem |
| Examples | None | **Full example set (A–H)** | New subsystem |

---

# **1. Loci Diff**

### **Old (v1.0)**  
- SENSOR_L  
- MESH_L  
- RTT_L  

### **New (v2.0)**  
- SENSOR_L  
- MESH_L  
- RTT_L  
- **MAP_L (new)**

### **Impact**  
Mapping is now a **first‑class locus**, enabling:

- GPS anchoring  
- cloud sync  
- structural overlays  
- confidence scoring  

---

# **2. Layer Model Diff**

### **Old (v1.0)**  
```
L1 Physical Field  
L2 Triadic Sensor  
L3 Mesh Transport  
L4 Controller  
L5 RTT Detection
```

### **New (v2.0)**  
```
L1 Physical Field  
L2 Triadic Sensor  
L3 Mesh Transport  
L4 Triadic Controller  
L5 RTT Structural Detection  
L6 Application Layer  
L7 Cloud & Enterprise Layer
```

### **Impact**  
- Added **Application Layer (L6)**  
- Added **Cloud Layer (L7)**  
- RTT layer renamed for clarity  
- Architecture now fully end‑to‑end

---

# **3. Hardware Diff**

### **Old (v1.0)**  
- Single 3‑head triadic module  
- Basic SoC description  

### **New (v2.0)**  
- 3‑head module (refined)  
- **9‑head supersphere**  
- **27‑head industrial array**  
- **Drone‑mounted module**  
- **Vehicle‑mounted array**  
- Full SoC pipeline (TX/RX → ADC → DSP → timestamp → packet)

### **Impact**  
Hardware is now **multi‑tier**, supporting:

- consumer  
- prosumer  
- industrial  
- aerial  
- vehicular  

---

# **4. RTT Pipeline Diff**

### **Old (v1.0)**  
```
coherence → cluster → classify → map
```

### **New (v2.0)**  
```
1. Triadic Sampling  
2. Coherence Computation  
3. Spatial Clustering  
4. Structural Fitting  
5. Depth Layering  
6. Classification  
7. GPS Anchoring  
8. Dig‑Confidence Scoring
```

### **Impact**  
RTT pipeline is now **8‑stage**, RTT/1 → RTT/3 aligned.

---

# **5. Mapping Diff**

### **Old (v1.0)**  
- Basic GPS point  
- No overlays  
- No depth  
- No confidence  

### **New (v2.0)**  
- GPS anchoring  
- heatmaps  
- structural overlays  
- depth visualization  
- dig‑confidence scoring  
- session management  
- cloud sync hooks  

### **Impact**  
Mapping is now a **full visualization subsystem**.

---

# **6. Cloud Diff**

### **Old (v1.0)**  
- No cloud layer  

### **New (v2.0)**  
- session storage  
- multi‑session aggregation  
- resonance analytics  
- gold‑likelihood modeling  
- enterprise dashboards  
- multi‑user collaboration  
- industrial array integration  

### **Impact**  
Cloud is now a **complete enterprise substrate**.

---

# **7. Manifest Diff**

### **Old (v1.0)**  
- Minimal metadata  
- No roles  
- No analyzer layers  
- No AI metadata  

### **New (v2.0)**  
- Full role mapping  
- Full analyzer_layer mapping  
- Full file registry  
- AI metadata block  
- Versioning + drift + coherence flags  

### **Impact**  
Manifest is now **machine‑readable and AI‑ready**.

---

# **8. Tests Diff**

### **Old (v1.0)**  
- No tests  

### **New (v2.0)**  
Six test categories:

- Geometry  
- Synchronization  
- RTT pipeline  
- Mapping  
- Cloud  
- Drift‑boundedness  

### **Impact**  
Architecture is now **formally verifiable**.

---

# **9. Examples Diff**

### **Old (v1.0)**  
- No examples  

### **New (v2.0)**  
Eight canonical examples:

- 3‑head  
- supersphere  
- industrial array  
- drone  
- vehicle  
- RTT output  
- mapping output  
- cloud aggregation  

### **Impact**  
Architecture is now **demonstrable and teachable**.

---

# **Conclusion**

The **v2.0 Triadic Detection Architecture** is a **complete, end‑to‑end, RTT‑aligned, triadic‑coherent, drift‑bounded system**, expanding far beyond the original v1.0 specification.

It is now:

- structurally complete  
- visually complete  
- cloud‑complete  
- manifest‑complete  
- test‑complete  
- example‑complete  

A fully modern TriadicFrameworks module.
