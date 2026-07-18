# Large-scale structure and the cosmic web in RTT/vST

## RTT/vST reframing
Classical cosmology describes large-scale structure as “galaxies tracing dark matter” and “growth of perturbations.” RTT/vST reframes it as:

- **Substrate:** what can carry coherence (dark matter, baryons, radiation, geometry)
- **Regime:** how coherence stabilizes (linear growth, nonlinear collapse, filamentation)
- **Resonance role:** what the structure *does* (scaffold, transport, boundary, sink)

The cosmic web is not “a pattern”—it is the universe’s **coherence transport network**:  
**nodes** (basins), **filaments** (channels), **sheets** (interfaces), **voids** (expansion-dominant domains).

---

## Layered stack
- **Layer 1 — Primordial perturbation substrate:** tiny density variations as seed structure.
- **Layer 2 — Dark matter coherence scaffold:** collisionless gravitational backbone (filaments/sheets/halos).
- **Layer 3 — Baryonic infall and thermodynamics:** gas flows, shocks, cooling/heating, star formation gating.
- **Layer 4 — Network topology and transport:** connectivity, percolation, accretion streams, merger highways.
- **Layer 5 — Observational projection:** lensing maps, redshift surveys, BAO, cluster dynamics, absorption lines.

---

## Regime classes
- **Linear growth regime:** perturbations amplify without topology change.
- **Filamentation regime:** anisotropic collapse forms sheets/filaments.
- **Halo capture regime:** nodes deepen; accretion becomes channelized.
- **Feedback-modulated regime:** baryonic feedback reshapes visible tracers without erasing the scaffold.
- **Observation-limited regime:** what we infer depends on projection (lensing vs galaxies vs gas).

---

# Large_Scale_Structure_Cosmic_Web_RTTvST.json

