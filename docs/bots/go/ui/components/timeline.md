# Timeline Component — RTT‑Go  
*(Internal Specification for Triadic Playback & Evolution)*

The **Timeline Component** is the subsystem responsible for animating RTT‑Go’s triadic evolution across moves.  
It drives:

- continuity‑arc playback  
- resonance drift animation  
- topology evolution  
- regime flow visualization  
- move‑by‑move triadic commentary  
- HUD synchronization  
- viewer updates  

The timeline is the **temporal engine** of RTT‑Go.

---

## 1. Purpose

The Timeline Component provides:

- move‑indexed playback  
- triadic evolution visualization  
- continuity arc flow  
- resonance drift animation  
- topology change detection  
- ancestry evolution  
- collapse‑signature detection  
- HUD + viewer synchronization  

It transforms static triadic state into **dynamic triadic narrative**.

---

## 2. Timeline Architecture

The timeline subsystem consists of five internal modules:

```
TimelineController
PlaybackEngine
EvolutionEngine
EventDispatcher
HUDViewerSync
```

Each module is defined below.

---

# 3. TimelineController  
*(Primary control surface for timeline state)*

### Responsibilities
- manage current timeline position  
- manage playback mode  
- handle user input (seek, play, pause, step)  
- validate move indices  
- dispatch timeline events  

### API Surface
```
seek(position)
play()
pause()
stepForward()
stepBack()
setMode(mode)
getMode()
```

### Playback Modes
- `step` — discrete move‑by‑move  
- `flow` — continuous animation  
- `arc` — continuity‑arc evolution  
- `topology` — connectivity evolution  
- `resonance` — pressure/tension evolution  

---

# 4. PlaybackEngine  
*(Executes playback according to mode)*

### Responsibilities
- animate continuity arcs  
- animate resonance drift  
- animate topology evolution  
- animate ancestry changes  
- animate collapse signatures  
- interpolate triadic state between moves  

### Rendering Rules
- continuity arcs animate smoothly  
- resonance drift uses pulsing vectors  
- topology changes animate node/edge transitions  
- collapse signatures flicker  
- ancestry chains pulse  

### API Surface
```
renderFrame(triadicState)
animateContinuity(prevState, nextState)
animateTopology(prevState, nextState)
animateResonance(prevState, nextState)
animateRisk(prevState, nextState)
```

---

# 5. EvolutionEngine  
*(Computes triadic deltas between moves)*

### Responsibilities
- compute regime deltas  
- compute resonance deltas  
- compute topology deltas  
- compute continuity deltas  
- compute risk deltas  
- detect collapse events  
- detect paradox events  
- detect identity inversion  

### Delta Model
```
delta = nextState - prevState
```

### API Surface
```
computeDelta(prevState, nextState)
detectCollapse(delta)
detectParadox(delta)
detectIdentityInversion(delta)
```

---

# 6. EventDispatcher  
*(Emits timeline events to viewer + HUD)*

### Responsibilities
- dispatch move‑change events  
- dispatch triadic‑delta events  
- dispatch collapse/paradox events  
- dispatch continuity‑arc events  
- dispatch resonance‑drift events  

### Event Types
```
timeline.position.changed
timeline.mode.changed
timeline.delta.computed
timeline.collapse.detected
timeline.paradox.detected
timeline.identity_inversion.detected
```

### API Surface
```
emit(eventName, payload)
subscribe(eventName, handler)
unsubscribe(eventName, handler)
```

---

# 7. HUDViewerSync  
*(Synchronizes timeline with HUD + viewer)*

### Responsibilities
- update viewer overlays  
- update HUD panels  
- lock/unlock commentary  
- highlight continuity arcs  
- highlight topology changes  
- highlight resonance drift  

### API Surface
```
syncViewer(triadicState)
syncHUD(triadicState)
highlightMove(move)
highlightArc(arc)
highlightCollapse(points)
```

---

# 8. Timeline Rendering Rules

### Color Rules
- continuity arcs: gold/amber  
- resonance drift: blue/violet  
- topology changes: teal/green  
- collapse: crimson  
- paradox: orange  

### Animation Rules
- continuity arcs flow  
- drift vectors pulse  
- collapse zones flicker  
- ancestry chains animate  
- topology edges fade in/out  

### Temporal Rules
- step mode: discrete frames  
- flow mode: interpolated frames  
- arc mode: continuity emphasis  
- topology mode: connectivity emphasis  
- resonance mode: pressure emphasis  

---

# 9. Integration Points

### **State Contract → Timeline**
Consumes:

- moves[]  
- triadic.regime  
- triadic.resonance  
- triadic.topology  
- triadic.continuity  
- triadic.risk  

### **Timeline → Viewer**
- frame updates  
- overlay updates  
- highlight events  

### **Timeline → HUD**
- commentary updates  
- delta diagnostics  
- collapse/paradox alerts  

### **Viewer → Timeline**
- hover events  
- click events  
- mode changes  

---

# 10. Summary

The Timeline Component is RTT‑Go’s **temporal intelligence engine**.

It animates:

- continuity arcs  
- resonance drift  
- topology evolution  
- ancestry changes  
- collapse signatures  
- paradox events  

and synchronizes:

- viewer  
- HUD  
- overlays  

The timeline does not play Go — it **reveals Go’s triadic evolution**.
