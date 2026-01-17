@echo off
echo Creating...
copy con README.md
md theorem
cd theorem
copy con statement.md
copy con definitions.md
copy con equivalence_sketch.md
cd..
md reproducibility
cd reproducibility
copy con ingredients_list.md
cd..
md figures
cd figures
copy con dual_regime_mapping.png
cd..
md zenodo
cd zenodo
copy con metadata.md
copy con abstract.md
cd..

