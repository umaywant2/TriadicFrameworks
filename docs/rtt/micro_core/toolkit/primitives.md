# 🔹 Primitives (MRT)

Primitives are the smallest actionable units in the Micro‑Resonance Toolkit (MRT).  
They define the minimal operations, checks, and structural adjustments that micro‑regimes can perform while remaining coherent.

Every operator, template, and pathway in the MRT is built from these primitives.

---

## 🧩 P₁ — State Read

**Purpose**  
Retrieve the current values of A, B, P, δ, Δt, and Dᶠ.

**Behavior**  
- read without modifying  
- return minimal, typed values  
- suitable for ultra‑low‑power loops  

**Used In**  
All operators and coherence tools.

---

## 🧩 P₂ — State Write

**Purpose**  
Apply a minimal update to A, B, or P.

**Behavior**  
- atomic write  
- bounded mutation  
- preserves triad integrity  

**Used In**  
Resonance operators, drift correction, inversions.

---

## 🧩 P₃ — Drift Measure

**Purpose**  
Compute δ (drift) for the current micro‑step.

**Behavior**  
- compare expected vs. actual state  
- return δ as a fractional value  
- no side effects  

**Used In**  
K₁ (Drift Bounding), stability checks.

---

## 🧩 P₄ — Timing Measure

**Purpose**  
Compute Δt (timing interval) between micro‑steps.

**Behavior**  
- measure elapsed micro‑time  
- return Δt  
- no structural modification  

**Used In**  
K₂ (Timing Stabilizer), resonance loops.

---

## 🧩 P₅ — Boundary Shift

**Purpose**  
Adjust the boundary node (B) by a minimal increment.

**Behavior**  
- B⁺ or B⁻ shift  
- bounded, reversible  
- preserves triad symmetry  

**Used In**  
K₃ (Boundary Alignment).

---

## 🧩 P₆ — Potential Update

**Purpose**  
Modify the potential node (P) based on micro‑state evolution.

**Behavior**  
- update P deterministically  
- maintain coherence with A and B  
- no uncontrolled expansion  

**Used In**  
Resonance loops, fractional transitions.

---

## 🧩 P₇ — Fractional Step

**Purpose**  
Move the micro‑state along the fractional ladder.

**Behavior**  
- Dᶠ₁ → Dᶠ₁+Δ  
- smooth, bounded transition  
- no overshoot  

**Used In**  
K₆ (Fractional‑Ladder Regulator).

---

## 🧩 P₈ — Inversion Trigger

**Purpose**  
Evaluate whether conditions for inversion (↺) are met.

**Behavior**  
- check coherence  
- check drift  
- check structural readiness  

**Used In**  
R₂ (Inversion Operator).

---

## 🧩 P₉ — Bridge Check

**Purpose**  
Determine whether the micro–macro bridge may activate.

**Behavior**  
- evaluate C ≥ C*  
- check resonance persistence  
- return boolean  

**Used In**  
K₇ (Bridge Gate).

---

## ✔️ Summary

MRT Primitives provide the smallest building blocks for:

- resonance  
- drift correction  
- timing stabilization  
- boundary alignment  
- fractional transitions  
- inversions  
- micro–macro bridging  

They are the atomic actions from which all micro‑scale behavior in RTT Micro Core is constructed.
