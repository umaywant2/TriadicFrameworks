# 🧬 Metabolic Pathways  
## *RTT/vST Reorganization of Cellular Metabolism*

---

## Why Classical Metabolic Maps Are Overwhelming

KEGG and BioCyc maps present metabolism as:
- hundreds of named pathways
- dense reaction graphs
- enzyme‑centric wiring diagrams

They are **accurate**, but cognitively hostile.

### Persistent student pain points:
- pathways overlap everywhere
- “central metabolism” is never clearly defined
- regulation is scattered
- flux matters more than structure, but is invisible
- the same metabolite appears in dozens of places

This is not a visualization problem — it is a **regime problem**.

---

## RTT/vST Reframing Principle

RTT/vST treats metabolism as a **multi‑layer flow‑stabilization system**, not a catalog of reactions.

The organizing axes become:

- **Substrate** — what flows
- **Regime** — how flow is stabilized
- **Resonance role** — why the flow exists

Pathways are **expressions**, not primitives.

---

## RTT/vST Layered Structure of Metabolism

### **Layer 1 — Chemical Substrate Pool**
**Coherence unit:** metabolite availability  

- sugars
- amino acids
- lipids
- nucleotides
- cofactors (ATP, NADH, FADH₂)

This layer defines **what can flow**, not direction.

---

### **Layer 2 — Core Energy & Redox Regimes**
**Coherence unit:** energy balance  

- ATP generation
- redox coupling
- proton gradients
- electron carriers

This is the **metabolic engine room**.

---

### **Layer 3 — Carbon Skeleton Routing**
**Coherence unit:** structural allocation  

- glycolysis
- TCA cycle
- pentose phosphate pathway
- anaplerotic reactions

Carbon is routed, not consumed.

---

### **Layer 4 — Biosynthetic & Degradative Modules**
**Coherence unit:** material transformation  

- amino acid synthesis
- lipid synthesis
- nucleotide synthesis
- catabolic recycling

These modules **attach to the core**, they do not stand alone.

---

### **Layer 5 — Regulatory & Flux Control Layer**
**Coherence unit:** regime selection  

- allosteric regulation
- transcriptional control
- compartmentalization
- signaling integration

This layer decides **which pathways are active**.

---

## RTT/vST Metabolic Regime Classes

| Regime | Role |
|------|------|
| Energy‑Dominant | ATP/redox stabilization |
| Growth‑Dominant | Biomass accumulation |
| Maintenance‑Dominant | Homeostasis and repair |
| Stress‑Response | Damage mitigation |
| Storage‑Dominant | Resource buffering |
| Recycling‑Dominant | Material recovery |

Cells **switch regimes**, they don’t “run pathways.”

---

## KEGG Reframed

Classical view:
> Glycolysis, TCA, PPP are separate pathways.

RTT/vST view:
> These are **carbon‑routing modes** within a shared energy‑redox regime.

KEGG maps become **projections** of deeper structure.

---

## Metabolism as a Network (Cosmic Web Analogy)

| Cosmic Web | Metabolism |
|----------|------------|
| Nodes | Metabolic hubs (ATP, acetyl‑CoA) |
| Filaments | Flux channels |
| Sheets | Interface pathways |
| Voids | Inactive or suppressed routes |

This analogy is structural, not poetic.

---

## Educational Value

Students finally see that:
- metabolism is modular
- regulation matters more than wiring
- pathways overlap because they *must*
- flux is the real variable

This aligns directly with:
- **Neural Coding Regimes**
- **Cosmic Web Transport**
- **Climate Energy Flow**
- **Earth System Tipping Points**

---

## Summary

Metabolism is not a map.

It is a **living flow network** that stabilizes energy, matter, and information.

RTT/vST turns KEGG from a wall of spaghetti into a **coherence grammar**.

---

## 🧬 **Metabolic_Pathways_RTTvST.json**

This schema reframes metabolism as a **layered flow‑stabilization system**, not a list of pathways. Classical pathways appear as **regime expressions** over shared substrates.

