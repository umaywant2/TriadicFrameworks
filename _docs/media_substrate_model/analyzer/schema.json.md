```json

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/media_substrate_model/analyzer/schema.json",
  "title": "Media Substrate Model Analyzer Schema",
  "description": "Input and output schema for the Media Substrate Model (MSM) Analyzer.",
  "type": "object",
  "properties": {
    "input": {
      "title": "Analyzer Input",
      "type": "object",
      "properties": {
        "vector": {
          "$ref": "#/$defs/MediaVector"
        },
        "metadata": {
          "type": "object",
          "description": "Optional adapter metadata used to refine analysis.",
          "additionalProperties": true
        }
      },
      "required": ["vector"],
      "additionalProperties": false
    },
    "output": {
      "title": "Analyzer Output",
      "type": "object",
      "properties": {
        "vector": {
          "$ref": "#/$defs/MediaVector"
        },
        "invariants": {
          "$ref": "#/$defs/MediaInvariantState"
        },
        "basin": {
          "$ref": "#/$defs/MediaBasinResult"
        },
        "mode": {
          "$ref": "#/$defs/MediaModeState"
        },
        "drift": {
          "$ref": "#/$defs/MediaDrift"
        },
        "transition": {
          "$ref": "#/$defs/MediaTransition"
        }
      },
      "required": [
        "vector",
        "invariants",
        "basin",
        "mode",
        "drift",
        "transition"
      ],
      "additionalProperties": false
    }
  },
  "required": ["input", "output"],
  "additionalProperties": false,
  "$defs": {
    "MediaVector": {
      "title": "MediaVector",
      "type": "object",
      "description": "Five-axis media physics vector [S, D, A, N, T].",
      "properties": {
        "S": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "Signal Integrity"
        },
        "D": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "Distribution Topology"
        },
        "A": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "Attention Dynamics"
        },
        "N": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "Narrative Coherence"
        },
        "T": {
          "type": "number",
          "minimum": 0,
          "maximum": 1,
          "description": "Temporal Cadence"
        }
      },
      "required": ["S", "D", "A", "N", "T"],
      "additionalProperties": false
    },
    "MediaInvariantState": {
      "title": "MediaInvariantState",
      "type": "object",
      "description": "Strain values for MSM invariants (0.0 aligned, 1.0 broken).",
      "properties": {
        "signalNarrativeCoherence": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "distributionAttentionFit": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "temporalSignalStability": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "attentionNarrativeFeedback": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        }
      },
      "required": [
        "signalNarrativeCoherence",
        "distributionAttentionFit",
        "temporalSignalStability",
        "attentionNarrativeFeedback"
      ],
      "additionalProperties": false
    },
    "MediaBasinResult": {
      "title": "MediaBasinResult",
      "type": "object",
      "description": "Basin classification result.",
      "properties": {
        "basin": {
          "type": "string",
          "description": "Identified basin name.",
          "enum": [
            "Broadcast",
            "Network",
            "Fragment",
            "Cascade",
            "Stagnation",
            "Reconstruction",
            "Unstable"
          ]
        },
        "distance": {
          "type": "number",
          "minimum": 0,
          "description": "Distance to canonical basin vector."
        },
        "gateSatisfied": {
          "type": "boolean",
          "description": "Whether basin gate conditions were satisfied."
        }
      },
      "required": ["basin", "distance", "gateSatisfied"],
      "additionalProperties": false
    },
    "MediaModeState": {
      "title": "MediaModeState",
      "type": "object",
      "description": "Behavioral mode inside the current basin.",
      "properties": {
        "mode": {
          "type": "string",
          "enum": [
            "Stable",
            "Tension",
            "Drift",
            "Cascade",
            "Collapse",
            "Reconstruction"
          ]
        },
        "driftMagnitude": {
          "type": "number",
          "minimum": 0
        },
        "dominantInvariant": {
          "type": "string",
          "enum": [
            "signalNarrativeCoherence",
            "distributionAttentionFit",
            "temporalSignalStability",
            "attentionNarrativeFeedback"
          ]
        }
      },
      "required": ["mode", "driftMagnitude", "dominantInvariant"],
      "additionalProperties": false
    },
    "MediaDrift": {
      "title": "MediaDrift",
      "type": "object",
      "description": "Drift between previous and current vectors.",
      "properties": {
        "delta": {
          "$ref": "#/$defs/MediaVector"
        },
        "magnitude": {
          "type": "number",
          "minimum": 0
        },
        "category": {
          "type": "string",
          "enum": ["micro", "meso", "macro", "regime_shift"]
        }
      },
      "required": ["delta", "magnitude", "category"],
      "additionalProperties": false
    },
    "MediaTransition": {
      "title": "MediaTransition",
      "type": "object",
      "description": "Detected structural transition between states.",
      "properties": {
        "from": {
          "type": "string",
          "description": "Previous basin/mode label (implementation-defined)."
        },
        "to": {
          "type": "string",
          "description": "Current basin/mode label (implementation-defined)."
        },
        "trigger": {
          "type": "string",
          "enum": [
            "invariant_break",
            "attention_spike",
            "cadence_acceleration",
            "signal_collapse",
            "narrative_collapse",
            "reconstruction",
            "none"
          ]
        },
        "severity": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        }
      },
      "required": ["from", "to", "trigger", "severity"],
      "additionalProperties": false
    }
  }
}
```
