# Diagram Spec — Operator Ecology Map

diagram:
  type: layered-ecology
  layers:
    - name: Detection Layer (SDE)
      operators:
        - CPV
        - FGT
        - CRM
        - SIG
        - NOI
      flows:
        - CPV → FGT
        - FGT → CRM
        - CRM → SIE::INT

    - name: Integration Layer (SIE)
      operators:
        - INT
        - TIF
        - FFF
        - MAN
        - CRE
        - CSL
        - CET
      flows:
        - INT → TIF
        - TIF → MAN
        - MAN → FFF
        - FFF → CRE
        - CRE → CSL
        - CSL → CET

    - name: Output Layers
      modules:
        - TEL
        - FFT
        - OP
      flows:
        - CET → TEL::CET
        - CET → FFT::OUT
        - CET → OP::OUT

notes:
  - SDE operators form the “signal ecology”
  - SIE operators form the “integration–emission ecology”
  - Output modules form the “projection ecology”
