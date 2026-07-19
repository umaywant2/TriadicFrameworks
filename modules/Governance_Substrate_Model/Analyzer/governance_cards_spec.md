# Governance Cards Specification  
*A unified card framework for structural governance analysis*

Governance cards are the primary UI units for presenting Analyzer, Observer, and Simulator outputs. They provide a compact, interpretable, and substrate‑aligned representation of structural vectors, coherence scores, drift signals, basin identity, and transition pathways. Cards are designed for dashboards, educational tools, and comparative governance explorers.

---

### Card Purpose

Governance cards serve four core functions:

- present structural information in a consistent, non‑ideological format  
- support comparison across systems, eras, or scenarios  
- surface drift, tension, and transition signals  
- provide narrative context for learners and analysts  

Cards are data‑driven and follow strict schemas to ensure interoperability across GSM modules.

---

## Card Types

### Structural Card
Represents a system’s current structural configuration.

- structural vector  
- nearest basin  
- basin distance  
- stability score  
- invariant alignment summary  
- awareness layer strength  
- narrative snippet  

### Drift Card
Represents movement between two structural states.

- drift vector  
- drift magnitude  
- drift category  
- active physics forces  
- invariant tension  
- basin movement  
- drift narrative  

### Transition Card
Represents a pathway through the transition graph.

- start basin  
- end basin  
- intermediate steps  
- total transition cost  
- stability implications  

### Observer Lens Card
Represents history, now, and future perspectives.

- historical vectors  
- drift sequences  
- current coherence  
- projected drift  
- future transition signals  

---

## Card Schema

### Header

```
header:
  title: <string>
  subtitle: <string>
  icon: <optional>
  metadata:
    source: analyzer | observer | simulator | dsl_adapter
    timestamp: <string>
```

### Structural Section

```
structural:
  vector:
    C: <number>
    M: <number>
    O: <number>
    A: <number>
    T: <number>
  basin:
    nearest: <CPL | CPF | CTR | PCL | HCL>
    distance: <number>
    stability: <0–1>
```

### Coherence Section

```
coherence:
  score: <0–100>
  invariants:
    aligned: <int>
    tension: <int>
    violated: <int>
  awareness:
    structural: <0–10>
    procedural: <0–10>
    historical: <0–10>
    anticipatory: <0–10>
    relational: <0–10>
```

### Dynamics Section

```
dynamics:
  drift:
    vector: [<dC>, <dM>, <dO>, <dA>, <dT>]
    magnitude: <number>
    category: micro | meso | macro | regime_shift
  forces:
    - axis_pair: <C↔O | M↔A | O↔T>
      magnitude: <number>
      direction: positive | negative
  transitions:
    likelihood: <0–1>
    pathway:
      start: <basin>
      end: <basin>
      cost: <number>
```

### Narrative Section

```
narrative:
  summary: <string>
  key_events:
    - <string>
  structural_highlights:
    - <string>
  drift_explanation:
    - <string>
  basin_context:
    - <string>
```

---

## Rendering Guidelines

- Cards must be readable at a glance.  
- Drift magnitude should be color‑coded by category.  
- Basin identity should use consistent iconography.  
- Narratives must be concise and structurally grounded.  
- Missing fields must degrade gracefully.  
- All numeric values must use consistent precision.  

---

## Integration Points

Governance cards are used by:

- Governance Alignment Dashboard  
- Transition Simulator  
- Triadic Observer timelines  
- DSL substrate adapter outputs  
- Comparative governance explorers  
- Educational modules  

They provide a unified visual language across the GSM ecosystem.
