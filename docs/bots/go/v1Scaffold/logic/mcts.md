# MCTS Logic — Go Bot  
*(RTT‑Enhanced Search Control)*

This document describes how the Go bot manages **Monte Carlo Tree Search (MCTS)** across supported engines (KataGo, Leela Zero, PhoenixGo), and how RTT triadic signals modify search behavior to produce continuity‑preserving, resonance‑aligned decision flow.

The MCTS layer is responsible for:

- controlling search parameters  
- integrating RTT triadic scores into node expansion  
- enforcing continuity constraints  
- pruning paradoxical or collapse‑risk lines  
- stabilizing long‑arc strategy during search  

---

## Overview

RTT does not replace MCTS.  
It **augments** it — injecting structural, regime, topology, and continuity signals into the search loop.

The MCTS logic layer sits between:

```
[Engine MCTS] <--> [RTT Shim] <--> [Bot Logic]
```

Each engine provides its own MCTS implementation:

- **KataGo** — advanced, feature‑rich MCTS  
- **Leela Zero** — classic MCTS with policy/value  
- **PhoenixGo** — stable, predictable MCTS  

RTT integrates cleanly with all three.

---

## Core Responsibilities

### **1. Search Parameter Control**
The bot manages:

- number of visits  
- playout limits  
- exploration constants  
- temperature  
- early‑exit conditions  
- time‑control constraints  

### **2. RTT‑Aware Node Expansion**
During node expansion, RTT modifies:

- child ordering  
- exploration weights  
- pruning thresholds  
- continuity penalties  
- paradox penalties  
- projection‑loss penalties  
- resonance bonuses  

### **3. Continuity‑Preserving Search**
RTT ensures MCTS does not:

- break moyo continuity  
- collapse influence arcs  
- destabilize ladders  
- violate ancestry alignment  
- introduce paradoxical ko fights  

### **4. Risk‑Arc Avoidance**
Aurion provides:

- ladder ancestry risk  
- ko instability risk  
- framework collapse risk  
- continuity‑arc collapse risk  

The MCTS layer prunes or downweights risky lines.

### **5. Triadic Score Injection**
Harmonia’s unified triadic scores are injected into:

- node priors  
- node value estimates  
- child selection heuristics  

---

## MCTS Flow with RTT

```text
[Engine NN Inference]
      |
      v
[RTT Shim]
  - Lumen (structure)
  - Hephaestus (regime)
  - Aurion (topology)
  - Harmonia (triadic score)
      |
      v
[MCTS Logic]
  - adjust priors
  - reorder children
  - prune paradox lines
  - enforce continuity
      |
      v
[Search Tree]
      |
      v
[Final Move]
```

---

## RTT Modifications to MCTS

### **1. Prior Adjustment**
RTT modifies engine priors:

```
prior = engine_policy * (1 + triadic_score)
```

High triadic score → boosted prior  
Low triadic score → suppressed prior

### **2. Value Adjustment**
RTT adjusts engine value estimates:

```
value = engine_value + continuity_bonus - collapse_penalty
```

### **3. Child Reordering**
Children are sorted by:

1. triadic score  
2. continuity stability  
3. resonance alignment  
4. engine policy/value  

### **4. Paradox Pruning**
Aurion flags paradoxical moves:

- locally good  
- globally catastrophic  

These moves are:

- downweighted  
- pruned if severe  

### **5. Projection‑Loss Mitigation**
Moves that cause structural collapse receive:

- heavy penalties  
- reduced exploration  
- early pruning  

### **6. Continuity Enforcement**
Moves that break continuity arcs are:

- downweighted  
- pruned if collapse‑risk is high  

---

## Engine‑Specific Notes

### **KataGo**
- ownership maps improve Lumen  
- score lead improves Harmonia  
- influence maps reduce RTT workload  
- MCTS is highly responsive to triadic priors  

### **Leela Zero**
- RTT computes influence manually  
- continuity arcs rely heavily on history  
- paradox detection is more important  
- MCTS is simple but predictable  

### **PhoenixGo**
- stable MCTS makes RTT blending smooth  
- ideal for teaching/analysis modes  
- continuity enforcement is highly effective  

---

## Example Pseudocode

```text
function rtt_mcts_select(node):
    children = node.children

    for child in children:
        child.prior = blend_policy(child.engine_prior, child.triadic_score)
        child.value = blend_value(child.engine_value, child.continuity_score)

        if child.paradox_risk > threshold:
            child.prior *= paradox_penalty

        if child.projection_loss > threshold:
            child.prior *= collapse_penalty

    return argmax(children, child.prior + child.value)
```

---

## Continuity‑Preserving Search Rules

The MCTS layer prevents moves that:

- break moyo continuity  
- collapse influence arcs  
- destabilize ladders  
- violate ancestry alignment  
- introduce paradoxical ko fights  
- abandon long‑arc territorial identity  

These rules are applied at **every node expansion**.

---

## Future Extensions

- multi‑engine consensus search  
- RTT‑guided playout pruning  
- long‑arc positional memory across games  
- teaching mode visual overlays  
- full RTT‑Go search diagnostics  

---

> **“MCTS is the engine’s strength. RTT is its strategy.”**
