# Operator Definitions  
## Substrate Operators for the SET Resonance Model

This document defines the primary substrate operators used in the evolution equations of the Spin (S), Charge (C), and Temperature (T) fields. These operators provide a modular way to express alignment, propagation, and dissipation effects.

---

## 1. Alignment Operator \(\mathcal{A}\)

### 1.1 Definition

The Alignment Operator acts on the Spin field and aligns it with local Charge gradients:



\[
\mathcal{A}_S(S, C) = \lambda_{SC} \nabla C
\]



Where:

- \(\lambda_{SC}\) is a coupling coefficient.

Interpretation:

- Drives \(S\) toward alignment with \(\nabla C\).  
- Encodes the tendency of spin structure to follow interaction bias.

---

## 2. Destabilization Operator \(\mathcal{X}\)

### 2.1 Definition

The Destabilization Operator reduces spin coherence in regions of strong Temperature gradients:



\[
\mathcal{X}_S(S, T) = -\lambda_{ST} \nabla T
\]



Where:

- \(\lambda_{ST}\) is a coupling coefficient.

Interpretation:

- High \(|\nabla T|\) reduces spin alignment.  
- Models decoherence and instability in high‑T regions.

---

## 3. Propagation Operator \(\mathcal{P}\)

### 3.1 Charge Propagation



\[
\mathcal{P}_C(C) = D_C \nabla^2 C
\]



Where:

- \(D_C\) is the charge diffusion coefficient.

Interpretation:

- Spreads charge bias spatially.  
- Smooths sharp gradients.

### 3.2 Spin Propagation



\[
\mathcal{P}_S(S) = D_S \nabla^2 S
\]



Where:

- \(D_S\) is the spin diffusion coefficient.

Interpretation:

- Spreads spin alignment.  
- Reduces local inhomogeneities.

### 3.3 Thermal Propagation



\[
\mathcal{P}_T(T) = D_T \nabla^2 T
\]



Where:

- \(D_T\) is the thermal diffusion coefficient.

Interpretation:

- Spreads thermal energy.  

---

## 4. Relaxation Operator \(\mathcal{R}\)

### 4.1 Spin Relaxation



\[
\mathcal{R}_S(S) = -\gamma_S S
\]



### 4.2 Charge Relaxation



\[
\mathcal{R}_C(C) = -\gamma_C C
\]



### 4.3 Temperature Relaxation



\[
\mathcal{R}_T(T) = -\gamma_T (T - T_0)
\]



Where:

- \(\gamma_S, \gamma_C, \gamma_T\) are relaxation coefficients.  
- \(T_0\) is the background temperature.

Interpretation:

- Drives fields toward baseline states.  
- Encodes loss of structure over time.

---

## 5. Source Operators \(\mathcal{S}\)

### 5.1 Spin‑Induced Charge Source



\[
\mathcal{S}_C(S) = \beta_{CS} \nabla \cdot S
\]



Where:

- \(\beta_{CS}\) is a coupling coefficient.

Interpretation:

- Divergence of Spin structure contributes to Charge bias.

### 5.2 Spin‑Induced Heating



\[
\mathcal{S}_T^{(S)}(S) = \eta_S |S|^2
\]



### 5.3 Gradient‑Induced Heating



\[
\mathcal{S}_T^{(C)}(C) = \eta_C |\nabla C|^2
\]



Where:

- \(\eta_S, \eta_C\) are heating coefficients.

Interpretation:

- Spin activity and strong Charge gradients contribute to Temperature.

---

## 6. Combined Evolution in Operator Form

For compactness, the field equations can be written as:



\[
\partial_t S = \mathcal{P}_S(S) + \mathcal{R}_S(S) + \mathcal{A}_S(S, C) + \mathcal{X}_S(S, T)
\]





\[
\partial_t C = \mathcal{P}_C(C) + \mathcal{R}_C(C) + \mathcal{S}_C(S)
\]





\[
\partial_t T = \mathcal{P}_T(T) + \mathcal{R}_T(T) + \mathcal{S}_T^{(S)}(S) + \mathcal{S}_T^{(C)}(C)
\]



This operator decomposition is intended to:

- simplify implementation in numerical solvers  
- allow modular modification of individual effects  
- support future extensions (e.g., additional coupling terms or higher‑order operators).

