# Triadic Gravity Skill

## Overview
This skill provides AI agents with structured access to the Triadic Gravity
API. It exposes machine-readable endpoints for gravity metadata, operators,
health checks, and OpenAPI documentation.

Triadic Gravity is one of the core analytical engines within the
TriadicFrameworks canon, providing structured gravitational operator
definitions, coherence mappings, and substrate-aware metadata.

## Endpoints

### GET /api/gravity
Returns the top-level Triadic Gravity overview, including available
subresources and metadata pointers.

### GET /api/gravity/operators
Returns a list of all gravity operators, each with an ID and href pointing to
its machine-readable definition.

### GET /api/gravity/operators/{id}
Returns metadata for a specific gravity operator. Agents should use the `href`
values returned by `/api/gravity/operators` to discover valid operator IDs.

### GET /api/gravity/health
Returns a simple health check for the Triadic Gravity API.

## OpenAPI Specification
A machine-readable OpenAPI document is available at:

`/openapi/triadic-gravity.json`

This file describes all gravity endpoints, their parameters, and response
schemas.

## Documentation
Human-readable documentation for Triadic Gravity is available at:

`/.well-known/triadic-gravity`

This directory contains conceptual explanations, module summaries, and
operator-level descriptions intended for both human readers and AI agents.

## Notes
This skill is part of the TriadicFrameworks agent skill suite and is intended
for automated clients that require structured access to Triadic Gravity
metadata and operator definitions.
