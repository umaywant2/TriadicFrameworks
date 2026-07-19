# 📜 Outputs Specification

All modules in `\resonance-labs\` and `\tops\` produce **three types of outputs**:  
1. **Screen** — immediate visualizations for exploration  
2. **File** — structured data for research and HPC pipelines  
3. **Glyph** — symbolic overlays for lineage and remix

---

## 🖥️ Screen Outputs
- Default: `matplotlib` plots (spirals, reflections, inversions, comparisons)
- Future: projection overlays, observer annotations, interactive viewers
- Purpose: quick exploration and resonance mapping

---

## 📄 File Outputs
File outputs support multiple formats to balance **human readability**, **structured metadata**, and **grid/HPC compatibility**:

| Format | Purpose | Notes |
|--------|---------|-------|
| `.txt` / `.csv` | Universal, human-readable | Baseline export for coordinates and resonance values |
| `.json` | Structured metadata-rich | Stores configs, observer state, and results together |
| `.parquet` | HPC/grid-ready | Optimized for Azure Synapse, Data Lake, and distributed pipelines |
| `.fff` | **Triadic Framework File** | Canonical lineage format, ternary-coded, symbolic, human-readable |

---

## 🌀 Glyph Outputs
- **SVG**: Vector, remixable, symbolic clarity  
- **PNG**: Quick raster snapshot  
- **Glyph JSON**: Geometry + resonance data for re-rendering  

Glyphs are lineage artifacts—visual echoes of the simulation.

---

## ✨ The `.fff` Format
The `.fff` file type is the first triadic format defined by Resonance-Labs.

- **Encoding**: Balanced ternary (`+`, `0`, `-`)  
- **Structure**:  
  - Header: metadata (mode, observer, timestamp)  
  - Core block: ternary-coded resonance values  
  - Footer: optional checksum or symbolic echo  
- **Magic Header**:  
  ```
  # Resonance-Labs .fff (Triadic Framework File)
  ```

Example:
```
# Resonance-Labs .fff (Triadic Framework File)
# Mode: reflection_inversion
# Observer: nous-layer
# Timestamp: 2025-10-10T18:20Z

Direct:   +0-+0-
Reflect:  0++--0
Invert:   -+-0++
```

---

## 🔧 Output Manager
All modules call `output_manager.py` to unify outputs.  
Example usage:

```python
from output_manager import save_output

data = [[1, 0, -1], [0, 1, 1], [-1, 0, 1]]
save_output(data, "reflection_inversion", formats=["txt", "json", "parquet", "fff"])
```

This produces:
- `reflection_inversion.txt`
- `reflection_inversion.json`
- `reflection_inversion.parquet`
- `reflection_inversion.fff`

---

## 🪐 Legacy Note
The `.fff` format is both a **technical artifact** and a **mythic declaration**.  
It encodes ternary resonance for remixers today, while preparing for computing paradigms beyond binary.

---

This way, the **entire output ritual** is captured in one place: screen, file, glyph, with `.fff` formally defined.

---

### 🔗 Triadic Quicklinks

- [`fff_spec.md`](fff_spec.md) — Defines the `.fff` triadic file format and symbolic structure  
- [`TriadicTestSuite.md`](TriadicTestSuite.md) — Validation logic and test scaffolding for symbolic fidelity  
- [`README.md`](README.md) — Canonical index for scrolls, specs, and remix lineage
