# Funding Flow Map — Philanthropy & Funding Transparency Module

This file defines the canonical RTT funding flow map for philanthropic systems.  
It provides a structural, triadic, AI-parsable model for tracing every dollar from source to outcome.

The goal: **make all flows visible, measurable, and aligned**.

---

# 1. Overview

Philanthropic funding flows through multiple layers:

**Donor → Foundation → Intermediary → NGO → Subcontractor → Local Partner → Beneficiary**

Each layer introduces:
- overhead  
- narrative  
- governance decisions  
- potential drift  
- potential leakage  

The Funding Flow Map uses RTT operators to make these flows structurally visible.

---

# 2. Core Flow Structure (RTT Funding Chain)

```
[Donor]
   ↓ FLOW
[Foundation]
   ↓ FLOW
[Intermediary]
   ↓ FLOW
[NGO]
   ↓ FLOW
[Subcontractor]
   ↓ FLOW
[Local Partner]
   ↓ FLOW
[Beneficiary]
```

Each node is evaluated using:

- **LOAD(node)**  
- **LEAK(node)**  
- **CONVERT(input → output)**  
- **REG(type)**  
- **DRF(type)**  
- **ACC(node)**  
- **VIS(node)**  

This creates a **triadic structural map** of the entire chain.

---

# 3. Flow Operators Applied to Philanthropy

## 3.1 FLOW(src → dst)
Maps the movement of funds.

Example:
```
FLOW(DonorA → FoundationB)
FLOW(FoundationB → NGO_C)
FLOW(NGO_C → LocalPartnerD)
```

---

## 3.2 LOAD(node)
Measures structural load (administrative, financial, governance).

Example:
```
LOAD(NGO_C) = high (multi-country operations)
```

---

## 3.3 LEAK(node)
Identifies dilution, overhead, or diversion.

Example:
```
LEAK(IntermediaryX) = 42%
```

---

## 3.4 CONVERT(input → output)
Maps how funds are transformed.

Example:
```
CONVERT($1M → $620k direct services)
```

---

## 3.5 ROUTE(path)
Describes the full multi-layer path.

Example:
```
ROUTE(Donor → Foundation → NGO → Subcontractor → Community)
```

---

# 4. Regime Mapping Along the Flow

Each node is tagged with its dominant regime:

- **AUTH** (authority)  
- **NAR** (narrative)  
- **EMO** (emotional)  
- **STR** (structural)  

Example:
```
REG(NAR) at FoundationB (impact branding)
REG(AUTH) at Board (donor capture)
REG(STR) at LocalPartner (direct service)
```

This reveals where **regime distortions** occur.

---

# 5. Drift Detection Along the Flow

Drift types:
- **mission drift**
- **financial drift**
- **governance drift**
- **reporting drift**

Example:
```
DRF(financial) at FoundationB (payout < 5%)
DRF(reporting) at NGO_C (narrative inflation)
```

---

# 6. Funding Flow Integrity Score

Each flow receives an integrity score based on:

- alignment (ALN)  
- coherence (COH)  
- visibility (VIS)  
- accountability (ACC)  
- leakage (LEAK)  
- drift (DRF)  

Example:
```
IntegrityScore = 0.62 (moderate drift, high leakage)
```

---

# 7. Triadic Observer for Funding Flows

The triadic observer extracts:

- **SIG** (signal: actual flows, outcomes)  
- **NOI** (noise: PR, emotional appeals)  
- **CTX** (context: constraints, governance)  
- **SYN** (structural synthesis)  

Example:
```
SIG: $2.4M delivered to programs
NOI: 38 pages of narrative reporting
CTX: multi-country compliance constraints
SYN: 61% alignment with donor intent
```

---

# 8. Flow Map Example (AI-Generated)

```
DonorA
  FLOW → FoundationB
    LOAD = medium
    LEAK = 12%
    REG = AUTH
  FLOW → IntermediaryX
    LOAD = high
    LEAK = 42%
    REG = NAR
  FLOW → NGO_C
    LOAD = medium
    LEAK = 18%
    REG = STR
  FLOW → LocalPartnerD
    LOAD = low
    LEAK = 4%
    REG = STR
  FLOW → Beneficiary
```

**Overall Integrity:** 0.54  
**Primary Drift:** financial + narrative  
**Primary Leakage:** IntermediaryX  

---

# 9. Flow Map Summary

The Funding Flow Map provides:

- a **structural view** of philanthropic flows  
- a **triadic regime map**  
- a **drift detection engine**  
- a **leakage and conversion model**  
- a **coherence and alignment score**  
- a **full-path trace** from donor to beneficiary  

This is the core of the Philanthropy module’s clarity engine.

Every dollar becomes **visible**, **traceable**, and **structurally accountable**.
