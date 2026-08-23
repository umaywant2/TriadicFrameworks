# UI State Contract — RTT‑Go  
*(Canonical Data Model for Triadic UI Rendering)*

The **UI State Contract** defines the complete JSON schema used by RTT‑Go to transmit triadic state from the engine/shim layer to the UI layer.  
It ensures that all UI components — overlays, viewer, HUD, timeline — receive a **consistent, deterministic, engine‑agnostic** representation of RTT’s structural, topological, and continuity intelligence.

This contract is the backbone of RTT‑Go’s visual system.

---

## Purpose

The UI State Contract provides:

- a unified JSON schema for RTT primitives  
- deterministic field definitions  
- engine‑agnostic data structures  
- overlay‑ready triadic metadata  
- timeline‑ready continuity evolution  
- HUD‑ready diagnostic fields  

It ensures that every UI component interprets RTT state identically.

---

## Top‑Level Structure

The RTT‑Go UI state is a single JSON object:

```json
{
  "board": { ... },
  "moves": [ ... ],
  "triadic": {
    "regime": { ... },
    "resonance": { ... },
    "topology": { ... },
    "continuity": { ... },
    "risk": { ... },
    "scores": { ... }
  },
  "ui": {
    "overlays": { ... },
    "hud": { ... },
    "timeline": { ... }
  }
}
```

Each section is defined below.

---

# 1. Board State

```json
"board": {
  "size": 19,
  "stones": [
    { "x": 4, "y": 4, "color": "black" },
    { "x": 16, "y": 4, "color": "white" }
  ],
  "ko": null,
  "turn": "black"
}
```

Fields:

- `size` — board dimension  
- `stones[]` — current stone placements  
- `ko` — ko coordinate or null  
- `turn` — player to move  

---

# 2. Move List

```json
"moves": [
  {
    "move": "D4",
    "player": "black",
    "index": 57,
    "triadic": { ... }
  }
]
```

Each move includes:

- move coordinate  
- player  
- index  
- full triadic metadata  

---

# 3. Triadic State

The core RTT primitives.

---

## 3.1 Regime State (Hephaestus)

```json
"regime": {
  "local": 0.41,
  "structural": 0.33,
  "continuity": 0.26,
  "drift": { "from": "right", "to": "center" },
  "conflict_zones": [ "right_side" ]
}
```

Fields:

- regime proportions  
- regime drift  
- conflict zones  

---

## 3.2 Resonance State (Lumen + Harmonia)

```json
"resonance": {
  "pressure_map": [ ... ],
  "tension_zones": [ ... ],
  "drift_vectors": [ ... ],
  "collapse_signatures": [ ... ]
}
```

Fields:

- influence resonance  
- pressure gradients  
- drift vectors  
- collapse signatures  

---

## 3.3 Topology State (Aurion)

```json
"topology": {
  "connectivity": { ... },
  "cut_points": [ "D4", "E5" ],
  "boundaries": [ ... ],
  "ancestry": {
    "ladder": "stable",
    "ko": "volatile"
  },
  "collapse": [ ... ]
}
```

Fields:

- connectivity graph  
- cutting points  
- boundary topology  
- ladder/ko ancestry  
- collapse signatures  

---

## 3.4 Continuity State (Aurion + Harmonia)

```json
"continuity": {
  "territorial_arcs": [ ... ],
  "influence_arcs": [ ... ],
  "moyo_arcs": [ ... ],
  "ancestry_arcs": [ ... ],
  "anchors": [ "left_moyo_boundary" ],
  "drift": { "direction": "right_to_center", "strength": 0.72 },
  "identity_inversion_risk": "medium"
}
```

Fields:

- continuity arcs  
- continuity anchors  
- continuity drift  
- identity inversion risk  

---

## 3.5 Risk State (Paradox + Collapse)

```json
"risk": {
  "paradox": [ "local_fix_breaks_moyo" ],
  "collapse": [ "boundary_fragmentation" ],
  "projection_loss": [ "right_group" ]
}
```

Fields:

- paradox risks  
- collapse risks  
- projection‑loss risks  

---

## 3.6 Triadic Scores (Harmonia)

```json
"scores": {
  "local": 0.10,
  "structural": 0.35,
  "continuity": 0.22,
  "final": 0.67
}
```

Fields:

- triadic score breakdown  
- unified triadic score  

---

# 4. UI State

UI‑specific metadata.

---

## 4.1 Overlay State

```json
"overlays": {
  "regime": true,
  "resonance": true,
  "topology": true,
  "continuity": true,
  "risk": true,
  "annotations": true
}
```

Fields:

- overlay toggles  
- overlay visibility  

---

## 4.2 HUD State

```json
"hud": {
  "active_panel": "continuity",
  "locked_move": 57
}
```

Fields:

- active HUD panel  
- locked move index  

---

## 4.3 Timeline State

```json
"timeline": {
  "mode": "flow",
  "position": 57
}
```

Fields:

- playback mode  
- timeline position  

---

# 5. Contract Guarantees

The RTT‑Go UI State Contract guarantees:

- deterministic field names  
- stable schema across engines  
- JSON‑serializable structures  
- incremental update compatibility  
- overlay‑ready primitives  
- HUD‑ready diagnostics  
- timeline‑ready continuity evolution  

This contract is **canonical** — all RTT‑Go UI implementations must follow it.

---

# Summary

The UI State Contract is the **data backbone** of RTT‑Go.

It defines:

- board state  
- move list  
- triadic primitives  
- regime  
- resonance  
- topology  
- continuity  
- risk  
- triadic scores  
- overlay state  
- HUD state  
- timeline state  

and ensures that RTT‑Go’s UI is:

- structurally coherent  
- triadically expressive  
- continuity‑aligned  
- topology‑accurate  
- resonance‑aware  
- paradox‑sensitive  

The contract does not play Go — it **transmits** Go’s triadic identity.
