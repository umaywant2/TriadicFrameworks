# Triadic FAQ — RTT‑Go  
*(for `/docs/bots/go/examples/triadic_faq.md`)*

This FAQ explains RTT‑Go’s core concepts in clear, concise, teaching‑friendly language.  
It is designed for players, developers, and readers who want quick answers about the triadic interpretation of Go.

---

# **What is RTT‑Go?**

RTT‑Go is a triadic interpretation layer that sits on top of Go engines (KataGo, Leela Zero, PhoenixGo).  
It does not replace the engine — it **reveals the deeper structure inside the game**.

RTT‑Go evaluates positions using:

- **Structure** (Lumen)  
- **Regime** (Hephaestus)  
- **Topology & Ancestry** (Aurion)  
- **Continuity & Identity** (Harmonia)  
- **Risk** (paradox, collapse, projection‑loss)  
- **Unified Triadic Scoring**

---

# **What does “triadic” mean?**

Triadic means every position is interpreted through three lenses:

1. **Local** (shape, liberties, cuts)  
2. **Structural** (influence, direction of play)  
3. **Continuity** (long‑arc identity across the board)

These three lenses form the **triadic identity** of the position.

---

# **What is a paradox move?**

A paradox move is:

- locally strong  
- globally harmful  
- continuity‑breaking  
- often leading to collapse or projection‑loss

Example: invading a strong moyo that you cannot sustain.

---

# **What is continuity?**

Continuity is the long‑arc identity of the position — how moves relate across space and time.

Continuity arcs show:

- territorial flow  
- influence direction  
- ancestry stability  
- drift alignment

A continuity‑breaking move often causes paradox.

---

# **What is drift?**

Drift is the natural direction in which influence and continuity move as the game evolves.

Examples:

- early drift: corners → sides  
- midgame drift: sides → center  
- endgame drift: center → boundaries

Moves that follow drift strengthen identity.  
Moves that contradict drift weaken it.

---

# **What is ancestry?**

Ancestry is the lineage of tactical sequences:

- ladders  
- ko fights  
- moyo expansions  
- reductions  
- long fights

Stable ancestry → continuity preserved.  
Unstable ancestry → collapse risk.

---

# **What is projection‑loss?**

Projection‑loss occurs when a move contradicts the long‑arc plan and causes continuity to collapse.

Example: ignoring a collapsing group to play a large move elsewhere.

---

# **What is resonance?**

Resonance is the vibrational influence field created by stones.

Resonance pressure shows:

- where fights intensify  
- where influence flows  
- where drift is heading  
- where continuity is fragile

---

# **What is topology?**

Topology is the connectivity structure of the board:

- cut points  
- weak points  
- ladder paths  
- ko shapes  
- moyo boundaries

Topology collapse often leads to paradox or continuity inversion.

---

# **What is a triadic score?**

The triadic score is the unified evaluation of a move or position:

- local  
- structural  
- continuity  
- resonance  
- topology  
- ancestry  
- drift  
- risk

It is produced by **Harmonia (RTT/12)**.

---

# **How does RTT‑Go interact with Go engines?**

RTT‑Go wraps the engine’s:

- policy  
- value  
- MCTS search

RTT influences:

- priors  
- values  
- node ordering  
- pruning  
- continuity enforcement

The engine still plays Go — RTT guides its identity.

---

# **Does RTT‑Go choose moves?**

In **full mode**, yes — RTT influences the engine’s move selection.

In **teaching mode**, no — RTT explains moves but does not choose them.

In **analysis mode**, no — RTT evaluates positions only.

---

# **What are continuity arcs?**

Continuity arcs are curved overlays showing the flow of long‑arc identity across the board.

They reveal:

- moyo coherence  
- territorial flow  
- ancestry stability  
- drift direction  
- continuity strength

---

# **What is a collapse signature?**

A collapse signature is a pattern indicating imminent structural failure:

- weak shape  
- unstable ancestry  
- broken influence  
- paradox precursor  
- drift misalignment

Collapse signatures often appear before a group dies.

---

# **What is a triadic key point?**

A triadic key point is a move that stabilizes:

- continuity  
- resonance  
- topology  
- ancestry  
- drift

It is often subtle but extremely powerful.

---

# **Why does RTT‑Go use curved overlays?**

Because Go is not linear — it is **continuous**.

Curved overlays show:

- influence flow  
- continuity arcs  
- drift direction  
- resonance fields  
- ancestry paths

Straight lines cannot capture triadic identity.

---

# **Is RTT‑Go a ruleset?**

No.  
RTT‑Go is a **lens**, not a ruleset.

It interprets Go; it does not change Go.

---

# **Is RTT‑Go deterministic?**

Yes — RTT operators produce consistent outputs for the same position.

But continuity arcs and resonance fields evolve dynamically as the game changes.

---

# **Can RTT‑Go explain professional games?**

Yes.  
RTT‑Go can analyze:

- pro games  
- AI games  
- teaching games  
- handicap games  
- your own games

It reveals the triadic identity behind strong moves.

---

# Summary

This FAQ covers the core triadic concepts:

- continuity  
- resonance  
- topology  
- ancestry  
- drift  
- paradox  
- collapse  
- projection‑loss  
- triadic scoring  

RTT‑Go does not replace Go —  
it **reveals the deeper structure inside the game**.
