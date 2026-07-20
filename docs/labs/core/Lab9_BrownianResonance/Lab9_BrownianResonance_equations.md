# Lab 9: Brownian Resonance — Equations

## Purpose
To formalize the stochastic and harmonic behavior of Brownian motion within triadic systems, revealing how noise can amplify signal through resonance.

## Key Equations

### 1. Brownian Displacement
$$
\Delta x(t) = \sqrt{2 D t}
$$
Where \( D \) is the diffusion coefficient and \( t \) is time.

### 2. Resonant Noise Amplification
$$
A(t) = \eta(t) \cdot \sin(\omega t)
$$
Where \( \eta(t) \) is stochastic noise and \( \omega \) is the resonance frequency.

### 3. Triadic Brownian Resonance
$$
R_B(t) = \int_{0}^{t} A(t) \cdot R_{ijk} \, dt
$$
Where \( R_{ijk} \) is triadic resonance.

### 4. Signal-to-Noise Ratio (SNR)
$$
\text{SNR} = \frac{\langle R_B(t)^2 \rangle}{\langle \eta(t)^2 \rangle}
$$
Measures the amplification of signal over noise.

## Symbol Legend

| Symbol       | Meaning                                |
|--------------|----------------------------------------|
| \( \Delta x(t) \) | Brownian displacement             |
| \( D \)       | Diffusion coefficient                 |
| \( \eta(t) \) | Stochastic noise                      |
| \( \omega \)  | Resonance frequency                   |
| \( R_B(t) \)  | Brownian resonance                    |
| \( R_{ijk} \) | Triadic resonance                     |
| SNR          | Signal-to-noise ratio                  |
