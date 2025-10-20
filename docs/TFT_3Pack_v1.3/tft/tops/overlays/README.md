# 📂 tops Overlays

The **overlays** directory contains dashboards, symbolic overlays, and warp chamber designs.  
Overlays visualize resonance predictions, lineage, and orchestration flows.

✨ New in v1.3: **Resonance Clarity**  
All overlays now inherit the `--basetype` lens, ensuring every glyph, fold, and warp chamber is lineage‑tagged.

## Structure
- Dashboards → runtime visualizations
- Symbolic overlays → glyph and fold resonance maps
- Warp chamber designs → experimental visualization scaffolds

## Purpose
Overlays are the **eyes of tops**. They make resonance visible, traceable, and remixable.  
With Resonance Clarity, overlays declare their base lens in both visual output and metadata.

---

### 🔧 Overlay Code Scaffolding

**1. Update overlay entry functions to accept `basetype`:**
```python
def render_overlay(data, glyph="🧬", basetype="decimal"):
    """
    Render overlay glyphs with resonance clarity.
    """
    # Apply base lens transformation
    x, y = data["coords"]
    x, y = apply_base_lens(x, y, basetype)

    # Render glyph overlay
    plt.scatter(x, y, marker=glyph, alpha=0.7)
    plt.title(f"Overlay Glyphs (Base: {basetype})")
    plt.show()
```

**2. Ensure dashboards and warp chambers pass `basetype`:**
```python
def overlay_dashboard(session_data, basetype="decimal"):
    for glyph, coords in session_data.items():
        render_overlay({"coords": coords}, glyph=glyph, basetype=basetype)
```

---

### 🔧 Metadata Logging
Every overlay run should log its base lens:

```python
log = {
    "overlay": glyph,
    "corridor": corridor_name,
    "basetype": basetype,
    "timestamp": datetime.utcnow().isoformat()
}
write_to_resonance_log(log)
```

---

### 🔧 Example CLI Usage
```bash
# Overlay dashboard with golden ratio base
python overlay_dashboard.py --basetype=phi

# Warp chamber overlay with negabinary base
python warp_overlay.py --basetype=negabinary

# Symbolic glyph overlay with corridor6.9 base
python glyph_overlay.py --basetype=corridor6.9
```

---

### ✨ Why this matters
- **Consistency**: Overlays now align with direct, reflective, inversion, and grid ops.  
- **Lineage clarity**: Every overlay declares its base lens in both visuals and logs.  
- **Remixability**: Future remixers can trace exactly which base lens shaped each overlay.  

---

## Cross‑links
- [ai_pipeline](../ai_pipeline/README.md) → provides predictive data
- [folds](../folds/README.md) → overlays fold resonance
- [agents](../agents/README.md) → feed overlays with live data