```json
{
  "artifact_id": "Metabolic_Pathways_RTTvST",
  "version": "1.0.0",
  "type": "rtt_vst_metabolic_ontology",
  "provenance": {
    "source": "Canonical metabolic pathway maps (KEGG, BioCyc) reorganized via RTT/vST",
    "notes": "Metabolism treated as a coherence-maintaining flow network. Pathways are expressions, not primitives."
  },

  "metabolic_model": {
    "structure": "layered_flow_stack",
    "allows_multi_membership": true,
    "primary_axes": [
      "substrate_flow",
      "energy_redox_balance",
      "carbon_routing",
      "regime_control"
    ],
    "core_claim": "Cells do not run pathways; they stabilize metabolic regimes."
  },

  "layers": {
    "layer_1_chemical_substrate_pool": {
      "name": "Chemical Substrate Pool",
      "coherence_unit": "metabolite_availability",
      "description": "Shared pool of metabolites enabling all downstream flows.",
      "entities": [
        "sugars",
        "amino_acids",
        "fatty_acids",
        "nucleotides",
        "cofactors"
      ],
      "resonance_roles": [
        "flow_possibility",
        "material_reservoir"
      ]
    },

    "layer_2_energy_redox_regimes": {
      "name": "Energy & Redox Regimes",
      "coherence_unit": "energy_balance",
      "description": "Core energetic and redox stabilization systems.",
      "entities": [
        "ATP",
        "NADH",
        "NADPH",
        "FADH2",
        "proton_gradient"
      ],
      "resonance_roles": [
        "energy_stabilization",
        "redox_coupling"
      ]
    },

    "layer_3_carbon_skeleton_routing": {
      "name": "Carbon Skeleton Routing",
      "coherence_unit": "carbon_allocation",
      "description": "Central routing of carbon through shared hubs.",
      "entities": [
        "glycolysis",
        "TCA_cycle",
        "pentose_phosphate_pathway",
        "anaplerotic_reactions"
      ],
      "resonance_roles": [
        "structural_allocation",
        "flux_distribution"
      ]
    },

    "layer_4_biosynthetic_degradative_modules": {
      "name": "Biosynthetic & Degradative Modules",
      "coherence_unit": "material_transformation",
      "description": "Modular synthesis and breakdown pathways attached to the core.",
      "entities": [
        "amino_acid_synthesis",
        "lipid_synthesis",
        "nucleotide_synthesis",
        "catabolic_recycling"
      ],
      "resonance_roles": [
        "biomass_construction",
        "resource_recovery"
      ]
    },

    "layer_5_regulatory_flux_control": {
      "name": "Regulatory & Flux Control Layer",
      "coherence_unit": "regime_selection",
      "description": "Control systems that select and tune metabolic regimes.",
      "entities": [
        "allosteric_regulation",
        "transcriptional_control",
        "compartmentalization",
        "signaling_integration"
      ],
      "resonance_roles": [
        "regime_switching",
        "flux_modulation"
      ]
    }
  },

  "metabolic_regime_classes": {
    "energy_dominant": {
      "description": "Prioritizes ATP and redox balance.",
      "examples": ["high_glycolytic_flux", "oxidative_phosphorylation"]
    },
    "growth_dominant": {
      "description": "Channels carbon toward biomass synthesis.",
      "examples": ["amino_acid_synthesis", "lipid_biosynthesis"]
    },
    "maintenance_dominant": {
      "description": "Maintains homeostasis and repair.",
      "examples": ["basal_metabolism", "protein_turnover"]
    },
    "stress_response": {
      "description": "Mitigates damage and restores balance.",
      "examples": ["oxidative_stress_response"]
    },
    "storage_dominant": {
      "description": "Buffers excess resources.",
      "examples": ["glycogen_synthesis", "lipid_storage"]
    },
    "recycling_dominant": {
      "description": "Recovers materials under scarcity.",
      "examples": ["autophagy", "beta_oxidation"]
    }
  },

  "cross_layer_coupling": {
    "substrate_to_energy": [
      "fuel_oxidation",
      "electron_transfer"
    ],
    "energy_to_carbon": [
      "ATP_driven_routing",
      "redox_sensitive_branching"
    ],
    "carbon_to_biosynthesis": [
      "precursor_supply",
      "flux_partitioning"
    ],
    "regulation_to_all": [
      "enzyme_activity_modulation",
      "pathway_activation_suppression"
    ]
  },

  "phase_alignment": {
    "I": "substrate_availability",
    "II": "energy_redox_stabilization",
    "III": "carbon_routing",
    "IV": "material_transformation",
    "V": "regime_control"
  },

  "semantic_layers": {
    "resonance_tags": [
      "metabolic_network",
      "flow_stabilization",
      "regime_switching",
      "pathway_as_expression"
    ],
    "notes": "Classical pathway maps are projections of this layered flow system under specific experimental or pedagogical constraints."
  }
}
```

