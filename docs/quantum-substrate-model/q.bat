@echo off
echo Creating...
copy con README.md
copy con CHANGELOG.md
md paper
cd paper
copy con abstract.md
copy con introduction.md
copy con scope_and_assumptions.md
copy con substrate_definition.md
copy con operator_dynamics.md
copy con regime_structure.md
copy con validation_checks.md
copy con discussion.md
copy con limitations.md
cd..
md figures
cd figures
copy con qsm_structural_overview.svg
cd..
md metadata
cd metadata
copy con CITATION.cff
copy con zenodo.json
copy con README.md
