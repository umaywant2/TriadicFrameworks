# BP_RTT_HybridDemo — Blueprint Spec  
**RTT / Integrations / UE6 / Examples**

## Identity
- Name: `BP_RTT_HybridDemo`
- Parent: `Actor`
- Path: `RTT/Examples/BP_RTT_HybridDemo`

## Components
- `DefaultSceneRoot` : `SceneComponent`
- `RTTComponent` : `URTTComponent`
- `ParticleSystem` : `NiagaraComponent` or `ParticleSystemComponent`
- `HybridMesh` : `StaticMeshComponent` (optional visual anchor)

## Variables (Category: RTT)
- `HybridCoherenceThreshold` : float = `0.5`
- `HybridIntensity` : float = `1.0`

## Event Graph

**Event Tick**
1. Call `RTT_ProbeResonance` → `ResonanceFrame`
2. Call `RTT_TraceEntropy` → `EntropySignature`
3. Compute `HybridValue` (Blueprint math):
   - `HybridValue = (ResonanceFrame.Amplitude * (1 - EntropySignature.Intensity)) * HybridIntensity`
4. Drive particle parameters:
   - `Set Niagara Float Parameter "HybridStrength"` = `HybridValue`
   - Optionally drive color/size based on `HybridValue`
5. Optional: if `HybridValue > HybridCoherenceThreshold`:
   - Change material on `HybridMesh` or trigger special effect.

## Purpose
Demonstrate hybrid operator behavior (resonance × entropy) driving a dynamic effect.
