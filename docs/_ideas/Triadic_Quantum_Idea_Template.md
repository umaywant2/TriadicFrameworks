## Triadic Quantum Idea Template

#### File path
`/docs/_ideas/<short_name>.md`

#### Title
# <Short descriptive title>

---

### 1. One-line summary
- **Summary:** A single clear sentence describing the idea and its intended function.

---

### 2. Triad (State · Interaction · Observation)
- **State:** Describe the prepared quantum degrees of freedom (e.g., single qubit, spin ensemble, photonic mode, density matrix form).  
- **Interaction:** Specify the Hamiltonian, gates, coupling mechanisms, or open-system channels (list main terms and control knobs).  
- **Observation:** Define the measurement operators or detectors (POVMs, heterodyne, photon counters), what you read out, and how results are recorded.

---

### 3. Minimal experimental spec (prepare → act → read)
- **Prepare:** Procedure, initial conditions, temperature, bias fields, and initialization fidelity target.  
- **Act:** Drive waveform(s), timing, pulse shapes, amplitudes, and expected unitary or dissipative effects.  
- **Read:** Readout window, measurement basis, integration time, and expected signal-to-noise.

---

### 4. Two measurable signatures
- **Signature A (primary):** Observable, analytic expression for expected value or spectrum, and the numeric scale (example formula + example number).  
- **Signature B (secondary):** Distinct observable that confirms coupling/quantumness (correlation, sideband, visibility, entanglement witness) and expected scale.

---

### 5. Dominant error channels and vulnerability ranking
- **Top 3 vulnerabilities (ranked):**
  1. **Vulnerability 1:** brief cause and mitigation idea.  
  2. **Vulnerability 2:** brief cause and mitigation idea.  
  3. **Vulnerability 3:** brief cause and mitigation idea.

---

### 6. Resource and material checklist
- **Materials:** list candidate materials, substrates, and why (e.g., low-loss magneto-optic, superconducting film).  
- **Instruments:** must-have measurement tools (e.g., VNA, LDV, BLS, cryostat, AWG, DAQ).  
- **Control infrastructure:** timing resolution, phase stability, and classical compute needs.

---

### 7. Minimal theoretical model
- **Operators and variables:** list symbols and definitions (e.g., H, σ_x, a, m).  
- **Equations:** main dynamical equation(s) (Hamiltonian, master equation, coupled-mode).  
- **Approximations:** linearization, rotating-wave, secular, Markovian, etc.

---

### 8. Quick worked numeric placeholders
- **Scale choice:** choose one — optical / THz / microwave / spin-ensemble.  
- **Placeholders to fill:** resonance freq f = ___ Hz; coupling g = ___ Hz; decoherence T1 = ___ s; T2 = ___ s; expected visibility = ___%.

---

### 9. Experimental roadmap (3 milestone steps)
1. **Milestone 1:** bench-level proof-of-principle; deliverable and pass/fail metric.  
2. **Milestone 2:** integrated device showing coupling; deliverable and metric.  
3. **Milestone 3:** robust demonstration with error budget and repeatability; deliverable and metric.

---

### 10. Notes, references, and open questions
- **Notes:** any quick context or derivations to stash.  
- **Open questions:** list 3–6 targeted unknowns to resolve next (materials, coupling strength, scaling limits).  
- **References:** cite key papers or prior art (short list).

---

### Usage
Copy this template into /docs/_ideas/<short_name>.md and fill each section. Use the triad sections as canonical anchors when converting intuition to math or experiment.
