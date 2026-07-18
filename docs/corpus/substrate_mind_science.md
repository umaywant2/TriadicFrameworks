substrate_mind_science 
# **README — Conscious Transfer Substrate Map v1**  
### *docs/substrate_mind_science/ct_substrate/README.md*

## **1. Purpose of This Directory**

This directory contains the **Conscious Transfer Substrate Map v1**, a formal, RTT‑compliant schema that defines the *minimal functional structure* of mind that can be:

- **Repeatably measured**  
- **Traceably mapped** to behavior and physiology  
- **Transfer‑addressable** across substrates  

It is the first layer of the Resonance Atlas designed specifically for **Conscious Transfer research**.

This schema is **not** a psychological or psychiatric model.  
It is a **substrate model** — a representation of the *functional invariants* that survive across tasks, individuals, and implementations.

---

## **2. Relationship to the Resonance Atlas**

The Resonance Atlas has three major layers:

1. **Minimal Empirical Mind Substrate v1**  
   - The distilled scientific core extracted from psychology + psychiatry  
   - Only green‑zone constructs (empirical, measurable, reproducible)

2. **Legacy‑Narratives Quarantine**  
   - All yellow/red constructs (interpretive, institutional, cultural, mythic)  
   - Preserved for context, but **never allowed** in substrate models

3. **Conscious Transfer Substrate Map (this directory)**  
   - The RTT‑filtered subset of the Minimal Substrate  
   - Formalized into a machine‑readable schema  
   - Ready for vST overlays and implementation work

The Conscious Transfer Substrate Map is therefore the **intersection** of:

- empirical mind science  
- RTT constraints  
- transfer‑ready formalization  

---

## **3. What This Schema Represents**

The schema defines four substrate layers:

### **A. Behavioral Layer**  
The lowest‑level functional invariants:

- conditioning laws  
- reinforcement structures  
- reaction‑time distributions  
- accuracy/error patterns  
- speed–accuracy tradeoff parameters  

These are the **observable invariants** that any conscious substrate must reproduce.

---

### **B. Cognitive Layer**  
The representational/computational invariants:

- working‑memory parameters  
- attention control parameters  
- drift‑diffusion decision models  
- signal‑detection parameters  
- reinforcement‑learning parameters  

These are the **task‑bound cognitive operators** that survive RTT filtering.

---

### **C. Measurement Layer**  
The interfaces that validate the substrate:

- psychometric reliability/validity  
- neuropsychological task batteries  
- normative z‑scores  

These are **not** the mind — they are the **measurement operators** that define equivalence across substrates.

---

### **D. Anchoring Constraints**  
The biological correlates that meet RTT criteria:

- lesion‑to‑function mappings  
- task‑locked neurophysiological signatures  
- stable pharmacological modulation profiles  

These are **constraints**, not requirements for biological tissue.

---

## **4. What This Schema Explicitly Excludes**

This schema **cannot** contain:

- DSM/ICD categories  
- personality disorders  
- psychoanalytic constructs  
- typologies (MBTI, Enneagram, etc.)  
- humanistic/existential frameworks  
- narrative‑based therapeutic models  
- cultural/institutional psychiatric categories  
- unfalsifiable or non‑substrate constructs  

All such material is stored in the **Legacy‑Narratives Quarantine**.

This ensures the substrate remains **scientifically clean** and **transfer‑ready**.

---

## **5. How RTT Interacts With This Schema**

RTT imposes three hard constraints:

- **Repeatability:**  
  Every field in the schema corresponds to a measurable pattern that replicates across trials.

- **Traceability:**  
  Every field has a clear mapping to behavior, physiology, or computational structure.

- **Transfer‑addressability:**  
  Every field can be instantiated in a non‑biological substrate without loss of functional identity.

If a construct fails any RTT condition, it is excluded.

---

## **6. How vST Will Overlay This Schema**

vST (Vectorized Substrate Topology) will attach to this schema by:

