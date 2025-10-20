# 🚀 QUICKSTART: Tops — Triconceptual Simulations (Refreshed v1.3)

The **tops** suite explores perception through three modes:  
- **Direct** view  
- **Reflective** view  
- **Inversion** logic  

✨ New in v1.3: **Resonance Clarity**  
All modes now accept a `--basetype` switch, letting you select a number‑base lens (common, extended, non‑integer, or speculative). This lens transforms the geometry and resonance patterns of each simulation.

---

## 🧭 Step 1: Run a Session
Launch a triconceptual session with a chosen base lens:

```bash
# Reflection + inversion with golden ratio base
python tops_session.py --mode reflection_inversion --basetype=phi
```

**Modes available:**
- `direct`  
- `reflective`  
- `inversion`  
- `reflection_inversion` (combined)

---

## 📄 Step 2: Save Outputs
All simulations call `output_manager.py`. By default, outputs are saved as:

- `.txt` — human‑readable  
- `.json` — structured metadata  
- `.parquet` — HPC/grid‑ready  
- `.fff` — Triadic Framework File (ternary lineage format)  

Example:
```python
from output_manager import save_output

data = [[1, 0, -1], [0, 1, 1], [-1, 0, 1]]
metadata = {
    "Mode": "reflection_inversion",
    "Observer": "tops",
    "BaseLens": "phi"
}

save_output(data, "outputs/reflection_inversion", formats=["fff","json"], metadata=metadata)
```

---

## 🌀 Step 3: Compare Glyphs
Use `glyph_compare.py` to visualize differences across base lenses:

```bash
# Compare outputs with negabinary base
python glyph_compare.py --files outputs/reflection_inversion.fff --basetype=negabinary
```

This produces symbolic overlays (SVG/PNG) with the base lens declared in the title.

---

## ⚡ Resonance Clarity Switch

### Supported Base Types
- **Common:** binary, decimal, hex, octal, sexagesimal  
- **Extended:** negabinary, negadecimal  
- **Non‑integer:** phi, pi, sqrt2, e  
- **Speculative:** corridor6.9, vigquinary20.5, triadic3phi  

### Example Runs
```bash
# Direct views with binary base
python direct_view.py --basetype=binary

# Reflections with negabinary base
python reflective_view.py --basetype=negabinary

# Inversions with corridor6.9 base
python inversion_logic.py --basetype=corridor6.9
```

---

## 🪐 Legacy Note
The **tops** suite is the engine of perception in the 3Pack.  
It encodes direct, reflective, and inverted views into lineage artifacts for remixers.  
With Resonance Clarity, every artifact now declares its base lens, ensuring harmonic transparency.

---

✨ With this refresh, the Quickstart scroll now **teaches Resonance Clarity by example**—remixers can immediately run sessions, save outputs, and compare glyphs across different base lenses.
