# UI API — RTT‑Go  
*(Public Interface for Triadic UI Integration)*

The **RTT‑Go UI API** defines how external systems — engines, shims, viewers, HUDs, and developer tools — communicate with the RTT‑Go UI layer.  
It provides a stable, deterministic interface for:

- sending RTT triadic state  
- updating overlays  
- controlling the viewer  
- updating the HUD  
- driving the timeline  
- receiving diagnostics  
- integrating custom UI modules  

This API is the canonical contract for all RTT‑Go UI integrations.

---

## 1. API Purpose

The UI API provides:

- a unified message format  
- deterministic update semantics  
- engine‑agnostic triadic state ingestion  
- overlay control endpoints  
- HUD control endpoints  
- timeline control endpoints  
- viewer interaction endpoints  
- diagnostic retrieval  

It ensures the UI behaves consistently across all RTT‑Go modes.

---

# 2. API Overview

The RTT‑Go UI API is composed of five subsystems:

```
State API
Overlay API
HUD API
Viewer API
Timeline API
Diagnostics API
```

Each subsystem is defined below.

---

# 3. State API  
*(Primary entry point for RTT triadic state)*

### Endpoint: `ui.state.update`

Updates the entire UI state using the canonical JSON contract.

#### Input
```json
{
  "board": { ... },
  "moves": [ ... ],
  "triadic": { ... },
  "ui": { ... }
}
```

#### Behavior
- merges incremental updates  
- triggers overlay refresh  
- updates HUD panels  
- updates viewer state  
- updates timeline position  

#### Guarantees
- deterministic updates  
- no partial state corruption  
- schema validation  

---

# 4. Overlay API  
*(Controls visibility and behavior of overlay layers)*

### Endpoint: `ui.overlay.toggle`

Toggles overlay visibility.

#### Input
```json
{ "overlay": "continuity", "enabled": true }
```

### Endpoint: `ui.overlay.set_opacity`

Sets overlay opacity.

#### Input
```json
{ "overlay": "resonance", "opacity": 0.35 }
```

### Endpoint: `ui.overlay.set_palette`

Sets overlay color palette.

#### Input
```json
{ "overlay": "regime", "palette": "regime.json" }
```

### Endpoint: `ui.overlay.refresh`

Forces a full overlay redraw.

---

# 5. HUD API  
*(Controls HUD panels and metadata display)*

### Endpoint: `ui.hud.set_panel`

Sets the active HUD panel.

#### Input
```json
{ "panel": "continuity" }
```

### Endpoint: `ui.hud.lock_move`

Locks HUD to a specific move.

#### Input
```json
{ "move": 57 }
```

### Endpoint: `ui.hud.unlock`

Unlocks HUD from a move.

### Endpoint: `ui.hud.update`

Updates HUD metadata.

---

# 6. Viewer API  
*(Controls the Triadic Viewer)*

### Endpoint: `ui.viewer.highlight_move`

Highlights a move on the board.

#### Input
```json
{ "move": "D4" }
```

### Endpoint: `ui.viewer.show_overlay`

Shows a specific overlay layer.

### Endpoint: `ui.viewer.hide_overlay`

Hides a specific overlay layer.

### Endpoint: `ui.viewer.set_mode`

Sets viewer mode:

- `teaching`  
- `analysis`  
- `developer`  
- `composite`  

#### Input
```json
{ "mode": "analysis" }
```

---

# 7. Timeline API  
*(Controls playback of triadic evolution)*

### Endpoint: `ui.timeline.set_mode`

Sets timeline playback mode.

#### Input
```json
{ "mode": "flow" }
```

### Endpoint: `ui.timeline.seek`

Moves the timeline to a specific position.

#### Input
```json
{ "position": 57 }
```

### Endpoint: `ui.timeline.play`

Starts playback.

### Endpoint: `ui.timeline.pause`

Pauses playback.

### Endpoint: `ui.timeline.step_forward`

Moves forward one move.

### Endpoint: `ui.timeline.step_back`

Moves backward one move.

---

# 8. Diagnostics API  
*(Retrieves triadic diagnostic information)*

### Endpoint: `ui.diagnostics.get_move`

Returns triadic diagnostics for a specific move.

#### Input
```json
{ "move": 57 }
```

#### Output
```json
{
  "regime": { ... },
  "topology": { ... },
  "continuity": { ... },
  "resonance": { ... },
  "risk": { ... },
  "scores": { ... }
}
```

### Endpoint: `ui.diagnostics.get_state`

Returns full triadic state.

### Endpoint: `ui.diagnostics.get_overlay_state`

Returns overlay visibility + palette + opacity.

---

# 9. Event Model

The UI API emits events:

```
ui.state.changed
ui.overlay.changed
ui.hud.changed
ui.viewer.changed
ui.timeline.changed
ui.diagnostics.ready
```

Events are:

- debounced  
- deterministic  
- ordered  
- engine‑agnostic  

---

# 10. API Summary

The RTT‑Go UI API defines:

- state ingestion  
- overlay control  
- HUD control  
- viewer control  
- timeline control  
- diagnostics retrieval  
- event model  

It is the **public interface** for RTT‑Go’s triadic UI.

The API does not play Go — it **connects** Go’s triadic intelligence to the UI.