- defining **state‑spaces** for each cognitive/behavioral operator  
- defining **transition operators** for learning and decision models  
- defining **mapping functions** for anchoring constraints  
- defining **equivalence tests** for substrate‑to‑substrate transfer  

The Conscious Transfer Substrate Map is therefore the **foundation** on which vST builds the actual transfer mechanics.

---

## **7. File Structure**

```
ct_substrate/
  ├── ct_substrate.schema.json     # The formal schema (RTT-filtered)
  ├── README.md                    # This file
  └── examples/                    # Optional: future example substrate instances
```

---

## **8. Contribution Rules**

To maintain substrate integrity:

- **No yellow/red constructs** may be added to this schema  
- All additions must satisfy **RTT conditions**  
- All fields must be **operationalizable** (task‑bound, measurable)  
- All mappings must be **explicit**, not narrative  
- All biological references must be **functional**, not anatomical storytelling  

Pull requests that introduce narrative, interpretive, or diagnostic constructs will be redirected to the **Legacy‑Narratives Quarantine**.
```json

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/ct_substrate.schema.json",
  "title": "Conscious Transfer Substrate Map v1",
  "type": "object",
  "required": [
    "behavioral_layer",
    "cognitive_layer",
    "measurement_layer",
    "anchoring_constraints"
  ],
  "properties": {
    "behavioral_layer": { "$ref": "#/$defs/BehavioralLayer" },
    "cognitive_layer": { "$ref": "#/$defs/CognitiveLayer" },
    "measurement_layer": { "$ref": "#/$defs/MeasurementLayer" },
    "anchoring_constraints": { "$ref": "#/$defs/AnchoringConstraints" }
  },

  "$defs": {
    "BehavioralLayer": {
      "type": "object",
      "required": ["conditioning_models", "performance_metrics"],
      "properties": {
        "conditioning_models": { "$ref": "#/$defs/ConditioningModels" },
        "performance_metrics": { "$ref": "#/$defs/PerformanceMetrics" }
      }
    },

    "ConditioningModels": {
      "type": "object",
      "properties": {
        "classical": {
          "type": "object",
          "properties": {
            "cs_us_mapping": { "type": "array", "items": { "type": "string" } },
            "acquisition_rate": { "type": "number" },
            "extinction_rate": { "type": "number" }
          }
        },
        "operant": {
          "type": "object",
          "properties": {
            "reinforcement_schedule": { "type": "string" },
            "learning_rate": { "type": "number" },
            "discount_factor": { "type": "number" }
          }
        }
      }
    },

    "PerformanceMetrics": {
      "type": "object",
      "properties": {
        "reaction_time_distribution": {
          "type": "array",
          "items": { "type": "number" }
        },
        "accuracy": { "type": "number" },
        "error_types": {
          "type": "array",
          "items": { "type": "string" }
        },
        "speed_accuracy_tradeoff": {
          "type": "object",
          "properties": {
            "slope": { "type": "number" },
            "intercept": { "type": "number" }
          }
        }
      }
    },

    "CognitiveLayer": {
      "type": "object",
      "required": [
        "working_memory",
        "attention",
        "decision_models",
        "learning_models"
      ],
      "properties": {
        "working_memory": { "$ref": "#/$defs/WorkingMemory" },
        "attention": { "$ref": "#/$defs/Attention" },
        "decision_models": { "$ref": "#/$defs/DecisionModels" },
        "learning_models": { "$ref": "#/$defs/LearningModels" }
      }
    },

    "WorkingMemory": {
      "type": "object",
      "properties": {
        "capacity": { "type": "integer" },
        "decay_rate": { "type": "number" },
        "refresh_rate": { "type": "number" }
      }
    },

    "Attention": {
      "type": "object",
      "properties": {
        "selective_filter_strength": { "type": "number" },
        "sustained_attention_stability": { "type": "number" },
        "switching_cost": { "type": "number" }
      }
    },

    "DecisionModels": {
      "type": "object",
      "properties": {
        "drift_diffusion": {
          "type": "object",
          "properties": {
            "drift_rate": { "type": "number" },
            "boundary_separation": { "type": "number" },
            "non_decision_time": { "type": "number" }
          }
        },
        "signal_detection": {
          "type": "object",
          "properties": {
            "sensitivity_d_prime": { "type": "number" },
            "criterion_c": { "type": "number" }
          }
        }
      }
    },

    "LearningModels": {
      "type": "object",
      "properties": {
        "reinforcement_learning": {
          "type": "object",
          "properties": {
            "learning_rate": { "type": "number" },
            "exploration_rate": { "type": "number" },
            "reward_sensitivity": { "type": "number" }
          }
        }
      }
    },

    "MeasurementLayer": {
      "type": "object",
      "required": ["psychometrics", "neuropsych_tests"],
      "properties": {
        "psychometrics": { "$ref": "#/$defs/Psychometrics" },
        "neuropsych_tests": { "$ref": "#/$defs/NeuropsychTests" }
      }
    },

    "Psychometrics": {
      "type": "object",
      "properties": {
        "reliability_alpha": { "type": "number" },
        "test_retest_stability": { "type": "number" },
        "factor_structure": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },

    "NeuropsychTests": {
      "type": "object",
      "properties": {
        "task_battery": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "task_name": { "type": "string" },
              "score": { "type": "number" },
              "normative_z": { "type": "number" }
            }
          }
        }
      }
    },

    "AnchoringConstraints": {
      "type": "object",
      "properties": {
        "circuit_mappings": { "$ref": "#/$defs/CircuitMappings" },
        "neurophys_signatures": { "$ref": "#/$defs/NeurophysSignatures" },
        "pharmacological_profiles": { "$ref": "#/$defs/PharmacologicalProfiles" }
      }
    },

    "CircuitMappings": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "region": { "type": "string" },
          "associated_function": { "type": "string" },
          "lesion_effect": { "type": "string" }
        }
      }
    },

    "NeurophysSignatures": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "task": { "type": "string" },
          "frequency_band": { "type": "string" },
          "amplitude": { "type": "number" },
          "latency": { "type": "number" }
        }
      }
    },

    "PharmacologicalProfiles": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "agent": { "type": "string" },
          "receptor_target": { "type": "string" },
          "effect_profile": { "type": "string" }
        }
      }
    }
  }
}
```
```json

{
  "behavioral_layer": {
    "conditioning_models": {
      "classical": {
        "cs_us_mapping": ["tone → airpuff", "light → mild startle"],
        "acquisition_rate": 0.42,
        "extinction_rate": 0.18
      },
      "operant": {
        "reinforcement_schedule": "VI-30",
        "learning_rate": 0.21,
        "discount_factor": 0.87
      }
    },
    "performance_metrics": {
      "reaction_time_distribution": [412, 398, 405, 421, 389, 402],
      "accuracy": 0.93,
      "error_types": ["omission", "commission"],
      "speed_accuracy_tradeoff": {
        "slope": -0.0041,
        "intercept": 0.97
      }
    }
  },

  "cognitive_layer": {
    "working_memory": {
      "capacity": 4,
      "decay_rate": 0.12,
      "refresh_rate": 0.31
    },
    "attention": {
      "selective_filter_strength": 0.74,
      "sustained_attention_stability": 0.81,
      "switching_cost": 142
    },
    "decision_models": {
      "drift_diffusion": {
        "drift_rate": 0.28,
        "boundary_separation": 1.12,
        "non_decision_time": 0.29
      },
      "signal_detection": {
        "sensitivity_d_prime": 1.84,
        "criterion_c": -0.12
      }
    },
    "learning_models": {
      "reinforcement_learning": {
        "learning_rate": 0.19,
        "exploration_rate": 0.11,
        "reward_sensitivity": 0.63
      }
    }
  },

  "measurement_layer": {
    "psychometrics": {
      "reliability_alpha": 0.91,
      "test_retest_stability": 0.88,
      "factor_structure": ["WM", "ATTN", "EXEC"]
    },
    "neuropsych_tests": {
      "task_battery": [
        {
          "task_name": "Digit Span",
          "score": 12,
          "normative_z": 0.45
        },
        {
          "task_name": "Stroop Interference",
          "score": 37,
          "normative_z": -0.22
        },
        {
          "task_name": "Trail Making B",
          "score": 74,
          "normative_z": 0.10
        }
      ]
    }
  },

  "anchoring_constraints": {
    "circuit_mappings": [
      {
        "region": "DLPFC",
        "associated_function": "working memory manipulation",
        "lesion_effect": "reduced WM capacity and increased distractibility"
      },
      {
        "region": "ACC",
        "associated_function": "conflict monitoring",
        "lesion_effect": "elevated error rates under high-conflict trials"
      }
    ],
    "neurophys_signatures": [
      {
        "task": "Go/No-Go",
        "frequency_band": "theta",
        "amplitude": 4.7,
        "latency": 310
      },
      {
        "task": "Oddball",
        "frequency_band": "P300",
        "amplitude": 11.2,
        "latency": 342
      }
    ],
    "pharmacological_profiles": [
      {
        "agent": "methylphenidate",
        "receptor_target": "DAT/NET blockade",
        "effect_profile": "increased drift rate and reduced RT variability"
      },
      {
        "agent": "lorazepam",
        "receptor_target": "GABA-A modulation",
        "effect_profile": "increased non-decision time and reduced d'"
      }
    ]
  }
}
```
# **ct_example_annotations.md**  
### *Human‑readable explanation of every field in `ct_example.json`*

