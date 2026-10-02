# MCP Skill

## Overview
The MCP skill provides machine-readable access to the TriadicFrameworks MCP
subsystem. It exposes MCP module definitions, capability metadata, diagnostic
fields, and server-card integration points used by automated agents.

This skill is intended for AI agents that need to interact with the MCP server,
discover available capabilities, or integrate MCP module logic into workspace
tools and automated workflows.

---

## Endpoints

### GET /api/mcp
Returns general MCP subsystem information.

### GET /api/mcp/modules
Returns a list of available MCP modules.

### GET /api/mcp/modules/{id}
Returns detailed metadata for a specific MCP module.

### GET /api/mcp/health
Returns health and readiness information for the MCP subsystem.

---

## OpenAPI
The OpenAPI description for this skill is available at:

`/openapi/mcp.json`

This specification defines:
- MCP module schemas  
- capability structures  
- diagnostic fields  
- server-card metadata  
- error formats  

---

## Documentation
Human-readable documentation is available at:

`/MCP`

This includes:
- MCP server overview  
- capability descriptions  
- module definitions  
- integration notes  
- examples  

---

## Notes
This skill supports:
- MCP module lookup  
- capability discovery  
- diagnostic evaluation  
- integration with workspace tools  
- alignment with TriadicFrameworks operators and metadata

Agents may use this skill to interpret MCP module metadata, discover server
capabilities, or integrate MCP logic into automated workflows.

