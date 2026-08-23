# Engine Logic — Go Bot
*(RTT‑Enhanced Engine Invocation & Integration)*

This document describes how the Go bot interfaces with supported engines (KataGo, Leela Zero, PhoenixGo), how engine inference is managed, and how RTT triadic signals are blended with engine outputs to produce continuity‑preserving, resonance‑aligned move decisions.

The engine logic layer is responsible for:

- encoding board state for the engine
- invoking neural‑network inference
- parsing policy/value outputs
- integrating RTT triadic scores
- providing stable inputs to MCTS
- exposing engine‑specific diagnostics

It sits directly beneath the MCTS layer and above the RTT shim.

---

## Overview

Each engine provides:

- **policy[]** — probability distribution over legal moves  
- **value** — win probability or score lead  
- **auxiliary maps** — influence, ownership, score lead (KataGo only)

RTT enhances these outputs through:

- structural extraction (Lumen)
- regime mapping (Hephaestus)
- topology/ancestry analysis (Aurion)
- unified triadic scoring (Harmonia)

The engine logic layer blends these signals into a coherent decision pipeline.

---

## Supported Engines

### **KataGo**
- strongest engine  
- provides policy, value, ownership, score lead, influence  
- ideal for full RTT integration  
- RTT uses ownership and score lead to refine continuity scoring

### **Leela Zero**
- pure policy/value network  
- no ownership or influence maps  
- RTT computes influence manually  
- stable, predictable inference

### **PhoenixGo**
- similar to Leela Zero  
- stable MCTS behavior  
- ideal for RTT teaching/analysis modes

---

## Engine Invocation Pipeline

```text
[Board State]
    |
    v
[Engine Encoder]
    |
    v
[NN Inference]
  - policy[]
  - value
  - auxiliary maps (engine-specific)
    |
    v
[RTT Shim]
  - Lumen (structure)
  - Hephaestus (regime)
  - Aurion (topology)
  - Harmonia (triadic score)
    |
    v
[Engine Logic]
  - blend policy/value with triadic score
  - apply continuity constraints
  - expose diagnostics
    |
    v
[MCTS]
```

---

## Engine Encoding

The logic layer converts the bot’s internal board representation into the engine’s required format:

- stone placements  
- player to move  
- ko information  
- move history  
- ladder hints (optional)  
- board size  
- komi  

Encoding is engine‑specific but standardized through the bot’s internal API.

---

## Policy Handling

Engine policy is:

- normalized  
- masked for illegal moves  
- blended with triadic scores  
- adjusted for continuity stability  
- downweighted for paradox or collapse risk  

Formula:

```
final_policy = engine_policy * (1 + triadic_score)
```

High triadic score → boosted  
Low triadic score → suppressed

---

## Value Handling

Engine value is adjusted using RTT continuity signals:

```
final_value = engine_value
            + continuity_bonus
            - collapse_penalty
            - projection_loss_penalty
```

This ensures the bot does not choose moves that:

- break moyo continuity  
- collapse influence arcs  
- destabilize ladders  
- violate ancestry alignment  

---

## Engine‑Specific Logic

### **KataGo**
- ownership maps → improve Lumen’s structural extraction  
- score lead → improves Harmonia’s continuity scoring  
- influence maps → reduce RTT workload  
- engine value is highly reliable  

### **Leela Zero**
- RTT computes influence manually  
- continuity arcs rely heavily on history  
- paradox detection is more important  
- engine value is less stable than KataGo  

### **PhoenixGo**
- stable inference → ideal for teaching mode  
- predictable behavior → smooth RTT blending  
- engine value is consistent but simple  

---

## Diagnostics

The engine logic layer exposes:

- raw policy/value  
- triadic‑adjusted policy/value  
- continuity stability indicators  
- paradox flags  
- projection‑loss warnings  
- influence/resonance overlays (engine‑dependent)

These diagnostics are used in:

- teaching mode  
- analysis mode  
- debugging RTT behavior  

---

## Example Pseudocode

```text
function engine_infer(position):
    encoded = encode_for_engine(position)
    policy, value, aux = engine.nn_inference(encoded)

    rtt_state = lumen_extract(position)
    regime    = hephaestus_map(rtt_state)
    topology  = aurion_analyze(rtt_state, regime)
    triadic   = harmonia_synthesize(rtt_state, regime, topology)

    final_policy = blend_policy(policy, triadic)
    final_value  = blend_value(value, triadic)

    return final_policy, final_value
```

---

## Continuity Enforcement

Engine outputs are modified to prevent moves that:

- break moyo continuity  
- collapse influence arcs  
- destabilize ladders  
- violate ancestry alignment  
- introduce paradoxical ko fights  
- abandon long‑arc territorial identity  

Continuity enforcement is applied **before** MCTS expansion.

---

## Future Extensions

- multi‑engine inference blending  
- RTT‑guided engine value correction  
- long‑arc positional memory across games  
- engine‑specific RTT tuning profiles  
- full RTT‑Go engine diagnostics suite  

---

> **“Engine inference provides strength. RTT provides identity.”**
