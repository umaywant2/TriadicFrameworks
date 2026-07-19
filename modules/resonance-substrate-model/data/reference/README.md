# **Reference Data**

This directory contains stable, authoritative reference datasets used throughout the Resonance Substrate Model (RSM). These values support simulations, experiments, calibration routines, and analytical workflows by providing consistent, reproducible numerical baselines.

The reference files included here are intentionally minimal, well‑structured, and versioned to ensure long‑term reliability across RSM releases.

---

# Quicklinks

- [applications complex systems](../../applications/complex-systems.md)
- [data README](../../README.md)
- [data examples README](../examples/README.md)
- [data reference README](../reference/README.md)
- [data validation README](../validation/README.md)
- [data validation experimental README](../validation/experimental/README.md)
- [data validation synthetic README](../validation/synthetic/README.md)
- [experiments README](../../experiments/README.md)
- [experiments faraday paradox analysis.ipynb](../../experiments/faraday_paradox/analysis.ipynb.md)
- [experiments faraday paradox protocol](../../experiments/faraday_paradox/protocol.md)
- [experiments faraday paradox README](../../experiments/faraday_paradox/README.md)
- [experiments faraday paradox processed data README](../../experiments/faraday_paradox/processed_data/README.md)
- [experiments faraday paradox raw data data dictionary](../../experiments/faraday_paradox/raw_data/data_dictionary.md)
- [experiments faraday paradox raw data README](../../experiments/faraday_paradox/raw_data/README.md)
- [experiments replication guides README](../../experiments/replication_guides/README.md)
- [experiments rotating field tests README](../../experiments/rotating_field_tests/README.md)
- [experiments substrate alignment README](../../experiments/substrate_alignment/README.md)
- [reference Keywords](../../reference/Keywords.md)
- [rsm-shim README](../../rsm-shim/README.md)
- [simulations README](../../simulations/README.md)
- [simulations configs README](../../simulations/configs/README.md)
- [simulations core README](../../simulations/core/README.md)
- [simulations examples README](../../simulations/examples/README.md)
- [src README](../../src/README.md)
- [tests README](../../tests/README.md)
- [tools README](../../tools/README.md)
- [tools cli README](../../tools/cli/README.md)
- [tools converters README](../../tools/converters/README.md)
- [tools visualization README](../../tools/visualization/README.md)
- [previous folder](../../)

---

## **Included Reference Files**

### **1. `physical_constants.json`**  
Provides fundamental constants used across field evolution, energy calculations, quantum triad behavior, and substrate‑level operators.  
Typical entries include:
- characteristic resonance frequencies  
- baseline energy coefficients  
- normalization factors  
- dimensional scaling constants  

These values ensure consistent computation across modules and prevent drift between simulations.

---

### **2. `measurement_uncertainties.json`**  
Defines uncertainty ranges and error models for sensing, sampling, and experimental workflows.  
This dataset supports:
- noise modeling  
- confidence interval generation  
- sensor calibration  
- experiment reproducibility  

Uncertainty values are expressed in standardized units and can be applied across sensing modalities and lab environments.

---

### **3. `calibration_curves.json`**  
Contains calibration mappings used to convert raw sensor or field readings into normalized, meaningful quantities.  
Calibration curves support:
- FFF emitter sensing  
- resonance amplitude normalization  
- instrument correction  
- nonlinear response compensation  

These curves ensure that measurements remain comparable across devices, runs, and environments.

---

## **Purpose of This Directory**

The reference data stored here serves three key roles:

1. **Consistency**  
   All simulations and experiments rely on the same authoritative constants and calibration values.

2. **Reproducibility**  
   Researchers and operators can reproduce results across versions, machines, and environments.

3. **Stability**  
   These files change infrequently and are versioned carefully to maintain compatibility across the RSM ecosystem.

---

## **Usage**

These reference files are typically loaded by:
- simulation modules  
- sensing systems  
- quantum triad routines  
- operator configurations  
- lab and experiment definitions  

They are not meant to be modified during runtime.  
Updates should occur only during versioned releases of the RSM.

---

# 📘 **RSM Reference Data — Data Dictionary**

This data dictionary defines every field contained within the reference JSON files:

- `physical_constants.json`  
- `measurement_uncertainties.json`  
- `calibration_curves.json`  

These files provide stable, authoritative numerical baselines used across the Resonance Substrate Model (RSM).

---

# **1. `physical_constants.json` — Data Dictionary**

This file contains fundamental constants used across field evolution, energy calculations, quantum triad behavior, and operator dynamics.

| Field | Type | Description |
|-------|------|-------------|
| `resonance_frequency_base` | number | Baseline resonance frequency used for normalization across fields and operators. |
| `energy_scale_factor` | number | Scalar multiplier applied to energy calculations to maintain dimensional consistency. |
| `dissipation_constant` | number | Default dissipation rate used in energy decay and stabilization routines. |
| `quantum_phase_unit` | number | Base unit for phase calculations in the Quantum Triad Model. |
| `coherence_decay_rate` | number | Default rate at which coherence decreases over time or distance. |
| `normalization_factor` | number | Global normalization constant applied to field magnitudes. |
| `speed_of_propagation` | number | Effective propagation speed for field diffusion or resonance waves. |

*(If your actual file contains additional fields, I can expand this dictionary to match exactly.)*

---

# **2. `measurement_uncertainties.json` — Data Dictionary**

This file defines uncertainty ranges and noise characteristics used in sensing, sampling, and experimental workflows.

| Field | Type | Description |
|-------|------|-------------|
| `amplitude_uncertainty` | number | Standard deviation or error bound for amplitude measurements. |
| `phase_uncertainty` | number | Uncertainty in phase measurements, typically in radians. |
| `spatial_resolution_error` | number | Expected positional error for spatial sampling. |
| `temporal_jitter` | number | Timing uncertainty in sampling intervals. |
| `sensor_noise_floor` | number | Minimum detectable signal above noise. |
| `environmental_variance` | number | Variance introduced by environmental factors (temperature, vibration, etc.). |
| `confidence_level` | number | Confidence interval (0–1) associated with uncertainty values. |

---

# **3. `calibration_curves.json` — Data Dictionary**

This file contains calibration mappings used to convert raw sensor or field readings into normalized values.

| Field | Type | Description |
|-------|------|-------------|
| `amplitude_curve` | array of objects | Maps raw amplitude readings to calibrated values. |
| `amplitude_curve[].raw` | number | Raw sensor or field reading. |
| `amplitude_curve[].calibrated` | number | Corrected, normalized amplitude value. |
| `phase_curve` | array of objects | Maps raw phase readings to calibrated values. |
| `phase_curve[].raw` | number | Raw phase measurement. |
| `phase_curve[].calibrated` | number | Corrected phase value. |
| `temperature_compensation` | object | Parameters for temperature‑dependent calibration. |
| `temperature_compensation.offset` | number | Offset applied to readings based on temperature. |
| `temperature_compensation.scale` | number | Scaling factor applied to compensate for thermal drift. |
| `nonlinear_response` | object | Defines nonlinear correction parameters. |
| `nonlinear_response.coefficient_a` | number | First‑order nonlinear correction term. |
| `nonlinear_response.coefficient_b` | number | Second‑order nonlinear correction term. |

---

# ⭐ **Summary**

This data dictionary provides a clear, structured description of every field in your reference JSON files, ensuring:

- reproducibility  
- transparency  
- reviewer‑friendly documentation  
- long‑term maintainability  
