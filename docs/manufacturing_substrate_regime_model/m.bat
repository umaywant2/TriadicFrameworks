@echo off
echo Creating...
copy con README.md
copy con CHANGELOG.md
copy con CITATION.cff
copy con zenodo.json
md overview
cd overview
copy con abstract.md
copy con scope_and_assumptions.md
copy con limitations.md
copy con terminology.md
cd..
md substrate
cd substrate
copy con substrate_definition.md
copy con regime_declaration.md
copy con boundary_semantics.md
copy con operating_envelopes.md
cd..
md calibration
cd calibration
copy con calibration_as_structure.md
copy con regime_aware_calibration.md
copy con drift_detection.md
copy con non_catastrophic_exit.md
cd..
md operators
cd operators
copy con operator_roles.md
copy con mediation_patterns.md
copy con inter_regime_mediation.md
cd..
md manufacturing_context
cd manufacturing_context
copy con lithography_systems.md
copy con extreme_regime_constraints.md
copy con yield_and_variability.md
cd..
md figures
cd figures
copy con msrm_structural_overview.svg
copy con regime_calibration_flow.svg
copy con boundary_and_exit_semantics.svg
cd..
md related_works
cd related_works
copy con relationship_to_bsm.md
copy con relationship_to_qsm.md
copy con relationship_to_rsm.md
cd..
md discussion
cd discussion
copy con implications_for_manufacturing.md
copy con deployment_considerations.md
copy con future_extensions.md
cd..