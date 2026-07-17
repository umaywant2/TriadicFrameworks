substrate 
# Triadic Substrate

The `substrate/` directory contains the core implementation of the Resonance Substrate Model.  
Where the manuscript defines the theory, this directory defines the *runtime substrate* that executes it.

The substrate is organized into three layers:

- **core/** — field definitions, state containers, update loops  
- **operators/** — diffusion, alignment, coupling, activation, stabilization  
- **utils/** — shared helpers, math routines, loaders, schema validators  

This directory is domain‑agnostic.  
All Earth, telescope, or other overlays plug *into* this substrate without modifying it.
# Substrate Core

The `core/` directory contains the fundamental runtime components:

- field containers (`phi`, `V`, `R`)
- timestep integrators
- operator pipelines
- simulation loop orchestration
- state serialization and snapshotting

This is the execution engine of the Resonance Substrate Model.  
All overlays (Earth, telescopes, etc.) map their domain data into these core structures.
# Operator System

The `operators/` directory implements the five operator families defined in the manuscript:

- **Diffusion**  
- **Alignment**  
- **Coupling**  
- **Activation**  
- **Stabilization**

Each operator acts on one or more of the triadic fields:

- scalar field `phi`
- vector field `V`
- resonance envelope `R`

Operators are pure functions:  
they take field states + coefficients and return updated fields.  
This keeps the substrate modular, testable, and easy to extend.
# Substrate Utilities

The `utils/` directory provides shared helper functions used across the substrate:

- numerical routines (gradients, Laplacians, normalization)
- coherence functional helpers
- logistic and nonlinear activation helpers
- schema validation utilities
- configuration loaders
- grid and mesh utilities

These utilities are intentionally lightweight and dependency‑minimal.  
They support the operator system without imposing domain assumptions.
