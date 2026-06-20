# RTT Agentic Module: Dominant Zeros of Nekrasov–Okounkov Polynomials

- [`nekr-okounkov-dominant-zeros_module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/Research/agentic/nekr-okounkov-dominant-zeros_module.json) — Agentic module schema role assignments

**Module ID:** `nekr_okounkov_dominant_zeros_rtt`  
**Source paper:** https://arxiv.org/pdf/2606.15394

This module wraps the paper *“Dominant Zeros of Nekrasov–Okounkov Polynomials”* in RTT operator grammar.  
It preserves the authors’ mathematics while exposing the structural regimes that govern the dominant-zero phenomenon, the bulk-zero cloud, and the asymptotic machinery behind them.

---

## 1. Purpose

- Make the paper **agentic** and machine‑navigable.  
- Clarify the **regime structure** behind dominant and bulk zeros.  
- Provide students with a clean conceptual map.  
- Support AI agents in reasoning over the paper without drift.

---

## 2. Core RTT view of the paper

Nekrasov–Okounkov polynomials \( P_n(x) \) arise from weighted sums over partitions.  
The authors show:

- For large \( n \), there is a **unique dominant zero** on the negative real axis.  
- All other zeros form a **bulk cloud** with predictable scaling.  
- The asymptotics are governed by a **saddle point** of the analytic continuation of the generating function.

The proof moves between partition combinatorics, analytic continuation, and steepest‑descent asymptotics.  
This module makes those transitions explicit.

---

## 3. RTT structures in this module

### Regimes
- `partition_expansion_regime`  
- `analytic_continuation_regime`  
- `saddle_point_regime`  
- `dominant_zero_regime`  
- `bulk_zero_regime`

### Tensions
- `combinatorial_vs_analytic`  
- `dominant_vs_bulk_zeros`  
- `local_saddle_vs_global_distribution`

### Transitions
- `partition_to_analytic_transition`  
- `analytic_to_saddle_transition`  
- `saddle_to_zero_localization_transition`

---

## 4. Operators

- **`partition_weight_operator`** — builds the polynomials from partitions.  
- **`analytic_continuation_operator`** — extends to complex x.  
- **`saddle_point_operator`** — performs steepest‑descent.  
- **`zero_localization_operator`** — identifies dominant and bulk zeros.

---

## 5. How to use this module

- **Students:**  
  Use this README alongside the PDF to understand how partition combinatorics produce analytic objects with rich zero structure.

- **Researchers:**  
  Query the module’s regimes and operators to explore structural dependencies.

- **Agents:**  
  Treat `module.json` as the canonical structural map of the paper.

---

## 6. Provenance

- **Module authoring:** TriadicFrameworks (RTT / agentic mapping).  
- **Original content:** Authors of arXiv:2606.15394.  
- **License:** Open educational use permitted.

---

# ✅ `diagram.txt`

```text
     +--------------------------------------------------------------+
     | nekr_okounkov_dominant_zeros_rtt                             |
     +--------------------------------------------------------------+

REGIMES
  [R1] partition_expansion_regime
  [R2] analytic_continuation_regime
  [R3] saddle_point_regime
  [R4] dominant_zero_regime
  [R5] bulk_zero_regime

TENSIONS
  [T1] combinatorial_vs_analytic
  [T2] dominant_vs_bulk_zeros
  [T3] local_saddle_vs_global_distribution

TRANSITIONS
  [X1] partition_to_analytic_transition
  [X2] analytic_to_saddle_transition
  [X3] saddle_to_zero_localization_transition

FLOW
  partition_expansion_regime (R1)
        |
        v
  analytic_continuation_regime (R2)
        |
        v
  saddle_point_regime (R3)
        |
        v
  dominant_zero_regime (R4)
        |
        v
  bulk_zero_regime (R5)
```
