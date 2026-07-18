flowchart TB
    subgraph Ladder[S → C (Ladder Layer)]
        Phi[TEL.Operator.Phi]
        Var[TEL.Operator.Variance]
    end

    subgraph Cycle[C ↔ H (Cycle Layer)]
        ResCore[TEL.Resonance.Core]
        ResPhi[TEL.Resonance.PhiChannel]
    end

    subgraph Map[H ↔ So (Map Layer)]
        EntField[TEL.Entropy.Field]
        Hybrid[TEL.Hybrid.Operator]
    end

    subgraph Atlas[A (Atlas Layer)]
        EntCollapse[TEL.Entropy.Collapse]
    end

    Phi --> ResPhi
    Var --> ResCore
    ResCore --> Hybrid
    ResPhi --> Hybrid
    EntField --> Hybrid
    EntField --> EntCollapse
