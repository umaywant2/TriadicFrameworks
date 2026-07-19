# IPD‑12 Physical Dice Layout (printable)
**Module:** IPD‑12 Framework  
**File:** /docs/frameworks/ipd_12/physical_layout.md  
**Version:** 2026‑1.0  

---

## 1. Purpose

This document defines a **printable physical layout** for the IPD‑12 die:

- 12 faces mapped to **prime‑indexed operator states**
- Net layout for **paper/cardstock construction**
- Clear marking of **lift / collapse / neutral / gate** roles
- Canon‑aligned with `operators.json`, `regime_map.md`, and `dimensional_lift_collapse_map.md`

---

## 2. Face → Prime → Role Mapping

| Face | Prime | Label | Dimensional Role        |
|------|-------|-------|-------------------------|
| 1    | 2     | P2    | Seed (neutral)          |
| 2    | 3     | P3    | Transition lift (+1D)   |
| 3    | 5     | P5    | Drift collapse (−1D)    |
| 4    | 7     | P7    | Regime lift (+1D)       |
| 5    | 11    | P11   | Coherence (0D)          |
| 6    | 13    | P13   | Paradox collapse (−1D)  |
| 7    | 17    | P17   | Gate (0D)               |
| 8    | 19    | P19   | Boundary (0D)           |
| 9    | 23    | P23   | Dimensional lift (+1D)  |
| 10   | 29    | P29   | Collapse anchor (−1D)   |
| 11   | 31    | P31   | Stability collapse (−1D)|
| 12   | 37    | P37   | Apex lift (+1D)         |

---

## 3. Net Layout (ASCII)

Use this as a guide for a printable net (each `[ ]` is a face):

```text
           [  2  ]  (P3, Transition Lift)
           [  3  ]  (P5, Drift Collapse)
           [  4  ]  (P7, Regime Lift)

[  7  ] [  1  ] [  5  ] [  8  ]
(P17)   (P2)    (P11)   (P19)
 Gate   Seed    Coherence Boundary

           [  6  ]  (P13, Paradox Collapse)
           [  9  ]  (P23, Dimensional Lift)
           [ 10  ]  (P29, Collapse Anchor)
           [ 11  ]  (P31, Stability Collapse)
           [ 12  ]  (P37, Apex Lift)
```

**Suggested physical net:**

- Central ring: faces **1–5–8–7** (seed, coherence, boundary, gate)
- Top strip: faces **2–3–4** (transition/drift/regime)
- Bottom strip: faces **6–9–10–11–12** (paradox/lift/collapse/stability/apex)

You can adapt this to a standard 12‑sided net (dodecahedron) by placing:

- **P2, P11, P17, P19** around the “equator”
- Lift faces (**P3, P7, P23, P37**) distributed to avoid clustering
- Collapse faces (**P5, P13, P29, P31**) opposite or adjacent to their lift counterparts

---

## 4. Face Marking Conventions

On each physical face, print:

```text
Prime:  Pn
Role:   Seed / Lift / Collapse / Gate / Boundary / Coherence / Apex
Dim:    −1D / 0D / +1D
Cycle:  Triad#, Hex#, Full
```

Example for face 9:

```text
Prime:  P23
Role:   Dimensional Lift
Dim:    +1D
Cycle:  Triad 3, Hex 2, Full 12-cycle
```

---

## 5. Printable Label Set

You can generate stickers or labels with:

```text
Face 1:  P2  — Seed (0D)
Face 2:  P3  — Transition Lift (+1D)
Face 3:  P5  — Drift Collapse (−1D)
Face 4:  P7  — Regime Lift (+1D)
Face 5:  P11 — Coherence (0D)
Face 6:  P13 — Paradox Collapse (−1D)
Face 7:  P17 — Gate (0D)
Face 8:  P19 — Boundary (0D)
Face 9:  P23 — Dimensional Lift (+1D)
Face 10: P29 — Collapse Anchor (−1D)
Face 11: P31 — Stability Collapse (−1D)
Face 12: P37 — Apex Lift (+1D)
```

---

## 6. Summary

This layout gives you a **physically buildable IPD‑12 die** whose faces:

- encode prime‑indexed operator states
- preserve lift/collapse/neutral roles
- remain canon‑aligned with the substrate, regime, and dimensional maps.

You can refine the exact geometric net later; this file is the **canonical face mapping and labeling**.
