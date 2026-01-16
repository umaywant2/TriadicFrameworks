@echo off
echo Creating...
copy con README.md
copy con relationship_to_msrm.md
copy con relationship_to_rsm.md
copy con relationship_to_enterprise_structural_awareness.md
copy con future_directions.md
md overview
cd overview
copy con purpose.md
copy con scope_and_non_goals.md
copy con terminology_alignment.md
cd..
md energy_regimes
cd energy_regimes
copy con steady_state_generation.md
copy con peak_demand_conditions.md
copy con renewable_variability.md
copy con emergency_operations.md
cd..
md grid_entry_points
cd grid_entry_points
copy con generation_assets.md
copy con transmission_networks.md
copy con distribution_systems.md
copy con storage_and_buffering.md
cd..
md minimal_schema
cd minimal_schema
copy con energy_regime_awareness.schema.json
copy con example_grid_declaration.yaml
copy con schema_design_notes.md
cd..
md integration_patterns
cd integration_patterns
copy con passive_grid_declaration.md
copy con operator_context_alignment.md
copy con observability_and_scada.md
copy con automation_boundary_markers.md
cd..
md operational_implications
cd operational_implications
copy con grid_event_interpretation.md
copy con load_shedding_context.md
copy con post_event_analysis.md
cd..
