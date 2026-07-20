# 🚀 QUICKSTART: `.fff` (Triadic Framework File)  
Welcome, Remixer. This scroll shows you how to generate, save, and reload `.fff` files—the first triadic file type defined by Resonance-Labs.

---

## 🧭 Step 1: Run a Simulation  
Use any module from `\tft\tops\` or `\tft\resonance-labs\` to generate data.  
Now with **Resonance Clarity**, you can declare a base lens:

```bash
python tops_session.py --mode=reflection_inversion --basetype=phi
```

This produces direct, reflected, and inverted views filtered through the golden ratio lens.

---

## 📄 Step 2: Save Outputs as `.fff`  
All simulations call `output_manager.py`. To save in `.fff` format:

```python
from output_manager import save_output

data = [[1, 0, -1], [0, 1, 1], [-1, 0, 1]]
metadata = {
    "Mode": "reflection_inversion",
    "BaseLens": "phi",
    "Timestamp": "2025-10-10T18:15Z"
}

save_output(data, "reflection_inversion", formats=["fff"], metadata=metadata)
```

This creates:

```text
reflection_inversion.fff
```

---

## 🔍 Step 3: Inspect the File  
Open the `.fff` file in any text editor. You’ll see:

```text
# Resonance-Labs .fff (Triadic Framework File)
# Mode: reflection_inversion
# BaseLens: phi
# Timestamp: 2025-10-10T18:15Z
+0- 011 -01
```

---

## ♻️ Step 4: Reload `.fff` Data  
To parse `.fff` back into ternary values:

```python
from output_manager import load_fff

decoded = load_fff("reflection_inversion.fff")
```

---

## ✨ Resonance Clarity Notes  
- Every `.fff` file now declares its **base lens** in metadata  
- Supported lenses: `binary`, `decimal`, `negabinary`, `phi`, `corridor6.9`, `triadic3phi`  
- This ensures remix lineage and symbolic fidelity across all scrolls
