# IPD‑12 Prime‑State SVG Icons
**Module:** IPD‑12 Framework  
**File:** /docs/frameworks/ipd_12/prime_state_icons.svg  
**Version:** 2026‑1.0  
**Role:** Visual / Dimensional / Operator Glyphs

---

## 1. Purpose

This file defines a **symbol‑based SVG sprite** for the 12 IPD‑12 prime states:

- One `<symbol>` per prime (`P2` … `P37`)
- Minimal, canon‑aligned geometric glyphs
- Encodes **Lift / Collapse / Neutral / Gate / Apex** via shape

You can reference each icon with:

```html
<svg class="ipd12-icon">
  <use href="#ipd12-P23" />
</svg>
```

---

## 2. Icon Design Language

- **Circle** → Neutral / Seed / Coherence / Gate / Boundary  
- **Up‑triangle** → Lift (+1D)  
- **Down‑triangle** → Collapse (−1D)  
- **Diamond** → Apex / Anomaly  
- **Stroke weight:** 2  
- **ViewBox:** `0 0 24 24`

---

## 3. SVG Sprite (copy as `prime_state_icons.svg`)

```svg
<svg xmlns="http://www.w3.org/2000/svg" style="display:none">

  <!-- P2 — Seed (Neutral) -->
  <symbol id="ipd12-P2" viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="6" fill="none" stroke="black" stroke-width="2" />
    <text x="12" y="20" font-size="5" text-anchor="middle">P2</text>
  </symbol>

  <!-- P3 — Transition Lift (+1D) -->
  <symbol id="ipd12-P3" viewBox="0 0 24 24">
    <polygon points="12,6 6,18 18,18" fill="none" stroke="black" stroke-width="2" />
    <text x="12" y="20" font-size="5" text-anchor="middle">P3</text>
  </symbol>

  <!-- P5 — Drift Collapse (−1D) -->
  <symbol id="ipd12-P5" viewBox="0 0 24 24">
    <polygon points="6,6 18,6 12,18" fill="none" stroke="black" stroke-width="2" />
    <text x="12" y="20" font-size="5" text-anchor="middle">P5</text>
  </symbol>

  <!-- P7 — Regime Lift (+1D) -->
  <symbol id="ipd12-P7" viewBox="0 0 24 24">
    <polygon points="12,4 5,18 19,18" fill="none" stroke="black" stroke-width="2" />
    <line x1="12" y1="4" x2="12" y2="1" stroke="black" stroke-width="2" />
    <text x="12" y="21" font-size="5" text-anchor="middle">P7</text>
  </symbol>

  <!-- P11 — Coherence (Neutral) -->
  <symbol id="ipd12-P11" viewBox="0 0 24 24">
    <circle cx="12" cy="12" r="7" fill="none" stroke="black" stroke-width="2" />
    <circle cx="12" cy="12" r="3" fill="none" stroke="black" stroke-width="2" />
    <text x="12" y="21" font-size="5" text-anchor="middle">P11</text>
  </symbol>

  <!-- P13 — Paradox Collapse (−1D) -->
  <symbol id="ipd12-P13" viewBox="0 0 24 24">
    <polygon points="5,7 19,7 12,19" fill="none" stroke="black" stroke-width="2" />
    <line x1="5" y1="7" x2="19" y2="7" stroke="black" stroke-width="2" />
    <text x="12" y="21" font-size="5" text-anchor="middle">P13</text>
  </symbol>

  <!-- P17 — Cycle Gate (Neutral) -->
  <symbol id="ipd12-P17" viewBox="0 0 24 24">
    <rect x="6" y="6" width="12" height="12" fill="none" stroke="black" stroke-width="2" />
    <line x1="10" y1="6" x2="10" y2="18" stroke="black" stroke-width="2" />
    <text x="12" y="21" font-size="5" text-anchor="middle">P17</text>
  </symbol>

  <!-- P19 — Boundary Node (Neutral) -->
  <symbol id="ipd12-P19" viewBox="0 0 24 24">
    <rect x="5" y="5" width="14" height="14" fill="none" stroke="black" stroke-width="2" />
    <line x1="5" y1="12" x2="19" y2="12" stroke="black" stroke-width="2" />
    <text x="12" y="21" font-size="5" text-anchor="middle">P19</text>
  </symbol>

  <!-- P23 — Dimensional Lift (+1D) -->
  <symbol id="ipd12-P23" viewBox="0 0 24 24">
    <polygon points="12,5 4,19 20,19" fill="none" stroke="black" stroke-width="2" />
    <circle cx="12" cy="9" r="2" fill="none" stroke="black" stroke-width="2" />
    <text x="12" y="21" font-size="5" text-anchor="middle">P23</text>
  </symbol>

  <!-- P29 — Collapse Anchor (−1D) -->
  <symbol id="ipd12-P29" viewBox="0 0 24 24">
    <polygon points="4,5 20,5 12,19" fill="none" stroke="black" stroke-width="2" />
    <circle cx="12" cy="15" r="2" fill="none" stroke="black" stroke-width="2" />
    <text x="12" y="21" font-size="5" text-anchor="middle">P29</text>
  </symbol>

  <!-- P31 — Stability Collapse (−1D) -->
  <symbol id="ipd12-P31" viewBox="0 0 24 24">
    <polygon points="6,6 18,6 18,18 6,18" fill="none" stroke="black" stroke-width="2" />
    <circle cx="12" cy="12" r="3" fill="none" stroke="black" stroke-width="2" />
    <text x="12" y="21" font-size="5" text-anchor="middle">P31</text>
  </symbol>

  <!-- P37 — Apex Lift (+1D, Apex) -->
  <symbol id="ipd12-P37" viewBox="0 0 24 24">
    <polygon points="12,4 4,12 12,20 20,12" fill="none" stroke="black" stroke-width="2" />
    <triangle />
    <polygon points="12,2 8,10 16,10" fill="none" stroke="black" stroke-width="2" />
    <text x="12" y="22" font-size="5" text-anchor="middle">P37</text>
  </symbol>

</svg>
```

---

## 4. Usage

Example in a markdown doc:

```html
<svg width="32" height="32">
  <use href="#ipd12-P7" />
</svg>
```

You can later refine stroke, color, or add CSS classes; this sprite is the **canonical ID and geometry layer** for IPD‑12 prime‑state icons.
