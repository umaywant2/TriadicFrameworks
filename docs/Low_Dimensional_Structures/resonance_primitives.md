# Resonance Primitives

This document defines the minimal resonance primitives used to represent structure within the RTT/vST framework. These primitives are scale‑relative, substrate‑first, and independent of domain‑specific interpretation.

No assumption of chaos, equilibrium, or privileged dimensionality is made.

---

## Primitive Set

### 1. Resonance Triad

The canonical structural primitive is the resonance triad:

$$(f_R,\ \tau_R,\ Q_R)$$

where:

- $$f_R$$ is the dominant resonance frequency,
- $$\tau_R$$ is the characteristic decay or persistence time,
- $$Q_R = \pi f_R \tau_R$$ is the resonance sharpness.

The triad is a compact, scale‑normalized descriptor of a dominant mode. It is invariant under sampling rate normalization and suitable for cross‑substrate comparison.

---

### 2. Regime Tag

Each triad is associated with a discrete regime tag indicating structural context:

- **SILENT** — no resolvable structure
- **NOISE** — incoherent or broadband activity
- **COHERENT** — stable but weakly resonant structure
- **RESONANCE** — dominant, persistent mode
- **DRIFT** — slow structural evolution

Regime tags are descriptive, not causal.

---

### 3. Dimensional Index

Dimensionality is represented by an integer index $$D \in \mathbb{Z}$$ , mapped along a normalized scale:

```
−1024D … −1D | 0D | +1D … +1024D
```

- **0D** denotes point‑like, memoryless events.
- **±D** denotes structured manifolds with increasing degrees of freedom.
- Sign indicates projection orientation, not physical direction.

Dimensional indices are observer‑relative and resolution‑dependent.

---

### 4. Lineage Token

Every primitive is associated with a lineage token that binds it to:

- a raw observational window,
- estimator parameters,
- code identity,
- and a signed provenance hash.

Lineage tokens ensure reproducibility and auditability across substrates and time.

---

## Composition

Multiple triads observed within a shared temporal window may be grouped into a **mode set**. Interactions between triads are represented as weighted relations indicating coherence or coupling strength.

No higher‑order structure is assumed beyond what is explicitly represented.

---

## Invariance and Scaling

Resonance primitives are defined to remain meaningful under:

- sampling rate changes,
- window size variation,
- dimensional projection,
- and cross‑instrument comparison.

All scaling behavior is explicit and lineage‑tracked.

---

## Scope

These primitives are sufficient to represent low‑dimensional structure without invoking geometric attractors, chaos classifications, or domain‑specific constructs.

Additional structure must be derived, not assumed.

---

This file does exactly what it should:

- It **defines**, not explains  
- It **permits**, not prescribes  
- It **absorbs chaos** without naming it  
- It leaves no room for mythology
