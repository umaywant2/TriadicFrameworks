# Topology Engine — RTT‑Go  
*(Aurion Layer: Connectivity, Boundaries, Cutting Points, Ancestry & Collapse)*  
  [github.com](https://github.com/umaywant2/TriadicFrameworks/edit/main/docs/bots/go/engine/topology.md)

The **Topology Engine** is the third module in the RTT‑Go evaluation pipeline.  
It computes the structural identity of the position — connectivity, boundaries, cutting points, ancestry, and collapse signatures.

Where the Regime Engine establishes the triadic baseline and the Resonance Engine reveals dynamic pressure, the Topology Engine determines **how the position is structurally wired**.

This module defines the **Aurion layer** of RTT‑Go.

---

## 1. Purpose

The Topology Engine provides:

- connectivity graph  
- cutting‑point detection  
- boundary topology  
- ladder/ko ancestry  
- topology collapse detection  
- structural metadata for continuity, risk, and scoring  

It is the **structural intelligence engine** of RTT‑Go.

---

## 2. Inputs

The Topology Engine consumes:

```
board.size
board.stones[]
board.turn
regime.conflict_zones
resonance.pressure_map
resonance.tension_zones
resonance.collapse_signatures
continuity.anchors
```

These inputs are normalized by the EngineShim.

---

## 3. Outputs

The Topology Engine produces:

```json
{
  "connectivity": { ... },
  "cut_points": [ "D4", "E5" ],
  "boundaries": [ ... ],
  "ancestry": {
    "ladder": "stable",
    "ko": "volatile"
  },
  "collapse": [ ... ],
  "stability": "stable|neutral|volatile"
}
```

These values feed directly into:

- ContinuityEngine  
- RiskEngine  
- ScoringEngine  
- StateEmitter  

---

# 4. Topology Model

RTT topology is composed of five structural primitives:

### **1. Connectivity Graph**
Group‑level structural wiring.

### **2. Cutting Points**
Points whose removal changes connectivity.

### **3. Boundary Topology**
Edges, perimeters, and structural boundaries.

### **4. Ancestry**
Ladder and ko lineage.

### **5. Collapse Signatures**
Structural failure precursors.

These primitives define the **structural backbone** of the position.

---

# 5. Computation Model

## 5.1 Connectivity Graph

Connectivity is computed from:

- adjacency  
- liberties  
- shared liberties  
- influence pressure  
- tension zones  

Conceptual model:

```
connectivity = build_graph(stones, adjacency, pressure)
```

Connectivity stability is derived from:

- pressure gradients  
- tension zones  
- collapse signatures  

---

## 5.2 Cutting Points

Cutting points are detected when:

- removing a stone splits a group  
- pressure gradients spike  
- tension zones overlap  
- continuity anchors weaken  

Detection model:

```
cut_points = detect_cut_points(connectivity, pressure, tension)
```

---

## 5.3 Boundary Topology

Boundary topology describes:

- group perimeters  
- territorial boundaries  
- moyo boundaries  
- structural edges  

Boundary stability is influenced by:

- pressure  
- drift  
- continuity anchors  

---

## 5.4 Ancestry (Ladder + Ko)

Ancestry determines whether:

- ladders are stable, unstable, or collapsing  
- ko ancestry is stable, volatile, or collapsing  

Ancestry is computed from:

- connectivity  
- pressure  
- tension  
- drift  
- collapse signatures  

Example output:

```
ancestry.ladder = "stable"
ancestry.ko = "volatile"
```

---

## 5.5 Topology Collapse

Topology collapse occurs when:

- connectivity becomes unstable  
- tension spikes  
- pressure overwhelms boundaries  
- continuity anchors fail  
- paradox precursors appear  

Detection model:

```
collapse = detect_topology_collapse(connectivity, pressure, tension, anchors)
```

---

# 6. Stability Evaluation

Topology stability describes whether the structural identity is:

- **stable**  
- **neutral**  
- **volatile**  

Volatility increases when:

- cutting points multiply  
- boundaries weaken  
- ancestry becomes unstable  
- collapse signatures appear  

---

# 7. Integration Points

### **TopologyEngine → ContinuityEngine**
Provides structural backbone for continuity arcs.

### **TopologyEngine → RiskEngine**
Provides collapse signatures + cutting points.

### **TopologyEngine → ScoringEngine**
Provides structural stability weighting.

### **TopologyEngine → StateEmitter**
Provides topology metadata for UI overlays + HUD.

---

# 8. Summary

The Topology Engine is RTT‑Go’s **structural intelligence engine**.

It computes:

- connectivity  
- cutting points  
- boundaries  
- ancestry  
- collapse  
- stability  

and provides essential structural metadata for all downstream modules.

The Topology Engine does not play Go — it **reveals** Go’s structural identity.
