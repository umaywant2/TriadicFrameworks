# Biology core problem solutions

## Solution to Problem 1 – Resonant cell growth

We are given



$$
G(t) = G_0 e^{D_3 τ_r t}
$$



The “growth factor” at time $$t$$ is



$$
F(t) = e^{D_3 τ_r t}
$$



If $$τ_r$$ is increased by 10%, then



$$
τ_r' = 1.1τ_r
$$



The new growth factor is



$$
F'(t) = e^{D_3 τ_r' t} = e^{D_3 (1.1τ_r) t} = e^{1.1 D_3 τ_r t}
$$



We can express this in terms of the original factor $$F(t)$$:



$$
F'(t) = \left(e^{D_3 τ_r t}\right)^{1.1} = \left(F(t)\right)^{1.1}
$$



So the factor by which the growth factor changes is



$$
\frac{F'(t)}{F(t)} = e^{(1.1 - 1) D_3 τ_r t} = e^{0.1 D_3 τ_r t}
$$



**Answer:** At fixed $$t$$, the growth factor is multiplied by $$e^{0.1 D_3 τ_r t}$$, equivalently $$F'(t) = F(t)^{1.1}$$

---

## Solution to Problem 2 – Protein folding stability under environmental resonance

Protein stability is modeled as



$$
P = \frac{ΛΘ}{D_9}
$$



We want to keep $$P$$ constant while $$D_9$$ changes. Let the new destabilizing factor be $$D_9'$$ and the new temperature parameter be $$Θ'$$ Constancy of $$P$$ means



$$
\frac{ΛΘ}{D_9} = \frac{ΛΘ'}{D_9'}
$$



We can cancel $$Λ$$ (assumed unchanged):



$$
\frac{Θ}{D_9} = \frac{Θ'}{D_9'}
$$



Solving for $$Θ'$$:



$$
Θ' = Θ \cdot \frac{D_9'}{D_9}
$$



**Answer:** $$Θ$$ must be scaled in direct proportion to the change in $$D_9$$, i.e. $$Θ' = Θ \cdot \dfrac{D_9'}{D_9}$$

---

## Solution to Problem 3 – Neural oscillation coupling

The neural resonance frequency is



$$
f_n = T_f D_6
$$



We assume $$D_6$$ is fixed. Let the required new frequency be $$f_n' = 1.15 f_n$$ (a 15% increase). Then



$$
f_n' = T_f' D_6 = 1.15 f_n = 1.15 T_f D_6
$$



Since $$D_6$$ is unchanged, we can divide both sides by $$D_6$$:



$$
T_f' = 1.15 T_f
$$



**Answer:** $$T_f$$ must be increased by 15% (multiplied by 1.15).
