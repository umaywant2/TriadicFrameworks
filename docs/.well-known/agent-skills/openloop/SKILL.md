# OpenLoop Skill

## Overview
The OpenLoop skill provides machine-readable access to TriadicFrameworks
open-loop modules. It exposes module definitions, input/output structures,
state behavior, drift-tolerant execution notes, and diagnostic metadata.

This skill is intended for AI agents that need to evaluate or integrate
open-loop modules within RTT, Quad Engine, or coherence-layer workflows.

---

## Endpoints

### GET /api/openloop
Returns general OpenLoop module information.

### GET /api/openloop/modules
Returns a list of available OpenLoop modules.

### GET /api/openloop/modules/{id}
Returns detailed metadata for a specific OpenLoop module.

### GET /api/openloop/health
Returns health and readiness information for the OpenLoop service.

---

## OpenAPI
The OpenAPI description for this skill is available at:

`/openapi/openloop.json`

This specification defines:
- OpenLoop module schemas  
- input/output field structures  
- drift-tolerant execution metadata  
- diagnostic fields  
- error formats  

---

## Documentation
Human-readable documentation is available at:

`/openloop`

This includes:
- module definitions  
- input/output structures  
- drift-tolerant execution notes  
- RTT integration examples  
- coherence-layer alignment  

---

## Notes
This skill supports:
- open-loop module lookup  
- drift-tolerant execution  
- RTT integration  
- Quad Engine evaluation  
- coherence-layer alignment

Agents may use this skill to interpret module metadata, perform open-loop
reasoning, or integrate OpenLoop logic into automated workflows.
