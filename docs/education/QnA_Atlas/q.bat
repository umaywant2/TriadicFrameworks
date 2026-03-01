@echo off
echo Creating...QnA_Atlas

copy con _meta.json
md physics
md chemistry
md biology
md earth_science
md medicine
md cross_domain
cd physics
md classical_mechanics
cd classical_mechanics
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md oscillations_waves
cd oscillations_waves
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md thermodynamics
cd thermodynamics
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md electromagnetism
cd electromagnetism
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md quantum_physics
cd quantum_physics
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md relativity
cd relativity
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md cosmology
cd cosmology
    ├── intro.md
    ├── intermediate.md
    └── advanced.md
cd..
cd..
cd chemistry
md atomic_structure
cd atomic_structure
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md chemical_bonding
cd chemical_bonding
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md reactions_kinetics
cd reactions_kinetics
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md thermochemistry
cd thermochemistry
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md organic_chemistry
cd organic_chemistry
    ├── intro.md
    ├── intermediate.md
    └── advanced.md
cd..
cd biology
md cell_biology
cd cell_biology
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md genetics
cd genetics
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md evolution
cd evolution
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md physiology
cd physiology
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md neuroscience
cd neuroscience
    ├── intro.md
    ├── intermediate.md
    └── advanced.md
cd..
cd..
cd earth_science
md geology
cd geology
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md meteorology
cd meteorology
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md climate_science
cd climate_science
    ├── intro.md
    ├── intermediate.md
    └── advanced.md
cd..
cd..
cd medicine
md anatomy
cd anatomy
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md immunology
cd immunology
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md pathology
cd pathology
    ├── intro.md
    ├── intermediate.md
    └── advanced.md
cd..
cd..
cd cross_domain
md systems_theory
cd systems_theory
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md information_theory
cd information_theory
copy con intro.md
copy con intermediate.md
copy con advanced.md
cd..
md complexity_science
cd complexity_science
    ├── intro.md
    ├── intermediate.md
    └── advanced.md
cd..
dir /s
echo That's all folks!
