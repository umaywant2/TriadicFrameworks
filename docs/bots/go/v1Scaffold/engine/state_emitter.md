# State Emitter — RTT‑Go  
*(Unified Triadic JSON Output Layer)*

The **State Emitter** is the final module in the RTT‑Go evaluation pipeline.  
It assembles all triadic primitives — regime, resonance, topology, continuity, risk, scoring — into a single unified JSON state consumed by the RTT‑Go UI.

Where the other engine modules compute triadic identity, the State Emitter **publishes** that identity in a canonical, UI‑ready format.

This module defines the **output layer** of RTT‑Go.

---

## 1. Purpose

The State Emitter provides:

- unified triadic JSON state  
- board state  
- move list  
- triadic primitives  
- overlay state  
- HUD state  
- timeline state  
- engine metadata  

It is the **serialization and publication engine** of RTT‑Go.

---

## 2. Inputs

The State Emitter consumes the outputs of all upstream modules:

```
RegimeEngine → regime.*
ResonanceEngine → resonance.*
TopologyEngine → topology.*
ContinuityEngine → continuity.*
RiskEngine → risk.*
ScoringEngine → scores.*
EngineShim → board.*, moves[]
```

These inputs are guaranteed to be normalized and deterministic.

---

## 3. Output Format

The State Emitter produces the canonical RTT‑Go UI state contract:

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
  },
  "meta": {
    "engine_version": "1.0.0",
    "triadic_version": "2026",
    "generated_at": "ISO-8601 timestamp"
  }
}
```

This is the **exact structure** expected by the RTT‑Go UI.

---

# 4. Emission Model

The State Emitter follows a deterministic assembly pipeline:

```
Board State
   ↓
Move List
   ↓
Triadic Primitives
   ↓
Overlay State
   ↓
HUD State
   ↓
Timeline State
   ↓
Metadata
   ↓
Unified JSON Output
```

Each stage enriches the final JSON object.

---

# 5. Component Assembly

## 5.1 Board State

Includes:

- board size  
- stones  
- turn  
- ko  
- captures  
- engine‑agnostic metadata  

Example:

```
board.size = 19
board.stones = [...]
board.turn = "black"
```

---

## 5.2 Move List

Includes:

- move coordinates  
- move number  
- player  
- triadic metadata per move  

Example:

```
moves[37].triadic.regime.local = 0.41
```

---

## 5.3 Triadic Primitives

Includes:

- regime  
- resonance  
- topology  
- continuity  
- risk  
- scores  

These are inserted exactly as computed by upstream modules.

---

## 5.4 Overlay State

Includes:

- overlay toggles  
- overlay opacity  
- overlay mode  
- overlay metadata  

Example:

```
ui.overlays.regime.enabled = true
ui.overlays.topology.opacity = 0.75
```

---

## 5.5 HUD State

Includes:

- active panel  
- commentary lock state  
- triadic metadata for display  
- risk indicators  

Example:

```
ui.hud.active_panel = "continuity"
```

---

## 5.6 Timeline State

Includes:

- current position  
- playback mode  
- delta metadata  
- collapse/paradox events  

Example:

```
ui.timeline.mode = "arc"
ui.timeline.position = 37
```

---

## 5.7 Metadata

Includes:

- engine version  
- triadic version  
- timestamp  
- deterministic hash  

Example:

```
meta.generated_at = "2026-08-23T22:05:00Z"
```

---

# 6. Determinism Guarantees

The State Emitter guarantees:

- deterministic output  
- stable field ordering  
- stable schema  
- JSON‑serializable structure  
- compatibility with RTT‑Go UI  
- compatibility with diagnostics + timeline  

The emitter never mutates upstream data — it only assembles.

---

# 7. Integration Points

### **StateEmitter → UI**
Provides the full triadic state for:

- viewer  
- overlays  
- HUD  
- timeline  

### **StateEmitter → Diagnostics**
Provides move‑indexed triadic metadata.

### **StateEmitter → Timeline**
Provides delta metadata for playback.

### **StateEmitter → EngineShim**
Receives normalized board + move data.

---

# 8. Summary

The State Emitter is RTT‑Go’s **publication engine**.

It assembles:

- board state  
- move list  
- triadic primitives  
- overlay state  
- HUD state  
- timeline state  
- metadata  

into a single unified JSON object consumed by the UI.

The State Emitter does not play Go — it **publishes** Go’s triadic identity.