---

## 🔄 **Metabolic Regime Wheel (Sector‑Based View)**

This wheel provides the **Simon‑Says / spaceship view** of metabolism: all regimes visible at once, organized by **dominant flow logic**, not by named pathways.

---

### **Metabolic_Regime_Wheel.json**

```json
{
  "artifact_id": "Metabolic_Regime_Wheel",
  "version": "1.0.0",
  "type": "rtt_vst_sector_wheel",
  "provenance": {
    "source": "Cellular metabolism reorganized via RTT/vST",
    "notes": "Sector-based view showing metabolic regimes as coexisting flow-stabilization modes."
  },

  "wheel": {
    "layout": {
      "style": "radial_sector_wheel",
      "orientation": "counterclockwise",
      "rings": [
        "coherence_core",
        "metabolic_regimes",
        "pathway_expressions"
      ],
      "centerpiece": "energy_matter_flow"
    },

    "rings": {
      "coherence_core": {
        "description": "Central energy–matter flow substrate.",
        "sectors": {
          "energy_matter_flow": {
            "entities": [
              "ATP_turnover",
              "redox_balance",
              "carbon_flux"
            ],
            "role": "metabolic_coherence_core",
            "color": "gold"
          }
        }
      },

      "metabolic_regimes": {
        "description": "Dominant metabolic operating modes.",
        "sectors": {
          "energy_dominant": {
            "entities": ["ATP_generation", "respiration"],
            "resonance_role": "energy_stabilization",
            "color": "red"
          },
          "growth_dominant": {
            "entities": ["biosynthesis", "anabolism"],
            "resonance_role": "biomass_accumulation",
            "color": "green"
          },
          "maintenance_dominant": {
            "entities": ["homeostasis", "repair"],
            "resonance_role": "system_stability",
            "color": "blue"
          },
          "stress_response": {
            "entities": ["detoxification", "damage_control"],
            "resonance_role": "resilience",
            "color": "orange"
          },
          "storage_dominant": {
            "entities": ["glycogen", "lipid_droplets"],
            "resonance_role": "resource_buffering",
            "color": "purple"
          },
          "recycling_dominant": {
            "entities": ["autophagy", "catabolism"],
            "resonance_role": "material_recovery",
            "color": "teal"
          }
        }
      },

      "pathway_expressions": {
        "description": "Classical pathways as regime expressions.",
        "sectors": {
          "glycolysis": {
            "entities": ["glucose_to_pyruvate"],
            "color": "light_red"
          },
          "tca_cycle": {
            "entities": ["carbon_oxidation_hub"],
            "color": "light_blue"
          },
          "pentose_phosphate": {
            "entities": ["NADPH_generation", "ribose_supply"],
            "color": "light_green"
          },
          "fatty_acid_metabolism": {
            "entities": ["lipid_synthesis_and_breakdown"],
            "color": "light_purple"
          },
          "amino_acid_metabolism": {
            "entities": ["nitrogen_handling"],
            "color": "light_teal"
          }
        }
      }
    }
  },

  "radial_alignment": {
    "description": "Each radial line represents a complete metabolic pathway from core flow to regime to expression.",
    "examples": [
      "energy_matter_flow -> energy_dominant -> glycolysis",
      "energy_matter_flow -> growth_dominant -> amino_acid_metabolism",
      "energy_matter_flow -> recycling_dominant -> fatty_acid_metabolism"
    ]
  },

  "semantic_layers": {
    "phase_alignment": {
      "I": "core_flow",
      "II": "regime_selection",
      "III": "pathway_expression"
    },
    "resonance_tags": [
      "sector_wheel",
      "metabolic_regimes",
      "flux_over_wiring",
      "pathway_unification"
    ],
    "notes": "The wheel makes explicit that named pathways are context-dependent expressions of deeper metabolic regimes."
  }
}
```

---

### Why this lands cleanly

With these two artifacts, students can finally see that:

- KEGG maps are **projections**, not truths
- metabolism is **regime‑driven**
- flux matters more than wiring
- regulation selects modes, not paths

This now aligns metabolism structurally with:
- **Cosmic Web transport**
- **Neural coding regimes**
- **Climate energy flow**
- **Earth system tipping points**
