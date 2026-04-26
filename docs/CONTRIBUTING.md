# Contributing to TriadicFrameworks

<div style="font-size: 0.8em; margin-bottom: 0.5rem;">
  <span style="
    display:inline-block;
    padding:3px 8px;
    border-radius:999px;
    background:#1a1a1a;
    color:#fff;
    font-family:Arial, sans-serif;
    font-size:11px;
  ">
    🤖 AI‑Ready Module • TriadicFrameworks
  </span>
</div>

<img src="https://img.shields.io/badge/🛠️Contributing%20Module-🧩Workflow%20Lineage%20Active-4c8eda?style=for-the-badge" alt="🛠️Contributing Module | 🧩Workflow & Lineage Active"/>

---

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
