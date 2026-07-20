# 🔄 Transition Detection

Transition detection identifies **when** and **why** a media ecosystem moves from one structural state to another. While basins describe where the system is located and modes describe how it behaves, transitions capture **the moment of change**—the crossing of thresholds that reshape the system’s trajectory.

Transitions are triggered by invariant breaks, drift acceleration, attention spikes, narrative collapse, cadence overload, or reconstruction forces. They are the Analyzer’s highest‑level signal of systemic change.

---

## 🧭 What Counts as a Transition

A transition occurs when the system crosses a boundary in either:

- **Basin** (e.g., Network → Fragment)  
- **Mode** (e.g., Tension → Drift)  
- **Both simultaneously** (e.g., Network/Drift → Cascade/Cascade)  

Transitions are not subtle fluctuations. They represent **structural reconfiguration**.

---

## 🧩 Inputs to Transition Detection

The Analyzer uses several signals to detect transitions:

- **Previous basin** vs **current basin**  
- **Previous mode** vs **current mode**  
- **Drift magnitude** and direction  
- **Invariant strain patterns**  
- **Attention volatility**  
- **Cadence acceleration or compression**  
- **Narrative stability or collapse**  

Transitions are detected only when these signals cross structural thresholds.

---

## ⚡ Transition Triggers

The MSM defines six primary trigger types:

### **Invariant Break**
One or more invariants exceed their strain threshold.  
Examples:
- Signal–Narrative Coherence breaks → narrative collapse  
- Distribution–Attention Fit breaks → cascade onset  

### **Attention Spike**
Sudden, extreme increase in A.  
Often leads to:
- Cascade  
- Narrative churn  
- Distribution overload  

### **Cadence Acceleration**
Temporal cadence increases faster than the system can stabilize.  
Common in:
- High‑velocity media cycles  
- Crisis events  
- Viral cascades  

### **Signal Collapse**
Sharp drop in S.  
Leads to:
- Narrative simplification  
- Epistemic decay  
- Collapse mode  

### **Narrative Collapse**
N drops rapidly due to conflict, fragmentation, or overload.  
Often paired with:
- High A volatility  
- High T  
- Drift acceleration  

### **Reconstruction**
Deliberate stabilization effort.  
Characterized by:
- Rising S  
- Rising N  
- Slowing T  
- Decreasing drift  

Reconstruction is the only positive‑direction trigger.

---

## 🌀 Basin Transitions

Basin transitions occur when the system’s structural fingerprint moves closer to a new attractor and satisfies its gate conditions.

Examples:

- **Network → Fragment**  
  Narrative divergence + distribution fragmentation  

- **Fragment → Cascade**  
  Attention spike + cadence acceleration  

- **Cascade → Collapse**  
  Overload + signal failure  

- **Collapse → Reconstruction**  
  Stabilization + rising coherence  

Basin transitions are the most visible form of systemic change.

---

## 🎛 Mode Transitions

Mode transitions reflect changes in **behavior**, not location.

Examples:

- **Stable → Tension**  
  Early invariant strain  

- **Tension → Drift**  
  Directional movement begins  

- **Drift → Cascade**  
  Volatility exceeds structural capacity  

- **Cascade → Collapse**  
  System overload  

- **Collapse → Reconstruction**  
  Stabilization begins  

Mode transitions often precede basin transitions.

---

## 🧬 Combined Transitions

Some transitions involve both basin and mode changes simultaneously.

Example:

```
Network / Drift  →  Cascade / Cascade
```

This indicates:
- A basin shift into the Cascade attractor  
- A behavioral shift into Cascade mode  
- A high‑severity structural event  

Combined transitions are rare but high‑impact.

---

## 📦 Output: MediaTransition

The Analyzer returns:

```
{
  from: string,
  to: string,
  trigger: string,
  severity: number
}
```

- **from** — previous basin/mode  
- **to** — current basin/mode  
- **trigger** — the dominant structural cause  
- **severity** — magnitude of the transition (0.0–1.0)  

Severity is influenced by drift magnitude, invariant breaks, and volatility.

---

## 🧠 Why Transitions Matter

Transitions reveal:

- When a system becomes unstable  
- When cascades are forming  
- When collapse is imminent  
- When reconstruction is underway  
- How media ecosystems evolve over time  

They are essential for monitoring, forecasting, and simulation.
