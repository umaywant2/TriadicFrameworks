flowchart LR
    subgraph UE6[UE6 Blueprints]
        P[BP_RTT_Primitives]
        R[BP_RTT_ResonanceDemo]
        E[BP_RTT_EntropyDemo]
        H[BP_RTT_HybridDemo]
    end

    subgraph Benchmarks[Benchmarks]
        Bphi1[Phi Stability]
        Bphi2[Emergence Coherence]
        Bvar1[Variance Smoothing]
        Bvar2[Temporal Stability]
        Bres1[Resonance Envelope]
        Bres2[Harmonic Stability]
        Bent1[Entropy Boundary Detection]
        Bent2[Collapse Signature]
        Bhyb1[Hybrid Coherence]
        Bhyb2[Cross‑Operator Stability]
    end

    subgraph TEL[Triadic Echo Lattice]
        Tphi[TEL.Operator.Phi]
        Tvar[TEL.Operator.Variance]
        TresC[TEL.Resonance.Core]
        TresH[TEL.Resonance.Harmonics]
        TentF[TEL.Entropy.Field]
        TentC[TEL.Entropy.Collapse]
        Thybrid[TEL.Hybrid.Operator]
    end

    %% UE6 → Benchmarks
    P -->|phi| Bphi1
    P -->|phi| Bphi2
    P -->|variance| Bvar1
    P -->|variance| Bvar2
    P -->|resonance| Bres1
    R -->|resonance| Bres1
    R -->|resonance| Bres2
    P -->|entropy| Bent1
    E -->|entropy| Bent1
    E -->|entropy| Bent2
    H -->|hybrid| Bhyb1
    H -->|hybrid| Bhyb2

    %% Benchmarks → TEL
    Bphi1 --> Tphi
    Bphi2 --> TresC
    Bvar1 --> Tvar
    Bvar2 --> Tvar
    Bres1 --> TresC
    Bres2 --> TresH
    Bent1 --> TentF
    Bent2 --> TentC
    Bhyb1 --> Thybrid
    Bhyb2 --> Thybrid
