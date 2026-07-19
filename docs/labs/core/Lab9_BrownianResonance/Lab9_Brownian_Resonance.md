# Lab 9: Brownian Resonance

## Mythic Preface
_"Chaos dances. Harmony listens. Resonance emerges."_  
Brownian motion is the whisper of entropy. Overlay it with rhythm, and you hear the cosmos breathe.

## Objective
Simulate Brownian motion and overlay harmonic resonance.

## Core Equations
Brownian path:


\[
x(t) = x_0 + \sum_{i=1}^{n} \Delta x_i
\]


Resonance overlay:


\[
R(t) = x(t) \cdot \sin(2\pi f t)
\]



## Tasks
- Generate Brownian path
- Apply sinusoidal overlay
- Visualize resonance emergence

## Engineer’s Notes
Use `np.cumsum(np.random.normal(...))` for Brownian path. Choose `f = 0.1` for slow resonance. Normalize for clarity.