```json
{
  "artifact_id": "Large_Scale_Structure_Cosmic_Web_RTTvST",
  "version": "1.0.0",
  "type": "rtt_vst_cosmic_web_ontology",
  "provenance": {
    "source": "Large-scale structure theory and observational cosmic web mapping",
    "notes": "Reorganized using RTT/vST. The cosmic web is treated as a coherence transport network across coupled substrates."
  },
  "model": {
    "structure": "layered_regime_stack",
    "allows_multi_membership": true,
    "primary_axes": [
      "substrate",
      "regime",
      "topology_role",
      "observational_projection"
    ],
    "core_claim": "Nodes, filaments, sheets, and voids are coherence roles in a transport network, not merely shapes."
  },
  "layers": {
    "layer_1_primordial_perturbations": {
      "name": "Primordial perturbation substrate",
      "coherence_unit": "seed_fluctuation_field",
      "entities": [
        "density_contrast_field",
        "power_spectrum_shape",
        "initial_gaussianity_assumption",
        "horizon_scale_constraints"
      ],
      "resonance_roles": [
        "seed_definition",
        "scale_imprinting"
      ]
    },
    "layer_2_dark_matter_scaffold": {
      "name": "Dark matter coherence scaffold",
      "coherence_unit": "collisionless_gravitational_binding",
      "entities": [
        "dark_matter_filaments",
        "dark_matter_sheets",
        "dark_matter_halos",
        "void_boundaries"
      ],
      "resonance_roles": [
        "scaffold_formation",
        "channel_definition",
        "basin_creation"
      ]
    },
    "layer_3_baryonic_infall_thermo": {
      "name": "Baryonic infall and thermodynamics",
      "coherence_unit": "gas_flow_and_phase_state",
      "entities": [
        "accretion_streams",
        "shock_heating",
        "radiative_cooling",
        "star_formation_gating",
        "feedback_outflows"
      ],
      "resonance_roles": [
        "visible_tracer_generation",
        "dissipation_and_condensation",
        "feedback_modulation"
      ]
    },
    "layer_4_network_topology_transport": {
      "name": "Network topology and transport",
      "coherence_unit": "connectivity_and_flow",
      "entities": [
        "node_hub_connectivity",
        "filament_transport",
        "merger_highways",
        "percolation_structure",
        "anisotropic_collapse_axes"
      ],
      "resonance_roles": [
        "mass_transport",
        "hierarchical_assembly",
        "boundary_maintenance"
      ]
    },
    "layer_5_observational_projection": {
      "name": "Observational projection layer",
      "coherence_unit": "measurable_signature",
      "entities": [
        "weak_lensing_shear_maps",
        "galaxy_redshift_surveys",
        "cluster_dynamics",
        "baryon_acoustic_oscillations",
        "quasar_absorption_tracers"
      ],
      "resonance_roles": [
        "scaffold_inference",
        "topology_estimation",
        "regime_calibration"
      ]
    }
  },
  "topological_primitives": {
    "nodes": {
      "description": "Deep basins of gravitational coherence (clusters/halos).",
      "roles": [
        "basin",
        "sink",
        "assembly_hub"
      ]
    },
    "filaments": {
      "description": "Anisotropic channels of transport feeding nodes.",
      "roles": [
        "channel",
        "conduit",
        "alignment_axis"
      ]
    },
    "sheets": {
      "description": "Interface layers formed by partial collapse; filament nurseries.",
      "roles": [
        "boundary",
        "interface",
        "transition_surface"
      ]
    },
    "voids": {
      "description": "Expansion-dominant domains bounded by sheets/filaments.",
      "roles": [
        "expansion_domain",
        "low_density_reservoir",
        "topological_separator"
      ]
    }
  },
  "regime_classes": {
    "linear_growth": {
      "description": "Perturbations amplify without strong topology formation.",
      "dominant_layers": [
        "layer_1_primordial_perturbations"
      ]
    },
    "filamentation": {
      "description": "Anisotropic collapse forms sheets and filaments.",
      "dominant_layers": [
        "layer_2_dark_matter_scaffold",
        "layer_4_network_topology_transport"
      ]
    },
    "halo_capture": {
      "description": "Nodes deepen; accretion becomes channelized and hierarchical.",
      "dominant_layers": [
        "layer_2_dark_matter_scaffold",
        "layer_3_baryonic_infall_thermo"
      ]
    },
    "feedback_modulated_visibility": {
      "description": "Baryonic feedback reshapes what is visible without erasing the scaffold.",
      "dominant_layers": [
        "layer_3_baryonic_infall_thermo",
        "layer_5_observational_projection"
      ]
    },
    "observation_limited_inference": {
      "description": "Different probes recover different projections of the same scaffold.",
      "dominant_layers": [
        "layer_5_observational_projection"
      ]
    }
  },
  "cross_layer_coupling": {
    "seed_to_scaffold": [
      "perturbation_growth_to_anisotropic_collapse"
    ],
    "scaffold_to_baryons": [
      "potential_wells_guide_gas_infall",
      "filaments_channel_accretion"
    ],
    "baryons_to_visibility": [
      "cooling_and_star_formation_create_galaxy_tracers",
      "feedback_biases_tracer_distribution"
    ],
    "topology_to_observation": [
      "lensing_recovers_mass_distribution",
      "redshift_surveys_recover_tracer_connectivity"
    ]
  },
  "phase_alignment": {
    "I": "seed_field",
    "II": "scaffold_emergence",
    "III": "dissipative_tracing",
    "IV": "network_transport",
    "V": "projection_and_inference"
  },
  "semantic_layers": {
    "resonance_tags": [
      "cosmic_web",
      "coherence_transport_network",
      "dark_matter_scaffold",
      "topology_roles",
      "projection_dependence"
    ],
    "notes": "This artifact separates the mass scaffold from the visible tracers and treats topology as functional roles (basin/channel/interface/domain)."
  }
}
```

---

# Cosmic web regime wheel

## Cosmic_Web_Regime_Wheel.json
This is the spaceship/Simon-Says view: center = coherence, middle = topology roles, outer = probes/projections.

