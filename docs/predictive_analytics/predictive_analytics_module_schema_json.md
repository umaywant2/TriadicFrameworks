# predictive_analytics_module_schema_json.md

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://www.triadicframeworks.org/schemas/predictive_analytics_module.schema.json",
  "title": "TriadicFrameworks Predictive Analytics Module Schema",
  "description": "Structural schema for the Predictive Analytics module manifest, including substrate-aware observation, model adapters, RTT extensions, Resonant IQ Fingerprint dimensions, validation criteria, metrics, ethical limits, examples, and navigation.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "predictive_analytics_module"
  ],
  "properties": {
    "predictive_analytics_module": {
      "$ref": "#/$defs/module"
    }
  },
  "$defs": {
    "nonEmptyString": {
      "type": "string",
      "minLength": 1
    },
    "identifier": {
      "type": "string",
      "minLength": 1,
      "pattern": "^[a-z0-9]+(?:[a-z0-9._-]*[a-z0-9])?$"
    },
    "operatorIdentifier": {
      "type": "string",
      "pattern": "^PA-[A-Z][A-Z0-9-]*$"
    },
    "metricIdentifier": {
      "type": "string",
      "pattern": "^PA-M[0-9]{2,3}$"
    },
    "criterionIdentifier": {
      "type": "string",
      "pattern": "^VCR-[0-9]{2,3}$"
    },
    "semanticVersion": {
      "type": "string",
      "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+(?:-[0-9A-Za-z.-]+)?(?:\\+[0-9A-Za-z.-]+)?$"
    },
    "relativePath": {
      "type": "string",
      "minLength": 1,
      "pattern": "^(?![a-zA-Z][a-zA-Z0-9+.-]*:)(?!/).+$"
    },
    "markdownPath": {
      "allOf": [
        {
          "$ref": "#/$defs/relativePath"
        },
        {
          "pattern": "\\.md$"
        }
      ]
    },
    "jsonPath": {
      "allOf": [
        {
          "$ref": "#/$defs/relativePath"
        },
        {
          "pattern": "\\.json$"
        }
      ]
    },
    "htmlPath": {
      "allOf": [
        {
          "$ref": "#/$defs/relativePath"
        },
        {
          "pattern": "\\.html$"
        }
      ]
    },
    "stringList": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/nonEmptyString"
      },
      "uniqueItems": true
    },
    "identifierList": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/identifier"
      },
      "uniqueItems": true
    },
    "confidence": {
      "type": "string",
      "enum": [
        "none",
        "very_low",
        "low",
        "medium",
        "high",
        "very_high",
        "unknown",
        "not_applicable"
      ]
    },
    "lifecycleState": {
      "type": "string",
      "enum": [
        "proposed",
        "experimental",
        "pilot",
        "validated_for_context",
        "restricted",
        "deprecated",
        "rejected"
      ]
    },
    "validationState": {
      "type": "string",
      "enum": [
        "unvalidated",
        "structurally_validated",
        "content_reviewed",
        "measurement_pilot",
        "construct_pilot",
        "substrate_validated",
        "predictively_validated",
        "fairness_reviewed",
        "decision_validated",
        "deprecated"
      ]
    },
    "applicabilityState": {
      "type": "string",
      "enum": [
        "applicable",
        "substrate_dependent",
        "unsupported",
        "unknown",
        "not_applicable"
      ]
    },
    "observationState": {
      "type": "string",
      "enum": [
        "observed",
        "partially_observed",
        "not_observed",
        "insufficient_evidence",
        "conflicting_evidence",
        "unknown",
        "not_applicable"
      ]
    },
    "direction": {
      "type": "string",
      "enum": [
        "higher_is_better",
        "lower_is_better",
        "target_range",
        "descriptive",
        "context_dependent"
      ]
    },
    "module": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "version",
        "id",
        "name",
        "description",
        "state",
        "generated_at",
        "source_repo",
        "source_path",
        "architecture",
        "lineage",
        "ai_metadata",
        "operators",
        "roles",
        "analyzer_layers",
        "adapters",
        "dimensions",
        "validation",
        "metrics",
        "ethics",
        "examples",
        "documents",
        "navigation"
      ],
      "properties": {
        "version": {
          "$ref": "#/$defs/semanticVersion"
        },
        "id": {
          "type": "string",
          "const": "predictive-analytics"
        },
        "name": {
          "type": "string",
          "const": "Predictive Analytics"
        },
        "short_name": {
          "type": "string",
          "default": "PA"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "tagline": {
          "type": "string",
          "default": "Predict the observation. Observe the predictor."
        },
        "category": {
          "type": "string",
          "enum": [
            "predictive-structural",
            "analytics-structural",
            "research-experimental"
          ],
          "default": "predictive-structural"
        },
        "state": {
          "$ref": "#/$defs/state"
        },
        "generated_at": {
          "type": "string",
          "format": "date-time"
        },
        "last_modified": {
          "type": "string",
          "format": "date"
        },
        "source_repo": {
          "type": "string",
          "format": "uri"
        },
        "source_path": {
          "type": "string",
          "const": "docs/predictive_analytics"
        },
        "canonical_url": {
          "type": "string",
          "format": "uri"
        },
        "license": {
          "type": "string",
          "default": "MIT"
        },
        "architecture": {
          "$ref": "#/$defs/architecture"
        },
        "lineage": {
          "$ref": "#/$defs/lineage"
        },
        "ai_metadata": {
          "$ref": "#/$defs/aiMetadata"
        },
        "operators": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/operator"
          }
        },
        "roles": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/role"
          }
        },
        "analyzer_layers": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/analyzerLayer"
          }
        },
        "adapters": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/adapter"
          }
        },
        "dimensions": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/dimension"
          }
        },
        "validation": {
          "$ref": "#/$defs/validation"
        },
        "metrics": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/metric"
          }
        },
        "ethics": {
          "$ref": "#/$defs/ethics"
        },
        "examples": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/example"
          }
        },
        "documents": {
          "type": "object",
          "minProperties": 1,
          "additionalProperties": {
            "$ref": "#/$defs/document"
          }
        },
        "navigation": {
          "$ref": "#/$defs/navigation"
        }
      }
    },
    "state": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "rtt",
        "coherence",
        "drift",
        "paradox",
        "regime",
        "lifecycle",
        "validation"
      ],
      "properties": {
        "rtt": {
          "type": "integer",
          "minimum": 0,
          "maximum": 1
        },
        "coherence": {
          "type": "string",
          "enum": [
            "unknown",
            "declared",
            "provisional",
            "stable",
            "validated",
            "degraded"
          ]
        },
        "drift": {
          "type": "string",
          "enum": [
            "unknown",
            "minimal",
            "bounded",
            "elevated",
            "unbounded"
          ]
        },
        "paradox": {
          "type": "string",
          "enum": [
            "none",
            "observed",
            "preserved",
            "structural",
            "unresolved"
          ]
        },
        "regime": {
          "type": "string",
          "enum": [
            "predictive",
            "structural",
            "predictive-structural",
            "experimental"
          ]
        },
        "lifecycle": {
          "$ref": "#/$defs/lifecycleState"
        },
        "validation": {
          "$ref": "#/$defs/validationState"
        },
        "decision_authority": {
          "type": "string",
          "enum": [
            "none",
            "research_only",
            "advisory",
            "context_validated",
            "prohibited"
          ],
          "default": "none"
        }
      }
    },
    "architecture": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "pattern",
        "primary_pipeline",
        "observation_boundary",
        "scalar_policy",
        "standalone_mode"
      ],
      "properties": {
        "pattern": {
          "type": "string",
          "enum": [
            "observer-adapter",
            "substrate-aware-predictive",
            "comparative-assessment"
          ]
        },
        "primary_pipeline": {
          "type": "array",
          "minItems": 2,
          "items": {
            "$ref": "#/$defs/nonEmptyString"
          }
        },
        "observation_boundary": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "scalar_policy": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "primary_representation",
            "composites_allowed",
            "loss_warning_required",
            "hidden_master_score_prohibited"
          ],
          "properties": {
            "primary_representation": {
              "type": "string",
              "enum": [
                "multidimensional_profile",
                "profile_topology",
                "comparative_assessment"
              ]
            },
            "composites_allowed": {
              "type": "boolean"
            },
            "loss_warning_required": {
              "type": "boolean",
              "const": true
            },
            "hidden_master_score_prohibited": {
              "type": "boolean",
              "const": true
            }
          }
        },
        "supports_human_observation": {
          "type": "boolean",
          "default": true
        },
        "supports_ai_observation": {
          "type": "boolean",
          "default": true
        },
        "supports_team_observation": {
          "type": "boolean",
          "default": true
        },
        "supports_organizational_observation": {
          "type": "boolean",
          "default": true
        },
        "standalone_mode": {
          "type": "boolean"
        }
      }
    },
    "lineage": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "version",
        "origin",
        "architecture",
        "note"
      ],
      "properties": {
        "version": {
          "$ref": "#/$defs/semanticVersion"
        },
        "previous_version": {
          "$ref": "#/$defs/semanticVersion"
        },
        "origin": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "promoted_at": {
          "type": "string",
          "format": "date-time"
        },
        "source_repo": {
          "type": "string",
          "format": "uri"
        },
        "source_path": {
          "$ref": "#/$defs/relativePath"
        },
        "architecture": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "parent_modules": {
          "$ref": "#/$defs/stringList"
        },
        "canon_dependencies": {
          "$ref": "#/$defs/stringList"
        },
        "note": {
          "$ref": "#/$defs/nonEmptyString"
        }
      }
    },
    "aiMetadata": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "schema_version",
        "embedding_strategy",
        "chunk_boundary",
        "context_window_advisory",
        "retrieval_hint",
        "semantic_tags",
        "model_compatibility",
        "standalone_mode",
        "generation_ts"
      ],
      "properties": {
        "schema_version": {
          "$ref": "#/$defs/semanticVersion"
        },
        "embedding_strategy": {
          "type": "string",
          "enum": [
            "per-doc-standalone",
            "section-aware",
            "profile-aware",
            "adapter-aware",
            "hybrid"
          ]
        },
        "chunk_boundary": {
          "type": "string",
          "enum": [
            "document",
            "section-heading",
            "dimension",
            "adapter",
            "metric",
            "observation-record"
          ]
        },
        "context_window_advisory": {
          "type": "string",
          "enum": [
            "small",
            "medium",
            "large",
            "extended"
          ]
        },
        "injection_pattern": {
          "type": "string",
          "enum": [
            "foundation-first",
            "adapter-first",
            "profile-first",
            "validation-first",
            "task-specific"
          ]
        },
        "retrieval_hint": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "semantic_tags": {
          "$ref": "#/$defs/stringList"
        },
        "model_compatibility": {
          "$ref": "#/$defs/stringList"
        },
        "audience": {
          "$ref": "#/$defs/stringList"
        },
        "standalone_mode": {
          "type": "boolean"
        },
        "generation_ts": {
          "type": "string",
          "format": "date-time"
        }
      }
    },
    "operator": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "label",
        "description",
        "inputs",
        "outputs",
        "status"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/operatorIdentifier"
        },
        "label": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "inputs": {
          "$ref": "#/$defs/stringList"
        },
        "outputs": {
          "$ref": "#/$defs/stringList"
        },
        "status": {
          "$ref": "#/$defs/lifecycleState"
        },
        "requires_human_review": {
          "type": "boolean"
        },
        "related_adapters": {
          "$ref": "#/$defs/identifierList"
        },
        "related_metrics": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/metricIdentifier"
          },
          "uniqueItems": true
        }
      }
    },
    "role": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "label",
        "description"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/identifier"
        },
        "label": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "allowed_document_types": {
          "$ref": "#/$defs/stringList"
        }
      }
    },
    "analyzerLayer": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "label",
        "description",
        "primary_documents"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/identifier"
        },
        "label": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "primary_documents": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/markdownPath"
          },
          "uniqueItems": true
        },
        "adapter_refs": {
          "$ref": "#/$defs/identifierList"
        },
        "operator_refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/operatorIdentifier"
          },
          "uniqueItems": true
        },
        "metric_refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/metricIdentifier"
          },
          "uniqueItems": true
        }
      }
    },
    "adapter": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name",
        "description",
        "status",
        "source_framework",
        "purpose",
        "supported_inputs",
        "outputs",
        "claims",
        "limitations",
        "validation_state"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/identifier"
        },
        "name": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "status": {
          "$ref": "#/$defs/lifecycleState"
        },
        "source_framework": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "source_document": {
          "$ref": "#/$defs/markdownPath"
        },
        "purpose": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "supported_inputs": {
          "$ref": "#/$defs/stringList"
        },
        "unsupported_inputs": {
          "$ref": "#/$defs/stringList"
        },
        "outputs": {
          "$ref": "#/$defs/stringList"
        },
        "claims": {
          "$ref": "#/$defs/stringList"
        },
        "limitations": {
          "$ref": "#/$defs/stringList"
        },
        "confounds": {
          "$ref": "#/$defs/stringList"
        },
        "validation_state": {
          "$ref": "#/$defs/validationState"
        },
        "ablation_metric": {
          "type": "string",
          "const": "PA-M36"
        },
        "decision_authority": {
          "type": "string",
          "enum": [
            "none",
            "advisory",
            "context_validated"
          ],
          "default": "none"
        }
      }
    },
    "dimension": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name",
        "description",
        "status",
        "operational_definition",
        "observable_indicators",
        "counter_indicators",
        "supported_substrates",
        "known_confounds",
        "applicability",
        "evidence_requirements",
        "validation_state"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/identifier"
        },
        "name": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "status": {
          "$ref": "#/$defs/lifecycleState"
        },
        "operational_definition": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "exclusions": {
          "$ref": "#/$defs/stringList"
        },
        "observable_indicators": {
          "$ref": "#/$defs/stringList"
        },
        "counter_indicators": {
          "$ref": "#/$defs/stringList"
        },
        "supported_substrates": {
          "$ref": "#/$defs/identifierList"
        },
        "known_confounds": {
          "$ref": "#/$defs/stringList"
        },
        "applicability": {
          "type": "object",
          "minProperties": 1,
          "additionalProperties": {
            "$ref": "#/$defs/applicabilityState"
          }
        },
        "evidence_requirements": {
          "$ref": "#/$defs/evidenceRequirements"
        },
        "preferred_expressions": {
          "$ref": "#/$defs/stringList"
        },
        "possible_suppressors": {
          "$ref": "#/$defs/stringList"
        },
        "related_dimensions": {
          "$ref": "#/$defs/identifierList"
        },
        "metric_refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/metricIdentifier"
          },
          "uniqueItems": true
        },
        "validation_state": {
          "$ref": "#/$defs/validationState"
        }
      }
    },
    "evidenceRequirements": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "minimum_independent_sources",
        "replication_required",
        "counterevidence_required",
        "traceability_required"
      ],
      "properties": {
        "minimum_independent_sources": {
          "type": "integer",
          "minimum": 1
        },
        "replication_required": {
          "type": "boolean"
        },
        "counterevidence_required": {
          "type": "boolean"
        },
        "traceability_required": {
          "type": "boolean",
          "const": true
        },
        "minimum_confidence": {
          "$ref": "#/$defs/confidence"
        },
        "allowed_evidence_types": {
          "$ref": "#/$defs/stringList"
        }
      }
    },
    "validation": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "state",
        "authorized_uses",
        "prohibited_uses",
        "levels",
        "criteria",
        "falsification_conditions",
        "reporting_requirements"
      ],
      "properties": {
        "state": {
          "$ref": "#/$defs/validationState"
        },
        "authorized_uses": {
          "$ref": "#/$defs/stringList"
        },
        "prohibited_uses": {
          "$ref": "#/$defs/stringList"
        },
        "levels": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/validationLevel"
          }
        },
        "criteria": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/validationCriterion"
          }
        },
        "falsification_conditions": {
          "$ref": "#/$defs/stringList"
        },
        "reporting_requirements": {
          "$ref": "#/$defs/stringList"
        },
        "threshold_policy": {
          "$ref": "#/$defs/thresholdPolicy"
        },
        "human_subjects_requirements": {
          "$ref": "#/$defs/stringList"
        }
      }
    },
    "validationLevel": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "level",
        "id",
        "name",
        "description",
        "requirements",
        "status"
      ],
      "properties": {
        "level": {
          "type": "integer",
          "minimum": 0,
          "maximum": 7
        },
        "id": {
          "$ref": "#/$defs/identifier"
        },
        "name": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "requirements": {
          "$ref": "#/$defs/stringList"
        },
        "status": {
          "type": "string",
          "enum": [
            "not_started",
            "in_progress",
            "passed",
            "failed",
            "not_applicable"
          ]
        },
        "evidence_refs": {
          "$ref": "#/$defs/stringList"
        }
      }
    },
    "validationCriterion": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name",
        "description",
        "pass_condition",
        "status"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/criterionIdentifier"
        },
        "name": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "pass_condition": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "failure_condition": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "metric_refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/metricIdentifier"
          },
          "uniqueItems": true
        },
        "status": {
          "type": "string",
          "enum": [
            "proposed",
            "not_tested",
            "testing",
            "passed",
            "failed",
            "inconclusive"
          ]
        }
      }
    },
    "thresholdPolicy": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "status",
        "universal_thresholds",
        "preregistration_required",
        "post_hoc_changes_disclosed"
      ],
      "properties": {
        "status": {
          "type": "string",
          "enum": [
            "study_specific",
            "context_validated",
            "fixed"
          ]
        },
        "universal_thresholds": {
          "type": "boolean",
          "default": false
        },
        "preregistration_required": {
          "type": "boolean"
        },
        "post_hoc_changes_disclosed": {
          "type": "boolean",
          "const": true
        }
      }
    },
    "metric": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name",
        "category",
        "purpose",
        "definition",
        "scale",
        "direction",
        "inputs",
        "applicability",
        "interpretation",
        "limitations",
        "subgroup_required",
        "lifecycle",
        "threshold"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/metricIdentifier"
        },
        "name": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "category": {
          "type": "string",
          "enum": [
            "evidence",
            "reliability",
            "stability",
            "validity",
            "substrate",
            "regime",
            "model_mismatch",
            "coherence",
            "drift",
            "uncertainty",
            "calibration",
            "counterfactual",
            "robustness",
            "fairness",
            "explainability",
            "review",
            "operational"
          ]
        },
        "purpose": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "definition": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "formula": {
          "type": "string"
        },
        "scale": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "direction": {
          "$ref": "#/$defs/direction"
        },
        "inputs": {
          "$ref": "#/$defs/stringList"
        },
        "applicability": {
          "$ref": "#/$defs/stringList"
        },
        "interpretation": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "limitations": {
          "$ref": "#/$defs/stringList"
        },
        "subgroup_required": {
          "type": "boolean"
        },
        "lifecycle": {
          "type": "string",
          "enum": [
            "proposed",
            "pilot",
            "validated",
            "restricted",
            "deprecated",
            "rejected"
          ]
        },
        "calculation_method": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "missing_data_policy": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "threshold": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "status"
          ],
          "properties": {
            "status": {
              "type": "string",
              "enum": [
                "unset",
                "study_specific",
                "provisional",
                "validated"
              ]
            },
            "value": {},
            "rationale": {
              "type": "string"
            },
            "validation_evidence": {
              "$ref": "#/$defs/stringList"
            },
            "review_date": {
              "type": "string",
              "format": "date"
            }
          }
        }
      }
    },
    "ethics": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "status",
        "principles",
        "invariants",
        "prohibited_uses",
        "high_stakes_policy",
        "consent",
        "privacy",
        "contestability",
        "temporal_limits",
        "human_review",
        "misuse_boundary"
      ],
      "properties": {
        "status": {
          "$ref": "#/$defs/lifecycleState"
        },
        "principles": {
          "$ref": "#/$defs/stringList"
        },
        "invariants": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "enum": [
              "prediction != identity",
              "measurement != total_capability",
              "capability != human_worth",
              "detail != validity",
              "complexity != truth",
              "correlation != causation",
              "profile != destiny",
              "model_fit != subject_value",
              "unknown != failure",
              "difference != superiority"
            ]
          },
          "uniqueItems": true
        },
        "prohibited_uses": {
          "$ref": "#/$defs/stringList"
        },
        "high_stakes_policy": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "decision_authority",
            "independent_use",
            "separate_validation_required"
          ],
          "properties": {
            "decision_authority": {
              "type": "string",
              "enum": [
                "none",
                "research_only",
                "advisory",
                "context_validated"
              ]
            },
            "independent_use": {
              "type": "boolean",
              "default": false
            },
            "separate_validation_required": {
              "type": "boolean",
              "const": true
            }
          }
        },
        "consent": {
          "$ref": "#/$defs/governanceControl"
        },
        "privacy": {
          "$ref": "#/$defs/governanceControl"
        },
        "contestability": {
          "$ref": "#/$defs/governanceControl"
        },
        "temporal_limits": {
          "$ref": "#/$defs/governanceControl"
        },
        "accessibility": {
          "$ref": "#/$defs/governanceControl"
        },
        "fairness": {
          "$ref": "#/$defs/governanceControl"
        },
        "human_review": {
          "$ref": "#/$defs/governanceControl"
        },
        "misuse_boundary": {
          "$ref": "#/$defs/stringList"
        },
        "known_limits": {
          "$ref": "#/$defs/stringList"
        },
        "deprecation_supported": {
          "type": "boolean",
          "const": true
        }
      }
    },
    "governanceControl": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "required",
        "description"
      ],
      "properties": {
        "required": {
          "type": "boolean"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "requirements": {
          "$ref": "#/$defs/stringList"
        },
        "exceptions": {
          "$ref": "#/$defs/stringList"
        }
      }
    },
    "example": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "name",
        "type",
        "file",
        "synthetic",
        "validation_state",
        "decision_authority"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/identifier"
        },
        "name": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "type": {
          "type": "string",
          "enum": [
            "resonant_iq_fingerprint",
            "model_mismatch",
            "substrate_comparison",
            "regime_transition",
            "counterfactual",
            "general"
          ]
        },
        "file": {
          "$ref": "#/$defs/markdownPath"
        },
        "synthetic": {
          "type": "boolean"
        },
        "subject_id": {
          "type": "string"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "validation_state": {
          "$ref": "#/$defs/validationState"
        },
        "decision_authority": {
          "type": "string",
          "enum": [
            "none",
            "research_only",
            "advisory",
            "context_validated"
          ]
        },
        "dimensions_used": {
          "$ref": "#/$defs/identifierList"
        },
        "adapters_used": {
          "$ref": "#/$defs/identifierList"
        },
        "metric_refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/metricIdentifier"
          },
          "uniqueItems": true
        }
      }
    },
    "document": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "id",
        "file",
        "role",
        "status",
        "anchor",
        "standalone"
      ],
      "properties": {
        "id": {
          "$ref": "#/$defs/identifier"
        },
        "file": {
          "oneOf": [
            {
              "$ref": "#/$defs/markdownPath"
            },
            {
              "$ref": "#/$defs/jsonPath"
            },
            {
              "$ref": "#/$defs/htmlPath"
            }
          ]
        },
        "role": {
          "$ref": "#/$defs/identifier"
        },
        "status": {
          "$ref": "#/$defs/lifecycleState"
        },
        "anchor": {
          "type": "string",
          "pattern": "^#[A-Za-z0-9_-]+$"
        },
        "standalone": {
          "type": "boolean"
        },
        "description": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "adapter_refs": {
          "$ref": "#/$defs/identifierList"
        },
        "dimension_refs": {
          "$ref": "#/$defs/identifierList"
        },
        "metric_refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/metricIdentifier"
          },
          "uniqueItems": true
        },
        "validation_refs": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/criterionIdentifier"
          },
          "uniqueItems": true
        }
      }
    },
    "navigation": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "index_path",
        "readme_path",
        "module_path",
        "schema_path",
        "default_document",
        "anchor_style",
        "sections",
        "doc_anchors"
      ],
      "properties": {
        "index_path": {
          "$ref": "#/$defs/htmlPath"
        },
        "readme_path": {
          "$ref": "#/$defs/markdownPath"
        },
        "module_path": {
          "$ref": "#/$defs/jsonPath"
        },
        "schema_path": {
          "$ref": "#/$defs/jsonPath"
        },
        "default_document": {
          "$ref": "#/$defs/markdownPath"
        },
        "anchor_style": {
          "type": "string",
          "enum": [
            "uppercase-doc-map",
            "lowercase-slug",
            "mixed"
          ]
        },
        "sections": {
          "type": "object",
          "minProperties": 1,
          "additionalProperties": {
            "type": "string",
            "pattern": "^#[A-Za-z0-9_-]+$"
          }
        },
        "doc_anchors": {
          "type": "object",
          "minProperties": 1,
          "additionalProperties": {
            "type": "string",
            "pattern": "^#[A-Za-z0-9_-]+$"
          }
        }
      }
    },
    "observationRecord": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "observation_id",
        "observed_system",
        "task_id",
        "substrate_id",
        "regime_id",
        "timestamp",
        "evaluator",
        "evidence_reference",
        "dimension_id",
        "state",
        "confidence",
        "limitations"
      ],
      "properties": {
        "observation_id": {
          "$ref": "#/$defs/identifier"
        },
        "observed_system": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "system_boundary": {
          "type": "string",
          "enum": [
            "individual_human",
            "ai_system",
            "human_ai_pair",
            "team",
            "organization",
            "robotic_system",
            "distributed_agents",
            "animal",
            "other"
          ]
        },
        "task_id": {
          "$ref": "#/$defs/identifier"
        },
        "substrate_id": {
          "$ref": "#/$defs/identifier"
        },
        "regime_id": {
          "$ref": "#/$defs/identifier"
        },
        "timestamp": {
          "type": "string",
          "format": "date-time"
        },
        "evaluator": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "evidence_reference": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "dimension_id": {
          "$ref": "#/$defs/identifier"
        },
        "state": {
          "$ref": "#/$defs/observationState"
        },
        "expression": {
          "type": "string",
          "enum": [
            "very_weak",
            "weak",
            "moderate",
            "strong",
            "very_strong",
            "variable",
            "unknown",
            "not_applicable"
          ]
        },
        "confidence": {
          "$ref": "#/$defs/confidence"
        },
        "stability": {
          "type": "string",
          "enum": [
            "unstable",
            "low",
            "moderate",
            "high",
            "unknown",
            "not_tested"
          ]
        },
        "scoring_rule": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "limitations": {
          "$ref": "#/$defs/stringList"
        },
        "alternative_interpretations": {
          "$ref": "#/$defs/stringList"
        },
        "recommended_action": {
          "$ref": "#/$defs/nonEmptyString"
        }
      }
    },
    "assessmentResult": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "assessment_id",
        "observed_system",
        "intended_use",
        "validation_state",
        "decision_authority",
        "observations",
        "uncertainty",
        "missing_evidence",
        "alternative_interpretations",
        "limitations",
        "review_path"
      ],
      "properties": {
        "assessment_id": {
          "$ref": "#/$defs/identifier"
        },
        "observed_system": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "intended_use": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "validation_state": {
          "$ref": "#/$defs/validationState"
        },
        "decision_authority": {
          "type": "string",
          "enum": [
            "none",
            "research_only",
            "advisory",
            "context_validated"
          ]
        },
        "observations": {
          "type": "array",
          "items": {
            "$ref": "#/$defs/observationRecord"
          }
        },
        "model_fit": {
          "type": "string",
          "enum": [
            "high",
            "moderate",
            "low",
            "mismatch_detected",
            "unresolved",
            "unknown"
          ]
        },
        "substrate_fit": {
          "type": "string",
          "enum": [
            "high",
            "moderate",
            "low",
            "partial",
            "mismatch_detected",
            "unresolved",
            "unknown"
          ]
        },
        "regime_fit": {
          "type": "string",
          "enum": [
            "high",
            "moderate",
            "low",
            "partial",
            "mismatch_detected",
            "unresolved",
            "unknown"
          ]
        },
        "uncertainty": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "missing_evidence": {
          "$ref": "#/$defs/stringList"
        },
        "alternative_interpretations": {
          "$ref": "#/$defs/stringList"
        },
        "limitations": {
          "$ref": "#/$defs/stringList"
        },
        "review_path": {
          "$ref": "#/$defs/nonEmptyString"
        },
        "composite": {
          "type": "object",
          "additionalProperties": false,
          "required": [
            "permitted",
            "interpretive_status",
            "sufficient_alone",
            "profile_required"
          ],
          "properties": {
            "permitted": {
              "type": "boolean"
            },
            "value": {},
            "interpretive_status": {
              "type": "string",
              "const": "lossy_projection"
            },
            "sufficient_alone": {
              "type": "boolean",
              "const": false
            },
            "profile_required": {
              "type": "boolean",
              "const": true
            }
          }
        }
      }
    }
  }
}
```
