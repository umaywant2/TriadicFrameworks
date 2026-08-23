# Viewer Component — RTT‑Go  
*(Internal Specification for the Triadic Viewer Engine)*

The **Viewer Component** is the core UI module responsible for rendering the Go board and all triadic overlays.  
It is the visual execution engine behind:

- Teaching Mode  
- Analysis Mode  
- Developer Mode  
- Composite Mode  
- Timeline playback  
- HUD synchronization  

This document defines the viewer’s internal architecture, responsibilities, rendering rules, and integration points.

---

## 1. Purpose

The Viewer Component provides:

- board rendering  
- stone rendering  
- overlay compositing  
- interaction handling  
- HUD event dispatch  
- timeline synchronization  
- triadic state visualization  

It is the **visual substrate** of RTT‑Go.

---

## 2. Viewer Architecture

The viewer is composed of five internal subsystems:

```
BoardRenderer
OverlayEngine
InteractionController
HUDBridge
TimelineSync
```

Each subsystem is defined below.

---

# 3. BoardRenderer  
*(Draws the Go board and stones)*

### Responsibilities
- draw board grid  
- draw stones  
- draw captures  
- draw ko markers  
- maintain coordinate mapping  
- handle zoom/pan (optional)  
- expose hit‑testing for interactions  

### Rendering Rules
- stones render above board  
- overlays render above stones  
- ko marker uses engine‑agnostic glyph  
- board grid uses fixed opacity (30%)  

### API Surface
```
renderBoard(boardState)
renderStones(stoneList)
highlightMove(move)
clearHighlights()
```

---

# 4. OverlayEngine  
*(Composites all RTT overlays)*

The OverlayEngine renders:

- regime overlay  
- resonance overlay  
- topology overlay  
- continuity overlay  
- paradox/collapse overlay  
- annotation overlay  

### Responsibilities
- layer ordering  
- palette application  
- shape rendering  
- animation scheduling  
- opacity management  
- overlay toggling  

### Layer Order
```
Regime
Resonance
Topology
Continuity
Paradox/Collapse
Annotations
```

### API Surface
```
renderOverlays(triadicState)
toggleOverlay(name, enabled)
setOverlayOpacity(name, value)
refresh()
```

---

# 5. InteractionController  
*(Handles user interaction with the viewer)*

### Responsibilities
- hover detection  
- click detection  
- move highlighting  
- dispatching HUD events  
- dispatching timeline events  
- composite mode toggling  

### Interaction Model
**Hover**  
- show move annotation  
- update HUD panels  
- highlight stones  

**Click**  
- lock HUD  
- freeze overlay state  
- show full triadic breakdown  

### API Surface
```
onHover(move)
onClick(move)
onOverlayToggle(name)
onModeChange(mode)
```

---

# 6. HUDBridge  
*(Connects viewer events to HUD panels)*

### Responsibilities
- send triadic metadata to HUD  
- synchronize active panel  
- lock/unlock move commentary  
- propagate overlay state  

### API Surface
```
updateHUD(triadicState)
lockMove(move)
unlockMove()
setActivePanel(panel)
```

---

# 7. TimelineSync  
*(Synchronizes viewer with timeline playback)*

### Responsibilities
- update viewer on timeline seek  
- animate continuity arcs  
- animate resonance drift  
- animate topology evolution  
- dispatch move events to HUD  

### Playback Modes
- Step Mode  
- Flow Mode  
- Arc Mode  
- Topology Mode  
- Resonance Mode  

### API Surface
```
seek(position)
play()
pause()
stepForward()
stepBack()
```

---

# 8. Viewer Modes

The viewer supports four modes:

### **Teaching Mode**
- overlays for candidate moves  
- regime emphasis  
- continuity arcs visible  
- paradox warnings active  

### **Analysis Mode**
- overlays for played moves  
- long‑arc continuity playback  
- topology evolution emphasis  

### **Developer Mode**
- raw RTT primitives  
- debug overlays  
- unfiltered topology graphs  

### **Composite Mode**
- all overlays active  
- full triadic visualization  

### API Surface
```
setMode(mode)
getMode()
```

---

# 9. Rendering Rules

### Color Rules
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

The viewer integrates with:

### **State Contract**
Consumes full triadic JSON state.

### **HUD**
Dispatches move metadata.

### **Timeline**
Synchronizes playback.

### **Overlays**
Renders all triadic layers.

### **Assets**
Uses icons, shapes, palettes, animations.

---

# 11. Summary

The Viewer Component is RTT‑Go’s **visual execution engine**.

It renders:

- board  
- stones  
- overlays  
- continuity arcs  
- topology graphs  
- resonance fields  
- paradox warnings  

and synchronizes:

- HUD  
- timeline  
- interaction model  

The viewer does not play Go — it **reveals** Go’s triadic identity.
