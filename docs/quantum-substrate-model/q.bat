@echo off
echo Creating qsm submission folders and file nubs
copy con QSM_in_60_Seconds_mini_card.md
copy con coherence_evolution_summary.md
copy con triadic_alignment_overview.md
rem qsm_scaffolding.md
copy con core_model_description.md
copy con operator_dictionary.md
copy con triadic_ladder.md
copy con collapse_chain_diagram.md
copy con entanglement_routing_map.md
md qsm_core
cd qsm_core
copy con qsm_entities.py
rem    QRP class
rem     - UncertaintyEnvelope
rem     - EntanglementLink
copy con qsm_operators.py
rem   - SPO, ELO, CLO, UEO, QRTO
copy con qsm_rtt_forms.py
rem      - FFF_QSM
rem      - SET_QSM
rem      - SNR_QSM
rem      - SER_QSM
cd..
md qsm_sim
cd qsm_sim
copy con qsm_sim_config_example.yaml
copy con qsm_sim_engine.py
rem      - tick loop
rem      - collapse evaluation
rem      - entanglement propagation
rem      - QSM → BSM transfer hooks
cd..
md qsm_tests
cd qsm_tests
copy con test_qrp_basics.py
copy con test_entanglement.py
copy con test_collapse.py
copy con test_transfer_stub.py
cd..
md submission
cd submission
copy con qsm_submission.md
rem            - abstract
rem            - model summary
rem            - triadic alignment
rem            - minimal code references
cd..
rem qsm_minimal_bundle.zip
rem             - qsm_core/
rem             - qsm_sim/
rem             - README.md
