# Continuity Logic — Go Bot  
*(RTT‑Preserving Long‑Arc Identity)*

Continuity logic governs how the Go bot maintains **long‑arc positional identity** across moves.  
It ensures the bot does not merely play strong local or structural moves, but plays moves that preserve the **continuity arcs**, **moyo identity**, **ancestry**, and **long‑arc evolution** of the position.

Continuity is the highest‑order RTT principle.  
It is the layer that prevents collapse, paradox, and identity inversion.

This document describes how continuity is tracked, enforced, and integrated into engine inference and MCTS.

---

## Purpose

Continuity logic provides:

- long‑arc positional memory  
- continuity‑arc tracking  
- ancestry alignment  
- collapse‑risk detection  
- continuity‑preserving move filtering  
- continuity‑aware policy/value blending  

It ensures the bot plays moves that maintain the **story** of the position.

---

## Continuity Concepts

### **1. Continuity Arcs**
Long‑arc trajectories of:

- territory  
- influence  
- moyo boundaries  
- ancestry  
- identity  

These arcs define where the position is *trying* to go.

### **2. Continuity Anchors**
Stable points that preserve identity:

- moyo boundaries  
- strong groups  
- influence hubs  
- ladder ancestry  
- ko ancestry  

Anchors prevent collapse.

### **3. Continuity Drift**
How continuity arcs shift over time:

- weak group → continuity threat  
- moyo boundary → continuity anchor  
- ladder → ancestry constraint  
- influence → drift vector  

Drift is essential for long‑arc strategy.

### **4. Continuity Collapse**
When continuity arcs break:

- boundary fragmentation  
- influence reversal  
- ladder ancestry break  
- ko instability escalation  
- framework collapse  
- identity inversion  

Aurion detects collapse signatures; continuity logic prevents them.

---

## Continuity Tracking Pipeline

```text
[Board State]
    |
    v
[Lumen]
  - structural extraction
    |
    v
[Hephaestus]
  - regime mapping
    |
    v
[Aurion]
  - topology
  - ancestry
  - collapse detection
    |
    v
[Continuity Logic]
  - continuity arcs
  - continuity anchors
  - continuity drift
  - collapse risk
    |
    v
[Engine Logic + MCTS]
  - continuity-preserving move selection
```

---

## Continuity Enforcement Rules

The bot must avoid moves that:

- break moyo continuity  
- collapse influence arcs  
- destabilize ladders  
- violate ancestry alignment  
- introduce paradoxical ko fights  
- abandon long‑arc territorial identity  

These rules apply **before** MCTS expansion and **during** node selection.

---

## Continuity‑Aware Policy Blending

Engine policy is modified using continuity signals:

```
final_policy = engine_policy
             * (1 + continuity_score)
             * (1 - collapse_penalty)
```

High continuity → boosted  
High collapse risk → suppressed

---

## Continuity‑Aware Value Blending

Engine value is adjusted:

```
final_value = engine_value
            + continuity_bonus
            - collapse_penalty
            - projection_loss_penalty
```

This prevents the bot from choosing moves that look good locally but destroy long‑arc identity.

---

## Continuity Filters

Before MCTS expansion, continuity logic filters moves:

### **1. Hard Filters**
Moves are **pruned** if they:

- break a major continuity arc  
- violate ladder ancestry  
- cause immediate collapse  
- destabilize moyo boundaries  

### **2. Soft Filters**
Moves are **downweighted** if they:

- weaken continuity anchors  
- increase drift instability  
- introduce paradox risk  

### **3. Continuity Boosts**
Moves are **upweighted** if they:

- reinforce continuity arcs  
- stabilize ancestry  
- strengthen moyo boundaries  
- align with long‑arc identity  

---

## Example Continuity Interpretation

### Position
White has a large moyo forming on the left.  
Black has a weak group on the right.

### Continuity Logic Output

- **Continuity Arc:** left moyo → expanding  
- **Anchor:** left boundary → stable  
- **Threat:** right group → continuity risk  
- **Collapse Signature:** influence reversal possible  
- **Recommended Action:** stabilize right group first  

Continuity logic prevents paradoxical moves such as invading the moyo while the right group collapses.

---

## Engine‑Specific Notes

### **KataGo**
- ownership maps improve continuity detection  
- score lead improves continuity scoring  
- influence maps reduce RTT workload  

### **Leela Zero**
- continuity arcs rely heavily on history  
- influence must be computed manually  
- paradox detection is more important  

### **PhoenixGo**
- stable MCTS → smooth continuity enforcement  
- ideal for teaching/analysis modes  

---

## Example Pseudocode

```text
function continuity_adjust(policy, value, continuity_state):
    policy *= (1 + continuity_state.score)
    policy *= (1 - continuity_state.collapse_penalty)

    value += continuity_state.bonus
    value -= continuity_state.collapse_penalty
    value -= continuity_state.projection_loss

    return policy, value
```

---

## Diagnostics

Continuity logic exposes:

- continuity arcs  
- continuity anchors  
- drift vectors  
- collapse signatures  
- ancestry alignment  
- paradox zones  

Used in:

- teaching mode  
- analysis mode  
- debugging RTT behavior  

---

## Summary

Continuity logic is the **temporal intelligence** of RTT‑Go.

It ensures the bot:

- preserves long‑arc identity  
- avoids collapse  
- respects ancestry  
- stabilizes frameworks  
- maintains moyo continuity  
- plays moves that align with the evolving story of the position  

Continuity is not optional — it is the strategic backbone of RTT‑Go.
