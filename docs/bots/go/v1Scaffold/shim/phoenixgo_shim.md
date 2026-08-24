# PhoenixGo RTT Shim  
*(RTT Integration Layer for PhoenixGo)*

The **RTT PhoenixGo Shim** integrates RTT’s triadic evaluation pipeline with **PhoenixGo’s** neural‑network policy/value inference and its notably stable MCTS search.

PhoenixGo is structurally similar to Leela Zero but with **more predictable MCTS behavior**, making it ideal for:

- RTT teaching mode  
- RTT analysis mode  
- hybrid triadic integration  
- continuity‑preserving play  

The shim does **not** replace PhoenixGo’s logic.  
It **wraps** it — injecting RTT structure, resonance, continuity, topology ancestry, and projection‑loss awareness into PhoenixGo’s decision loop.

---

## 1. Purpose

The RTT Shim for PhoenixGo:

- converts board + search state into RTT primitives  
- runs the RTT agentic stack  
  - **Lumen → Hephaestus → Aurion → Harmonia**  
- produces **triadic scores** for candidate moves  
- reweights PhoenixGo’s:
  - policy priors  
  - value estimates  
  - MCTS node expansion priorities  
- enforces continuity‑preserving, resonance‑aligned decision flow  

PhoenixGo remains PhoenixGo — RTT simply reveals and stabilizes the deeper structure already inside the game.

---

## 2. Integration Points

PhoenixGo exposes clean, predictable hook points for RTT integration:

---

### **Policy/Value Post‑Processing**

PhoenixGo outputs:

- `policy[]` — move probabilities  
- `value` — win probability  

RTT injects:

- triadic score blending  
- continuity weighting  
- resonance pressure adjustments  
- paradox/collapse suppression  

This produces **continuity‑aware priors** and **identity‑aware value estimates**.

---

### **MCTS Node Expansion**

PhoenixGo’s stable MCTS allows RTT to:

- reorder child nodes  
- adjust exploration constants  
- prune paradoxical lines  
- stabilize long‑arc continuity  
- suppress collapse‑risk branches  
- promote continuity‑preserving sequences  

This produces **triadic‑stable search behavior**.

---

### **Search Loop**

RTT observes:

- influence evolution  
- pressure gradients  
- ko threats  
- ladder ancestry  
- continuity arcs  
- drift/coherence balance  

These feed into Aurion + Harmonia.

---

## 3. RTT Flow

```
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

## 4. RTT Primitive Extraction

### Lumen (RTT/1)
Extracts:

- influence fields  
- pressure gradients  
- group connectivity  
- shape identity  
- continuity anchors  

PhoenixGo does not provide ownership maps, so RTT computes influence internally.

---

### Hephaestus (RTT/2)
Assigns regime profiles:

- **1/3 local** — liberties, cuts, shape  
- **2/3 structural** — influence, direction of play  
- **3/3 continuity** — long‑arc identity  

---

### Aurion (RTT/3)
Evaluates:

- ladder ancestry  
- ko topology  
- projection‑loss  
- continuity collapse  
- paradox precursors  

PhoenixGo’s stable MCTS makes Aurion’s topology signals highly reliable.

---

### Harmonia (RTT/12)
Synthesizes:

- local shape  
- global structure  
- continuity arcs  
- resonance pressure  
- drift/coherence  
- operator lineage  

Produces **triadic scores** per move.

---

## 5. Triadic Scoring Model

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

Blending with PhoenixGo’s native outputs:

```
final_policy = blend(policy, triadic_score)
final_value  = blend(value, continuity_score)
```

Blend modes:

- **strict triadic** — RTT dominates  
- **hybrid** — RTT + PhoenixGo balanced  
- **teaching mode** — RTT annotations only  
- **analysis mode** — RTT overlays, no move selection  

---

## 6. Shim Responsibilities

### 1. **State Conversion**
Convert PhoenixGo’s board + search state into RTT primitives.

### 2. **Agentic Execution**
Run the RTT stack:

1. Lumen  
2. Hephaestus  
3. Aurion  
4. Harmonia  

### 3. **Score Injection**
Feed triadic scores into:

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

## 7. Example Shim Pseudocode

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

## 8. Modes

### **RTT‑Go Bot**
Full triadic integration.

### **Teaching Mode**
PhoenixGo plays normally; RTT provides overlays.

### **Analysis Mode**
RTT evaluates human games.

### **Hybrid Mode**
PhoenixGo + RTT blended decision logic.

---

## 9. File Location

```
/docs/bots/go/shim/phoenixgo_shim.md
```

---

## 10. Summary

The RTT PhoenixGo Shim is a **triadic decision layer** that enhances PhoenixGo with:

- structural identity  
- resonance pressure  
- continuity arcs  
- ancestry stability  
- paradox/collapse detection  
- unified triadic scoring  

PhoenixGo still plays Go — RTT simply reveals the deeper structure already inside it.