This document explains the meaning of each field in the **Conscious Transfer Substrate Map v1** example instance.  
It is written for clarity, not for formal specification — the schema remains the authoritative source.

---

# **1. Behavioral Layer**

The behavioral layer captures **observable, repeatable patterns** in how an agent learns and performs tasks.

## **1.1 Conditioning Models**

### **classical.cs_us_mapping**  
Pairs of stimuli showing which conditioned stimulus (CS) predicts which unconditioned stimulus (US).  
Example: “tone → airpuff” means the tone reliably precedes an airpuff.

### **classical.acquisition_rate**  
How quickly the agent learns the CS–US association.

### **classical.extinction_rate**  
How quickly the association fades when the CS is no longer followed by the US.

### **operant.reinforcement_schedule**  
The rule governing when rewards are delivered (e.g., variable interval 30 seconds).

### **operant.learning_rate**  
How strongly new outcomes update behavior.

### **operant.discount_factor**  
How much future rewards matter relative to immediate ones.

---

## **1.2 Performance Metrics**

### **reaction_time_distribution**  
A sample of reaction times (in milliseconds) from a standard task.

### **accuracy**  
Proportion of correct responses.

### **error_types**  
Categories of mistakes the agent makes (e.g., omissions, commissions).

### **speed_accuracy_tradeoff.slope / intercept**  
How the agent balances speed vs. accuracy — a stable behavioral signature.

