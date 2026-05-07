# DPU‑Ready Operator Algebra (v0.1)

## 1. State Space

- **Triad space:**  
  $$\mathcal{T} = \{ (s,c,u) \in \mathbb{R}_{\ge 0}^3 \mid s + c + u = 1 \}$$

- **Asymmetry functional:**  
  $$A : \mathcal{T} \to [0,1]$$ , with canonical $$A(T^\*) = 0.01$$

- **Extended state:**  
  $$S = (T, A(T))$$ , where $$T \in \mathcal{T}$$

## 2. Core Operators

- **Continuity operator:**  
  $$O : \mathcal{T} \to \mathcal{T} \times [0,1]$$  
  $$O(T) = (T, A(T))$$

- **Regime projection operators:**  
  - $$P_s(T) = s$$ (subconscious weight)  
  - $$P_c(T) = c$$ (consciousness weight)  
  - $$P_u(T) = u$$ (supconsciousness weight)

- **Normalization operator:**  
  $$N(s,c,u) = \frac{1}{s+c+u}(s,c,u)$$ for non‑zero sum

## 3. Composition Rules

- **Sequential composition (DPU step):**  
  For two legal transforms $$F_1, F_2 : \mathcal{T} \to \mathcal{T}$$ :  
  $$(F_2 \circ F_1)(T) = F_2(F_1(T))$$

- **Continuity‑preserving transform:**  
  A transform $$F$$ is DPU‑legal iff:  
  - $$F(T) \in \mathcal{T}$$  
  - $$A(F(T)) > 0$$ whenever $$A(T) > 0$$

- **Idempotent identity check:**  
  $$I(T) = T$$  
  $$O(I(T)) = O(T)$$ (no change in identity or asymmetry)

## 4. DPU Legality Predicate

- **Predicate:**  
  $$\text{Legal}_\text{DPU}(F)$$ holds iff:  
  - $$F : \mathcal{T} \to \mathcal{T}$$  
  - $$\forall T \in \mathcal{T}, A(T) > 0 \Rightarrow A(F(T)) > 0$$

This algebra gives a DPU:

- a typed state space  
- legal transforms  
- continuity constraints  
- and a way to chain operations without breaking identity.
