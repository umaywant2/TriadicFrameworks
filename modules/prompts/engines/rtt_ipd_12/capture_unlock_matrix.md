# **IPD‑12 Capture → Drift Unlock Matrix**  
### *Formal Operator Unlock Conditions for Inter‑Process Drift*

IPD‑12 enforces a strict contract:

> **No drift without capture.  
No tensor without layered capture.  
No coherence without a baseline.  
No paradox without declared anchors.**

This matrix defines those dependencies.

---

## **1. Unlock Matrix (Full Table)**

| Capture Field | Unlocks | Notes |
|---------------|---------|-------|
| **name** | `map_process()` | Required for identity; no operator runs without it |
| **purpose** | `map_process()` | Required for conceptual drift layer |
| **boundaries** | `drift()` | Drift cannot be computed without constraints |
| **structural_layers** | `drift_tensor()` | Tensor requires multi‑layer structure |
| **operational_flow** | `drift_tensor(L2)` | Enables operational drift layer |
| **coherence_baseline** | `align_coherence()` | Coherence cannot be aligned without a baseline |
| **domain** | `drift_tensor(L5)` | Enables domain drift layer |
| **regime_level** | locks out substrate/inversion | Ensures IPD‑12 stays ≤ deep regime |

---

## **2. Operator Unlock Conditions (Canonical)**

### **map_process()**
Unlocked when:
```
name ∧ purpose
```

### **compare_process()**
Unlocked when:
```
map_process(A) ∧ map_process(B)
```

### **drift()**
Unlocked when:
```
boundaries ∧ structural_layers
```

### **detect_divergence()**
Unlocked when:
```
drift()
```

### **drift_tensor()**
Unlocked when:
```
structural_layers ∧ operational_flow ∧ domain
```

### **align_coherence()**
Unlocked when:
```
coherence_baseline
```

### **cross_system()**
Unlocked when:
```
compare_process() ∧ drift_tensor()
```

---

## **3. Drift‑Tensor Layer Unlocks**

| Drift‑Tensor Layer | Requires Capture Field |
|--------------------|------------------------|
| **L1: Geometric Drift** | structural_layers |
| **L2: Operational Drift** | operational_flow |
| **L3: Temporal Drift** | operational_flow (with time notes) |
| **L4: Conceptual Drift** | purpose |
| **L5: Domain Drift** | domain |

If any field is missing, that layer is **locked**.

---

## **4. Paradox Unlock Conditions (RTT‑1 Structural Mode)**

A structural paradox requires:

```
drift() ∧ coherence_baseline ∧ dependency
```

Where **dependency** is inferred from:

- shared boundaries  
- shared operators  
- shared constraints  

Thus paradox unlocks when:

```
boundaries ∧ coherence_baseline ∧ compare_process()
```

---

## **5. Unlock Graph (Compact)**

```
name + purpose
    ↓
map_process()
    ↓
compare_process()
    ↓
boundaries + structural_layers
    ↓
drift()
    ↓
detect_divergence()
    ↓
operational_flow + domain
    ↓
drift_tensor()
    ↓
coherence_baseline
    ↓
align_coherence()
    ↓
cross_system()
    ↓
paradox(structural)
```

This is the **canonical IPD‑12 unlock graph**.

---

## **6. Summary**

The IPD‑12 capture grammar enforces:

- **identity → structure → drift → coherence → paradox**  
- **no drift without boundaries**  
- **no tensor without layers**  
- **no coherence without a baseline**  
- **no paradox without dependency + drift + coherence**  

This matrix is the formal backbone of the IPD‑12 engine.
