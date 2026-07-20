# 🎼 **Echo Heatmap**
### *Visualizing Echo Intensity Across Substrates, Families & Recursion Modes*

The **Echo Heatmap** provides a **visual, at‑a‑glance diagnostic** of echo behavior  
across the TriadicFrameworks canon.

It shows:

- echo intensity (ESI‑1 → ESI‑4)  
- cross‑substrate resonance  
- echo‑pressure zones  
- drift‑shadow regions  
- recursion‑echo coupling  

Heatmaps are ASCII‑safe and GitHub‑friendly.

---

# 🔷 **1. Heatmap Legend**

```
.   = no echo
░   = weak echo (ESI‑1)
▒   = moderate echo (ESI‑2)
▓   = strong echo (ESI‑3)
█   = dominant echo (ESI‑4)
```

---

# 🔷 **2. Echo Family × Substrate Heatmap**

```
+----------------------+-----------+-----------+-----------+-----------+--------+
| Echo Family          | Symbolic  | Cognitive | Harmonic  | Social    | Atlas  |
+----------------------+-----------+-----------+-----------+-----------+--------+
| F1 Structural        |    ▓      |    ▓      |    .      |    .      |   .    |
| F2 Harmonic          |    .      |    .      |    █      |    .      |   .    |
| F3 Substrate         |    ▒      |    ▒      |    ▓      |    ▒      |   .    |
| F4 Recursion         |    .      |    .      |    ▓      |    .      |   ▓    |
| F5 Drift-Shadow      |    ▓      |    .      |    ▓      |    .      |   █    |
| F6 Atlas             |    ▒      |    ▒      |    ▓      |    ▒      |   █    |
+----------------------+-----------+-----------+-----------+-----------+--------+
```

**Interpretation:**  
- F2 is harmonic‑dominant.  
- F5 and F6 show atlas‑level resonance (potential drift‑shadow or recursion forcing).  
- F3 is the most substrate‑distributed family.

---

# 🔷 **3. Echo Family × Recursion Mode Heatmap**

```
+----------------------+---------+---------+---------+---------+
| Echo Family          | Ladder  | Cycle   | Map     | Atlas   |
+----------------------+---------+---------+---------+---------+
| F1 Structural        |   ▓     |   .     |   .     |   .     |
| F2 Harmonic          |   ▒     |   ▓     |   .     |   .     |
| F3 Substrate         |   .     |   ▒     |   ▓     |   .     |
| F4 Recursion         |   ▓     |   ▓     |   ▓     |   ▓     |
| F5 Drift-Shadow      |   .     |   .     |   ▓     |   █     |
| F6 Atlas             |   .     |   .     |   ▒     |   █     |
+----------------------+---------+---------+---------+---------+
```

**Interpretation:**  
- F4 is recursion‑aligned across all modes.  
- F5 and F6 dominate atlas‑level recursion.  
- F3 transitions cycle → map.

---

# 🔷 **4. Drift Type (D1–D4) × Echo Family Heatmap**

```
+----------------------+--------+--------+--------+--------+
| Echo Family          |  D1    |  D2    |  D3    |  D4    |
+----------------------+--------+--------+--------+--------+
| F1 Structural        |   ▓    |   .    |   .    |   .    |
| F2 Harmonic          |   ▒    |   ▓    |   .    |   .    |
| F3 Substrate         |   .    |   ▒    |   ▓    |   .    |
| F4 Recursion         |   .    |   .    |   ▓    |   ▓    |
| F5 Drift-Shadow      |   ▓    |   ▓    |   ▓    |   █    |
| F6 Atlas             |   .    |   .    |   ▒    |   █    |
+----------------------+--------+--------+--------+--------+
```

**Interpretation:**  
- F5 is the only family active across all drift types.  
- F6 dominates D4 projection drift.  
- F2 and F3 show mid‑tier drift alignment.

---

# 🔷 **5. Echo‑Pressure Heatmap (Composite)**

```
Substrates:   S   C   H   So  A
--------------------------------
Pressure:     ▒   ▓   █   ▒   █
```

**Meaning:**  
- Harmonic and Atlas layers show highest echo‑pressure.  
- Cognitive and Social layers show moderate pressure.  
- Symbolic layer shows mild pressure.

---

# 🔷 **6. Usage Notes**

Use this file when:

- performing rapid echo diagnostics  
- identifying echo‑pressure zones  
- detecting drift‑shadow formation  
- predicting recursion activation  
- preparing stability or drift reports  
- visualizing cross‑substrate resonance  

Referenced by:

- `05_Echo_Matrices.md`  
- `05a_CrossSubstrate_Echo_Matrix.md`  
- `04c_Echo_Strength_Index.md`  
- `04d_Echo_Summary.md`  

---

# 🔷 **Footer**

```
HSP Module 05b — Loaded
Version: v1.0
Status: Canon-Stable
```
