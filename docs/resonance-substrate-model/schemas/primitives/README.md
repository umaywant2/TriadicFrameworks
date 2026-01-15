# **Primitives**

This directory defines the foundational schemas used throughout the Resonance Substrate Model (RSM). These schemas represent the lowest‑level substrate constructs—fields, coordinates, envelopes, and operators—that higher‑layer systems build upon. They provide the essential mathematical and structural vocabulary for simulations, experiments, sensing, and quantum‑substrate interactions.

Below is a detailed description of each schema contained in this directory.

---

# Quicklinks

- [schemas index](../index.md)
- [schemas README](../README.md)
- [schemas coeus README](../coeus/README.md)
- [schemas dimensional README](../dimensional/README.md)
- [schemas distributed README](../distributed/README.md)
- [schemas energy README](../energy/README.md)
- [schemas experiments README](../experiments/README.md)
- [schemas fields README](../fields/README.md)
- [schemas finance README](../finance/README.md)
- [schemas identity README](../identity/README.md)
- [schemas infrastructure README](../infrastructure/README.md)
- [schemas lab README](../lab/README.md)
- [schemas language README](../language/README.md)
- [schemas networking README](../networking/README.md)
- [schemas operators README](../operators/README.md)
- [schemas quantum README](../quantum/README.md)
- [schemas sensing README](../sensing/README.md)
- [schemas simulations README](../simulations/README.md)
- [schemas universe-core README](../universe-core/README.md)
- [previous folder](../)

---

# **Schema Descriptions**

## **1. `primitives.schema.json`**  
Defines the atomic building blocks used across the entire RSM ecosystem, including:
- numbers  
- vectors  
- matrices  
- ranges  
- flags  
- generic key‑value structures  

This schema underpins all other schemas in this directory.

---

## **2. `vector3.schema.json`**  
Represents a 3‑dimensional vector used for:
- spatial coordinates  
- field gradients  
- spin orientations  
- directional operators  

Fields and operators frequently reference this structure for consistent vector math.

---

## **3. `grid_coordinates.schema.json`**  
Defines coordinate positions within the substrate grid.  
Includes:
- x, y, z indices  
- optional world‑space coordinates  
- optional resolution or scaling metadata  

Used by fields, operators, and sensing modules to anchor data in space.

---

## **4. `scalar_field.schema.json`**  
Represents a scalar field distributed across the substrate.  
Common uses:
- temperature  
- density  
- amplitude  
- potential values  

Includes support for:
- grid mapping  
- default values  
- boundary behavior  

---

## **5. `vector_field.schema.json`** *(if present; otherwise skip)*  
Represents a vector field across the substrate.  
Used for:
- flow fields  
- directional forces  
- spin orientations  
- gradient propagation  

(If your folder does not contain this file, I can generate it for you.)

---

## **6. `spin_field.schema.json`**  
Defines a spin‑based vector field, typically used for:
- spin alignment  
- resonance‑phase coupling  
- quantum triad interactions  

Often paired with operators such as alignment or coupling.

---

## **7. `charge_field.schema.json`**  
Represents a field of charge‑like values.  
Useful for:
- charge distributions  
- polarity maps  
- field‑driven interactions  
- substrate‑level force modeling  

This schema supports both continuous and discrete charge representations.

---

## **8. `temperature_field.schema.json`**  
A specialized scalar field representing temperature.  
Includes:
- temperature units  
- thermal gradients  
- dissipation parameters  

Often used in experiments, lab environments, and energy modeling.

---

## **9. `resonance_envelope.schema.json`**  
Defines the resonance‑envelope field—one of the core constructs of the RSM.  
Includes:
- amplitude  
- phase  
- coherence  
- envelope propagation parameters  

This field interacts closely with:
- quantum triad states  
- operators  
- sensing modules  
- energy dissipation  

---

## **10. `substrate_operator.schema.json`**  
Defines a low‑level operator acting on substrate fields.  
Includes:
- operator type  
- parameters  
- target fields  
- optional coupling behavior  

This schema is used by higher‑level operator definitions and simulation modules.

---

# **Purpose of This Directory**

These schemas form the **primitive substrate layer** of the RSM. They provide:

- **Consistency**  
  Shared definitions for fields, coordinates, and operators.

- **Interoperability**  
  Higher‑level schemas (fields, energy, quantum, distributed, sensing) rely on these primitives.

- **Reusability**  
  Common structures like `vector3`, `grid_coordinates`, and `scalar_field` appear throughout the RSM.

- **Extensibility**  
  New field types or operators can be added without breaking existing systems.

---

# **Navigation**

Return to the RSM schema index:  
`../index.md`

Return to the RSM root:  
`../../../README.md`

---
