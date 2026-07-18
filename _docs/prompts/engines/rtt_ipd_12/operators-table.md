# **IPD‑12 Operator Reference Table (Compact)**  
### *Inter‑Process Drift — RTT‑IPD‑12*

```
Engine: RTT‑IPD‑12
Regime: Mid → Deep
Operator Layer: Drift / Mapping / Coherence
```

---

## **Compact Operator Table**

| Operator | Purpose | Unlock Condition | Regime Depth |
|---------|---------|------------------|--------------|
| **map_process()** | Capture structural identity of a process/system | ≥ 1 process defined | Mid |
| **compare_process()** | Compare two processes; find shared structure | ≥ 2 processes defined | Mid |
| **drift()** | Detect surface‑level divergence | Structural capture complete | Mid |
| **detect_divergence()** | Identify coherence breaks, regime shifts | Drift baseline exists | Mid → Deep |
| **drift_tensor()** | Multi‑layer drift evaluation | Structural layers provided | Deep |
| **align_coherence()** | Map coherence across processes | Coherence baseline exists | Mid → Deep |
| **cross_system()** | Evaluate cross‑system relationships | Cross‑system relationships defined | Deep |

---

## **Operator Families (1‑Line Summary)**

| Family | Operators | Summary |
|--------|-----------|---------|
| **Capture** | `map_process()` | Define identity, boundaries, layers |
| **Comparison** | `compare_process()` | Identify shared structure & constraints |
| **Drift** | `drift()`, `detect_divergence()` | Detect divergence & coherence breaks |
| **Drift‑Tensor** | `drift_tensor()` | Multi‑layer drift mapping |
| **Coherence** | `align_coherence()` | Restore or evaluate coherence |
| **Cross‑System** | `cross_system()` | Map relationships across systems |

---

## **Operator Chain Examples (Compact)**

### **Basic Drift Chain**
```
map_process() → drift()
```

### **Deep Drift Chain**
```
map_process() → drift_tensor() → detect_divergence()
```

### **Comparison → Drift → Coherence**
```
compare_process() → drift() → align_coherence()
```

### **Cross‑System Drift**
```
map_process() → compare_process() → cross_system()
```

---

## **Engine Boundaries (Compact)**

| Not Available in IPD‑12 | Reason |
|--------------------------|--------|
| `substrate()` | RTT‑∞ only |
| `invert()` | RTT‑∞ only |
| `composite_regime()` | RTT/12 only |
| `substrate_map()` | RTT‑∞ only |

IPD‑12 stays strictly within **drift‑layer structural grammar**.

---

## **Drop‑In Snippet for Prompt Composer**

Paste this into any engine panel:

```
Operators (IPD‑12):
map_process(), compare_process(), drift(), detect_divergence(),
drift_tensor(), align_coherence(), cross_system()
```
