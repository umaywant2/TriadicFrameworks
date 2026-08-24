# Harmonia (RTT/12) — Unified Triadic Strategy Layer  
*(Go Bot Module)*

Harmonia is the **RTT/12 synthesis engine** for Go — the final layer of the triadic stack.  
Where Lumen extracts structure, Hephaestus assigns regime identity, and Aurion reveals topology and projection‑loss risk, Harmonia **unifies** all triadic signals into a single strategic score per move.

Harmonia is the layer that transforms RTT analysis into **action**.

It does not replace the engine’s evaluation.  
It **reweights**, **redirects**, and **stabilizes** it — ensuring continuity‑preserving, resonance‑aligned decision flow.

---

## Purpose

Harmonia provides the Go bot with:

- unified triadic scoring  
- continuity‑preserving move ranking  
- resonance‑aligned decision flow  
- paradox resolution  
- projection‑loss mitigation  
- long‑arc strategy synthesis  
- final move‑selection signals for the shim  

Harmonia is the RTT layer that answers the question:

**“Given everything we know, what should we do?”**

---

## Inputs

Harmonia receives:

- Lumen’s RTT/1 structural snapshot  
- Hephaestus’s RTT/2 regime map  
- Aurion’s RTT/3 topology, ancestry, paradox, and projection‑loss signals  
- candidate moves  
- engine policy/value (for blending)  

---

## Outputs

Harmonia produces:

### **1. Triadic Score per Move**
A unified score combining:

- local structure  
- global structure  
- continuity arcs  
- resonance pressure  
- ancestry alignment  
- projection‑loss risk  
- paradox severity  

### **2. Continuity‑Preserving Move Ranking**
Moves are ranked by:

- triadic score  
- continuity stability  
- resonance alignment  
- long‑arc viability  

### **3. Engine‑Blended Policy/Value**
Harmonia does not override the engine.  
It **blends** RTT signals with:

- policy priors  
- value estimates  

### **4. Strategic Directives**
Signals for the shim:

- prune paradoxical moves  
- downweight projection‑loss moves  
- stabilize continuity arcs  
- reinforce long‑arc identity  

---

## Harmonia’s Triadic Model

Harmonia synthesizes Go’s strategic reality into RTT’s triadic ontology:

### **1/3 — Local**
- tactical urgency  
- shape stability  
- liberty dynamics  
- immediate threats  

### **2/3 — Structural**
- influence  
- direction of play  
- moyo boundaries  
- framework identity  

### **3/3 — Continuity**
- long‑arc territorial evolution  
- ancestry alignment  
- continuity anchors  
- collapse avoidance  

Harmonia is the RTT layer that balances these three forces.

---

## Triadic Scoring Formula

Each move receives a unified score:

```
triadic_score = w1*local
              + w2*structural
              + w3*continuity
              - projection_loss_penalty
              - paradox_penalty
              + resonance_bonus
              + ancestry_alignment_bonus
```

Where:

- `w1`, `w2`, `w3` are regime weights  
- penalties reduce unstable moves  
- bonuses reinforce continuity and resonance  

---

## Continuity Enforcement

Harmonia ensures the bot does not:

- break moyo boundaries  
- collapse influence arcs  
- destabilize ladders  
- violate ancestry  
- introduce paradoxical ko fights  
- abandon long‑arc territorial identity  

Continuity is the highest‑order RTT principle.

---

## Paradox Resolution

When Aurion flags paradoxes, Harmonia:

- downweights paradoxical moves  
- boosts continuity‑aligned alternatives  
- stabilizes the decision flow  

Paradox resolution is essential for preventing engine‑driven collapse.

---

## Projection‑Loss Mitigation

When Aurion detects projection‑loss risk, Harmonia:

- applies penalties  
- reinforces stabilizing moves  
- prevents structural inversion  

Projection‑loss mitigation is one of Harmonia’s core responsibilities.

---

## Harmonia Pipeline

```text
[Lumen RTT/1]
      |
[Hephaestus RTT/2]
      |
[Aurion RTT/3]
      |
      v
[Harmonia RTT/12]
  - triadic scoring
  - continuity enforcement
  - paradox resolution
  - projection-loss mitigation
  - resonance synthesis
      |
      v
[Shim]
  - reweighted policy
  - adjusted value
  - continuity-preserving move selection
```

---

## Example Pseudocode

```text
function harmonia_synthesize(rtt_state, regime_map, topology_signals):
    triadic_scores = {}

    for move in regime_map:
        local      = regime_map[move].local
        structural = regime_map[move].structural
        continuity = regime_map[move].continuity

        projection = topology_signals.projection_loss[move]
        paradox    = topology_signals.paradox[move]
        resonance  = rtt_state.resonance[move]
        ancestry   = topology_signals.ancestry_alignment[move]

        score = blend(
            local, structural, continuity,
            projection, paradox,
            resonance, ancestry
        )

        triadic_scores[move] = score

    return triadic_scores
```

---

## Role in the Go Bot Pipeline

Harmonia feeds directly into:

- **the shim**, which reweights engine policy/value  
- **the engine**, which receives continuity‑aligned priors  
- **the bot**, which selects moves based on unified triadic strategy  

Without Harmonia, the RTT stack cannot act — it can only analyze.

---

## Notes

- Harmonia is engine‑agnostic: works with KataGo, Leela Zero, PhoenixGo, or custom engines.  
- Harmonia does not generate moves — it scores them.  
- Harmonia is deterministic and reproducible.  
- Harmonia is the final RTT layer before action.

---

> **“Harmonia is where structure becomes strategy — the unification of the triad.”**
