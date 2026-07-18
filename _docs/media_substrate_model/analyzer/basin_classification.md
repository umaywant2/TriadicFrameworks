# 🌀 Basin Classification

Basin classification identifies **where** a media ecosystem sits within the Media Substrate Model. Each basin represents a structural attractor shaped by the interaction of signal integrity, distribution topology, attention dynamics, narrative coherence, and temporal cadence. The Analyzer determines basin membership by comparing the current MediaVector to canonical basin vectors and applying gate conditions that ensure structural fit.

Basins are not content categories. They are **behavioral regimes** that describe how media systems organize, stabilize, fragment, or cascade.

---

## 📚 The Six MSM Basins

The MSM defines six canonical basins:

- **Broadcast** — centralized distribution, high coherence, low volatility  
- **Network** — distributed flow, plural narratives, rhythmic attention cycles  
- **Fragment** — siloed clusters, incompatible narratives, low cross‑talk  
- **Cascade** — high volatility, rapid amplification, narrative churn  
- **Stagnation** — low energy, weak narratives, slow cadence  
- **Reconstruction** — deliberate rebuilding of coherence and signal integrity  

Each basin has a canonical vector representing its structural center.

---

## 📐 Canonical Basin Vectors

Each basin is defined by a representative MediaVector:

```
[S, D, A, N, T]
```

These vectors serve as attractor centers. The Analyzer computes the distance between the current vector and each canonical vector to determine the closest structural match.

Distance alone is not enough—gate conditions ensure the system actually satisfies the structural requirements of the basin.

---

## 🚧 Gate Conditions

Gate conditions prevent misclassification by ensuring that the system meets the minimum structural requirements for a basin. Examples include:

- Minimum narrative coherence for Broadcast  
- Minimum distribution connectivity for Network  
- Minimum fragmentation for Fragment  
- Minimum attention volatility for Cascade  
- Maximum energy thresholds for Stagnation  
- Minimum signal integrity for Reconstruction  

If a vector is close to a canonical basin but fails its gates, the system is classified as **Unstable / Transitional**.

---

## 🧭 Classification Process

The Analyzer performs basin classification in three steps:

### 1. **Compute distance to each canonical vector**
The Analyzer calculates the Euclidean distance between the current vector and each basin’s canonical vector.

### 2. **Apply gate conditions**
The closest basin is only valid if its gate conditions are satisfied.  
If not, the Analyzer checks the next‑closest basin.

### 3. **Fallback to Unstable / Transitional**
If no basin’s gates are satisfied, the system is classified as:

```
basin: "Unstable"
gateSatisfied: false
```

This indicates drift, transition, or structural incoherence.

---

## 🧩 Basin Signatures

Each basin has a characteristic structural signature:

### **Broadcast**
- High S  
- High N  
- Centralized D  
- Low A  
- Slow T  

### **Network**
- Moderate S  
- Distributed D  
- Moderate A  
- Plural N  
- Rhythmic T  

### **Fragment**
- Low N  
- Fragmented D  
- Localized A  
- Weak cross‑talk  

### **Cascade**
- High A  
- High T  
- Low N  
- Overloaded D  
- Signal strain  

### **Stagnation**
- Low A  
- Low T  
- Weak N  
- Low energy  

### **Reconstruction**
- Rising S  
- Rising N  
- Moderate A  
- Stabilizing T  
- Guided D  

These signatures help interpret why a system was classified into a particular basin.

---

## 🧬 Output: MediaBasinResult

The Analyzer returns a structured object:

```
{
  basin: string,
  distance: number,
  gateSatisfied: boolean
}
```

- **basin** — the identified attractor  
- **distance** — how close the vector is to the canonical center  
- **gateSatisfied** — whether structural requirements were met  

This output feeds directly into mode determination, drift detection, and transition analysis.
