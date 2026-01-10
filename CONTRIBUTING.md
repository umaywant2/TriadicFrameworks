# Contributing to TriadicFrameworks

Thank you for your interest in contributing to the TriadicFrameworks ecosystem.

## Repository Structure

- `docs/resonance-substrate-model/` — canonical manuscript and theory
- `substrate/` — core runtime implementation
- `overlays/` — domain-specific extensions (Earth, telescopes, etc.)

## Contribution Guidelines

### 1. Keep the Canon Pure
Do not modify the manuscript or core theory without discussion.

### 2. Substrate Contributions
- Operators must be pure functions.
- Core components must remain domain-agnostic.
- Utilities should be dependency-light.

### 3. Overlay Contributions
- Each overlay must define:
  - a schema
  - transforms
  - examples
- Overlays must not modify the substrate.

### 4. Code Style
- Use Python 3.11+
- Follow PEP8
- Include docstrings for all public functions

### 5. Pull Requests
- Describe the purpose clearly
- Reference related issues
- Include tests when applicable

We welcome contributions that expand the substrate, add overlays, or improve documentation.
