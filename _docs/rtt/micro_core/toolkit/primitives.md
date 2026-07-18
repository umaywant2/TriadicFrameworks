# 🔹 **Primitives (MRT)**  
*The smallest actionable units in the Micro‑Resonance Toolkit*

Primitives define the minimal operations, measurements, and structural adjustments that micro‑regimes can perform while remaining coherent.  
Every operator, template, and pathway in the MRT is built from these primitives.

They are:

- deterministic  
- low‑overhead  
- coherence‑preserving  
- suitable for embedded and ultra‑low‑power systems  

---

## 🧩 **P₁ — State Read**

**Purpose**  
Retrieve the current values of A, B, P, δ, Δt, and Dᶠ.

**Behavior**  
- read without modifying  
- return minimal, typed values  
- suitable for ultra‑low‑power loops  

**Used In**  
All operators and coherence tools.

---

## 🧩 **P₂ — State Write**

**Purpose**  
Apply a minimal update to A, B, or P.

**Behavior**  
- atomic write  
- bounded mutation  
- preserves triad integrity  

**Used In**  
Resonance operators, drift correction, inversions.

---

## 🧩 **P₃ — Drift Measure**

**Purpose**  
Compute δ (drift) for the current micro‑step.

**Behavior**  
- compare expected vs. actual state  
- return δ as a fractional value  
- no side effects  

**Used In**  
K₁ (Drift Bounding), stability checks.

---

## 🧩 **P₄ — Timing Measure**

**Purpose**  
Compute Δt (timing interval) between micro‑steps.

**Behavior**  
- measure elapsed micro‑time  
- return Δt  
- no structural modification  

**Used In**  
K₂ (Timing Stabilizer), resonance loops.

---

## 🧩 **P₅ — Boundary Shift**  
*(Completed canonical version — your file cuts off here in the tab.)*

**Purpose**  
Apply a minimal, coherence‑preserving adjustment to the boundary node (B).

**Behavior**  
- detect B⁺ / B⁻ displacement  
- apply bounded correction  
- maintain triad symmetry  
- no inversion or structural collapse  

**Used In**  
K₃ (Boundary Alignment), inversion preparation.

---

## 🧩 **P₆ — Coherence Sample**

**Purpose**  
Measure instantaneous coherence C for the current micro‑state.

**Behavior**  
- evaluate structural, timing, and energy alignment  
- return C as a normalized value  
- no mutation  

**Used In**  
K₅ (Inversion Guard), μ→Μ bridge activation.

---

## 🧩 **P₇ — Fractional Step**

**Purpose**  
Perform a minimal fractional‑dimensional adjustment (Dᶠ → Dᶠ + Δ).

**Behavior**  
- bounded fractional shift  
- maintain Δt and δ within thresholds  
- reversible  
- coherence‑preserving  

**Used In**  
Fractional‑ladder transitions, R₂, K₆.

---

## ✔️ **Summary**

| Primitive | Purpose |
|----------|----------|
| **P₁** | Read state values |
| **P₂** | Write minimal state updates |
| **P₃** | Measure drift |
| **P₄** | Measure timing |
| **P₅** | Adjust boundary position |
| **P₆** | Sample coherence |
| **P₇** | Perform fractional‑dimensional step |

These primitives form the **atomic action layer** of the MRT — everything else is built on top of them.
