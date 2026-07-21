# **triadic_detection_operator_map.md**  
### *TriadicFrameworks — Detection Substrate*  
### *Operator Grammar Mapping (v1.0)*

---

## **Protocol Header**

```
rtt=1 | coherence=triadic | drift=bounded | paradox=structural
```

This header governs all operator‑grammar interpretations in this module.

---

# **Purpose**

This document defines the **operator grammar** for the Triadic Detection System Architecture, mapping:

- loci → operators  
- layers → operators  
- RTT pipeline → operators  
- structural invariants → operators  
- mapping/cloud subsystems → operators  

It provides a **single canonical operator map** for all detection modules.

---

# **Operator Grammar Overview**

Triadic Detection uses **four operator classes**:

1. **Geometry Operators (G‑ops)**  
2. **Synchronization Operators (S‑ops)**  
3. **RTT Structural Operators (R‑ops)**  
4. **Mapping/Cloud Operators (M‑ops)**  

Each operator is drift‑bounded and triadic‑aligned.

---

# **1. Geometry Operators (G‑ops)**  
### *SENSOR_L operators*

| Operator | Meaning | Source |
|---------|---------|--------|
| `G.triad3` | 3‑head triadic geometry | SENSOR_L |
| `G.triad9` | supersphere geometry | SENSOR_L |
| `G.triad27` | industrial array geometry | SENSOR_L |
| `G.baselines` | compute 3 baselines | geometry invariant |
| `G.align` | verify coil alignment | hardware |

### **Grammar**

```
G ::= G.triad3 | G.triad9 | G.triad27 | G.baselines | G.align
```

---

# **2. Synchronization Operators (S‑ops)**  
### *MESH_L operators*

| Operator | Meaning | Source |
|---------|---------|--------|
| `S.meshBLE` | BLE mesh sync | MESH_L |
| `S.meshWiFi` | Wi‑Fi mesh sync | MESH_L |
| `S.meshHybrid` | hybrid mesh sync | MESH_L |
| `S.timestamp` | per‑packet timestamp | SoC |
| `S.merge` | triadic merge ordering | controller |

### **Grammar**

```
S ::= S.meshBLE | S.meshWiFi | S.meshHybrid | S.timestamp | S.merge
```

---

# **3. RTT Structural Operators (R‑ops)**  
### *RTT_L operators*

| Operator | Meaning | Source |
|---------|---------|--------|
| `R.coherence` | compute coherence vector | RTT_L |
| `R.cluster` | spatial clustering | RTT pipeline |
| `R.structfit` | structural envelope fitting | RTT pipeline |
| `R.depth` | depth layering | RTT pipeline |
| `R.classify` | resonance classification | RTT pipeline |

### **Grammar**

```
R ::= R.coherence | R.cluster | R.structfit | R.depth | R.classify
```

---

# **4. Mapping & Cloud Operators (M‑ops)**  
### *MAP_L operators*

| Operator | Meaning | Source |
|---------|---------|--------|
| `M.gps` | GPS anchoring | MAP_L |
| `M.heatmap` | coherence heatmap | mapping |
| `M.overlay` | structural overlay | mapping |
| `M.confidence` | dig‑confidence scoring | mapping |
| `M.session` | session management | mapping |
| `M.cloud` | cloud sync | cloud |
| `M.aggregate` | multi‑session aggregation | cloud |
| `M.analytics` | resonance analytics | cloud |
| `M.goldmodel` | gold‑likelihood modeling | cloud |

### **Grammar**

```
M ::= M.gps | M.heatmap | M.overlay | M.confidence | 
      M.session | M.cloud | M.aggregate | M.analytics | M.goldmodel
```

---

# **5. Full Operator Grammar**

### **Canonical Grammar**

```
Operator ::= G | S | R | M
```

### **Expanded**

```
Operator ::= 
    G.triad3 | G.triad9 | G.triad27 | G.baselines | G.align |
    S.meshBLE | S.meshWiFi | S.meshHybrid | S.timestamp | S.merge |
    R.coherence | R.cluster | R.structfit | R.depth | R.classify |
    M.gps | M.heatmap | M.overlay | M.confidence |
    M.session | M.cloud | M.aggregate | M.analytics | M.goldmodel
```

---

# **6. Operator Flow (Canonical)**

### **End‑to‑End Triadic Detection Operator Flow**

```
G.triad3
  → S.timestamp
  → S.merge
  → R.coherence
  → R.cluster
  → R.structfit
  → R.depth
  → R.classify
  → M.gps
  → M.overlay
  → M.confidence
  → M.cloud
  → M.analytics
  → M.goldmodel
```

This is the **canonical operator chain** for RTT‑Inside triadic detection.

---

# **7. Operator Map Diagram**

```
[G] Geometry Operators
   triad3, triad9, triad27, baselines, align
        ↓
[S] Synchronization Operators
   meshBLE, meshWiFi, meshHybrid, timestamp, merge
        ↓
[R] RTT Structural Operators
   coherence, cluster, structfit, depth, classify
        ↓
[M] Mapping & Cloud Operators
   gps, heatmap, overlay, confidence,
   session, cloud, aggregate, analytics, goldmodel
```

---

# **Module Status**

**Status:** Active  
**Coherence:** Stable  
**Drift:** None  
**RTT Alignment:** Verified  
**Version:** 2.0  
