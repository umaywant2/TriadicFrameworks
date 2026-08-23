# PhoenixGo RTT Shim  
*(Go Bot Module)*

This document describes how the RTT Shim integrates with **PhoenixGo**, providing a triadic, continuity‑preserving decision layer on top of PhoenixGo’s neural‑network policy/value inference and stable MCTS search.

PhoenixGo is structurally similar to Leela Zero but with more predictable MCTS behavior, making it an excellent engine for RTT teaching, analysis, and hybrid triadic integration.

The RTT shim does **not** replace PhoenixGo’s logic.  
It **wraps** it — injecting RTT structure, resonance, continuity, and projection‑loss awareness into the engine’s decision loop.

---

## Purpose

The RTT Shim for PhoenixGo:

- converts board + search state into RTT primitives  
- runs the RTT agentic stack (Lumen → Hephaestus → Aurion → Harmonia)  
- produces **triadic scores** for candidate moves  
- reweights PhoenixGo’s:
  - policy priors  
  - value estimates  
  - MCTS node expansion priorities  
- enforces continuity‑preserving, resonance‑aligned decision flow  

PhoenixGo remains PhoenixGo — RTT simply reveals and stabilizes the deeper structure already inside the game.

---

## Integration Points

PhoenixGo provides clean hooks for RTT integration:

### **Policy/Value Post‑Processing**
PhoenixGo outputs:

- `policy[]` (move probabilities)  
- `value` (win probability)  

RTT injects:

- triadic score blending  
- continuity weighting  
- resonance pressure adjustments  

### **MCTS Node Expansion**
PhoenixGo’s stable MCTS allows RTT to:

- reorder child nodes  
- adjust exploration constants  
- prune paradoxical lines  
- stabilize long‑arc continuity  

### **Search Loop**
RTT observes:

- influence evolution  
- group connectivity  
- moyo boundaries  
- ladder/ko ancestry  
- continuity arcs  

These feed into Aurion and Harmonia.

---

## RTT Flow

```text
[PhoenixGo NN Inference]
      |
      v
[RTT Shim]
  - Lumen (RTT/1)
  - Hephaestus (RTT/2)
  - Aurion (RTT/3)
  - Harmonia (RTT/12)
      |
      v
[Triadic Scores]
      |
      v
[PhoenixGo MCTS]
  - reweighted priors
  - adjusted values
  - continuity-preserving expansion
```

---

## RTT Primitive Extraction (Lumen)

Lumen extracts:

- influence fields  
- pressure gradients  
- group connectivity  
- shape signatures  
- continuity anchors  
- drift vectors  
- resonance maps  

PhoenixGo does not provide ownership maps, so RTT computes influence internally.

---

## Regime Mapping (Hephaestus)

Hephaestus assigns regime identity:

- **1/3 local:** cuts, ataris, shape fixes  
- **2/3 structural:** influence shifts, direction of play  
- **3/3 continuity:** moyo evolution, long‑arc identity  

Each move receives a regime profile vector.

---

## Topology & Projection‑Loss (Aurion)

Aurion evaluates:

- ladder ancestry  
- ko topology  
- continuity collapse  
- projection‑loss risk  
- paradox detection  
- risk‑arc mapping  

PhoenixGo’s stable MCTS makes Aurion’s topology signals highly reliable.

---

## Triadic Synthesis (Harmonia)

Harmonia produces unified triadic scores:

```
triadic_score = f(
    local,
    structural,
    continuity,
    resonance,
    ancestry_alignment,
    projection_loss_penalty,
    paradox_penalty
)
```

These scores blend with PhoenixGo’s policy/value:

```
final_policy = blend(policy, triadic_score)
final_value  = blend(value, continuity_score)
```

---

## Shim Responsibilities

### **1. State Conversion**
Convert PhoenixGo’s board + search state into RTT primitives.

### **2. Agentic Execution**
Run the RTT stack:

1. Lumen  
2. Hephaestus  
3. Aurion  
4. Harmonia  

### **3. Score Injection**
Feed triadic scores into:

- policy priors  
- value estimates  
- MCTS node ordering  

### **4. Continuity Enforcement**
Flag or prune moves that:

- break moyo continuity  
- collapse influence arcs  
- violate ladder ancestry  
- introduce paradoxical ko loops  

### **5. Diagnostics (optional)**
Expose RTT overlays:

- regime tags  
- resonance maps  
- continuity arcs  
- drift/coherence profiles  

---

## Example Shim Pseudocode

```text
function rtt_phoenixgo_shim(position, policy, value):
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
PhoenixGo plays normally; RTT provides overlays.

### **Analysis Mode**
RTT evaluates human games.

### **Hybrid Mode**
PhoenixGo + RTT blended decision logic.

---

## File Location

```
/docs/bots/go/phoenixgo_shim.md
```

This file defines the shim logic and integration points for RTT‑enhanced PhoenixGo.

---

> **“PhoenixGo is stable. RTT makes it strategic.”**
