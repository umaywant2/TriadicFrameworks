# Flow Break Cases — Philanthropy Module  
## Structural Failure Patterns in Multi‑Layer Funding Chains (RTT/1)

This file catalogs **flow break cases** in philanthropic systems.  
A flow break is a structural failure where funding, information, or accountability **stops**, **loops**, **dissipates**, or **becomes opaque**.

Flow breaks are detectable using:
- FLOW / TRACE  
- SET load  
- Governance substrate  
- Drift detection  
- Triadic observer  

---

# 1. Case Type A — Hard Break (FLOW = 0)

A **hard break** occurs when funds stop moving entirely.

```
FLOW(src → dst) = 0
RED(flow_break)
```

Common causes:
- frozen grants  
- stalled approvals  
- governance bottlenecks  
- missing documentation  

Structural signature:
```
D1 = high (structural)
D2 = medium (dimensional)
D3 = low
D4 = medium
```

---

# 2. Case Type B — Soft Break (FLOW ↓ but not zero)

A **soft break** occurs when funds move, but far below expected levels.

```
FLOW(src → dst) << expected
SET_LEAK(node) ↑
```

Common causes:
- excessive overhead  
- compliance drag  
- multi‑layer routing  
- narrative‑driven delays  

Structural signature:
```
D1 = medium
D2 = high
D3 = medium
D4 = low
```

---

# 3. Case Type C — Loop Break (Circular Routing)

A **loop break** occurs when funds circulate between nodes without progressing.

```
FLOW(A → B)
FLOW(B → A)
TRACE(path) = circular
```

Common causes:
- regranting loops  
- fiscal sponsorship recursion  
- governance asymmetry  

Structural signature:
```
D1 = high
D2 = high
D3 = medium
D4 = medium
```

---

# 4. Case Type D — Dissipation Break (Energy Loss)

A **dissipation break** occurs when SET load collapses due to extreme leakage.

```
SET_LEAK(node) > 60%
SET_BAL(node) < 0.40
```

Common causes:
- administrative overload  
- branding‑heavy intermediaries  
- inefficient procurement  

Structural signature:
```
D1 = medium
D2 = high
D3 = medium
D4 = high
```

---

# 5. Case Type E — Opaque Break (Visibility Failure)

An **opaque break** occurs when visibility collapses.

```
VIS(node) = low
OPA(node) = high
TRACE(path) = incomplete
```

Common causes:
- missing reports  
- unverified subgrants  
- narrative‑only updates  

Structural signature:
```
D1 = high
D2 = medium
D3 = high
D4 = high
```

---

# 6. Case Type F — Regime Break (Narrative Override)

A **regime break** occurs when narrative, emotion, or authority overrides structure.

```
REG(node) = NAR / EMO / AUTH
NOI ↑
SIG ↓
```

Common causes:
- donor emotion  
- PR‑driven intermediaries  
- political influence  

Structural signature:
```
D1 = medium
D2 = low
D3 = high
D4 = high
```

---

# 7. Case Type G — Beneficiary Break (Output Failure)

A **beneficiary break** occurs when funds reach the final node but fail to convert into outcomes.

```
FLOW(LocalPartner → Beneficiary) = expected
OUTCOME = low
SET_OUT ↓
```

Common causes:
- misaligned programs  
- weak local capacity  
- poor implementation  

Structural signature:
```
D1 = medium
D2 = low
D3 = medium
D4 = medium
```

---

# 8. Flow Break Detection Operators

Flow breaks are detected using:

```
RED(flow_break)
RED(opacity)
RED(leakage)
RED(overhead_spike)
RED(narrative_inflation)
```

And confirmed via:

```
SIG ↓
NOI ↑
REG(type)
DRF(category)
SET_LEAK ↑
SET_BAL ↓
TRACE(path)
```

---

# 9. Flow Break Signature

A flow break signature summarizes the anomaly:

```
FLOW_BREAK_SIGNATURE:
  Type = {{A–G}}
  Node = {{node}}
  Severity = {{low/med/high}}
  SET_LEAK = {{value}}
  VIS = {{value}}
  REG = {{type}}
  DRIFT = {{D1–D4}}
  Notes = {{context}}
```

Example:
```
FLOW_BREAK_SIGNATURE:
  Type = C (Loop Break)
  Node = Intermediary
  Severity = high
  SET_LEAK = 51%
  VIS = low
  REG = NAR
  DRIFT = D1 + D2 + D3
  Notes = regranting loop detected
```

---

# Summary

Flow breaks in philanthropic systems are:

- detectable  
- classifiable  
- structural  
- correctable  

This file provides a library of flow break patterns to support donors, auditors, analysts, and AI agents in identifying and resolving structural failures in funding systems.
