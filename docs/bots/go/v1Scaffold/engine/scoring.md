# Scoring Engine — RTT‑Go  
*(Harmonia Layer: Local, Structural, Continuity & Unified Triadic Score)*

The **Scoring Engine** is the sixth module in the RTT‑Go evaluation pipeline.  
It computes the triadic score of the position — a unified measure of local strength, structural stability, continuity identity, and risk severity.

Where the Regime, Resonance, Topology, Continuity, and Risk engines compute triadic primitives, the Scoring Engine **integrates** them into a single coherent triadic score.

This module defines the **Harmonia layer** of RTT‑Go.

---

## 1. Purpose

The Scoring Engine provides:

- local score  
- structural score  
- continuity score  
- unified triadic score  
- score metadata for diagnostics, timeline, and UI  

It is the **triadic synthesis engine** of RTT‑Go.

---

## 2. Inputs

The Scoring Engine consumes:

```
regime.local
regime.structural
regime.continuity
resonance.pressure_map
resonance.tension_zones
topology.connectivity
topology.cut_points
continuity.territorial_arcs
continuity.influence_arcs
continuity.moyo_arcs
continuity.identity_inversion_risk
risk.severity
risk.paradox
risk.collapse
risk.projection_loss
```

These inputs are normalized by the EngineShim.

---

## 3. Outputs

The Scoring Engine produces:

```json
{
  "local": 0.41,
  "structural": 0.33,
  "continuity": 0.26,
  "final": 0.68,
  "stability": "stable|neutral|volatile"
}
```

These values feed directly into:

- Diagnostics  
- Timeline  
- StateEmitter  

---

# 4. Scoring Model

RTT scoring is composed of four triadic primitives:

### **1. Local Score**
Tactical strength, shape stability, liberty health.

### **2. Structural Score**
Influence, thickness, pressure stability, connectivity.

### **3. Continuity Score**
Long‑arc identity, territorial arcs, moyo arcs, ancestry arcs.

### **4. Unified Triadic Score**
Weighted synthesis of all three, adjusted by risk severity.

These primitives define the **triadic strength** of the position.

---

# 5. Computation Model

## 5.1 Local Score

Local score is computed from:

- liberties  
- shape stability  
- adjacency density  
- tactical threat index  
- local fight clusters  

Conceptual model:

```
local_score = f(liberties, shape, adjacency, threats)
```

---

## 5.2 Structural Score

Structural score is computed from:

- influence gradients  
- thickness vectors  
- pressure stability  
- connectivity stability  
- cutting‑point density  

Conceptual model:

```
structural_score = g(influence, thickness, pressure, connectivity)
```

---

## 5.3 Continuity Score

Continuity score is computed from:

- territorial arcs  
- influence arcs  
- moyo arcs  
- ancestry arcs  
- identity inversion risk  

Conceptual model:

```
continuity_score = h(arcs, anchors, inversion_risk)
```

---

## 5.4 Unified Triadic Score

The unified triadic score synthesizes:

```
final_score = w1 * local
             + w2 * structural
             + w3 * continuity
             - risk_penalty
```

Where:

- `w1`, `w2`, `w3` are regime‑derived weights  
- `risk_penalty` is derived from risk severity  

Risk penalty model:

```
risk_penalty = severity_factor(risk.severity)
```

Severity factors:

- **low** → minimal penalty  
- **medium** → moderate penalty  
- **high** → strong penalty  

---

## 5.5 Stability Evaluation

Score stability describes whether the triadic score is:

- **stable**  
- **neutral**  
- **volatile**  

Volatility increases when:

- risk severity increases  
- continuity arcs destabilize  
- connectivity weakens  
- pressure spikes  

---

# 6. Integration Points

### **ScoringEngine → Diagnostics**
Provides triadic score breakdown for commentary.

### **ScoringEngine → Timeline**
Provides score evolution across moves.

### **ScoringEngine → StateEmitter**
Provides triadic score metadata for UI overlays + HUD.

---

# 7. Summary

The Scoring Engine is RTT‑Go’s **triadic synthesis engine**.

It computes:

- local score  
- structural score  
- continuity score  
- unified triadic score  
- stability  

and provides essential triadic strength metadata for all downstream modules.

The Scoring Engine does not play Go — it **reveals** Go’s triadic strength.
