# Continuity Engine — RTT‑Go  
*(Aurion + Harmonia Layer: Territorial, Influence, Moyo, Ancestry & Identity)*

The **Continuity Engine** is the fourth module in the RTT‑Go evaluation pipeline.  
It computes the long‑arc identity of the position — how groups, territories, moyos, and ancestries evolve across time and space.

Where the Regime Engine establishes the triadic baseline, the Resonance Engine reveals dynamic pressure, and the Topology Engine defines structural wiring, the Continuity Engine determines **how the position persists, transforms, or collapses across arcs**.

This module defines the **Aurion + Harmonia long‑arc layer** of RTT‑Go.

---

## 1. Purpose

The Continuity Engine provides:

- territorial arcs  
- influence arcs  
- moyo arcs  
- ancestry arcs  
- continuity anchors  
- continuity drift  
- identity inversion risk  
- long‑arc metadata for risk, scoring, and UI  

It is the **temporal‑structural identity engine** of RTT‑Go.

---

## 2. Inputs

The Continuity Engine consumes:

```
board.size
board.stones[]
board.turn
regime.continuity
regime.drift
resonance.pressure_map
resonance.drift_vectors
topology.connectivity
topology.boundaries
topology.ancestry
topology.collapse
```

These inputs are normalized by the EngineShim.

---

## 3. Outputs

The Continuity Engine produces:

```json
{
  "territorial_arcs": [ ... ],
  "influence_arcs": [ ... ],
  "moyo_arcs": [ ... ],
  "ancestry_arcs": [ ... ],
  "anchors": [ "left_moyo_boundary" ],
  "drift": {
    "direction": "right_to_center",
    "strength": 0.72
  },
  "identity_inversion_risk": "medium",
  "stability": "stable|neutral|volatile"
}
```

These values feed directly into:

- RiskEngine  
- ScoringEngine  
- Timeline  
- StateEmitter  

---

# 4. Continuity Model

RTT continuity is composed of five long‑arc primitives:

### **1. Territorial Arcs**
Long‑range territorial flow across the board.

### **2. Influence Arcs**
Large‑scale influence movement and evolution.

### **3. Moyo Arcs**
Moyo formation, expansion, contraction, and collapse.

### **4. Ancestry Arcs**
Ladder, ko, and structural lineage across moves.

### **5. Continuity Anchors**
Stable points that preserve identity across arcs.

These primitives define the **long‑arc identity** of the position.

---

# 5. Computation Model

## 5.1 Territorial Arcs

Territorial arcs are computed from:

- boundary topology  
- influence gradients  
- pressure direction  
- continuity anchors  

Conceptual model:

```
territorial_arcs = compute_territorial(boundaries, influence, anchors)
```

---

## 5.2 Influence Arcs

Influence arcs describe **how influence flows across time**.

Computed from:

- influence resonance  
- drift vectors  
- structural regime  
- continuity anchors  

Conceptual model:

```
influence_arcs = compute_influence(influence, drift, anchors)
```

---

## 5.3 Moyo Arcs

Moyo arcs describe:

- moyo formation  
- moyo expansion  
- moyo contraction  
- moyo collapse  

Computed from:

- territorial arcs  
- pressure gradients  
- continuity drift  
- topology collapse signatures  

Conceptual model:

```
moyo_arcs = compute_moyo(territorial_arcs, pressure, collapse)
```

---

## 5.4 Ancestry Arcs

Ancestry arcs track:

- ladder lineage  
- ko lineage  
- structural ancestry  
- collapse ancestry  

Computed from:

- topology ancestry  
- pressure  
- drift  
- collapse signatures  

Conceptual model:

```
ancestry_arcs = compute_ancestry(ancestry, pressure, drift)
```

---

## 5.5 Continuity Anchors

Continuity anchors are **stable identity points**.

Anchors are detected when:

- boundaries remain stable  
- influence arcs remain consistent  
- ancestry arcs remain stable  
- drift vectors remain coherent  

Detection model:

```
anchors = detect_anchors(boundaries, influence_arcs, ancestry_arcs)
```

---

## 5.6 Continuity Drift

Continuity drift describes **how long‑arc identity is shifting**.

Example:

```
direction: right_to_center
strength: 0.72
```

Drift is computed from:

- influence arc direction  
- territorial arc direction  
- moyo arc direction  
- ancestry arc direction  

Conceptual model:

```
drift = compute_drift(territorial_arcs, influence_arcs, moyo_arcs)
```

---

## 5.7 Identity Inversion Risk

Identity inversion occurs when:

- continuity arcs contradict structural arcs  
- anchors collapse  
- drift reverses direction  
- ancestry arcs destabilize  
- paradox precursors appear  

Detection model:

```
identity_inversion_risk = detect_inversion(arcs, anchors, drift)
```

---

# 6. Stability Evaluation

Continuity stability describes whether long‑arc identity is:

- **stable**  
- **neutral**  
- **volatile**  

Volatility increases when:

- arcs diverge  
- anchors weaken  
- drift accelerates  
- collapse signatures appear  

---

# 7. Integration Points

### **ContinuityEngine → RiskEngine**
Provides inversion risk + arc instability.

### **ContinuityEngine → ScoringEngine**
Provides continuity score weighting.

### **ContinuityEngine → Timeline**
Provides arc evolution for playback.

### **ContinuityEngine → StateEmitter**
Provides continuity metadata for UI overlays + HUD.

---

# 8. Summary

The Continuity Engine is RTT‑Go’s **long‑arc identity engine**.

It computes:

- territorial arcs  
- influence arcs  
- moyo arcs  
- ancestry arcs  
- continuity anchors  
- continuity drift  
- identity inversion risk  
- stability  

and provides essential temporal‑structural metadata for all downstream modules.

The Continuity Engine does not play Go — it **reveals** Go’s long‑arc identity.
