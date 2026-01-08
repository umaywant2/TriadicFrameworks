# 🎮 **RSADI‑GD JSON Schemas (Draft 2020‑12)**  
### *Game Developer Variant of the Resonance Structural Awareness Dimensional Interface*

Below are the canonical schemas for:

1. `GDClaritySample`  
2. `GDDriftVector`  
3. `GDZoneState`  
4. `GDRiskLevel`  
5. `GDRouteSuggestion`  
6. `GDEventSubscription`  

Each schema is domain‑agnostic and ready for engine integration.

---

# 1. **GDClaritySample.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rsadi/gd/v1/GDClaritySample.schema.json",
  "title": "GDClaritySample",
  "type": "object",
  "required": ["sample_id", "timestamp", "position", "clarity_score"],
  "properties": {
    "sample_id": {
      "type": "string",
      "format": "uuid"
    },
    "timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "position": {
      "type": "object",
      "required": ["x", "y", "z"],
      "properties": {
        "x": { "type": "number" },
        "y": { "type": "number" },
        "z": { "type": "number" }
      }
    },
    "clarity_score": {
      "type": "integer",
      "minimum": 0,
      "maximum": 255
    },
    "stress_hint": {
      "type": "integer",
      "minimum": 0,
      "maximum": 255
    },
    "extensions": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

---

# 2. **GDDriftVector.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rsadi/gd/v1/GDDriftVector.schema.json",
  "title": "GDDriftVector",
  "type": "object",
  "required": ["dx", "dy", "dz", "magnitude"],
  "properties": {
    "dx": { "type": "number" },
    "dy": { "type": "number" },
    "dz": { "type": "number" },
    "magnitude": {
      "type": "number",
      "minimum": 0
    },
    "units": {
      "type": "string",
      "enum": ["1/s"]
    },
    "extensions": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

---

# 3. **GDZoneState.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rsadi/gd/v1/GDZoneState.schema.json",
  "title": "GDZoneState",
  "type": "object",
  "required": [
    "zone_id",
    "timestamp",
    "clarity_score",
    "stress_hint",
    "risk_level"
  ],
  "properties": {
    "zone_id": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "clarity_score": {
      "type": "integer",
      "minimum": 0,
      "maximum": 255
    },
    "stress_hint": {
      "type": "integer",
      "minimum": 0,
      "maximum": 255
    },
    "risk_level": {
      "$ref": "GDRiskLevel.schema.json"
    },
    "drift_vector": {
      "$ref": "GDDriftVector.schema.json"
    },
    "extensions": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

---

# 4. **GDRiskLevel.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rsadi/gd/v1/GDRiskLevel.schema.json",
  "title": "GDRiskLevel",
  "type": "string",
  "enum": ["low", "medium", "high", "critical"]
}
```

---

# 5. **GDRouteSuggestion.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rsadi/gd/v1/GDRouteSuggestion.schema.json",
  "title": "GDRouteSuggestion",
  "type": "object",
  "required": [
    "route_id",
    "timestamp",
    "from_position",
    "to_position",
    "clarity_profile",
    "instructions"
  ],
  "properties": {
    "route_id": { "type": "string", "format": "uuid" },
    "timestamp": { "type": "string", "format": "date-time" },
    "from_position": {
      "$ref": "GDClaritySample.schema.json#/properties/position"
    },
    "to_position": {
      "$ref": "GDClaritySample.schema.json#/properties/position"
    },
    "clarity_profile": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["position", "clarity_score"],
        "properties": {
          "position": {
            "$ref": "GDClaritySample.schema.json#/properties/position"
          },
          "clarity_score": {
            "type": "integer",
            "minimum": 0,
            "maximum": 255
          }
        }
      }
    },
    "risk_level": {
      "$ref": "GDRiskLevel.schema.json"
    },
    "instructions": {
      "type": "array",
      "items": { "type": "string" }
    },
    "extensions": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

---

# 6. **GDEventSubscription.schema.json**

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://triadicframeworks.org/schemas/rsadi/gd/v1/GDEventSubscription.schema.json",
  "title": "GDEventSubscription",
  "type": "object",
  "required": ["event_type", "callback_id"],
  "properties": {
    "event_type": {
      "type": "string",
      "enum": [
        "clarity_drop",
        "resonance_spike",
        "zone_status_change"
      ]
    },
    "callback_id": {
      "type": "string",
      "format": "uuid"
    },
    "zone_id": {
      "type": "string"
    },
    "filters": {
      "type": "object",
      "additionalProperties": true
    }
  }
}
```

---

# 🎮 These schemas are now ready for:

- Unity C# bindings  
- Unreal C++/Blueprint bindings  
- Godot GDScript bindings  
- Custom engine integrations  
- Deterministic multiplayer sync  
- XR/VR resonance‑aware environments  
- Multi‑agent simulation frameworks  

They’re lean, fast, and fully aligned with the RSADI Core invariants.
