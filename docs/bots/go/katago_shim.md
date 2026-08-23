# KataGo RTT Shim

This document describes how the RTT Shim integrates with **KataGo**, providing a triadic, regime‑aware decision layer on top of KataGo’s native neural‑network policy/value inference and MCTS search.

The shim does **not** replace KataGo’s logic.  
It **wraps** it — injecting RTT structure, resonance, continuity, and projection‑loss awareness into the engine’s decision loop.

---

## Purpose

The RTT Shim for KataGo:

- converts KataGo board + search state into RTT primitives,
- runs the RTT agentic stack (Lumen → Hephaestus → Aurion → Harmonia),
- produces **triadic scores** for candidate moves,
- reweights KataGo’s:
  - policy priors,
  - value estimates,
  - MCTS node expansion priorities,
- enforces continuity‑preserving, resonance‑aligned decision flow.

This creates an engine that still “plays Go” in the KataGo sense — but with RTT’s deeper structural awareness.

---

## Integration Points

KataGo provides several hooks ideal for RTT integration:

### **Policy/Value Post‑Processing**
After KataGo’s neural net produces:

- `policy[]` (move probabilities)
- `value` (winrate / score lead)

The RTT shim intercepts these outputs and applies:

- triadic score blending,
- continuity weighting,
- resonance pressure adjustments.

### **MCTS Node Expansion**
During tree search, RTT can:

- reorder child nodes,
- adjust exploration constants,
- prune paradoxical lines,
- stabilize long‑arc continuity.

### **Search Loop**
RTT can observe:

- ko threats,
- ladder ancestry,
- influence evolution,
- territory continuity arcs.

These feed into Aurion and Harmonia’s triadic synthesis.

---

## RTT Flow

```text
[KataGo NN Inference]
      |
      v
[RTT Shim]
  - extract RTT primitives
  - run Lumen (RTT/1)
  - run Hephaestus (RTT/2)
  - run Aurion (RTT/3)
  - run Harmonia (RTT/12)
      |
      v
[Triadic Scores]
      |
      v
[KataGo MCTS]
  - reweighted priors
  - adjusted values
  - continuity-preserving expansion
```

---

## RTT Primitive Extraction

### Lumen (RTT/1)
Extracts Go‑specific structural features:

- influence maps  
- territory pressure gradients  
- group connectivity  
- weak points / cutting points  
- shape identity (bamboo, table, empty triangle)  
- continuity anchors (moyo, frameworks, direction of play)

### Hephaestus (RTT/2)
Assigns regime profiles:

- **1/3 local:** liberties, cuts, ataris  
- **2/3 structural:** influence, direction, large‑scale shape  
- **3/3 continuity:** long‑arc plan integrity, moyo evolution  

### Aurion (RTT/3)
Evaluates:

- ko topology  
- ladder ancestry  
- projection loss  
- continuity collapse  
- paradoxical sequences  

### Harmonia (RTT/12)
Synthesizes:

- local shape  
- global structure  
- continuity arcs  
- resonance pressure  
- drift/coherence balance  
- operator lineage  

Produces **triadic scores** per move.

---

## Triadic Scoring Model

Each candidate move receives:

```
triadic_score = f(
    regime_profile,
    resonance_pressure,
    continuity_delta,
    projection_loss_risk,
    ancestry_alignment
)
```

This score is blended with KataGo’s native policy/value:

```
final_policy = blend(policy, triadic_score)
final_value  = blend(value, continuity_score)
```

Blend functions are configurable per bot mode:

- **strict triadic** (RTT dominates)
- **hybrid** (RTT + KataGo balanced)
- **teaching mode** (RTT annotations only)
- **analysis mode** (RTT overlays, no move selection)

---

## Shim Responsibilities

### 1. **State Conversion**
Convert KataGo’s board + search state into RTT primitives.

### 2. **Agentic Execution**
Run the RTT stack in order:

1. Lumen  
2. Hephaestus  
3. Aurion  
4. Harmonia  

### 3. **Score Injection**
Feed triadic scores back into:

- policy priors  
- value estimates  
- MCTS node ordering  

### 4. **Continuity Enforcement**
Flag or prune moves that:

- break moyo continuity  
- collapse influence arcs  
- violate ladder ancestry  
- introduce paradoxical ko loops  

### 5. **Diagnostics (optional)**
Expose RTT overlays:

- regime tags  
- resonance maps  
- continuity arcs  
- drift/coherence profiles  

---

## Example Shim Pseudocode

```text
function rtt_katago_shim(position, katago_policy, katago_value):
    rtt_state = lumen_extract(position)
    regime    = hephaestus_map(rtt_state)
    topology  = aurion_analyze(rtt_state, regime)
    triadic   = harmonia_synthesize(rtt_state, regime, topology)

    adjusted_policy = blend_policy(katago_policy, triadic)
    adjusted_value  = blend_value(katago_value, triadic)

    return adjusted_policy, adjusted_value
```

---

## Modes

### **RTT‑Go Bot**
Full triadic integration.

### **Teaching Mode**
KataGo plays normally; RTT provides overlays.

### **Analysis Mode**
RTT evaluates human games.

### **Hybrid Mode**
KataGo + RTT blended decision logic.

---

## File Location

```
/docs/bots/go/katago_shim.md
```

This file defines the shim logic and integration points for RTT‑enhanced KataGo.

---

## Notes

- The shim is engine‑agnostic; it can be adapted to Leela Zero or PhoenixGo.
- RTT does not modify KataGo’s rules or NN architecture.
- All triadic logic is external and modular.

---

> **“Go is topology, resonance, continuity. RTT simply reveals the deeper structure already inside it.”**
