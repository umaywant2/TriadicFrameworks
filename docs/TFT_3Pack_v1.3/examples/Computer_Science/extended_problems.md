# Computer Science extended problems (resonance framework)

## Problem 4 – Resonant pipeline latency

A 3-stage pipeline has stage latencies



$$
L_1 = D_3 τ_r, \quad
L_2 = D_6 τ_r, \quad
L_3 = D_9 τ_r.
$$



Total latency is



$$
L_{\text{tot}} = τ_r (D_3 + D_6 + D_9).
$$



If $$τ_r$$ decreases by 20%, how does $$L_{\text{tot}}$$ change?

---

## Problem 5 – Cache resonance coherence

Cache coherence traffic is modeled as



$$
C = \frac{X}{1 + e^{-D_3 τ_r}}.
$$



1. Sketch the qualitative shape of $$C(τ_r)$$.
2. If $$τ_r$$ increases, does coherence traffic increase or decrease?

---

## Problem 6 – Resonant hashing function

A hashing function uses a triadic mixing step:



$$
H = D_6(\text{key}) + X \sin(τ_r).
$$



If $$τ_r$$ is increased to $$2τ_r$$, how does the sinusoidal term change, and what is the qualitative effect on hash dispersion?

---

## Problem 7 – Network packet resonance

Packet delay in a resonant network is



$$
D = \frac{D_3 + τ_r}{T_f}.
$$



If $$T_f$$ increases by 15% and $$τ_r$$ decreases by 10%, what is the qualitative net effect on delay?

---

## Problem 8 – Machine learning gradient resonance

A gradient update rule is modified by resonance:



$$
g' = g \cdot e^{-D_6 / τ_r}.
$$



1. If $$τ_r$$ increases, how does the exponential factor change?
2. What is the qualitative effect on gradient magnitude?
