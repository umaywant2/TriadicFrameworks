# 🌀 Media Substrate Basins

Media ecosystems tend to settle into a small number of stable or semi‑stable attractor regions called **basins**. Each basin represents a characteristic configuration of the five substrate axes:

```
[S, D, A, N, T]
```

Basins define the topology of the media substrate. They determine how systems behave under tension, how drift accumulates, and how transitions occur.

The MSM defines **six basins**:

- Broadcast  
- Network  
- Fragment  
- Cascade  
- Stagnation  
- Reconstruction  

Each basin has a **canonical vector**, **gate conditions**, and **adjacent basins** that describe likely transition pathways.

---

## 📡 Broadcast Basin

### Canonical Vector
\[
[0.85,\ 0.80,\ 0.45,\ 0.85,\ 0.35]
\]

### Structural Profile
- High signal integrity  
- Centralized distribution  
- Pooled, steady attention  
- Strong narrative coherence  
- Slow to moderate cadence  

### Gate Conditions
- \(S > 0.70\)  
- \(N > 0.70\)  
- \(D > 0.60\)  
- \(T < 0.50\)

### Adjacent Basins
- **Network** (decentralization, pluralization)  
- **Stagnation** (attention decay, narrative exhaustion)

---

## 🌐 Network Basin

### Canonical Vector
\[
[0.75,\ 0.65,\ 0.60,\ 0.65,\ 0.55]
\]

### Structural Profile
- Distributed or federated topology  
- Plural but interoperable narratives  
- Rhythmic attention cycles  
- Moderate cadence  
- Good but not perfect signal integrity  

### Gate Conditions
- \(D > 0.50\)  
- \(N > 0.50\)  
- \(T\) between \(0.40\) and \(0.70\)

### Adjacent Basins
- **Broadcast** (recentralization)  
- **Fragment** (siloing, coherence loss)  
- **Cascade** (attention spikes + cadence acceleration)

---

## 🧩 Fragment Basin

### Canonical Vector
\[
[0.55,\ 0.30,\ 0.55,\ 0.30,\ 0.50]
\]

### Structural Profile
- Fragmented distribution  
- Siloed or incompatible narratives  
- Mixed signal integrity  
- Localized attention spikes  
- Mixed cadence  

### Gate Conditions
- \(D < 0.40\)  
- \(N < 0.45\)

### Adjacent Basins
- **Cascade** (attention surge + temporary reconnection)  
- **Stagnation** (attention decay)  
- **Network** (re‑connection and coherence rebuilding)

---

## ⚡ Cascade Basin

### Canonical Vector
\[
[0.40,\ 0.70,\ 0.90,\ 0.35,\ 0.85]
\]

### Structural Profile
- Overwhelmed signal  
- Highly connected distribution  
- Extreme attention volatility  
- Rapid narrative churn  
- Very fast cadence  

### Gate Conditions
- \(A > 0.75\)  
- \(T > 0.70\)

### Adjacent Basins
- **Fragment** (post‑cascade narrative collapse)  
- **Stagnation** (attention crash)  
- **Reconstruction** (intentional stabilization)

---

## 💤 Stagnation Basin

### Canonical Vector
\[
[0.45,\ 0.40,\ 0.20,\ 0.35,\ 0.25]
\]

### Structural Profile
- Low attention  
- Weak or repetitive narratives  
- Sparse or decayed distribution  
- Slow cadence  
- Mediocre signal integrity  

### Gate Conditions
- \(A < 0.30\)  
- \(T < 0.40\)  
- \(N < 0.45\)

### Adjacent Basins
- **Reconstruction** (signal + narrative investment)  
- **Network** (attention revival + distribution repair)

---

## 🛠 Reconstruction Basin

### Canonical Vector
\[
[0.70,\ 0.55,\ 0.40,\ 0.60,\ 0.40]
\]

### Structural Profile
- Rising signal integrity  
- Re‑architecting distribution  
- Guided, moderate attention  
- Re‑stitching narrative coherence  
- Intentionally moderated cadence  

### Gate Conditions
- \(S\) increasing  
- \(N\) increasing  
- \(T\) between \(0.30\) and \(0.50\)

### Adjacent Basins
- **Broadcast** (recentralization)  
- **Network** (resilient distributed reconstruction)  
- **Stagnation** (failed reconstruction)

---

## 🔍 Basin Classification Rules

### Step 1 — Nearest Canonical Vector
Compute Euclidean distance to each canonical vector:

\[
d = \sqrt{(S-S_b)^2 + (D-D_b)^2 + (A-A_b)^2 + (N-N_b)^2 + (T-T_b)^2}
\]

The nearest basin is the initial candidate.

### Step 2 — Gate Check
If the nearest basin’s gate conditions are satisfied → classify.

If not → choose the nearest basin whose gate is satisfied.

### Step 3 — Transitional State
If no basin gates are satisfied → classify as **Unstable / Transitional**.

---

## 🔄 Basin Transitions

### Common transitions
- **Broadcast → Network**  
  Decentralization, cadence increase, narrative pluralization.

- **Network → Fragment**  
  Siloing, coherence loss, distribution decay.

- **Fragment → Cascade**  
  Attention spike + temporary reconnection.

- **Cascade → Stagnation**  
  Attention crash, narrative exhaustion.

- **Cascade → Reconstruction**  
  Intentional slowing of cadence + signal repair.

- **Reconstruction → Broadcast or Network**  
  Depending on whether the system recentralizes or distributes.

---

## 🧱 Basin Summary

Each basin represents a stable or semi‑stable region of the media substrate:

- **Broadcast** — coherence anchored by high signal and centralization.  
- **Network** — plural but interoperable media ecosystems.  
- **Fragment** — siloed, incompatible realities.  
- **Cascade** — high‑energy, high‑speed reconfiguration.  
- **Stagnation** — low‑energy, decayed media environments.  
- **Reconstruction** — deliberate rebuilding after collapse.

These basins form the topology that the MSM Analyzer will classify, monitor, and simulate once the substrate base is complete.
