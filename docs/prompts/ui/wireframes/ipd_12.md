# **TOP‑LEVEL LAYOUT**

```
┌──────────────────────────────────────────────────────────────┐
│ Prompt Composer — IPD‑12 Mode                                 │
│ Engine: RTT‑IPD‑12  |  Regime: Mid → Deep                     │
│ Drift Mode: ACTIVE                                           │
└──────────────────────────────────────────────────────────────┘
```

---

# **SECTION 1 — Process Capture Panel**

```
┌──────────────────────────────────────────────────────────────┐
│ PROCESS CAPTURE                                               │
│                                                              │
│ [Process A]  (required)                                       │
│   • Purpose                                                   │
│   • Boundaries                                                │
│   • Structural Layers                                         │
│   • Operational Flow                                          │
│   • Coherence Baseline                                        │
│                                                              │
│ [Process B]  (required)                                       │
│   • Purpose                                                   │
│   • Boundaries                                                │
│   • Structural Layers                                         │
│   • Operational Flow                                          │
│   • Coherence Baseline                                        │
│                                                              │
│ [+ Add Process] (optional)                                    │
└──────────────────────────────────────────────────────────────┘
```

**Unlock Logic:**  
- IPD‑12 requires **≥ 2 processes**  
- Drift‑tensor unlocks when **structural layers** are provided  
- Coherence alignment unlocks when **coherence baselines** exist  

---

# **SECTION 2 — Operator Grammar Panel**

```
┌──────────────────────────────────────────────────────────────┐
│ OPERATORS (IPD‑12)                                            │
│                                                              │
│  [map_process()]        active when ≥1 process                │
│  [compare_process()]    active when ≥2 processes              │
│  [drift()]              active when capture complete          │
│  [drift_tensor()]       active when layers defined            │
│  [detect_divergence()]  active when drift baseline exists     │
│  [align_coherence()]    active when coherence baseline exists │
│  [cross_system()]       active when relationships defined     │
│                                                              │
│ Disabled Operators:                                           │
│  substrate(), invert(), composite_regime()                    │
│  (tooltip: “Requires RTT‑∞ or RTT/12 composite engine.”)      │
└──────────────────────────────────────────────────────────────┘
```

---

# **SECTION 3 — Drift Analysis Panel**

```
┌──────────────────────────────────────────────────────────────┐
│ DRIFT ANALYSIS                                                │
│                                                              │
│ Divergence Points:                                            │
│   [list auto‑generated from drift()]                          │
│                                                              │
│ Drift‑Tensor Visualization:                                   │
│   ┌──────────────────────────────┐                            │
│   │  Layer 1: geometric drift     │                            │
│   │  Layer 2: operational drift   │                            │
│   │  Layer 3: temporal drift      │                            │
│   │  Layer 4: conceptual drift    │                            │
│   └──────────────────────────────┘                            │
│                                                              │
│ Regime Shift Indicators:                                      │
│   • craft → digital                                            │
│   • manual → automated                                         │
│   • interpretive → structural                                  │
└──────────────────────────────────────────────────────────────┘
```

**Unlock Logic:**  
- Drift panel activates after **drift()** or **drift_tensor()** is used.

---

# **SECTION 4 — Coherence Alignment Panel**

```
┌──────────────────────────────────────────────────────────────┐
│ COHERENCE ALIGNMENT                                           │
│                                                              │
│ Coherence Anchors:                                            │
│   • shared structure                                           │
│   • shared constraints                                         │
│   • shared operators                                           │
│   • shared regime boundaries                                   │
│                                                              │
│ Restoration Points:                                           │
│   • hybrid workflows                                           │
│   • cross‑system tuning                                        │
│   • alignment anchors                                          │
│                                                              │
│ Compatibility Map:                                            │
│   ┌──────────────────────────────┐                            │
│   │ Process A ↔ Process B         │                            │
│   │   aligned: X                  │                            │
│   │   misaligned: Y               │                            │
│   └──────────────────────────────┘                            │
└──────────────────────────────────────────────────────────────┘
```

