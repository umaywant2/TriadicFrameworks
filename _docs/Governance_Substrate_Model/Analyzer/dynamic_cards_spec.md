# Dynamic Cards Specification  
*UI representation of Analyzer, Observer, and Simulator artifacts*

Dynamic cards present structural information in a compact, interpretable format. They translate vectors, basin classifications, drift signals, and coherence scores into visual components that can be used in dashboards, educational tools, and interactive governance explorers.

Cards are **data‑driven**, **schema‑consistent**, and **non‑ideological**. They reflect the GSM substrate and Analyzer pipeline without embedding policy preferences or normative judgments.

---

## Card Architecture

Each card is composed of five layers:

1. **Header Layer** — identity and context  
2. **Structural Layer** — vector and basin  
3. **Coherence Layer** — scores and invariant alignment  
4. **Dynamics Layer** — drift, forces, transitions  
5. **Narrative Layer** — human‑readable explanation  

Cards may be rendered in compact or expanded form depending on UI needs.

---

## 1. Header Layer

```
header:
  title: <string>
  subtitle: <string>
  icon: <optional>
  metadata:
    source: analyzer | observer | simulator | dsl_adapter
    timestamp: <string>
```

Used to identify the artifact and its origin.

---

## 2. Structural Layer

```
structural_section:
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

This layer anchors the card in the governance manifold.

---

## 3. Coherence Layer

```
coherence_section:
  coherence_score: <0–100>
  invariant_alignment:
    aligned: <int>
    tension: <int>
    violated: <int>
  awareness_strength:
    structural: <0–10>
    procedural: <0–10>
    historical: <0–10>
    anticipatory: <0–10>
    relational: <0–10>
```

This layer summarizes structural integrity.

---

## 4. Dynamics Layer

```
dynamics_section:
  drift:
    vector: [<dC>, <dM>, <dO>, <dA>, <dT>]
    magnitude: <number>
    category: micro | meso | macro | regime_shift
  forces:
    active:
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

This layer shows movement, tension, and transition pressure.

---

## 5. Narrative Layer

```
narrative_section:
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

This layer provides human‑readable interpretation.

---

## Card Types

### 1. **Structural Snapshot Card**
Used for profiles, DSL inputs, and static system descriptions.

Includes:
- header  
- structural section  
- coherence section  
- narrative summary  

### 2. **Drift Card**
Used for comparing two vectors or snapshots.

Includes:
- header  
- drift vector + magnitude  
- active forces  
- basin movement  
- drift narrative  

### 3. **Transition Card**
Used for simulator outputs.

Includes:
- header  
- transition pathway  
- cost breakdown  
- stability implications  

### 4. **Observer Lens Card**
Used for triadic observer outputs.

Includes:
- history vector  
- now vector  
- projected drift  
- lens‑specific narrative  

---

## Rendering Rules

- Cards must be **data‑first**, not decorative.  
- All numeric fields must be displayed with consistent precision.  
- Drift magnitude must be color‑coded by category.  
- Basin identity must use consistent iconography.  
- Narratives must be concise and structurally grounded.  
- Cards must degrade gracefully when fields are missing.  

---

## Integration Points

Dynamic cards are used by:

- Analyzer dashboards  
- Governance comparison tools  
- Educational modules  
- Transition Simulator UI  
- Observer timelines  
- DSL integration layers  

They provide a unified visual language for structural governance analysis.
