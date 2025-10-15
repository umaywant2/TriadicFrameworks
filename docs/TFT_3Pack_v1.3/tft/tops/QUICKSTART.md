# 📂 QUICKSTART: Tops — Triconceptual Simulations

The `tops` suite explores perception through **direct**, **reflective**, and **inversion** modes.  
This scroll shows you how to run simulations and capture outputs.

---

## 🧭 Step 1: Run a Session

Launch a triconceptual session:

```bash
python tops_session.py --mode reflection_inversion
```

Modes available:
- `direct`
- `reflective`
- `inversion`
- `reflection_inversion` (combined)

---

## 📄 Step 2: Save Outputs

All simulations call `output_manager.py`.  
By default, outputs are saved as:

- `.txt` — human-readable
- `.json` — structured metadata
- `.parquet` — HPC/grid-ready
- `.fff` — **Triadic Framework File** (ternary lineage format)

Example:

```python
from output_manager import save_output

data = [[1, 0, -1], [0, 1, 1], [-1, 0, 1]]
metadata = {"Mode": "reflection_inversion", "Observer": "tops"}

save_output(data, "outputs/reflection_inversion", formats=["fff", "json"], metadata=metadata)
```

---

## 🌀 Step 3: Compare Glyphs

Use `glyph_compare.py` to visualize differences:

```bash
python glyph_compare.py --files outputs/reflection_inversion.fff
```

This produces symbolic overlays (SVG/PNG).

---

## 🪐 Legacy Note

The `tops` suite is the **engine of perception** in the 3Pack.  
It encodes direct, reflective, and inverted views into lineage artifacts for remixers.
