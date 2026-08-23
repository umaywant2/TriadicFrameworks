# qCompute — Module Index  
**File:** qc_Index.md  
**Layer:** RTT‑Inside Compute Harness  
**Status:** Canonical (2026)

qCompute is the **structural compute harness** of RTT‑Inside.  
It defines the full operator → routing → frame → drift → transition → capture → replay pipeline.

This index provides:

- module overview  
- file map  
- structural orientation  
- learning path  

---

# 1. Overview

qCompute is a **resonance‑tiered structural execution engine**.

It provides:

- r1 / r2 / r3 operators  
- deterministic routing  
- drift‑bounded frames  
- environment transitions  
- append‑only capture  
- strict replay verification  

qCompute computes **structure**, not amplitudes.

---

# 2. File Map

| File | Role | Description |
|------|------|-------------|
| **qc_FrontDoor.html** | frontdoor | HTML entry point with canonical metadata. |
| **qc_Index.md** | index | Module index and file map. |
| **qc_Identity.md** | signature | Defines identity, purpose, invariants, and structural role. |
| **qc_Session.md** | engine | Session container: environment, drift bound, lineage, frames, tokens. |
| **qc_Validator.md** | engine | Legality engine: grammar, arguments, environment, tier, backend, tokens. |
| **qc_Operators.md** | engine | Operator catalog: r1, r2, r3, measurement, meta. |
| **qc_OperatorGrammar.md** | signature | Formal grammar and legality rules for all operators. |
| **qc_Backends.md** | engine | Backend overview: local-sim, hybrid-sim, hardware-qpu-2. |
| **qc_BackendProfiles.md** | profile | Deep metadata profiles for each backend. |
| **qc_Router.md** | engine | Routing engine: backend selection, frame reuse, tier escalation, overflow. |
| **qc_ResonanceFrame.md** | engine | Frame manager: lifecycle, tier monotonicity, backend binding, drift. |
| **qc_Drift.md** | engine | Drift engine: predicted/measured drift, accumulation, overflow. |
| **qc_Transitions.md** | engine | Environment transitions: sandbox → production → archive. |
| **qc_Capture.md** | engine | Append‑only ledger writer: operators, frames, transitions, hash chain. |
| **qc_Replay.md** | engine | Replay verifier: reconstructs session, checks invariants, verifies hashes. |
| **qc_API.md** | signature | Public API surface for sessions, operators, transitions, capture, replay. |
| **qc_Flow.md** | map | Narrative walkthrough of the structural pipeline. |
| **qc_Examples_Minimal.md** | example | Minimal structural examples. |
| **qc_Examples_Advanced.md** | example | Advanced multi‑frame, multi‑transition examples. |
| **qc_Module.json** | manifest | Module identity, file roles, analyzer layers, schema. |

---

# 3. Structural Orientation

qCompute is organized into **five layers**:

### 1. Identity Layer  
Defines what the module *is* and *is not*.

### 2. Operator Layer  
Operators, grammar, validation.

### 3. Dimensional Layer  
Backends, backend profiles.

### 4. Regime Layer  
Routing, frames, drift, transitions.

### 5. Ledger Layer  
Capture + replay.

This structure mirrors the RTT‑Inside architecture.

---

# 4. Learning Path

Recommended reading order:

1. **qc_Identity.md**  
2. **qc_Operators.md**  
3. **qc_OperatorGrammar.md**  
4. **qc_Backends.md**  
5. **qc_Router.md**  
6. **qc_ResonanceFrame.md**  
7. **qc_Drift.md**  
8. **qc_Transitions.md**  
9. **qc_Capture.md**  
10. **qc_Replay.md**  
11. **qc_API.md**  
12. **qc_Examples_Minimal.md**  
13. **qc_Examples_Advanced.md**  
14. **qc_Flow.md**

---

# 5. Summary

qCompute is the **structural compute substrate** of RTT‑Inside.

This index provides:

- orientation  
- file map  
- structural overview  
- learning path  

Use this page as the **front‑door reference** for the entire module.
