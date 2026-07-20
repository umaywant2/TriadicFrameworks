# 🎨 **1. Glyph‑Assignment Logic (RTT‑Aligned Minimal Edition)**

This logic assigns glyphs based on **phase**, **substrate**, and **resonance corridor**.  
It mirrors the clarity of your phase ladder and keeps the system drift‑free.

## **Conceptual Rules**

### **Rule 1 — Phase Determines Glyph Family**
Each phase has a canonical glyph family:

| Phase | Symbol | Glyph Family |
|-------|--------|--------------|
| I | ⚛️ | Atom / Quantum / Blue |
| II | 🧬 | DNA / Biological / Green |
| III | 🍃 | Leaf / Ecological / Teal |
| IV | ⛰️ | Mountain / Geological / Brown |
| V | 📜 | Scroll / Mythic / Purple |
| VI | ⭐ | Star / Cosmic / Gold |

This ensures **visual coherence** across the Atlas.

---

### **Rule 2 — Substrate Determines Glyph Variant**
Within each family, the substrate selects the variant:

Examples:

- **molecular vibration → Blue Atom**  
- **neural oscillation → Green Neuron**  
- **seasonal cycle → Teal Spiral**  
- **seismic resonance → Brown Faultline**  
- **civilizational cycle → Purple Epoch**  
- **stellar spectrum → Gold Radiant Star**

Variants are optional but help scanners and overlays.

---

### **Rule 3 — Drift Flags Modify Glyph**
If drift is detected:

- **minor drift → add hollow outline**  
- **moderate drift → add dashed outline**  
- **severe drift → add red overlay glyph**  

This gives instant visual feedback.

---

## **Minimal Code Version**

```python
def assign_glyph(symbol, substrate=None, drift=None):
    base = {
        "⚛️": "Blue Atom",
        "🧬": "Green DNA",
        "🍃": "Teal Leaf",
        "⛰️": "Brown Mountain",
        "📜": "Purple Scroll",
        "⭐": "Gold Star"
    }.get(symbol, "Unknown")

    # Substrate-specific variants (optional)
    if substrate:
        if "vibration" in substrate:
            base = "Blue Atom"
        elif "neural" in substrate:
            base = "Green Neuron"
        elif "seasonal" in substrate:
            base = "Teal Spiral"
        elif "seismic" in substrate:
            base = "Brown Faultline"
        elif "civilizational" in substrate:
            base = "Purple Epoch"
        elif "stellar" in substrate:
            base = "Gold Radiant Star"

    # Drift overlays
    if drift == "minor":
        return base + " (hollow)"
    if drift == "moderate":
        return base + " (dashed)"
    if drift == "severe":
        return base + " (red-overlay)"

    return base
```

This is intentionally minimal and easy to extend.
