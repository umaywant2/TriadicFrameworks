# 🧬 Invariant Evaluation

Invariant evaluation is the MSM Analyzer’s first structural test. Invariants measure how well a media ecosystem maintains coherence across the five axes of media physics—signal integrity, distribution topology, attention dynamics, narrative coherence, and temporal cadence. When invariants strain or break, the system begins drifting toward new basins or destabilizing into cascade or collapse.

Each invariant returns a value between **0.0 (aligned)** and **1.0 (broken)**. These values form the *MediaInvariantState*, which drives basin classification, mode determination, drift detection, and transition analysis.

---

## 🛰 Signal–Narrative Coherence

This invariant measures whether the system’s **signal integrity (S)** is strong enough to support its **narrative coherence (N)**. Misalignment between these axes produces structural instability.

- High S + high N indicates aligned, stable narratives.
- Low S + high N suggests narratives outrunning fidelity.
- High S + low N indicates fragmentation or conflict.
- Low S + low N signals collapse conditions.

Strain increases when narratives become more complex or volatile than the underlying signal can sustain.

---

## 🌐 Distribution–Attention Fit

This invariant evaluates whether the **distribution topology (D)** can carry the system’s **attention dynamics (A)** without overload.

- High D + high A supports stable amplification.
- Low D + high A creates cascade risk.
- High D + low A indicates underutilized networks.
- Low D + low A reflects stagnation.

Strain rises when attention spikes exceed the carrying capacity of the distribution structure.

---

## ⏱ Temporal–Signal Stability

This invariant measures whether **temporal cadence (T)** is moving faster than **signal integrity (S)** can support.

- Low T + high S supports long‑form coherence.
- High T + high S is accelerated but stable.
- High T + low S produces churn and distortion.
- Low T + low S reflects stagnation or decay.

Strain increases when cadence accelerates beyond the system’s ability to maintain fidelity.

---

## ⚡ Attention–Narrative Feedback

This invariant captures whether **attention dynamics (A)** reinforce or destabilize **narrative coherence (N)**.

- Moderate A + high N reinforces stability.
- High A + high N creates pressure but remains coherent.
- High A + low N produces narrative churn and collapse.
- Low A + low N reflects stagnation.

Strain increases when attention volatility destabilizes weak or conflicting narratives.

---

## 🧩 Interpreting Invariant Patterns

Individual invariants matter, but patterns matter more. The Analyzer looks for combinations such as:

- High Distribution–Attention strain + high Attention–Narrative strain → cascade conditions.
- High Signal–Narrative strain + high Temporal–Signal strain → epistemic decay.
- Low strain across all invariants → stable or reconstructing systems.
- Mixed strain patterns → drift or tension modes.

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

This state feeds directly into:

- Basin classification  
- Mode determination  
- Drift detection  
- Transition analysis  

Invariant strain is the backbone of the MSM Analyzer’s interpretation of media ecosystems.
