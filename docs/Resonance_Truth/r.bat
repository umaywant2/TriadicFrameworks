@echo off
echo Creating...
rem docs/Resonance_Truth/
echo . > README.md
echo . > module.json
echo . > examples_capture.md

md architecture
cd architecture
echo . > README.md
echo . > truth_service_architecture.md
echo . > truth_service_components.md
echo . > truth_service_data_model.md
echo . > truth_service_api.yaml
echo . > implementation_roadmap.md
cd..
md crosswalks
cd crosswalks
echo . > README.md
echo . > operational_truth_systems.md
echo . > scoring_criteria.md
echo . > 01_ntp_temporal_truth.md
echo . > 02_dns_locational_truth.md
echo . > 03_iam_identity_truth.md
echo . > 04_pki_integrity_truth.md
echo . > 05_policy_authority_truth.md
echo . > 06_distributed_state_truth.md
echo . > 07_ledger_transactional_truth.md
echo . > 08_desired_state_intent_truth.md
echo . > 09_telemetry_observational_truth.md
echo . > 10_provenance_lineage_truth.md
cd..
md schemas
cd schemas
echo . > README.md
echo . > claim.schema.json
echo . > observation.schema.json
echo . > source.schema.json
echo . > anchor.schema.json
echo . > lineage.schema.json
echo . > regime.schema.json
echo . > evaluation.schema.json
echo . > truth_state.schema.json
echo . > coherence_state.schema.json
echo . > drift_state.schema.json
echo . > paradox.schema.json
echo . > correction_policy.schema.json
cd..
md fixtures
cd fixtures
echo . > README.md
md ntp
cd ntp
echo . > coherent.json
echo . > minor_drift.json
echo . > outlier.json
echo . > fragmented.json
echo . > stale.json
echo . > indeterminate.json
cd..
cd..
md tests
cd tests
echo . > README.md
md qualification
echo . > qualification\stub.txt
md coherence
echo . > coherence\stub.txt
md drift
echo . > drift\stub.txt
md paradox
echo . > paradox\stub.txt
md regime
echo . > regime\stub.txt
md lifecycle
echo . > lifecycle\stub.txt