---

# **2. Cognitive Layer**

The cognitive layer captures **task‑bound computational operators** that survive RTT filtering.

## **2.1 Working Memory**

### **capacity**  
How many items can be actively maintained at once.

### **decay_rate**  
How quickly information fades without rehearsal.

### **refresh_rate**  
How quickly the agent can refresh or cycle items to keep them active.

---

## **2.2 Attention**

### **selective_filter_strength**  
How effectively irrelevant information is filtered out.

### **sustained_attention_stability**  
How consistently attention is maintained over time.

### **switching_cost**  
Extra time required to switch between tasks or rules.

---

## **2.3 Decision Models**

### **drift_diffusion.drift_rate**  
How quickly evidence accumulates toward a decision.

### **drift_diffusion.boundary_separation**  
How cautious or bold the decision threshold is.

### **drift_diffusion.non_decision_time**  
Time spent on perception and motor execution, not decision‑making.

### **signal_detection.sensitivity_d_prime**  
How well the agent distinguishes signal from noise.

### **signal_detection.criterion_c**  
Bias toward saying “yes” or “no” when uncertain.

---

## **2.4 Learning Models**

### **reinforcement_learning.learning_rate**  
How strongly new outcomes update value estimates.

### **reinforcement_learning.exploration_rate**  
How often the agent tries new actions instead of exploiting known ones.

