## RTT_Primitives.uasset  
**Blueprint Class — UE6 RTT Operator Primitives**

`RTT_Primitives.uasset` is the reference Blueprint for exposing RTT operator behavior inside Unreal Engine 6.  
It provides a minimal, operator‑first implementation of φ–V–R, invariants, resonance metrics, and entropy signatures using the `URTTComponent` C++ bindings.

### Purpose
- Demonstrate RTT operators in a real‑time UE6 environment  
- Provide a clean example of φ, variance, resonance, and entropy sampling  
- Serve as a debugging and teaching tool for RTT integrations  
- Act as a template for developers integrating RTT into gameplay systems  

### Structure
- **Parent Class:** `Actor`  
- **Components:**  
  - `RTTComponent` (URTTComponent)  
- **Variables:**  
  - `PhiDebugColor`, `ResonanceDebugColor`, `EntropyDebugColor`  
  - `ResonanceScale`, `EntropyScale`  

### Event Graph
- Calls:  
  - `RTT_ApplyPhiField`  
  - `RTT_ApplyVarianceStabilizer`  
  - `RTT_ProbeResonance`  
  - `RTT_TraceEntropy`  
- Draws debug spheres for resonance + entropy fields  
- Provides optional pure functions for operator‑specific visualization  

### Usage
Place `BP_RTT_Primitives` in any level to visualize RTT operator behavior in real time.  
Useful for debugging, teaching, and validating RTT integrations across UE6 systems.

### Status
Active, stable, and aligned with the 2026 RTT Integrations standard.