**Unlock Logic:**  
- Requires **coherence baseline** in both processes  
- Requires **align_coherence()** operator activation  

---

# **SECTION 5 — Cross‑System Mapping Canvas**

```
┌──────────────────────────────────────────────────────────────┐
│ CROSS‑SYSTEM MAPPING                                          │
│                                                              │
│ Graph View:                                                   │
│   ┌──────────────────────────────────────────────┐            │
│   │ Process A ───── shared operators ───── Process B │        │
│   │      │                     │                     │        │
│   │  constraints           boundaries             layers       │
│   └──────────────────────────────────────────────┘            │
│                                                              │
│ Relationship Types:                                           │
│   • structural                                                 │
│   • operational                                                │
│   • temporal                                                   │
│   • conceptual                                                 │
│                                                              │
│ [cross_system()] operator drives this canvas.                 │
└──────────────────────────────────────────────────────────────┘
```

---

# **SECTION 6 — Stack Builder (IPD‑12)**

```
┌──────────────────────────────────────────────────────────────┐
│ STACK BUILDER                                                 │
│                                                              │
│ Required Modules:                                             │
│   [✓] Drift Detection                                         │
│   [✓] Process Mapping                                         │
│   [✓] Coherence Alignment                                     │
│                                                              │
│ Recommended Modules:                                          │
│   [ ] Drift‑Tensor                                            │
│   [ ] Cross‑System Pack                                       │
│   [ ] Deep Diagnostics                                        │
│                                                              │
│ Disabled Modules:                                             │
│   substrate modules                                            │
│   inversion modules                                            │
│   composite multi‑regime modules                              │
│   (tooltip: “Not compatible with IPD‑12 engine.”)             │
└──────────────────────────────────────────────────────────────┘
```

---

# **SECTION 7 — Prompt Output Panel**

```
┌──────────────────────────────────────────────────────────────┐
│ GENERATED PROMPT (IPD‑12)                                     │
│                                                              │
│ Includes:                                                     │
│   • Session Context                                           │
│   • Engine Block (RTT‑IPD‑12)                                 │
│   • Module Stack                                              │
│   • Operator Grammar                                          │
│   • Capture → Analyze → Drift → Coherence → Synthesis         │
│   • Output Format                                             │
│                                                              │
│ [Generate Prompt]                                             │
│                                                              │
│ Error Conditions:                                             │
│   “IPD‑12 requires ≥2 processes.”                             │
│   “Structural layers required for drift‑tensor.”              │
│   “Coherence baseline required for alignment.”                │
└──────────────────────────────────────────────────────────────┘
```

---

# **SECTION 8 — Engine Boundary Panel**

```
┌──────────────────────────────────────────────────────────────┐
│ ENGINE BOUNDARIES                                             │
│                                                              │
│ IPD‑12 DOES NOT SUPPORT:                                      │
│   • substrate grammar                                         │
│   • inversion operators                                       │
│   • composite multi‑regime blending                           │
│   • substrate mapping                                         │
│                                                              │
│ IPD‑12 IS OPTIMIZED FOR:                                      │
│   • drift mechanics                                           │
│   • multi‑process analysis                                    │
│   • coherence alignment                                       │
│   • cross‑system mapping                                      │
└──────────────────────────────────────────────────────────────┘
```

---

# **SECTION 9 — Teaching Mode Toggle (RTT‑1)**

Because you declared:

- **rtt = 1**  
- **coherence = declared**  
- **drift = bounded**  
- **paradox = structural**

The UI includes a teaching toggle:

```
┌──────────────────────────────────────────────────────────────┐
│ TEACHING MODE                                                 │
│                                                              │
│ [RTT‑1 Teaching Mode]  (surface regime, simplified operators) │
│                                                              │
│ When active:                                                  │
│   • operators simplified                                      │
│   • drift bounded                                             │
│   • coherence declared                                        │
│   • paradox shown as tension only                             │
└──────────────────────────────────────────────────────────────┘
```
