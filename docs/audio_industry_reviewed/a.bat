@echo off
echo Creating...
rem /docs/audio_industry_reviewed

copy con README.md
copy con 00_executive_summary.md
md 01_audio_industry_history
cd 01_audio_industry_history
copy con 01_early_acoustics_and_analog.md
copy con 02_recording_eras_and_formats.md
copy con 03_digital_audio_and_compression.md
copy con 04_industry_fumbles_and_tradeoffs.md
copy con 05_modern_audio_landscape.md
cd..
md 02_vst_alignment_and_clarity
cd 02_vst_alignment_and_clarity
copy con 01_why_clarity_matters.md
copy con 02_audio_as_substrate.md
copy con 03_vst_alignment_principles.md
copy con 04_failure_modes_without_alignment.md
cd..
md 03_human_ear_substrate_constraints
cd 03_human_ear_substrate_constraints
copy con 01_human_hearing_ranges.md
copy con 02_safe_and_friendly_frequency_bands.md
copy con 03_dynamic_range_and_perceptual_limits.md
copy con 04_containment_of_human_audio.md
copy con 05_parent_regime_alignment.md
cd..
md 04_musical_notation_reexamined
cd 04_musical_notation_reexamined
copy con 01_history_of_musical_notation.md
copy con 02_limitations_of_current_notation.md
copy con 03_vst_informed_notation_models.md
copy con 04_learning_first_design_principles.md
copy con 05_successor_notation_examples.md
cd..
md 05_case_studies_and_examples
cd 05_case_studies_and_examples
copy con 01_mastering_and_loudness_wars.md
copy con 02_spatial_audio_and_surround.md
copy con 03_remastering_and_restoration.md
copy con 04_failures_of_overextension.md
cd..
copy con 06_conclusions_and_future_work.md
echo Complete.