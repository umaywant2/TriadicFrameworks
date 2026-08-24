# RTT Chess Bot Module

This module describes how TriadicFrameworks integrates RTT agentic logic with existing chess engines (e.g., Stockfish, Leela Chess Zero, Fairy‑Stockfish) to create an operator‑first, regime‑aware chess bot.

---

## Overview

**Goal:**  
Wrap a standard chess engine with RTT’s triadic decision layer, without replacing its native move generation or search.

RTT adds:

- **Regime‑aware evaluation** (1/3 material, 2/3 structure, 3/3 continuity)
- **Resonance‑pressure fields** over the position
- **Triadic projection loss detection** (where plans leak coherence)
- **Loop stability and ancestry tracking** for long‑arc strategy
- **Operator lineage** for move sequences (not just single moves)

The result is a chess bot that still “plays chess” in the usual sense—but its decisions are informed by RTT’s deeper structure.

---

## Architecture

```text
[GUI / Client]
      |
      v
[Chess Engine]  (Stockfish / Leela / etc.)
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

- **Chess Engine:** Handles rules, move generation, search (minimax, MCTS, NNUE, etc.).
- **RTT Shim:** Translates engine position/state into RTT primitives and feeds back adjusted evaluations or move preferences.
- **RTT Agentic Layer:** Applies triadic logic to guide or re‑weight the engine’s choices.

---

## RTT Layer: Role per Engine

### Lumen (RTT/1) — Structural Extraction

- **Board topology:** piece graph, control maps, king safety regions.
- **Continuity anchors:** plans, threats, and long‑arc motifs (e.g., minority attack, central squeeze).
- **Resonance fields:** pressure over files, diagonals, complexes (light/dark squares).

### Hephaestus (RTT/2) — Regime Mapping

- **1/3 (Material):** captures, trades, raw piece count.
- **2/3 (Structure):** pawn chains, outposts, open lines, weak complexes.
- **3/3 (Continuity):** plan integrity, narrative of the game, identity of the position (who is “playing for what”).

Hephaestus tags each candidate move with its regime profile, allowing RTT to prefer moves that maintain or improve continuity rather than just short‑term gain.

### Aurion (RTT/3) — Topology & Loop Stability

- **Loop detection:** repeated motifs, cycling attacks, perpetual threats.
- **Projection loss:** where a move breaks the long‑arc plan or collapses a resonance field.
- **Ancestry:** how current choices relate to earlier commitments (opening choice, pawn structure decisions).

Aurion flags moves that introduce paradox or unstable loops, even if the engine’s raw eval likes them.

### Harmonia (RTT/12) — Unified Strategy

- Synthesizes:
  - material, structure, continuity,
  - resonance pressure,
  - drift/coherence balance,
  - operator lineage.
- Produces a **triadic score** per move or line, which the shim feeds back into the engine as:
  - eval adjustments,
  - move ordering hints,
  - pruning guidance.

---

## Shim Design

The shim sits between the engine’s evaluation/search and the RTT layer.

**Typical flow:**

1. **Engine** generates candidate moves and/or principal variations.
2. **Shim**:
   - converts the current position + candidate moves into RTT state,
   - calls Lumen → Hephaestus → Aurion → Harmonia,
   - receives triadic scores.
3. **Shim** feeds back:
   - modified evaluation scores,
   - reordered move lists,
   - optional “do not play” flags for paradoxical lines.
4. **Engine** continues search with RTT‑informed guidance.

Implementation‑wise, this usually hooks into:

- Stockfish: `eval()` and move ordering in `search.cpp`.
- Leela‑style engines: policy/value post‑processing before MCTS expansion.

---

## Use Cases

- **RTT‑Chess Bot:** A standalone engine that plays with triadic awareness.
- **Teaching Mode:** Show players:
  - regime tags per move (1/3 vs 2/3 vs 3/3),
  - resonance maps over the board,
  - continuity‑preserving vs continuity‑breaking moves.
- **Analysis Mode:** Evaluate human games for:
  - drift/coherence,
  - plan stability,
  - resonance‑pressure evolution.

---

## Files (Suggested Layout)

```text
/docs/bots/chess/
  README.md
  /logic/        # notes on chosen engine(s) and integration points
  /rtt/
    lumen.md
    hephaestus.md
    aurion.md
    harmonia.md
  /shim/
    stockfish_shim.md
    leela_shim.md
  /examples/
    rtt_chess_examples.md
  /analysis/
    regime_maps.md
    resonance_fields.md
```

---

> “I’m not always a Polymath… more often I’m just math…”

This module is exactly that: just math—triadic, operator‑first, resonance‑aware math—applied to chess.
