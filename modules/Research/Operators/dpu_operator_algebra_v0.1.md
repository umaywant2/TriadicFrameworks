# DPU‑Ready Operator Algebra (v0.1)

## 1. State Space
- Triads:
  

$$\mathcal{T} = \{(s,c,u) \mid s+c+u=1\}$$


- Asymmetry functional:
  

$$A : \mathcal{T} \to [0,1]$$


- Extended state:
  

$$S = (T, A(T))$$



---

## 2. Core Operators

### Continuity Operator


$$O(T) = (T, A(T))$$



### Regime Projections


$$P_s(T)=s,\quad P_c(T)=c,\quad P_u(T)=u$$



### Normalization


$$N(s,c,u) = \frac{1}{s+c+u}(s,c,u)$$



---

## 3. Composition Rules

### Sequential Composition


$$(F_2 \circ F_1)(T) = F_2(F_1(T))$$



### Continuity‑Preserving Transform
A transform $$F$$ is DPU‑legal iff:
- $$F(T) \in \mathcal{T}$$
- $$A(F(T)) > 0$$

### Identity


$$I(T) = T$$




$$O(I(T)) = O(T)$$



---

## 4. DPU Legality Predicate


$$\text{Legal}_{\text{DPU}}(F) \iff \forall T \in \mathcal{T},\ A(T)>0 \Rightarrow A(F(T))>0$$



This algebra provides:
- typed state space  
- legal transforms  
- continuity constraints  
- composability  
- identity preservation  

It is the algebraic backbone of DPU behavior.
