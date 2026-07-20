# 🌐 RTT Facilities — Global Index Schema  
**Unified Dashboard Backbone**

This document defines the **Global Index Schema** used by all RTT Facilities dashboards.

It provides a **normalized, extensible structure** for representing infrastructure risk, readiness, and governance state across cities, systems, corridors, and asset classes.

---

## 1. Purpose

The Global Index Schema exists to:

- Provide a single, canonical data backbone  
- Enable consistent dashboards across domains  
- Support corridor‑level and system‑level drill‑downs  
- Preserve governance context alongside metrics  
- Prevent dashboard fragmentation and metric drift  

All Facilities dashboards derive from this schema.

---

## 2. Design Principles

The schema is designed to be:

- **Hierarchical** — global → region → city → corridor → asset  
- **Composable** — domains extend without redefining  
- **Governance‑aware** — decisions, not just metrics  
- **Time‑aware** — trends over snapshots  
- **Explainable** — human‑legible fields  

---

## 3. Top‑Level Structure

```json
{
  "schema_version": "1.0.0",
  "generated_at": "ISO-8601 timestamp",
  "scope": "global | region | city",
  "entities": []
}
```

---

## 4. Entity Model

Each entity represents a **governance‑relevant unit**.

```json
{
  "entity_id": "string",
  "entity_type": "continent | region | city | corridor | asset",
  "name": "string",
  "parent_id": "string | null",
  "location": {
    "lat": "number",
    "lon": "number"
  },
  "systems": [],
  "scores": {},
  "classification": {},
  "capital": {},
  "audit": {},
  "status": {}
}
```

---

## 5. Systems Block

```json
"systems": [
  {
    "system_type": "electrical | water | wastewater | transportation | communications | public_buildings",
    "dependencies": [],
    "propagation_role": "initiator | amplifier | receiver"
  }
]
```

---

## 6. Scoring Block

```json
"scores": {
  "drift": {
    "value": "number",
    "trend": "improving | stable | degrading"
  },
  "harmonics": {
    "value": "number",
    "pattern": "low | moderate | high"
  },
  "propagation": {
    "value": "number",
    "risk_level": "low | medium | high"
  }
}
```

---

## 7. Corridor Classification Block

```json
"classification": {
  "corridor_class": "C-0 | C-1 | C-2 | C-3 | C-4",
  "last_reviewed": "ISO-8601 timestamp",
  "review_trigger": "scheduled | event | audit"
}
```

---

## 8. Capital Alignment Block

```json
"capital": {
  "modernization_cycle": "10-year | 20-year | 50-year",
  "priority": "low | medium | high",
  "deferred_risk": true,
  "next_review": "ISO-8601 timestamp"
}
```

---

## 9. Audit Block

```json
"audit": {
  "last_audit": "ISO-8601 timestamp",
  "audit_trigger": "scheduled | risk | incident",
  "findings": "summary string",
  "follow_up_required": true
}
```

---

## 10. Status Block

```json
"status": {
  "operational": "normal | stressed | degraded",
  "intervention_active": false,
  "public_visibility": "internal | leadership | public"
}
```

---

## 11. Domain Extension Pattern

Domain extensions (e.g., **RTT‑AGERI**) may add:

```json
"domain_extensions": {
  "RTT-AGERI": {
    "above_ground_exposure": "low | medium | high",
    "climate_stress_index": "number"
  }
}
```

Extensions **must not** redefine core fields.

---

## 12. Canonical Status

This schema is **canonical**.

All RTT Facilities dashboards, indices, and visualizations must conform to this structure.
