# Phase III UV/THz Atlas Schema

## Arrays

- uv_amplitude[N, H, W]
- uv_phase[N, H, W]
- thz_amplitude[N, H, W]
- thz_phase[N, H, W]
- confidence[N, H, W]

## Metadata

- f_uv
- f_thz
- pulse_widths
- safety_flags
- PLL_status

## Notes

Schema for storing UV/THz strobe atlases in NPZ/HDF5 format.
