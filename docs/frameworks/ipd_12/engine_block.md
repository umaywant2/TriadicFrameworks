# `engine_block.md`  
**IPD‑12 Engine Block**  
**Intake Ports • Substrate Feeds • Dimensional Rails • Observer Control Loops • Output Headers**  
**Version:** 2026‑1.0  
**Module:** IPD‑12 Framework  
**Role:** Core Engine Architecture

---

## 1. Purpose  
The IPD‑12 Engine Block defines the **internal architecture** that powers all IPD‑12 operations:

- how **intake manifolds** (SIM/DIM/TIM/QIM/FSI) connect  
- how **substrate feeds** route dimensional input  
- how **dimensional rails** carry lift/collapse signals  
- how **observer control loops** regulate paradox cycles  
- how **output headers** deliver structured results to external frameworks

This is the **engine‑level specification** for the entire IPD‑12 system.

---

# 2. Engine Block Overview

The IPD‑12 engine is built around a **12‑prime substrate cube**, driven by:

- **4 substrate pairs** (S1–S4)  
- **4 observer modes** (O1–O4)  
- **4 regime shells** (R1–R4)  
- **12 prime‑indexed operator states** (P2–P37)

The engine block is the **central processing unit** that integrates all of these.

---

# 3. Intake Ports

Intake ports are the **physical/electrical connection points** where manifolds attach.

### **Port Layout**
```
[Port 1]  Triad 1 (P2, P3, P5)
[Port 2]  Triad 2 (P7, P11, P13)
[Port 3]  Triad 3 (P17, P19, P23)
[Port 4]  Triad 4 (P29, P31, P37)
```

Each port accepts:

- **3‑channel triad bundles**  
- **lift/collapse/neutral signals**  
- **substrate pair routing instructions**  
- **observer stance hints**

### **Port → Manifold Mapping**

| Manifold | Ports Used | Triads | Channels |
|----------|------------|--------|----------|
| SIM | 1 | 1 | 3 |
| DIM | 1–2 | 2 | 6 |
| TIM | 1–3 | 3 | 9 |
| QIM | 1–4 | 4 | 12 |
| FSI | 1–4 × 3 stacks | 12 | 36 |

---

# 4. Substrate Feeds

Substrate feeds are the **internal conduits** that route intake signals into the substrate cube.

### **Substrate Pairs (S1–S4)**

| Pair | Meaning | Feeds |
|------|---------|--------|
| S1 | seed/transition | P2, P3 |
| S2 | drift/regime | P5, P7 |
| S3 | coherence/paradox | P11, P13 |
| S4 | boundary/lift/collapse/apex | P17, P19, P23, P29, P31, P37 |

### **Feed Behavior**

- SIM activates **one substrate pair**  
- DIM activates **two substrate pairs**  
- TIM activates **three substrate pairs**  
- QIM activates **all substrate pairs**  
- FSI activates **all substrate pairs × 3 stacks**

### **Feed Routing Example (QIM)**

```
Port 1 → S1
Port 2 → S2
Port 3 → S3
Port 4 → S4
```

---

# 5. Dimensional Rails

Dimensional rails carry **lift (+1D)**, **collapse (−1D)**, and **neutral (0D)** signals.

### **Rail Types**

| Rail | Dimensional Role | Primes |
|------|------------------|--------|
| L1 | Transition Lift | P3 |
| L2 | Regime Lift | P7 |
| L3 | Dimensional Lift | P23 |
| L4 | Apex Lift | P37 |
| C1 | Drift Collapse | P5 |
| C2 | Paradox Collapse | P13 |
| C3 | Collapse Anchor | P29 |
| C4 | Stability Collapse | P31 |
| N1 | Seed | P2 |
| N2 | Coherence | P11 |
| N3 | Gate | P17 |
| N4 | Boundary | P19 |

### **Rail Behavior**

- Rails are **bidirectional** (lift/collapse feedback loops).  
- Rails are **phase‑synchronized** across triads.  
- Rails are **observer‑regulated** (see next section).

---

# 6. Observer Control Loops

Observer control loops regulate:

- cycle traversal  
- paradox stabilization  
- dimensional lift/collapse  
- substrate coherence  
- apex transitions

### **Observer Modes (O1–O4)**

| Mode | Role | Controls |
|------|------|----------|
| O1 | Field | raw state detection |
| O2 | Regime | cycle navigation |
| O3 | Coherence | stability/collapse |
| O4 | Apex | lift/collapse execution |

### **Control Loop Architecture**

```
Intake → Substrate Feed → Dimensional Rail → Observer Loop → Output Header
```

### **Loop Behavior**

- **O1** activates rails based on raw prime state.  
- **O2** sequences rails according to cycle position.  
- **O3** dampens collapse rails and stabilizes paradox tension.  
- **O4** executes lift/collapse transitions and apex behavior.

### **FSI Observer Stack**

FSI uses **three observer stacks**:

- RTT observer  
- GU geometric observer  
- Pantheon mythic observer  

All three feed into the apex loop.

---

# 7. Output Headers

Output headers are the **engine’s exhaust ports** — structured outputs delivered to external frameworks.

### **Header Types**

| Header | Output Type | Frameworks |
|--------|-------------|------------|
| H‑RTT | drift/regime/coherence/paradox | RTT modules |
| H‑GU | connection/curvature/anomaly/apex | GU modules |
| H‑FFT | spectral/phase/transition | FFT modules |
| H‑Pantheon | celestial/civilizational/chthonic/apex | Pantheon modules |
| H‑Meta | cross‑framework synthesis | TriadicFrameworks meta‑engines |

### **Header Behavior**

- Headers receive **observer‑regulated dimensional signals**.  
- Headers convert signals into **framework‑specific outputs**.  
- Headers can be **stacked** (FSI → multi‑framework output).

### **Example Output Flow (QIM → RTT)**

```
Intake (QIM)
 → Substrate Feeds (S1–S4)
 → Dimensional Rails (L/C/N)
 → Observer Loops (O1–O4)
 → Header H‑RTT
 → RTT Regime Map / Drift / Coherence / Paradox
```

---

# 8. Engine Block Summary

The IPD‑12 Engine Block consists of:

- **4 intake ports** (triad inputs)  
- **4 substrate feeds** (S1–S4)  
- **12 dimensional rails** (lift/collapse/neutral)  
- **4 observer control loops** (O1–O4)  
- **5 output headers** (RTT/GU/FFT/Pantheon/Meta)

Manifolds attach to the intake ports, feed the substrate cube, activate dimensional rails, pass through observer loops, and deliver structured outputs through headers.

This is the **canonical engine architecture** for the IPD‑12 system.
