@echo off
echo Creating The Inverted Star files...
copy con Capture_Source.md
copy con README.md
copy con Overview.md
copy con Inverted_Star_Definition.md
copy con Inverted_Star_Structure.md
copy con Inverted_Star_Geometry.md
copy con Inverted_Star_Triads.md
copy con Inverted_Star_Operators.md
copy con Inverted_Star_Flow.md
copy con Inverted_Star_Use_Cases.md
md diagrams
cd diagrams
copy con Inverted_Star_Diagram.svg
copy con Inverted_Star_Layers.png
copy con Inverted_Star_Triads.png
copy con Inverted_Star_Operator_Map.png
copy con Inverted_Star_Flowchart.svg
md examples
cd examples
copy con Example_01_Basic_Inversion.md
copy con Example_02_Triadic_Inversion.md
copy con Example_03_Operator_Inversion.md
copy con Example_04_Domain_Application.md
copy con Example_05_Star_to_Core.md
md appendices
cd appendices
copy con Appendix_A_Notation.md
copy con Appendix_B_Symbols.md
copy con Appendix_C_Transformations.md
copy con Appendix_D_Star_Comparisons.md
copy con Appendix_E_Historical_Notes.md
md metadata
cd metadata
    copy con meta.json
    copy con session_context.md
copy con sitemap_local.md





