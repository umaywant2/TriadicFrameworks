# RTT Agentic Module: Almost All Primes Are Partially Regular

- [`partial-regular-primes_module.json`](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/refs/heads/main/docs/Research/agentic/partial-regular-primes_module.json) — Agentic module schema role assignments

**Module ID:** `partial_regular_primes_rtt`  
**Source paper:** https://arxiv.org/pdf/2602.05090

This module wraps the paper *“Almost all primes are partially regular”* in RTT operator grammar.  
It preserves the authors’ results while exposing the structural regimes that govern irregularity, partial regularity, and density-one phenomena.

---

## 1. Purpose

- Make the paper **agentic** and machine-navigable.  
- Clarify the **regime structure** behind partial regularity of primes.  
- Provide students with a clean conceptual map.  
- Support AI agents in reasoning over the paper without drift.

---

## 2. Core RTT view of the paper

The paper proves that **almost all primes are partially regular**, meaning:

- A prime may be irregular at some Bernoulli indices,  
- but for a positive proportion of admissible indices, it behaves regularly,  
- and the set of such primes has **density 1**.

This involves three interacting structures:

- **Bernoulli irregularity regime:**  
  Irregularity is defined by divisibility of Bernoulli numerators.

- **Partial regularity regime:**  
  A relaxed notion of regularity that allows some irregular pairs.

- **Analytic density regime:**  
  Density-one results require analytic number theory tools.

The proof moves between these regimes, often implicitly.  
This module makes those transitions explicit.

---

## 3. RTT structures in this module

### Regimes
- `bernoulli_irregularity_regime`  
- `partial_regularity_regime`  
- `analytic_density_regime`

### Tensions
- `local_vs_global_irregularity`  
- `combinatorial_vs_analytic`  
- `rare_irregularity_vs_density_one`

### Transitions
- `irregular_to_partial_transition`  
- `local_condition_to_density_transition`  
- `exception_control_transition`

---

## 4. Operators

- **`irregularity_operator`** — detects irregular pairs (p, k).  
- **`partial_regularity_operator`** — measures proportion of regular indices.  
- **`density_operator`** — evaluates analytic density of prime subsets.

---

## 5. How to use this module

- **Students:**  
  Use this README alongside the PDF to understand how irregularity and density interact.

- **Researchers:**  
  Query the module’s regimes and operators to explore structural dependencies.

- **Agents:**  
  Treat `module.json` as the canonical structural map of the paper.

---

## 6. Provenance

- **Module authoring:** TriadicFrameworks (RTT / agentic mapping).  
- **Original content:** Authors of arXiv:2602.05090.  
- **License:** Open educational use permitted.

---

# ✅ **diagram.txt**  
*(ASCII regime–tension–transition map)*

```text
        +---------------------------------------------+
        | partial_regular_primes_rtt                  |
        +---------------------------------------------+

REGIMES
  [R1] bernoulli_irregularity_regime
  [R2] partial_regularity_regime
  [R3] analytic_density_regime

TENSIONS
  [T1] local_vs_global_irregularity     (R1 <--> R2)
  [T2] combinatorial_vs_analytic        (R1 <--> R3)
  [T3] rare_irregularity_vs_density_one (R2 <--> R3)

TRANSITIONS
  [X1] irregular_to_partial_transition      (R1 -> R2)
  [X2] local_condition_to_density_transition (R1/R2 -> R3)
  [X3] exception_control_transition         (R3)

FLOW
  bernoulli_irregularity_regime (R1)
        |
        v
  partial_regularity_regime (R2)
        |
        v
  analytic_density_regime (R3)
```
