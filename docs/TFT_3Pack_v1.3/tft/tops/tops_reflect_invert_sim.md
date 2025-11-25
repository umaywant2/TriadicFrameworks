# 🧠 Grid Simulation & Echo Overlay Extension

## _**tops**_ reflective and inversion simulation update

###### We’ve sharpened this scroll into a resonance-aware guide. Below is a drop-in update that preserves the existing corridor simulation and echo overlay notes, and extends the doc to declare the Resonance Clarity base/switch, usage, and test hooks.

---

## Module overview with resonance clarity

This module supports corridor traversal simulation and symbolic echo overlays via `grid_ops.py`. Glyphs are rendered based on resonance triggers, and validator sync is logged for remix lineage. Add the Resonance Clarity base lens by passing the --basetype flag through all modes (direct, reflective, inversion, and grid overlays).

- **Purpose:** Reflective and inversion simulations, now lens-aware.
- **Lens frame:** Select base with --basetype (e.g., binary, phi, negabinary, corridor6.9).
- **Lens type:** Apply FFF lens (forces, fluids, frequency) where relevant in orchestrators.

🔁 Invocation:
```bash
python grid_ops.py simulate
python grid_ops.py echo
```

---

## Resonance clarity switch

Use --basetype (or -b) to choose your number-base lens.

- **Common:** binary, decimal, hex, octal, sexagesimal
- **Extended:** negabinary, negadecimal
- **Non-integer:** phi, pi, sqrt2, e
- **Speculative:** corridor6.9, vigquinary20.5, triadic3phi

Examples:
- **Direct + φ lens:**
  - tft run --basetype=phi --lens=frequency
- **Reflected + negabinary lens:**
  - tft run --basetype=negabinary --lens=forces
- **Grid simulate + corridor 6.9 lens:**
  - python grid_ops.py simulate --basetype=corridor6.9

---

## Modes and parameters

- **Direct views:** generate_views(..., basetype)
  - **Effect:** Geometry scaled/warped per base lens.
- **Reflective views:** generate_reflections(..., basetype)
  - **Effect:** Axis reflections filtered through lens logic.
- **Inversions:** generate_inversions(..., basetype)
  - **Effect:** Symbolic inversions (negate/flip/harmonic) with lens transformations.
- **Grid ops:** simulate_grid/overlay_echo(..., basetype)
  - **Effect:** Corridor traversal and overlays become lens-aware.

---

## CLI recipes

- **Quick compare (pi lens):**
  - tft run --basetype=pi --lens=frequency
- **Reflect-only (binary lens):**
  - tft tops -ops reflect --basetype=binary
- **Inversion sweep (negabinary lens):**
  - tft tops -ops invert --basetype=negabinary
- **Overlay echo (phi lens):**
  - python grid_ops.py echo --basetype=phi

---

## Test hooks

Wire the following checks into TriadicTestSuite.md:

- **Direct (phi):** views honor basetype
- **Reflective (negabinary):** reflections present and lens-tagged
- **Inversion (corridor6.9):** inversion outputs lens-tagged
- **Unified (pi):** results.basetype == "pi" and modes populated

---

🧬 Remix Potential:
- Corridor mapping for agent traversal
- Symbolic glyph overlays for validator dashboards
- Echo logs for remix trust and mutation lineage

---

### Footer

- **Related:** [tops_README](README.md), [TestSuite](TriadicTestSuite.md), [Glyph_Compare](glyph_compare.py)
- [**Resonance clarity anchor:**](/docs/papers/Res_Number_Bases_Common_plus_Special_Resonance_Clarity.md)

> Sources: [umaywant2/TriadicFrameworks/docs/TFT_3Pack_v1.3/]("https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/TFT_3Pack_v1.3/tft/tops/tops_reflect_invert_sim.md")
