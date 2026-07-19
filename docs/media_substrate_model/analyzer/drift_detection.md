# 🧭 Drift Detection

Drift detection measures **directional movement** across the Media Substrate. While invariants describe internal strain and basins describe structural location, drift reveals **how fast and in what direction the system is moving**. Drift is one of the strongest predictors of transitions, instability, and regime shifts within media ecosystems.

Drift is not sentiment, engagement, or narrative change alone. It is a **vector‑level displacement** across the five axes of media physics:

```
[S, D, A, N, T]
```

---

## 📐 What Drift Measures

Drift captures changes in:

- **Signal Integrity (S)** — rising or falling fidelity  
- **Distribution Topology (D)** — centralization, fragmentation, or re‑networking  
- **Attention Dynamics (A)** — volatility, spikes, burnout  
- **Narrative Coherence (N)** — alignment, conflict, collapse  
- **Temporal Cadence (T)** — acceleration, compression, slowdown  

A system with high drift is structurally unstable, even if its current basin appears stable.

---

## 🔢 Computing Drift

Drift is computed as the difference between two MediaVectors:

```
Δ = currentVector – previousVector
```

Magnitude is calculated using Euclidean distance:

```
magnitude = sqrt(ΔS² + ΔD² + ΔA² + ΔN² + ΔT²)
```

This magnitude determines the drift category.

---

## 🧬 Drift Categories

The MSM Analyzer classifies drift into four categories:

### **Micro Drift**
Small, routine adjustments.
- Low invariant strain  
- No basin pressure  
- Normal narrative or attention fluctuation  

### **Meso Drift**
Meaningful directional movement.
- One or more invariants rising  
- Early basin tension  
- Narrative wobble or attention irregularity  

### **Macro Drift**
Large structural movement.
- Multiple invariants strained  
- Basin boundaries approaching  
- Distribution or narrative instability  

### **Regime Shift**
System‑level reconfiguration.
- Invariants breaking  
- Basin transition imminent or underway  
- Cascade, collapse, or reconstruction conditions  

Regime shifts are rare but high‑impact.

---

## 🧩 Drift Signatures

Different axes produce different drift signatures:

- **High ΔA + High ΔT** → cascade or burnout  
- **High ΔN + Low ΔS** → narrative collapse  
- **High ΔD + High ΔN** → fragmentation  
- **High ΔS + High ΔN** → reconstruction  
- **High ΔT + Low ΔS** → epistemic decay  

These signatures help interpret *why* drift is occurring.

---

## 🌀 Drift and Basins

Drift determines whether the system is:

- **Settling deeper** into its current basin  
- **Moving toward** a neighboring basin  
- **Escaping** its attractor entirely  
- **Crossing** into cascade or collapse  
- **Climbing** into reconstruction  

Basin classification tells you *where* the system is.  
Drift tells you *where it’s going*.

---

## 🎛 Drift and Modes

Modes are strongly influenced by drift magnitude:

- **Stable** → micro drift  
- **Tension** → micro or meso drift  
- **Drift** → meso or macro drift  
- **Cascade** → macro drift  
- **Collapse** → macro or regime shift  
- **Reconstruction** → meso drift with rising S and N  

Drift is the primary driver of mode transitions.

---

## 🔄 Drift and Transitions

Transitions occur when drift crosses structural thresholds:

- Basin → Basin  
- Mode → Mode  
- Stable → Tension → Drift → Cascade → Collapse → Reconstruction  

The Analyzer uses drift magnitude and direction to determine:

- **Trigger type**  
- **Severity**  
- **Trajectory**  
- **Expected next basin or mode**  

Drift is the earliest and most reliable indicator of systemic change.

---

## 📦 Output: MediaDrift

The Analyzer returns:

```
{
  delta: MediaVector,
  magnitude: number,
  category: "micro" | "meso" | "macro" | "regime_shift"
}
```

This output feeds directly into transition detection and longitudinal analysis.
