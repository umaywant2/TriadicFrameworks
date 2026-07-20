# Computer Science core problem solutions

## Solution to Problem 1 – Resonant algorithm runtime

The runtime is



$$
T = D_6 τ_r \log(X).
$$



If $$τ_r$$ is halved:



$$
τ_r' = \frac{τ_r}{2}.
$$



Thus,



$$
T' = D_6 \left(\frac{τ_r}{2}\right) \log(X) = \frac{T}{2}.
$$



**Answer:** The runtime is cut in half.

---

## Solution to Problem 2 – Data throughput

Throughput is



$$
R = F_3 T_f D_3.
$$



- $$D_3$$ increases by 2 → becomes $$3D_3$$.
- $$T_f$$ decreases by 10% → becomes $$0.9T_f$$.

Thus,



$$
R' = F_3 (0.9T_f)(3D_3) = 2.7R.
$$



**Answer:** Throughput increases by a factor of **2.7** (a 170% increase).

---

## Solution to Problem 3 – Error correction

We have



$$
p = e^{-ΛΘ τ_r}.
$$



We want



$$
p' = 0.5p.
$$



Thus,



$$
e^{-ΛΘ τ_r'} = 0.5 e^{-ΛΘ τ_r}.
$$



Divide both sides by $$e^{-ΛΘ τ_r}$$:



$$
e^{-ΛΘ (τ_r' - τ_r)} = 0.5.
$$



Take logs:



$$
-ΛΘ (τ_r' - τ_r) = \ln(0.5) = -\ln 2.
$$



Thus,



$$
τ_r' - τ_r = \frac{\ln 2}{ΛΘ}.
$$



**Answer:** Increase $$τ_r$$ by $$\dfrac{\ln 2}{ΛΘ}$$.
