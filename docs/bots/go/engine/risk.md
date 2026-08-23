# Risk Engine — RTT‑Go  
*(Paradox, Collapse, Projection‑Loss & Severity Computation)*

The **Risk Engine** is the fifth module in the RTT‑Go evaluation pipeline.  
It detects structural, dynamic, and long‑arc failure conditions — paradox, collapse, projection‑loss, and identity instability — forming the **paradox/collapse layer** of RTT‑Go.

Where the Regime, Resonance, Topology, and Continuity engines compute triadic identity, the Risk Engine determines **where that identity is at risk of breaking**.

This module defines the **critical‑state intelligence layer** of RTT‑Go.

---

## 1. Purpose

The Risk Engine provides:

- paradox detection  
- collapse detection  
- projection‑loss detection  
- risk severity evaluation  
- risk metadata for scoring, diagnostics, timeline, and UI  

It is the **triadic failure‑detection engine** of RTT‑Go.

---

## 2. Inputs

The Risk Engine consumes:

```
regime.drift
regime.conflict_zones
resonance.tension_zones
resonance.pressure_map
resonance.collapse_signatures
topology.connectivity
topology.cut_points
topology.boundaries
topology.ancestry
topology.collapse
continuity.anchors
continuity.drift
continuity.identity_inversion_risk
```

These inputs are normalized by the EngineShim.

---

## 3. Outputs

The Risk Engine produces:

```json
{
  "paradox": [ ... ],
  "collapse": [ ... ],
  "projection_loss": [ ... ],
  "severity": "low|medium|high",
  "stability": "stable|neutral|volatile"
}
```

These values feed directly into:

- ScoringEngine  
- Diagnostics  
- Timeline  
- StateEmitter  

---

# 4. Risk Model

RTT risk is composed of three critical primitives:

### **1. Paradox**
Contradictions between structural, dynamic, and continuity identity.

### **2. Collapse**
Structural failure precursors or active breakdown.

### **3. Projection‑Loss**
Loss of long‑arc identity or continuity projection.

These primitives define the **critical‑state behavior** of the position.

---

# 5. Computation Model

## 5.1 Paradox Detection

Paradox occurs when:

- continuity arcs contradict structural arcs  
- regime drift contradicts resonance drift  
- ancestry arcs contradict connectivity  
- anchors collapse while pressure increases  

Detection model:

```
paradox = detect_paradox(regime, resonance, topology, continuity)
```

Paradox is often a precursor to collapse.

---

## 5.2 Collapse Detection

Collapse occurs when:

- connectivity becomes unstable  
- tension spikes beyond threshold  
- pressure overwhelms boundaries  
- continuity anchors fail  
- paradox intensifies  

Detection model:

```
collapse = detect_collapse(connectivity, tension, pressure, anchors)
```

Collapse signatures may be local, structural, or long‑arc.

---

## 5.3 Projection‑Loss Detection

Projection‑loss occurs when:

- continuity arcs lose coherence  
- drift reverses direction  
- anchors destabilize  
- ancestry arcs collapse  
- identity inversion risk spikes  

Detection model:

```
projection_loss = detect_projection_loss(arcs, anchors, drift)
```

Projection‑loss is the long‑arc counterpart to collapse.

---

## 5.4 Risk Severity

Severity is computed from:

- paradox count  
- collapse magnitude  
- projection‑loss intensity  
- drift acceleration  
- anchor stability  
- ancestry stability  

Severity scale:

- **low** — stable identity  
- **medium** — identity under stress  
- **high** — identity at risk of failure  

---

## 5.5 Stability Evaluation

Risk stability describes whether the critical‑state identity is:

- **stable**  
- **neutral**  
- **volatile**  

Volatility increases when:

- paradox intensifies  
- collapse signatures multiply  
- projection‑loss accelerates  
- drift destabilizes  
- anchors weaken  

---

# 6. Integration Points

### **RiskEngine → ScoringEngine**
Provides severity weighting for triadic scoring.

### **RiskEngine → Diagnostics**
Provides paradox/collapse/projection‑loss metadata.

### **RiskEngine → Timeline**
Provides collapse/paradox events for playback.

### **RiskEngine → StateEmitter**
Provides risk metadata for UI overlays + HUD.

---

# 7. Summary

The Risk Engine is RTT‑Go’s **critical‑state intelligence engine**.

It computes:

- paradox  
- collapse  
- projection‑loss  
- severity  
- stability  

and provides essential failure‑state metadata for all downstream modules.

The Risk Engine does not play Go — it **reveals** where Go’s triadic identity is at risk.
