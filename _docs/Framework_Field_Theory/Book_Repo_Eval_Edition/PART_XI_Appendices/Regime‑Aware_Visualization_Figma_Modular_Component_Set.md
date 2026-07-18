# **Regime‑Aware Visualization — Figma Modular Component Set**  
### *A complete component architecture for assembling the full diagram inside Figma*

Below is the **canonical component hierarchy**, followed by **per‑component specifications**.

---

# **1. Component Hierarchy (Figma‑Ready)**

```
RegimeAwareVisualization/
│
├── 01_RegimeSpace_CI_FI/
│     ├── Axes
│     ├── RegimePoints
│     ├── TrajectoryCurve
│     └── Labels
│
├── 02_RegimeCards/
│     ├── StableCard
│     ├── TransitionalCard
│     ├── ParadoxCard
│     ├── InterferenceCard
│     └── CoherenceCard
│
├── 03_OperatorDominanceTable/
│     ├── HeaderRow
│     ├── OperatorRows
│     └── RegimeColumns
│
├── 04_TriadicTimeLayers/
│     ├── Layer_fast_tr
│     ├── Layer_medium_td
│     └── Layer_slow_ta
│
├── 05_DSET_Contribution/
│     ├── FormulaBlock
│     ├── ContributionBars
│     └── CombinedOverlay
│
├── 06_CompositeVisualizationTemplate/
│     ├── FieldLayer_phi
│     ├── FlowLayer_V
│     ├── CoherenceLayer_R
│     ├── DSETOverlay
│     ├── RegimeTint
│     ├── TransitionSurfaces
│     └── TriadicTimeMarkers
│
└── 07_RegimeLegend/
      ├── StableSwatch
      ├── TransitionalSwatch
      ├── ParadoxSwatch
      ├── InterferenceSwatch
      └── CoherenceSwatch
```

Each of these is a **standalone Figma component**, and the full diagram is simply an **Instance Composition** of them.

---

# **2. Component Specifications (Figma‑Modular)**

Below are the exact shapes, frames, and text blocks you’ll create in Figma.

---

## **01 — Regime Space (CI–FI Plane)**

### **Component: `RegimeSpace_CI_FI`**
**Frame size:** 900 × 520  
**Contents:**

- **Axes**
  - Horizontal FI axis (stroke 3px white)
  - Vertical CI axis (stroke 3px white)

- **Regime Points (5 components)**
  - `StablePoint` — circle, 20px, Deep Blue  
  - `TransitionalPoint` — circle, 20px, Amber  
  - `ParadoxPoint` — triangle, Crimson  
  - `InterferencePoint` — square, Violet  
  - `CoherencePoint` — star, Emerald  

- **Trajectory Curve**
  - Bezier curve, dashed 6/6, #888

- **Labels**
  - FI label (bottom right)
  - CI label (top left)

---

## **02 — Regime Cards**

Each card is a standalone component.

### **Component: `StableCard`**
**Frame:** 220 × 360  
**Color:** Deep Blue swatch  
**Text:**  
- “Stable”  
- “Low CI / Low FI / High S / Low α”

Repeat for:

- `TransitionalCard` (Amber)  
- `ParadoxCard` (Crimson)  
- `InterferenceCard` (Violet)  
- `CoherenceCard` (Emerald)

These become **variants** in a `RegimeCard` component set.

---

## **03 — Operator Dominance Table**

### **Component: `OperatorDominanceTable`**
**Frame:** 900 × 360  
**Subcomponents:**

- `OperatorRow` (5 variants: D, A, C, α, S)
- `RegimeColumn` (5 variants: Stable → Coherence)
- `DominanceCell` (text variants: ↑, ↓, ↑↑, ↓↓, ↕)

This table is built entirely from reusable text tokens.

---

## **04 — Triadic‑Time Layers**

### **Component: `TriadicTimeLayer`**
Variants:

- `fast_tr` — blue bar  
- `medium_td` — teal bar  
- `slow_ta` — brown bar  

Each bar is:

- 520 × 40  
- Rounded corners 8px  
- Label left‑aligned

---

## **05 — ΔSET Contribution**

### **Component: `DSET_FormulaBlock`**
Monospace text block containing:

```
ΔSET(x) = κ₁ R(x) + κ₂ |V(x)|² + κ₃ φ(x)
```

### **Component: `DSET_ContributionBars`**
Three bars:

- R contribution — Emerald  
- V contribution — Amber  
- φ contribution — Gray‑Blue  

### **Component: `DSET_CombinedOverlay`**
Stacked translucent rectangles:

- Emerald 35%  
- Amber 25%  
- Gray‑Blue 25%

---

## **06 — Composite Visualization Template**

This is the **most important Figma component**.

### **Component: `CompositeVisualization`**
**Frame:** 900 × 260  
**Layers (each a subcomponent):**

1. `FieldLayer_phi` — heatmap placeholder  
2. `FlowLayer_V` — arrow grid  
3. `CoherenceLayer_R` — contour lines  
4. `DSETOverlay` — semi‑transparent color layer  
5. `RegimeTint` — 20% opacity regime color  
6. `TransitionSurfaces` — curved white lines  
7. `TriadicTimeMarkers` — small labeled ticks

Each layer is toggleable via Figma’s **Boolean properties**.

---

## **07 — Regime Legend**

### **Component: `RegimeLegend`**
Contains:

- `StableSwatch` — Deep Blue  
- `TransitionalSwatch` — Amber  
- `ParadoxSwatch` — Crimson  
- `InterferenceSwatch` — Violet  
- `CoherenceSwatch` — Emerald  

Each swatch is a 40 × 20 rectangle with label.

---

# **3. Assembly Instructions (Figma)**

To build the full diagram:

1. Create a new frame: **2400 × 1600**  
2. Place components in this order:

```
[01_RegimeSpace_CI_FI]
[02_RegimeCards] (5‑column layout)
[03_OperatorDominanceTable]
[04_TriadicTimeLayers]
[05_DSET_Contribution]
[06_CompositeVisualizationTemplate]
[07_RegimeLegend]
```

3. Use **Auto‑Layout** for vertical stacking.  
4. Use **Component Instances**, not copies.  
5. Add **Variants** for dark/light mode if desired.
