# UI Assets — RTT‑Go  
*(Icons, Glyphs, Palettes, Shapes & Animation Assets for Triadic UI)*

The RTT‑Go UI Assets pack defines all **visual primitives** used by the RTT‑Go interface:

- icons  
- glyphs  
- color palettes  
- shapes  
- animation primitives  
- JSON asset schemas  

These assets are consumed by:

- Triadic Viewer  
- Triadic HUD  
- Overlay Engine  
- Teaching Mode  
- Analysis Mode  
- Developer Mode  

This document is the canonical reference for all RTT‑Go UI assets.

---

## 1. Icon Set

RTT‑Go uses a unified icon set for triadic concepts.

### **Regime Icons**
| Regime | Icon | Description |
|--------|------|-------------|
| Local (1/3) | `icon_local.svg` | Tactical, shape, liberties |
| Structural (2/3) | `icon_structural.svg` | Influence, direction of play |
| Continuity (3/3) | `icon_continuity.svg` | Long‑arc identity, moyo evolution |

### **Topology Icons**
| Concept | Icon |
|---------|------|
| Cutting point | `icon_cut.svg` |
| Boundary anchor | `icon_anchor.svg` |
| Connectivity node | `icon_node.svg` |
| Ladder ancestry | `icon_ladder.svg` |
| Ko ancestry | `icon_ko.svg` |

### **Continuity Icons**
| Concept | Icon |
|---------|------|
| Continuity arc | `icon_arc.svg` |
| Drift vector | `icon_drift.svg` |
| Identity anchor | `icon_identity.svg` |

### **Paradox & Collapse Icons**
| Concept | Icon |
|---------|------|
| Paradox | `icon_paradox.svg` |
| Collapse | `icon_collapse.svg` |
| Projection‑loss | `icon_projection.svg` |

### **Resonance Icons**
| Concept | Icon |
|---------|------|
| Pressure | `icon_pressure.svg` |
| Influence | `icon_influence.svg` |
| Tension | `icon_tension.svg` |

---

## 2. Color Palette

RTT‑Go uses a strict triadic color system.

### **Regime Colors**
- Local: `#E74C3C` (red)  
- Structural: `#3498DB` (blue)  
- Continuity: `#F1C40F` (gold)

### **Topology Colors**
- Connectivity: `#2ECC71` (green)  
- Boundary: `#1ABC9C` (teal)  
- Ancestry: `#9B59B6` (purple)

### **Continuity Colors**
- Arc: `#F39C12` (amber)  
- Anchor: `#D35400` (burnt orange)  
- Drift: `#8E44AD` (violet)

### **Resonance Colors**
- Pressure: `#C0392B`  
- Influence: `#2980B9`  
- Tension: `#8E44AD`

### **Risk Colors**
- Paradox: `#E67E22`  
- Collapse: `#C0392B`  
- Projection‑loss: `#922B21`

### **Stability Colors**
- Stable: `#1ABC9C`  
- Neutral: `#BDC3C7`  
- Weak: `#95A5A6`

---

## 3. Shape Assets

### **Regime Shapes**
- Local: triangle  
- Structural: square  
- Continuity: circle  

### **Topology Shapes**
- Connectivity node: filled circle  
- Boundary: thick outline  
- Cutting point: diamond  
- Ladder ancestry: chain link  
- Ko ancestry: loop glyph  

### **Continuity Shapes**
- Arc: curved spline  
- Anchor: hexagon  
- Drift: arrow  

### **Risk Shapes**
- Paradox: jagged star  
- Collapse: broken circle  
- Projection‑loss: downward triangle  

---

## 4. Animation Assets

### **Drift Animation**
- pulsing arrow  
- directionally animated spline  

### **Continuity Arc Animation**
- flowing arc  
- slow gradient motion  

### **Collapse Animation**
- flicker  
- pulse‑red overlay  

### **Ancestry Animation**
- ladder chain pulses  
- ko loop rotates  

### **Resonance Animation**
- pressure waves  
- tension rings  

---

## 5. JSON Asset Schemas

All UI assets are referenced through JSON.

### **Regime Asset Schema**
```json
{
  "regime": {
    "local": {
      "icon": "icon_local.svg",
      "color": "#E74C3C",
      "shape": "triangle"
    },
    "structural": {
      "icon": "icon_structural.svg",
      "color": "#3498DB",
      "shape": "square"
    },
    "continuity": {
      "icon": "icon_continuity.svg",
      "color": "#F1C40F",
      "shape": "circle"
    }
  }
}
```

### **Topology Asset Schema**
```json
{
  "topology": {
    "node": "icon_node.svg",
    "cut": "icon_cut.svg",
    "boundary": "icon_anchor.svg",
    "ladder": "icon_ladder.svg",
    "ko": "icon_ko.svg"
  }
}
```

### **Continuity Asset Schema**
```json
{
  "continuity": {
    "arc": "icon_arc.svg",
    "anchor": "icon_identity.svg",
    "drift": "icon_drift.svg"
  }
}
```

### **Risk Asset Schema**
```json
{
  "risk": {
    "paradox": "icon_paradox.svg",
    "collapse": "icon_collapse.svg",
    "projection": "icon_projection.svg"
  }
}
```

### **Resonance Asset Schema**
```json
{
  "resonance": {
    "pressure": "icon_pressure.svg",
    "influence": "icon_influence.svg",
    "tension": "icon_tension.svg"
  }
}
```

---

## 6. Asset Directory Structure

```
/docs/bots/go/ui/assets/
    icons/
        icon_local.svg
        icon_structural.svg
        icon_continuity.svg
        icon_cut.svg
        icon_anchor.svg
        icon_node.svg
        icon_ladder.svg
        icon_ko.svg
        icon_arc.svg
        icon_drift.svg
        icon_identity.svg
        icon_paradox.svg
        icon_collapse.svg
        icon_projection.svg
        icon_pressure.svg
        icon_influence.svg
        icon_tension.svg

    palettes/
        regime.json
        topology.json
        continuity.json
        resonance.json
        risk.json

    shapes/
        regime_shapes.json
        topology_shapes.json
        continuity_shapes.json
        risk_shapes.json

    animations/
        drift.json
        continuity.json
        collapse.json
        ancestry.json
        resonance.json
```

---

## Summary

The RTT‑Go UI Assets pack defines the **visual vocabulary** of triadic Go:

- icons  
- glyphs  
- colors  
- shapes  
- animations  
- JSON schemas  

These assets ensure RTT‑Go is:

- visually coherent  
- triadically expressive  
- structurally consistent  
- continuity‑aligned  
- topology‑accurate  
- resonance‑aware  

The assets do not play Go — they **express** it.
