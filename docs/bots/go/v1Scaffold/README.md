# RTT‑Go Bot Module  
*(TriadicFrameworks — Operator‑First, Regime‑Aware Go Engine)*

The **RTT‑Go Bot Module** integrates Resonance‑Time Theory (RTT) with existing Go engines (KataGo, Leela Zero, PhoenixGo) to create an operator‑first, regime‑aware Go bot.

Go is uniquely suited for RTT because its gameplay is fundamentally about:

- territory resonance  
- long‑arc continuity  
- pressure fields  
- topology  
- drift/coherence balance  

RTT does not replace these properties — it **reveals** them.

---

# 1. Overview

**Goal:** Wrap a standard Go engine with RTT’s triadic decision layer while preserving its native MCTS + neural network policy/value logic.

RTT adds:

- regime‑aware evaluation (1/3 local, 2/3 structural, 3/3 continuity)  
- resonance‑pressure fields across the board  
- triadic projection‑loss detection (shape collapse, broken influence)  
- loop stability + ancestry tracking (ko fights, ladders, long‑arc plans)  
- operator lineage for move sequences  

The result is a Go bot that plays with **deep strategic continuity and resonance awareness**.

---

# 2. Architecture

```
[GUI / Client]
      ↓
[Go Engine] (KataGo / Leela Zero / PhoenixGo)
      ↓
[RTT Shim]
      ↓
[RTT Agentic Layer]
      ↓
[RTT Engine]
      ↓
[State Emitter]
      ↓
[RTT‑Go UI]
```

### Go Engine  
Handles rules, move generation, neural inference, and MCTS search.

### RTT Shim  
Converts board state + candidate moves into RTT primitives and feeds back triadic evaluations.

### RTT Agentic Layer  
Applies triadic logic to guide or re‑weight the engine’s choices.

### RTT Engine  
Computes the full triadic identity of the position.

### RTT‑Go UI  
Renders triadic overlays, HUD, timeline, diagnostics.

---

# 3. RTT Agentic Layer  
*(Lumen → Hephaestus → Aurion → Harmonia)*

The agentic layer applies RTT’s four operator families to Go.

---

## Lumen (RTT/1) — Structural Extraction  
Extracts Go‑specific RTT primitives:

- influence maps (light/dark resonance fields)  
- territory pressure gradients  
- connectivity topology (groups, liberties, weak points)  
- continuity anchors (moyo, frameworks, long‑arc plans)  
- shape identity (triangles, bamboo joints, empty triangles, table shapes)

Lumen produces a **triadic structural snapshot** of the board.

---

## Hephaestus (RTT/2) — Regime Mapping  
Tags each move with its regime profile:

- **1/3 Local:** liberties, cuts, ataris, immediate shape  
- **2/3 Structural:** influence, direction of play, large‑scale structure  
- **3/3 Continuity:** long‑arc plan integrity, moyo evolution, identity of the position  

This allows RTT to prefer moves that maintain continuity rather than just local gain.

---

## Aurion (RTT/3) — Topology & Loop Stability  
Evaluates:

- ko topology (loop stability, paradox points)  
- ladder ancestry (success vs collapse)  
- projection‑loss (moves that break global plans)  
- group ancestry (how current moves relate to earlier commitments)

Aurion flags moves that introduce paradox or collapse continuity — even if the engine’s raw eval likes them.

---

## Harmonia (RTT/12) — Unified Strategy  
Synthesizes:

- local shape  
- global structure  
- continuity  
- resonance pressure  
- drift/coherence balance  
- operator lineage  

Produces a **triadic score** per move or line, which the shim feeds back into the engine as:

- eval adjustments  
- MCTS node reweighting  
- policy/value post‑processing  
- pruning guidance  

---

# 4. Shim Design  
*(Engine‑agnostic integration layer)*

The shim sits between the engine’s MCTS expansion and RTT’s triadic evaluation.

### Typical Flow

1. Engine generates candidate moves via policy network.  
2. Shim converts board + candidate moves into RTT state.  
3. Shim calls:  
   **Lumen → Hephaestus → Aurion → Harmonia**  
4. Shim receives triadic scores.  
5. Shim reweights:  
   - MCTS node priors  
   - move ordering  
   - value estimates  
6. Engine continues search with RTT‑informed guidance.

### Integration Points

- **KataGo:** `Analysis.cpp`, `Search.cpp`, policy/value post‑processing  
- **Leela Zero:** MCTS node prior adjustments  
- **PhoenixGo:** similar MCTS hooks  

---

# 5. Use Cases

### **RTT‑Go Bot**  
A standalone engine that plays with triadic awareness.

### **Teaching Mode**  
Shows players:

- regime tags per move  
- resonance maps  
- continuity‑preserving vs continuity‑breaking moves  

### **Analysis Mode**  
Evaluates human games for:

- drift/coherence  
- moyo stability  
- influence resonance  
- continuity arcs  

---

# 6. Files (Suggested Layout)

```
/docs/bots/go/
    README.md
    /engine/
        architecture.md
        regime.md
        resonance.md
        topology.md
        continuity.md
        risk.md
        scoring.md
        state_emitter.md

    /logic/
        # notes on chosen engine(s) and integration points

    /rtt/
        lumen.md
        hephaestus.md
        aurion.md
        harmonia.md

    /shim/
        katago_shim.md
        leela_zero_shim.md

    /examples/
        rtt_go_examples.md

    /analysis/
        regime_maps.md
        resonance_fields.md
```

---

# 7. Summary

RTT‑Go is a **triadic Go engine** that enhances standard engines with:

- regime awareness  
- resonance pressure  
- topology stability  
- continuity arcs  
- paradox/collapse detection  
- unified triadic scoring  

Go is pure math, pure topology, pure resonance.  
RTT simply reveals the deeper structure already inside it.
