# RTT‑Go Logic Layer  
*(Engine Integration Notes & MCTS Hooking Model)*

The **Logic Layer** describes how RTT integrates with external Go engines.  
It does not compute triadic primitives — it defines the *mechanics* of integration:

- where RTT attaches  
- how RTT reweights engine decisions  
- how the shim communicates with MCTS  
- how triadic scores influence search  

This layer is engine‑agnostic.

---

## 1. Purpose

The logic layer provides:

- integration points for KataGo, Leela Zero, PhoenixGo  
- MCTS hook definitions  
- policy/value post‑processing rules  
- triadic score blending rules  
- engine‑agnostic shim contract  

It is the **bridge** between the Go engine and the RTT engine.

---

## 2. Integration Model

```
[Go Engine]
   ↓ (board state)
[RTT Shim]
   ↓ (triadic primitives)
[RTT Engine]
   ↓ (triadic scores)
[RTT Shim]
   ↓ (reweighted priors/values)
[Go Engine]
```

The engine remains in control of move generation.  
RTT influences *how strongly* the engine prefers each move.

---

## 3. MCTS Integration Points

### **1. Policy Priors**
RTT reweights the engine’s policy distribution:

```
final_policy = blend(engine_policy, triadic_score)
```

### **2. Value Estimates**
RTT adjusts value estimates based on continuity, resonance, and risk:

```
final_value = blend(engine_value, continuity_score)
```

### **3. Node Expansion**
RTT influences:

- node ordering  
- pruning  
- exploration constants  
- continuity‑preserving expansion  

### **4. Search Loop**
RTT observes:

- ko threats  
- ladder ancestry  
- influence evolution  
- continuity arcs  

These feed into Aurion + Harmonia.

---

## 4. Engine‑Specific Notes

### **KataGo**
Hooks:  
- `Analysis.cpp`  
- `Search.cpp`  
- policy/value post‑processing  
- MCTS node expansion  

### **Leela Zero**
Hooks:  
- MCTS prior reweighting  
- node ordering  
- playout pruning  

### **PhoenixGo**
Hooks:  
- policy/value blending  
- search loop adjustments  

---

## 5. Shim Contract

The shim must provide:

```
normalize(board_state)
extract_rtt_primitives()
run_rtt_pipeline()
blend_policy()
blend_value()
return_adjusted_scores()
```

The shim is the **only** module that touches the engine directly.

---

## 6. Summary

The logic layer defines:

- how RTT attaches to engines  
- how triadic scores influence search  
- how the shim communicates with MCTS  
- how policy/value blending works  

It is the **integration backbone** of RTT‑Go.

---

# ✅ 2. `/docs/bots/go/rtt/` — Operator‑Family Documentation  
Below is a complete index + four operator‑family documents.

---

## `/docs/bots/go/rtt/README.md`

# RTT Operator Families  
*(Lumen → Hephaestus → Aurion → Harmonia)*

RTT‑Go uses four operator families to evaluate Go positions:

- **Lumen** — structural extraction  
- **Hephaestus** — regime mapping  
- **Aurion** — topology & ancestry  
- **Harmonia** — unified triadic synthesis  

These operators form the **agentic layer** of RTT‑Go.

---

## `/docs/bots/go/rtt/lumen.md`

# Lumen — RTT/1  
*(Structural Extraction Layer)*

Lumen extracts Go‑specific RTT primitives:

- influence maps  
- territory pressure gradients  
- connectivity topology  
- continuity anchors  
- shape identity  

Lumen produces the **structural snapshot** of the board.

---

## `/docs/bots/go/rtt/hephaestus.md`

# Hephaestus — RTT/2  
*(Regime Mapping Layer)*

Hephaestus assigns regime profiles:

- **1/3 Local** — liberties, cuts, shape  
- **2/3 Structural** — influence, direction of play  
- **3/3 Continuity** — long‑arc identity  

Hephaestus produces the **regime distribution**.

---

## `/docs/bots/go/rtt/aurion.md`

# Aurion — RTT/3  
*(Topology & Loop Stability Layer)*

Aurion evaluates:

- ko topology  
- ladder ancestry  
- projection‑loss  
- continuity collapse  
- paradox precursors  

Aurion produces the **structural‑temporal stability** of the position.

---

## `/docs/bots/go/rtt/harmonia.md`

# Harmonia — RTT/12  
*(Unified Triadic Synthesis Layer)*

Harmonia synthesizes:

- local shape  
- global structure  
- continuity arcs  
- resonance pressure  
- drift/coherence  
- operator lineage  

Harmonia produces the **triadic score**.

---

# ✅ 3. `/docs/bots/go/shim/katago_shim.md` — Shim Implementation  
Your existing shim file is already complete and canon‑aligned.  
However, now that you’ve moved it into `/shim/`, here is the **updated version** with correct path references and a few refinements.

---

## `/docs/bots/go/shim/katago_shim.md`

# KataGo RTT Shim  
*(RTT Integration Layer for KataGo)*

The KataGo RTT Shim wraps KataGo’s native policy/value inference and MCTS search with RTT’s triadic evaluation pipeline.

The shim does **not** replace KataGo’s logic — it **wraps** it.

---

## 1. Purpose

The shim:

- converts KataGo board state → RTT primitives  
- runs Lumen → Hephaestus → Aurion → Harmonia  
- produces triadic scores  
- reweights KataGo’s policy/value  
- adjusts MCTS node expansion  
- enforces continuity‑preserving decision flow  

---

## 2. Integration Points

### **Policy/Value Post‑Processing**
RTT intercepts:

- `policy[]`  
- `value`  

and applies triadic blending.

### **MCTS Node Expansion**
RTT adjusts:

- node ordering  
- exploration constants  
- pruning  
- continuity enforcement  

### **Search Loop**
RTT observes:

- ko threats  
- ladder ancestry  
- influence evolution  
- continuity arcs  

---

## 3. RTT Flow

```
[KataGo NN Inference]
      ↓
[RTT Shim]
      ↓
[Lumen → Hephaestus → Aurion → Harmonia]
      ↓
[Triadic Scores]
      ↓
[KataGo MCTS]
```

---

## 4. Shim Responsibilities

- state conversion  
- agentic execution  
- score injection  
- continuity enforcement  
- diagnostics (optional)  

---

## 5. Example Shim Pseudocode

```
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

## 6. File Location

```
/docs/bots/go/shim/katago_shim.md
```
