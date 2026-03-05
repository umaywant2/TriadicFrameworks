@echo off
echo Creating...
copy con workflow_overview.md
copy con student_disclaimer.md
md examples
cd examples
copy con sensory_triggered_memory_example.md
copy con chronic_load_adaptation_example.md
copy con environmental_audio_context_example.md
cd..
md schemas
cd schemas
copy con session_schema_minimal.json.md
copy con regime_context_block.json.md
copy con triadic_integration_example.json.md
cd..
md adapters
cd adapters
copy con ai_augmentation_context.md
copy con ai_drift_calibration_example.json.md
copy con resonance_seed_notes.md
cd..
