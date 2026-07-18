# 🟣 **Unified Diagram Index (SVG + Mermaid)**  
### *SDE + SIE + Projection Layers*

## Unified Diagram Index
### Structural Detection Engine (SDE)  
### Structural Integration Engine (SIE)  
### Projection Layers (TEL / FFT / OP)

This index lists all diagrams in both **SVG** and **Mermaid** formats.

---

# 1. Operator Ecology Map

## 1.1 SVG
File: `operator_ecology.svg`  
Description: Layered ecology of SDE → SIE → TEL/FFT/OP.

## 1.2 Mermaid
File: `operator_ecology.mmd`

```mermaid
flowchart LR
  subgraph SDE[Structural Detection Engine]
    CPV[CPV]
    FGT[FGT]
    CRM[CRM]
    CPV --> FGT --> CRM
  end

  subgraph SIE[Structural Integration Engine]
    INT[INT]
    TIF[TIF]
    MAN[MAN]
    FFF[FFF]
    CRE[CRE]
    CSL[CSL]
    CET[CET]
    INT --> TIF --> MAN --> FFF --> CRE --> CSL --> CET
  end

  subgraph OUT[Output Modules]
    TEL[TEL::CET]
    FFT[FFT::OUT]
    OP[OP::OUT]
  end

  CRM --> INT
  CET --> TEL
  CET --> FFT
  CET --> OP
```

---

# 2. Operator Flow (SDE → SIE → TEL/FFT/OP)

## 2.1 SVG
File: `operator_flow.svg`  
Description: Linear pipeline from detection → integration → projection.

## 2.2 Mermaid
File: `operator_flow.mmd`

```mermaid
flowchart LR
  subgraph SDE[Detection Layer — SDE]
    CPV
    FGT
    CRM
    PACK1[SDE::PACKET()]
  end

  subgraph SIE[Integration–Emission Layer — SIE]
    INT
    TIF
    FFF
    MAN
    CRE
    CSL
    CET
    PACK2[SIE::PACKET()]
  end

  subgraph PROJ[Projection Layer]
    TEL[TEL::CET()]
    FFT[FFT::OUT()]
    OP[OP::OUT()]
  end

  CPV --> FGT --> CRM --> PACK1 --> INT
  INT --> TIF --> MAN --> FFF --> CRE --> CSL --> CET --> PACK2
  CET --> TEL
  CET --> FFT
  CET --> OP
```

---

# 3. Integration–Emission Manifold (RTT/3)

## 3.1 SVG
File: `integration_emission_manifold.svg`  
Description: 6‑axis manifold with continuity vectors and zones.

## 3.2 Mermaid
File: `integration_emission_manifold.mmd`

```mermaid
graph TD
  A[RTT/3 Integration–Emission Manifold]

  subgraph Axes
    D[D — Drift Continuity]
    E[E — Envelope Continuity]
    C[C — Continuity Vector]
    FI[FI — Fusion‑Integration Curvature]
    EM[EM — Emission Curvature]
    R[R — Regime Identity]
  end

  subgraph Vectors
    ICV[ICV — Integration‑Continuity Vector]
    ECV[ECV — Emission‑Continuity Vector]
    RCV[RCV — Regime‑Continuity Vector]
  end

  A --> D
  A --> E
  A --> C
  A --> FI
  A --> EM
  A --> R

  D --> ICV
  E --> ECV
  R --> RCV

  subgraph Zones
    U[Zone U — Unified]
    S[Zone S — Stable]
    M[Zone M — Mixed]
    D2[Zone D — Divergent]
    X[Zone X — Inversion]
  end

  A --> U
  A --> S
  A --> M
  A --> D2
  A --> X
```

---

# 4. Collapse→Recovery Engine (CRE)

## 4.1 SVG
File: `collapse_recovery_engine.svg`  
Description: CAV → CSV → REV stabilization flow.

## 4.2 Mermaid
File: `collapse_recovery_engine.mmd`

```mermaid
flowchart LR
  subgraph Collapse[Collapse Input]
    AMP[Amplitude]
    CURV[Curvature]
    TORS[Torsion]
  end

  subgraph CRE[Collapse→Recovery Engine]
    CAV[CAV — Collapse Absorption]
    CSV[CSV — Continuity Stabilization]
    REV[REV — Recovery Emission]
  end

  subgraph Output[Recovery Output]
    REC[Recovery + Restored Continuity]
  end

  AMP --> CAV
  CURV --> CAV
  TORS --> CAV

  CAV --> CSV --> REV --> REC
```

---

# 5. Canon‑Wide Summary Diagram (Optional)

## 5.1 One‑Line Flow (Mermaid)

```mermaid
flowchart LR
  SDE[SDE::PACKET()] --> SIE[SIE::PACKET()]
  SIE --> TEL[TEL::CET()]
  SIE --> FFT[FFT::OUT()]
  SIE --> OP[OP::OUT()]
```

---

# 6. File Placement Guide

Place all diagrams here:

```
/docs/operators/diagrams/
    operator_ecology.svg
    operator_ecology.mmd
    operator_flow.svg
    operator_flow.mmd
    integration_emission_manifold.svg
    integration_emission_manifold.mmd
    collapse_recovery_engine.svg
    collapse_recovery_engine.mmd
```

---

# 7. Student‑Friendly Notes

- SVG = printable, high‑resolution, poster‑ready  
- Mermaid = inline, editable, GitHub‑renderable  
- Both formats are canonical and interchangeable  
