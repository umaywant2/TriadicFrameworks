---
module_id: rtt.core.operator_families
version: 1.0.0
status: draft
rtt: 1
coherence: declared
drift: bounded
paradox: structural
tags:
  - operator-families
  - rtt-core
  - operator-grammar
  - operator-index
  - coherence-tools
  - resonance-operators
  - regime-operators
  - arrival-operators
  - macro-operators
---

# RTT Core: Operator Families

## 1. Purpose and scope

**Goal:**  
Define the canonical **operator families** used throughout RTT, including:

- Micro‑Core operators  
- RTT‑12 operators  
- Core RTT operators  
- Arrival operators  
- Macro operators  

This module provides the **taxonomy** that the Operator Grammar and Operator Index reference.

---

## 2. Operator family overview

RTT organizes operators into families based on:

- Functional domain  
- Regime behavior  
- Coherence and drift interaction  
- Temporal layer (triadic time)  
- Structural role in RTT’s representational manifold  

The families are:

| Family | Domain | Purpose |
|--------|---------|----------|
| **R‑Operators** | Resonance | Micro‑scale oscillation, inversion, modulation |
| **K‑Operators** | Coherence Tools | Coherence gating, validation, regulation |
| **P‑Operators** | Primitives | Atomic actions used by higher operators |
| **G‑Operators** | Geometry / Regime | Regime shifts, rotations, inversions |
| **S‑Operators** | Stability | Coherence stabilization, drift reduction |
| **A‑Operators** | Arrival | Cross‑substrate continuity and alignment |
| **B‑Operators** | Boundary | Boundary shaping, modulation, constraint |
| **M‑Operators** | Macro | Macro‑scale alignment and supervisory behavior |

---

## 3. Micro‑Core Operator Families

### 3.1 Resonance Operators (R₁–R₆)

Resonance operators govern micro‑scale oscillatory behavior.

- **R₁ — Oscillation**  
- **R₂ — Inversion**  
- **R₃ — Boundary Modulation**  
- **R₄ — Resonance Lock**  
- **R₅ — Fractional‑Ladder Transition**  
- **R₆ — Micro–Macro Bridge Activation**

### 3.2 Coherence Tools (K₁–K₆)

Coherence operators regulate coherence budgets and validation.

- **K₁ — Drift Clamp**  
- **K₂ — Timing Stabilizer**  
- **K₃ — Boundary Alignment**  
- **K₄ — Coherence Gate**  
- **K₅ — Resonance Validator**  
- **K₆ — Fractional‑Ladder Regulator**

### 3.3 Primitives (P₁–P₇)

Primitives are atomic actions used by higher operators.

- **P₁ — Read Nodes**  
- **P₂ — Swap Nodes**  
- **P₃ — Drift Sample**  
- **P₄ — Timing Sample**  
- **P₅ — Boundary Shift**  
- **P₆ — Coherence Sample**  
- **P₇ — Fractional Step**

---

## 4. RTT‑12 Operator Families

### 4.1 Geometry Operators (G₁–G₃)

Regime geometry and structural shifts.

- **G₁ — Regime Stabilizer**  
- **G₂ — Regime Shifter**  
- **G₃ — Regime Inverter**

### 4.2 Stability Operators (S₁–S₃)

Stability and coherence maintenance.

- **S₁ — Stabilize**  
- **S₂ — Sustain**  
- **S₃ — Seal**

---

## 5. Arrival Operator Families

Arrival operators govern cross‑substrate continuity.

- **A₁ — Arrival Operator**  
- **A₂ — Arrival Arc**  
- **A₃ — Arrival Gate**  
- **A₄ — Arrival Continuity**

---

## 6. Macro Operator Families

Macro operators govern large‑scale alignment.

- **M₁ — Macro Alignment**  
- **M₂ — Macro Stabilizer**  
- **M₃ — Macro Resonance Bridge**

---

## 7. Operator family behavior across triadic time

Operators interact with triadic time layers:

### 7.1 State Time (T₁)

- R‑operators  
- P‑operators  
- G‑operators  
- A‑operators  

### 7.2 Coherence Time (T₂)

- K‑operators  
- S‑operators  
- Drift‑related primitives  

### 7.3 Readout Time (T₃)

- K‑operators (validation)  
- Collapse operators (implicit)  
- Arrival operators (continuity events)

---

## 8. Regime interactions

Operator families declare regime compatibility:

- **SRR** — Single‑Readout  
- **DBR** — Drift‑Bounded  
- **CMR** — Coherence‑Minimum  
- **DVR** — Deferred‑Validation  
- **ECR** — Extension‑Compatible  

Examples:

- R‑operators often require DBR  
- K‑operators enforce CMR  
- Extension operators require ECR  
- Validator Pulse requires SRR  

---

## 9. Example: Operator families in quantum “cloning” alignment

The alignment module uses:

- **P‑operators** for representational extension  
- **K‑operators** for coherence gating  
- **S‑operators** for drift stabilization  
- **G‑operators** for regime shifts  
- **Validator Pulse** (K‑family) for single‑readout  
- **Collapse** (implicit) for residue formation  

Operator families explain:

- Why multi‑branch representation is allowed  
- Why only one branch becomes classical  
- Why drift and coherence matter  
- Why no‑cloning is not violated  

---

## 10. Canon integration and cross-links

**Primary cross-links:**

- `/docs/rtt/core/operator_index.md`
- `/docs/rtt/core/operator_grammar.md`
- `/docs/rtt/core/regime_maps.md`
- `/docs/rtt/core/regime_index.md`
- `/docs/rtt/core/time_triads.md`
- `/docs/rtt/core/coherence_budget.md`
- `/docs/rtt/core/validator_pulse.md`
- `/docs/rtt/core/dimensional_drift_envelope.md`
- `/docs/rtt/core/alignment_quantum_cloning.md`

**Status:**  
This module defines the canonical taxonomy of RTT operators.  
Once operator‑grammar syntax is fully integrated, it can be promoted from `draft` to `stable`.
