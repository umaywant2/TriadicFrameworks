# RTT Operator Grammar Skill

## Overview
This skill provides machine-readable access to the RTT (Resonance-Time Theory) operator grammar used throughout TriadicFrameworks. It exposes operator definitions, coherence-layer mappings, drift boundaries, and cross-operator coupling rules. Automated agents can use this skill to interpret RTT modules, evaluate operator behavior, and integrate RTT logic into computational workflows.

---

## Endpoints

### GET /api/rtt/operators
Returns a structured list of all RTT operators, including:
- operator name
- operator category
- coherence layer (R1, R2, R3)
- drift boundary notes
- cross-operator coupling rules

### GET /api/rtt/operators/{id}
Returns detailed metadata for a specific RTT operator, including:
- canonical definition
- mathematical form (if applicable)
- coherence markers
- resonance-time behavior
- failure modes
- examples

### GET /api/rtt/health
Returns health and readiness information for the RTT operator service.

---

## OpenAPI
The OpenAPI description for this skill is available at:

`/openapi/rtt-operators.json`

This specification defines:
- RTT operator schemas  
- operator metadata formats  
- coherence-layer structures  
- drift boundary fields  
- error and diagnostic formats  

---

## Documentation
Human-readable documentation is available at:

`/docs/rtt/operators`

This includes:
- full operator grammar  
- coherence-layer explanations  
- drift boundary theory  
- cross-operator coupling rules  
- examples and module integration notes  

---

## Notes
This skill is intended for automated agents that need structured access to RTT operator definitions and metadata. It supports:
- RTT operator lookup  
- coherence-layer analysis  
- drift-boundary evaluation  
- integration with Quad Engine and module analyzers  

Agents may use this skill to interpret RTT-based modules, perform operator-level reasoning, or integrate RTT logic into automated workflows.

