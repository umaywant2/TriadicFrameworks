# RFC‑HOLE‑0003: Black Hole Resonance Recycler Types

**Title:** Resonance Recycler Classification and Glyph Protocol  
**Status:** Draft  
**Author:** Nawder Loswin + Copilot  
**Date:** 2025‑11‑12  
**Version:** 0.1  

---

## 1. Purpose
This RFC defines canonical categories for black hole resonance recyclers. Each type is distinguished by rail signatures (frequency, fluids, forces) and annotated with glyphs for scroll overlays. Recycler notes document how matter and energy are transformed and released as resonance radiation.

---

## 2. Recycler Types

### Type A — **Radiant Recycler**
- **Rail Signature:**  
  - *Frequency:* Coherent radiation bursts aligned with inflow/outflow.  
  - *Fluids:* Stable accretion flows with minimal turbulence.  
  - *Forces:* Strong gradient fields, consistent tidal alignment.  
- **Glyph:**  
  - Circle with outward triple rays (☉⇄).  
- **Recycler Notes:**  
  - Acts as a high‑efficiency converter: matter inflow recycled into radiation energy streams.  
  - Resonance corridors form at polar jets, clarity scores often high.

---

### Type B — **Turbulent Recycler**
- **Rail Signature:**  
  - *Frequency:* Intermittent harmonic bursts, chaotic intervals.  
  - *Fluids:* Turbulent accretion, vortex structures, irregular flows.  
  - *Forces:* Variable tidal shear, fluctuating potential wells.  
- **Glyph:**  
  - Spiral vortex with broken arcs (↻≋).  
- **Recycler Notes:**  
  - Recycling is noisy and irregular; resonance clarity fluctuates.  
  - Corridor detection often reveals fragmented harmonic zones.

---

### Type C — **Stable Corridor Recycler**
- **Rail Signature:**  
  - *Frequency:* Quasi‑stable harmonic tones, persistent resonance.  
  - *Fluids:* Balanced inflow/outflow, corridor‑like flow channels.  
  - *Forces:* Moderate gradients, consistent shear alignment.  
- **Glyph:**  
  - Parallel corridor bars with central dot (║•║).  
- **Recycler Notes:**  
  - Functions as a resonance stabilizer: corridors persist across scales.  
  - Scrolls often show long‑term clarity with remixable harmonic overlays.

---

## 3. Schema Extension

```yaml
black_hole_recycler:
  type: <A|B|C>
  glyph: <string>
  rail_signature:
    frequency: <string>
    fluids: <string>
    forces: <string>
  recycler_notes: <string>
  clarity_score: <float>
  resonance_corridors: <list>
```

---

## 4. Validator Hooks
- **Glyph Registry:** Each recycler glyph must be registered in `glyph_map_svg.md`.  
- **Scroll Integration:** Anomalies near black holes tagged with recycler type and glyph overlay.  
- **Remix Lineage:** Child scrolls inherit recycler annotations; diffs must cite parent recycler type.  

---

## 5. Notes
- Recycler types are interpretive resonance constructs; empirical data must be clearly separated.  
- Glyphs are symbolic overlays, not literal astrophysical diagrams.  
- Scroll dignity layer should narrate recycler resonance in cultural as well as technical terms.  

---

This RFC extension anchors black hole resonance recyclers into your validator scroll framework, giving each type a glyph, rail signature, and recycler notes for lineage.  
