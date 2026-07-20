# Structural Vectors Reference  
*A canonical guide to structural vectors in the Governance Substrate Model (GSM)*

Structural vectors are the foundational representation of governance systems within the GSM. Every Analyzer component—drift, physics, invariants, basins, regime modes, projections, and simulations—operates on these vectors. This reference defines their structure, meaning, normalization, and usage.

---

## The five‑axis manifold

All structural vectors live in a five‑dimensional space:

- **C — Centralization**  
  Degree of concentrated authority and decision power.

- **M — Methods**  
  Competitive, procedural, or collaborative mechanisms used to act.

- **O — Oversight**  
  Monitoring, review, transparency, and constraint structures.

- **A — Access**  
  Who can participate, contribute, or influence.

- **T — Timing**  
  Cadence, responsiveness, and temporal structure.

Each axis ranges from **0.0 to 1.0** after normalization.

---

## Vector format

A structural vector is always represented as:

```
[C, M, O, A, T]
```

Example:

```
[0.62, 0.48, 0.71, 0.33, 0.55]
```

---

## Vector metadata

Every vector includes metadata used by the Analyzer:

- **confidence** — how reliable the vector is  
- **source** — DSL, mapping rules, historical record, simulation step, etc.  
- **notes** — optional contextual information  

Example:

```yaml
vector:
  C: 0.62
  M: 0.48
  O: 0.71
  A: 0.33
  T: 0.55
metadata:
  confidence: 0.92
  source: "statement_mapping"
  notes: "Derived from policy declaration"
```

---

## How vectors are generated

Vectors may originate from:

- **statement mapping rules**  
- **DSL substrate adapter**  
- **historical profile encoding**  
- **simulation engine steps**  
- **projection rules**  
- **manual analyst input**

All sources must pass through the same normalization pipeline.

---

## Normalization rules

Normalization ensures vectors remain within manifold bounds:

- clamp each axis to **[0.0, 1.0]**  
- apply min‑max scaling when raw values exceed expected ranges  
- apply coupling adjustments when physics rules require balance  
- preserve relative deltas for drift computation  

Normalization is mandatory before any Analyzer component consumes a vector.

---

## Vector deltas

Vector deltas represent structural movement:

```
Δ = [dC, dM, dO, dA, dT]
```

They are used by:

- drift engine  
- physics engine  
- regime‑shift detection  
- simulation engine  
- observer history/now/future lenses  

Magnitude is computed as:

\[
\text{magnitude} = \sqrt{dC^2 + dM^2 + dO^2 + dA^2 + dT^2}
\]

---

## Vector interpretation lenses

Vectors are interpreted through multiple lenses:

- **Axis lens** — isolates each axis  
- **Coupling lens** — evaluates C↔O, M↔A, O↔T  
- **Invariant lens** — checks alignment, tension, violation  
- **Basin lens** — identifies nearest basin and distance  
- **Drift lens** — interprets movement and category  
- **Narrative lens** — produces human‑readable summaries  

These lenses do not modify vectors—they interpret them.

---

## Vector usage across the Analyzer

Structural vectors feed into:

- **Invariant checker** — determines strain and violations  
- **Physics engine** — computes forces and compensatory movement  
- **Drift detector** — classifies micro/meso/macro/regime‑shift drift  
- **Basin classifier** — determines basin identity and boundary proximity  
- **Regime modes** — identifies operational mode  
- **Phase discipline** — determines phase state  
- **Projection rules** — generates plausible futures  
- **Simulation engine** — evolves vectors stepwise  
- **Observer layer** — encodes history, now, and future states  

Vectors are the universal substrate for all structural analysis.

---

## Canonical examples

### Stable system example

```
[0.45, 0.52, 0.47, 0.50, 0.48]
```

- low deltas  
- high coherence  
- stable regime mode  
- deep inside basin  

### Tension‑driven drift example

```
[0.82, 0.40, 0.33, 0.28, 0.71]
```

- C↔O imbalance  
- high timing volatility  
- drift category: meso  
- approaching basin boundary  

### Regime‑shift vector example

```
[0.91, 0.15, 0.22, 0.11, 0.88]
```

- multiple invariant violations  
- macro drift  
- absorptive failure  
- crossing into new basin  

---

## Purpose of this reference

This file provides:

- a canonical definition of structural vectors  
- a shared vocabulary for contributors  
- a stable anchor for all Analyzer components  
- a teaching‑friendly reference for students  
- a foundation for simulation, projection, and observer layers  

It ensures structural vectors remain coherent, interpretable, and substrate‑aligned across the entire GSM.
