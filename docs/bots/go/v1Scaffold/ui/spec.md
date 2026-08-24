# UI Specification — RTT‑Go  
*(Formal Triadic UI Architecture & Rendering Model)*

The RTT‑Go UI Specification defines the **visual, structural, and interaction rules** for rendering triadic overlays, continuity arcs, topology graphs, resonance fields, paradox warnings, and regime classifications on top of the Go board.

This specification governs:

- Teaching Mode  
- Analysis Mode  
- Triadic Viewer  
- Developer Mode  
- RTT‑Go UI integrations  
- Debugging overlays  

It is the canonical reference for all RTT‑Go UI implementations.

---

## 1. UI Architecture Overview

The RTT‑Go UI stack consists of five major components:

```
Board Renderer
Overlay Engine
Triadic HUD
Interaction Layer
Timeline / Playback System
```

Each component is modular, deterministic, and engine‑agnostic.

---

## 2. Rendering Pipeline

The UI uses a **layered rendering pipeline**:

```
Base Board
Stone Layer
Regime Layer
Resonance Layer
Topology Layer
Continuity Layer
Paradox/Collapse Layer
Move Annotation Layer
HUD Layer
```

Layers are composited in this exact order.

---

## 3. Overlay Engine Specification

The Overlay Engine renders all RTT visual layers.

### 3.1 Regime Layer (Hephaestus)

Displays regime identity:

- Local (1/3) — red  
- Structural (2/3) — blue  
- Continuity (3/3) — gold  

Elements:

- regime glyphs  
- regime heatmaps  
- regime zone outlines  

### 3.2 Resonance Layer (Lumen + Harmonia)

Displays dynamic pressure:

- influence gradients  
- tension contours  
- drift vectors  
- collapse signatures  

Elements:

- soft gradient fields  
- vector arrows  
- tension rings  

### 3.3 Topology Layer (Aurion)

Displays structural connectivity:

- group connectivity graph  
- cutting‑point topology  
- moyo boundary topology  
- ladder/ko ancestry chains  

Elements:

- node‑edge graphs  
- boundary outlines  
- ancestry lines  

### 3.4 Continuity Layer (Aurion + Harmonia)

Displays long‑arc identity:

- territorial arcs  
- influence arcs  
- moyo arcs  
- ancestry arcs  
- continuity anchors  

Elements:

- curved arc lines  
- anchor markers  
- flow diagrams  

### 3.5 Paradox & Collapse Layer

Displays warnings:

- paradox zones  
- collapse‑risk shading  
- identity inversion markers  

Elements:

- red shading  
- collapse glyphs  
- paradox markers  

### 3.6 Move Annotation Layer

Displays RTT commentary:

- triadic regime  
- continuity impact  
- paradox/collapse risk  
- ancestry alignment  

Elements:

- tooltips  
- inline annotations  
- sidebar commentary  

---

## 4. Triadic HUD Specification

The HUD displays RTT metadata.

### 4.1 Regime Panel
Shows:

- regime distribution  
- regime drift  
- conflict zones  

### 4.2 Topology Panel
Shows:

- connectivity graph  
- ancestry chains  
- collapse signatures  

### 4.3 Continuity Panel
Shows:

- continuity arcs  
- anchors  
- drift vectors  
- identity evolution  

### 4.4 Resonance Panel
Shows:

- influence resonance  
- pressure gradients  
- tension zones  

### 4.5 Move Commentary Panel
Shows:

- triadic regime  
- continuity impact  
- paradox/collapse risk  
- ancestry alignment  

---

## 5. Interaction Model Specification

### 5.1 Hover Behavior
Hovering a move displays:

- regime tag  
- triadic score  
- continuity impact  
- paradox/collapse risk  
- ancestry alignment  

### 5.2 Click Behavior
Clicking a move displays:

- full triadic breakdown  
- structural/topological context  
- continuity‑arc implications  
- resonance snapshot  

### 5.3 Toggle Controls
Users can toggle:

- regime  
- resonance  
- topology  
- continuity  
- paradox/collapse  
- all triadic layers  

### 5.4 Composite Mode
Displays all overlays simultaneously.

---

## 6. Timeline / Playback Specification

The timeline supports:

- move‑by‑move triadic evolution  
- continuity‑arc playback  
- resonance drift animation  
- topology evolution  
- ancestry evolution  
- collapse‑signature detection  

Playback modes:

- Step Mode  
- Flow Mode  
- Arc Mode  
- Topology Mode  
- Resonance Mode  

---

## 7. Rendering Rules

### 7.1 Layer Ordering
Continuity arcs must render above topology.  
Paradox warnings must render above continuity.  
Resonance fields must render below topology.

### 7.2 Color System
- Local: red  
- Structural: blue  
- Continuity: gold  
- Collapse: crimson  
- Paradox: orange  
- Stability: teal  

### 7.3 Opacity Rules
- resonance fields: 20–40%  
- topology graphs: 60–80%  
- continuity arcs: 70–90%  
- collapse zones: 40–60%  

### 7.4 Animation Rules
Optional animations:

- drift vectors pulse  
- continuity arcs flow  
- collapse zones flicker  
- ancestry chains animate on hover  

---

## 8. Data Contract Specification

The UI receives RTT primitives as structured JSON:

```json
{
  "regime": { ... },
  "resonance": { ... },
  "topology": { ... },
  "continuity": { ... },
  "paradox": { ... },
  "collapse": { ... },
  "triadic_scores": { ... },
  "annotations": { ... }
}
```

All fields are deterministic and engine‑agnostic.

---

## 9. Developer Notes

- UI is stateless; RTT provides all state  
- overlay data is JSON‑serializable  
- viewer is engine‑agnostic  
- rendering is deterministic  
- supports incremental updates  
- teaching/analysis modes share the same viewer  

---

## Summary

The RTT‑Go UI Specification defines the **complete visual architecture** for triadic overlays, continuity arcs, topology graphs, resonance fields, paradox warnings, and triadic commentary.

It ensures RTT‑Go is:

- structurally coherent  
- visually consistent  
- triadically expressive  
- continuity‑aware  
- topology‑accurate  
- resonance‑aligned  

The UI does not play Go — it **reveals** Go.
