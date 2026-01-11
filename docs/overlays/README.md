# Domain Overlays

The `overlays/` directory contains domain‑specific extensions of the Resonance Substrate Model.

Each overlay provides:

- a domain‑specific schema  
- transforms that map real‑world data into triadic fields  
- examples demonstrating usage  
- optional domain‑specific operators or metrics  

Current overlays:

- **earth/** — geophysical and climate‑model field transforms  
- **telescopes/** — multi‑instrument observational coherence transforms

Overlays do *not* modify the substrate.  
They sit on top of it, mapping domain data into the triadic field architecture.
