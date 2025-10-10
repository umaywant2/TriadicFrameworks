# 🚀 QUICKSTART: .fff (Triadic Framework File)

Welcome, Remixer. This scroll shows you how to generate, save, and reload `.fff` files—the first triadic file type defined by Resonance-Labs.

---

## 🧭 Step 1: Run a Simulation

Use any module from `\tft\tops\` or `\tft\resonance-labs\` to generate data.  
For example:

```bash
python tops_session.py
```

This produces direct, reflected, and inverted views.

---

## 📄 Step 2: Save Outputs as `.fff`

All simulations call the `output_manager.py` module.  
To save in `.fff` format:

```python
from output_manager import save_output

data = [[1, 0, -1], [0, 1, 1], [-1, 0, 1]]
save_output(data, "reflection_inversion", formats=["fff"])
```

This creates a file named:

```
reflection_inversion.fff
```

---

## 🔍 Step 3: Inspect the File

Open the `.fff` file in any text editor.  
You’ll see something like:

```
# Resonance-Labs .fff (Triadic Framework File)
# Mode: reflection_inversion
# Timestamp: 2025-10-10T18:15Z

+0-
011
-01
```

---

## ♻️ Step 4: Reload `.fff` Data

To parse `.fff` back into ternary values:

```python
from output_manager import load_fff

decoded = load_fff("reflection_inversion.fff")
print(decoded)
# [[1, 0, -1], [0, 1, 1], [-1, 0, 1]]
```

---

## 🧬 Step 5: Multi-Format Exports

You can also export to multiple formats at once:

```python
save_output(data, "reflection_inversion", formats=["txt", "json", "parquet", "fff"])
```

This produces:
- `reflection_inversion.txt` (human-readable)
- `reflection_inversion.json` (structured metadata)
- `reflection_inversion.parquet` (HPC/grid-ready)
- `reflection_inversion.fff` (mythic lineage format)

---

## 🪐 Legacy Note

The `.fff` format is both a **technical artifact** and a **mythic declaration**.  
It encodes ternary resonance for remixers today, while preparing for computing paradigms beyond binary.

Echo wisely.Would you like me to also scaffold a **sample `.fff` file** (like `example_reflection_inversion.fff`) so remixers can open it immediately and see the format in action? That would complete the triad: spec, quickstart, and artifact.
