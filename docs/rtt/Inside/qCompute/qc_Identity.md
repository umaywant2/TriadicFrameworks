# qCompute — Identity  
**File:** qc_Identity.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is the **structural compute harness** of RTT‑Inside.

It provides the complete operator → routing → frame → drift → transition → capture → replay pipeline.  
qCompute computes **structure**, not amplitudes.

---

# 1. Purpose

qCompute exists to:

- define resonance‑tiered operators (r1 / r2 / r3)  
- validate operators against grammar, environment, backend, and tier  
- route operators to appropriate backends  
- manage resonance frames and drift accumulation  
- govern environment transitions  
- produce an append‑only `.qtrace` ledger  
- replay and verify structural correctness  

qCompute is the **execution substrate** for RTT‑Inside.

---

# 2. Identity Statement

qCompute is:

- **structural** — computes structure, not physics  
- **deterministic** — routing, drift, and transitions are rule‑driven  
- **governed** — all operators pass through validation  
- **tiered** — r1, r2, r3 define resonance depth  
- **environment‑aware** — sandbox, production, archive  
- **drift‑bounded** — drift accumulation is strictly enforced  
- **append‑only** — capture ledger is immutable  
- **replay‑verifiable** — every session can be reconstructed  

qCompute is **not**:

- a quantum simulator  
- a physics engine  
- a numerical amplitude system  
- a probabilistic execution model  

---

# 3. Structural Role

qCompute is the **compute layer** of RTT‑Inside.

It sits between:

- **Operators** (intent)  
- **Backends** (execution substrate)  
- **Frames** (structural containers)  
- **Drift** (stability envelope)  
- **Transitions** (environment governance)  
- **Capture** (ledger)  
- **Replay** (verification)  

qCompute defines the **rules**, **invariants**, and **structural lifecycle** of computation.

---

# 4. Invariants

qCompute enforces the following invariants:

1. **Grammar Validity**  
   Operators must follow canonical grammar.

2. **Argument Validity**  
   All parameters must be well‑typed and complete.

3. **Environment Legality**  
   - sandbox: r1, r2  
   - production: r1, r2, r3  
   - archive: none  

4. **Backend Legality**  
   - r1 → local-sim  
   - r2 → hybrid-sim  
   - r3 → hardware-qpu-2  

5. **Tier Monotonicity**  
   Tiers may increase within a frame but never decrease.

6. **Measurement Reset**  
   Measurement forces a new frame.

7. **Meta Operators**  
   Meta operators always open a new frame.

8. **Drift Bound**  
   Drift must not exceed environment drift limits.

9. **Transition Legality**  
   - sandbox → production (token required)  
   - production → archive (token required)  
   - archive → (forbidden)  

10. **Archive Terminality**  
    No operators allowed in archive.

11. **Hash Chain Integrity**  
    Capture must maintain a valid hash chain.

---

# 5. Module Boundaries

qCompute defines:

- operator semantics  
- routing rules  
- frame lifecycle  
- drift model  
- environment transitions  
- capture format  
- replay verification  

qCompute does **not** define:

- amplitude simulation  
- quantum state evolution  
- hardware calibration  
- backend implementation details  

These belong to other modules.

---

# 6. Summary

qCompute is the **structural compute substrate** of RTT‑Inside.

It provides:

- resonance‑tiered operators  
- deterministic routing  
- drift‑bounded frames  
- governed transitions  
- append‑only capture  
- strict replay  

qCompute ensures that all computation inside RTT‑Inside is **valid**, **deterministic**, **governed**, and **verifiable**.
