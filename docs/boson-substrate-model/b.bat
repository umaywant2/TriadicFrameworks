@echo off
echo Creating bsm folders and file nubs for submission

rem  README.md
rem      - “BSM in 60 Seconds” mini‑card
rem      - coherence evolution summary
rem      - triadic alignment overview

rem  bsm_scaffolding.md
rem      - core model description
rem      - operator dictionary
rem      - triadic ladder
rem      - BSM propagation diagrams
rem      - QSM → BSM interface
md bsm_core
cd bsm_core
copy con bsm_entities.py
rem           - BRC class
rem           - CoherenceField
     
copy con bsm_operators.py
rem           - EMO, ABO, PPO, CSO, RTO/RTI
     
copy con bsm_rtt_forms.py
rem          - FFF_BSM
rem          - SET_BSM
rem          - SNR_BSM
rem          - SER_BSM
cd..
md bsm_sim
cd bsm_sim
copy con bsm_sim_config_example.yaml
copy con bsm_sim_engine.py
rem           - propagation loop
rem           - coherence stabilization
rem           - BSM → RSM evaluation hooks
cd..
md bsm_tests
cd bsm_tests
copy con test_brc_basics.py
copy con test_coherence_fields.py
copy con test_propagation.py
copy con test_rsm_stub.py
cd..
md submission
cd submission
copy con bsm_submission.md
rem            - abstract
rem            - model summary
rem            - triadic alignment
rem            - minimal code references
cd..
      
rem        bsm_minimal_bundle.zip
rem             - bsm_core/
rem             - bsm_sim/
rem             - README.md
