# Data Dictionary — Faraday Paradox Raw Data

This document defines the fields used in the raw CSV files for the Faraday Paradox experimental series.

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
