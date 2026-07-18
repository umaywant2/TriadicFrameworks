# Data Dictionary — Faraday Paradox Raw Data

This document defines the fields used in the raw CSV files for the Faraday Paradox experimental series.

---

# Quicklinks

- [applications complex systems](../../../applications/complex-systems.md)
- [data README](../../../data/README.md)
- [data examples README](../../../data/examples/README.md)
- [data reference README](../../../data/reference/README.md)
- [data validation README](../../../data/validation/README.md)
- [data validation experimental README](../../../data/validation/experimental/README.md)
- [data validation synthetic README](../../../data/validation/synthetic/README.md)
- [experiments README](../../README.md)
- [experiments faraday paradox analysis.ipynb](../analysis.ipynb.md)
- [experiments faraday paradox protocol](../protocol.md)
- [experiments faraday paradox README](../README.md)
- [experiments faraday paradox processed data README](../processed_data/README.md)
- [experiments faraday paradox raw data README](README.md)
- [experiments replication guides README](../../replication_guides/README.md)
- [experiments rotating field tests README](../../rotating_field_tests/README.md)
- [experiments substrate alignment README](../../substrate_alignment/README.md)
- [reference Keywords](../../../reference/Keywords.md)
- [rsm-shim README](../../../rsm-shim/README.md)
- [simulations README](../../../simulations/README.md)
- [simulations configs README](../../../simulations/configs/README.md)
- [simulations core README](../../../simulations/core/README.md)
- [simulations examples README](../../../simulations/examples/README.md)
- [src README](../../../src/README.md)
- [tests README](../../../tests/README.md)
- [tools README](../../../tools/README.md)
- [tools cli README](../../../tools/cli/README.md)
- [tools converters README](../../../tools/converters/README.md)
- [tools visualization README](../../../tools/visualization/README.md)
- [previous folder](../)

---

## Fields

### `timestamp`
- **Type:** number  
- **Units:** seconds or simulation steps  
- **Description:** Monotonically increasing time index for each measurement.

### `rotation_rate`
- **Type:** number  
- **Units:** radians/second (or simulation‑defined units)  
- **Description:** Angular velocity of the rotating magnetic field source.

### `induced_signal`
- **Type:** number  
- **Units:** volts (physical) or arbitrary substrate units (simulation)  
- **Description:** Measured EMF or substrate‑analog response at the given timestamp.

### `field_alignment`
- **Type:** number  
- **Units:** dimensionless (0–1 recommended)  
- **Description:** Optional metric representing spin‑field or resonance alignment.

### `notes`
- **Type:** string  
- **Description:** Optional annotations for anomalies, calibration steps, or operator comments.

## Notes
- All fields are raw and unprocessed.  
- Derived metrics (e.g., smoothed signals, envelope activation) belong in processed datasets, not here.
