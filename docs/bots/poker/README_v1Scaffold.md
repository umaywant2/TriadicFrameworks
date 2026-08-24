# RTT Poker Bot Module

This module describes how TriadicFrameworks integrates RTT agentic logic with existing poker engines (Texas Hold’em, Omaha, 7‑Card Stud, and common open‑source bots) to create an operator‑first, regime‑aware poker bot.

Poker is uniquely suited for RTT because it is fundamentally about:
- hidden information,
- probabilistic resonance,
- drift/coherence under uncertainty,
- long‑arc continuity of strategy,
- identity and narrative of play.

RTT enhances these native properties rather than replacing them.

---

## Overview

**Goal:**  
Wrap a standard poker engine with RTT’s triadic decision layer while preserving its native evaluation, hand‑ranking, and betting logic.

RTT adds:

- **Regime‑aware evaluation** (1/3 odds, 2/3 table structure, 3/3 continuity)
- **Resonance‑pressure fields** (betting pressure, pot momentum, player identity)
- **Triadic projection loss detection** (strategy collapse, bluff misalignment)
- **Loop stability and ancestry tracking** (betting arcs, narrative of hands)
- **Operator lineage** for betting sequences (not just card strength)

The result is a poker bot that plays with deeper strategic continuity and resonance awareness.

---

## Architecture

```text
[Client / Table Interface]
      |
      v
[Poker Engine]  (hand eval, odds, betting logic)
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

- **Poker Engine:** Handles rules, hand evaluation, pot calculation, and betting actions.
- **RTT Shim:** Converts table state + betting history into RTT primitives and feeds back triadic evaluations.
- **RTT Agentic Layer:** Applies triadic logic to guide or re‑weight the engine’s choices.

---

## RTT Layer: Role per Engine

### Lumen (RTT/1) — Structural Extraction

Extracts poker‑specific RTT primitives:

- **Hand resonance:** strength, potential, draw pressure.
- **Table topology:** number of players, stack sizes, position.
- **Betting arcs:** narrative of the hand (tight, loose, aggressive, passive).
- **Continuity anchors:** long‑arc strategy (tight‑aggressive, loose‑aggressive, trapping).
- **Hidden‑state identity:** opponent modeling, bluff potential.

Lumen produces a triadic structural snapshot of the table.

---

### Hephaestus (RTT/2) — Regime Mapping

Tags each action with its regime profile:

- **1/3 (Odds):** pot odds, hand equity, immediate EV.
- **2/3 (Structure):** position, stack pressure, table dynamics.
- **3/3 (Continuity):** narrative integrity, bluff consistency, identity of the hand.

This allows RTT to prefer actions that maintain continuity rather than just short‑term gain.

---

### Aurion (RTT/3) — Topology & Loop Stability

Evaluates:

- **Betting loops:** repeated aggression, pressure cycles, bluff arcs.
- **Projection loss:** actions that break the long‑arc plan.
- **Opponent ancestry:** how opponents’ actions relate to earlier commitments.
- **Continuity collapse:** where a bluff or value line becomes paradoxical.

Aurion flags actions that introduce paradox or collapse continuity—even if the engine’s raw EV likes them.

---

### Harmonia (RTT/12) — Unified Strategy

Synthesizes:

- odds,
- table structure,
- continuity,
- resonance pressure,
- drift/coherence balance,
- operator lineage.

Produces a **triadic score** per action, which the shim feeds back into the engine as:

- EV adjustments,
- action preference weighting,
- fold/call/raise guidance,
- bluff‑line stability checks.

---

## Shim Design

The shim sits between the engine’s action selection and RTT’s triadic evaluation.

**Typical flow:**

1. **Engine** evaluates hand strength and possible actions.
2. **Shim**:
   - converts table + betting history into RTT state,
   - calls Lumen → Hephaestus → Aurion → Harmonia,
   - receives triadic scores.
3. **Shim** reweights:
   - action EV,
   - bluff probability,
   - raise/call/fold thresholds.
4. **Engine** continues with RTT‑informed guidance.

Integration points:

- **OpenHoldem:** bot logic hooks for EV and action selection.
- **PokerSnowie‑style engines:** post‑EV adjustment layer.
- **Custom bots:** decision loop injection.

---

## Use Cases

- **RTT‑Poker Bot:** A standalone engine that plays with triadic awareness.
- **Teaching Mode:** Show players:
  - regime tags per action,
  - resonance maps,
  - continuity‑preserving vs continuity‑breaking lines.
- **Analysis Mode:** Evaluate hands for:
  - drift/coherence,
  - bluff stability,
  - pressure resonance,
  - continuity arcs.

---

## Files (Suggested Layout)

```text
/docs/bots/poker/
  README.md
  /logic/        # notes on chosen engine(s) and integration points
  /rtt/
    lumen.md
    hephaestus.md
    aurion.md
    harmonia.md
  /shim/
    openholdem_shim.md
    generic_poker_shim.md
  /examples/
    rtt_poker_examples.md
  /analysis/
    regime_maps.md
    resonance_fields.md
```

---

> **“I’m not always a Polymath… more often I’m just math…”**

Poker is math, psychology, pressure, and continuity.  
RTT simply reveals the deeper structure already inside it.
