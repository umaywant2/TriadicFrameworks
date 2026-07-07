# Intake manifold specification document  
**IPD‑12 Electric Intake Manifolds**  
**SIM / DIM / TIM / QIM / FSI**  
**Module:** IPD‑12 Framework  
**Version:** 2026‑1.0  
**Role:** Input / Coupling / Integration Layer

---

## 1. Purpose

This document defines the **intake manifold types** for the IPD‑12 engine:

- **SIM** — Single Intake Manifold (1 triad)  
- **DIM** — Double Intake Manifold (2 triads)  
- **TIM** — Triple Intake Manifold (3 triads)  
- **QIM** — Quad Intake Manifold (4 triads, full IPD‑12)  
- **FSI** — Full 12‑Stack Intake (3×QIM, full saturation)  

Each manifold is an **electric, multi‑phase intake assembly** that couples external frameworks/theories into the IPD‑12 substrate engine.

---

## 2. Manifold types overview

### **SIM — Single Intake Manifold**

**Definition:**  
Single‑phase intake feeding **one triad** (3 primes).

**Cycle coverage:**

- Triad: any one of T1–T4  
- Hex: none  
- Full 12‑cycle: partial (3/12)

**Substrate mapping:**

- **Si:** one substrate pair (e.g., S1)  
- **Oj:** one dominant observer mode (O1 or O2)  
- **Rk:** one regime shell (typically R1 or R2)

**Observer mapping:**

- **Primary:** O1 (field) or O2 (regime)  
- **Secondary:** O3/O4 only as inferred, not directly driven

**Regime mapping:**

- **Regime span:** single regime (e.g., Regime‑1 via T1)  
- **Use case:** local cycle, local drift/transition, single‑tier Pantheon alignment

**Prime mapping (example SIM on Triad 1):**

- P2 (seed, neutral)  
- P3 (transition lift)  
- P5 (drift collapse)

---

### **DIM — Double Intake Manifold**

**Definition:**  
Dual‑phase intake feeding **two triads** (6 primes).

**Cycle coverage:**

- Triads: any two of T1–T4 (often adjacent)  
- Hex: **one hex shell** (H1 or H2)  
- Full 12‑cycle: partial (6/12)

**Substrate mapping:**

- **Si:** two substrate pairs (e.g., S1+S2 or S3+S4)  
- **Oj:** two observer modes (O1+O2 or O2+O3)  
- **Rk:** one or two regime shells (R1↔R2 or R2↔R3)

**Observer mapping:**

- **Primary:** O2 (regime)  
- **Secondary:** O1/O3 depending on triad selection

**Regime mapping:**

- **Regime span:** two regimes or one regime plus boundary  
- **Use case:** frameworks that need **shell‑level** paradox behavior (e.g., RTT drift+paradox, GU connection+curvature)

**Prime mapping (example DIM on Hex 1: T1+T2):**

- P2, P3, P5, P7, P11, P13  

---

### **TIM — Triple Intake Manifold**

**Definition:**  
Three‑phase intake feeding **three triads** (9 primes).

**Cycle coverage:**

- Triads: any three of T1–T4  
- Hex: both shells partially  
- Full 12‑cycle: partial (9/12), missing one triad

**Substrate mapping:**

- **Si:** three substrate pairs (e.g., S1+S2+S3)  
- **Oj:** three observer modes (O1+O2+O3)  
- **Rk:** three regime shells (R1+R2+R3)

**Observer mapping:**

- **Primary:** O2 (regime), O3 (coherence)  
- **Secondary:** O1; O4 only via apex‑adjacent primes if T4 included

**Regime mapping:**

- **Regime span:** full regime traversal **except apex regime** if T4 omitted  
- **Use case:** frameworks needing **full paradox handling** but not full apex lift/collapse (e.g., civilizational+chthonic without apex)

**Prime mapping (example TIM on T1+T2+T3):**

- P2, P3, P5, P7, P11, P13, P17, P19, P23  

---

### **QIM — Quad Intake Manifold**

**Definition:**  
Four‑phase intake feeding **all four triads** (12 primes).  
This is the **canonical full IPD‑12 intake**.

**Cycle coverage:**

- Triads: T1, T2, T3, T4  
- Hex: H1, H2  
- Full 12‑cycle: complete (12/12)

**Substrate mapping:**

