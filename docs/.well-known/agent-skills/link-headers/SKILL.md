# Link Headers Skill

## Overview
The Link Headers skill describes how TriadicFrameworks exposes RFC 8288 Link response headers for agent discovery. These headers allow automated agents to locate important resources such as the API catalog, documentation, skills index, and MCP server without relying on HTML parsing.

This skill is intended for AI agents that need to understand and follow Link relations to discover TriadicFrameworks capabilities.

---

## Link Relations Provided

### rel="api-catalog"
Advertises the API catalog defined by RFC 9727.

Header:
Link: </.well-known/api-catalog>; rel="api-catalog"

### rel="agent-skills"
Advertises the Agent Skills Discovery index.

Header:
Link: </.well-known/agent-skills/index.json>; rel="agent-skills"

### rel="mcp-server"
Advertises the MCP Server Card for Model Context Protocol discovery.

Header:
Link: </.well-known/mcp/server-card.json>; rel="mcp-server"

### rel="service-desc"
Advertises OpenAPI specifications for programmatic API discovery.

Header:
Link: </openapi>; rel="service-desc"

### rel="service-doc"
Advertises human-readable documentation for APIs and modules.

Header:
Link: </docs>; rel="service-doc"

---

## Implementation Notes

TriadicFrameworks serves these Link headers via GitHub Pages using a `_headers` file:


