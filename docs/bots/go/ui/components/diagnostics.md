# Diagnostics Component — RTT‑Go  
*(Internal Specification for Triadic Diagnostic Extraction & Reporting)*

The **Diagnostics Component** is RTT‑Go’s analytical subsystem.  
Where the viewer renders overlays and the HUD displays metadata, the diagnostics engine **computes**, **extracts**, and **summarizes** triadic intelligence for any move or state.

Diagnostics power:

- Teaching Mode commentary  
- Analysis Mode breakdowns  
- HUD commentary panel  
- timeline delta reporting  
- developer debugging overlays  
- triadic score computation  

It is the **analytical backbone** of RTT‑Go.

---

## 1. Purpose

The Diagnostics Component provides:

- triadic regime analysis  
- resonance field diagnostics  
- topology connectivity analysis  
- continuity‑arc evaluation  
- ancestry alignment checks  
- paradox/collapse detection  
- identity inversion detection  
- triadic score computation  
- delta analysis between moves  

It converts RTT primitives into **structured triadic insight**.

---

## 2. Diagnostics Architecture

Diagnostics consist of five internal modules:

```
RegimeDiagnostics
ResonanceDiagnostics
TopologyDiagnostics
ContinuityDiagnostics
RiskDiagnostics
```

Each module consumes triadic state and produces structured diagnostic output.

---

# 3. RegimeDiagnostics  
*(Analyzes local/structural/continuity regime identity)*

### Responsibilities
- compute regime proportions  
- detect regime drift  
- identify conflict zones  
- evaluate regime stability  

### Inputs
```
triadic.regime.local
triadic.regime.structural
triadic.regime.continuity
triadic.regime.drift
triadic.regime.conflict_zones
```

### Outputs
```
{
  "distribution": { ... },
  "drift": { ... },
  "conflicts": [ ... ],
  "stability": "stable|volatile"
}
```

### API Surface
```
analyzeRegime(regimeState)
```

---

# 4. ResonanceDiagnostics  
*(Analyzes influence, pressure, tension, drift)*

### Responsibilities
- detect high‑tension zones  
- evaluate pressure gradients  
- compute drift vector strength  
- detect collapse signatures  

### Inputs
```
triadic.resonance.pressure_map
triadic.resonance.tension_zones
triadic.resonance.drift_vectors
triadic.resonance.collapse_signatures
```

### Outputs
```
{
  "tension": [ ... ],
  "pressure": [ ... ],
  "drift": { ... },
  "collapse": [ ... ]
}
```

### API Surface
```
analyzeResonance(resonanceState)
```

---

# 5. TopologyDiagnostics  
*(Analyzes connectivity, boundaries, ancestry, collapse)*

### Responsibilities
- compute connectivity stability  
- detect cutting points  
- evaluate boundary topology  
- analyze ladder/ko ancestry  
- detect topology collapse  

### Inputs
```
triadic.topology.connectivity
triadic.topology.cut_points
triadic.topology.boundaries
triadic.topology.ancestry
triadic.topology.collapse
```

### Outputs
```
{
  "connectivity": { ... },
  "cut_points": [ ... ],
  "boundaries": [ ... ],
  "ancestry": { ... },
  "collapse": [ ... ]
}
```

### API Surface
```
analyzeTopology(topologyState)
```

---

# 6. ContinuityDiagnostics  
*(Analyzes long‑arc identity)*

### Responsibilities
- evaluate territorial/influence/moyo arcs  
- detect continuity anchors  
- compute continuity drift  
- detect identity inversion risk  

### Inputs
```
triadic.continuity.territorial_arcs
triadic.continuity.influence_arcs
triadic.continuity.moyo_arcs
triadic.continuity.ancestry_arcs
triadic.continuity.anchors
triadic.continuity.drift
triadic.continuity.identity_inversion_risk
```

### Outputs
```
{
  "arcs": { ... },
  "anchors": [ ... ],
  "drift": { ... },
  "identity_inversion": "low|medium|high"
}
```

### API Surface
```
analyzeContinuity(continuityState)
```

---

# 7. RiskDiagnostics  
*(Analyzes paradox, collapse, projection‑loss)*

### Responsibilities
- detect paradox events  
- detect collapse events  
- detect projection‑loss events  
- compute risk severity  

### Inputs
```
triadic.risk.paradox
triadic.risk.collapse
triadic.risk.projection_loss
```

### Outputs
```
{
  "paradox": [ ... ],
  "collapse": [ ... ],
  "projection_loss": [ ... ],
  "severity": "low|medium|high"
}
```

### API Surface
```
analyzeRisk(riskState)
```

---

# 8. MoveDiagnostics  
*(Aggregates diagnostics for a single move)*

### Responsibilities
- combine regime/resonance/topology/continuity/risk diagnostics  
- compute triadic score  
- produce structured commentary  

### Inputs
```
moves[index].triadic
triadic.scores
```

### Outputs
```
{
  "regime": { ... },
  "resonance": { ... },
  "topology": { ... },
  "continuity": { ... },
  "risk": { ... },
  "scores": { ... },
  "commentary": "..."
}
```

### API Surface
```
diagnoseMove(moveState)
```

---

# 9. DeltaDiagnostics  
*(Analyzes triadic evolution between moves)*

### Responsibilities
- compute deltas for all triadic fields  
- detect collapse/paradox/inversion events  
- produce delta commentary  

### Inputs
```
prevState
nextState
```

### Outputs
```
{
  "delta": { ... },
  "collapse": [ ... ],
  "paradox": [ ... ],
  "identity_inversion": [ ... ],
  "commentary": "..."
}
```

### API Surface
```
diagnoseDelta(prevState, nextState)
```

---

# 10. Integration Points

### **Viewer → Diagnostics**
- hover events  
- click events  
- timeline events  

### **HUD → Diagnostics**
- commentary panel updates  
- panel‑specific diagnostic requests  

### **Timeline → Diagnostics**
- delta computation  
- collapse/paradox detection  

### **State Contract → Diagnostics**
Consumes:

- regime  
- resonance  
- topology  
- continuity  
- risk  
- triadic scores  

---

# 11. Summary

The Diagnostics Component is RTT‑Go’s **triadic analysis engine**.

It computes:

- regime identity  
- resonance tension  
- topology stability  
- continuity arcs  
- paradox/collapse  
- identity inversion  
- triadic scores  
- move deltas  

and provides structured triadic insight for:

- viewer  
- HUD  
- overlays  
- timeline  

Diagnostics do not play Go — they **explain** Go’s triadic meaning.