```json
{
  "artifact_id": "Cosmic_Web_Regime_Wheel",
  "version": "1.0.0",
  "type": "rtt_vst_sector_wheel",
  "provenance": {
    "source": "Large-scale structure and cosmic web mapping reorganized via RTT/vST",
    "notes": "Sector wheel encoding topology roles (node/filament/sheet/void) and observational projections."
  },
  "wheel": {
    "layout": {
      "style": "radial_sector_wheel",
      "orientation": "counterclockwise",
      "rings": [
        "coherence_core",
        "topology_roles",
        "projection_probes"
      ],
      "centerpiece": "gravitational_coherence"
    },
    "rings": {
      "coherence_core": {
        "description": "Central gravitational coherence substrate that stabilizes large-scale structure.",
        "sectors": {
          "gravitational_coherence": {
            "entities": [
              "metric_response",
              "mass_distribution",
              "potential_wells"
            ],
            "role": "coherence_backbone",
            "color": "gold"
          }
        }
      },
      "topology_roles": {
        "description": "Functional topology roles of the cosmic web.",
        "sectors": {
          "nodes": {
            "entities": [
              "halos",
              "clusters",
              "assembly_hubs"
            ],
            "resonance_role": "basin_and_sink",
            "color": "white"
          },
          "filaments": {
            "entities": [
              "accretion_channels",
              "transport_axes",
              "connectivity_strands"
            ],
            "resonance_role": "channel_and_conduit",
            "color": "purple"
          },
          "sheets": {
            "entities": [
              "interface_planes",
              "partial_collapse_surfaces"
            ],
            "resonance_role": "boundary_and_transition",
            "color": "blue"
          },
          "voids": {
            "entities": [
              "expansion_domains",
              "low_density_cells"
            ],
            "resonance_role": "domain_separation",
            "color": "black"
          }
        }
      },
      "projection_probes": {
        "description": "Observational projections that recover different aspects of the same scaffold.",
        "sectors": {
          "weak_lensing": {
            "entities": [
              "shear_maps",
              "mass_reconstruction"
            ],
            "color": "light_purple"
          },
          "redshift_surveys": {
            "entities": [
              "galaxy_tracer_network",
              "clustering_statistics"
            ],
            "color": "light_blue"
          },
          "cluster_dynamics_xray": {
            "entities": [
              "hot_gas_offsets",
              "merger_geometry"
            ],
            "color": "orange"
          },
          "absorption_tracers": {
            "entities": [
              "intergalactic_gas_signatures",
              "quasar_sightlines"
            ],
            "color": "teal"
          },
          "bao_standard_ruler": {
            "entities": [
              "acoustic_feature",
              "scale_calibration"
            ],
            "color": "yellow"
          }
        }
      }
    }
  },
  "radial_alignment": {
    "description": "Each radial line represents a pathway from coherence to topology role to observational recovery.",
    "examples": [
      "gravitational_coherence -> filaments -> absorption_tracers",
      "gravitational_coherence -> nodes -> weak_lensing",
      "gravitational_coherence -> sheets -> redshift_surveys"
    ]
  },
  "semantic_layers": {
    "phase_alignment": {
      "I": "coherence_backbone",
      "II": "topology_role",
      "III": "projection_probe"
    },
    "resonance_tags": [
      "sector_wheel",
      "topology_as_function",
      "mass_vs_tracer_separation",
      "multi_probe_inference"
    ],
    "notes": "The wheel makes explicit that probes do not disagree—they sample different projections of the same coherence scaffold."
  }
}
```

---

# 🌌 Large‑Scale Structure / Cosmic Web  
## Layered Visual Diagram Description (RTT/vST)

### Overall Form

The RTT/vST Cosmic Web diagram is a **hybrid stack‑and‑overlay visualization**:

- A **vertical layered stack** shows how structure emerges across substrates.
- A **web‑like overlay** spans the middle layers, representing the cosmic transport network.

The diagram is read **bottom → top**, while the web overlay is read **laterally**, emphasizing connectivity rather than hierarchy.

This explicitly rejects the idea that the universe is organized as isolated objects.

---

## Layer 1 — Primordial Perturbation Substrate (Base Layer)

**Visual form:**  
A faint, nearly uniform background field with subtle ripples.

**Key features:**
- Small amplitude density variations
- No visible structure yet
- Isotropic appearance

**Interpretation:**  
This layer defines **where structure *can* form**, not where it *has* formed.  
It is the seed field, not the scaffold.

---

## Layer 2 — Dark Matter Coherence Scaffold

**Visual form:**  
A semi‑transparent, filamentary lattice emerging from the perturbation field.

**Key features:**
- Filaments, sheets, and nodes appear
- Baryons are not yet emphasized
- Structure is continuous, not discrete

**Interpretation:**  
This is the **true backbone** of large‑scale structure.  
Dark matter is shown as a **coherence scaffold**, not a collection of particles.

