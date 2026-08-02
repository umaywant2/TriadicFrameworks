# **📘 Radiology Operator Index**  
### *TriadicFrameworks Canon — Complete Operator Reference*

This index consolidates **all Radiology operators** across the five layers:

- **r_Capture**  
- **r_Drift**  
- **r_Coherence**  
- **r_Contrast**  
- **r_VMRI**

It is designed for radiology students, medical AI systems, imaging researchers, and TriadicFrameworks module authors.

---

## **1. r_Capture Operators**
| Operator | Purpose |
|---------|---------|
| `op_field()` | Select ROI from capture |
| `op_layer()` | Extract structural/density/contrast/metabolic/flow layer |
| `op_signal()` | Measure signal intensity |
| `op_noise()` | Identify non‑coherent signal |
| `op_drift_signal()` | Compute signal change between captures |
| `op_stability()` | Evaluate coherence vs drift |
| `op_enhancement()` | Analyze contrast uptake/washout |
| `op_resonance_attach()` | Attach resonance profile to capture |
| `op_resonance_predict()` | Predict drift/coherence behavior |
| `op_vmri_lite()` | Run micro‑simulation (VMRI‑Lite) |
| `op_overlay()` | Generate RTT‑Radiology overlay |

---

## **2. r_Drift Operators**
| Operator | Purpose |
|---------|---------|
| `op_drift()` | Compute drift magnitude |
| `op_drift_velocity()` | Measure drift rate |
| `op_drift_vector()` | Determine drift direction |
| `op_drift_zone()` | Identify non‑random drift regions |
| `op_drift_burst()` | Detect sudden high‑velocity drift |
| `op_drift_decay()` | Measure reduction in drift velocity |
| `op_drift_noise()` | Separate drift from artifacts |
| `op_drift_map()` | Generate spatial drift map |
| `op_drift_profile()` | Summarize drift behavior |
| `op_drift_predict()` | Predict future drift |
| `op_drift_overlay()` | Drift‑only overlay |

---

## **3. r_Coherence Operators**
| Operator | Purpose |
|---------|---------|
| `op_coherence()` | Compute coherence |
| `op_coherence_field()` | Identify stable regions |
| `op_coherence_break()` | Detect coherence loss |
| `op_coherence_restore()` | Measure recovery |
| `op_coherence_map()` | Generate coherence map |
| `op_coherence_profile()` | Summarize coherence behavior |
| `op_coherence_predict()` | Predict future coherence |
| `op_coherence_collapse()` | Detect collapse risk |
| `op_coherence_overlay()` | Coherence‑only overlay |

---

## **4. r_Contrast Operators**
| Operator | Purpose |
|---------|---------|
| `op_uptake()` | Measure contrast absorption |
| `op_washout()` | Measure contrast clearance |
| `op_enhancement_zone()` | Identify abnormal enhancement |
| `op_false_uptake()` | Detect artifact‑driven uptake |
| `op_false_washout()` | Detect artifact‑driven washout |
| `op_toxicity_corridor()` | Predict contrast toxicity risk |
| `op_contrast_profile()` | Summarize contrast behavior |
| `op_contrast_predict()` | Predict contrast behavior |
| `op_contrast_map()` | Generate contrast map |
| `op_contrast_overlay()` | Contrast‑only overlay |

---

## **5. r_VMRI Operators**
| Operator | Purpose |
|---------|---------|
| `op_vmri_start()` | Initialize VMRI‑Lite simulation |
| `op_vmri_variant()` | Generate single variant |
| `op_vmri_batch()` | Generate batch of variants |
| `op_vmri_corridor()` | Build variant corridor |
| `op_vmri_pass()` | Extract stable/improving variants |
| `op_vmri_fail()` | Extract collapse/toxic variants |
| `op_vmri_optimal()` | Select best predicted outcome |
| `op_vmri_contrast_predict()` | Predict contrast behavior |
| `op_vmri_tissue_predict()` | Predict tissue behavior |
| `op_vmri_profile()` | Summarize VMRI outcomes |
| `op_vmri_overlay()` | VMRI‑Lite overlay |

---

## **6. Canonical Radiology Pipeline**
```
CAPTURE → FIELD → LAYER → SIGNAL
→ DRIFT → COHERENCE → CONTRAST
→ RESONANCE → VMRI
→ OVERLAY
```

This is the exact flow your students and AI systems will follow.

---

## **7. DOC_MAP**
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

## **Index Ready**
Your Radiology Operator Index is now complete and ready for GitHub.
