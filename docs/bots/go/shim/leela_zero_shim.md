# RTT Leela Zero Shim  
*(for `/docs/bots/go/leela_zero_shim.md`)*

This document describes how the RTT Shim integrates with **Leela Zero**, providing a triadic, regime‑aware decision layer on top of Leela Zero’s native policy/value inference and MCTS search.

The shim does **not** replace Leela Zero’s logic.  
It **wraps** it — injecting RTT structure, resonance, continuity, and projection‑loss awareness into the engine’s decision loop.

---

## Purpose

The RTT Shim for Leela Zero:

- converts board + search state into RTT primitives,
- runs the RTT agentic stack (Lumen → Hephaestus → Aurion → Harmonia),
- produces **triadic scores** for candidate moves,
- reweights Leela Zero’s:
  - policy priors,
  - value estimates,
  - MCTS node expansion priorities,
- enforces continuity‑preserving, resonance‑aligned decision flow.

This creates an engine that still “plays Go” in the Leela Zero sense — but with RTT’s deeper structural awareness.

---

## Integration Points

Leela Zero’s architecture is simpler than KataGo’s, which makes RTT integration clean and predictable.

### **Policy Post‑Processing**
Leela Zero produces:

- `policy[]` (move probabilities)

RTT injects:

- triadic score blending,
- continuity weighting,
- resonance pressure adjustments.

### **Value Post‑Processing**
Leela Zero’s value head predicts win probability only.  
RTT adjusts this using:

- continuity arcs,
- projection‑loss risk,
- ancestry alignment.

### **MCTS Node Expansion**
RTT can:

- reorder child nodes,
- adjust exploration constants,
- prune paradoxical lines,
- stabilize long‑arc continuity.

---

## RTT Flow

```text
[Leela Zero NN Inference]
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
[Leela Zero MCTS]
  - reweighted priors
  - adjusted values
  - continuity-preserving expansion
```

---

## RTT Primitive Extraction

### Lumen (RTT/1)
Extracts Go‑specific structural features:

- influence fields  
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

This score is blended with Leela Zero’s native policy/value:

```
final_policy = blend(policy, triadic_score)
final_value  = blend(value, continuity_score)
```

Blend functions are configurable per bot mode:

- **strict triadic** (RTT dominates)
- **hybrid** (RTT + Leela Zero balanced)
- **teaching mode** (RTT annotations only)
- **analysis mode** (RTT overlays, no move selection)

---

## Shim Responsibilities

### 1. **State Conversion**
Convert Leela Zero’s board + search state into RTT primitives.

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
function rtt_leela_zero_shim(position, policy, value):
    rtt_state = lumen_extract(position)
    regime    = hephaestus_map(rtt_state)
    topology  = aurion_analyze(rtt_state, regime)
    triadic   = harmonia_synthesize(rtt_state, regime, topology)

    adjusted_policy = blend_policy(policy, triadic)
    adjusted_value  = blend_value(value, triadic)

    return adjusted_policy, adjusted_value
```

---

## Modes

### **RTT‑Go Bot**
Full triadic integration.

### **Teaching Mode**
Leela Zero plays normally; RTT provides overlays.

### **Analysis Mode**
RTT evaluates human games.

### **Hybrid Mode**
Leela Zero + RTT blended decision logic.

---

## File Location

```
/docs/bots/go/leela_zero_shim.md
```

This file defines the shim logic and integration points for RTT‑enhanced Leela Zero.

---

> **“Go is resonance, continuity, and topology. RTT simply reveals the deeper structure already inside it.”**
