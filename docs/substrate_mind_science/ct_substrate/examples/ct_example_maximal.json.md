```json

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
