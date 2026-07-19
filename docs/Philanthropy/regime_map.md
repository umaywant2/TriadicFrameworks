# Regime Map — Philanthropy Module  
## Structural Regime Patterns Across Funding Flows (RTT/1)

This file defines how **regimes** shape behavior in philanthropic systems.  
Regimes are decision‑shaping forces that influence how funding moves, how governance operates, and how outcomes emerge.

Philanthropy exhibits four canonical regime types:

- **AUTH** — authority‑driven  
- **NAR** — narrative‑driven  
- **EMO** — emotion‑driven  
- **STR** — structural  

Regimes are detected using the **Triadic Observer**:
```
SIG — structural truth
NOI — narrative/emotional noise
REG — regime classification
SYN — synthesis
```

---

# 1. Regime Overview

| Regime | Description | Impact on Flows | Impact on SET Load | Drift Risk |
|--------|-------------|------------------|---------------------|------------|
| **AUTH** | Authority‑driven decisions | centralized routing | moderate SET_LEAK | governance drift |
| **NAR** | Narrative‑driven decisions | PR‑shaped flows | high SET_LEAK | reporting drift |
| **EMO** | Emotion‑driven decisions | crisis surges, volatility | unstable SET_IN | regime drift |
| **STR** | Structural decisions | efficient routing | low SET_LEAK | minimal drift |

---

# 2. Regime Patterns by Node

## Donor
```
AUTH — donor dictates structure
NAR — donor influenced by storytelling
EMO — crisis‑driven giving
STR — clear intent + structural routing
```

## Foundation
```
AUTH — board‑driven decisions
NAR — branding‑heavy grantmaking
EMO — reactive funding cycles
STR — standards‑based allocation
```

## Intermediary
```
AUTH — centralized control
NAR — impact theater, PR inflation
EMO — donor‑pleasing behavior
STR — transparent regranting
```

## NGO
```
AUTH — top‑down program design
NAR — narrative‑heavy reporting
EMO — donor‑appeasement cycles
STR — evidence‑based implementation
```

## Local Partner
```
AUTH — local political influence
NAR — story‑driven updates
EMO — community pressure
STR — grounded, contextual execution
```

## Beneficiary
```
AUTH — imposed program structure
NAR — selective reporting
EMO — crisis‑response behavior
STR — direct outcome generation
```

---

# 3. Regime Effects on Funding Flow

### AUTH Regime
```
FLOW = centralized
TRACE = partial
SET_LEAK = moderate
OPA ↑
ASYM ↑
```

### NAR Regime
```
FLOW = distorted by storytelling
NOI ↑
SET_LEAK ↑↑
DRF(reporting)
```

### EMO Regime
```
FLOW = volatile
SET_IN = surge
SET_OUT = inconsistent
DRF(regime)
```

### STR Regime
```
FLOW = efficient
TRACE = full
SET_LEAK = low
COH ↑
```

---

# 4. Regime Detection Operators

Regimes are detected using:

```
REG(node) = AUTH / NAR / EMO / STR
SIG(data)
NOI(data)
CTX(node)
SYN(system)
```

Mapping:
- **SIG ↓** → non‑structural regime  
- **NOI ↑** → NAR or EMO  
- **ASYM ↑** → AUTH  
- **OPA ↑** → AUTH or NAR  
- **SET_LEAK ↑** → NAR or EMO  

---

# 5. Regime Drift

Regime drift occurs when a non‑structural regime dominates:

```
DRF(regime) = high when:
  REG = NAR
  REG = EMO
  REG = AUTH (unchecked)
```

Effects:
- narrative inflation  
- emotional volatility  
- authority asymmetry  
- flow distortion  
- outcome incoherence  

---

# 6. Regime Signatures

A regime signature summarizes the dominant regime forces:

```
REGIME_SIGNATURE:
  Donor = {{AUTH/NAR/EMO/STR}}
  Foundation = {{AUTH/NAR/EMO/STR}}
  Intermediary = {{AUTH/NAR/EMO/STR}}
  NGO = {{AUTH/NAR/EMO/STR}}
  LocalPartner = {{AUTH/NAR/EMO/STR}}
  Beneficiary = {{AUTH/NAR/EMO/STR}}
  Primary = {{REG}}
  Notes = {{context}}
```

Example:
```
REGIME_SIGNATURE:
  Donor = EMO
  Foundation = AUTH
  Intermediary = NAR
  NGO = STR
  LocalPartner = STR
  Beneficiary = STR
  Primary = NAR
  Notes = narrative-driven intermediary distorting flow
```

---

# 7. Regime Corrections (Structural)

Corrections use the FIX operator:

```
FIX(Foundation) → increase transparency
FIX(Intermediary) → reduce narrative incentives
FIX(NGO) → strengthen evidence base
FIX(LocalPartner) → improve governance
```

Corrections target **structure**, not individuals.

---

# Summary

Regimes shape philanthropic systems by influencing:
- flow integrity  
- governance substrate  
- SET load  
- drift patterns  
- outcome coherence  

The regime map provides a structural lens for detecting and correcting non‑structural forces in funding flows.
