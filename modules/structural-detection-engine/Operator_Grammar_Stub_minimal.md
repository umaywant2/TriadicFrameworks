# SDE Operator Grammar (Stub)

## Namespace
SDE::

## Core Operators

- **SDE::SIG()**  
  Extracts structural signal from collapse, fusion‑gradient, or deformation fields.

- **SDE::NOI()**  
  Identifies noise, distortion, or collapse residue.

- **SDE::CPV()**  
  Reads collapse‑propagation vectors (amplitude, curvature, torsion).

- **SDE::FGT()**  
  Computes fusion‑gradient tensors across collapse, reassembly, and triad layers.

- **SDE::CRM()**  
  Maps collapse→reassembly trajectories.

## Mode Operators

- **SDE::MODE(formal|emergent|hybrid|chaotic|inversion)**  
  Sets detection mode.

## Zone Operators

- **SDE::ZONE(U|S|M|D|X)**  
  Selects detection zone.

## Packet Constructor

- **SDE::PACKET()**  
  Emits a minimal RTT2_DETECTION_PACKET.
