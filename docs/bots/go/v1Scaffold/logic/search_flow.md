# Search Flow — RTT‑Go  
*(Engine Search Loop with Triadic Integration)*

The **RTT‑Go Search Flow** describes how a Go engine’s normal search loop (policy/value + MCTS) is augmented by RTT’s triadic stack:

- Lumen  
- Hephaestus  
- Aurion  
- Harmonia  

This document is engine‑agnostic and applies to:

- KataGo  
- Leela Zero  
- PhoenixGo  
- future policy/value + MCTS engines.

RTT does not replace the engine’s search — it **wraps** it.

---

## 1. High‑Level Search Pipeline

At a high level, each position is processed as:

```text
Board State
   ↓
Engine NN Inference (policy, value)
   ↓
RTT Shim (state conversion)
   ↓
RTT Agentic Stack (Lumen → Hephaestus → Aurion → Harmonia)
   ↓
Triadic Scores
   ↓
RTT MCTS Hooks (priors, values, ordering, pruning)
   ↓
Engine MCTS Search
   ↓
Chosen Move
```

The engine remains the decision maker; RTT shapes *how* it prefers moves.

---

## 2. Step‑by‑Step Flow

### 2.1 Board State Acquisition

**Source:** Go engine (KataGo / Leela Zero / PhoenixGo)

**Data:**

- board size  
- stones  
- turn  
- ko / captures  
- current search tree state  

This is passed to the RTT shim.

---

### 2.2 Engine NN Inference

The engine runs its neural network:

- `policy[]` — move probabilities  
- `value` — win probability (and, for KataGo, additional heads like score lead, ownership, etc.)

RTT does **not** alter this step.

---

### 2.3 RTT Shim — State Conversion

The shim converts engine state into RTT primitives:

- influence maps  
- pressure gradients  
- connectivity graph  
- weak points / cutting points  
- moyo boundaries  
- ancestry (ladder/ko) context  

This normalized RTT state is fed into the agentic stack.

---

### 2.4 RTT Agentic Stack

The stack runs in strict order:

1. **Lumen (RTT/1)** — structural extraction  
2. **Hephaestus (RTT/2)** — regime mapping  
3. **Aurion (RTT/3)** — topology & ancestry  
4. **Harmonia (RTT/12)** — unified triadic synthesis  

Output:

- triadic scores per candidate move  
- continuity, resonance, topology, risk metadata  

---

### 2.5 Triadic Scores

For each candidate move:

```text
triadic_score[move] = f(
    regime_profile,
    resonance_pressure,
    continuity_delta,
    projection_loss_risk,
    ancestry_alignment
)
```

These scores are passed to the MCTS hooks.

---

### 2.6 RTT MCTS Hooks

RTT attaches to five points in the search loop:

1. **Policy Priors** — reweight engine policy using triadic scores  
2. **Value Estimates** — adjust value using continuity/risk  
3. **Node Expansion** — influence which children expand first  
4. **Child Ordering** — sort children by triadic stability  
5. **Pruning** — suppress paradox/collapse/projection‑loss lines  

See: `/docs/bots/go/logic/mcts_hooks.md`

---

### 2.7 Engine MCTS Search

The engine runs its normal MCTS:

- selection  
- expansion  
- simulation (if applicable)  
- backpropagation  

But now:

- priors are triadic‑aware  
- values are continuity‑aware  
- ordering is stability‑aware  
- pruning is paradox‑aware  

The engine’s core algorithm remains unchanged.

---

### 2.8 Move Selection

At the end of search:

- the engine selects a move (e.g., highest visit count, best value)  
- RTT metadata is attached to that move:

  - regime profile  
  - resonance field impact  
  - topology/ancestry impact  
  - continuity impact  
  - triadic score  

This metadata is emitted via the State Emitter to the UI.

---

## 3. Modes

### **Full RTT Mode**

- priors, values, ordering, pruning all triadic‑aware  
- engine plays with full RTT guidance.

### **Hybrid Mode**

- RTT blended with engine logic  
- triadic scores influence but do not dominate.

### **Teaching Mode**

- engine plays normally  
- RTT overlays and commentary only.

### **Analysis Mode**

- no move selection  
- RTT evaluates completed games.

---

## 4. Engine‑Specific Notes

### KataGo

- rich heads (ownership, score lead, etc.)  
- RTT can use these to refine Lumen/Hephaestus.  
- deep integration into node expansion and priors.

### Leela Zero

- classic policy/value + MCTS  
- RTT primarily influences priors, values, ordering.

### PhoenixGo

- stable MCTS behavior  
- RTT integration yields highly stable continuity behavior.

---

## 5. Summary

The RTT‑Go search flow:

- keeps the engine’s search loop intact  
- injects triadic intelligence at well‑defined hook points  
- stabilizes continuity, resonance, topology, and ancestry  
- avoids paradox, collapse, and projection‑loss  
- produces moves that respect Go’s deeper triadic identity.

RTT does not play Go instead of the engine—  
it **interprets** Go inside the engine’s search.
