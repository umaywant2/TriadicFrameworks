# MightyTHOR Registry

The **registry** directory contains Thor‑specific registries for orchestration.  
It indexes agents, overlays, and resonance mappings.

## Structure
- Agent registry → maps Thor agents to roles
- Overlay registry → indexes dashboards
- Resonance registry → maps folds to orchestration contexts

## Purpose
The registry is the **index layer** of Thor.  
It ensures every agent, overlay, and fold is discoverable and orchestrated.

## Cross‑links
- [agents](../agents/) → registry maps agents
- [overlays](../overlays/) → registry indexes dashboards
- [folds](../folds/) → resonance registry references fold data
