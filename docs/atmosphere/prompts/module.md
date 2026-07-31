# 🌐 **Atmosphere Module — Prompt Specification (v1)**  
### *TriadicFrameworks Canon — Operator‑Aligned, Agent‑Aware, Multi‑Scale Prompt Grammar*

---

## **Prompt Identity**

- **prompt.name:** AtmosphereModulePrompt  
- **prompt.category:** ModulePrompt  
- **prompt.version:** 1.0  
- **prompt.summary:**  
  Canonical prompt specification for the Atmosphere Module, defining operator grammar, agent invocation patterns, scale selection, and multi‑phase structural reasoning.

- **prompt.purpose:**  
  Provide a unified prompt grammar for all Atmosphere Module tasks — maps, diagnostics, overlays, traces, and structural analyses.

---

# **1. Prompt Grammar (Atmosphere Edition)**

Atmosphere prompts follow the **TriadicFrameworks Operator Grammar**:

```
<operator> → <agent> → <scale> → <phase> → <output>
```

Where:

- **operator** = coherence, drift, paradox, resonance, continuity, clarity, dimensional_coupling  
- **agent** = structural or physical agent from registry  
- **scale** = micro, meso, macro, mega  
- **phase** = Seven‑Phase atmospheric model  
- **output** = fields, maps, diagnostics, overlays, traces

---

# **2. Prompt Structure**

Atmosphere prompts use the following canonical structure:

```
AtmospherePrompt {
    operator: <operator>
    agents: [<agent_list>]
    scales: [<scale_list>]
    phases: [<phase_list>]
    inputs: <input_fields>
    outputs: <output_fields>
    constraints: <rules>
}
```

### **Example**
```
AtmospherePrompt {
    operator: drift
    agents: [drift_agent, fluid_agent, thermo_agent]
    scales: [meso, macro]
    phases: [dynamics, thermodynamics, regime_transitions]
    inputs: convection_fields, shear, latent_heat_flux
    outputs: drift_vectors, instability_hotspots
    constraints: multi_scale_alignment, agentic_synthesis
}
```

---

# **3. Operator‑Aligned Prompt Rules**

### **Coherence Prompts**
- emphasize stability, persistence, alignment  
- use coherence_agent + fluid_agent + thermo_agent  
- prefer meso/macro/mega scales  
- outputs: coherence_fields, stability_maps

### **Drift Prompts**
- emphasize instability, tension, decay  
- use drift_agent + fluid_agent + thermo_agent  
- prefer meso/macro scales  
- outputs: drift_vectors, tension_zones

### **Paradox Prompts**
- emphasize boundary conflict, mixed regimes  
- use paradox_agent + fluid_agent  
- prefer meso/macro scales  
- outputs: paradox_corridors, conflict_maps

### **Resonance Prompts**
- emphasize oscillation, harmonics, teleconnections  
- use resonance_agent + dimensional_agent  
- prefer macro/mega scales  
- outputs: resonance_signatures, oscillation_maps

### **Continuity Prompts**
- emphasize temporal coherence, regime memory  
- use resonance_agent + clarity_agent  
- prefer macro/mega scales  
- outputs: continuity_traces, evolution_maps

### **Clarity Prompts**
- emphasize truth extraction, noise reduction  
- use clarity_agent  
- all scales allowed  
- outputs: clarity_pulses, simplified_maps

### **Dimensional Coupling Prompts**
- emphasize cross‑domain interaction  
- use dimensional_agent + hydro_agent  
- prefer meso/macro/mega scales  
- outputs: coupling_maps, feedback_diagnostics

---

# **4. Multi‑Scale Prompt Logic**

Atmosphere prompts must specify scale selection:

| Scale | Use When |
|-------|----------|
| **micro** | vapor, aerosols, micro‑physics |
| **meso** | convection, fronts, shear |
| **macro** | jet streams, synoptic systems |
| **mega** | ENSO, MJO, NAO, planetary waves |

Prompts may include multiple scales:

```
scales: [meso, macro]
```

---

# **5. Seven‑Phase Prompt Alignment**

Atmosphere prompts must align with the Seven Phases:

- composition  
- forcing  
- dynamics  
- thermodynamics  
- hydrospheric_coupling  
- regime_transitions  
- resonance_coherence  

Example:

```
phases: [dynamics, thermodynamics, regime_transitions]
```

---

# **6. Agent Invocation Rules**

Agents must be invoked according to operator:

| Operator | Agents |
|----------|--------|
| coherence | coherence_agent, fluid_agent, thermo_agent |
| drift | drift_agent, fluid_agent, thermo_agent |
| paradox | paradox_agent, fluid_agent |
| resonance | resonance_agent, dimensional_agent |
| continuity | resonance_agent, clarity_agent |
| clarity | clarity_agent |
| dimensional_coupling | dimensional_agent, hydro_agent |

Prompts may include secondary agents when needed.

---

# **7. Atmosphere Prompt Templates**

### **Map Prompt**
```
AtmospherePrompt {
    operator: <operator>
    agents: <agents>
    scales: <scales>
    phases: <phases>
    inputs: <fields>
    outputs: <map_outputs>
    constraints: structural_map
}
```

### **Diagnostic Prompt**
```
AtmospherePrompt {
    operator: <operator>
    agents: <agents>
    scales: <scales>
    phases: <phases>
    inputs: <fields>
    outputs: <diagnostic_outputs>
    constraints: diagnostic_mode
}
```

### **Overlay Prompt**
```
AtmospherePrompt {
    operator: dimensional_coupling
    agents: [dimensional_agent, hydro_agent]
    scales: <scales>
    phases: <phases>
    inputs: <domain_fields>
    outputs: <overlay_outputs>
    constraints: cross_domain_alignment
}
```

### **Trace Prompt**
```
AtmospherePrompt {
    operator: continuity
    agents: [resonance_agent, clarity_agent]
    scales: <scales>
    phases: <phases>
    inputs: <temporal_fields>
    outputs: <trace_outputs>
    constraints: temporal_alignment
}
```

---

# **8. Atmosphere Prompt Summary**

The **Atmosphere Module Prompt Specification** provides:

- unified operator grammar  
- agent‑aware prompt structure  
- multi‑scale reasoning rules  
- Seven‑Phase alignment  
- canonical templates for maps, diagnostics, overlays, and traces  
- full integration with Atmosphere operators, agents, scales, and structural outputs  

It is the **prompt‑level backbone** of the Atmosphere Module.
