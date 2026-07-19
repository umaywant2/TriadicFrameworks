# Diagram Spec — Operator Flow (SDE → SIE → TEL/FFT/OP)

diagram:
  type: linear-flow
  stages:
    - stage: SDE (Detection)
      operators:
        - CPV
        - FGT
        - CRM
      output: SDE::PACKET

    - stage: SIE (Integration–Emission)
      operators:
        - INT
        - TIF
        - FFF
        - MAN
        - CRE
        - CSL
        - CET
      input: SDE::PACKET
      output: SIE::PACKET

    - stage: Projection
      branches:
        - TEL:
            receives: CET
            outputs: TEL::CET
        - FFT:
            receives: CET
            outputs: FFT::OUT
        - OP:
            receives: CET
            outputs: OP::OUT

notes:
  - Flow is always left → right
  - SDE prepares structure; SIE transforms it; TEL/FFT/OP project it
