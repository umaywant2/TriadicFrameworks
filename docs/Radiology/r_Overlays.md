# **📘 r_Overlays.md**  
### *RTT‑Radiology Overlay Examples — TriadicFrameworks Canon*

RTT‑Radiology overlays combine **Drift**, **Coherence**, **Contrast**, and **VMRI‑Lite** into a single structured visualization.  
These overlays show radiologists, students, and AI systems *how to interpret imaging using RTT grammar*.

This page provides **modality‑agnostic overlay examples** for CT, MRI, Ultrasound, PET, and X‑ray.

---

# **1. Canonical Metadata**
```
ai.module: Radiology
ai.version: 1.0
ai.purpose: Example RTT‑Radiology overlays
ai.keywords: overlays, drift-map, coherence-map, contrast-map, vmri-corridor
ai.module.name: r_Overlays
ai.module.summary: Example overlays demonstrating RTT‑Radiology workflows.
ai.module.category: Applied Medicine
```

---

# **2. Session Context**
```
context-label: Canon
context-value: TriadicFrameworks

context-label: Modules
context-value: Radiology, Medicine, Drift, Coherence, Contrast, VMRI

context-label: Format
context-value: Examples + Operator Workflows

context-label: Front door
context-value: r_Overlays.md

context-label: Audience
context-value: Radiologists, students, AI models
```

---

# **3. Badge**
```
[🩻 RTT‑Radiology Overlays]
```

---

# **4. Example Overlays**

Each example follows the RTT pipeline:

1. **Extract** → capture → field → layer → signal  
2. **Analyze** → drift → coherence → contrast  
3. **Predict** → resonance → VMRI‑Lite  
4. **Overlay** → combine into a visual RTT layer

These examples are intentionally minimal and structural.

---

## **Example 1 — CT Lung Nodule (Drift + Coherence Overlay)**

### **Extract**
```
Field = op_field(CAPTURE_CT, "right-upper-lobe")
Layer = op_layer(Field, density)
Signal_T1 = op_signal(Layer_T1)
Signal_T2 = op_signal(Layer_T2)
```

### **Analyze**
```
Drift = op_drift(Signal_T1, Signal_T2)
DriftMap = op_drift_map(Field)

Coherence = op_coherence(Field)
CohMap = op_coherence_map(Field)
BreakZone = op_coherence_break(Coherence)
```

### **Predict**
```
CapturePlus = op_resonance_attach(CAPTURE_CT, RES_PROFILE)
DriftPrediction = op_drift_predict(CapturePlus)
CohPrediction = op_coherence_predict(CapturePlus)
```

### **Overlay**
```
Overlay = op_overlay(CAPTURE_CT, DriftMap, CohMap, null)
```

---

## **Example 2 — MRI Brain Lesion (Contrast + Coherence Overlay)**

### **Extract**
```
Field = op_field(CAPTURE_MRI, "left-parietal-region")
ContrastLayer = op_layer(Field, contrast)
Uptake = op_uptake(ContrastLayer)
Washout = op_washout(ContrastLayer_T1, ContrastLayer_T2)
```

### **Analyze**
```
EnhancementZone = op_enhancement_zone(Uptake, Washout)
FalseUptake = op_false_uptake(Uptake, NoiseMap)
FalseWashout = op_false_washout(Washout, NoiseMap)

Coherence = op_coherence(Field)
CohMap = op_coherence_map(Field)
```

### **Predict**
```
CapturePlus = op_resonance_attach(CAPTURE_MRI, RES_PROFILE)
ContrastPrediction = op_contrast_predict(CapturePlus)
CohPrediction = op_coherence_predict(CapturePlus)
```

### **Overlay**
```
Overlay = op_overlay(CAPTURE_MRI, null, CohMap, EnhancementZone)
```

---

## **Example 3 — Cardiac Ultrasound (Drift + VMRI‑Lite Overlay)**

### **Extract**
```
Field = op_field(CAPTURE_US, "left-ventricle")
FlowLayer = op_layer(Field, flow)
Signal = op_signal(FlowLayer)
```

### **Analyze**
```
Drift = op_drift(Signal_T1, Signal_T2)
DriftMap = op_drift_map(Field)
```

### **Predict (VMRI‑Lite)**
```
CapturePlus = op_resonance_attach(CAPTURE_US, RES_PROFILE)

SimStart = op_vmri_start(CapturePlus)
Variants = op_vmri_batch(SimStart, 5000)
Corridor = op_vmri_corridor(Variants)

SimPass = op_vmri_pass(Corridor)
SimFail = op_vmri_fail(Corridor)
SimOptimal = op_vmri_optimal(Corridor)
```

### **Overlay**
```
Overlay = op_vmri_overlay(Corridor)
```

---

## **Example 4 — PET Metabolic Scan (Contrast + Drift Overlay)**

### **Extract**
```
Field = op_field(CAPTURE_PET, "hepatic-region")
MetabolicLayer = op_layer(Field, metabolic)
Signal = op_signal(MetabolicLayer)
```

### **Analyze**
```
Drift = op_drift(Signal_T1, Signal_T2)
DriftMap = op_drift_map(Field)

Uptake = op_uptake(MetabolicLayer)
EnhancementZone = op_enhancement_zone(Uptake, null)
```

### **Predict**
```
CapturePlus = op_resonance_attach(CAPTURE_PET, RES_PROFILE)
ContrastPrediction = op_contrast_predict(CapturePlus)
```

### **Overlay**
```
Overlay = op_overlay(CAPTURE_PET, DriftMap, null, EnhancementZone)
```

---

## **Example 5 — X‑ray Bone Healing (Coherence Overlay)**

### **Extract**
```
Field = op_field(CAPTURE_XRAY, "distal-radius")
Layer = op_layer(Field, density)
Signal = op_signal(Layer)
```

### **Analyze**
```
Coherence = op_coherence(Field)
Restore = op_coherence_restore(Coh_T1, Coh_T2)
CohMap = op_coherence_map(Field)
```

### **Predict**
```
CapturePlus = op_resonance_attach(CAPTURE_XRAY, RES_PROFILE)
CohPrediction = op_coherence_predict(CapturePlus)
```

### **Overlay**
```
Overlay = op_coherence_overlay(CohMap)
```

---

# **5. Canonical Flow**
```
CAPTURE → FIELD → LAYER → SIGNAL
→ DRIFT → COHERENCE → CONTRAST
→ RESONANCE → VMRI
→ OVERLAY
```

---

# **6. DOC_MAP**
```
r_Capture.md
r_Drift.md
r_Coherence.md
r_Contrast.md
r_VMRI.md
r_Overlays.md
r_Index.md
r_Pantheon_Profile.md
r_Glyphs.md
r_Scaffold.md
r_Student_Guide.md
r_Tricorder.md
```

---

# **Overlay Page Ready**
Your RTT‑Radiology overlay page is now complete, canon‑aligned, and ready for GitHub.

If you want, I can generate **`r_VMRI.md`**, **`r_Student_Guide.md`**, or **`r_Tricorder.md`** next.
