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
General OpenLoop overview.

### GET /api/openloop/modules
List of available OpenLoop modules.

### GET /api/openloop/modules/{id}
Detailed metadata for a specific OpenLoop module.

### GET /api/openloop/health
Health and readiness information for the OpenLoop service.

---

## OpenAPI
The OpenAPI description for this skill is available at:

`/openapi/openloop.json`

---

## Documentation
Human-readable documentation is available at:

`/docs/openloop`

---

## Notes
This skill supports:
- open-loop module lookup
- drift-tolerant execution
- RTT integration
- Quad Engine evaluation
- coherence-layer alignment

