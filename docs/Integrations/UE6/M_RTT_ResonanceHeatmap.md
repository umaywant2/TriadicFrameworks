# M_RTT_ResonanceHeatmap — Material Specification  
**RTT / Integrations / UE6 / Materials**

A dynamic heatmap material that visualizes resonance amplitude and frequency.

---

## Material Type
`Material` (Surface)  
`Blend Mode: Translucent`  
`Shading Model: Unlit`

---

## Inputs (Dynamic Material Parameters)

| Parameter | Type | Purpose |
|----------|------|---------|
| `ResonanceAmplitude` | float | drives heatmap intensity |
| `ResonanceFrequency` | float | drives color oscillation |
| `ResonancePhase` | float | optional phase offset |

---

## Node Graph

- **Amplitude →** multiply with gradient ramp  
- **Frequency →** sine wave → color lerp  
- **Phase →** added to frequency before sine  
- **Output Color:**  
  - low amplitude → deep blue  
  - mid amplitude → magenta  
  - high amplitude → white-hot  

---

## Usage
Apply to meshes or debug planes.  
Drive parameters from `RTT_ResonanceProbe` output.
