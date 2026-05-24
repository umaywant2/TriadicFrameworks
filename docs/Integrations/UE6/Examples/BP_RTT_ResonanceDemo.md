# BP_RTT_ResonanceDemo — Blueprint Spec  
**RTT / Integrations / UE6 / Examples**

## Identity
- Name: `BP_RTT_ResonanceDemo`
- Parent: `Actor`
- Path: `RTT/Examples/BP_RTT_ResonanceDemo`

## Components
- `DefaultSceneRoot` : `SceneComponent`
- `RTTComponent` : `URTTComponent` (attached to root)
- `Mesh` : `StaticMeshComponent` (visual target plane or sphere)

## Variables (Category: RTT)
- `ResonanceScale` : float = `1.0`
- `ResonanceColor` : LinearColor = `(1.0, 0.3, 0.8, 1.0)`

## Event Graph

**Event BeginPlay**
- Create Dynamic Material Instance for `Mesh` using `M_RTT_ResonanceHeatmap`
- Store as `ResonanceMID`

**Event Tick**
1. Call `RTT_ProbeResonance` on `RTTComponent` → `ResonanceFrame`
2. Set scalar params on `ResonanceMID`:
   - `ResonanceAmplitude` = `ResonanceFrame.Amplitude * ResonanceScale`
   - `ResonanceFrequency` = `ResonanceFrame.Frequency`
   - `ResonancePhase` = `ResonanceFrame.Phase`
3. Optional: `Draw Debug Sphere` at actor location using amplitude‑scaled radius.

## Purpose
Visual, material‑driven resonance demo using the heatmap material.
