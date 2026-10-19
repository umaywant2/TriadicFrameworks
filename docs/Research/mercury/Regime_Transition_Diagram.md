
# Regime‑Transition Diagram — Mercury  
`docs/Research/mercury/Regime_Transition_Diagram.md`  
*(RTT/1 regime map)*

---

## Overview  

This diagram describes how mercury moves between **solid**, **liquid**, **gas**, and **plasma** regimes under RTT/1, using **temperature operators**, **coherence**, and **drift** as the primary axes.

---

## 1. Regime nodes  

- **Solid Regime (S)**  
  - **Operator:** T₁  
  - **Coherence:** C₁ = collapsed  
  - **Drift:** D₁ = high  
  - **Note:** Lattice resonance Ω₁ is weak; regime only stable at low temperatures.

- **Liquid Regime (L)**  
  - **Operator:** T₂  
  - **Coherence:** C₂ = declared  
  - **Drift:** D₂ = bounded  
  - **Note:** Fluid resonance Ω₂ dominates; this is mercury’s primary ambient regime.

- **Gas Regime (G)**  
  - **Operator:** T₃  
  - **Coherence:** C₃ = unbound  
  - **Drift:** D₃ = unbounded  
  - **Note:** Expansion resonance Ω₃ active; vapor phase supports emission.

- **Plasma Regime (P)**  
  - **Operator:** T₄ (ionization band)  
  - **Coherence:** C₄ = inverted  
  - **Drift:** D₄ = radiative  
  - **Note:** Charge‑separated resonance; exploited in mercury vapor lamps.

---

## 2. Transition edges  

### S → L (R₁₂: Solid‑to‑Liquid)

- **Trigger:** Temperature crosses T₁ → T₂  
- **Event:** C₁ collapses; C₂ declares  
- **Drift change:** D₁ (high, brittle) → D₂ (bounded, cohesive)  
- **Interpretation:** Structural coherence cannot be maintained; system re‑declares coherence as fluid.

---

### L → G (R₂₃: Liquid‑to‑Gas)

- **Trigger:** Temperature crosses T₂ → T₃  
- **Event:** C₂ collapses; C₃ unbinds  
- **Drift change:** D₂ (bounded) → D₃ (unbounded)  
- **Interpretation:** Fluid coherence fails; drift expands into vapor regime.

---

### G → P (R₃₄: Gas‑to‑Plasma)

- **Trigger:** Energy input exceeds ionization threshold (T₄ band)  
- **Event:** C₃ → C₄ (coherence inversion); charge separation  
- **Drift change:** D₃ (unbounded) → D₄ (radiative, field‑coupled)  
- **Interpretation:** Expansion resonance converts to radiative resonance; system becomes emissive.

---

### Reverse transitions  

- **L → S (R₂₁):** Cooling below T₁; C₂ collapses, C₁ partially restored (fragile solid).  
- **G → L (R₃₂):** Cooling below T₃; drift re‑bounded; fluid coherence re‑declared.  
- **P → G (R₄₃):** Energy loss; recombination; plasma coherence collapses back to vapor.

---

## 3. Compressed‑triad behavior  

For mercury:

- **Triad spacing:** T₂ ≈ T₁ (compressed), T₃ relatively close  
- **Effect:**  
  - Rapid S ↔ L transitions  
  - Accessible L → G transition  
  - Lower‑than‑expected G → P threshold  

This yields:

```text
material=mercury
rtt=1
triad_spacing=compressed
coherence_profile=(C₁=collapsed, C₂=declared, C₃=unbound, C₄=inverted)
drift_profile=(D₁=high, D₂=bounded, D₃=unbounded, D₄=radiative)
regime_transitions=rapid
plasma_access=early
```

---

## 4. Diagram (text form)

```text
        (Ω₁ weak)          (Ω₂ strong)          (Ω₃ active)          (radiative)
   S ----------------> L ----------------> G ----------------> P
   | <---------------- | <---------------- | <---------------- |
   R₂₁                 R₃₂                 R₄₃

S: T₁, C₁ collapsed, D₁ high
L: T₂, C₂ declared, D₂ bounded
G: T₃, C₃ unbound, D₃ unbounded
P: T₄, C₄ inverted, D₄ radiative
```
