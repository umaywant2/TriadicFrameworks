@echo off
echo Creating...
copy con README.md
copy con relationship_to_msrm.md
copy con relationship_to_rsm.md
copy con future_directions.md
md overview
cd overview
copy con purpose.md
copy con scope_and_non_goals.md
copy con terminology_alignment.md
cd..
md entry_points
cd entry_points
copy con configuration_surfaces.md
copy con policy_objects.md
copy con metadata_and_annotations.md
copy con lifecycle_states.md
cd..
md minimal_schema
cd minimal_schema
copy con structural_awareness.schema.json
copy con example_single_file.yaml
copy con schema_design_notes.md
cd..
md integration_patterns
cd integration_patterns
copy con passive_declaration.md
copy con documentation_only_adoption.md
copy con observability_alignment.md
copy con automation_boundary_markers.md
cd..
md enterprise_examples
cd enterprise_examples
copy con configuration_management.md
copy con monitoring_and_alerting.md
copy con identity_and_access.md
copy con service_orchestration.md
cd..
md operational_implications
cd operational_implications
copy con incident_interpretation.md
copy con change_management.md
copy con postmortem_clarity.md
cd..
