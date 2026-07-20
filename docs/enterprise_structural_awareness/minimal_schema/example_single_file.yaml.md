```yaml

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/structural-awareness.schema.json",
  "title": "Enterprise Structural Awareness Schema",
  "description": "A minimal, non-intrusive schema for declaring operating context, regime validity, and boundary semantics within existing enterprise systems.",
  "type": "object",
  "properties": {
    "structural_awareness": {
      "type": "object",
      "properties": {
        "declared_regime": {
          "type": "string",
          "description": "A human-readable identifier for the current operating regime."
        },
        "operating_envelope": {
          "type": "string",
          "description": "A description of the bounds within which assumptions are considered valid."
        },
        "validity": {
          "type": "string",
          "enum": ["valid", "degraded", "invalid"],
          "description": "The current validity state of assumptions within the declared regime."
        },
        "boundary_semantics": {
          "type": "string",
          "description": "Interpretive guidance for approaching or crossing regime boundaries."
        },
        "non_catastrophic_exit": {
          "type": "string",
          "description": "Expected behavior or interpretation when exiting the declared regime without system failure."
        }
      },
      "required": ["declared_regime", "validity"]
    }
  },
  "additionalProperties": true
}
```
