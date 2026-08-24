# Triadic Viewer — RTT‑Go  
*(Unified Visual Interface for Triadic Interpretation)*

The **Triadic Viewer** is the primary UI component for RTT‑Go.  
It renders all RTT overlays — structural, regime, topology, resonance, continuity, paradox, collapse — into a single interactive visual system.

Where Teaching Mode explains candidate moves and Analysis Mode explains played moves, the Triadic Viewer provides the **visual substrate** for both.

It is the RTT‑Go equivalent of a “triadic microscope.”

---

## Purpose

The Triadic Viewer provides:

- unified triadic visualization  
- interactive overlay toggles  
- long‑arc continuity playback  
- structural/topological diagrams  
- resonance field animations  
- ancestry and ladder/ko visualization  
- paradox and collapse warnings  
- move‑by‑move triadic commentary  

It is the **front‑end lens** through which RTT interprets Go.

---

## Viewer Architecture

The Triadic Viewer is composed of five subsystems:

1. **Board Renderer**  
2. **Overlay Engine**  
3. **Triadic HUD (Heads‑Up Display)**  
4. **Interaction Layer**  
5. **Timeline / Playback System**

These components work together to display RTT’s triadic understanding of the position.

---

## 1. Board Renderer

Responsible for:

- drawing the Go board  
- stones, captures, ko markers  
- coordinate grid  
- hover/click detection  
- smooth animations  

The board renderer is engine‑agnostic and receives updates from the bot logic layer.

---

## 2. Overlay Engine

The overlay engine renders all RTT layers:

- **Regime Layer**  
- **Resonance Layer**  
- **Topology Layer**  
- **Continuity Layer**  
- **Paradox/Collapse Layer**  
- **Move Annotation Layer**

Each layer is independently toggleable.

### Layer Ordering

```
Board
Stones
Regime
Resonance
Topology
Continuity
Paradox/Collapse
Annotations
```

This ordering ensures clarity and prevents visual collisions.

---

## 3. Triadic HUD

The HUD displays RTT metadata:

### **Regime Panel**
Shows:

- local / structural / continuity distribution  
- regime drift  
- conflict zones  

### **Topology Panel**
Shows:

- connectivity graph  
- ancestry chains  
- collapse signatures  

### **Continuity Panel**
Shows:

- continuity arcs  
- anchors  
- drift vectors  
- identity evolution  

### **Resonance Panel**
Shows:

- influence resonance  
- pressure gradients  
- tension zones  

### **Move Commentary Panel**
Shows:

- triadic regime  
- continuity impact  
- paradox/collapse risk  
- ancestry alignment  

The HUD updates dynamically as the user hovers or scrubs through moves.

---

## 4. Interaction Layer

The viewer supports rich interaction:

### **Hover**
Displays:

- regime tag  
- triadic score  
- continuity impact  
- paradox/collapse risk  
- ancestry alignment  

### **Click**
Displays:

- full triadic breakdown  
- structural/topological context  
- continuity‑arc implications  
- resonance snapshot  

### **Toggle Controls**
Users can toggle:

- regime  
- resonance  
- topology  
- continuity  
- paradox/collapse  
- all triadic layers  

### **Composite Mode**
Displays all overlays simultaneously.

---

## 5. Timeline / Playback System

The viewer includes a timeline for:

- move‑by‑move triadic evolution  
- continuity‑arc playback  
- resonance drift animation  
- topology changes over time  
- ancestry evolution (ladder/ko)  
- collapse‑signature detection  

### Playback Modes

- **Step Mode** — move‑by‑move  
- **Flow Mode** — continuous animation  
- **Arc Mode** — continuity‑arc evolution  
- **Topology Mode** — connectivity evolution  
- **Resonance Mode** — pressure evolution  

---

## Example Viewer Session

### Position
White has a large moyo on the left.  
Black has a weak group on the right.

### Viewer Output

**Regime Layer:**  
Left → continuity  
Right → local  
Center → structural  

**Resonance Layer:**  
Right side → high tension  
Left side → stable  

**Topology Layer:**  
Cutting points → collapse risk  
Moyo boundary → continuity anchor  

**Continuity Layer:**  
Left arc → expanding  
Right arc → collapsing  

**Paradox Layer:**  
Local fix breaks global continuity  

**HUD Commentary:**  
```
Move 42 — Regime conflict
Move 57 — Continuity collapse
Move 103 — Continuity alignment
Move 121 — Topology inversion
```

The viewer visually explains the entire triadic identity of the position.

---

## Developer Notes

- overlay data is JSON‑serializable  
- viewer is engine‑agnostic  
- RTT primitives come from the shim  
- rendering is deterministic  
- supports incremental updates  
- teaching/analysis modes share the same viewer  
- animations are optional but recommended  

---

## Summary

The Triadic Viewer is RTT‑Go’s **visual intelligence system**.

It reveals:

- structure  
- regime  
- topology  
- continuity  
- resonance  
- paradox  
- collapse  

and allows users to see Go through the triadic lens.

The viewer does not play Go — it **illuminates** it.
