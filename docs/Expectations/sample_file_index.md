# **Sample File Index — Expectations Module**  
**TriadicFrameworks Canon**  
**Location:** `/docs/Expectations/`  
**Role:** Directory map for all sample files supporting the Expectations module  
**Version:** 2026‑1.0  

---

## **Purpose**

This index provides a **clear, navigable list of sample files** included in the Expectations module.  
These samples demonstrate:

- intake manifolds  
- output headers  
- engine block structure  
- substrate engines  
- observer bundles  
- cross‑domain examples  
- research‑grade profiles (HPC, QC, Medicine)

They serve as **starter references** for students, researchers, and AI agents.

---

# **1. Intake Manifold Samples**  
**Directory:** `/docs/Expectations/samples/intake_manifolds/`

| File | Description |
|------|-------------|
| `sim_intake.svg` | Single Intake Manifold (1 triad) |
| `dim_intake.svg` | Double Intake Manifold (2 triads / 1 hex) |
| `tim_intake.svg` | Triple Intake Manifold (3 triads) |
| `qim_intake.svg` | Quad Intake Manifold (full IPD‑12) |
| `fsi_intake.svg` | Full 12‑Stack Intake (3×QIM) |

These files demonstrate how external frameworks enter the IPD‑12 engine.

---

# **2. Header Manifold Samples**  
**Directory:** `/docs/Expectations/samples/header_manifolds/`

| File | Description |
|------|-------------|
| `rtt_header.svg` | RTT output header |
| `gu_header.svg` | GU output header |
| `fft_header.svg` | FFT output header |
| `pantheon_header.svg` | Pantheon output header |
| `dimensional_header.svg` | Pure dimensional header |
| `substrate_header.svg` | Raw substrate header |
| `observer_header.svg` | Observer bundle header |
| `h_med_header.svg` | Medical header (risk/progression/intervention/targets) |

These illustrate how IPD‑12 produces structured outputs.

---

# **3. Engine Block Samples**  
**Directory:** `/docs/Expectations/samples/engine_block/`

| File | Description |
|------|-------------|
| `ipd12_engine_block.svg` | Full IPD‑12 engine block diagram |
| `engine_block.md` | Engine block specification (ports, feeds, rails, loops, headers) |

These files show the internal architecture of the IPD‑12 engine.

---

# **4. Prime‑State Samples**  
**Directory:** `/docs/Expectations/samples/prime_states/`

| File | Description |
|------|-------------|
| `prime_state_index.md` | List of all prime‑indexed states (P2–P37) |
| `prime_state_icons.svg` | Icon atlas for prime states |

These help students and AIs identify prime‑indexed operators.

---

# **5. HPC+QC Substrate Engine Samples**  
**Directory:** `/docs/Expectations/samples/hpc_qc_substrate/`

| File | Description |
|------|-------------|
| `hpc_qc_substrate_engine.md` | Hybrid HPC+QC substrate engine profile |
| `qc_calibration_observer_map.md` | Mapping calibration/telemetry → observer rails |
| `hpc_qc_intake_examples.md` | Example hybrid workflows (SIM–FSI) |

These files demonstrate how IPD‑12 models hybrid HPC+QC systems.

---

# **6. Observer Overhead & Gain Samples**  
**Directory:** `/docs/Expectations/samples/observer_overhead/`

| File | Description |
|------|-------------|
| `observer_overhead_gain_spec.md` | Overhead vs gain across HPC, QC, Medicine |
| `observer_cost_table.md` | Manifold‑level overhead table |
| `observer_gain_table.md` | Manifold‑level gain table |

These support performance and research evaluation.

---

# **7. Cross‑Domain Examples**  
**Directory:** `/docs/Expectations/samples/cross_domain/`

| File | Description |
|------|-------------|
| `physics_to_medicine.md` | Mapping GU/RTT → computational medicine |
| `qc_to_hpc.md` | Mapping QC → HPC via substrate engines |
| `fft_to_fcg.md` | Mapping FFT → FCG for framework creation |
| `rf_builder_examples.md` | Regime‑Field Builder examples |

These demonstrate TriadicFrameworks’ cross‑domain power.

---

# **8. Meta Files**

| File | Description |
|------|-------------|
| `Expectations.md` | Main Expectations module document |
| `e_Capture.md` | Capture document for the Expectations module |
| `module.json` | Canon metadata for the Expectations module |
| `README.md` | Overview for `/docs/Expectations/` |

---

## **Notes**

- All sample files follow TriadicFrameworks canon formatting.  
- SVGs are GitHub‑safe (single root, no external references).  
- Markdown files follow the triadic lens and module grammar.  
- This index updates automatically as new samples are added.
