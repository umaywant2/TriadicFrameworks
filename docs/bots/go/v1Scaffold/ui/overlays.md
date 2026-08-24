# UI Overlays — RTT‑Go  
*(Visual Layer Specification for Triadic Overlays)*

The UI Overlays system renders RTT’s structural, regime, topology, resonance, and continuity information directly on top of the Go board.  
It is the **visual front‑end** of RTT‑Go, used in:

- Teaching Mode  
- Analysis Mode  
- Developer Mode  
- RTT‑Go Viewer integrations  
- Debugging overlays  

This document defines how overlays are structured, layered, rendered, and interacted with.

---

## Purpose

UI overlays provide:

- visual triadic interpretation of the board  
- structural and topological diagrams  
- continuity‑arc visualization  
- resonance fields and drift vectors  
- paradox and collapse warnings  
- move‑specific triadic annotations  

They allow users to *see* RTT’s understanding of the position.

---

## Overlay Architecture

RTT‑Go overlays follow a **layered rendering model**:

```
Base Board
  ↓
Stone Layer
  ↓
Regime Layer (Hephaestus)
  ↓
Resonance Layer (Lumen + Harmonia)
  ↓
Topology Layer (Aurion)
  ↓
Continuity Layer (Aurion + Harmonia)
  ↓
Paradox/Collapse Layer
  ↓
Move Annotation Layer
```

Each layer is independent and can be toggled on/off.

---

## Overlay Layers

### **1. Regime Layer (Hephaestus)**  
Displays regime identity for each candidate move:

- Local (1/3) — red markers  
- Structural (2/3) — blue markers  
- Continuity (3/3) — gold markers  

Rendering:

- small regime glyph near each move  
- optional heatmap showing regime zones  
- regime legend in sidebar  

---

### **2. Resonance Layer (Lumen + Harmonia)**  
Displays dynamic pressure and influence:

- influence gradients  
- tension contours  
- drift vectors  
- collapse signatures  

Rendering:

- soft gradient fields  
- vector arrows  
- tension rings around unstable groups  

---

### **3. Topology Layer (Aurion)**  
Displays structural connectivity:

- group connectivity graph  
- cutting‑point topology  
- moyo boundary topology  
- ladder/ko ancestry chains  

Rendering:

- node‑edge graph overlay  
- boundary outlines  
- ancestry lines  

---

### **4. Continuity Layer (Aurion + Harmonia)**  
Displays long‑arc identity:

- territorial arcs  
- influence arcs  
- moyo arcs  
- ancestry arcs  
- continuity anchors  

Rendering:

- curved arc lines  
- anchor markers  
- long‑arc flow diagrams  

---

### **5. Paradox & Collapse Layer**  
Displays warnings for moves or zones that:

- break continuity  
- collapse influence arcs  
- destabilize ladders  
- violate ancestry  
- invert identity  

Rendering:

- red shading  
- collapse glyphs  
- paradox markers  

---

### **6. Move Annotation Layer**  
Displays RTT commentary for each candidate move:

- triadic regime  
- continuity impact  
- paradox risk  
- collapse risk  
- ancestry alignment  

Rendering:

- tooltip on hover  
- sidebar list  
- inline annotation near move  

---

## Overlay Interaction Model

### **Toggle Controls**
Users can toggle overlays:

- Regime  
- Resonance  
- Topology  
- Continuity  
- Paradox/Collapse  
- All Triadic Layers  

### **Hover Interactions**
Hovering a move shows:

- regime tag  
- triadic score  
- continuity impact  
- paradox/collapse risk  
- ancestry alignment  

### **Click Interactions**
Clicking a move shows:

- full triadic breakdown  
- structural/topological context  
- continuity‑arc implications  
- resonance field snapshot  

### **Composite Mode**
Displays all overlays simultaneously.

---

## Rendering Rules

### **Layer Ordering**
Continuity arcs must render *above* topology graphs.  
Paradox warnings must render *above* continuity arcs.  
Resonance fields must render *below* topology graphs.

### **Color System**
- Local: red  
- Structural: blue  
- Continuity: gold  
- Collapse: crimson  
- Paradox: orange  
- Stability: teal  

### **Opacity Rules**
- resonance fields: 20–40%  
- topology graphs: 60–80%  
- continuity arcs: 70–90%  
- collapse zones: 40–60%  

### **Animation**
Optional animations:

- drift vectors pulse  
- continuity arcs flow  
- collapse zones flicker  
- ancestry chains animate on hover  

---

## Example Composite Overlay

### Position
White has a large moyo on the left.  
Black has a weak group on the right.

### Composite Overlay Interpretation

- **Regime:**  
  - left moyo → continuity  
  - right weakness → local  
  - center → structural  

- **Resonance:**  
  - right side → high tension  
  - left side → stable  

- **Topology:**  
  - cutting points → collapse risk  
  - moyo boundary → continuity anchor  

- **Continuity:**  
  - left arc → expanding  
  - right arc → collapsing  

- **Paradox:**  
  - local fix breaks global continuity  

This composite overlay visually explains the entire triadic identity of the position.

---

## Developer Notes

- overlays are engine‑agnostic  
- RTT primitives come from the shim  
- rendering is deterministic  
- overlay data is JSON‑serializable  
- UI layer must support incremental updates  
- teaching/analysis modes use identical overlay engine  

---

## Summary

UI overlays are the **visual intelligence layer** of RTT‑Go.

They reveal:

- structure  
- regime  
- topology  
- continuity  
- resonance  
- paradox  
- collapse  

and allow users to see Go through the triadic lens.

RTT‑Go overlays do not play Go — they **illuminate** it.
