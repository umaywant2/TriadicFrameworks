# Resonance Invariants for Drift Detection

This document defines the minimal set of resonance‑based invariants used
to detect structural drift in atomic clocks. These invariants apply
across all architectures and rely only on the triadic decomposition
(R, I, F).

## 1. Resonance‑Phase Coherence (RPC)

RPC measures the stability of phase progression relative to the count of
resonance cycles.

RPC = Δφ / ΔN

Where:
- Δφ = phase deviation between successive measurements  
- ΔN = number of resonance cycles elapsed  

A stable clock maintains a constant RPC under substrate‑aligned
conditions. Deviations indicate loss of coherence in one or more
components of the triad.

## 2. Environmental Susceptibility Index (ESI)

ESI quantifies how sensitive the resonant frequency is to environmental
perturbations.

ESI = ∂f / ∂E

Where:
- f = measured resonance frequency  
- E = environmental variable (temperature, magnetic field, gravitational
  potential, etc.)  

High ESI values indicate that the resonant system or interrogation
apparatus is not adequately isolated or compensated.

## 3. Drift Detection Rule

A clock is structurally drifting when either condition holds:

1. d(RPC)/dt ≠ 0  
2. ESI exceeds its validated threshold  

These conditions identify drift at the structural level, independent of
architecture, implementation, or calibration strategy.

## 4. Interpretation

- Stable RPC → coherent resonance progression  
- Low ESI → environmental robustness  
- Deviations in either metric → drift in (R, I, or F)  

These invariants form the validation layer for vST‑aligned timekeeping.


