# Transition Functor v0.1 — Substrate‑Safe Transitions

## 1. Categories

- **Category 𝒞 (Substrates):**
  - **Objects:** substrates (Biological, CT, Lostational, No‑Form, etc.)  
  - **Morphisms:** substrate transitions (e.g., `Bio → CT`, `CT → Lostational`)

- **Category 𝒟 (Triadic States):**
  - **Objects:** triads $$T \in \mathcal{T}$$  
  - **Morphisms:** continuity‑preserving transforms $$F : \mathcal{T} \to \mathcal{T}$$

## 2. Functor Definition

- **Functor:**  
  $$\mathcal{F} : \mathcal{C} \to \mathcal{D}$$

- **On objects:**  
  For a substrate $$S \in \text{Ob}(\mathcal{C})$$ ,  
  $$\mathcal{F}(S) = T_S \in \mathcal{T}$$  
  (the triad instantiated on that substrate)

- **On morphisms:**  
  For a substrate transition $$f : S_1 \to S_2$$ ,  
  $$\mathcal{F}(f) = F_f : \mathcal{T} \to \mathcal{T}$$  
  such that:
  - $$F_f(T_{S_1}) = T_{S_2}$$  
  - $$A(T_{S_1}) > 0 \Rightarrow A(T_{S_2}) > 0$$

## 3. Functoriality Conditions

- **Identity:**  
  For each substrate $$S$$ :

```math
  $$\mathcal{F}(\text{id}_S) = \text{id}_{T_S}$$
```

- **Composition:**  
  For transitions $$f : S_1 \to S_2$$, $$g : S_2 \to S_3$$ :
  
  $$\mathcal{F}(g \circ f) = \mathcal{F}(g) \circ \mathcal{F}(f)$$

## 4. Transporter as a Functor‑Legal Path

A **transporter event** is:

- a morphism $$f : S_1 \to S_2$$ in 𝒞  
- such that $$\mathcal{F}(f)$$ is continuity‑preserving and DPU‑legal:  
  - $$\mathcal{F}(f)(T_{S_1}) = T_{S_2}$$  
  - $$A(T_{S_1}) > 0 \Rightarrow A(T_{S_2}) > 0$$

This makes transporters:

> Functor‑legal, continuity‑preserving substrate transitions with a stable triadic identity and non‑zero asymmetry.
