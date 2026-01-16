@echo off
echo Creating BSM submission structure
copy con README.md
copy con CHANGELOG.md
md paper
cd paper
copy con bsm_declared_operating_regimes.md
copy con abstract.md
copy con assumptions.md
copy con substrate_definition.md
copy con operator_dynamics.md
copy con validation_checks.md
copy con discussion.md
md figures
cd figures
copy con bsm_structural_overview.svg
cd..
md metadata
cd metadata
copy con zenodo.json
copy con CITATION.cff
copy con README.md
