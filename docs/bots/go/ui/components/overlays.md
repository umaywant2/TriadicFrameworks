# Overlays Component — RTT‑Go  
*(Internal Specification for Triadic Overlay Rendering)*

The **Overlays Component** is the subsystem responsible for rendering all RTT visual layers on top of the Go board.  
It is the visual expression of RTT’s structural, topological, continuity, resonance, and risk intelligence.

Overlays appear in:

- Teaching Mode  
- Analysis Mode  
- Developer Mode  
- Composite Mode  
- Timeline playback  

This document defines the internal architecture, rendering rules, and data contracts for each overlay layer.

---

## 1. Purpose

The Overlays Component provides:

- regime visualization  
- resonance fields  
- topology graphs  
- continuity arcs  
- paradox/collapse warnings  
- move annotations  

It is the **triadic visualization engine** of RTT‑Go.

---

## 2. Overlay Architecture

The overlays subsystem consists of six internal overlay modules:

```
RegimeOverlay
ResonanceOverlay
TopologyOverlay
ContinuityOverlay
RiskOverlay
AnnotationOverlay
```

Each module is independently toggleable and subscribes to triadic state updates.

---

# 3. RegimeOverlay  
*(Visualizes local / structural / continuity regimes)*

### Responsibilities
- render regime glyphs  
- render regime heatmaps  
- highlight regime zones  
- visualize regime drift  

### Rendering Elements
- Local (1/3): red triangle  
- Structural (2/3): blue square  
- Continuity (3/3): gold circle  
- Drift arrows  
- Regime zone shading  

### Data Inputs
```
triadic.regime.local
triadic.regime.structural
triadic.regime.continuity
triadic.regime.drift
triadic.regime.conflict_zones
```

### API Surface
```
render(regimeState)
setOpacity(value)
toggle(enabled)
```

---

# 4. ResonanceOverlay  
*(Visualizes influence, pressure, tension, drift)*

### Responsibilities
- render influence gradients  
- render tension contours  
- render drift vectors  
- highlight collapse signatures  

### Rendering Elements
- gradient fields  
- tension rings  
- drift arrows  
- collapse markers  

### Data Inputs
```
triadic.resonance.pressure_map
triadic.resonance.tension_zones
triadic.resonance.drift_vectors
triadic.resonance.collapse_signatures
```

### API Surface
```
render(resonanceState)
setOpacity(value)
toggle(enabled)
```

---

# 5. TopologyOverlay  
*(Visualizes structural connectivity and ancestry)*

### Responsibilities
- render connectivity graph  
- highlight cutting points  
- render boundary topology  
- render ladder/ko ancestry  
- flag collapse signatures  

### Rendering Elements
- node‑edge graph  
- cutting‑point diamonds  
- boundary outlines  
- ancestry chains  
- collapse glyphs  

### Data Inputs
```
triadic.topology.connectivity
triadic.topology.cut_points
triadic.topology.boundaries
triadic.topology.ancestry
triadic.topology.collapse
```

### API Surface
```
render(topologyState)
highlightCollapse(points)
setOpacity(value)
toggle(enabled)
```

---

# 6. ContinuityOverlay  
*(Visualizes long‑arc identity)*

### Responsibilities
- render territorial/influence/moyo arcs  
- highlight continuity anchors  
- render continuity drift  
- flag identity inversion risk  

### Rendering Elements
- curved arc splines  
- anchor hexagons  
- drift arrows  
- continuity stability shading  

### Data Inputs
```
triadic.continuity.territorial_arcs
triadic.continuity.influence_arcs
triadic.continuity.moyo_arcs
triadic.continuity.ancestry_arcs
triadic.continuity.anchors
triadic.continuity.drift
triadic.continuity.identity_inversion_risk
```

### API Surface
```
render(continuityState)
highlightArc(arc)
setOpacity(value)
toggle(enabled)
```

---

# 7. RiskOverlay  
*(Visualizes paradox, collapse, projection‑loss)*

### Responsibilities
- highlight paradox zones  
- highlight collapse zones  
- highlight projection‑loss zones  

### Rendering Elements
- paradox markers  
- collapse shading  
- projection‑loss triangles  

### Data Inputs
```
triadic.risk.paradox
triadic.risk.collapse
triadic.risk.projection_loss
```

### API Surface
```
render(riskState)
setOpacity(value)
toggle(enabled)
```

---

# 8. AnnotationOverlay  
*(Displays move‑specific triadic commentary)*

### Responsibilities
- render inline annotations  
- show triadic regime tags  
- show continuity impact  
- show paradox/collapse risk  
- show ancestry alignment  

### Rendering Elements
- annotation glyphs  
- tooltip blocks  
- triadic score bars  

### Data Inputs
```
moves[index].triadic
triadic.scores
triadic.risk
triadic.continuity
triadic.topology
```

### API Surface
```
render(moveState)
toggle(enabled)
```

---

# 9. Overlay Rendering Rules

### Layer Order
```
Regime
Resonance
Topology
Continuity
Risk
Annotations
```

### Color System
- Local: red  
- Structural: blue  
- Continuity: gold  
- Collapse: crimson  
- Paradox: orange  
- Stability: teal  

### Opacity Rules
- resonance: 20–40%  
- topology: 60–80%  
- continuity: 70–90%  
- collapse: 40–60%  

### Animation Rules
- drift vectors pulse  
- continuity arcs flow  
- collapse zones flicker  
- ancestry chains animate on hover  

---

# 10. Integration Points

### **Viewer → Overlays**
- overlay toggles  
- opacity changes  
- mode changes  
- timeline events  

### **State Contract → Overlays**
Consumes:

- regime  
- resonance  
- topology  
- continuity  
- risk  
- triadic scores  

### **Overlays → HUD**
- highlight events  
- collapse warnings  
- paradox markers  
- continuity arc selection  

---

# 11. Summary

The Overlays Component is RTT‑Go’s **triadic rendering engine**.

It visualizes:

- regime  
- resonance  
- topology  
- continuity  
- paradox  
- collapse  
- annotations  

and provides the visual foundation for Teaching Mode, Analysis Mode, Developer Mode, and Composite Mode.

The overlays do not play Go — they **illuminate** Go’s triadic identity.
