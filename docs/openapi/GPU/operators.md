# operators — TFT.OpenGPU.Stack.Module
**Operator Registry for TFT.OpenGPU.Stack.Module**  
**RTT:** 1  
**Coherence:** Declared  
**Drift:** Bounded  
**Paradox:** Structural  

---

## 1. Substrate Operators
Substrate operators define the hidden-view mechanics of dimensional intent.

- **Op.Wrap** — wrap external primitive into substrate form  
- **Op.Intent** — declare dimensional intent  
- **Op.Cycle** — substrate cycle for reconstruction  
- **Op.Bind** — bind substrate primitive to rendering layer  
- **Op.Resolve** — resolve substrate primitive into execution layer  

---

## 2. Rendering Operators
Rendering operators define the middle-view reconstruction of scene primitives.

- **Render.Scene** — construct scene graph  
- **Render.Node** — create scene node  
- **Render.Mesh** — represent surface geometry  
- **Render.Light** — define lighting primitive  
- **Render.Camera** — define camera primitive  
- **Render.Material** — apply material intent  
- **Render.ShaderGraph** — shader graph intent  
- **Render.Transform** — apply dimensional transform  
- **Render.Viewport** — declare viewport substrate  
- **Render.Pass** — execute rendering pass  

---

## 3. Execution Operators
Execution operators define the visible-view GPU work.

- **Exec.Dispatch** — dispatch substrate cycle to GPU  
- **Exec.Kernel** — execution kernel  
- **Exec.Tile** — tile-level compute block  
- **Exec.Warp** — warp-equivalent execution group  
- **Exec.Stream** — execution stream for parallel work  
- **Exec.VRAM.Surface** — GPU surface allocation  
- **Exec.VRAM.Region** — dimensional region mapping  
- **Exec.VRAM.Bind** — bind primitive to VRAM surface  
- **Exec.DMA.Buffer** — DMA-safe buffer for remote transport  
- **Exec.vGPU.Slice** — allocate vGPU slice  
- **Exec.vGPU.Cycle** — execution cycle for Cloud PC tiering  
- **Exec.vGPU.Priority** — scheduling priority  
- **Exec.vGPU.Isolation** — SR‑IOV isolation boundary  
- **Exec.Reconstruct.Surface** — reconstruct dimensional surface  
- **Exec.Reconstruct.Material** — reconstruct material intent  
- **Exec.Reconstruct.Transform** — reconstruct transform intent  
- **Exec.Reconstruct.Viewport** — reconstruct viewport substrate  

---

## 4. RDP Integration Operators
Operators enabling TFT primitive streams inside RDP.

- **RDP.PrimitiveStream** — encode substrate primitives for transport  
- **RDP.Decode** — decode primitive stream on endpoint  
- **RDP.Reconstruct** — reconstruct dimensional intent via GPU  

---

## 5. Cloud PC Tiering Operators
Operators defining tier → vGPU → fidelity mapping.

- **Tier.Cycle** — number of substrate cycles  
- **Tier.VRAM** — VRAM allocation  
- **Tier.Priority** — GPU scheduling priority  
- **Tier.Fidelity** — reconstruction fidelity  

---

## 6. Canonical Operator Summary
Operators define the structural mechanics of the module:

- substrate → rendering → execution  
- dimensional intent → scene → GPU work  
- primitive stream → RDP → reconstruction  
- tier → vGPU slice → fidelity  

All operators remain RTT-aligned and drift-bounded.

