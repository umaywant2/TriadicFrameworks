# Biology extended problems (resonance framework)

## Problem 4 – Resonant competition between two species

Two microbial species, A and B, share a nutrient source. Their populations are modeled as



$$
A(t) = A_0 e^{D_3 τ_r t}, \quad
B(t) = B_0 e^{D_6 τ_r t},
$$



with $$D_6 > D_3$$, and the same environmental resonant-time $$τ_r$$.

1. Derive an expression for the time $$t^*$$ at which $$B(t) = A(t)$$.
2. If $$τ_r$$ is decreased (shorter environmental cycles), what happens qualitatively to $$t^*$$: does B overtake A earlier or later?

---

## Problem 5 – Enzyme activity and resonance “temperature”

Enzyme activity is modeled by a resonance-like relationship



$$
E_{\text{act}} = X e^{-1/(ΛΘ)},
$$



where $$X = F_3 \cdot T_f$$ captures frequency-elevated catalytic capacity, and $$ΛΘ$$ encodes the effective “temperature resonance” of the enzyme.

1. If $$Λ$$ doubles, how does the exponent $$-1/(ΛΘ)$$ change?
2. Does this increase or decrease the value of $$E_{\text{act}}$$?

---

## Problem 6 – Circadian rhythm entrainment

A set of cells maintains a circadian rhythm modeled by a phase $$\phi(t)$$ that advances with an effective frequency



$$
\omega_{\text{eff}} = \frac{T_f}{τ_r},
$$



where $$T_f$$ depends on a light cue and $$τ_r$$ encodes internal resonant-time of the clock.

The target period is 24 hours, so the desired effective frequency is $$\omega_{\text{target}} = 2\pi / 24$$.

1. Write the equation relating $$T_f$$, $$τ_r$$, and $$\omega_{\text{target}}$$.
2. If $$τ_r$$ is fixed, what value of $$T_f$$ is needed to maintain a 24-hour period?

---

## Problem 7 – Population carrying capacity under triadic regulation

A population grows according to



$$
N(t) = \frac{K}{1 + e^{-D_3 (t - τ_r)}},
$$



where $$K$$ is carrying capacity and $$τ_r$$ sets the resonant-time of the midpoint of growth.

1. What is $$N(τ_r)$$ in terms of $$K$$?
2. If $$τ_r$$ increases, how does the timing of the transition to rapid growth (near the midpoint) shift?

---

## Problem 8 – Signal cascade resonance in a pathway

A three-step signaling cascade has activity levels $$S_1, S_2, S_3$$ modeled as



$$
S_1 = F_3, \quad
S_2 = D_3(τ_r) S_1, \quad
S_3 = T_f S_2.
$$



The output activity is $$S_{\text{out}} = S_3$$. Suppose the cell adapts to a new environment by decreasing $$τ_r$$ by 20% and increasing $$T_f$$ by 30%.

1. Express the ratio $$S_{\text{out}}'/S_{\text{out}}$$ in terms of the scaling of $$D_3(τ_r)$$ with $$τ_r$$.
2. Assuming $$D_3(τ_r)$$ is approximately proportional to $$τ_r$$, compute the net approximate change in $$S_{\text{out}}$$.
