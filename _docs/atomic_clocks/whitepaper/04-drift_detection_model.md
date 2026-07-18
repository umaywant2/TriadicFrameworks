# Drift‑Detection Model

Atomic clocks maintain stability by preserving coherence across the
triad: the resonant system (R), the interrogation system (I), and the
feedback system (F). Drift occurs when coherence is lost in any
component of the triad, causing the measured frequency or phase to
deviate from its validated resonance behavior. This section defines a
minimal, architecture‑independent drift‑detection model based on
resonance invariants.

## 1. Resonance‑Phase Coherence (RPC)

Resonance‑phase coherence measures the stability of phase progression
relative to the count of resonance cycles. It is defined as:

RPC = Δφ / ΔN

Where:
- Δφ = phase deviation between successive measurements  
- ΔN = number of resonance cycles elapsed  

A stable clock maintains a constant RPC under substrate‑aligned
conditions. Deviations indicate loss of coherence in R, I, or F.

RPC is sensitive to:
- interrogation errors  
- cavity drift  
- servo instability  
- environmental perturbations  
- frequency pulling  

## 2. Environmental Susceptibility Index (ESI)

The environmental susceptibility index quantifies how strongly the
resonant frequency responds to external variables. It is defined as:

ESI = ∂f / ∂E

Where:
- f = measured resonance frequency  
- E = environmental variable (temperature, magnetic field, gravitational
  potential, etc.)  

High ESI values indicate that the resonant system or interrogation
apparatus is not adequately isolated or compensated.

ESI captures:
- thermal sensitivity  
- magnetic field coupling  
- blackbody radiation shifts  
- gravitational potential differences  
- local environmental drift  

## 3. Structural Drift Condition

A clock is structurally drifting when either condition holds:

1. d(RPC)/dt ≠ 0  
2. ESI exceeds its validated threshold  

These conditions identify drift at the structural level, independent of
architecture, implementation, or calibration strategy.

## 4. Interpretation

- **Stable RPC + low ESI**  
  The clock is structurally aligned. Resonance cycles accumulate
  coherently, and environmental coupling is suppressed.

- **RPC deviation**  
  Indicates loss of coherence in interrogation or feedback systems.

- **High ESI**  
  Indicates environmental sensitivity or insufficient compensation.

- **Both conditions violated**  
  Indicates systemic drift affecting multiple components of the triad.

## 5. Role in vST

These invariants form the validation layer for vST‑aligned timekeeping.
They provide a unified method for comparing architectures, diagnosing
drift, and evaluating stability without relying on architecture‑specific
corrections or empirical models.
