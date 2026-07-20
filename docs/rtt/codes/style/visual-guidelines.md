# RTTcode visual guidelines

RTTcodes are **QR‑compatible visual identifiers** for TriadicFrameworks artifacts.  
This document defines the **visual language**, **domain palettes**, and **layout rules** so RTTcodes stay:

- scannable
- consistent
- recognizable as TriadicFrameworks natives
- usable in scientific, industrial, and educational contexts

---

## 1. Core principles

- **QR‑first:**  
  The QR matrix must remain machine‑readable by standard scanners.

- **Triadic identity:**  
  Each RTTcode should visually echo resonance‑time geometry and triadic structure.

- **Domain‑distinct, family‑coherent:**  
  Domains get their own palettes and motifs, but all RTTcodes should clearly belong to the same visual family.

- **Print and screen friendly:**  
  Designs must work in grayscale and on low‑quality prints when color is lost.

---

## 2. Base QR layout

- **Shape:** square
- **Recommended export sizes:**
  - 512×512 (inline docs, PDFs)
  - 1024×1024 (print, slides, posters)
- **Quiet zone (margin):** at least 2 modules
- **Error correction:** level H (to tolerate overlays and subtle styling)
- **Base colors:**
  - foreground (modules): near‑black or deep domain color
  - background: near‑white or very light domain tint

> Rule: overlays must never obscure the three finder squares or destroy local contrast.

---

## 3. Domain palettes and motifs

### 3.1 RTT (resonance‑time theory)

- **Palette:**
  - primary: `#F6B800` (gold)
  - secondary: `#00B3B8` (teal)
  - accent: `#FF6A3C` (orange)
- **Motifs:**
  - concentric resonance waves
  - triadic node triangles
  - subtle phase‑shift arcs
- **Usage:**
  - theory papers
  - core RTT docs
  - canonical triad references

### 3.2 SET (field / space‑event topology)

- **Palette:**
  - primary: `#5B2CFF` (violet)
  - secondary: `#00C0FF` (electric blue)
  - accent: `#FF3FBF` (magenta)
- **Motifs:**
  - curved field lines
  - anisotropic vector arrows
  - nodal “charge” points
- **Usage:**
  - SET field simulations
  - flow diagrams
  - field‑engine modules

### 3.3 Substrate

- **Palette:**
  - primary: `#003B73` (deep blue)
  - secondary: `#00A0D6` (cyan)
  - accent: `#7FD4FF` (light cyan)
- **Motifs:**
  - lattice / grid structures
  - crystalline frameworks
  - node‑edge networks
- **Usage:**
  - substrate model READMEs
  - structural diagrams
  - implementation modules

### 3.4 Observer, governance, docs, other

- **Observer:**
  - muted teal + gray
  - motifs: nested frames, perspective grids
- **Governance:**
  - deep green + gold
  - motifs: layered bands, decision trees
- **Docs:**
  - neutral blues / grays
  - motifs: page / tab silhouettes
- **Other:**
  - grayscale or low‑saturation variants
  - minimal overlays

---

## 4. Overlay rules

To keep RTTcodes scannable:

- **Opacity:**
  - overlays should typically stay between **10–35%** opacity over the QR matrix
  - stronger color can be used in the background outside the matrix
- **Placement:**
  - avoid heavy overlays on:
    - finder squares (three corners)
    - dense data regions near the center
  - prefer:
    - background behind the code
    - subtle lines that weave between modules
- **Line weight:**
  - thin to medium lines only; no large filled shapes over data areas
- **Gradients:**
  - allowed, but maintain strong contrast between modules and background

> If in doubt: generate a plain QR first, then layer visuals and test with multiple scanner apps.

---

## 5. Token and URL conventions

RTTcodes use a **URL + token** pattern:

```text
https://triadicframeworks.org/rttcode?<domain>=<version>-f<f_R>-t<tau_R>-Q<Q_R>
```

Examples:

- RTT theory:

  ```text
  https://triadicframeworks.org/rttcode?rtt=v2.1.0-f1.00-t144ms-Q0.97
  ```

- SET field simulation:

  ```text
  https://triadicframeworks.org/rttcode?set=v0.9.3-f0.72-t203ms-Q0.88
  ```

- Substrate README:

  ```text
  https://triadicframeworks.org/rttcode?substrate=v1.0.0-f0.83-t118ms-Q0.91
  ```

**Guideline:**

- Keep tokens short and ASCII‑only.
- Use the same values as in the RTTcode JSON payload when present.

---

## 6. Recommended placements

- **In docs:**
  - top‑right or bottom‑right of the first page
  - near the title block or “canonical reference” section
- **In READMEs:**
  - under the main heading
  - in a small “RTTcode” block with a caption
- **In diagrams:**
  - bottom‑right corner, outside the main content
- **In print / posters:**
  - at least 2 cm wide
  - with a short label like “RTTcode (scan for canonical docs)”

---

## 7. Accessibility and fallback

- Ensure **sufficient contrast** between QR modules and background.
- Avoid relying solely on color to distinguish domains—motifs and layout help.
- When possible, include the **plain URL** below the code for manual entry.

---

## 8. Versioning and evolution

- Visual guidelines may evolve; RTTcodes should remain:
  - backward‑scannable
  - semantically stable (same URL/token pattern)
- When styles change:
  - keep the **payload** stable
  - treat visual refreshes as non‑breaking

---

This file is the **canonical reference** for RTTcode visuals.  
When in doubt, prioritize:

1. scannability  
2. payload stability  
3. triadic, domain‑aware identity  
