@echo off
echo Creating...
md 00_Frontmatter
cd 00_Frontmatter
echo . > 00_Foreword.md
echo . > 01_Dedication.md
echo . > 02_Acknowledgments.md
cd..
md 10_Part_I_The_Grammar_Layer
cd 10_Part_I_The_Grammar_Layer
echo . > 10_Chapter_01_The_Missing_Layer_in_AI.md
echo . > 11_Chapter_02_Operators.md
echo . > 12_Chapter_03_Invariants.md
echo . > 13_Chapter_04_Regimes.md
cd..
md 20_Part_II_Structure_as_Substrate
cd 20_Part_II_Structure_as_Substrate
echo . > 20_Chapter_05_Substrate_Thinking_vs_App_Thinking.md
echo . > 21_Chapter_06_Governance_Substrate_Model.md
echo . > 22_Chapter_07_Adapters_Awareness_Containment.md
cd..
md 30_Part_III_Drift_City
cd 30_Part_III_Drift_City
echo . > 30_Chapter_08_The_Drift_Problem.md
echo . > 31_Chapter_09_Why_AI_Startups_Drift_Faster.md
echo . > 32_Chapter_10_How_Grammar_Prevents_Drift.md
cd..
md 40_Part_IV_Benchmarks_and_Coherence
cd 40_Part_IV_Benchmarks_and_Coherence
echo . > 40_Chapter_11_Benchmarks_as_Governance.md
echo . > 41_Chapter_12_Building_Coherent_AI_Systems.md
cd..
md 50_Appendices
cd 50_Appendices
echo . > 50_Appendix_A_Glossary.md
echo . > 51_Appendix_B_Operator_Grammar_Quick_Reference.md
echo . > 52_Appendix_C_Benchmarking_Patterns_and_Templates.md
echo . > 53_Appendix_D_GSM_Layer_Mapping.md
echo . > 54_Appendix_E_Recommended_Reading_and_Canon_Notes.md
cd..
md 60_Module_Metadata
cd 60_Module_Metadata
echo . > 60_module.json
echo . > 61_README.md
echo . > 62_index.md  
cd..
md 70_Marketing_Materials
cd 70_Marketing_Materials
echo . > 70_Cover_Description.md
echo . > 71_Back_of_Book_Blurb.md
echo . > 72_Marketing_One_Pager.md
echo . > 73_Press_Kit.md
echo . > 74_Author_Bio.md
cd..
md 80_Printable_Editions
cd 80_Printable_Editions
echo . > 80_Printable_Text_Layout.md
cd..