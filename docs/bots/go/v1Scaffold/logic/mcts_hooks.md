# MCTS Hooks — RTT‑Go  
*(Unified Triadic Integration Points for Go Engines)*

The **RTT‑Go MCTS Hooks** define how RTT integrates with any Go engine’s Monte Carlo Tree Search (MCTS).  
These hooks are engine‑agnostic and apply to:

- KataGo  
- Leela Zero  
- PhoenixGo  
- future engines using policy/value + MCTS

RTT does **not** replace MCTS.  
It **augments** it — injecting triadic intelligence into:

- node priors  
- node values  
- node ordering  
- pruning  
- exploration  
- continuity enforcement  

This document defines the complete RTT‑Go MCTS integration model.

---

## 1. Purpose

RTT hooks provide:

- triadic reweighting of policy priors  
- continuity‑aware value adjustments  
- paradox/collapse suppression  
- continuity‑preserving node ordering  
- drift/coherence‑aligned exploration  
- pruning of collapse‑risk lines  
- ancestry‑aware search stability  

These hooks allow RTT to guide the engine without replacing its core logic.

---

## 2. MCTS Hook Overview

RTT attaches to five points in the MCTS loop:

```
1. Policy Priors
2. Value Estimates
3. Node Expansion
4. Child Ordering
5. Pruning
```

Each hook is optional — but together they form the full triadic integration.

---

# 3. Hook 1 — Policy Priors  
*(Triadic Prior Reweighting)*

Engines produce a raw policy distribution:

```
policy[move] = probability
```

RTT computes a triadic score:

```
triadic_score[move]
```

RTT blends them:

```
final_policy[move] = blend(policy[move], triadic_score[move])
```

Blend modes:

- **strict triadic** — RTT dominates  
- **hybrid** — RTT + engine balanced  
- **teaching mode** — RTT annotations only  
- **analysis mode** — no blending  

Effects:

- continuity‑preserving moves rise  
- collapse‑risk moves fall  
- paradox moves are suppressed  
- long‑arc moves gain stability  

---

# 4. Hook 2 — Value Estimates  
*(Continuity‑Aware Value Adjustment)*

Engines produce a raw value:

```
value = win_probability
```

RTT adjusts this using:

- continuity arcs  
- projection‑loss risk  
- ancestry alignment  
- drift/coherence  
- collapse signatures  

Final value:

```
final_value = blend(value, continuity_score)
```

Effects:

- continuity‑aligned lines gain confidence  
- collapse‑risk lines lose confidence  
- paradox lines are penalized  

---

# 5. Hook 3 — Node Expansion  
*(Triadic‑Stable Expansion)*

During node expansion, RTT modifies:

- exploration constants  
- expansion order  
- expansion thresholds  

Rules:

- continuity‑preserving children expand earlier  
- collapse‑risk children expand later or not at all  
- paradox children are downweighted  
- drift‑aligned children receive exploration bonuses  

This stabilizes long‑arc strategy.

---

# 6. Hook 4 — Child Ordering  
*(Triadic Ordering of Candidate Moves)*

RTT sorts children using:

1. triadic score  
2. continuity stability  
3. resonance pressure  
4. ancestry alignment  
5. engine policy/value  

This ordering is used by:

- KataGo  
- Leela Zero  
- PhoenixGo  

Effects:

- stable long‑arc lines rise  
- collapse‑risk lines fall  
- paradox lines are deprioritized  

---

# 7. Hook 5 — Pruning  
*(Paradox, Collapse, Projection‑Loss)*

RTT prunes moves that:

- break moyo continuity  
- collapse influence arcs  
- violate ladder ancestry  
- introduce paradoxical ko loops  
- destabilize long‑arc identity  

Pruning modes:

- **soft prune** — downweight  
- **medium prune** — deprioritize  
- **hard prune** — remove from search  

Engines remain in control — RTT only influences.

---

# 8. Unified Hook Flow

```
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
[RTT MCTS Hooks]
  1. Policy Priors
  2. Value Estimates
  3. Node Expansion
  4. Child Ordering
  5. Pruning
      |
      v
[Engine MCTS]
```

This is the **canonical RTT‑Go MCTS integration pipeline**.

---

# 9. Engine‑Specific Notes

### **KataGo**
- rich MCTS  
- RTT hooks deeply into node expansion  
- policy/value blending highly effective  

### **Leela Zero**
- classic MCTS  
- RTT hooks primarily into priors + ordering  

### **PhoenixGo**
- stable MCTS  
- RTT hooks produce extremely stable continuity behavior  

---

# 10. Summary

RTT‑Go MCTS Hooks provide:

- triadic priors  
- continuity‑aware values  
- stable expansion  
- triadic ordering  
- paradox/collapse pruning  

They allow RTT to guide any Go engine while preserving its native logic.

RTT does not play Go — it **reveals** Go’s triadic identity inside the search.
