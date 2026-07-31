# 🌐 **Atmosphere Module — Scale Registry**  
### *TriadicFrameworks Canon — Multi‑Scale Atmospheric System*

---

## **Registry Identity**

- **registry.name:** AtmosphereScales  
- **registry.category:** ScaleSystem  
- **registry.version:** 1.0  
- **registry.summary:**  
  Canonical registry defining the multi‑scale structure of atmospheric systems, used by the Atmosphere module for overlays, diagnostics, agentic interpretation, and RTT operator mapping.

- **registry.purpose:**  
  Provide a unified scale taxonomy for interpreting atmospheric behavior from micro‑scale processes to mega‑scale planetary oscillations.

---

# **Atmospheric Scales (Canonical Definitions)**

Each scale includes:

- **scale.id**  
- **scale.name**  
- **scale.range**  
- **scale.description**  
- **scale.domains**  
- **scale.operators**  
- **scale.agents**  
- **scale.phases**

---

## **Scale 1 — Micro**
**scale.id:** 1  
**scale.name:** micro  
**range:** millimeters → meters  

**Description:**  
Small‑scale atmospheric processes: aerosols, particulates, microphysics, condensation nuclei, droplet formation, and micro‑turbulence.

**Domains:** composition, thermodynamics  
**Operators:** clarity, coherence  
**Agents:** chem_agent, thermo_agent, clarity_agent  
**Phases:** composition, thermodynamics  

---

## **Scale 2 — Meso**
**scale.id:** 2  
**scale.name:** meso  
**range:** kilometers → hundreds of kilometers  

**Description:**  
Cloud systems, convection, thunderstorms, mesoscale convective complexes, sea breezes, fronts, and regional circulation.

**Domains:** dynamics, forcing, transitions  
**Operators:** coherence, drift, paradox  
**Agents:** fluid_agent, thermo_agent, drift_agent, paradox_agent  
**Phases:** dynamics, forcing, regime_transitions  

---

## **Scale 3 — Macro**
**scale.id:** 3  
**scale.name:** macro  
**range:** continental → hemispheric  

**Description:**  
Jet streams, storm tracks, synoptic systems, Rossby waves, large‑scale pressure fields, and planetary circulation cells.

**Domains:** dynamics, thermodynamics, resonance  
**Operators:** coherence, drift, resonance, continuity  
**Agents:** fluid_agent, radiative_agent, resonance_agent  
**Phases:** dynamics, thermodynamics, resonance_coherence  

---

## **Scale 4 — Mega**
**scale.id:** 4  
**scale.name:** mega  
**range:** planetary → global  

**Description:**  
Planetary waves, global oscillations (ENSO, MJO, NAO, QBO), teleconnections, AMOC interactions, and long‑term climate coherence.

**Domains:** resonance, dimensional coupling  
**Operators:** resonance, continuity, dimensional_coupling  
**Agents:** resonance_agent, dimensional_agent, clarity_agent  
**Phases:** resonance_coherence, hydrospheric_coupling  

---

# **Canonical Scale Table**

| ID | Scale | Range | Domains | Operators | Agents | Phases |
|----|--------|--------|---------|-----------|--------|--------|
| 1 | micro | mm → m | composition, thermodynamics | clarity, coherence | chem_agent, thermo_agent | composition, thermodynamics |
| 2 | meso | km → 100s km | dynamics, forcing, transitions | coherence, drift, paradox | fluid_agent, thermo_agent | dynamics, forcing, transitions |
| 3 | macro | continental → hemispheric | dynamics, thermodynamics, resonance | coherence, drift, resonance, continuity | fluid_agent, radiative_agent | dynamics, thermodynamics, resonance |
| 4 | mega | planetary → global | resonance, coupling | resonance, continuity, dimensional_coupling | resonance_agent, dimensional_agent | resonance_coherence, hydrospheric |