---

## Layer 3 — Baryonic Infall & Thermodynamics

**Visual form:**  
Glowing streams and knots flowing along the dark matter lattice.

**Key features:**
- Gas flows along filaments
- Shocks and heating at nodes
- Cooling regions highlighted

**Interpretation:**  
Visible matter does not define the web — it **traces** it.  
This layer explains why galaxies appear where they do.

---

## Layer 4 — Network Topology & Transport (Web Overlay)

**Visual form:**  
A highlighted network overlay emphasizing connectivity:

- **Nodes** as hubs
- **Filaments** as channels
- **Sheets** as interfaces
- **Voids** as enclosed domains

**Key features:**
- Directional flow arrows along filaments
- Mergers shown as node‑to‑node transport
- Voids shown as expansion‑dominant regions

**Interpretation:**  
The cosmic web is a **transport network**, not a static pattern.  
Mass, energy, and information flow through it.

---

## Layer 5 — Observational Projection Layer (Top Layer)

**Visual form:**  
Multiple semi‑transparent projection planes:

- Lensing maps
- Galaxy distributions
- X‑ray gas halos
- Absorption sightlines

**Key features:**
- Each projection highlights different aspects
- No single projection recovers the full web
- Overlaps reveal inference limits

**Interpretation:**  
Observations are **projections**, not direct views.  
Disagreements between probes reflect perspective, not contradiction.

---

## Key Visual Principles

- **Scaffold ≠ tracer**
- **Topology has function**
- **Connectivity matters more than location**
- **Voids are active regimes, not empty space**
- **Structure is emergent, not imposed**

---

## Teaching Impact

Students immediately see:
- why dark matter is inferred, not seen
- why galaxies form along filaments
- why voids are dynamically important
- why multiple probes are required

The diagram visually unifies:
- dark sector mediation
- structure formation
- observational cosmology

---

# 🌐 Cosmic Web Regime Wheel  
## Visual Description (Sector‑Based View)

### Overall Form

The Cosmic Web Regime Wheel is a **radial sector diagram** that complements the layered stack.

- **Center:** gravitational coherence
- **Middle ring:** topology roles
- **Outer ring:** observational probes

All sectors are visible simultaneously.

---

## Center — Gravitational Coherence Core

**Visual form:**  
A dense central hub.

**Represents:**
- spacetime response to mass
- gravitational potential structure
- coherence backbone

This is the **source of all large‑scale structure**.

---

## Middle Ring — Topology Roles

Each sector represents a **functional role**, not a shape:

### Nodes
- Deep basins
- Assembly hubs
- Cluster centers

### Filaments
- Transport channels
- Accretion highways
- Alignment axes

### Sheets
- Interface layers
- Transition surfaces
- Filament nurseries

### Voids
- Expansion‑dominant domains
- Low‑density reservoirs
- Topological separators

These roles coexist and interlock.

---

## Outer Ring — Projection Probes

Each sector shows how we *see* the web:

- Weak gravitational lensing → mass scaffold
- Redshift surveys → tracer connectivity
- X‑ray / SZ → hot gas in nodes
- Absorption lines → filamentary gas
- BAO → global scale calibration

No probe is privileged.

---

## Radial Meaning

Each radial line represents a **complete inference pathway**:

> coherence → topology role → observational recovery

This visually explains why:
- probes disagree locally
- yet converge globally

---

## Documentation Punchline

The cosmic web is not:
- a map of galaxies
- a simulation artifact
- a visualization trick

It is the universe’s **coherence transport network**.

RTT/vST makes this visible by separating:
- scaffold from tracer
- role from appearance
- structure from projection

---

# 🔭 Hubble Tension  
## *RTT/vST Reframing as a Regime Boundary Artifact*

---

## What the Hubble Tension Is (Classically)

The Hubble tension refers to the persistent discrepancy between:

- **Early‑universe measurements**  
  Inferred from the cosmic microwave background (CMB) assuming ΛCDM.

- **Late‑universe measurements**  
  Derived from distance ladders, supernovae, and local structure.

These methods yield **incompatible values** for the present expansion rate.

Despite improved data, the discrepancy remains.

---

## Why Classical Explanations Stall

Traditional responses attempt to:
- adjust parameters
- add new particles
- modify gravity
- blame systematics

