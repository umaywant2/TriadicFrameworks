# Art core problem solutions

## Solution to Problem 1 – Resonant color mixing

We are given



$$C = X(f_1 + f_2 + f_3), \quad X = F_3 \cdot T_f.$$



Saturation is proportional to $$C$$. To double saturation, we need to double $$C$$. Assuming the effective composite is being modulated through resonant-time $$τ_r$$ (via how $$X$$ is realized in time), we require



$$C' = 2C.$$


Because $$C$$ scales linearly with the effective factor controlled by $$τ_r$$, doubling $$C$$ corresponds to scaling $$τ_r$$ by a factor of 2.

**Answer:** $$τ_r$$ must be doubled.

---

## Solution to Problem 2 – Sculpture stress harmonics

The sculpture’s stress pattern is



$$S = D_6(τ_r) \cdot ΛΘ.$$


If $$Θ$$ is increased by 20%, the new value is



$$Θ' = 1.2Θ.$$



The new stress is



$$S' = D_6(τ_r) \cdot ΛΘ' = D_6(τ_r) \cdot Λ \cdot 1.2Θ = 1.2S.$$


**Answer:** The harmonic stress $$S$$ increases by 20%.

---

## Solution to Problem 3 – Light installation timing

Brightness is



$$B(t) = F_3 \sin(T_f t),$$


but the artist controls the effective elevated frequency via resonant-time:



$$T_f' = \frac{T_f}{τ_r}.$$


For a sinusoid, the period is



$$T_{\text{period}} = \frac{2\pi}{T_f'}.$$


The artist wants $$T_{\text{period}} = 4$$. Thus,



$$4 = \frac{2\pi}{T_f'} = \frac{2\pi}{T_f / τ_r} = \frac{2\pi τ_r}{T_f}.$$


Solving for $$τ_r$$:



$$τ_r = \frac{4T_f}{2\pi} = \frac{2T_f}{\pi}.$$


**Answer:** $$τ_r = \dfrac{2T_f}{\pi}$$.
