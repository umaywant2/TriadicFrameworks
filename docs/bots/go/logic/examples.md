# Logic Examples — Go Bot  
*(RTT‑Enhanced Engine + MCTS Integration)*

This document provides **developer‑facing examples** demonstrating how the Go bot’s logic layer blends engine outputs with RTT triadic signals (Lumen → Hephaestus → Aurion → Harmonia) to produce continuity‑preserving, resonance‑aligned move decisions.

These examples illustrate:

- engine inference  
- RTT primitive extraction  
- triadic score blending  
- continuity enforcement  
- paradox/prior collapse avoidance  
- MCTS node selection behavior  

---

## Example 1 — Engine Policy + Triadic Score Blending

### Position
Black has a weak group on the right.  
White has a large moyo forming on the left.

### Engine Output (KataGo)
```
policy:
  A: 0.42
  B: 0.33
  C: 0.25

value: 0.54
```

### RTT Output
- **A:** local (1/3), paradox risk  
- **B:** structural (2/3), stabilizing  
- **C:** continuity (3/3), risky due to weak group  

Triadic scores:
```
A: 0.10
B: 0.35
C: 0.22
```

### Blended Policy
```
final_policy[A] = 0.42 * (1 + 0.10) = 0.462
final_policy[B] = 0.33 * (1 + 0.35) = 0.445
final_policy[C] = 0.25 * (1 + 0.22) = 0.305
```

### Result
Move **B** rises from second to first due to structural + continuity alignment.

---

## Example 2 — Continuity Enforcement Overrides Engine Value

### Engine Value
```
value = 0.61
```

### RTT Continuity Signals
- moyo boundary at risk  
- weak group collapsing  
- continuity arc breaking  
- projection‑loss penalty = 0.18  

### Adjusted Value
```
final_value = 0.61 - 0.18 = 0.43
```

The bot avoids a move that looks good to the engine but destroys long‑arc identity.

---

## Example 3 — Paradox Pruning in MCTS

### Candidate Move
Move **A** fixes a local shape defect but breaks moyo continuity.

### Aurion Flags
- paradox severity: high  
- continuity collapse risk: medium  
- ancestry misalignment: high  

### MCTS Behavior
```
child.prior *= paradox_penalty
child.prior *= collapse_penalty
```

If penalties drop the prior below threshold, the node is **pruned**.

### Result
Move **A** is removed from search entirely.

---

## Example 4 — Ladder Ancestry Controls Search

### Position
A ladder determines global influence.

### Engine Policy
Engine suggests ignoring the ladder.

### RTT Output
- ladder ancestry arc = critical  
- ancestry break = catastrophic  
- projection‑loss = high  

### MCTS Adjustment
```
child.prior *= 0.05
child.value -= 0.20
```

### Result
Search avoids lines that break ladder ancestry.

---

## Example 5 — Influence Drift Stabilizes Move Selection

### Influence Drift (Lumen)
- left side → stable  
- right side → collapsing  
- drift vector → right → center  

### Harmonia Scoring
Moves that stabilize drift receive bonuses:

```
triadic_score += resonance_bonus
```

### Result
Stabilizing moves rise in ranking even if engine policy is low.

---

## Example 6 — Continuity Arc Reinforcement

### Continuity Arc
Left moyo boundary → continuity anchor  
Right weakness → continuity threat  

### Move Candidates
- **A:** invade moyo  
- **B:** reduce moyo  
- **C:** stabilize weak group  

### RTT Interpretation
- A → continuity collapse  
- B → structural alignment  
- C → continuity preservation  

### Final Decision
Move **C** selected due to continuity preservation.

---

## Example 7 — Teaching Mode Output

Teaching mode does not modify engine behavior.  
It overlays RTT signals:

```
Move A — Local (1/3)
  - Tactical fix
  - Paradox risk: high

Move B — Structural (2/3)
  - Influence shift
  - Continuity impact: positive

Move C — Continuity (3/3)
  - Long-arc moyo evolution
  - Collapse risk: medium
```

---

## Example 8 — Analysis Mode Output

Analysis mode evaluates human games:

```
Move 57 — Continuity collapse detected
  - moyo boundary broken
  - influence drift reversed
  - ancestry alignment lost

Move 103 — Continuity alignment
  - framework evolution preserved
  - long-arc identity reinforced
```

---

## Summary

These examples demonstrate how the Go bot logic layer:

- blends engine policy/value with RTT triadic scores  
- enforces continuity  
- prunes paradox and collapse‑risk moves  
- stabilizes long‑arc identity  
- produces resonance‑aligned strategy  
- integrates cleanly with MCTS  

RTT‑Go logic is where **engine strength meets triadic intelligence**.
