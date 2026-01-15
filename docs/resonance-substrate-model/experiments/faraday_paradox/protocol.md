# Faraday Paradox Experiment Protocol  
*Resonance Substrate Model — Experimental Series*

---

# Quicklinks

- [applications complex systems](../../applications/complex-systems.md)
- [data README](../../data/README.md)
- [data examples README](../../data/examples/README.md)
- [data reference README](../../data/reference/README.md)
- [data validation README](../../data/validation/README.md)
- [data validation experimental README](../../data/validation/experimental/README.md)
- [data validation synthetic README](../../data/validation/synthetic/README.md)
- [experiments README](../README.md)
- [experiments faraday paradox analysis.ipynb](analysis.ipynb.md)
- [experiments faraday paradox README](README.md)
- [experiments faraday paradox processed data README](processed_data/README.md)
- [experiments faraday paradox raw data data dictionary](raw_data/data_dictionary.md)
- [experiments faraday paradox raw data README](raw_data/README.md)
- [experiments replication guides README](../replication_guides/README.md)
- [experiments rotating field tests README](../rotating_field_tests/README.md)
- [experiments substrate alignment README](../substrate_alignment/README.md)
- [reference Keywords](../../reference/Keywords.md)
- [rsm-shim README](../../rsm-shim/README.md)
- [simulations README](../../simulations/README.md)
- [simulations configs README](../../simulations/configs/README.md)
- [simulations core README](../../simulations/core/README.md)
- [simulations examples README](../../simulations/examples/README.md)
- [src README](../../src/README.md)
- [tests README](../../tests/README.md)
- [tools README](../../tools/README.md)
- [tools cli README](../../tools/cli/README.md)
- [tools converters README](../../tools/converters/README.md)
- [tools visualization README](../../tools/visualization/README.md)
- [previous folder](../)

---

## 1. Objective
To investigate paradox‑class induction behavior under rotating magnetic fields and stationary conductors, and to compare classical EM predictions with resonance‑substrate field responses.

## 2. Background
Faraday’s Paradox describes a counterintuitive induction phenomenon where rotation of a magnet does not always induce the expected EMF in a stationary conductor.  
This experiment adapts the classical setup into the Resonance Substrate Model to explore:
- field alignment
- resonance envelope deformation
- spin‑field coherence under rotation

## 3. Apparatus
- rotating field source (physical or simulated)
- stationary conductive loop or substrate analog
- field sensors or substrate probes
- data acquisition system
- reference diagram: `apparatus_diagram.svg`

## 4. Procedure
### 4.1 Setup
1. Position the stationary conductor or substrate grid.  
2. Align the rotating magnetic field source with the central axis.  
3. Initialize measurement probes and baseline readings.  

### 4.2 Execution
1. Begin rotation at low angular velocity.  
2. Record induced field values and resonance envelope activation.  
3. Increase rotation speed in controlled increments.  
4. Capture spin‑field alignment and diffusion behavior at each step.  

### 4.3 Data Collection
- induced EMF or substrate‑analog signal  
- field vector snapshots  
- resonance envelope activation maps  
- rotation rate and stability metrics  

## 5. Analysis
Analysis is performed in `analysis.ipynb`, including:
- time‑series plots  
- field vector visualizations  
- comparison to classical EM predictions  
- substrate‑specific deviations  

## 6. Expected Outcomes
- reproduction of paradox‑class induction behavior  
- identification of resonance‑specific field responses  
- insight into substrate alignment under rotational forcing  

## 7. References
See `references.bib` in the whitepaper directory.

