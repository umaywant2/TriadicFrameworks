# 🧬 Invariant Evaluation

Invariant evaluation is the Analyzer’s first structural test. Invariants measure how well the media ecosystem maintains coherence across its five axes—signal, distribution, attention, narrative, and cadence. When invariants strain or break, the system begins drifting toward new basins or destabilizing into cascade or collapse.

Each invariant returns a value in the range:

```
0.0 = aligned (no strain)
1.0 = broken (full strain)
```

These values form the **MediaInvariantState**, which drives basin classification, mode determination, drift detection, and transition analysis.

---

## 🛰 Signal–Narrative Coherence

This invariant measures whether the system’s **signal integrity (S)** is strong enough to support its **narrative coherence (N)**.

- High S + high N → aligned  
- Low S + high N → unstable (narratives outrun fidelity)  
- High S + low N → fragmented or conflicting narratives  
- Low S + low N → collapse conditions  

Strain increases when narratives become more complex or volatile than the underlying signal can support.

---

## 🌐 Distribution–Attention Fit

This invariant measures whether the **distribution topology (D)** can carry the system’s **attention dynamics (A)** without overload.

- High D + high A → stable amplification  
- Low D + high A → cascade risk  
- High D + low A → underutilized network  
- Low D + low A → stagnation  

Strain increases when attention spikes exceed the carrying capacity of the distribution structure.

---

## ⏱ Temporal–Signal Stability

This invariant measures whether **temporal cadence (T)** is moving faster than **signal integrity (S)** can sustain.

- Low T + high S → stable long‑form coherence  
- High T + high S → accelerated but stable  
- High T + low S → churn, distortion, collapse  
- Low T + low S → stagnation or decay  

Strain increases when cadence accelerates beyond the system’s ability to verify or maintain fidelity.

---

## ⚡ Attention–Narrative Feedback

This invariant measures whether **attention dynamics (A)** are destabilizing or reinforcing **narrative coherence (N)**.

- Moderate A + high N → stable reinforcement  
- High A + high N → pressure but coherent  
- High A + low N → narrative churn, conflict, collapse  
- Low A + low N → stagnation  

Strain increases when attention volatility destabilizes weak or conflicting narratives.

---

## 🧩 Interpreting Invariant Patterns

Individual invariants matter, but **patterns** matter more. The Analyzer looks for combinations such as:

- High Distribution–Attention strain + high Attention–Narrative strain → cascade conditions  
- High Signal–Narrative strain + high Temporal–Signal strain → epistemic decay  
- Low strain across all invariants → stable or reconstructing systems  
- Mixed strain patterns → drift or tension modes  

These patterns determine the system’s behavioral mode and its likelihood of transitioning between basins.

---

## 🧭 Output: MediaInvariantState

The Analyzer returns a structured object:

```
{
  signalNarrativeCoherence: number,
  distributionAttentionFit: number,
  temporalSignalStability: number,
  attentionNarrativeFeedback: number
}
```

This state is used by:

- Basin classification  
- Mode determination  
- Drift detection  
- Transition analysis  

Invariant strain is the backbone of the MSM Analyzer’s interpretation of media ecosystems.
