# HUD Component — RTT‑Go  
*(Internal Specification for the Triadic Heads‑Up Display)*

The **HUD Component** is the informational counterpart to the Triadic Viewer.  
Where the viewer renders the board and overlays, the HUD presents **structured triadic metadata** — regime flow, topology diagnostics, continuity arcs, resonance fields, and move commentary.

The HUD is used in:

- Teaching Mode  
- Analysis Mode  
- Developer Mode  
- Composite Mode  

It is the **triadic dashboard** of RTT‑Go.

---

## 1. Purpose

The HUD Component provides:

- regime distribution  
- topology diagnostics  
- continuity‑arc status  
- resonance metrics  
- ancestry alignment  
- paradox/collapse warnings  
- triadic score breakdowns  
- move‑by‑move commentary  

It is the **informational intelligence layer** of RTT‑Go.

---

## 2. HUD Architecture

The HUD consists of five internal panels:

```
RegimePanel
TopologyPanel
ContinuityPanel
ResonancePanel
CommentaryPanel
```

Each panel is independently renderable and subscribes to viewer events.

---

# 3. RegimePanel  
*(Displays regime identity and flow)*

### Responsibilities
- show local / structural / continuity proportions  
- display regime drift vectors  
- highlight conflict zones  
- visualize regime stability  

### Rendering Elements
- bar graph  
- drift arrows  
- conflict markers  
- regime color legend  

### API Surface
```
renderRegime(regimeState)
setActive()
setInactive()
```

---

# 4. TopologyPanel  
*(Displays structural connectivity and ancestry)*

### Responsibilities
- show connectivity graph  
- highlight cutting points  
- display boundary topology  
- show ladder/ko ancestry  
- flag collapse signatures  

### Rendering Elements
- mini node‑edge graph  
- ancestry chain diagram  
- collapse glyphs  
- boundary stability meter  

### API Surface
```
renderTopology(topologyState)
highlightCollapse(points)
setActive()
setInactive()
```

---

# 5. ContinuityPanel  
*(Displays long‑arc identity)*

### Responsibilities
- show territorial/influence/moyo arcs  
- highlight continuity anchors  
- display continuity drift  
- flag identity inversion risk  

### Rendering Elements
- arc flow diagram  
- anchor markers  
- drift vector chart  
- continuity stability meter  

### API Surface
```
renderContinuity(continuityState)
highlightArc(arc)
setActive()
setInactive()
```

---

# 6. ResonancePanel  
*(Displays dynamic pressure and tension)*

### Responsibilities
- show influence resonance  
- highlight tension zones  
- display pressure gradients  
- show drift vectors  
- flag collapse signatures  

### Rendering Elements
- resonance heatmap thumbnail  
- tension bar  
- drift arrow cluster  
- collapse indicator  

### API Surface
```
renderResonance(resonanceState)
highlightTension(zone)
setActive()
setInactive()
```

---

# 7. CommentaryPanel  
*(Displays triadic commentary for selected/hovered moves)*

### Responsibilities
- show triadic regime  
- display triadic score breakdown  
- show continuity impact  
- flag paradox/collapse risk  
- show ancestry alignment  
- provide structural/topological context  

### Rendering Elements
- structured commentary block  
- triadic score bars  
- risk icons  
- continuity arc preview  

### API Surface
```
renderCommentary(moveState)
lockMove(move)
unlockMove()
setActive()
setInactive()
```

---

# 8. HUD Interaction Model

### Hover
- update all panels  
- highlight relevant triadic metadata  
- show lightweight commentary  

### Click
- lock commentary panel  
- freeze triadic metadata  
- show full breakdown  

### Timeline Scrubbing
- animate regime drift  
- animate continuity arcs  
- animate topology evolution  
- animate resonance drift  

---

# 9. HUD Rendering Rules

### Color System
- Local: red  
- Structural: blue  
- Continuity: gold  
- Collapse: crimson  
- Paradox: orange  
- Stability: teal  

### Layout Rules
```
RegimePanel        (left)
TopologyPanel      (center-left)
ContinuityPanel    (center-right)
ResonancePanel     (right)
CommentaryPanel    (bottom)
```

### Animation Rules
- drift vectors pulse  
- continuity arcs flow  
- collapse warnings flicker  
- ancestry chains animate on hover  

---

# 10. Integration Points

### **Viewer → HUD**
- hover events  
- click events  
- timeline events  
- overlay toggles  

### **State Contract → HUD**
Consumes:

- regime  
- topology  
- continuity  
- resonance  
- risk  
- triadic scores  

### **HUD → Viewer**
- active panel changes  
- move lock/unlock  
- commentary updates  

---

# 11. Summary

The HUD Component is RTT‑Go’s **informational intelligence engine**.

It reveals:

- regime flow  
- topology  
- continuity  
- resonance  
- ancestry  
- paradox  
- collapse  

and provides structured triadic commentary for every position.

The HUD does not play Go — it **interprets** Go’s triadic identity.
