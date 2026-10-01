# Link Headers Skill

## Overview
The Link Headers skill describes how TriadicFrameworks exposes RFC 8288 Link
response headers for agent discovery. These headers allow automated agents to
locate important resources such as the API catalog, OpenAPI specifications,
documentation, agent skills, and MCP server metadata without relying on HTML
parsing.

This skill is intended for AI agents that need to understand and follow Link
relations to discover TriadicFrameworks capabilities.

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
Advertises machine-readable OpenAPI specifications for programmatic API
discovery.

Header:
Link: </openapi>; rel="service-desc"

### rel="service-doc"
Advertises human-readable documentation for APIs, modules, and subsystem
explanations.

Header:
Link: </.well-known>; rel="service-doc"

### rel="service-auth"
Advertises authentication instructions for AI agents.

Header:
Link: </.well-known/Auth.md>; rel="service-auth"

### rel="sitemap"
Advertises the site sitemap for global resource discovery.

Header:
Link: </sitemap.xml>; rel="sitemap"

### rel="robots"
Advertises the robots.txt file for crawler guidance.

Header:
Link: </robots.txt>; rel="robots"

---

## Combined Header Format
TriadicFrameworks serves all Link relations using a **single combined Link
header**, as required by Cloudflare Transform Rules (which enforce unique
header names). RFC 8288 allows multiple link-values within one header.

Example:

Link: </.well-known/api-catalog>; rel="api-catalog",
      </.well-known/agent-skills/index.json>; rel="agent-skills",
      </.well-known/mcp/server-card.json>; rel="mcp-server",
      </openapi>; rel="service-desc",
      </.well-known>; rel="service-doc",
      </.well-known/Auth.md>; rel="service-auth",
      </sitemap.xml>; rel="sitemap",
      </robots.txt>; rel="robots"

---

## Implementation Notes

TriadicFrameworks serves these Link headers via Cloudflare Response Header
Transform Rules. Because Cloudflare requires unique header names, all Link
relations are combined into a single `Link:` header using comma-separated
RFC 8288 link-values.

These headers are included on all pages to ensure consistent agent
discoverability across the entire domain.

---

## Documentation

- RFC 8288 (Web Linking)
- RFC 9727 (API Catalog)
- TriadicFrameworks Agent Skills Index:
  `/.well-known/agent-skills/index.json`
- TriadicFrameworks MCP Server Card:
  `/.well-known/mcp/server-card.json`

---

## Notes
Agents may use these Link relations to:
- discover the API catalog
- locate OpenAPI specifications
- retrieve documentation
- find the MCP server
- enumerate available agent skills
- locate authentication instructions
- perform full-site discovery via sitemap and robots metadata

This skill ensures that TriadicFrameworks is fully discoverable by modern AI
agents using standardized link-based discovery mechanisms.