### **reinforcement_learning.reward_sensitivity**  
How strongly rewards influence behavior.

---

# **3. Measurement Layer**

The measurement layer defines **how the substrate is validated**, not the substrate itself.

## **3.1 Psychometrics**

### **reliability_alpha**  
Internal consistency of measurement instruments.

### **test_retest_stability**  
How stable scores are across repeated testing.

### **factor_structure**  
Latent dimensions extracted from performance (e.g., working memory, attention).

---

## **3.2 Neuropsych Tests**

### **task_battery.task_name**  
Name of a standardized cognitive test.

### **task_battery.score**  
Raw performance score.

### **task_battery.normative_z**  
How the score compares to population norms (in standard deviations).

---

# **4. Anchoring Constraints**

These are **biological correlates** that meet RTT criteria — stable, traceable, and functionally meaningful.

## **4.1 Circuit Mappings**

### **region**  
Brain region with a known functional role.

### **associated_function**  
What cognitive/behavioral process the region supports.

### **lesion_effect**  
What happens when the region is damaged — a functional anchor.

---

## **4.2 Neurophysiological Signatures**

### **task**  
The task during which the signature appears.

### **frequency_band**  
EEG/MEG frequency or ERP component.

### **amplitude**  
Strength of the signal.

### **latency**  
Time delay between stimulus and neural response.

---

## **4.3 Pharmacological Profiles**

### **agent**  
Drug or compound with a known effect profile.

### **receptor_target**  
Primary biological target (e.g., dopamine transporter).

### **effect_profile**  
How the agent modulates behavior or cognitive parameters.

---

# **How to Use This File**

This annotation file is meant to:

- help researchers understand the meaning of each field  
- support onboarding into the Conscious Transfer substrate  
- clarify how the example instance relates to the schema  
- maintain conceptual cleanliness without narrative drift  

It is not a substitute for the schema — it is a **guide** to interpreting instances.
```json

{
  "behavioral_layer": {
    "conditioning_models": {
      "classical": {
        "cs_us_mapping": [
          "tone → airpuff",
          "light → mild startle",
          "vibration → reward cue"
        ],
        "acquisition_rate": 0.47,
        "extinction_rate": 0.16
      },
      "operant": {
        "reinforcement_schedule": "VR-12",
        "learning_rate": 0.24,
        "discount_factor": 0.91
      }
    },
    "performance_metrics": {
      "reaction_time_distribution": [
        412, 398, 405, 421, 389, 402, 395, 417, 409, 393
      ],
      "accuracy": 0.94,
      "error_types": [
        "omission",
        "commission",
        "intrusion"
      ],
      "speed_accuracy_tradeoff": {
        "slope": -0.0038,
        "intercept": 0.98
      }
    }
  },

  "cognitive_layer": {
    "working_memory": {
      "capacity": 5,
      "decay_rate": 0.11,
      "refresh_rate": 0.34
    },
    "attention": {
      "selective_filter_strength": 0.78,
      "sustained_attention_stability": 0.83,
      "switching_cost": 128
    },
    "decision_models": {
      "drift_diffusion": {
        "drift_rate": 0.31,
        "boundary_separation": 1.18,
        "non_decision_time": 0.27
      },
      "signal_detection": {
        "sensitivity_d_prime": 1.92,
        "criterion_c": -0.08
      }
    },
    "learning_models": {
      "reinforcement_learning": {
        "learning_rate": 0.22,
        "exploration_rate": 0.14,
        "reward_sensitivity": 0.67
      }
    }
  },

  "measurement_layer": {
    "psychometrics": {
      "reliability_alpha": 0.93,
      "test_retest_stability": 0.89,
      "factor_structure": [
        "WM",
        "ATTN",
        "EXEC",
        "RL"
      ]
    },
    "neuropsych_tests": {
      "task_battery": [
        {
          "task_name": "Digit Span",
          "score": 13,
          "normative_z": 0.62
        },
        {
          "task_name": "Stroop Interference",
          "score": 35,
          "normative_z": -0.10
        },
        {
          "task_name": "Trail Making A",
          "score": 29,
          "normative_z": 0.55
        },
        {
          "task_name": "Trail Making B",
          "score": 71,
          "normative_z": 0.18
        },
        {
          "task_name": "N‑Back (2‑back)",
          "score": 87,
          "normative_z": 0.41
        }
      ]
    }
  },

  "anchoring_constraints": {
    "circuit_mappings": [
      {
        "region": "DLPFC",
        "associated_function": "working memory manipulation",
        "lesion_effect": "reduced WM capacity and increased distractibility"
      },
      {
        "region": "ACC",
        "associated_function": "conflict monitoring",
        "lesion_effect": "elevated error rates under high-conflict trials"
      },
      {
        "region": "Ventral Striatum",
        "associated_function": "reward prediction",
        "lesion_effect": "flattened reward sensitivity and impaired RL updating"
      }
    ],
    "neurophys_signatures": [
      {
        "task": "Go/No-Go",
        "frequency_band": "theta",
        "amplitude": 4.9,
        "latency": 308
      },
      {
        "task": "Oddball",
        "frequency_band": "P300",
        "amplitude": 11.7,
        "latency": 339
      },
      {
        "task": "Flanker",
        "frequency_band": "ERN",
        "amplitude": -5.1,
        "latency": 92
      }
    ],
    "pharmacological_profiles": [
      {
        "agent": "methylphenidate",
        "receptor_target": "DAT/NET blockade",
        "effect_profile": "increased drift rate, reduced RT variability, improved WM stability"
      },
      {
        "agent": "lorazepam",
        "receptor_target": "GABA-A modulation",
        "effect_profile": "increased non-decision time, reduced d', reduced selective filter strength"
      },
      {
        "agent": "modafinil",
        "receptor_target": "DAT inhibition + orexin modulation",
        "effect_profile": "enhanced sustained attention stability and reduced switching cost"
      }
    ]
  }
}
```
```json

{
  "behavioral_layer": {
    "conditioning_models": {
      "classical": {
        "cs_us_mapping": [],
        "acquisition_rate": 0.0,
        "extinction_rate": 0.0
      },
      "operant": {
        "reinforcement_schedule": "FR-1",
        "learning_rate": 0.0,
        "discount_factor": 0.0
      }
    },
    "performance_metrics": {
      "reaction_time_distribution": [],
      "accuracy": 0.0,
      "error_types": [],
      "speed_accuracy_tradeoff": {
        "slope": 0.0,
        "intercept": 0.0
      }
    }
  },

  "cognitive_layer": {
    "working_memory": {
      "capacity": 0,
      "decay_rate": 0.0,
      "refresh_rate": 0.0
    },
    "attention": {
      "selective_filter_strength": 0.0,
      "sustained_attention_stability": 0.0,
      "switching_cost": 0
    },
    "decision_models": {
      "drift_diffusion": {
        "drift_rate": 0.0,
        "boundary_separation": 0.0,
        "non_decision_time": 0.0
      },
      "signal_detection": {
        "sensitivity_d_prime": 0.0,
        "criterion_c": 0.0
      }
    },
    "learning_models": {
      "reinforcement_learning": {
        "learning_rate": 0.0,
        "exploration_rate": 0.0,
        "reward_sensitivity": 0.0
      }
    }
  },

  "measurement_layer": {
    "psychometrics": {
      "reliability_alpha": 0.0,
      "test_retest_stability": 0.0,
      "factor_structure": []
    },
    "neuropsych_tests": {
      "task_battery": []
    }
  },

  "anchoring_constraints": {
    "circuit_mappings": [],
    "neurophys_signatures": [],
    "pharmacological_profiles": []
  }
}
```
