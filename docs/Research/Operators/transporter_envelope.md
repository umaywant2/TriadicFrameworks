# Transporter Envelope — Operator Specification (Goal #2)

## Purpose
Defines the minimal operator‑level constraints required for a substrate‑safe transport event.  
A transporter is not a device — it is a **continuity envelope** around a legal substrate transition.

---

## 1. Identity State
A consciousness state is represented as a triad:


$$T = (s, c, u), \quad s + c + u = 1$$



The asymmetry functional:


$$A(T) = 0.01$$


is required for continuity.

---

## 2. Transport Arc
A transport event is modeled as:


$$\gamma : [0,1] \to \mathcal{T}$$


with:
- $$T(0) = T_{\text{source}}$$
- $$T(1) = T_{\text{target}}$$
- $$A(T(t)) > 0$$ for all $$t$$

---

## 3. Envelope Definition
A **Transporter Envelope** is the set:


$$E = \{ T(t), A(T(t)) \mid t \in [0,1] \}$$



A transition is valid iff:
- $$T(t) \in \mathcal{T}$$
- $$A(T(t)) > 0$$
- No branching  
- No duplication  
- No collapse to ∅  

---

## 4. Transporter Claim (v0.3)
A transporter is:

> A continuity‑preserving envelope around a substrate transition arc γ, where the triad T and asymmetry functional A(T) remain valid and non‑zero for the entire path.

This is the first typed, non‑dual, non‑ghosting definition of a transporter in the canon.
