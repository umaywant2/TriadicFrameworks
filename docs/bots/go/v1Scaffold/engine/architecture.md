# RTT‑Go Engine Architecture  
*(Internal Structure of the Triadic Bot Logic Layer)*

The **RTT‑Go Engine Architecture** defines the computational structure of RTT‑Go — the triadic Go engine built on Resonance‑Time Theory (RTT).  
It describes how the engine evaluates positions, computes triadic primitives, detects paradox/collapse events, and emits the unified triadic state consumed by the UI.

This document is the **blueprint** for the entire bot logic layer.

---

## 1. Purpose

The engine architecture provides:

- a deterministic evaluation pipeline  
- modular triadic primitive generators  
- structural/topological analysis  
- continuity‑arc computation  
- resonance field computation  
- paradox/collapse detection  
- triadic scoring  
- unified state emission  

It is the **thinking layer** of RTT‑Go.

---

## 2. Engine Overview

The RTT‑Go engine is composed of eight modules:

```
RegimeEngine
ResonanceEngine
TopologyEngine
ContinuityEngine
RiskEngine
ScoringEngine
StateEmitter
EngineShim
```

These modules form a directed evaluation pipeline.

---

## 3. Evaluation Pipeline

The engine processes each position using a deterministic pipeline:

```
Board State
   ↓
RegimeEngine
   ↓
ResonanceEngine
   ↓
TopologyEngine
   ↓
ContinuityEngine
   ↓
RiskEngine
   ↓
ScoringEngine
   ↓
StateEmitter
```

Each module consumes the output of the previous module and enriches the triadic state.

---

# 4. Module Specifications

## 4.1 RegimeEngine  
*(Hephaestus — local/structural/continuity regime)*

### Responsibilities
- compute regime proportions  
- detect regime drift  
- identify conflict zones  
- evaluate regime stability  

### Outputs
```
regime.local
regime.structural
regime.continuity
regime.drift
regime.conflict_zones
```

---

## 4.2 ResonanceEngine  
*(Lumen + Harmonia — influence, pressure, tension)*

### Responsibilities
- compute influence resonance  
- compute pressure gradients  
- detect tension zones  
- compute drift vectors  
- detect collapse signatures  

### Outputs
```
resonance.pressure_map
resonance.tension_zones
resonance.drift_vectors
resonance.collapse_signatures
```

---

## 4.3 TopologyEngine  
*(Aurion — connectivity, boundaries, ancestry)*

### Responsibilities
- compute connectivity graph  
- detect cutting points  
- compute boundary topology  
- compute ladder/ko ancestry  
- detect topology collapse  

### Outputs
```
topology.connectivity
topology.cut_points
topology.boundaries
topology.ancestry
topology.collapse
```

---

## 4.4 ContinuityEngine  
*(Aurion + Harmonia — long‑arc identity)*

### Responsibilities
- compute territorial arcs  
- compute influence arcs  
- compute moyo arcs  
- compute ancestry arcs  
- detect continuity anchors  
- compute continuity drift  
- detect identity inversion risk  

### Outputs
```
continuity.territorial_arcs
continuity.influence_arcs
continuity.moyo_arcs
continuity.ancestry_arcs
continuity.anchors
continuity.drift
continuity.identity_inversion_risk
```

---

## 4.5 RiskEngine  
*(Paradox, collapse, projection‑loss)*

### Responsibilities
- detect paradox events  
- detect collapse events  
- detect projection‑loss events  
- compute risk severity  

### Outputs
```
risk.paradox
risk.collapse
risk.projection_loss
risk.severity
```

---

## 4.6 ScoringEngine  
*(Harmonia — unified triadic scoring)*

### Responsibilities
- compute local score  
- compute structural score  
- compute continuity score  
- compute unified triadic score  

### Outputs
```
scores.local
scores.structural
scores.continuity
scores.final
```

---

## 4.7 StateEmitter  
*(Unified triadic JSON state)*

### Responsibilities
- assemble board state  
- assemble move list  
- assemble triadic primitives  
- assemble overlay state  
- assemble HUD state  
- assemble timeline state  

### Output Format
The emitter produces the canonical UI state contract:

```
{
  "board": { ... },
  "moves": [ ... ],
  "triadic": { ... },
  "ui": { ... }
}
```

---

## 4.8 EngineShim  
*(Engine‑agnostic integration layer)*

### Responsibilities
- receive board state from external engines  
- normalize engine‑specific primitives  
- feed normalized state into RTT pipeline  
- ensure deterministic evaluation  

The shim allows RTT‑Go to integrate with any Go engine.

---

# 5. Engine Guarantees

The RTT‑Go engine guarantees:

- deterministic triadic evaluation  
- engine‑agnostic integration  
- stable module interfaces  
- JSON‑serializable output  
- incremental update compatibility  
- full compatibility with RTT‑Go UI  

---

# 6. Summary

The RTT‑Go Engine Architecture defines the **complete computational structure** of RTT‑Go.

It describes:

- the evaluation pipeline  
- regime computation  
- resonance computation  
- topology computation  
- continuity computation  
- risk computation  
- triadic scoring  
- unified state emission  

The engine does not play Go — it **interprets** Go through the triadic lens.
