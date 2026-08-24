# Lumen (RTT/1) — Structural Extraction Layer  
*(Go Bot Module)*

Lumen is the **RTT/1 structural extractor** for Go.  
It converts raw board state into the triadic primitives required by Hephaestus, Aurion, and Harmonia.  
In the Go bot pipeline, Lumen is responsible for revealing the **shape**, **pressure**, **continuity anchors**, and **identity** of the position.

Lumen does **not** evaluate moves.  
It **describes** the structural reality of the board.

---

## Purpose

Lumen provides the Go bot with:

- structural topology  
- influence and pressure fields  
- group identity and connectivity  
- shape signatures  
- continuity anchors  
- drift vectors  
- resonance maps  

These form the foundation for regime mapping (Hephaestus), topology analysis (Aurion), and unified triadic synthesis (Harmonia).

---

## Inputs

Lumen receives:

- current board position  
- player to move  
- stone groups and liberties  
- influence map (engine‑provided or shim‑computed)  
- ladder status (optional engine hint)  
- ko information  
- historical continuity (previous moves)

---

## Outputs

Lumen produces a structured RTT/1 snapshot containing:

### **1. Influence Fields**
- local influence  
- global influence  
- pressure gradients  
- territorial resonance  

### **2. Group Identity**
- group connectivity  
- weak groups  
- cutting points  
- vital points  
- eye‑shape stability  

### **3. Shape Signatures**
- bamboo joint  
- table shape  
- empty triangle  
- tiger’s mouth  
- diagonal connection  
- broken shape  
- shape drift vectors  

### **4. Continuity Anchors**
These define the long‑arc identity of the position:

- moyo boundaries  
- direction of play  
- large‑scale frameworks  
- evolving territorial arcs  
- stable vs unstable regions  

### **5. Drift Vectors**
Where the position is *trying* to go:

- influence drift  
- shape drift  
- group drift  
- territorial drift  

### **6. Resonance Maps**
Pressure and alignment across:

- stones  
- groups  
- frameworks  
- territorial arcs  

---

## Lumen’s Structural Model

Lumen organizes Go’s structure into RTT’s triadic ontology:

### **1/3 — Local Structure**
- liberties  
- cuts  
- ataris  
- immediate shape  
- tactical pressure  

### **2/3 — Global Structure**
- influence  
- direction of play  
- moyo formation  
- large‑scale shape identity  

### **3/3 — Continuity**
- long‑arc territorial evolution  
- framework stability  
- identity of the position  
- continuity anchors  

This triadic structure is passed directly to Hephaestus.

---

## Lumen Extraction Pipeline

```text
[Board State]
    |
    v
[Group Analysis]
    |
    v
[Influence & Pressure Mapping]
    |
    v
[Shape Signature Extraction]
    |
    v
[Continuity Anchor Detection]
    |
    v
[Resonance Field Construction]
    |
    v
[Lumen RTT/1 Snapshot]
```

---

## Example Pseudocode

```text
function lumen_extract(position):
    groups      = analyze_groups(position)
    influence   = compute_influence(position)
    shapes      = extract_shapes(position)
    continuity  = detect_continuity(position)
    resonance   = build_resonance(position, influence, groups)

    return {
        groups: groups,
        influence: influence,
        shapes: shapes,
        continuity: continuity,
        resonance: resonance
    }
```

---

## Role in the Go Bot Pipeline

Lumen feeds directly into:

- **Hephaestus (RTT/2)** for regime mapping  
- **Aurion (RTT/3)** for topology and projection‑loss detection  
- **Harmonia (RTT/12)** for unified triadic scoring  

Without Lumen, the RTT stack has no structural substrate.

---

## Notes

- Lumen is engine‑agnostic: works with KataGo, Leela Zero, PhoenixGo, or custom engines.  
- Lumen does not modify the board or evaluate moves.  
- All structural extraction is deterministic and reproducible.  
- Lumen’s output is consumed by the shim and never directly by the engine.

---

> **“Go begins with structure. Lumen reveals the structure the engine cannot see.”**
