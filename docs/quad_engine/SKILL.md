# Quad Engine Skill

## Overview
The Quad Engine provides structured, machine-readable access to TriadicFrameworks’ computational substrate. It exposes resonance-time operators, module evaluators, coherence analyzers, and diagnostic endpoints used for automated reasoning over TriadicFrameworks modules.

This skill is intended for AI agents that need to execute Quad Engine operations, retrieve structured module metadata, or perform RTT/FFF-based evaluations.

---

## Endpoints

### GET /api/quad
Returns general Quad Engine information, available operators, and engine capabilities.

### POST /api/quad/eval
Executes a Quad Engine evaluation request.  
Input includes:
- operator
- module
- payload
- coherence-layer selection

Output includes:
- evaluation result
- resonance-time metrics
- drift boundary notes
- diagnostic flags

### GET /api/quad/operators
Returns a machine-readable list of all supported Quad Engine operators.

### GET /api/quad/health
Returns health and readiness information for the Quad Engine service.

---

## OpenAPI
The OpenAPI description for this skill is available at:

`/openapi/quad.json`

This specification defines:
- request/response schemas  
- operator grammar  
- evaluation payload formats  
- error and diagnostic structures  

---

## Documentation
Human-readable documentation is available at:

`/docs/quad-engine`

This includes:
- conceptual overview  
- RTT/FFF integration notes  
- operator grammar reference  
- examples and module walkthroughs  

---

## Notes
This skill is designed for automated agents that require structured access to TriadicFrameworks’ computational layer.  
It supports:
- RTT operator evaluation  
- module metadata extraction  
- coherence-layer diagnostics  
- resonance-time analysis  

Agents may use this skill to integrate TriadicFrameworks logic into workflows, reasoning engines, or automated analysis pipelines.
