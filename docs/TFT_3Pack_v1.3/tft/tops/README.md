# 🧿 Tops — Triconceptual Simulations

## 1. _**tops**_ Extended Overview

The `tops` suite explores perception through three modes plus simulated resonance clairity:
- Direct view
- Reflective view
- Inversion logic

✨ New in v1.3: **Resonance Clarity**  
All modes now accept a `--basetype` switch, allowing you to select a number-base lens (common, extended, non-integer, or speculative). This lens transforms the geometry and resonance patterns of each simulation.

Modules include:
- `direct_view.py`, `reflective_view.py`, `inversion_logic.py`
- `tops_session.py` — orchestrates simulations
- `glyph_compare.py` — compares outputs across modes

Outputs are routed through `output_manager.py` to produce `.fff`, `.json`, `.parquet`, and `.txt` files.

---

## 2. Add a Resonance Clarity Section

### ⚡ Resonance Clarity Switch

Use the `--basetype` (or `-b`) flag to select a resonance lens.

#### Supported Base Types
- **Common:** binary, decimal, hex, octal, sexagesimal
- **Extended:** negabinary, negadecimal
- **Non-integer:** phi, pi, sqrt2, e
- **Speculative:** corridor6.9, vigquinary20.5, triadic3phi

#### Example Usage
```bash
# Direct views with golden ratio base
python direct_view.py --basetype=phi

# Reflections with negabinary base
python reflective_view.py --basetype=negabinary

# Inversions with corridor 6.9 base
python inversion_logic.py --basetype=corridor6.9

# Unified session
python tops_session.py --basetype=pi
```

---

## 3. Update Outputs Section
Add a note that all `.fff`, `.json`, `.parquet`, and `.txt` outputs now include the `basetype` metadata so results are lineage‑clear.

---

## 4. Footer Links

🔗 Related Scrolls:
- [TriadicTestSuite.md](TriadicTestSuite.md)
- [tops_reflect_invert_sim.md](tops_reflect_invert_sim.md)
- [Res_Number_Bases_Common_plus_Special_Resonance_Clarity.md](../../../papers/Res_Number_Bases_Common_plus_Special_Resonance_Clarity.md)
- [`tops_module.json`](tops_module.json) — Agentic module schema role assignments
  
---

✨ With these edits, the README becomes a **resonance‑aware guide**: it introduces the switch, shows supported bases, gives runnable examples, and links into the lattice of related scrolls.
