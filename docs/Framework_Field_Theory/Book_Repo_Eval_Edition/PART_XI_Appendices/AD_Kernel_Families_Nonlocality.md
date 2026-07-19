# **Appendix AD — Kernel Families & Nonlocality**  
### *Formalizing the nonlocal structures that govern coherence propagation in FFT*

Framework Field Theory (FFT) incorporates **nonlocal interactions** through kernel‑based operators.  
These kernels allow distant regions of a system to influence one another, enabling:

- long‑range coherence  
- resonance propagation  
- multi‑scale coupling  
- regime‑dependent influence  
- structural pattern formation  

This appendix defines the **canonical kernel families**, their mathematical properties, and their role in FFT’s operator ecology.

---

# **1. Purpose of Kernels in FFT**

Kernels appear primarily in the **Coupling Operator**:

```math
C[\phi, V](x) = \int_{\Omega} K(x - y)\, g(\phi(y), V(y))\, dy
```

They encode how information, coherence, or influence travels across space.

Kernels allow FFT to model:

- nonlocal coherence waves  
- long‑range structural influence  
- cross‑field modulation  
- multi‑scale interactions  
- emergent pattern formation  

Without kernels, FFT would reduce to a purely local PDE system — losing its dimensional richness.

---

# **2. Canonical Kernel Families**

FFT supports several kernel families, each corresponding to a different type of nonlocal behavior.

---

## **2.1 Gaussian Kernels (Local‑Dominant, Smooth)**

$$K_G(r) = \frac{1}{(2\pi \ell^2)^{n/2}} \exp\!\left(-\frac{r^2}{2\ell^2}\right)$$

**Properties:**

- smooth  
- rapidly decaying  
- local influence dominates  
- controlled by scale parameter ℓ  

**Use cases:**

- coherence smoothing  
- short‑range coupling  
- stable pattern formation  

---

## **2.2 Exponential Kernels (Longer Reach)**

$$K_E(r) = \frac{1}{2\ell} \exp\!\left(-\frac{|r|}{\ell}\right)$$

**Properties:**

- heavier tails than Gaussian  
- supports longer‑range influence  
- sharper transitions  

**Use cases:**

- resonance propagation  
- regime‑boundary interactions  

---

## **2.3 Power‑Law Kernels (Scale‑Free Influence)**

$$K_P(r) = \frac{1}{(1 + |r|^2)^{\alpha/2}}$$

**Properties:**

- slow decay  
- multi‑scale coupling  
- fractal‑like influence patterns  

**Use cases:**

- systems with no characteristic scale  
- coherence spanning large domains  

---

## **2.4 Compact‑Support Kernels (Finite Influence)**
```math
K_C(r) =
\begin{cases}
\frac{1}{Z} (1 - \frac{|r|}{\ell})^p, & |r| < \ell \\
0, & |r| \ge \ell
\end{cases}
```

**Properties:**

- strictly finite influence radius  
- computationally efficient  
- tunable smoothness (p)  

**Use cases:**

- simulations requiring strict locality bounds  
- domain‑limited interactions  

---

## **2.5 Anisotropic Kernels (Directional Influence)**

$$K_A(r) = \exp\!\left(- r^\top M^{-1} r \right)$$

where **M** is a positive‑definite matrix.

**Properties:**

- direction‑dependent influence  
- elongated or compressed coherence regions  

**Use cases:**

- flow‑aligned coherence  
- directional pattern formation  

---

# **3. Kernel Selection Guidelines**

### **3.1 Choose Gaussian when:**

- smoothness is desired  
- influence is mostly local  
- stability is important  

### **3.2 Choose Exponential when:**

- influence should reach farther  
- transitions should be sharper  

### **3.3 Choose Power‑Law when:**

- the system has no natural scale  
- long‑range coherence is essential  

### **3.4 Choose Compact‑Support when:**

- computational efficiency matters  
- strict locality is required  

### **3.5 Choose Anisotropic when:**

- coherence aligns with flow  
- directional structure is present  

---

# **4. Kernel Normalization**

All kernels should satisfy:

$$\int_{\Omega} K(r)\, dr = 1$$

This ensures:

- consistent scaling  
- stable coupling  
- predictable ΔSET contributions  

---

# **5. Nonlocality & Regime Behavior**

FFT’s regimes respond differently to kernel structure:

| Regime | Kernel Behavior |
|--------|-----------------|
| **Stable** | Gaussian or compact‑support preferred |
| **Transitional** | Exponential or anisotropic kernels dominate |
| **Paradox** | Power‑law kernels capture cross‑scale influence |
| **Interference** | Mixed kernels produce interference patterns |
| **Coherence** | Gaussian + power‑law hybrids model long‑range order |

This is the first appendix to explicitly tie kernels to **regime‑level behavior**.

---

# **6. Kernel‑Driven ΔSET Contributions**

Using Appendix AB:

```math
\Delta SET(x) = \kappa_1 R(x) + \kappa_2 \lVert V(x) \rVert^2 + \kappa_3 \phi(x)
+ \int_{\Omega} K(x-y)\, h(\phi(y), V(y), R(y))\, dy
```

Kernels allow ΔSET to:

- propagate coherence  
- accumulate nonlocal contributions  
- generate large‑scale structural effects  

---

# **7. Implementation Notes**

### **7.1 Efficient Computation**
Use:

- FFT‑based convolution for Gaussian/exponential  
- sparse kernels for compact‑support  
- hierarchical methods for power‑law  

### **7.2 Stability Considerations**
Nonlocal terms may require:

- smaller timesteps  
- implicit integration  
- kernel truncation  

### **7.3 Documentation Requirements**
Simulations must record:

- kernel family  
- kernel parameters  
- normalization method  
- computational method  

---

# **Closing Statement**

> **Appendix AD establishes the canonical kernel families and nonlocal structures that power FFT’s long‑range coherence, multi‑scale coupling, and regime‑dependent behavior. Kernels are the mathematical backbone of FFT’s nonlocality.**
