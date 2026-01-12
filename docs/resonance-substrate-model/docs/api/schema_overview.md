# Schema Overview

This document provides a conceptual overview of the schema system used in the Resonance Substrate Model.

---

## 1. Schema Categories

### Field Schemas
Define scalar, vector, spin-field, and resonance envelope structures.

### Operator Schemas
Specify operator parameters, types, and composition rules.

### Simulation Schemas
Describe grid configuration, timesteps, boundary conditions, and solver settings.

### Experiment Schemas
Capture metadata, apparatus details, and run configurations.

### Distributed Layer Schemas
Define node identities, communication channels, and synchronization rules.

---

## 2. Schema Structure
Most schemas follow a common pattern:
- `id` — unique identifier  
- `type` — schema category  
- `fields` — required and optional parameters  
- `constraints` — validation rules  
- `metadata` — descriptive information  

---

## 3. Schema Relationships
Schemas may reference one another:
- simulation schemas reference operator schemas  
- experiment schemas reference field schemas  
- distributed schemas reference simulation schemas  

This modularity enables flexible composition.

---

## 4. Purpose
The schema system provides:
- consistency across modules  
- clarity for contributors  
- a stable foundation for tooling and automation  