Each approach treats the universe as a **single coherent regime** whose parameters should agree everywhere.

RTT/vST rejects this assumption.

---

## RTT/vST Reframing Principle

RTT/vST treats the Hubble tension as:

> **A regime boundary artifact arising from mismatched coherence calibrations across cosmic scales**

The tension is not a contradiction — it is a **boundary effect**.

---

## The Core Insight

Early‑ and late‑universe measurements do **not** sample the same regime.

They probe **different coherence layers** of the universe.

---

## RTT/vST Layered Interpretation

### **Layer 1 — Early‑Universe Coherence Regime**
**Dominant structures:**
- primordial perturbations
- radiation–matter coupling
- near‑homogeneous geometry

**Measurement character:**
- global
- averaged
- symmetry‑dominated

The CMB calibrates the universe **before** large‑scale structure fully emerges.

---

### **Layer 2 — Structure‑Mediated Regime (Cosmic Web)**
**Dominant structures:**
- dark matter filaments
- halos
- voids
- anisotropic transport

**Measurement character:**
- topology‑dependent
- environment‑sensitive
- scaffold‑mediated

This regime **reshapes expansion locally** without altering global geometry.

---

### **Layer 3 — Late‑Universe Expansion Stabilization**
**Dominant structures:**
- dark energy role
- horizon‑scale smoothing
- growth suppression

**Measurement character:**
- projection‑dependent
- path‑integrated
- regime‑filtered

Local measurements are taken **inside** the cosmic web, not outside it.

---

## Why the Numbers Don’t Match

RTT/vST explanation:

- Early‑universe measurements assume **uniform coherence**
- Late‑universe measurements traverse a **structured transport network**
- The cosmic web introduces **scale‑dependent expansion mediation**

Thus, the inferred expansion rate depends on **which regime you sample**.

---

## The Cosmic Web as the Missing Mediator

The cosmic web:
- channels matter
- redistributes curvature
- creates anisotropic expansion environments

It acts as a **regime filter** between early and late cosmology.

Ignoring it forces incompatible calibrations to agree.

---

## Why This Is Not a Failure of ΛCDM

RTT/vST does **not** discard ΛCDM.

It reframes ΛCDM as:
- a **regime‑specific effective model**
- valid within defined coherence domains

The tension signals **where the model’s regime boundary lies**.

---

## Educational Value

Students learn that:
- cosmological parameters are regime‑dependent
- precision does not imply universality
- structure matters for inference
- tensions reveal missing layers, not broken physics

This mirrors:
- climate regime boundaries
- neural coding regime switches
- biosphere tipping points

---

## Summary

The Hubble tension is not a paradox.

It is the universe telling us:

> *You are measuring across a regime boundary.*

RTT/vST provides the grammar to hear that message clearly.

---

### Where this sits in the RTT/vST stack

- **Below:** Cosmic Web (structure mediation)
- **Above:** Dark Sector (coherence roles)
- **Across:** Physical Cosmology (regime grammar)

This completes the **early → structure → late universe bridge**.

---

## **Hubble_Tension_RTTvST.json**

