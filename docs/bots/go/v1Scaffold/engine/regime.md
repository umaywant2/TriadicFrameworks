# Regime Engine — RTT‑Go  
*(Hephaestus Layer: Local / Structural / Continuity Regime Computation)*

The **Regime Engine** is the first module in the RTT‑Go evaluation pipeline.  
It computes the triadic regime identity of the position — the balance between **local**, **structural**, and **continuity** forces acting on the board.

This module defines the **Hephaestus layer** of RTT‑Go.

---

## 1. Purpose

The Regime Engine provides:

- local/structural/continuity regime proportions  
- regime drift direction + magnitude  
- conflict zone detection  
- stability evaluation  
- regime metadata for all downstream modules  

It establishes the **triadic baseline** for the entire engine pipeline.

---

## 2. Inputs

The Regime Engine consumes:

```
board.size
board.stones[]
board.turn
board.ko
move_history[]
local_shape_metrics
influence_metrics
continuity_anchor_candidates
```

These inputs are engine‑agnostic and provided by the EngineShim.

---

## 3. Outputs

The Regime Engine produces:

```json
{
  "local": 0.41,
  "structural": 0.33,
  "continuity": 0.26,
  "drift": {
    "from": "right",
    "to": "center",
    "strength": 0.72
  },
  "conflict_zones": [ "right_side" ],
  "stability": "volatile"
}
```

These values feed directly into:

- ResonanceEngine  
- TopologyEngine  
- ContinuityEngine  
- RiskEngine  
- ScoringEngine  
- StateEmitter  

---

## 4. Regime Model

RTT defines three fundamental regimes:

### **Local Regime (1/3) — Tactical Reality**
- liberties  
- shape  
- adjacency  
- immediate threats  
- local fights  

### **Structural Regime (2/3) — Direction of Play**
- influence  
- thickness  
- flow  
- positional gravity  
- large‑scale pressure  

### **Continuity Regime (3/3) — Long‑Arc Identity**
- moyo arcs  
- territorial arcs  
- ancestry arcs  
- continuity anchors  
- identity inversion risk  

The Regime Engine computes the **proportion** of each regime in the current position.

---

## 5. Computation Model

### 5.1 Local Regime Computation
Local regime is computed from:

- liberty counts  
- shape stability  
- adjacency density  
- tactical threat index  
- local fight clusters  

Formula (conceptual):

```
local = f(liberties, shape, adjacency, threats)
```

### 5.2 Structural Regime Computation
Structural regime is computed from:

- influence gradients  
- thickness vectors  
- direction‑of‑play fields  
- pressure zones  
- structural drift  

Formula (conceptual):

```
structural = g(influence, thickness, flow, pressure)
```

### 5.3 Continuity Regime Computation
Continuity regime is computed from:

- territorial arcs  
- moyo arcs  
- ancestry arcs  
- continuity anchors  
- identity inversion risk  

Formula (conceptual):

```
continuity = h(arcs, anchors, inversion_risk)
```

---

## 6. Regime Drift

Regime drift describes **how the triadic identity is shifting**.

Example:

```
from: right_side
to: center
strength: 0.72
```

Drift is computed from:

- influence flow  
- continuity arc direction  
- pressure gradients  
- topology changes  

---

## 7. Conflict Zones

Conflict zones identify areas where regime forces collide.

Example:

```
conflict_zones: ["right_side"]
```

Conflict detection uses:

- local vs structural mismatch  
- continuity vs structural tension  
- collapse signatures  
- paradox precursors  

---

## 8. Stability Evaluation

Stability describes whether the regime distribution is:

- **stable**  
- **neutral**  
- **volatile**  

Volatility increases when:

- drift strength is high  
- conflict zones are active  
- continuity anchors are weak  
- collapse signatures appear  

---

## 9. Integration Points

### **RegimeEngine → ResonanceEngine**
Provides structural baseline for resonance computation.

### **RegimeEngine → TopologyEngine**
Provides conflict zones and drift direction.

### **RegimeEngine → ContinuityEngine**
Provides continuity proportion baseline.

### **RegimeEngine → RiskEngine**
Provides paradox/collapse precursors.

### **RegimeEngine → ScoringEngine**
Provides triadic score weighting.

### **RegimeEngine → StateEmitter**
Provides regime metadata for UI.

---

## 10. Summary

The Regime Engine is RTT‑Go’s **triadic baseline generator**.

It computes:

- local regime  
- structural regime  
- continuity regime  
- regime drift  
- conflict zones  
- stability  

and provides foundational triadic metadata for all downstream modules.

The Regime Engine does not play Go — it **reveals** Go’s triadic identity.
