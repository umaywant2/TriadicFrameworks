# TriadicFrameworks OpenAPI Directory

This directory contains machine-readable OpenAPI specifications for all
TriadicFrameworks API components. Each file describes the structure, endpoints,
parameters, and response formats for a specific subsystem.

## Available Specifications

### RTT Operator Grammar
`/openapi/rtt-operators.json`
Defines:
- RTT operator schemas
- operator metadata formats
- coherence-layer structures
- drift boundary fields
- diagnostic and error formats

### Triadic Gravity
`/openapi/triadic-gravity.json`
Defines:
- gravity operator schemas
- gravity metadata formats
- health endpoints
- operator-level structures

## Purpose
These OpenAPI documents allow automated agents, MCP clients, and other
machine-driven systems to:
- discover API capabilities
- validate request/response formats
- integrate TriadicFrameworks logic into computational workflows
- perform schema-aware reasoning

## Notes
All OpenAPI files in this directory are designed for machine readability and
agent compatibility. Human-readable documentation for each subsystem is
available under the corresponding `.well-known` directory.
