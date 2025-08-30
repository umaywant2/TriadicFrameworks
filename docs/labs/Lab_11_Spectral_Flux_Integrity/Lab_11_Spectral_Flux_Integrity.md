# Lab 11: Spectral Flux Integrity

## Mythic Preface
_"The spectrum speaks. Integrity listens. Flux reveals the truth."_  
Spectral flux integrity is the heartbeat of signal coherence—tracking how energy shifts across dimensions.

## Objective
Simulate multi-band spectral signals and compute flux integrity over time.

## Core Equation


\[
\Phi(t) = \frac{d}{dt} \left[ \sum_{i=1}^{N} S_i(t)^2 \right]
\]


Where:
- \(S_i(t)\) are spectral components
- \(\Phi(t)\) measures flux integrity

## Tasks
- Generate N sinusoidal signals with varying frequency and phase
- Compute instantaneous spectral energy
- Derive flux integrity using time gradient
- Visualize energy and flux over time

## Engineer’s Notes
Use `np.gradient()` for time derivative. Normalize each \(S_i(t)\) before squaring. Try `N = 5`, `f_i = 0.5 + 0.2*i`, and phase offsets \(\phi_i = \pi/i\).
