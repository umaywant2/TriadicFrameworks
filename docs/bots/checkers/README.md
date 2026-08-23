# RTT Checkers Bot Module

This module describes how TriadicFrameworks integrates RTT agentic logic with existing Checkers engines to create an operator‑first, regime‑aware bot.

Checkers is ideal for RTT because it blends:
- forced sequences,
- structural tension,
- continuity arcs,
- projection‑loss traps,
- long‑arc strategy (king paths, laddering),
- resonance pressure across diagonals.

RTT enhances these native properties rather than replacing them.

---

## Overview

**Goal:**  
Wrap a standard Checkers engine with RTT’s triadic decision layer while preserving its native move generation, forced‑capture rules, and evaluation logic.

RTT adds:

- **Regime‑aware evaluation** (1/3 material, 2/3 structure, 3/3 continuity)
- **Resonance‑pressure fields** (diagonal control, ladder tension)
- **Triadic projection loss detection** (broken ladders, collapsed king paths)
- **Loop stability and ancestry tracking** (forced capture arcs)
- **Operator lineage** for move sequences

The result is a Checkers bot that plays with deeper strategic continuity and resonance awareness.

---

## Architecture

```text
[Checkers Engine]
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

- **Engine:** Handles rules, forced captures, move generation, kinging, and evaluation.
- **RTT Shim:** Converts board state + candidate moves into RTT primitives.
- **RTT Agentic Layer:** Applies triadic logic to guide or re‑weight choices.

---

## RTT Layer: Role per Engine

### Lumen (RTT/1) — Structural Extraction

Extracts Checkers‑specific RTT primitives:

- **Diagonal resonance:** control, tension, pressure.
- **Ladder topology:** multi‑jump sequences, forced arcs.
- **King path continuity:** long‑arc mobility and identity.
- **Structural anchors:** safe squares, protected chains.
- **Projection‑loss points:** moves that collapse ladders or expose forced captures.

Lumen produces a triadic structural snapshot of the board.

---

### Hephaestus (RTT/2) — Regime Mapping

Tags each move with its regime profile:

- **1/3 (Material):** captures, trades, kinging.
- **2/3 (Structure):** diagonal control, ladder building, chain stability.
- **3/3 (Continuity):** long‑arc plan integrity (king path, ladder arc, positional squeeze).

This reveals why some “legal” moves are structurally inferior.

---

### Aurion (RTT/3) — Topology & Loop Stability

Evaluates:

- **Forced‑capture loops:** stability, collapse risk.
- **Ladder ancestry:** multi‑jump sequences and their continuity.
- **Projection loss:** moves that break structural arcs.
- **Continuity collapse:** exposing forced captures or losing king path identity.

Aurion flags paradoxical moves even when the engine’s raw eval likes them.

---

### Harmonia (RTT/12) — Unified Strategy

Synthesizes:

- material,
- diagonal structure,
- continuity arcs,
- resonance pressure,
- drift/coherence balance,
- operator lineage.

Produces a **triadic score** per move, which the shim feeds back into the engine.

---

## Shim Design

The shim sits between the engine’s move generator and RTT’s triadic evaluation.

**Typical flow:**

1. **Engine** generates legal moves (including forced captures).
2. **Shim**:
   - converts board + candidate moves into RTT state,
   - calls Lumen → Hephaestus → Aurion → Harmonia,
   - receives triadic scores.
3. **Shim** reorders moves or selects the highest‑scoring one.
4. **Engine** executes the RTT‑informed move.

Integration points:

- **OpenCheckers engines:** eval hooks, move selection.
- **Minimax/MCTS bots:** post‑eval adjustment layer.
- **Custom engines:** decision loop injection.

---

## Use Cases

- **RTT‑Checkers Bot:** A bot that plays with triadic awareness.
- **Teaching Mode:** Show players:
  - regime tags per move,
  - resonance maps,
  - continuity arcs,
  - drift/coherence profiles.
- **Analysis Mode:** Evaluate games for:
  - ladder stability,
  - diagonal resonance,
  - king path continuity,
  - forced‑capture arcs.

---

## Files (Suggested Layout)

```text
/docs/bots/checkers/
  README.md
  /logic/        # engine notes: forced captures, kinging, eval
  /rtt/
    lumen.md
    hephaestus.md
    aurion.md
    harmonia.md
  /shim/
    generic_checkers_shim.md
  /examples/
    rtt_checkers_examples.md
  /analysis/
    regime_maps.md
    resonance_fields.md
```

---

> **“I’m not always a Polymath… more often I’m just math…”**

Checkers is pure structure, pressure, and continuity.  
RTT simply reveals the deeper math already inside it.
