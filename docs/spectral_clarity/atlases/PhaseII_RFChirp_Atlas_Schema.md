# Phase II RF/Chirp Atlas Schema

## Arrays

- rf_quadrature[N, H, W]
- rf_phase_bins[N]
- chirp_phase[N, H, W]
- confidence[N, H, W]

## Metadata

- f_rf
- chirp_start
- chirp_end
- chirp_rate
- PLL_status

## Notes

Schema for storing RF lock-in and chirp scan atlases in NPZ/HDF5 format.
