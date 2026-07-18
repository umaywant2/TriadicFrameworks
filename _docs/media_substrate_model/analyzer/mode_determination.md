# 🎛 Mode Determination

Mode determination identifies **how** a media ecosystem is behaving inside its current basin. While basins describe *where* the system sits in the substrate topology, modes describe the **behavioral state** of the system—its stability, tension, drift, volatility, collapse, or reconstruction.

Modes are driven by invariant strain, drift magnitude, cadence pressure, and attention volatility. They reveal whether the system is absorbing pressure, destabilizing, cascading, or rebuilding.

---

## 🧩 The Six MSM Modes

The MSM defines six behavioral modes:

- **Stable** — low strain, coherent narratives, balanced attention  
- **Tension** — early strain, rising volatility, pre‑drift conditions  
- **Drift** — directional movement across the substrate, weakening invariants  
- **Cascade** — runaway amplification, narrative churn, overloaded distribution  
- **Collapse** — structural failure, narrative breakdown, attention crash  
- **Reconstruction** — deliberate rebuilding of coherence and signal integrity  

Modes are not tied to specific basins; any basin can exhibit any mode depending on structural pressure.

---

## 🧭 Inputs to Mode Determination

The Analyzer determines mode using four primary signals:

- **Invariant strain** — how close the system is to breaking physics constraints  
- **Drift magnitude** — how quickly the system is moving across the substrate  
- **Attention volatility** — spikes, churn, or burnout  
- **Cadence pressure** — acceleration or compression of temporal rhythms  

These signals combine to reveal the system’s behavioral state.

---

## 📐 Mode Logic

### **Stable**
The system is structurally aligned:
- Low invariant strain  
- Low drift  
- Moderate or low attention volatility  
- Cadence within carrying capacity  

Stable systems absorb pressure without destabilizing.

---

### **Tension**
Early signs of instability:
- One or more invariants showing moderate strain  
- Attention volatility rising  
- Cadence beginning to accelerate  
- Drift detectable but small  

Tension is the precursor to drift.

---

### **Drift**
Directional movement across the substrate:
- Invariant strain increasing  
- Drift magnitude above threshold  
- Narrative or distribution wobble  
- Attention patterns becoming irregular  

Drift indicates the system is leaving its current attractor.

---

### **Cascade**
Runaway amplification and overload:
- High attention volatility  
- High cadence pressure  
- Distribution–Attention Fit breaking  
- Narrative coherence collapsing  
- Drift accelerating  

Cascade is a high‑energy, unstable mode.

---

### **Collapse**
Structural failure:
- Multiple invariants broken  
- Narrative coherence near zero  
- Attention crashes after overload  
- Cadence destabilized  
- Drift magnitude unpredictable  

Collapse often precedes stagnation or reconstruction.

---

### **Reconstruction**
Deliberate stabilization:
- Signal integrity rising  
- Narrative coherence improving  
- Cadence slowing  
- Attention stabilizing  
- Drift decreasing  

Reconstruction is the only mode that moves the system *toward* stability.

---

## 🧬 Mode Thresholds

Mode thresholds are determined by combinations of:

- Invariant strain levels  
- Drift magnitude categories  
- Attention volatility patterns  
- Cadence acceleration or compression  

Examples:

- Moderate strain + low drift → **Tension**  
- High strain + directional drift → **Drift**  
- High A volatility + high T + broken invariants → **Cascade**  
- Low A + low T + low N → **Collapse**  
- Rising S + rising N + slowing T → **Reconstruction**  

Modes are not binary; they reflect structural patterns.

---

## 📦 Output: MediaModeState

The Analyzer returns:

```
{
  mode: string,
  driftMagnitude: number,
  dominantInvariant: keyof MediaInvariantState
}
```

- **mode** — the behavioral state  
- **driftMagnitude** — how fast the system is moving  
- **dominantInvariant** — the invariant contributing most to strain  

This output feeds directly into transition detection and longitudinal analysis.