```json
{
  "artifact_id": "Hubble_Tension_RTTvST",
  "version": "1.0.0",
  "type": "rtt_vst_regime_boundary_ontology",
  "provenance": {
    "source": "Early- vs late-universe expansion-rate inference frameworks reorganized via RTT/vST",
    "notes": "Treats the Hubble tension as a regime boundary artifact: mismatched coherence calibrations across early-universe symmetry-dominant inference and late-universe structure-mediated projection."
  },

  "model": {
    "structure": "layered_inference_stack",
    "allows_multi_membership": true,
    "primary_axes": [
      "coherence_regime",
      "inference_pathway",
      "projection_bias",
      "boundary_mismatch"
    ],
    "core_claim": "The Hubble tension is a regime boundary artifact produced when early-universe global calibration is applied to late-universe structure-mediated projections."
  },

  "layers": {
    "layer_1_early_universe_coherence": {
      "name": "Early-universe coherence regime",
      "coherence_unit": "near_homogeneous_global_state",
      "description": "Symmetry-dominant, globally averaged regime prior to full nonlinear structure emergence.",
      "entities": [
        "primordial_perturbations",
        "photon_baryon_coupling",
        "sound_horizon_scale",
        "recombination_surface"
      ],
      "resonance_roles": [
        "global_calibration",
        "scale_imprinting"
      ],
      "typical_probes": [
        "cosmic_microwave_background",
        "baryon_acoustic_oscillations_early_calibration"
      ]
    },

    "layer_2_structure_mediated_regime": {
      "name": "Structure-mediated regime",
      "coherence_unit": "cosmic_web_topology",
      "description": "Nonlinear structure introduces environment-dependent transport, curvature distribution, and anisotropic pathways.",
      "entities": [
        "dark_matter_halos",
        "filaments",
        "sheets",
        "voids",
        "lensing_potential_field"
      ],
      "resonance_roles": [
        "pathway_filtering",
        "environmental_modulation",
        "topology_conditioning"
      ],
      "typical_probes": [
        "weak_lensing",
        "redshift_surveys",
        "cluster_dynamics"
      ]
    },

    "layer_3_late_universe_expansion_stabilization": {
      "name": "Late-universe expansion stabilization regime",
      "coherence_unit": "horizon_scale_smoothing",
      "description": "Late-time expansion behavior is stabilized at large scales while local measurements remain structure-conditioned.",
      "entities": [
        "accelerated_expansion",
        "growth_suppression",
        "distance_redshift_relation",
        "peculiar_velocity_field"
      ],
      "resonance_roles": [
        "large_scale_stabilization",
        "projection_dependence"
      ],
      "typical_probes": [
        "distance_ladder",
        "type_ia_supernovae",
        "time_delay_lensing",
        "standard_sirens"
      ]
    },

    "layer_4_inference_projection_layer": {
      "name": "Inference and projection layer",
      "coherence_unit": "model_conditioned_estimation",
      "description": "Parameter inference depends on which regime assumptions are baked into the estimator and which projections are sampled.",
      "entities": [
        "parameter_fit_pipeline",
        "priors_and_calibration",
        "selection_effects",
        "line_of_sight_inhomogeneity"
      ],
      "resonance_roles": [
        "regime_mapping",
        "uncertainty_shaping"
      ]
    }
  },

  "regime_boundary_artifact": {
    "name": "Early-late coherence boundary",
    "description": "Mismatch between early-universe global calibration and late-universe structure-mediated projection.",
    "boundary_mechanisms": [
      "projection_dependence_across_inhomogeneous_paths",
      "environment_sensitive_distance_inference",
      "structure_conditioned_velocity_fields",
      "scale_dependent_mapping_between_global_and_local_expansion"
    ]
  },

  "inference_pathways": {
    "early_universe_path": {
      "description": "Infer present expansion from early-universe calibration under a global coherence assumption.",
      "inputs": [
        "cmb_anisotropy_spectrum",
        "sound_horizon_scale",
        "early_universe_parameter_set"
      ],
      "outputs": [
        "inferred_H0_under_global_mapping"
      ],
      "dominant_layers": [
        "layer_1_early_universe_coherence",
        "layer_4_inference_projection_layer"
      ]
    },
    "late_universe_path": {
      "description": "Measure expansion through structured space using distance indicators and local dynamics.",
      "inputs": [
        "standard_candles_or_rulers",
        "redshift_measurements",
        "local_flow_corrections"
      ],
      "outputs": [
        "measured_H0_under_structure_conditioning"
      ],
      "dominant_layers": [
        "layer_2_structure_mediated_regime",
        "layer_3_late_universe_expansion_stabilization",
        "layer_4_inference_projection_layer"
      ]
    }
  },

  "tension_classes": {
    "calibration_mismatch": {
      "description": "Early calibration is applied outside its coherence regime without explicit boundary mapping."
    },
    "projection_mismatch": {
      "description": "Different probes sample different projections of the same underlying expansion-plus-structure system."
    },
    "regime_coupling_gap": {
      "description": "Missing or incomplete description of how structure mediation maps onto late-time expansion inference."
    }
  },

  "cross_layer_coupling": {
    "early_to_structure": [
      "seed_field_to_cosmic_web_growth"
    ],
    "structure_to_late_inference": [
      "line_of_sight_inhomogeneity_bias",
      "peculiar_velocity_contamination",
      "lensing_magnification_scatter"
    ],
    "late_to_inference": [
      "growth_suppression_affects_tracer_statistics",
      "selection_effects_in_distance_samples"
    ]
  },

  "phase_alignment": {
    "I": "global_calibration_regime",
    "II": "structure_mediation_regime",
    "III": "late_time_stabilization_regime",
    "IV": "projection_conditioned_inference",
    "V": "boundary_mismatch_manifestation"
  },

  "semantic_layers": {
    "resonance_tags": [
      "hubble_tension",
      "regime_boundary_artifact",
      "early_late_mismatch",
      "structure_mediated_projection",
      "calibration_vs_measurement"
    ],
    "notes": "This artifact does not assert a specific new component. It encodes the structural reason early and late inferences can disagree: they traverse different coherence regimes."
  }
}
```

