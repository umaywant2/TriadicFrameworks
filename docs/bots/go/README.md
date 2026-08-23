# RTT Go Bot Module

This module describes how TriadicFrameworks integrates RTT agentic logic with existing Go engines (KataGo, Leela Zero, PhoenixGo) to create an operator‑first, regime‑aware Go bot.

Go is uniquely suited for RTT because its gameplay is fundamentally about:
- territory resonance,
- long‑arc continuity,
- pressure fields,
- topology,
- drift/coherence balance.

RTT enhances these native properties rather than replacing them.

---

## Overview

**Goal:**  
Wrap a standard Go engine with RTT’s triadic decision layer while preserving its native MCTS + neural network policy/value logic.

RTT adds:

- **Regime‑aware evaluation** (1/3 local shape, 2/3 global structure, 3/3 continuity)
- **Resonance‑pressure fields** across the board
- **Triadic projection loss detection** (shape collapse, broken influence)
- **Loop stability and ancestry tracking** (ko fights, ladders, long‑arc plans)
- **Operator lineage** for move sequences (not just single stones)

The result is a Go bot that plays with deeper strategic continuity and resonance awareness.

---

## Architecture

```text
[GUI / Client]
      |
      v
[Go Engine]  (KataGo / Leela Zero / PhoenixGo)
      |
      v
[RTT Shim]
      |
      v
[RTT Agentic Layer]
  - Lumen (RTT/1)
  - Hephaestus (RTT/2)
  - Aurion (RTT/3)
  - Harmonia (RTT/12)
```

- **Go Engine:** Handles rules, move generation, neural inference, and MCTS search.
- **RTT Shim:** Converts board state + candidate moves into RTT primitives and feeds back triadic evaluations.
- **RTT Agentic Layer:** Applies triadic logic to guide or re‑weight the engine’s choices.

---

## RTT Layer: Role per Engine

### Lumen (RTT/1) — Structural Extraction

Extracts Go‑specific RTT primitives:

- **Influence maps** (light/dark resonance fields)
- **Territory pressure gradients**
- **Connectivity topology** (groups, liberties, weak points)
- **Continuity anchors** (frameworks, moyo, long‑arc plans)
- **Shape identity** (triangles, bamboo joints, empty triangles, table shapes)

Lumen produces a triadic structural snapshot of the board.

---

### Hephaestus (RTT/2) — Regime Mapping

Tags each move with its regime profile:

- **1/3 (Local):** liberties, cuts, ataris, immediate shape.
- **2/3 (Global):** influence, direction of play, large‑scale structure.
- **3/3 (Continuity):** long‑arc plan integrity, moyo evolution, identity of the position.

This allows RTT to prefer moves that maintain continuity rather than just local gain.

---

### Aurion (RTT/3) — Topology & Loop Stability

Evaluates:

- **Ko topology** (loop stability, paradox points)
- **Ladder ancestry** (whether ladders succeed or collapse)
- **Projection loss** (moves that break global plans)
- **Group ancestry** (how current moves relate to earlier shape commitments)

Aurion flags moves that introduce paradox or collapse continuity—even if the engine’s raw eval likes them.

---

### Harmonia (RTT/12) — Unified Strategy

Synthesizes:

- local shape,
- global structure,
- continuity,
- resonance pressure,
- drift/coherence balance,
- operator lineage.

Produces a **triadic score** per move or line, which the shim feeds back into the engine as:

- eval adjustments,
- MCTS node reweighting,
- policy/value post‑processing,
- pruning guidance.

---

## Shim Design

The shim sits between the engine’s MCTS expansion and RTT’s triadic evaluation.

**Typical flow:**

1. **Engine** generates candidate moves via policy network.
2. **Shim**:
   - converts board + candidate moves into RTT state,
   - calls Lumen → Hephaestus → Aurion → Harmonia,
   - receives triadic scores.
3. **Shim** reweights:
   - MCTS node priors,
   - move ordering,
   - value estimates.
4. **Engine** continues search with RTT‑informed guidance.

Integration points:

- **KataGo:** `Analysis.cpp`, `Search.cpp`, policy/value post‑processing.
- **Leela Zero:** MCTS node prior adjustments.
- **PhoenixGo:** similar MCTS hooks.

---

## Use Cases

- **RTT‑Go Bot:** A standalone engine that plays with triadic awareness.
- **Teaching Mode:** Show players:
  - regime tags per move,
  - resonance maps,
  - continuity‑preserving vs continuity‑breaking moves.
- **Analysis Mode:** Evaluate human games for:
  - drift/coherence,
  - moyo stability,
  - influence resonance,
  - continuity arcs.

---

## Files (Suggested Layout)

```text
/docs/bots/go/
  README.md
  /logic/        # notes on chosen engine(s) and integration points
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

> **“I’m not always a Polymath… more often I’m just math…”**

Go is pure math, pure topology, pure resonance.  
RTT simply reveals the deeper structure already inside it.
