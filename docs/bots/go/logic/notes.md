# Go Bot Logic — Developer Notes

This file contains internal notes for the Go bot logic layer.  
It documents how the bot interacts with Go engines (KataGo, Leela Zero, PhoenixGo), how the RTT shim integrates with engine outputs, and how move selection, search control, and continuity‑preserving behavior are implemented.

These notes are **developer‑facing** and not part of the public documentation.

---

## Overview

The Go bot logic layer is responsible for:

- managing engine inference (policy/value)
- controlling MCTS search parameters
- integrating RTT triadic scores
- selecting continuity‑preserving moves
- exposing diagnostics for teaching/analysis modes
- maintaining long‑arc positional context across moves

The logic layer sits between:

```
[Engine] <--> [RTT Shim] <--> [Bot Logic] <--> [UI / Discord / CLI]
```

---

## Engines Supported

### **KataGo**
- strongest engine
- provides policy, value, ownership, score lead, influence
- ideal for RTT integration

### **Leela Zero**
- pure policy/value network
- simpler MCTS
- RTT fills in missing structural signals

### **PhoenixGo**
- similar to Leela Zero
- stable, predictable MCTS behavior
- good for RTT teaching mode

---

## Core Responsibilities

### **1. Engine Invocation**
The logic layer handles:

- board encoding
- engine command execution
- parsing policy/value outputs
- managing MCTS parameters (visits, playouts, temperature)

### **2. RTT Integration**
The logic layer receives:

- triadic scores from Harmonia
- projection‑loss/paradox flags from Aurion
- regime profiles from Hephaestus
- structural maps from Lumen

It blends these with engine outputs.

### **3. Move Selection**
Move selection is based on:

- engine policy
- engine value
- triadic score
- continuity stability
- resonance alignment
- risk arc avoidance

### **4. Continuity Tracking**
The logic layer maintains:

- long‑arc positional identity
- moyo boundaries
- influence evolution
- ladder/ko ancestry
- continuity anchors

This context is passed to the RTT shim each turn.

### **5. Diagnostics**
In teaching/analysis modes, the logic layer exposes:

- regime tags
- resonance maps
- continuity arcs
- projection‑loss warnings
- paradox flags
- triadic score breakdowns

---

## Move Selection Pipeline

```text
[Engine Policy/Value]
      |
      v
[RTT Shim]
  - Lumen (structure)
  - Hephaestus (regime)
  - Aurion (topology)
  - Harmonia (triadic score)
      |
      v
[Bot Logic]
  - blend policy/value with triadic score
  - apply continuity constraints
  - prune paradoxical moves
  - mitigate projection-loss
      |
      v
[Final Move]
```

---

## Blending Strategy

The logic layer uses a configurable blending model:

### **Strict Triadic Mode**
RTT dominates engine evaluation.

### **Hybrid Mode**
RTT + engine blended equally.

### **Engine‑First Mode**
Engine dominates; RTT provides stability corrections.

### **Teaching Mode**
Engine plays normally; RTT overlays are shown.

### **Analysis Mode**
RTT evaluates human games; no move selection.

---

## Continuity Enforcement Rules

The logic layer prevents moves that:

- break moyo continuity
- collapse influence arcs
- destabilize ladders
- violate ancestry alignment
- introduce paradoxical ko fights
- abandon long‑arc territorial identity

These rules are applied after triadic scoring.

---

## Risk Management

Aurion provides:

- projection‑loss risk
- paradox severity
- ladder ancestry risk
- ko instability risk
- framework collapse risk

The logic layer:

- downweights risky moves
- prunes catastrophic moves
- boosts stabilizing alternatives

---

## Engine‑Specific Notes

### **KataGo**
- ownership maps help Lumen
- score lead helps Harmonia
- influence maps reduce RTT workload

### **Leela Zero**
- RTT must compute influence manually
- continuity arcs rely heavily on history
- paradox detection is more important

### **PhoenixGo**
- stable MCTS makes RTT blending predictable
- good for testing continuity enforcement

---

## Future Extensions

- multi‑engine consensus mode  
- RTT‑guided playout pruning  
- long‑arc positional memory across games  
- teaching mode visual overlays  
- full RTT‑Go analysis suite  

---

> **“Logic is where engine strength meets triadic strategy.”**
