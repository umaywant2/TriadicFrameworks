@echo off
echo Creating...
copy con README.md
copy con CHANGELOG.md
copy con VERSIONING.md
copy con LICENSE_NOTES.md
md 00_intent_and_boundaries
cd 00_intent_and_boundaries
copy con README.md
copy con scope.md
copy con nonclaims.md
copy con terminology.md
copy con ethics_and_misuse_notes.md
cd..
md 01_creators_assumption
cd 01_creators_assumption
copy con README.md
copy con creators_assumption.md
copy con minimal_axioms.md
copy con falsifiability_and_failure_modes.md
cd..
md 02_model_overview
cd 02_model_overview
copy con README.md
copy con one_page_overview.md
copy con glossary.md
copy con diagrams.md
cd..
md 03_primitives
cd 03_primitives
copy con README.md
copy con primitives_index.md
copy con resonance_core_primitives.md
copy con state_and_transition_primitives.md
copy con validity_and_context_primitives.md
cd..
md 04_wrapped_resonance_structural_aware_cores
cd 04_wrapped_resonance_structural_aware_cores
copy con README.md
copy con wrsadc_variant_definition.md
copy con wrapper_interfaces.md
copy con core_lifecycle.md
copy con boundary_conditions.md
cd..
md 05_autonomous_forms
cd 05_autonomous_forms
copy con README.md
copy con autonomous_form_definition.md
copy con autonomy_levels.md
copy con agency_without_anthropomorphism.md
copy con evaluation_signals.md
cd..
md 06_architecture_patterns
cd 06_architecture_patterns
copy con README.md
copy con reference_architecture.md
copy con patterns_catalog.md
copy con anti_patterns.md
copy con integration_notes.md
cd..
md 07_worked_examples
cd 07_worked_examples
copy con README.md
copy con example_01_minimal_agent_loop.md
copy con example_02_multi_core_federation.md
copy con example_03_regime_shift_handling.md
copy con example_04_sandbox_sim_notes.md
cd..
md 08_alignment_with_rsm_and_rtt
cd 08_alignment_with_rsm_and_rtt
copy con README.md
copy con rsm_alignment_notes.md
copy con rtt_lens_mapping.md
copy con interoperability_contracts.md
cd..
md 09_validation_and_tests
cd 09_validation_and_tests
copy con README.md
copy con test_philosophy.md
copy con measurable_predictions.md
copy con benchmark_suggestions.md
copy con red_team_questions.md
cd..
md 10_release_artifacts
cd 10_release_artifacts
copy con README.md
copy con zenodo_abstract.md
copy con citation.bib
copy con keywords.md
