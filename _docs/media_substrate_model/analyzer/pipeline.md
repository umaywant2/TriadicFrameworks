# 📡 MSM Analyzer Pipeline

The MSM Analyzer processes media ecosystem states through a structured evaluation pipeline. Each stage transforms raw adapter output into increasingly meaningful substrate interpretations: invariants, basins, modes, drift, and transitions. The pipeline is deterministic, substrate‑agnostic, and fully aligned with the MSM’s conceptual architecture.

The Analyzer does not interpret content. It evaluates **structure**, **energy**, and **coherence** across the five MSM axes.

---

## 🧱 1. Input → MediaVector

The pipeline begins with an adapter converting raw external signals into a normalized **MediaVector**:

```
[S, D, A, N, T]
```

- **S — Signal Integrity**  
- **D — Distribution Topology**  
- **A — Attention Dynamics**  
- **N — Narrative Coherence**  
- **T — Temporal Cadence**

The Analyzer expects all values in the range **0.0–1.0**.  
If the adapter provides additional metadata (e.g., volatility hints, narrative conflict markers), the Analyzer may use it to refine later stages.

---

## 🧬 2. Invariant Evaluation

The Analyzer computes strain across the MSM’s four invariants:

- **Signal–Narrative Coherence**  
- **Distribution–Attention Fit**  
- **Temporal–Signal Stability**  
- **Attention–Narrative Feedback**

Each invariant returns a strain value:

```
0.0 = aligned
1.0 = broken
```

Invariant strain is the backbone of the pipeline.  
It determines whether the system is stable, drifting, or approaching cascade conditions.

---

## 🌀 3. Basin Classification

The Analyzer compares the vector to the six MSM basins:

- Broadcast  
- Network  
- Fragment  
- Cascade  
- Stagnation  
- Reconstruction  

Classification uses:

- Distance to canonical vectors  
- Gate conditions  
- Invariant strain patterns  

If no basin’s gates are satisfied, the system is classified as **Unstable / Transitional**.

Basins describe **where** the system is located in the media substrate topology.

---

## 🎛 4. Mode Determination

Modes describe **how** the system behaves inside its basin:

- Stable  
- Tension  
- Drift  
- Cascade  
- Collapse  
- Reconstruction  

Mode determination uses:

- Invariant strain  
- Drift magnitude  
- Cadence pressure  
- Attention volatility  
- Narrative stability  

Modes reveal whether the system is absorbing pressure, destabilizing, collapsing, or rebuilding.

---

## 🧭 5. Drift Detection

Drift measures directional movement across the substrate:

- Δ vector  
- Drift magnitude  
- Drift category:
  - micro  
  - meso  
  - macro  
  - regime_shift  

Drift is the primary indicator of basin transitions and early warning signals of instability.

---

## 🔄 6. Transition Detection

Transitions occur when the system crosses basin or mode boundaries.  
The Analyzer identifies:

- **from** → **to**  
- **trigger type**  
- **severity**  

Trigger types include:

- invariant_break  
- attention_spike  
- cadence_acceleration  
- signal_collapse  
- narrative_collapse  
- reconstruction  

Transitions describe **why** the system moved and **how severe** the shift was.

---

## 🧩 7. Output Assembly

The Analyzer returns a structured object containing:

- Normalized MediaVector  
- InvariantState  
- BasinResult  
- ModeState  
- Drift  
- Transition  

This output can be used for:

- Monitoring  
- Visualization  
- Simulation  
- Comparative analysis  
- Longitudinal tracking  

The pipeline ensures that every media ecosystem—regardless of platform, format, or scale—can be evaluated using the same structural grammar.
