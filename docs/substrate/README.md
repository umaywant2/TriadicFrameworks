# Triadic Substrate

<img src="https://img.shields.io/badge/Open%20for%20Traduction-Ready%20for%20Students-4c8eda?style=for-the-badge" alt="Open for Traduction | Ready for Students"/>

The `substrate/` directory contains the core implementation of the Resonance Substrate Model.  
Where the manuscript defines the theory, this directory defines the *runtime substrate* that executes it.

The substrate is organized into three layers:

- **core/** — field definitions, state containers, update loops  
- **operators/** — diffusion, alignment, coupling, activation, stabilization  
- **utils/** — shared helpers, math routines, loaders, schema validators  

This directory is domain‑agnostic.  
All Earth, telescope, or other overlays plug *into* this substrate without modifying it.
