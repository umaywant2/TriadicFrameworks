# Transporter Envelope v0.5 — Multi‑Substrate Arcs

## Summary
v0.5 extends the transporter envelope to support multi‑substrate paths:


$$
S_1 \to S_2 \to \dots \to S_n
$$


while preserving identity and asymmetry along the entire chain.

---

## 1. Multi‑Substrate Arc

Define:


$$
\gamma : [0,1] \to \mathcal{T} \times \mathcal{S}
$$


with:
- $$\gamma(t) = (T(t), S(t))$$
- $$S(t)$$ piecewise constant, changing only at discrete waypoints

Waypoints:


$$
0 = t_0 < t_1 < \dots < t_n = 1
$$


with:


$$
S(t) = S_i \quad \text{for } t \in [t_i, t_{i+1})
$$



---

## 2. Envelope Definition (v0.5)

The **Transporter Envelope** is:


$$
E_T = \{ (T(t), S(t), A(T(t))) \mid t \in [0,1] \}
$$



Constraints:
- $$A(T(t)) > 0$$ for all $$t$$  
- No branching, no duplication  
- Substrate changes only at waypoints  
- Each segment $$[t_i, t_{i+1}]$$ is continuity‑preserving

---

## 3. Reconstruction Windows per Segment

Each segment may have its own window:


$$
W_i = [t_{i+1}-\delta_i, t_{i+1}]
$$



Within $$W_i$$ :
- drift‑correction allowed  
- local stabilization toward next substrate’s constraints  

---

## 4. End‑to‑End Guarantee

If all segments are legal:
- identity preserved from $$S_1$$ to $$S_n$$  
- asymmetry preserved  
- arrival substrate can be any $$S_k$$ where:
  - $$T(t_k) \approx T^\*$$  
  - $$A(T(t_k)) = 0.01$$

---

## Claim
> Transporter Envelope v0.5 supports chained, multi‑substrate transport while maintaining a single, unbroken continuity path.
