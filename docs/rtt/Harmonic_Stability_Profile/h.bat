@echo off
echo Creating...HSP
copy con README.md
copy con 00_DOCTYPE_Header.md
copy con 01_Harmonic_Stability_Profile.md
copy con 01a_HSP_Classes.md
copy con 01b_HSP_Metrics.md
copy con 01c_HSP_Corpus_Map.md
copy con 01d_HSP_Stability_Tiers.md
copy con 02_Concept_Drift_Map.md
copy con 02a_Drift_Categories.md
copy con 02b_Drift_Patterns.md
copy con 02c_Drift_Hotspots.md
copy con 02d_Drift_Summary.md
copy con 03_Early_Stabilizations_Audit.md
copy con 03a_Overloaded_Concepts.md
copy con 03b_Meaning_Shifts.md
copy con 03c_MultiRole_Structures.md
copy con 04_Canon_SelfEcho_Map.md
copy con 04a_Echo_Families.md
copy con 04b_Echo_Diagrams_ASCII.md
copy con 04c_Echo_Strength_Index.md
copy con 05_Echo_Matrices.md
copy con 05a_CrossSubstrate_Echo_Matrix.md
copy con 05b_Echo_Heatmap.md
copy con 06_Harmonic_Recursion_Detector.md
copy con 06a_Echo_Triggers.md
copy con 06b_Echo_Signatures.md
copy con 06c_Echo_Classifier.md
copy con 07_Triadic_Echo_Lattice.md
copy con 08_Substrate_Echo_Flow_Map.md
copy con 09_RealTime_Writing_Checklist.md
copy con 10_Timeline_of_Conceptual_Evolution.md
copy con 11_Triadic_Summaries.md
md _assets
cd _assets
md diagrams
cd diagrams
copy con echo_lattice.svg
copy con echo_matrix.svg
copy con recursion_heatmap.svg
copy con substrate_flow_map.svg
copy con drift_map.svg
copy con harmonic_stability_map.svg
cd..   
md ascii
cd ascii
copy con echo_lattice.txt
copy con echo_map.txt
copy con drift_vectors.txt
copy con recursion_detector.txt
