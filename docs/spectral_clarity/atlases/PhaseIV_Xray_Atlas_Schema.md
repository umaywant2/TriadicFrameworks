# Phase IV X-ray Atlas Schema

## Arrays

- xray_amplitude[N, H, W]
- xray_phase[N, H, W]
- confidence[N, H, W]

## Metadata

- f_xray
- pulse_width
- facility_sync_clock
- safety_flags

## Notes

Schema for storing X-ray strobe atlases in NPZ/HDF5 format.
