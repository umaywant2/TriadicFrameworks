# 🧪 MSM Analyzer — Worked Examples

These examples illustrate how the MSM Analyzer interprets media ecosystem states using the five‑axis MediaVector, invariant evaluation, basin classification, mode determination, drift detection, and transition analysis. Each example shows a full end‑to‑end evaluation, mirroring the Analyzer pipeline.

---

## 📘 Example 1 — Network System Entering Drift

### Input Vector
```
{
  S: 0.58,
  D: 0.72,
  A: 0.41,
  N: 0.63,
  T: 0.47
}
```

### Invariant Evaluation
- Signal–Narrative Coherence: **0.22**  
- Distribution–Attention Fit: **0.18**  
- Temporal–Signal Stability: **0.31**  
- Attention–Narrative Feedback: **0.27**

Moderate strain across multiple invariants indicates early instability.

### Basin Classification
- Closest basin: **Network**  
- Gate conditions: **Satisfied**  
- Distance: **0.19**

The system remains in the Network basin but is under pressure.

### Mode Determination
- Drift magnitude: **0.14** (meso drift)  
- Dominant invariant: **Temporal–Signal Stability**  
- Mode: **Tension**

The system is beginning to destabilize but has not yet entered full drift.

### Drift Detection
- Δ from previous vector: moderate  
- Category: **meso drift**

### Transition Detection
- Previous: Network / Stable  
- Current: Network / Tension  
- Trigger: **cadence acceleration**  
- Severity: **0.42**

The system is shifting toward Drift mode.

---

## 📙 Example 2 — Fragment System Collapsing into Cascade

### Input Vector
```
{
  S: 0.29,
  D: 0.34,
  A: 0.88,
  N: 0.21,
  T: 0.91
}
```

### Invariant Evaluation
- Signal–Narrative Coherence: **0.71**  
- Distribution–Attention Fit: **0.83**  
- Temporal–Signal Stability: **0.92**  
- Attention–Narrative Feedback: **0.79**

Multiple invariants are near or above collapse thresholds.

### Basin Classification
- Closest basin: **Cascade**  
- Gate conditions: **Satisfied**  
- Distance: **0.11**

The system has entered the Cascade attractor.

### Mode Determination
- Drift magnitude: **0.37** (macro drift)  
- Dominant invariant: **Temporal–Signal Stability**  
- Mode: **Cascade**

The system is in a high‑energy, unstable state.

### Drift Detection
- Δ from previous vector: large  
- Category: **macro drift**

### Transition Detection
- Previous: Fragment / Drift  
- Current: Cascade / Cascade  
- Trigger: **attention spike + cadence acceleration**  
- Severity: **0.87**

This is a high‑severity structural transition.

---

## 📗 Example 3 — Collapse Moving into Reconstruction

### Input Vector
```
{
  S: 0.44,
  D: 0.39,
  A: 0.27,
  N: 0.36,
  T: 0.33
}
```

### Invariant Evaluation
- Signal–Narrative Coherence: **0.41**  
- Distribution–Attention Fit: **0.19**  
- Temporal–Signal Stability: **0.22**  
- Attention–Narrative Feedback: **0.28**

Strain is decreasing across all invariants.

### Basin Classification
- Closest basin: **Reconstruction**  
- Gate conditions: **Satisfied**  
- Distance: **0.17**

The system is stabilizing and rebuilding.

### Mode Determination
- Drift magnitude: **0.09** (micro drift)  
- Dominant invariant: **Signal–Narrative Coherence**  
- Mode: **Reconstruction**

The system is recovering from collapse.

### Drift Detection
- Δ from previous vector: small  
- Category: **micro drift**

### Transition Detection
- Previous: Collapse / Collapse  
- Current: Reconstruction / Reconstruction  
- Trigger: **signal recovery + narrative stabilization**  
- Severity: **0.33**

A positive‑direction transition.

---

## 📕 Example 4 — Stagnation with Minimal Drift

### Input Vector
```
{
  S: 0.31,
  D: 0.28,
  A: 0.12,
  N: 0.29,
  T: 0.14
}
```

### Invariant Evaluation
- Signal–Narrative Coherence: **0.38**  
- Distribution–Attention Fit: **0.09**  
- Temporal–Signal Stability: **0.12**  
- Attention–Narrative Feedback: **0.17**

Low strain but also low energy.

### Basin Classification
- Closest basin: **Stagnation**  
- Gate conditions: **Satisfied**  
- Distance: **0.13**

### Mode Determination
- Drift magnitude: **0.03** (micro drift)  
- Mode: **Stable**

The system is quiet, low‑energy, and structurally inert.

### Drift Detection
- Category: **micro drift**

### Transition Detection
- No transition detected  
- Trigger: **none**  
- Severity: **0.00**

The system remains in Stagnation.

---

## 📓 Example 5 — Broadcast System Under Early Pressure

### Input Vector
```
{
  S: 0.82,
  D: 0.91,
  A: 0.22,
  N: 0.87,
  T: 0.29
}
```

### Invariant Evaluation
- Signal–Narrative Coherence: **0.08**  
- Distribution–Attention Fit: **0.11**  
- Temporal–Signal Stability: **0.14**  
- Attention–Narrative Feedback: **0.09**

Very low strain; system is stable.

### Basin Classification
- Closest basin: **Broadcast**  
- Gate conditions: **Satisfied**  
- Distance: **0.07**

### Mode Determination
- Drift magnitude: **0.05**  
- Mode: **Stable**

### Drift Detection
- Category: **micro drift**

### Transition Detection
- No transition  
- System remains stable

---

These examples give us a complete set of reference patterns for how the MSM Analyzer behaves across different structural conditions. 
