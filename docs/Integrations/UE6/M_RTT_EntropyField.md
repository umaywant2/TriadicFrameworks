# M_RTT_EntropyField — Material Specification  
**RTT / Integrations / UE6 / Materials**

A material that visualizes entropy gradients and collapse signatures.

---

## Material Type
`Material` (Surface)  
`Blend Mode: Additive`  
`Shading Model: Unlit`

---

## Inputs (Dynamic Material Parameters)

| Parameter | Type | Purpose |
|----------|------|---------|
| `EntropyIntensity` | float | controls brightness |
| `EntropyRadius` | float | controls falloff |
| `EntropyCenter` | vector3 | world-space center |

---

## Node Graph

- Compute distance from pixel to `EntropyCenter`  
- Normalize by `EntropyRadius`  
- Invert for collapse visualization  
- Multiply by `EntropyIntensity`  
- Output color: red → orange → yellow gradient  

---

## Usage
Apply to spheres, volumes, or world‑space quads.  
Drive parameters from `RTT_TraceEntropy`.