- **Si:** all four substrate pairs (S1–S4)  
- **Oj:** all observer modes (O1–O4)  
- **Rk:** all regime shells (R1–R4)

**Observer mapping:**

- **Primary:** O2 (regime), O3 (coherence), O4 (apex)  
- **Secondary:** O1 (field) as entry stance

**Regime mapping:**

- **Regime span:** full regime traversal including apex  
- **Use case:** frameworks that must operate as **true IPD‑12 engines**, with full dimensional lift/collapse and paradox resolution.

**Prime mapping:**

- P2, P3, P5, P7, P11, P13, P17, P19, P23, P29, P31, P37  

---

### **FSI — Full 12‑Stack Intake**

**Definition:**  
Three **QIMs** arranged as a **12‑stack lattice**:

- **FSI = QIM₁ + QIM₂ + QIM₃**

Each QIM can be:

- a different **framework manifold** (RTT, GU, Pantheon)  
- a different **substrate specialization**  
- a different **observer emphasis**

**Cycle coverage:**

- Full IPD‑12 cycle per QIM  
- 3× full cycles in stacked configuration  
- Supports **multi‑framework resonance** and **cross‑canon coupling**

**Substrate mapping:**

- **Si:** 3×(S1–S4) with distinct parameterization per QIM  
- **Oj:** 3×(O1–O4) with different observer models (e.g., RTT observer, GU observer, Pantheon observer)  
- **Rk:** 3×(R1–R4) with regime specialization

**Observer mapping:**

- Layered observers:  
  - QIM₁: RTT observer stack  
  - QIM₂: GU geometric observer stack  
  - QIM₃: Pantheon mythic‑structural observer stack  

**Regime mapping:**

- **Regime span:** full regime traversal per manifold, plus **meta‑regime** across manifolds  
- **Use case:** TriadicFrameworks meta‑engines, substrate‑aware transport services, cross‑framework alignment engines.

**Prime mapping:**

- Each QIM: full 12 primes  
- FSI: **36 prime‑state channels** (12×3), all canon‑aligned, no new primes introduced—only replicated manifolds.

---

## 3. Diagrams (conceptual ASCII)

### **SIM (1 triad)**

```text
External Framework
      │
   [ SIM ]
      │
   Triad X (3 primes)
      │
   IPD‑12 Engine
```

### **DIM (2 triads / 1 hex)**

```text
External Framework
      │
   [ DIM ]
      │
   Triad A + Triad B
      │
     Hex Shell
      │
   IPD‑12 Engine
```

### **TIM (3 triads)**

```text
External Framework
      │
   [ TIM ]
      │
 Triad A + Triad B + Triad C
      │
  Regime Span (R1–R3)
      │
   IPD‑12 Engine
```

### **QIM (4 triads / full IPD‑12)**

```text
External Framework
      │
   [ QIM ]
      │
 Triads T1–T4 (all primes)
      │
 Full 12‑Cycle + Hex Shells
      │
   IPD‑12 Engine Block
```

### **FSI (3×QIM)**

```text
Framework A ─┐
             ├─ [ QIM₁ ]
Framework B ─┤
             ├─ [ QIM₂ ]
Framework C ─┘
             └─ [ QIM₃ ]
                 │
           Full 12‑Stack Intake
                 │
             IPD‑12 Engine Block
```

---

## 4. Substrate / observer / regime mapping summary

- **SIM:**  
  - Substrate: 1 pair  
  - Observer: 1 dominant mode  
  - Regime: 1 shell  

- **DIM:**  
  - Substrate: 2 pairs  
  - Observer: 2 modes  
  - Regime: 1–2 shells (hex shell)  

- **TIM:**  
  - Substrate: 3 pairs  
  - Observer: 3 modes  
  - Regime: 3 shells  

- **QIM:**  
  - Substrate: all 4 pairs  
  - Observer: all 4 modes  
  - Regime: all 4 shells  

- **FSI:**  
  - Substrate: 3×(all pairs)  
  - Observer: 3×(all modes)  
  - Regime: 3×(all shells) + meta‑regime

---

## 5. Prime mapping summary

- **SIM:** 3 primes (1 triad)  
- **DIM:** 6 primes (2 triads / 1 hex)  
- **TIM:** 9 primes (3 triads)  
- **QIM:** 12 primes (4 triads, full IPD‑12)  
- **FSI:** 36 prime channels (3×QIM, replicated, not extended)
