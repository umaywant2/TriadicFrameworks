# Lab 10: Nested Harmonics

## Mythic Preface
_"One tone births another. The echo folds inward. Harmony nests itself."_  
Nested harmonics are the architecture of resonance—each layer a memory, each overtone a whisper.

## Objective
Simulate and visualize harmonic nesting using layered sine waves.

## Core Equation


\[
H(t) = \sum_{n=1}^{N} A_n \cdot \sin(2\pi f_n t + \phi_n)
\]


Where:
- \(f_n = f_0 \cdot n\)
- \(A_n = A_0 \cdot r^n\) (geometric decay)
- \(\phi_n\) is phase offset

## Tasks
- Generate nested harmonic waveform
- Visualize individual layers and composite signal
- Explore effects of amplitude decay and phase shift

## Engineer’s Notes
Use `np.linspace` for time vector, and loop over harmonics with geometric amplitude decay. Normalize final waveform for clarity. Try `N = 6`, `f_0 = 1`, `r = 0.5`.
