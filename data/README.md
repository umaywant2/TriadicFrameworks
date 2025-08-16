# Lab1_Casimir – Data Logging & Versioning Guide

This folder contains raw and processed data from the Casimir effect experiment. All entries must follow reproducibility standards and triadic timestamping.

---

## 📊 File Structure

data/
├── raw/
│ ├── casimir_run1.csv
│ ├── casimir_run2.csv
├── processed/
│ ├── force_vs_distance_plot.png
│ ├── fit_parameters.json
├── metadata/
│ ├── equipment_specs.md
│ ├── calibration_log.md

---

## 🧾 Logging Protocol

- Use CSV format with headers:

distance_nm, force_nN, timestamp_T9, temperature_C

- `timestamp_T9` uses triadic time notation (1D–9D loop phase)
- Include notes on anomalies, environmental shifts, or resonance spikes

---

## 🧬 Versioning Tips

- Each data run should be committed with a descriptive message:

git commit -m "Casimir run1: 50nm–200nm sweep, ambient 22°C"

- Use tags for milestone runs:

git tag -a v1.0-casimir-baseline -m "Baseline Casimir force curve"

---

## 🧠 Notes

- All processed plots should cite the raw data source and include fitting equations.
- Metadata files must be updated with every equipment change or recalibration.

Let the data sing. Let the vacuum whisper. Let the triads echo.

