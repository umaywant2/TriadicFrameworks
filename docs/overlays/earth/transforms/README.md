# Earth Transforms

The `transforms/` directory contains functions that convert Earth simulation data
(NetCDF, HDF5, gridded fields) into triadic fields:

- scalar extraction and normalization  
- vector field extraction and rotation handling  
- coherence functional computation  
- resonance envelope initialization and update  

Transforms are designed to be composable and schema‑driven.
