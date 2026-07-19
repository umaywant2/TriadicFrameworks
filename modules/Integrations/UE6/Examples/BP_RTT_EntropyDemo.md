# BP_RTT_EntropyDemo — Blueprint Spec  
**RTT / Integrations / UE6 / Examples**

## Identity
- Name: `BP_RTT_EntropyDemo`
- Parent: `Actor`
- Path: `RTT/Examples/BP_RTT_EntropyDemo`

## Components
- `DefaultSceneRoot` : `SceneComponent`
- `RTTComponent` : `URTTComponent`
- `EntropySphere` : `StaticMeshComponent` (sphere with `M_RTT_EntropyField`)

## Variables (Category: RTT)
- `EntropyScale` : float = `1.0`

## Event Graph

**Event BeginPlay**
- Create Dynamic Material Instance for `EntropySphere` using `M_RTT_EntropyField`
- Store as `EntropyMID`

**Event Tick**
1. Call `RTT_TraceEntropy` on `RTTComponent` → `EntropySignature`
2. Set scalar/vector params on `EntropyMID`:
   - `EntropyIntensity` = `EntropySignature.Intensity`
   - `EntropyRadius` = `EntropySignature.Radius * EntropyScale`
   - `EntropyCenter` = `EntropySignature.Location`
3. Optional: `Draw Debug Sphere` at `EntropySignature.Location`.

## Purpose
Spatial entropy field visualization using the entropy material.
