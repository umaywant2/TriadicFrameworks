# RTT Leela Zero Shim  
*(for `/docs/bots/go/shim/leela_zero_shim.md`)*

The **RTT Leela Zero Shim** integrates RTT’s triadic evaluation pipeline with **Leela Zero’s** native policy/value inference and MCTS search.

Leela Zero’s architecture is simpler than KataGo’s — no ownership maps, no score‑lead head, no territory estimation — which makes RTT integration **clean, predictable, and stable**.

The shim does **not** replace Leela Zero’s logic.  
It **wraps** it, injecting RTT’s:

- structural identity  
- resonance pressure  
- continuity arcs  
- topology ancestry  
- paradox/collapse detection  
- unified triadic scoring  

into Leela Zero’s decision loop.

---

## 1. Purpose

The RTT Shim for Leela Zero:

- converts board + search state into RTT primitives  
- runs the RTT agentic stack  
  - **Lumen → Hephaestus → Aurion → Harmonia**  
- produces **triadic scores** for candidate moves  
- reweights Leela Zero’s:
  - policy priors  
  - value estimates  
  - MCTS node expansion priorities  
- enforces continuity‑preserving, resonance‑aligned decision flow  

This creates an engine that still “plays Go” in the Leela Zero sense — but with RTT’s deeper structural awareness.

---

## 2. Integration Points

Leela Zero’s architecture exposes three clean hook points:

---

### **Policy Post‑Processing**

Leela Zero produces:

- `policy[]` — move probabilities

RTT injects:

- triadic score blending  
- continuity weighting  
- resonance pressure adjustments  
- paradox/collapse suppression  

This produces **continuity‑aware priors**.

---

### **Value Post‑Processing**

Leela Zero’s value head predicts **win probability only**.

RTT adjusts this using:

- continuity arcs  
- projection‑loss risk  
- ancestry alignment  
- long‑arc drift  
- collapse signatures  

This produces **identity‑aware value estimates**.

---

### **MCTS Node Expansion**

RTT can:

- reorder child nodes  
- adjust exploration constants  
- prune paradoxical lines  
- stabilize long‑arc continuity  
- suppress collapse‑risk branches  
- promote continuity‑preserving sequences  

This produces **triadic‑stable search behavior**.

---

## 3. RTT Flow

```
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

## 4. RTT Primitive Extraction

### Lumen (RTT/1)
Extracts Go‑specific structural features:

- influence fields  
- pressure gradients  
- group connectivity  
- weak points / cutting points  
- shape identity  
- continuity anchors  

### Hephaestus (RTT/2)
Assigns regime profiles:

- **1/3 local** — liberties, cuts, shape  
- **2/3 structural** — influence, direction of play  
- **3/3 continuity** — long‑arc identity  

### Aurion (RTT/3)
Evaluates:

- ko topology  
- ladder ancestry  
- projection‑loss  
- continuity collapse  
- paradox precursors  

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

This score is blended with Leela Zero’s native policy/value:

```
final_policy = blend(policy, triadic_score)
final_value  = blend(value, continuity_score)
```

Blend modes:

- **strict triadic** — RTT dominates  
- **hybrid** — RTT + Leela Zero balanced  
- **teaching mode** — RTT annotations only  
- **analysis mode** — RTT overlays, no move selection  

---

## 6. Shim Responsibilities

### 1. **State Conversion**
Convert Leela Zero’s board + search state into RTT primitives.

### 2. **Agentic Execution**
Run the RTT stack:

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

## 7. Example Shim Pseudocode

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

## 8. Modes

### **RTT‑Go Bot**
Full triadic integration.

### **Teaching Mode**
Leela Zero plays normally; RTT provides overlays.

### **Analysis Mode**
RTT evaluates human games.

### **Hybrid Mode**
Leela Zero + RTT blended decision logic.

---

## 9. File Location

```
/docs/bots/go/shim/leela_zero_shim.md
```

---

## 10. Summary

The RTT Leela Zero Shim is a **triadic decision layer** that enhances Leela Zero with:

- structural identity  
- resonance pressure  
- continuity arcs  
- ancestry stability  
- paradox/collapse detection  
- unified triadic scoring  

Leela Zero still plays Go — RTT simply reveals the deeper structure already inside it.
