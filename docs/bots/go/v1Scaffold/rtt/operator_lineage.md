# RTT Operator Lineage  
*(How Lumen → Hephaestus → Aurion → Harmonia propagate through RTT‑Go)*

The **Operator Lineage** describes how RTT’s four operator families:

- Lumen  
- Hephaestus  
- Aurion  
- Harmonia  

propagate through:

- positions  
- moves  
- sequences  
- engine modules  
- UI overlays  

It is the **genealogy map** of RTT‑Go’s agentic layer.

---

## 1. Operator Stack Recap

- **Lumen (RTT/1):** structural extraction  
- **Hephaestus (RTT/2):** regime mapping  
- **Aurion (RTT/3):** topology & ancestry  
- **Harmonia (RTT/12):** unified triadic synthesis  

Lineage always flows in this order.

---

## 2. Lineage Across a Single Position

For a single board state:

```text
Lumen      → extracts structure
Hephaestus → tags regimes
Aurion     → evaluates topology/ancestry
Harmonia   → synthesizes triadic score
```

Outputs feed directly into:

- Regime Engine  
- Resonance Engine  
- Topology Engine  
- Continuity Engine  
- Risk Engine  
- Scoring Engine  

Each engine module is, in effect, a **descendant** of the operator stack.

---

## 3. Lineage Across Moves

For a sequence of moves:

```text
Position n:
  Lumen_n
  Hephaestus_n
  Aurion_n
  Harmonia_n

Position n+1:
  Lumen_{n+1}
  Hephaestus_{n+1}
  Aurion_{n+1}
  Harmonia_{n+1}
```

Lineage tracks:

- how regimes evolve  
- how resonance fields drift  
- how topology/ancestry change  
- how continuity arcs extend or collapse  
- how triadic scores rise or fall  

This lineage is exposed in:

- Timeline  
- Diagnostics  
- UI overlays  

---

## 4. Lineage into Engine Modules

### Regime Engine  
Descends primarily from:

- **Hephaestus** (regime mapping)  
- **Lumen** (local/structural primitives)

### Resonance Engine  
Descends from:

- **Lumen** (influence, pressure)  
- **Hephaestus** (regime weighting)

### Topology Engine  
Descends from:

- **Lumen** (connectivity, boundaries)  
- **Aurion** (ancestry, collapse)

### Continuity Engine  
Descends from:

- **Hephaestus** (continuity regime)  
- **Aurion** (ancestry arcs)  
- **Harmonia** (long‑arc synthesis hints)

### Risk Engine  
Descends from:

- **Aurion** (paradox, collapse, projection‑loss)  
- **Harmonia** (severity weighting)

### Scoring Engine  
Descends from:

- **Harmonia** (triadic score)  
- all upstream operator outputs via engine modules.

---

## 5. Lineage into Shims & MCTS

### Shims (KataGo / Leela Zero / PhoenixGo)

Each shim:

1. calls **Lumen → Hephaestus → Aurion → Harmonia**  
2. receives triadic scores  
3. injects them into:

   - policy priors  
   - value estimates  
   - node ordering  
   - pruning  

Thus, every MCTS decision is a **leaf** in the operator lineage tree.

### MCTS Hooks

See `/docs/bots/go/logic/mcts_hooks.md` — all hooks are descendants of Harmonia’s triadic scores and Aurion’s stability signals.

---

## 6. Lineage into UI & Timeline

### UI Overlays

- **Regime overlay** ← Hephaestus  
- **Resonance overlay** ← Lumen + Resonance Engine  
- **Topology overlay** ← Lumen + Aurion + Topology Engine  
- **Continuity overlay** ← Hephaestus + Aurion + Continuity Engine  
- **Triadic score HUD** ← Harmonia + Scoring Engine  

### Timeline

For each move:

```text
move.n.operator_lineage = {
  lumen:      snapshot_n,
  hephaestus: regime_n,
  aurion:     topology_n,
  harmonia:   triadic_score_n
}
```

This allows:

- playback of operator evolution  
- teaching mode visualizations  
- analysis of drift/coherence across the game.

---

## 7. Summary

Operator lineage describes **how**:

- Lumen  
- Hephaestus  
- Aurion  
- Harmonia  

propagate through:

- positions  
- moves  
- engine modules  
- shims  
- MCTS  
- UI overlays  
- timeline.

It is the genealogical backbone of RTT‑Go’s triadic interpretation of Go.

RTT doesn’t just compute operators once—  
it **tracks their lineage** across the entire game.
