# Blueprint Node Naming Conventions  
**RTT / Integrations / UE6**

This document defines the canonical naming conventions for all RTT Blueprint nodes inside Unreal Engine 6.  
Names follow the RTT operator grammar (φ–V–R, 3C, entropy, hybrid) and UE6’s Blueprint style rules.

All names are **minimal**, **operator‑first**, **mechanically queryable**, and **stable across versions**.

---

## 1. Naming Rules (Canonical)

1. **Prefix all RTT nodes with `RTT_`**  
   Ensures mechanical discoverability in the Blueprint palette.

2. **Use PascalCase after the prefix**  
   Example: `RTT_PhiField`, not `RTT_phifield`.

3. **Operator‑first naming**  
   Node names begin with the operator or invariant they expose.

4. **No abbreviations except φ–V–R**  
   - φ → Phi  
   - V → Variance  
   - R → Resonance  

5. **No suffixes like “Node”, “BP”, “Func”**  
   RTT nodes are primitives, not helpers.

6. **One operator per node**  
   Multi‑operator nodes are hybrid nodes and must use the `Hybrid` prefix.

---

## 2. Core Operator Nodes (φ–V–R)

| RTT Operator | Blueprint Node Name | Purpose |
|--------------|---------------------|---------|
| **φ** | `RTT_PhiField` | emergence field sampling |
| **V** | `RTT_VarianceStabilizer` | variance smoothing / temporal stabilization |
| **R** | `RTT_ResonanceProbe` | resonance envelope extraction |

---

## 3. Invariant Nodes (3C)

| Invariant | Blueprint Node Name | Purpose |
|----------|----------------------|---------|
| **Coherence** | `RTT_CoherenceCheck` | coherence rise detection |
| **Consistency** | `RTT_ConsistencyCheck` | geometry + lighting consistency |
| **Continuity** | `RTT_ContinuityCheck` | harmonic continuity detection |

---

## 4. Entropy Nodes

| Entropy Concept | Blueprint Node Name | Purpose |
|-----------------|----------------------|---------|
| Entropy Flow | `RTT_EntropyTrace` | entropy gradient tracing |
| Entropy Collapse | `RTT_EntropyCollapseCheck` | collapse signature detection |
| Entropy Boundary | `RTT_EntropyBoundary` | world‑partition boundary mapping |

---

## 5. Hybrid / Multi‑Regime Nodes

Hybrid nodes combine classical + spectral + temporal behavior.

| Hybrid Concept | Blueprint Node Name | Purpose |
|----------------|----------------------|---------|
| Hybrid Operator | `RTT_HybridOperator` | multi‑regime operator evaluation |
| Hybrid State | `RTT_HybridStateProbe` | hybrid state extraction |
| Hybrid Ladder | `RTT_HybridLadder` | quantum‑classical ladder evaluation |

---

## 6. Utility Nodes

| Utility | Blueprint Node Name | Purpose |
|---------|----------------------|---------|
| Debug Resonance | `RTT_DebugResonance` | visualize resonance envelopes |
| Debug Entropy | `RTT_DebugEntropy` | visualize entropy fields |
| Operator Timeline | `RTT_OperatorTimeline` | operator‑timeline debugging |

---

## 7. Naming Anti‑Patterns (Do Not Use)

❌ `RTT_phi_field`  
❌ `RTT-Resonance-Probe`  
❌ `ResonanceProbeRTT`  
❌ `RTT_OperatorNode`  
❌ `RTT_ResonanceProbe_v2`  
❌ `RTT_Entropy` (too vague)  

---

## 8. Summary

All RTT Blueprint nodes in UE6 must follow:

```
RTT_<Operator><Descriptor>
```

Examples:

```
RTT_PhiField
RTT_VarianceStabilizer
RTT_ResonanceProbe
RTT_EntropyTrace
RTT_HybridOperator
```

These conventions ensure:

- cross‑module consistency  
- AI‑parsability  
- zero drift  
- predictable operator discovery  
- stable integration with Benchmarks + TEL  

---

## Status

Active, stable, and aligned with the 2026 RTT Integrations standard.
