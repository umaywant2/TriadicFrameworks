# t_Substrate — TFT.OpenGPU.Stack.Module
**Resonance-Time Theory Substrate Document**  
**Module:** TFT.OpenGPU.Stack.Module  
**RTT:** 1  
**Coherence:** Declared  
**Drift:** Bounded  
**Paradox:** Structural  

---

## 1. Substrate Intent  
The substrate layer defines the **dimensional primitives** and **structural operators** that govern the TFT.OpenGPU.Stack.  
It is the **hidden view** of the module — the layer beneath rendering and execution — where dimensional intent is expressed before becoming visible through GPU reconstruction.

The substrate is responsible for:

- expressing draw intent as dimensional primitives  
- maintaining RTT coherence across rendering and execution layers  
- providing a unified representation for remote transport (RDP/TFT stream)  
- enabling Cloud PC tiering through substrate cycles  
- defining the structural paradox between hidden and visible views  

---

## 2. Substrate Principles  

### **2.1 Hidden View (Inverted Star Alignment)**  
The substrate is the **inner star** — the structural layer that is not directly visible to the user.  
Rendering and execution layers are the **outer star**, the visible projection.

The substrate governs:

- what is drawn  
- how dimensional intent is expressed  
- how primitives map to GPU cycles  
- how remote reconstruction occurs  

### **2.2 Dimensional Intent**  
All substrate primitives encode **intent**, not **pixels**.

Examples:

- “draw surface at dimensional coordinate”  
- “apply material intent”  
- “transform primitive through substrate cycle”  
- “declare viewport substrate”  

This allows remote endpoints to reconstruct the final view using their own GPU.

### **2.3 Bounded Drift**  
Substrate reinterpretation of rendering or execution primitives is allowed only within bounded drift:

- reinterpretation must preserve dimensional intent  
- reinterpretation must not alter RTT coherence  
- reinterpretation must remain structurally consistent  

---

## 3. Substrate Primitive Families  

### **3.1 Dimensional Primitives**
- `Dim.Point` — dimensional coordinate  
- `Dim.Surface` — drawable surface intent  
- `Dim.Material` — material intent wrapper  
- `Dim.Transform` — dimensional transform operator  
- `Dim.Viewport` — viewport substrate declaration  

### **3.2 Substrate Operators**
- `Op.Wrap` — wrap external primitive into substrate form  
- `Op.Cycle` — substrate cycle for reconstruction  
- `Op.Intent` — declare dimensional intent  
- `Op.Bind` — bind substrate primitive to rendering layer  
- `Op.Resolve` — resolve substrate primitive into execution layer  

### **3.3 Primitive Streams**
Primitive streams are the transport form of substrate primitives:

- `Stream.Primitive` — ordered dimensional primitives  
- `Stream.Cycle` — substrate cycle metadata  
- `Stream.Viewport` — viewport substrate declaration  
- `Stream.Material` — material intent stream  

These streams are suitable for insertion into RDP via RDPEGFX or custom virtual channels.

---

## 4. Substrate → Rendering Mapping  
The substrate maps into the rendering layer through declared coherence:

| Substrate Primitive | Rendering Primitive |
|---------------------|---------------------|
| Dim.Surface         | Mesh / surface      |
| Dim.Material        | Material graph      |
| Dim.Transform       | Scene transform     |
| Dim.Viewport        | Camera/viewport     |
| Op.Cycle            | GPU reconstruction pass |

This mapping is **declared**, not inferred.

---

## 5. Substrate → Execution Mapping  
The substrate maps into the execution layer through bounded drift:

| Substrate Operator | Execution Primitive |
|--------------------|---------------------|
| Op.Resolve         | Kernel / warp / tile |
| Op.Cycle           | GPU cycle allocation |
| Dim.Surface        | VRAM surface mapping |
| Dim.Transform      | execution transform |
| Stream.Primitive   | DMA-safe surface intent |

This mapping preserves RTT coherence.

---

## 6. Substrate and RDP Integration  
The substrate defines the insertion point for TFT primitives inside RDP:

- substrate primitives → encoded as TFT primitive stream  
- stream transported via RDPEGFX or custom virtual channel  
- endpoint GPU reconstructs dimensional intent  
- RDP retains security, reliability, ordering, session setup  

This allows:

- smooth remote desktops  
- GPU-native reconstruction  
- Cloud PC tiering  
- AMD-friendly execution paths  

---

## 7. Substrate and Cloud PC Tiering  
Cloud PC tiers map directly to substrate cycles:

- Tier → number of substrate cycles  
- Tier → VRAM allocation  
- Tier → reconstruction fidelity  
- Tier → GPU scheduling priority  

Even minimal tiers achieve smooth rendering due to dimensional primitives.

---

## 8. Canonical Substrate Summary  
The substrate layer of the TFT.OpenGPU.Stack.Module:

- defines dimensional primitives  
- governs hidden-view intent  
- maps coherently into rendering and execution layers  
- provides primitive streams for RDP integration  
- enables Cloud PC tiering  
- aligns with RTT (rtt=1, coherence declared, drift bounded, paradox structural)  
- establishes the foundation for an open GPU stack independent of NVIDIA’s closed ecosystem  

This document captures the substrate layer for canonical reference.

