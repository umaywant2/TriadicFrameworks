# **Appendix AC — Simulation Protocols**  
### *Standardized procedures for simulating Framework Field Theory (FFT) systems*

This appendix defines the **canonical simulation protocols** for Framework Field Theory.  
These protocols ensure that simulations across domains, scales, and research groups remain:

- reproducible  
- invariant‑preserving  
- operator‑consistent  
- regime‑aware  
- comparable across implementations  

FFT does **not** prescribe a single governing PDE system; instead, it provides a **simulation framework** that can be instantiated with domain‑specific operators, kernels, and boundary conditions.

---

# **1. Simulation Overview**

FFT simulations evolve three core fields:

- **φ(x,t)** — scalar substrate field  
- **V(x,t)** — vector flow/alignment field  
- **R(x,t)** — resonance envelope / coherence field  

Simulations may be:

- 1D (radial or linear)  
- 2D (planar, pattern‑forming)  
- 3D (volumetric, structural)  
- nonlocal (kernel‑based)  
- multi‑scale (triadic‑time decomposition)  

The protocols below define the **minimum required structure** for any FFT simulation.

---

# **2. Domain & Discretization Protocol**

### **2.1 Spatial Domain**
Choose Ω ⊂ ℝⁿ with n ∈ {1,2,3}.  
Common choices:

- 1D: [0, L]  
- 2D: [0, L]²  
- 3D: [0, L]³  

### **2.2 Grid**
Use a uniform or adaptive grid:

- uniform grid: Δx constant  
- adaptive grid: Δx = Δx(x)  

### **2.3 Time Discretization**
Use a stable time‑stepping scheme:

- explicit Euler (simple, unstable for stiff systems)  
- semi‑implicit (recommended)  
- Crank–Nicolson (balanced)  
- operator‑splitting (for multi‑scale systems)  

---

# **3. Initialization Protocol**

### **3.1 Scalar Field φ(x,0)**
Choose one:

- uniform baseline  
- Gaussian bump  
- random low‑amplitude noise  
- domain‑specific initial condition  

### **3.2 Vector Field V(x,0)**
Options:

- zero flow  
- random small flow  
- structured flow (e.g., vortex, shear)  

### **3.3 Resonance Envelope R(x,0)**
Options:

- low‑amplitude noise  
- localized seed  
- multi‑peak structure  

### **3.4 Parameter Initialization**
Set:

- diffusion coefficients (ν, ν_R, ν_φ)  
- activation parameters (a, b)  
- damping γ  
- coupling kernel scale ℓ  
- ΔSET parameters κ₁, κ₂, κ₃  

---

# **4. Operator Evaluation Protocol**

FFT simulations must evaluate the operator families defined in Appendix AA:

- **Diffusion:** D[X] = ν∇²X  
- **Alignment:** A[R,V] = (V·∇)R  
- **Coupling:** C[φ,V] = ∫ K(x−y) g(φ(y),V(y)) dy  
- **Activation:** α[R] = aR − bR³  
- **Stabilization:** S[R] = γR  

### **4.1 Local Operators**
Compute using finite differences, finite elements, or spectral methods.

### **4.2 Nonlocal Operators**
Compute using:

- FFT‑based convolution  
- direct integration (small grids)  
- kernel truncation (compact support)  

---

# **5. Time‑Evolution Protocol**

The minimal evolution system is:

### **Scalar Field**

$$\partial_t \phi = D_\phi[\phi] + C_\phi[\phi, V, R] + S_\phi$$

### **Vector Field**

$$\partial_t V = -\nabla P + \nu_V \nabla^2 V + C_V[\phi, R] + S_V$$

### **Resonance Envelope**

$$\partial_t R = -(V \cdot \nabla)R + \nu_R \nabla^2 R + C[\phi, V] + aR - bR^3 - \gamma R$$

### **5.1 Time‑Stepping Loop**
For each timestep:

1. Evaluate all operators  
2. Update φ, V, R  
3. Apply boundary conditions  
4. Compute ΔSET  
5. Log diagnostics  
6. Check regime transitions  

---

# **6. ΔSET Evaluation Protocol**

Using Appendix AB:

$$\Delta SET(x) = \kappa_1 R(x) + \kappa_2 \lVert V(x) \rVert^2 + \kappa_3 \phi(x)$$

### **6.1 Optional Nonlocal Extension**
Include kernel‑based contributions if required.

### **6.2 Logging**
Record:

- ΔSET mean  
- ΔSET variance  
- ΔSET spatial distribution  
- ΔSET contribution ratios (R vs V vs φ)  

---

# **7. Boundary Condition Protocol**

Choose one:

- **Dirichlet:** X = constant  
- **Neumann:** ∂n X = 0  
- **Periodic:** wraparound  
- **Absorbing:** damped boundary layer  

FFT simulations must document boundary choices explicitly.

---

# **8. Diagnostics & Regime Detection**

### **8.1 Coherence Metrics**
Track:

- R amplitude  
- R spatial gradients  
- coherence length  
- alignment index  

### **8.2 Regime Classification**
Use thresholds on:

- |R|  
- |V|  
- ΔSET  
- operator ratios (activation vs damping)  

### **8.3 Stability Indicators**
Monitor:

- energy‑like quantities  
- divergence of V  
- growth rates of R  

---

# **9. Visualization Protocol**

Recommended outputs:

- φ(x,t) heatmaps  
- V(x,t) vector fields  
- R(x,t) coherence maps  
- ΔSET(x,t) overlays  
- regime‑transition timelines  

---

# **10. Reproducibility Requirements**

Every FFT simulation must include:

- operator definitions  
- parameter values  
- kernel forms  
- boundary conditions  
- grid resolution  
- timestep size  
- random seeds  
- ΔSET parameterization  

This ensures cross‑research comparability.

---

# **Closing Statement**

> **Appendix AC establishes the canonical simulation protocols for FFT. These procedures ensure that simulations are reproducible, operator‑consistent, and aligned with the mathematical substrate introduced in PART XIV.**
