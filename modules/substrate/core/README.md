# Substrate Core

The `core/` directory contains the fundamental runtime components:

- field containers (`phi`, `V`, `R`)
- timestep integrators
- operator pipelines
- simulation loop orchestration
- state serialization and snapshotting

This is the execution engine of the Resonance Substrate Model.  
All overlays (Earth, telescopes, etc.) map their domain data into these core structures.