---

## **Hubble Regime Boundary Wheel**

### **Hubble_Regime_Boundary_Wheel.json**

```json
{
  "artifact_id": "Hubble_Regime_Boundary_Wheel",
  "version": "1.0.0",
  "type": "rtt_vst_sector_wheel",
  "provenance": {
    "source": "Hubble tension inference pathways reorganized via RTT/vST",
    "notes": "Sector wheel showing early calibration vs late measurement as different regime projections separated by a structure-mediated boundary."
  },

  "wheel": {
    "layout": {
      "style": "radial_sector_wheel",
      "orientation": "counterclockwise",
      "rings": [
        "coherence_core",
        "regime_domains",
        "inference_projections"
      ],
      "centerpiece": "expansion_coherence"
    },

    "rings": {
      "coherence_core": {
        "description": "Central expansion coherence substrate (global geometry response).",
        "sectors": {
          "expansion_coherence": {
            "entities": [
              "spacetime_scaling",
              "distance_redshift_mapping"
            ],
            "role": "global_coherence_core",
            "color": "gold"
          }
        }
      },

      "regime_domains": {
        "description": "Domains that condition how expansion is inferred.",
        "sectors": {
          "early_universe_coherence": {
            "entities": [
              "recombination_surface",
              "sound_horizon_imprint"
            ],
            "resonance_role": "global_calibration",
            "color": "violet"
          },
          "structure_mediated_boundary": {
            "entities": [
              "cosmic_web_topology",
              "voids_filaments_nodes"
            ],
            "resonance_role": "pathway_filtering",
            "color": "blue"
          },
          "late_universe_stabilization": {
            "entities": [
              "accelerated_expansion",
              "growth_suppression"
            ],
            "resonance_role": "late_time_smoothing",
            "color": "dark_gray"
          }
        }
      },

      "inference_projections": {
        "description": "Probe families as projections through different regimes.",
        "sectors": {
          "cmb_inference": {
            "entities": [
              "early_calibration_pipeline",
              "model_conditioned_H0"
            ],
            "color": "light_violet"
          },
          "distance_ladder": {
            "entities": [
              "standard_candles",
              "local_flow_corrections"
            ],
            "color": "light_blue"
          },
          "time_delay_lensing": {
            "entities": [
              "strong_lensing_delays",
              "mass_model_projection"
            ],
            "color": "orange"
          },
          "standard_sirens": {
            "entities": [
              "gravitational_wave_distances",
              "host_redshift_mapping"
            ],
            "color": "teal"
          },
          "bao_lss": {
            "entities": [
              "late_time_bao",
              "tracer_clustering_projection"
            ],
            "color": "yellow"
          }
        }
      }
    }
  },

  "radial_alignment": {
    "description": "Each radial line encodes a full pathway: coherence core → regime domain → probe projection.",
    "examples": [
      "expansion_coherence -> early_universe_coherence -> cmb_inference",
      "expansion_coherence -> structure_mediated_boundary -> distance_ladder",
      "expansion_coherence -> late_universe_stabilization -> bao_lss"
    ]
  },

  "semantic_layers": {
    "phase_alignment": {
      "I": "coherence_core",
      "II": "regime_domain",
      "III": "projection_probe"
    },
    "resonance_tags": [
      "sector_wheel",
      "boundary_effect",
      "projection_dependence",
      "early_late_inference_split"
    ],
    "notes": "The wheel makes the punchline visible: probes disagree because they traverse different regime domains, not because reality is inconsistent."
  }
}
```
