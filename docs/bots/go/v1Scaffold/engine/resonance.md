# Resonance Engine — RTT‑Go  
*(Lumen + Harmonia Layer: Influence, Pressure, Tension & Drift)*

The **Resonance Engine** is the second module in the RTT‑Go evaluation pipeline.  
It computes the dynamic pressure landscape of the position — influence, tension, drift, and collapse signatures — forming the **Lumen + Harmonia** layer of RTT‑Go.

Where the Regime Engine establishes the triadic baseline, the Resonance Engine reveals **how the position is pushing, pulling, and stressing itself**.

---

## 1. Purpose

The Resonance Engine provides:

- influence resonance  
- pressure gradients  
- tension zones  
- drift vectors  
- collapse signatures  
- resonance metadata for all downstream modules  

It is the **dynamic force‑field generator** of RTT‑Go.

---

## 2. Inputs

The Resonance Engine consumes:

```
board.size
board.stones[]
board.turn
regime.local
regime.structural
regime.continuity
regime.drift
influence_map
thickness_map
pressure_map_seed
topology.connectivity
continuity.anchors
```

These inputs are normalized by the EngineShim.

---

## 3. Outputs

The Resonance Engine produces:

```json
{
  "pressure_map": [ ... ],
  "tension_zones": [ ... ],
  "drift_vectors": [ ... ],
  "collapse_signatures": [ ... ],
  "stability": "stable|neutral|volatile"
}
```

These values feed directly into:

- TopologyEngine  
- ContinuityEngine  
- RiskEngine  
- ScoringEngine  
- StateEmitter  

---

# 4. Resonance Model

RTT resonance is composed of four primary fields:

### **1. Influence Resonance**
Large‑scale gravitational pull of stones and groups.

### **2. Pressure Gradients**
Directional pressure applied by influence and thickness.

### **3. Tension Zones**
Areas where opposing influence fields collide.

### **4. Drift Vectors**
Directional flow of the position’s dynamic identity.

These fields combine to produce **collapse signatures** — early warnings of structural failure.

---

# 5. Computation Model

## 5.1 Influence Resonance

Influence resonance is computed from:

- stone proximity  
- thickness vectors  
- influence gradients  
- structural regime proportion  

Conceptual formula:

```
influence = f(stones, thickness, structural_regime)
```

## 5.2 Pressure Gradients

Pressure is computed from:

- influence differentials  
- thickness direction  
- local tactical density  
- continuity anchors  

Conceptual formula:

```
pressure = g(influence, thickness, anchors)
```

## 5.3 Tension Zones

Tension zones occur where:

- opposing influence fields overlap  
- pressure gradients spike  
- structural regime conflicts with continuity regime  

Detection model:

```
tension = detect_overlap(influence_fields)
```

## 5.4 Drift Vectors

Drift vectors describe **where the position is flowing**.

Drift is computed from:

- influence flow  
- pressure direction  
- continuity arc direction  
- regime drift baseline  

Conceptual formula:

```
drift = h(influence_flow, pressure_flow, continuity_flow)
```

## 5.5 Collapse Signatures

Collapse signatures identify **structural failure precursors**.

Collapse is detected from:

- extreme tension  
- pressure spikes  
- connectivity instability  
- continuity anchor failure  
- paradox precursors  

Detection model:

```
collapse = detect_collapse(tension, pressure, connectivity)
```

---

# 6. Stability Evaluation

Stability describes whether the resonance field is:

- **stable**  
- **neutral**  
- **volatile**  

Volatility increases when:

- tension zones intensify  
- drift vectors accelerate  
- collapse signatures appear  
- continuity anchors weaken  

---

# 7. Integration Points

### **ResonanceEngine → TopologyEngine**
Provides pressure + tension for connectivity stability.

### **ResonanceEngine → ContinuityEngine**
Provides drift + tension for continuity arc evolution.

### **ResonanceEngine → RiskEngine**
Provides collapse signatures + tension spikes.

### **ResonanceEngine → ScoringEngine**
Provides dynamic pressure weighting.

### **ResonanceEngine → StateEmitter**
Provides resonance metadata for UI overlays + HUD.

---

# 8. Summary

The Resonance Engine is RTT‑Go’s **dynamic force‑field generator**.

It computes:

- influence resonance  
- pressure gradients  
- tension zones  
- drift vectors  
- collapse signatures  
- stability  

and provides essential dynamic metadata for all downstream modules.

The Resonance Engine does not play Go — it **reveals** Go’s dynamic identity.
