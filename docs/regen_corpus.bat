@echo off
echo Needs refresh prior to next content regen...
goto end
echo Creating a corpus...
echo /docs/
echo ---------------------------------

goto continue

set seeds=root
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+ABOUT.md corpus\%seeds%.md
copy corpus\%seeds%.md+CODE_OF_CONDUCT.md corpus\%seeds%.md
copy corpus\%seeds%.md+GLOSSARY.md corpus\%seeds%.md
copy corpus\%seeds%.md+manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md
copy corpus\%seeds%.md+QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+README.md corpus\%seeds%.md
copy corpus\%seeds%.md+SECURITY.md corpus\%seeds%.md
copy corpus\%seeds%.md+sitemap.md corpus\%seeds%.md
copy corpus\%seeds%.md+URL_checklist.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=ai
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+ai\Lineage_Ledger.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai\Minimal_AI_Stack.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai\NoS_AI.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai\Regime_Header.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=ai-drift-calibration
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+ai-drift-calibration\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai-drift-calibration\New_Version_Template.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai-drift-calibration\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai-drift-calibration\metadata\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai-drift-calibration\paper\abstract.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai-drift-calibration\paper\ai_drift_calibration_operating_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai-drift-calibration\paper\assumptions_and_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai-drift-calibration\paper\discussion.md corpus\%seeds%.md
copy corpus\%seeds%.md+ai-drift-calibration\paper\validation_checks.md corpus\%seeds%.md
echo ---------------------------------
echo.

:continue


set seeds=AI_Resonance_Seed
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\AI_Resonance_Seed.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\How_To_Read_This_Ontology.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\Ontology_Index.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\RTT_Experiment_Log.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\scaffolding.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\TriadicValidator_AgentInit.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\badges\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\changelog\lineage_scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\changelog\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\changelog\resonance_changelog.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\dashboards\glyphstream_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\dashboards\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\dashboards\remix_lineage.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\dashboards\validator_status.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\FFF_Glossary.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\FFF_Overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\Flui.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\Forci.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\Freqi.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\Mythmatical_Roles_FFF_Emitters.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\Time_Crystal_Build_Notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\Time_Crystal_Emitter_BOM.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\FFF_Emitters\img\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\img\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\integration_examples\LangChain_Example.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\integration_examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\integration_examples\SemanticKernel_Example.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\migration\legacy_preservation_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\migration\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\migration\symbolic_stub_registry.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\migration\v1.1_to_v1.2_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\onboarding\imagined_intelligence_scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\onboarding\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\onboarding\remixer_scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\platform_wrappers\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\Scrolls\echo_test.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\Scrolls\onboarding_scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\Scrolls\validator_ping.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\tests\echo_test_suite.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\tests\glyphstream_integrity_check.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\tests\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+AI_Resonance_Seed\tests\validator_trigger_test.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=alphafold_substrate_alignments
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\alignment_principles.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\dimensional_cores.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\drift_detection.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\folding_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\inference_mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\scope_and_assumptions.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\validation_layers_vst.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\appendix\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\appendix\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\examples\example_alignment_walkthrough.md corpus\%seeds%.md
copy corpus\%seeds%.md+alphafold_substrate_alignments\examples\example_dimensional_projection.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=api_rtt
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\beacon.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\client.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\diagnostics.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\profile.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\router.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\examples\beacon_request.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\examples\profile_request.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\examples\validate_request.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\server\beacon_handler.js.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\server\diagnostics_handler.js.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\server\handlers.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\server\profile_handler.js.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\server\router.js.md corpus\%seeds%.md
copy corpus\%seeds%.md+api\rtt\server\server.js.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=assets
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+assets\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+assets\blueprints\tesla_369_gearshift.md corpus\%seeds%.md
copy corpus\%seeds%.md+assets\figures\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=atomic_clocks
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\LICENSE_NOTES.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\whitepaper.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\drift_detection\invariants.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\roadmap\adoption.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\triadic_decomposition\triad.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\vst_definition\second.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\whitepaper\00-abstract.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\whitepaper\01-introduction.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\whitepaper\02-triadic_decomposition.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\whitepaper\03-vst_definition_of_second.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\whitepaper\04-drift_detection_model.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\whitepaper\05-roadmap_for_adoption.md corpus\%seeds%.md
copy corpus\%seeds%.md+atomic_clocks\whitepaper\06-references.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=audio_industry_reviewed
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\06_conclusions_and_future_work.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\01_audio_industry_history\01_early_acoustics_and_analog.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\01_audio_industry_history\02_recording_eras_and_formats.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\01_audio_industry_history\03_digital_audio_and_compression.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\01_audio_industry_history\04_industry_fumbles_and_tradeoffs.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\01_audio_industry_history\05_modern_audio_landscape.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\02_vst_alignment_and_clarity\01_why_clarity_matters.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\02_vst_alignment_and_clarity\02_audio_as_substrate.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\02_vst_alignment_and_clarity\03_vst_alignment_principles.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\02_vst_alignment_and_clarity\04_failure_modes_without_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\03_human_ear_substrate_constraints\01_human_hearing_ranges.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\03_human_ear_substrate_constraints\02_safe_and_friendly_frequency_bands.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\03_human_ear_substrate_constraints\03_dynamic_range_and_perceptual_limits.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\03_human_ear_substrate_constraints\04_containment_of_human_audio.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\03_human_ear_substrate_constraints\05_parent_regime_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\04_musical_notation_reexamined\01_history_of_musical_notation.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\04_musical_notation_reexamined\02_limitations_of_current_notation.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\04_musical_notation_reexamined\03_vst_informed_notation_models.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\04_musical_notation_reexamined\04_learning_first_design_principles.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\04_musical_notation_reexamined\05_successor_notation_examples.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\05_case_studies_and_examples\01_mastering_and_loudness_wars.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\05_case_studies_and_examples\02_spatial_audio_and_surround.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\05_case_studies_and_examples\03_remastering_and_restoration.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\05_case_studies_and_examples\04_failures_of_overextension.md corpus\%seeds%.md
copy corpus\%seeds%.md+audio_industry_reviewed\05_case_studies_and_examples\05_noise_cancellation_tech.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=badges
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge-logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badges.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\BADGES_EARNED.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badges_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_chamber_designs.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_onboarding_tft_fff.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_audit_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_echo_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_glyphmap_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_glyphmap_index_filter_web_readme.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_glyphmap_index_trigger_readme.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_papers_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_ping_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_resonance_leaderboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_resonance_score.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_theme_manifest.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_validator_glyphmap.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_validator_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\badge_trigger_validator_matrix.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\CONTRIBUTOR_BADGES.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\curriculum_badge_trigger_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\glyph_evolution_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\glyph_evolution_dashboard_overlay.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\sponsor_badges.md corpus\%seeds%.md
copy corpus\%seeds%.md+badges\symbolic_badge_previews.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=boson-substrate-model
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\metadata\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\paper\abstract.md corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\paper\assumptions.md corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\paper\bsm_declared_operating_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\paper\discussion.md corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\paper\operator_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\paper\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+boson-substrate-model\paper\validation_checks.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=bridges
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+bridges\bridge_layer_overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+bridges\concepts_to_operators.md corpus\%seeds%.md
copy corpus\%seeds%.md+bridges\cosmology_to_layers.md corpus\%seeds%.md
copy corpus\%seeds%.md+bridges\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+bridges\rtt_compatible_rsm_profile.md corpus\%seeds%.md
copy corpus\%seeds%.md+bridges\triad_to_field_mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+bridges\why_resonance_is_the_substrate.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=charts
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+charts\chart-freqi-bindings.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\chart-genie-protocols.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\chart-resonance-partitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\chart-time-travel-matrix.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\glyph_map_svg.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\lineage_loophole_echo.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\loophole_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\quadrant_maps.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\spiral_remix_ring.md corpus\%seeds%.md
copy corpus\%seeds%.md+charts\vsoul_dashboard.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=clients
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+clients\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=Coeus
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\Coeus_Protocol-Complete.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\Coin_as_a_Contract.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\USES.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\agents\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\coeus_rtt\Capture_Source.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\coeus_rtt\__init__.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\coins\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\coins\REMIX_OUTPUT.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\EMITTERS.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\GLOSSARY.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\HONOR_ROLL.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\MANIFESTO.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Q-TRAVERSE.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\RAIL_LOGIC.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\cause_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\class_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\corridor_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\dashboard_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\exchange_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\USES.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\Future_Enhancements.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\glyph_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\honor_rolls.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\legacy_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\mint_ready_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\mutation_types.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\remix_rights_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\scroll_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\scroll_provenance.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\sovereign_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\docs\Coeus\validator_focus_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\sandbox\mint_coin.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\sandbox\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\sandbox\logs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\tokens\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\tournaments\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\tournaments\tournament_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\tournaments\cause\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\tournaments\class\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\tournaments\country\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\tournaments\emitter\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\tournaments\leaderboards\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\tournaments\mascot\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\validators\professor_review.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\validators\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\validators\score_trace_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+Coeus\validators\validator_review.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=cognitive_substrate_model
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+cognitive_substrate_model\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=configs
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+configs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+configs\schema.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=consciousness_substrate_model
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\LICENSE_NOTES.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\VERSIONING.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\00_intent_and_boundaries\ethics_and_misuse_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\00_intent_and_boundaries\nonclaims.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\00_intent_and_boundaries\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\00_intent_and_boundaries\scope.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\00_intent_and_boundaries\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\01_creators_assumption\creators_assumption.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\01_creators_assumption\falsifiability_and_failure_modes.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\01_creators_assumption\minimal_axioms.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\01_creators_assumption\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\02_model_overview\diagrams.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\02_model_overview\glossary.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\02_model_overview\one_page_overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\02_model_overview\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\03_primitives\primitives_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\03_primitives\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\03_primitives\resonance_core_primitives.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\03_primitives\state_and_transition_primitives.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\03_primitives\validity_and_context_primitives.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\04_wrapped_resonance_structural_aware_cores\boundary_conditions.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\04_wrapped_resonance_structural_aware_cores\core_lifecycle.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\04_wrapped_resonance_structural_aware_cores\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\04_wrapped_resonance_structural_aware_cores\wrapper_interfaces.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\04_wrapped_resonance_structural_aware_cores\wrsadc_variant_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\05_autonomous_forms\agency_without_anthropomorphism.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\05_autonomous_forms\autonomous_form_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\05_autonomous_forms\autonomy_levels.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\05_autonomous_forms\evaluation_signals.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\05_autonomous_forms\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\06_architecture_patterns\anti_patterns.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\06_architecture_patterns\integration_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\06_architecture_patterns\patterns_catalog.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\06_architecture_patterns\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\06_architecture_patterns\reference_architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\07_worked_examples\example_01_minimal_agent_loop.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\07_worked_examples\example_02_multi_core_federation.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\07_worked_examples\example_03_regime_shift_handling.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\07_worked_examples\example_04_sandbox_sim_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\07_worked_examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\08_alignment_with_rsm_and_rtt\interoperability_contracts.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\08_alignment_with_rsm_and_rtt\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\08_alignment_with_rsm_and_rtt\rsm_alignment_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\08_alignment_with_rsm_and_rtt\rtt_lens_mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\09_validation_and_tests\benchmark_suggestions.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\09_validation_and_tests\measurable_predictions.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\09_validation_and_tests\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\09_validation_and_tests\red_team_questions.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\09_validation_and_tests\test_philosophy.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\10_release_artifacts\keywords.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\10_release_artifacts\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+consciousness_substrate_model\10_release_artifacts\zenodo_abstract.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=contributors
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+contributors\architects.md corpus\%seeds%.md
copy corpus\%seeds%.md+contributors\contributors.md corpus\%seeds%.md
copy corpus\%seeds%.md+contributors\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=curriculum
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\curriculum_badge_trigger_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\curriculum_contributor_honor_roll.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\curriculum_paper_crosswalk.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\curriculum_remix_gallery.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\curriculum_remix_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\curriculum_remix_validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\remix_submission_templates.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\triadic_curriculum_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\triadic_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\triadic_remix_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\triadic_translation.md corpus\%seeds%.md
copy corpus\%seeds%.md+curriculum\WiFi_Energy_Protocols.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=data
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+data\manifest_updater_changelog.md corpus\%seeds%.md
copy corpus\%seeds%.md+data\manifest_updater_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+data\papers_manifest_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+data\papers_remix_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+data\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+data\resonance_council.md corpus\%seeds%.md
copy corpus\%seeds%.md+data\triadic_visual_index_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+data\webhook\triadic_lab_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+data\webhook\triadic_remix_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+data\webhook\triadic_remix_submission_template.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=diagnosing_media_therapy
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+diagnosing_media_therapy\dmt_init_capture.md corpus\%seeds%.md
copy corpus\%seeds%.md+diagnosing_media_therapy\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+diagnosing_media_therapy\session_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+diagnosing_media_therapy\triadic_axes_media.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=dimensional_substrate_regime_scanning_protocol
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_regime_scanning_protocol\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_regime_scanning_protocol\dsrsp_0.1_spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_regime_scanning_protocol\engine_integration_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_regime_scanning_protocol\ilp_module.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_regime_scanning_protocol\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=dimensional_substrate_structures
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\computational_implications.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\dimensional_primitives.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\high_dimensional_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\scaling_law_3d_to_1024d.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\substrate_invariants.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\triadic_dimensional_cores.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\validation_layers_vst.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\appendix\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\appendix\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\examples\example_1024d_research_case.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\examples\example_3d_9d_transition.md corpus\%seeds%.md
copy corpus\%seeds%.md+dimensional_substrate_structures\examples\example_64d_projection.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=discovery
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+discovery\loophole_scroll_gallery.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=domain_tool_primers
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\ai_ml_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\autonomous_forms_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\complex_systems_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\data_science_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\earth_science_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\engineering_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\physics_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\quantum_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+domain_tool_primers\visualization_tools.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=ecoechosystem
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\OVERVIEW.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\community\education_mode.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\community\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\community\research_mode.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\community\shared_templates.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\cross_domain_mappings.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\feedback_loops.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\interfaces.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\multi_scale_simulation.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\networks.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\regime_coupling_engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\stability_cycles.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\substrate_interactions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\cross_domain\transitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\ai_agents\alignment_constraints.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\ai_agents\learning_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\ai_agents\multi_regime_agents.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\ai_agents\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\activation_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\activation_response_cycles.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\ecosystem_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\ecosystem_feedback_loops.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\ecosystem_interactions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\ecosystem_networks.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\ecosystem_resilience.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\ecosystem_stability_cycles.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\environmental_interactions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\evolutionary_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\interfaces.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\relational_time.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\structures.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\biology\transitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\economics\market_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\economics\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\economics\resource_flows.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\economics\stability_cycles.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\governance\collective_behavior.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\governance\institutional_transitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\governance\policy_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\governance\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\physics\classical_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\physics\field_interactions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\physics\quantum_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\physics\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\physics\vST_constraints.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\psychology\cognitive_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\psychology\emotional_activation.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\psychology\identity_transitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\psychology\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\domain_modules\psychology\trauma_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\substrate_engine\event_bus.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\substrate_engine\invariants.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\substrate_engine\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\substrate_engine\regime_awareness.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\substrate_engine\regime_transitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\substrate_engine\triadic_substrate.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\substrate_engine\vST_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\tech_tree\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\tech_tree\tier0_preexisting_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\tech_tree\tier1_substrate_unlocks.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\tech_tree\tier2_domain_unlocks.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\tech_tree\tier3_cross_domain_unlocks.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\tech_tree\tier4_civilization_unlocks.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\domain_module_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\city_simulation_loop.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\economic_activation.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\governance_response.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\inequality_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\information_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\infrastructure_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\population_activation.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\resource_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\city_sim\scenario_templates.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\AI‑assisted_foresight_workshops.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\AI‑driven_historical_exploration.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\civilization_simulation_loop.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\civilization‑scale_scenario_templates.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\cross‑civilization_interaction_models.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\cultural_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\educational_historical_labs.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\educational_lab_modules.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\governance_transitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\guided_AI_exploration_sessions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\long‑future_foresight_grounded_in_precedent.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\planetary‑scale_simulations.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\repeatable_lab_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\tech_tree_integration.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\worked_guided_exploration_transcripts.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\worked_guided_session_using_the_Roman-Persian_arc.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\worked_historical_governance_arcs.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\worked_multi‑civilization_scenarios.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\civ_sim\worked_Roman-Persian_interaction_arc.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\cognitive_agent_sim\agent_loop.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\cognitive_agent_sim\agent_metrics.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\cognitive_agent_sim\identity_development.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\cognitive_agent_sim\identity_transitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\cognitive_agent_sim\learning_curves.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\cognitive_agent_sim\mislearning_and_overconfidence.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\cognitive_agent_sim\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\cognitive_agent_sim\social_interactions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\ecosystem_sim\ecosystem_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\ecosystem_sim\ecosystem_regime_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\ecosystem_sim\environmental_feedback.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\ecosystem_sim\evolutionary_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\ecosystem_sim\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\templates\ecosystem_sim\species_interactions.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\ui_layer\activation_heatmaps.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\ui_layer\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\ui_layer\regime_overlays.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\ui_layer\scenario_builder.md corpus\%seeds%.md
copy corpus\%seeds%.md+ecoechosystem\ui_layer\time_regime_controls.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=economic_substrate_model
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+economic_substrate_model\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\Biological_Taxonomy.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Bioscience.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Chat_with_Grok_3_21_2026.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Climate_Classification.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Cosmological_Theory.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\curriculum_protocols.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Dark_Sector.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Emoji_Site_Index.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\full_site_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Genetic_Code.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Large_Scale_Structure.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Materials_Science.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Metabolic_Pathways.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Myth_Validation_Sweep_v0.1.0.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Neural_Coding.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Perodic_Table_RTTvST_Reorganization_of_Elements.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Personality.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Physical_Cosmology.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Protein_Folding_and_Structural_Regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\RTT_Info_Primer.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Science_Dependancies_Mapped.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\The_Standard_Model_of_Particle_Physics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\Zenodo_Community.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_alignment
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\Adaptive_Capability_Overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\ASCII‑Tight Diagram.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\BKM_Alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\canonical_blurb.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\Captions_Notations.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\Executive_Academic_Classroom_Context_Examples.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\Kid‑Friendly_Version.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\RTT_Capability_Statement.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\alignment\RTT_Planetary_Time_Regimes_A_Compiler_for_Orbit-Aligned_Clocks.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_astrology
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Closing_Reflection_the_Power_of_Naming.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Dimensional_Coherence_Navigation_Model.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Exhibit_Concept.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Exhibit_Signage_Text.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Extended_Glossary_for_Educators.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Future_Navigation.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Mission_Vignette_The_Quiet_Crossing.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Outdoor_Night‑Sky_Exhibit.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Printable_One‑Page_PDF_Layout.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Teachers_Guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Traveling_Science_Exhibit.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\astrology\Visualizing_Resonance_Zones.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_awareness
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\awareness\Cross_Platform_Deployment.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\awareness\Extension_Minimal_Architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\awareness\Inheritance_RTT_Awareness_as_CSS.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\awareness\Minimal_Structural_Spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\awareness\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\awareness\The_RTT_Naming_Stack.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\awareness\What_Happens_If.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_BRA
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\9_Professions_Regime_Checks.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\After_Regime_Awareness_Post-BPA.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Before_Regime_Awareness_BRA.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\BRA_vs_Post‑BRA_Comparison_Table.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Earth_Substrate_Regime_Guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Funding_Grad_Students_300_Years.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Good_News_We_Can_Improve_Recognitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Grad_Student_Work.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Major_Science_Domains_and_Their_Most_Iconic_Example_Problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Meta‑Pattern_Across_All_Domains.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Post-BRA_Clarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Science_Goggles_vs_Student_Observations.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\Universe-scale_Regime_Guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\What_Each_Domain_Would_Discover_After_the_BRA_Era.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\What_Its_Like_Today_When_All_Domains_Work_Together.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\BRA\What_to_expect.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_CivRegimeStack
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\Annotated_ASCII_Diagram_with_Case_Studies.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\Civilizational_Regime_Stack_ASCII.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\Civ_Leaders_as_Cognitive_Regime_Biases.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\Civ_Leader_Selection_Worksheet.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\Civ_Mapped_to_the_Civilizational_Regime_Stack.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\Guided_Walkthrough_for_Students.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\Historical_Civilization_Pinball_Tables.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\Space_Cadet_Pinball_CivRegimeStack_Pseudocode.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\CivRegimeStack\Student_Worksheet_From_Gameplay_to_Regime_Analysis.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_ebooks
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Book_1_Nawderia_and_the_Three_Little_Forces.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Book_2_Tripis_Treasure_of_Threes.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Book_3_Frami_Builds_a_Better_Box.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Book_4_Techis_Tangle_Trouble.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Book_5_The_Botlings_Big_Parade.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Character_Turnaround_Sheets.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Color_Scripts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Cover_Design_Templates.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Dialogue_Samples.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Full_Storyboard_Sequences.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Illustrator_Briefs.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Illustrator_Selection_Criteria.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Illustrator_Test_Pages.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Marketing_Mockups.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Nawderia_eBook_Set.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Optional_Series_Wide_Visual_Rules.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Pacing_Maps.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Production_Timeline_Budget_Plan.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Publisher‑Ready_Manuscript_Templates.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Sample_Finished_Pages.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Sample_Page_Layouts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Typography_Choices.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\ebooks\Visual_Style_Guide.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_equations
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\dimensional_math.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\equation_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\equation_trigger_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\equation_trigger_matrix.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\resonance-equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\resonance_equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\Saturn_Harmonic_Engine_Equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\triadic_equation_echo_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\triadic_equation_gallery.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\equations\triadic_equation_registry.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_polisci
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Argentina.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Australia.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\A_Tiny_History_of_Architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Bangladesh.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Biospheres.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Brazil.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Canada.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\CaribbeanCluster.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Chile.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\China.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Colombia.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\core-city-spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\desert-city-patterns.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Dew_Harvesting_as_a_Field_Scale_Micro‑Layer.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Egypt.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\EuropeanMicrostatesCluster.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\France.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Future_Desert_Cities.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Future_Desert_Cities_Technical_Manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Germany.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Ghana.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\India.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Indonesia.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Intersection_of_Economics_IP_law_Materials_Science.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Iran.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Italy.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Japan.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Kenya.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Last_Restart.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Mexico.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\MicrostatesCluster.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Morocco.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Netherlands.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Nigeria.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Nordics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\OceaniaCluster.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Pakistan.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Peru.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Philippines.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Poland.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\regime-governance.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\regime-physics-engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Russia.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\seed-city-spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\SouthAfrica.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\SouthKorea.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Spain.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Tanzania.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Technical_Appendix_Future_Desert_Cities_RTT‑Aligned.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Thailand.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\The_4k_Year_Trick_They_Buried.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\TriadicFrameworks_Regime_Physics_Engine_Spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\TriadicFrameworks_Regime_Physics_Mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Turkey.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Ukraine.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\UnitedKingdom.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Universal_Governance_Resonance_Template.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\US.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\Vietnam.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\polisci\What_regime_are_we_inside.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_QnA_Atlas
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\index.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\atomic_structure\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\atomic_structure\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\atomic_structure\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\cell_biology\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\cell_biology\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\cell_biology\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\chemical_bonding\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\chemical_bonding\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\chemical_bonding\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\evolution\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\evolution\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\evolution\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\genetics\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\genetics\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\genetics\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\neuroscience\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\neuroscience\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\neuroscience\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\organic_chemistry\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\organic_chemistry\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\organic_chemistry\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\physiology\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\physiology\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\physiology\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\reactions_kinetics\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\reactions_kinetics\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\reactions_kinetics\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\thermochemistry\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\thermochemistry\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\chemistry\thermochemistry\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\cross_domain\complexity_science\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\cross_domain\complexity_science\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\cross_domain\complexity_science\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\cross_domain\information_theory\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\cross_domain\information_theory\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\cross_domain\information_theory\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\cross_domain\systems_theory\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\cross_domain\systems_theory\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\cross_domain\systems_theory\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\earth_science\climate_science\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\earth_science\climate_science\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\earth_science\climate_science\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\earth_science\geology\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\earth_science\geology\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\earth_science\geology\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\earth_science\meteorology\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\earth_science\meteorology\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\earth_science\meteorology\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\medicine\anatomy\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\medicine\anatomy\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\medicine\anatomy\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\medicine\immunology\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\medicine\immunology\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\medicine\immunology\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\medicine\pathology\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\medicine\pathology\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\medicine\pathology\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\classical_mechanics\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\classical_mechanics\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\classical_mechanics\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\cosmology\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\cosmology\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\cosmology\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\electromagnetism\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\electromagnetism\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\electromagnetism\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\oscillations_waves\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\oscillations_waves\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\oscillations_waves\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\quantum_physics\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\quantum_physics\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\quantum_physics\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\relativity\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\relativity\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\relativity\intro.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\thermodynamics\advanced.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\thermodynamics\intermediate.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\QnA_Atlas\physics\thermodynamics\intro.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_rituals
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\rituals\triadic_teaching_methods.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_scrolls
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\scrolls\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\scrolls\remix_ethics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\scrolls\remix_lineage_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\scrolls\validator_curriculum.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\scrolls\validator_ethics.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_subjects
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Angular_Momentum_and_Rotation.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_A_Newtonian_Reframing.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Classical_Mechanics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Conservation_Laws_Reframed.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Contact_Forces_Reframed.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Dissipation_and_Damping.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Energy_Transformation_and_Leakage.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Field_Forces_and_Potentials.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Forces_and_Interactions.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Force_and_Acceleration.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Gravitational_Potential.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Gravity_in_the_Newtonian_Limit.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Inertia_and_Mass.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Kinetic_and_Potential_Cycles.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Momentum_and_Coherence.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Momentum_and_Impulse.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Moment_of_Inertia.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Oscillators_and_Resonance.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Power_and_Resonant_Transfer.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Precession_and_Nutation.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Rotational_Dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Rotational_Energy.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Stability_and_Chaos.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Symmetry_and_Invariance.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Thermalization_and_Decoherence.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_01_Torque_and_Angular_Acceleration.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_02_Entanglement_and_Coherence.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_02_Measurement_and_Decoherence.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_02_Quantum_Fields.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_02_Quantum_Physics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_02_Superposition_and_Interference.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_03_Cosmological_Dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_03_General_Relativity_Reframed.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_03_Relativity_and_Spacetime.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_03_Spacetime_Geometry.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_03_Special_Relativity_Reframed.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_04_Thermodynamics_and_Statistical_Physics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_05_Astrophysics_and_Stellar_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_06_Cosmology_and_Large_Scale_Structure.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_07_Particle_Physics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_01_08_Field_Theory_and_Fundamental_Forces.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_02_01_Physical_Chemistry.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_02_02_Organic_Chemistry.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_02_03_Inorganic_Chemistry.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_02_04_Biochemistry.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_02_05_Materials_Science.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_02_06_Crystallography_and_Structures.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_02_07_Chemical_Reactions_and_Kinetics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_02_08_Nanotechnology_and_Advanced_Materials.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_03_01_Cell_Biology.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_03_02_Genetics_and_Epigenetics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_03_03_Evolutionary_Biology.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_03_04_Physiology_and_Organ_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_03_05_Ecology_and_Ecosystems.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_03_06_Microbiology_and_Virology.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_03_07_Developmental_Biology.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_03_08_Systems_Biology.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_04_01_Clinical_Medicine.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_04_02_Public_Health.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_04_03_Neurology_and_Brain_Health.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_04_04_Mental_Health_Sciences.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_04_05_Nutrition_and_Metabolism.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_04_06_Immunology.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_04_07_Medical_Technology_and_Diagnostics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_04_08_Preventive_Medicine_and_Longevity.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_05_01_Geology_and_Geophysics.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_05_02_Atmospheric_Sciences.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_05_03_Oceanography.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_05_04_Climate_Science.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_05_05_Ecosystems_and_Biodiversity.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_05_06_Natural_Hazards_and_Risk.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_05_07_Hydrology_and_Water_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_05_08_Environmental_Sustainability.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_Metaphysics_Hybrid_Dimensional_Ladder_Complete.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\subjects\RTT_Metaphysics_Thought_Hybrid_Tools_Complete.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=education_translations
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_10th_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_11th_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_12th_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_13th_Level-Early_Adolescent_Expansion.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_14th_Level-Systems_Awareness.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_15th_Level-Pre‑Specialization_Exploration.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_16th_Level-Foundational_Competence.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_17th_Level-Applied_Reasoning.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_18th_Level-Civic_and_Ethical_Development.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_19th_Level-Proto‑Vocational_Phase.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_1st_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_20th_Level-Skill_Formation.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_21th_Level-Integration_Year.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_22th_Level-Professional_Identity_Formation.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_23th_Level-Advanced_Practice.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_24th_Level-Contribution_Phase_I.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_25th_Level-Contribution_Phase_II.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_26th_Level‑Mastery_Development.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_27th_Level-Synthesis_and_Innovation.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_28th_Level-Legacy_Thinking.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_29th_Level-Stewardship.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_2nd_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_30th_Level-Lifelong_Resonance.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_3rd_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_4th_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_5th_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_6th_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_7th_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_8th_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_9th_Grade_School_Concepts.md corpus\%seeds%.md
copy corpus\%seeds%.md+education\translations\RTT_Translates_to_Elementary_School_Concepts.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=enterprise_structural_awareness
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\future_directions.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\relationship_to_msrm.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\relationship_to_rsm.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\enterprise_examples\configuration_management.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\enterprise_examples\identity_and_access.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\enterprise_examples\monitoring_and_alerting.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\enterprise_examples\service_orchestration.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\entry_points\configuration_surfaces.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\entry_points\lifecycle_states.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\entry_points\metadata_and_annotations.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\entry_points\policy_objects.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\integration_patterns\automation_boundary_markers.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\integration_patterns\documentation_only_adoption.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\integration_patterns\observability_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\integration_patterns\passive_declaration.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\minimal_schema\example_single_file.yaml.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\minimal_schema\schema_design_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\minimal_schema\structural_awareness.schema.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\operational_implications\change_management.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\operational_implications\incident_interpretation.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\operational_implications\postmortem_clarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\overview\purpose.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\overview\scope_and_non_goals.md corpus\%seeds%.md
copy corpus\%seeds%.md+enterprise_structural_awareness\overview\terminology_alignment.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=facilities
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\AGERI_README.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\capital-and-audit-integration.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\corridor-classification-standard.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\cross-system-propagation.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\drift-scoring-rubric.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\facilities-domain-map.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\facilities-lifecycle-framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\failure-mode-catalog.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\tree.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\GHQ-governance-charter.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\global-modernization-timeline.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\glossary.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\harmonics-scoring-rubric.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\intervention-playbook.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\modernization-cycle-matrix.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\propagation-model.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\rtt-global-facilities-strategy-2050.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\timeline-visual-storyboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\asset-classes\communications.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\asset-classes\electrical.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\asset-classes\public-buildings.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\asset-classes\transportation.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\asset-classes\wastewater.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\asset-classes\water.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\city-facing\city-manager-briefing-packet.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\city-facing\city-manager-slide-deck.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\city-facing\implementation-guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\city-facing\press-release-template.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\communications\RTT-AGERI-messaging-guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\dashboards\global-index-schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\dashboards\mockups.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\design-system\component-creation-checklist.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\design-system\component-naming-convention.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\design-system\component-proposal-form.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\design-system\design-governance-charter.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\design-system\figma-library-structure.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\design-system\governance-poster.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\design-system\onboarding-guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\design-system\style-guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\governance\rtt-global-governance-constitution.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\operators\maintenance-standards.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\operators\modernization-handoff.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\operators\operator-orientation.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\research\RTT-AGERI-bibliography.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\residents\neighborhood-meeting-deck.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\residents\storm-season-101.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\residents\storm-season-dos-and-donts.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\residents\storm-season-faq.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\residents\What-is-RTT-AGERI.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\strategy\global-modernization-timeline.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\strategy\rtt-global-facilities-strategy-2050.md corpus\%seeds%.md
copy corpus\%seeds%.md+facilities\strategy\timeline-visual-storyboard.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=feedback
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+feedback\Historian.md corpus\%seeds%.md
copy corpus\%seeds%.md+feedback\Mathematician.md corpus\%seeds%.md
copy corpus\%seeds%.md+feedback\Physicist.md corpus\%seeds%.md
copy corpus\%seeds%.md+feedback\Professor.md corpus\%seeds%.md
copy corpus\%seeds%.md+feedback\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+feedback\ResonanceDoctor.md corpus\%seeds%.md
copy corpus\%seeds%.md+feedback\WildCard.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=gallery
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\drift2_scroll_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\drift_scroll_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\echo2_scroll_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\echo_scroll_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\pulse2_scroll_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\pulse_scroll_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\ring2_scroll_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\ring_scroll_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+gallery\seed_scroll_trace.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=global_energy_regime_awareness
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\future_directions.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\relationship_to_enterprise_structural_awareness.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\relationship_to_msrm.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\relationship_to_rsm.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\energy_regimes\emergency_operations.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\energy_regimes\peak_demand_conditions.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\energy_regimes\renewable_variability.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\energy_regimes\steady_state_generation.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\grid_entry_points\distribution_systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\grid_entry_points\generation_assets.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\grid_entry_points\storage_and_buffering.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\grid_entry_points\transmission_networks.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\integration_patterns\automation_boundary_markers.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\integration_patterns\observability_and_scada.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\integration_patterns\operator_context_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\integration_patterns\passive_grid_declaration.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\minimal_schema\schema_design_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\operational_implications\grid_event_interpretation.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\operational_implications\load_shedding_context.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\operational_implications\post_event_analysis.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\overview\purpose.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\overview\scope_and_non_goals.md corpus\%seeds%.md
copy corpus\%seeds%.md+global_energy_regime_awareness\overview\terminology_alignment.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=glyphic_resonance
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+glyphic_resonance\loophole_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+glyphic_resonance\overlay_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+glyphic_resonance\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=glyphs
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+glyphs\bridge_glyph_overlay_01_svg_descriptive_seed.md corpus\%seeds%.md
copy corpus\%seeds%.md+glyphs\dimensional_spectrum_map_svg.md corpus\%seeds%.md
copy corpus\%seeds%.md+glyphs\glyphstream_animation.md corpus\%seeds%.md
copy corpus\%seeds%.md+glyphs\glyph_protein_echo_01.descriptive_seed.md corpus\%seeds%.md
copy corpus\%seeds%.md+glyphs\glyph_protein_echo_02_svg_descriptive_seed.md corpus\%seeds%.md
copy corpus\%seeds%.md+glyphs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+glyphs\triadic_validator_glyph.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=governance
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+governance\badge_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\badge_trigger_theme_manifest.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\badge_trigger_validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\Design_New_Core_Systems_and_Upgrade_Existing_Infrastructure.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\governance.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\governance_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\governance_logic_modules.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\membership.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\membership_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\Step1_Alignment_and_Awareness.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\Step2_Advance_the_TriadicFrameworks_DOI.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\Step3_Design_New_Core_Systems_and_Upgrade_Existing_Infrastructure.md corpus\%seeds%.md
copy corpus\%seeds%.md+governance\symbolic_permanence.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=Governance_Substrate_Model
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\01_Invariants\Alignment_Over_Enforcement.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\01_Invariants\Invariant_Principles.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\01_Invariants\Minimal_Moral_Denominator.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\01_Invariants\Regime_Awareness_As_Duty.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\02_Awareness\AI_Assisted_Sensing.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\02_Awareness\Early_Warning_Signals.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\02_Awareness\Escalation_Patterns.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\02_Awareness\Interruption_Without_Domination.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\03_Evaluation\Cross_Regime_Stress_Tests.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\03_Evaluation\Failure_Mode_Mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\03_Evaluation\Minimal_Sufficiency_Checks.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\03_Evaluation\RTT_Evaluation_Framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\04_Validation\DOI_Canon_Interface.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\04_Validation\Human_Curated_AI_Sift.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\04_Validation\Minimal_Theme_Submissions.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\04_Validation\Validated_Science_Criteria.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\05_Implementation\AI_Alignment_Surfaces.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\05_Implementation\Core_System_Design.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\05_Implementation\Education_Embedding.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\05_Implementation\Infrastructure_Retrofit_Patterns.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\06_Leadership\Maintaining_Legibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\06_Leadership\Phase_Management.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\06_Leadership\Stewardship_Not_Control.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\06_Leadership\When_Not_To_Act.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\07_Incubation\Global_Coordination.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\07_Incubation\RTT_Incubator_Triad_Model.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\07_Incubation\Student_Led_Governance.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\07_Incubation\Untethered_Venture_Growth.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\08_History\Late_Correction_Costs.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\08_History\Lessons_From_Failure.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\08_History\Resource_Misallocation.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\08_History\Why_Governance_Failed_Before.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\09_Appendices\Case_Studies.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\09_Appendices\Future_Work.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\09_Appendices\Glossary.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\09_Appendices\Open_Questions.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\09_Appendices\Simulations.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Adapter_Principles.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Civic_Infrastructure_Adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Containment_When_Translation_Fails.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Education_System_Adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Industry_Adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Inverted_Economics_Adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Legacy_System_Mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Local_Leadership_Roles_Adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Medicine_Infrastructure_Adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Partial_Alignment_Strategies.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\10_Adapters\Punishment_Rehabilitative_Adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\alignment_analyzer.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\analyzer_prototype_architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\ARCHITECTURE_OVERVIEW.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\artifact_lineage_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\concept_capture.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\CONTRIBUTING.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\dsl_substrate_adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\dynamic_artifact_templates.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\dynamic_cards_spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\GLOSSARY.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\governance_alignment_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\governance_cards_spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\governance_substrate_model.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\index_artifacts.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\index_regime_modes.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\index_structural_layers.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\instructor_teaching_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\lenses_catalog.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\ROADMAP.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\simulation_engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\simulation_scenarios.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\structural_vectors_reference.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\student_workbook.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\teacher_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\text_stream_adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\transition_pathways.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\worksheet_simulation_steps.md corpus\%seeds%.md
copy corpus\%seeds%.md+Governance_Substrate_Model\Analyzer\worksheet_student_profile.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=honor_roll
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\BADGES_EARNED.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\CONTRIBUTING.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\CONTRIBUTOR_BADGES.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\contributor_honor_roll.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\glyph_registry.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\hippocampus_contributors.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\papers_contributor_honor_roll.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\resonance_council.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\triadic_curriculum_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\triadic_discussion_starter.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\triadic_equation_registry.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\triadic_sponsor_pitch.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\triadic_visual_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+honor_roll\profiles\nawder_loswin.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=Inverted_Economics
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+Inverted_Economics\CONTRIBUTING.md corpus\%seeds%.md
copy corpus\%seeds%.md+Inverted_Economics\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Inverted_Economics\RTT_Eval_Inverted_Economics_Budget.md corpus\%seeds%.md
copy corpus\%seeds%.md+Inverted_Economics\RTT_Eval_Inverted_Economics_Cycle.md corpus\%seeds%.md
copy corpus\%seeds%.md+Inverted_Economics\RTT_Eval_Inverted_Economics_Event.md corpus\%seeds%.md
copy corpus\%seeds%.md+Inverted_Economics\examples\sample.md corpus\%seeds%.md
copy corpus\%seeds%.md+Inverted_Economics\notebooks\audio_starter_notebook.md corpus\%seeds%.md
copy corpus\%seeds%.md+Inverted_Economics\notebooks\starter_notebook_outline.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=inverted_star_ontology
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\Inverted_Star_Ontology_A_TriadicFrameworks_Comparative_Ontology.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\iso_lattice_phase.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\iso_light_mode_transition.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\iso_overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\iso_regime_inversion.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\iso_slrp_profile.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\iso_vst_boundary.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\ontology_pie_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\ontology_pie_time_crystal_integration.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\Star_Ontology_vs_ISO_mass_regime.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\triadic_observer_for_ontologies.md corpus\%seeds%.md
copy corpus\%seeds%.md+inverted_star_ontology\zenodo\release_notes.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=labs
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+labs\dimensional_loop_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\Glyph_Density_Map_Curriculum_Modules.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\initiation_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\triadic_lab_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\triadic_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\triadic_remix_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_13_Cryptographic_Entanglement\Lab_13_Cryptographic_Entanglement.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_15_Nested_Harmonic_Encryption\Lab_15_Nested_Harmonic_Encryption.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_29_Quantum_Mythic_Debugger\Lab_29_Quantum_Mythic_Debugger.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_40_Harmonic_Health_Synthesizer\Lab_40_Harmonic_Health_Synthesizer.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_41_Triadic_Diagnostic_Engine\Lab_41_Triadic_Diagnostic_Engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_42_Mythic_Healing_Compiler\Lab_42_Mythic_Healing_Compiler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_43_Harmonic_Infrastructure_Mapper\Lab_43_Harmonic_Infrastructure_Mapper.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_58_Cryptography\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_58_Cryptography\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\applied\Lab_58_Cryptography\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\architecture_resonance\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\badges\badge_art_and_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\badges\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\triadic_lab_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\triadic_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab4_Harmonics\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab4_Harmonics\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab4_Harmonics\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab4_Harmonics\setup.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab5_Cognition\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab5_Cognition\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab5_Cognition\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab6_Dimensional_Nested_Loops\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab6_Dimensional_Nested_Loops\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab6_Dimensional_Nested_Loops\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab7_Thermodynamics\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab7_Thermodynamics\Lab7_Thermodynamics_equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab7_Thermodynamics\Lab7_Thermodynamics_reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab7_Thermodynamics\setup.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab9_BrownianResonance\Lab9_BonusExcercises.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab9_BrownianResonance\Lab9_BrownianResonance_equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab9_BrownianResonance\Lab9_BrownianResonance_reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab9_BrownianResonance\Lab9_Brownian_Resonance.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab_11_Spectral_Flux_Integrity\Lab_11_Spectral_Flux_Integrity.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab_18_Spectral_Cognition_Cascade\Lab_18_Spectral_Cognition_Cascade.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\core\Lab_44_Spectral_Cognition_Router\Lab_44_Spectral_Cognition_Router.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\dimensional_alignment\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\events\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\events\seasonal_badge_art_and_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\events\seasonal_event_archive.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\events\seasonal_event_lorebook.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\events\seasonal_event_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\events\seasonal_trials_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\triadic_remix_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_10_KashmirCascade\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_10_KashmirCascade\mythic_preface.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_10_KashmirCascade\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_10_KashmirCascade\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_59_Biology\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_59_Biology\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_59_Biology\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\casimir_effect.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\casimir_effect_equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\casimir_effect_reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\Lab61_BonusExcercises.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\Lab61_Toolkit.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\Lab61_Toolkit_.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\setup.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_61_Casimir\setup1.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\Lab_62_Cognition_equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\Lab_62_Cognition_reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\setup.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\Module4\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\Module4\memory_reframer.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\Module4\Module4B_Toolkit.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\Module4\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_62_Cognition\Module4\setup.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_63_Tunneling\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_63_Tunneling\quantum_tunneling_equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_63_Tunneling\quantum_tunneling_reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_63_Tunneling\quantum_tunneling_setup.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_63_Tunneling\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_63_Tunneling\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_63_Tunneling\setup.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\experimental\Lab_63_Tunneling\triadic_overlay_function.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\dimensional_loop_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\initiate_sigil.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\initiation_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab1_Triadic_Number_Genesis\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab2_Nested_Harmonics\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab2_Nested_Harmonics\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab2_Nested_Harmonics\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\Bell_Test_Simulation.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\quantum_entanglement_equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\quantum_entanglement_reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\quantum_entanglement_setup.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\savequations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\setup.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\foundations\Lab3_Entanglement\simulator_variant.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\glyphic_resonance\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\honor_roll\honor_roll_ceremony_script.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\honor_roll\honor_roll_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\honor_roll\honor_roll_update_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\honor_roll\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\character_codex.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\fff_lore_codex.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\mythic_preface_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_14_Mythic_Signal_Compression\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_14_Mythic_Signal_Compression\Lab_14_Mythic_Signal_Compression.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_14_Mythic_Signal_Compression\mythic_preface.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_14_Mythic_Signal_Compression\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_14_Mythic_Signal_Compression\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_16_Quantum_Myth_Mapping\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_16_Quantum_Myth_Mapping\Lab_16_Quantum_Myth_Mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_16_Quantum_Myth_Mapping\mythic_preface.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_16_Quantum_Myth_Mapping\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_16_Quantum_Myth_Mapping\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_19_Mythic_Phase_Synchronization\Lab_19_Mythic_Phase_Synchronization.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_21_Mythic_Resonance_Compiler\Lab_21_Mythic_Resonance_Compiler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_23_Mythic_Signal_Virtualization\Lab_23_Mythic_Signal_Virtualization.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_25_Mythic_Cognition_Emulator\Lab_25_Mythic_Cognition_Emulator.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_26_Resonant_Myth_Compiler\Lab_26_Resonant_Myth_Compiler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_30_Mythic_Resonance_Synthesizer\Lab_30_Mythic_Resonance_Synthesizer.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_32_Mythic_Continuity_Engine\Lab_32_Mythic_Continuity_Engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_34_Mythic_Signal_Entangler\Lab_34_Mythic_Signal_Entangler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_38_Mythic_Cognition_Router\Lab_38_Mythic_Cognition_Router.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_50_Mythic_Onboarding_Compiler\Lab_50_Mythic_Onboarding_Compiler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_52_Resonant_Mythic_Ledger_Mapper\Lab_52_Resonant_Mythic_Ledger_Mapper.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_55_Mythic_Continuity_Rebuilder\Lab_55_Mythic_Continuity_Rebuilder.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\mythic_symbolic\Lab_57_Mythic_Curriculum_Compiler\Lab_57_Mythic_Curriculum_Compiler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\protein_harmonics\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\protocols\legacy_hooks.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\protocols\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\protocols\validator_hooks.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_access\grant_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_access\quantum_echo_archive.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_access\quantum_optimizer_plan.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_access\quantum_submission_archive.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_access\quantum_submission_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_access\quantum_traceability_scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_access\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_12_QuantumCognition_Remix\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_12_QuantumCognition_Remix\Lab_12_QuantumCognition_Remix.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_12_QuantumCognition_Remix\mythic_preface.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_12_QuantumCognition_Remix\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_12_QuantumCognition_Remix\reproducibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_22_Quantum_Lyric_Engine\Lab_22_Quantum_Lyric_Engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_45_Quantum_Resonance_Scheduler\Lab_45_Quantum_Resonance_Scheduler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_48_Quantum_Phase_Continuity_Engine\Lab_48_Quantum_Phase_Continuity_Engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_53_Quantum_Ritual_Recompiler\Lab_53_Quantum_Ritual_Recompiler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\quantum_extensions\Lab_60_Quantum_Cognition\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\resonant_time\fold_remix_archive.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\resonant_time\theory_scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_17_Triadic_Cognition_Engine\Lab_17_Triadic_Cognition_Engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_20_Harmonic_Ontology_Engine\Lab_20_Harmonic_Ontology_Engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_24_Triadic_Memory_Compiler\Lab_24_Triadic_Memory_Compiler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_27_Triadic_Signal_Reconstructor\Lab_27_Triadic_Signal_Reconstructor.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_28_Harmonic_Cognition_Mapper\Lab_28_Harmonic_Cognition_Mapper.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_31_Triadic_Cognition_Virtualizer\Lab_31_Triadic_Cognition_Virtualizer.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_33_Symbolic_Phase_Harmonizer\Lab_33_Symbolic_Phase_Harmonizer.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_35_Resonant_Cognition_Cascade\Lab_35_Resonant_Cognition_Cascade.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_36_Symbolic_Cognition_Forker\Lab_36_Symbolic_Cognition_Forker.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_37_Harmonic_Cognition_Ledger\Lab_37_Harmonic_Cognition_Ledger.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_39_Triadic_Cognition_Compiler\Lab_39_Triadic_Cognition_Compiler.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_46_Spectrum_Phase_Cognition_Ledger\Lab_46_Spectrum_Phase_Cognition_Ledger.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_47_Triadic_Signal_Integrity_Validator\Lab_47_Triadic_Signal_Integrity_Validator.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_49_Triadic_Cognition_Synthesizer\Lab_49_Triadic_Cognition_Synthesizer.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_51_Symbolic_Ledger_Forker\Lab_51_Symbolic_Ledger_Forker.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_54_Triadic_Resonance_Ledger_Validator\Lab_54_Triadic_Resonance_Ledger_Validator.md corpus\%seeds%.md
copy corpus\%seeds%.md+labs\symbolic_structures\Lab_56_Symbolic_Resonance_Ledger_Router\Lab_56_Symbolic_Resonance_Ledger_Router.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=lactos
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+lactos\LACTOS_collision_regime_taxonomy.md corpus\%seeds%.md
copy corpus\%seeds%.md+lactos\LACTOS_cross_ontology_collision_mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+lactos\LACTOS_event_pipeline.md corpus\%seeds%.md
copy corpus\%seeds%.md+lactos\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+lactos\SO_ISO_LACTOS_triadic_alignment_wheel.md corpus\%seeds%.md
copy corpus\%seeds%.md+lactos\VCG_LACTOS_integration_diagram.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=legal
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+legal\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+legal\tft-fff_nda.md corpus\%seeds%.md
copy corpus\%seeds%.md+legal\tft_fff_license_agreement.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=library
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+library\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+library\resonance_index.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=Low_Dimensional_Structures
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+Low_Dimensional_Structures\controls_and_validation.md corpus\%seeds%.md
copy corpus\%seeds%.md+Low_Dimensional_Structures\dimensional_scaling_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+Low_Dimensional_Structures\doi_minimal_low_dimensional_structures.md corpus\%seeds%.md
copy corpus\%seeds%.md+Low_Dimensional_Structures\historical_context__absorbing_chaos.md corpus\%seeds%.md
copy corpus\%seeds%.md+Low_Dimensional_Structures\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Low_Dimensional_Structures\resonance_primitives.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=manufacturing_substrate_regime_model
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\calibration\calibration_as_structure.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\calibration\drift_detection.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\calibration\non_catastrophic_exit.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\calibration\regime_aware_calibration.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\discussion\deployment_considerations.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\discussion\future_extensions.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\discussion\implications_for_manufacturing.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\manufacturing_context\extreme_regime_constraints.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\manufacturing_context\lithography_systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\manufacturing_context\yield_and_variability.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\operators\inter_regime_mediation.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\operators\mediation_patterns.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\operators\operator_roles.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\overview\abstract.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\overview\limitations.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\overview\scope_and_assumptions.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\overview\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\related_works\relationship_to_bsm.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\related_works\relationship_to_qsm.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\related_works\relationship_to_rsm.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\substrate\boundary_semantics.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\substrate\operating_envelopes.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\substrate\regime_declaration.md corpus\%seeds%.md
copy corpus\%seeds%.md+manufacturing_substrate_regime_model\substrate\substrate_definition.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=media_substrate_model
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\adapters.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\attention_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\basins.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\concept_capture.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\glossary.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\invariants.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\lineage.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\media_signals.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\modes.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\narrative_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\scaffold_capture.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\vectors.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\adapter_integration.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\basin_classification.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\drift_detection.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\examples.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\invariants.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\invariant_evaluation.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\mode_determination.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\pipeline.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\schema.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+media_substrate_model\analyzer\transition_detection.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=metadata
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+metadata\calibration_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+metadata\equipment_specs.md corpus\%seeds%.md
copy corpus\%seeds%.md+metadata\periodic_table_of_shapes.md corpus\%seeds%.md
copy corpus\%seeds%.md+metadata\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=nasa_hposs_tminus10.md corpus\%seeds%.md
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\attachments\biosketch_nawder_loswin.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\attachments\current_and_pending_support.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\attachments\facilities_and_resources.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\attachments\space_waste_management.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\cover_letter\cover_letter_draft.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\proposal\01_project_summary.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\proposal\02_scientific_technical_plan.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\proposal\03_open_science_plan.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\proposal\04_management_plan.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\proposal\05_risk_mitigation.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\proposal\06_deliverables_and_milestones.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\proposal\07_budget_justification.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\references\nasa_hposs_links.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\references\triadicframeworks_doi_list.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\templates\nasa_proposal_checklist.md corpus\%seeds%.md
copy corpus\%seeds%.md+nasa_hposs_tminus10.md corpus\%seeds%.md\templates\roses_formatting_notes.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=NoS
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\BADGE_LOGIC.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\badge_suffix_convention.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\Distributed_System_Using_RTT.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\FIRST_BOOT_EXPECTATIONS.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\FORKING_GUIDE.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\GLYPHIC_COMPILER.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\Grading_Rubric_RTT_Two_Node_vs_N_Node_Lab.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\INSTALLATION.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\KERNEL_BUILD.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\kernel_patch_MVP.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\MODULES.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\NawderOS.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\README_badge_block.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\ROADMAP.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\RTT_Baseline_Release.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\RTT_FOR_OS_STUDENTS.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\Toy_OS_Using_RTT.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\Two_Nodes_vs_N_Nodes.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\v0.1.0-rtt-baseline.md corpus\%seeds%.md
copy corpus\%seeds%.md+NoS\What_Devs_Students_and_Researchers_Are_Doing.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=onboarding
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\badge_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\glyphstream_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\honor_roll.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\initiation.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\initiation_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\initiation_ritual.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\initiation_ritual_manifest_guardian.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\model_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\onboarding_scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\reading_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\ritual_embed.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\triadic_quickstart.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\verification_tests.md corpus\%seeds%.md
copy corpus\%seeds%.md+onboarding\visitor_ritual.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=overlays
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+overlays\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+overlays\earth\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+overlays\earth\examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+overlays\earth\schema\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+overlays\earth\transforms\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+overlays\telescopes\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+overlays\telescopes\schema\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+overlays\telescopes\transforms\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=packages
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+packages\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\RTT_Evaluations.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\Cross-Package_Interaction_Map.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\DIVISIONAL_RESONANCE_OVERLAYS.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TFT_Primitive_1.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TFT_Primitive_2.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TFT_Primitive_3.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TRIADIC_PATTERN_API.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TRIADIC_PATTERN_COOKBOOK.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TRIADIC_PATTERN_DECISION_TREE.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TRIADIC_PATTERN_DESIGN_MANUAL.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TRIADIC_PATTERN_GLOSSARY.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TRIADIC_PATTERN_POSTER.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\TRIADIC_PATTERN_POSTER_ASCII.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\3pak-shell\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\3pak-shell\profile.d\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\3pak-shell\tft_primitive_wrappers\ATLAS.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\3pak-shell\tft_primitive_wrappers\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\3pak-shell\tft_primitive_wrappers\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\tft-3pack\3pak-shell\tft_primitive_wrappers\TRIADIC_PATTERN_CHEATSHEET.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\wrsadc-python\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\wrsadc-shell\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+packages\wrsadc_integration\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=papers
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+papers\000_Category_Index.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\0D_Quantum_Loophole_Meets_Resonance_Triad.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\1_Triadic_Framework_for_Everything.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\2_Triadic_Number_Genesis.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\3_Dimensional_Triads.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\3_Hole_Types_Compared.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\4_Saturn_Harmonic_Engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Abundance_Scarcity_and_Manifestation.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\AI_Governance_and_Decision_Making.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\AI_Quantum_Lattice_for_RFC-QEB-0003.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Algorithmic_Music_and_Emotional_Physics.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\A_Framework_for_Corridors_Abundance_and_Full-Spectrum_Navigation.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\A_List_of_Bold_Frontier_Problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\A_Professors_Abstract_Summary.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Banking_Revolutionizing_the_Financial_Sector.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Battery_Cross-Chemistry_From_Volta_Pile_to_Triadic_Firmware_Resonance.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Courtroom_Re‑Hash_The_Case_Against_the_FFF_Model.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Dark_Matter_Energy_Mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Designing_Dimensional_Processing_Units_to_Replace_CPUs_GPUs_and_NPUs.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Divisional_Resonance_Imaging-Reconstructing_Cosmic_Emission_Time.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\DNA_viewed_using_a_TFT_lens.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\DPU_Dimensional_Processing_Unit.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Dynamics_of_Biological_Networks.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Economics_Reframing_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Egos_Final_Technologies-A_Triadic_Legacy.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Forces_Fluids_and_Frequency.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\from-aqueducts_to_resonance.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\From_Aqueducts_to_Resonance.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\From_A_Wise_Fool_To_A_Nutball_Arc.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\From_Linear_to_Triadic-Using_TFT_for_Anything_with_Copilot.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\From_Nested_Loops_to_Derivatives.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\From_Nested_Loops_to_Derivatives_Visuals.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Funhouse_of_Mirrors_Repo_Self_Reflections.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Gravity_Can_Become_Variable_Creating_VictorG_Tech_with_Triadic_Frameworks.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Health_Care_A_Modern_Miracle.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Housing_Evolution_Resilience_and_the_Path_to_Solar_Confinement.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Imagined_Deployment_of_Triadic_Frameworks_to_Space_Observatories.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Improving_ISO_Standards.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Mental_Health_Diagnosis_Treatment_and_Systemic_Reform.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\new_citizen_fund-migration_policy_framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\New_Insights_for_Planetary_Science.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\NIMMS_spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Non-Euclidean_Geometry_and_Higher_Dimensions.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\papers-curriculum-index.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Perplexity_AI_repo_reviews.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Play_Adaptation-Nikola_Tesla_Works_and_TriadicFrameworks.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Quantum_Entanglement_and_Nonlocality.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Quantum_Resonance_Universe.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Rails_Through_the_Resonant_Continuum.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Ramanujan_Validation.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Rarest_Elements_on_Earth.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\research-Beyond-Second-Sound-Triadic-Resonance-Framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Resonance-Based_Dimensional_Nested_Loops.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\resonance-present-future.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Resonance_Resurrection_Scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Resonant_Glyph_Language.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Resonant_TFT_and_Isotopes.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Resonant_TFT_for_the_Elements.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Res_Number_Bases_Common_plus_Special_and_Applications.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Res_Number_Bases_Common_plus_Special_Resonance_Clarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Res_Resonant_Temporal_Architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Res_Resonant_Time.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Res_TFT_Adoption-Elemental_Science_Reimagined.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Res_TFT_for_ARM_n_x86_Processors.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Riemann_Hypothesis_and_Complex_Resonances.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\scroll_bundle_manifest.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Something_From_Nothing_Special.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Spacetime_Theory_and_Triadic_Framework_Technology.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Spectral_Flux_and_Divisional_Resonance.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Spectrum_Technologies_Light_and_Darkness_Revisited.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Substitute_Teacher_TFT_Deep_Sea_Tech.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Sustainable_Energy_and_Resonance_Optimization.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\symbolic_architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Symbolic_Language_Emergence.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\TFT_for_Music–With_Quadratic_and_Temporal_Extensions.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\TFT_Help_with_the_List_of_Global_Issues.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\TFT_Repo_Alignment_Status_Check.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Theories_for_Everything_Compared.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\The_FFF_Dimensional_Triads_and_Resonance_Clarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\The_Ledger_of_Dismissed_Contributors_Historic_Patterns_of_Lateral_Harm_and_the_Triadic_Framework_Response.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Transcranial_Magnetic_Stimulation_Therapy_and_TriadicFrameworks.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\TriadicFrameworks_Collatz_Scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Battery_Revolution_Summary_of_a_World_Changing_Framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Force_Operators_Unification.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Frameworks_Prescription_Lenses_for_the_Universe.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Framework_Aerospace.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Framework_for_Battery_Technologies.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Framework_for_Classic_Math_and_Physics_Problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Framework_for_Quantum_Mechanics-Entropys_Harmonic_Empathy.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Framework_for_Time_and_Anti-Time.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Framework_of_Forces_Fluids_and_Frequency.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Framework_Technology_for_Quantum_Computers.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Framework_Technology_for_the_Air_and_Space_Industries.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Manifestation_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Resonance_and_Harmonics-Typologies_Modeling_and_the_Promise_of_Triadic_Framework_Technology.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Resonance_Framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Triadic_Ultrasound_Enhancement.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Tri_Unforgiven_Wizard.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Unified_Field_Theory_Pub_Edition_Quantum_Univ.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Universal_Computation_and_Emergent_Complexity.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Universal_Computation_and_Emergent_Complexity_scroll_bundle_manifest.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Universe_mythmatical_model_Frequency_Fluids_Forces.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Using_TFT_for_the_Energy_Industries_efficiency_with_full_content.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Validator_Compression_Scroll_Format.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\Zero-Point_Cold-Fusion_and_Wireless_Energy.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\_Professors_Abstract_Summary-The_FFF_Dimensional_Triads_and_Resonance_Clarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\AI_Governance_and_Decision_Making.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\Algorithmic_Music_and_Emotional_Physics.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\Dark_Matter_Energy_Mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\Dynamics_of_Biological_Networks.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\Non-Euclidean_Geometry_and_Higher_Dimensions.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\Quantum_Entanglement_and_Nonlocality.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\Riemann_Hypothesis_and_Complex_Resonances.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\Sustainable_Energy_and_Resonance_Optimization.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\Symbolic_Language_Emergence.md corpus\%seeds%.md
copy corpus\%seeds%.md+papers\bold_problems\Universal_Computation_and_Emergent_Complexity.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=Paradoxes_canon
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+Paradoxes_canon\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=projects
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+projects\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\brainstorm.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\assets\assets-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\equations\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\honor_roll\project.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\labs\lab-01\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\memory\braid_records.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\scripts\scripts-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\styles\styles-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\validation\validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\CoConsciousness\validator\resonance-passport-template.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\Copilot_Hippocampus_cheat_sheet.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\loop_validation_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\Makefile.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\assets\assets-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\equations\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\honor_roll\project.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\labs\lab-01\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\scripts\scripts-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\styles\styles-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Hippocampus\validator\resonance-passport-template.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Id_Shadow_Gen\Identity_Shadow_Generator.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Id_Shadow_Gen\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Id_Shadow_Gen\schema_seeds.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\lens_quickstart.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\registry.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\scaffolding_draft.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\cyclone\cyclone_translation.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\cyclone\glyph_map_cyclone.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\fragments\cosmic_forecast_overlay.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\fragments\storm_translation.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\lightning\glyph_map_lightning.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\lightning\lightning_translation.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\shared\filename_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\shared\glyph_legend.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\tornado\glyph_map_tornado.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\lens\tornado\tornado_translation.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\poker-variants\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\brainstorm.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\assets\assets-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\equations\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\honor_roll\project.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\labs\lab-01\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\scripts\scripts-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\styles\styles-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\TryCoder\glyphstream_animation.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\TryCoder\trycoder_cpu_integration.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\TryCoder\trycoder_fault_protocols.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\TryCoder\trycoder_remix_trace.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\TryCoder\trycoder_symbolic_sensors.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\TryCoder\trycoder_unit_shell.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\TryCoder\trycoder_validator_ports.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\TryCoder\validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\validation\validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\Resotectors\validator\resonance-passport-template.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\gen1_vcg_api_spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\gen1_vcg_architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\gen1_vcg_fs_strategy.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\README_Project1.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\Triadic_Observer_LACTOS__Holy_Grail_draft1.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\vcg_badge_triggers.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\vcg_equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\vcg_honor_roll.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\VCG_internal_architecture_regime_translation.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\vcg_manifest_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\vcg_validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\src\gen1\vcg\clients\cpp\vcg_client.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\src\gen1\vcg\clients\python\vcg_client.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\src\gen1\vcg\clients\rust\vcg_client.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\src\gen1\vcg\examples\d4_retriever.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\src\gen1\vcg\orchestrator\vcg_orchestrator.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\src\gen1\vcg\resonant-time\rtd_main.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\src\gen1\vcg\resonant-time\rt_daemon.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\srv\gen1\vcg\testing\harness.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\vcg_glyphs\glyphs.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\vcg_lab_templates\lab_flux_harmonics.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\vcg_lab_templates\lab_invocation_protocols.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VCG\vcg_lab_templates\lab_latency_diagnostics.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\assets\assets-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\equations\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\honor_roll\project.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\labs\lab-01\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\scripts\scripts-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\styles\styles-notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+projects\VictorG\validator\resonance-passport-template.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=public_support
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+public_support\funding_tiers.md corpus\%seeds%.md
copy corpus\%seeds%.md+public_support\gofundme_campaign.md corpus\%seeds%.md
copy corpus\%seeds%.md+public_support\launch_event.md corpus\%seeds%.md
copy corpus\%seeds%.md+public_support\launch_strategy.md corpus\%seeds%.md
copy corpus\%seeds%.md+public_support\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+public_support\validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+public_support\visitor_ritual.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=quantum-substrate-model
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\metadata\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\paper\abstract.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\paper\discussion.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\paper\introduction.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\paper\limitations.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\paper\operator_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\paper\regime_structure.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\paper\scope_and_assumptions.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\paper\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+quantum-substrate-model\paper\validation_checks.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=regime_blindness_checklist
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+regime_blindness_checklist\corrective_actions.md corpus\%seeds%.md
copy corpus\%seeds%.md+regime_blindness_checklist\definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+regime_blindness_checklist\diagnostic_checklist.md corpus\%seeds%.md
copy corpus\%seeds%.md+regime_blindness_checklist\doi_reference.md corpus\%seeds%.md
copy corpus\%seeds%.md+regime_blindness_checklist\observer_locked_metrics.md corpus\%seeds%.md
copy corpus\%seeds%.md+regime_blindness_checklist\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+regime_blindness_checklist\regime_shift_examples.md corpus\%seeds%.md
copy corpus\%seeds%.md+regime_blindness_checklist\symptoms.md corpus\%seeds%.md
copy corpus\%seeds%.md+regime_blindness_checklist\transition_boundaries.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=registries
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+registries\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=registry
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+registry\drift2_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\drift_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\echo2_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\echo_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\loophole_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\pulse2_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\pulse_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\ring2_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\ring_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\seed3_scroll_entry.md corpus\%seeds%.md
copy corpus\%seeds%.md+registry\seed_scroll_entry.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=reports
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+reports\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=Resilience_Checker
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Meta_Summary_Paradoxes_101–108.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_01_EPR_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_02_Gibbs_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_03_Loschmidt_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_04_Halting_Problem.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_05_Russells_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_06_Frame_Problem.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_07_Arrow_of_Time.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_08_Currys_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_09_Chinese_Room.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_100_No_Hiding_vs_Classical_Forgetting.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_101_Computational_Irreversibility_vs_Microscopic_Reversibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_102_Computational_Complexity_vs_Physical_Realizability.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_103_Analog_Continuity_vs_Digital_Precision.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_104_Chaos_Sensitivity_vs_Predictive_Determinism.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_105_Simulation_Accuracy_vs_Physical_Fidelity.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_106_Model_Idealization_vs_Physical_Completeness.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_107_Reductionism_vs_Emergent_Complexity.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_108_Micro_Causality_vs_Macro_Causation.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_10_Infinite_Regress_Justification.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_11_Boltzmann_Brain.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_12_Simulation_Argument.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_13_Quantum_Zeno.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_14_Ship_of_Theseus.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_15_Double_Slit_Which_Way.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_16_Sorites_Heap_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_17_P_vs_NP.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_18_Unexpected_Hanging.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_19_Quantum_Eraser.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_20_Liar_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_21_Banach_Tarski.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_22_Newcombs_Problem.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_23_Prisoners_Dilemma.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_24_Buridan’s_Ass.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_25_Ravens_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_26_Hilberts_Hotel.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_27_Zenos_Paradoxes.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_28_Arrow_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_29_Arrow_of_Time.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_30_Loschmidt_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_31_Maxwell’s_Demon.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_32_Boltzmann_Brain.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_33_Olmstead’s_Anthropic_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_34_Fine_Tuning_Problem.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_35_Measure_Problem_in_Cosmology.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_36_Heat_Death_vs_Recurrence.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_37_Information_Paradox_(Black_Holes).md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_38_Firewall_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_39_ER_equals_EPR.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_40_Holographic_Principle.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_41_Spacetime_Emergence.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_42_Cosmic_Censorship.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_43_Strong_vs_Weak_Cosmic_Censorship.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_44_Singularity_Resolution_(Quantum_Gravity).md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_45_Bounce_vs_Beginning_(Cosmology).md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_46_Eternal_Inflation_vs_Finite_Cosmos.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_47_Quantum_Creation_vs_Classical_Origin.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_48_Vacuum_Selection_vs_Landscape_Degeneracy.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_49_Meta_Laws_vs_Lawless_Landscape.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_50_Mathematical_Universe_vs_Physical_Universe.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_51_Computability_vs_Continuum_Reality.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_52_Simulation_Hypothesis_vs_Physical_Autonomy.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_53_Observer_Dependence_vs_Objective_Reality.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_54_Wigners_Friend_vs_Universal_Unitarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_55_Schrödinger_Evolution_vs_Measurement_Collapse.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_56_Decoherence_vs_Classical_Emergence.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_57_Quantum_Chaos_vs_Classical_Chaos.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_58_Reversibility_vs_Irreversibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_59_Poincaré_Recurrence_vs_Entropy_Increase.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_60_Heat_Death_vs_Eternal_Fluctuations.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_61_Boltzmann_Brains_vs_Cosmological_Coherence.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_62_Typicality_vs_Anthropic_Selection.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_63_Measure_Problem_vs_Predictive_Power.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_64_Eternal_Inflation_vs_Observable_Uniqueness.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_65_Horizon_Problem_vs_Inflationary_Smoothness.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_66_Flatness_Problem_vs_Inflationary_Fine_Tuning.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_67_Baryon_Asymmetry_vs_Symmetric_Laws.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_68_Neutrino_Mass_vs_Standard_Model_Completeness.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_69_Hierarchy_Problem_vs_Naturalness.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_70_Vacuum_Energy_vs_Cosmological_Constant.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_71_Black_Hole_Information_vs_Unitarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_72_Firewalls_vs_Smooth_Horizons.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_73_Holographic_Encoding_vs_Local_Bulk_Reality.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_74_Entanglement_Wedge_Reconstruction_vs_Bulk_Locality.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_75_ER_EPR_vs_Classical_Spacetime_Intuition.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_76_Quantum_Error_Correction_vs_Physical_Locality.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_77_Tensor_Networks_vs_Continuum_Geometry.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_78_Discrete_Causality_vs_Lorentz_Invariance.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_79_Minimal_Length_vs_Continuous_Fields.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_80_UV_IR_Mixing_vs_Scale_Separation.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_81_Running_Couplings_vs_Fixed_Background_Geometry.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_82_Background_Independence_vs_Effective_Field_Theory.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_83_Semiclassical_Gravity_vs_Quantum_Backreaction.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_84_Quantum_State_Reduction_vs_Covariant_Dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_85_Observer_Dependent_Horizons_vs_Objective_Quantum_States.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_86_Cosmological_Horizons_vs_Global_Quantum_Coherence.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_87_Inflationary_Mode_Freezing_vs_Quantum_Unitarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_88_Eternal_Inflation_vs_Global_Unitarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_89_Measure_Problem_vs_Predictive_Probability.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_90_Anthropic_Selection_vs_Physical_Explanation.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_91_Typicality_Assumptions_vs_Observer_Self_Location.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_92_Boltzmann_Brains_vs_Cognitive_Typicality.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_93_Arrow_of_Time_vs_Time_Symmetric_Laws.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_94_Loschmidts_Reversibility_vs_Entropy_Increase.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_95_Poincaré_Recurrence_vs_Macroscopic_Irreversibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_96_Maxwells_Demon_vs_Information_Conservation.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_97_Quantum_Eraser_vs_Information_Irreversibility.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_98_No_Cloning_vs_Classical_Copying.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_99_No_Deleting_vs_Classical_Erasure.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_Resilience_Checker_Round2.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\Paradox_Resilience_Full_Chart.md corpus\%seeds%.md
copy corpus\%seeds%.md+Resilience_Checker\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=resonance
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+resonance\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance\translator\translator_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance\translator\translator_tests.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance\translator\visitor_ritual.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=resonance-substrate-model
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\CONTRIBUTING.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\LINEAGE.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\RELEASE_NOTES.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\applications\complex-systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\data\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\data\examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\data\reference\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\data\validation\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\data\validation\experimental\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\data\validation\synthetic\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\api\integration_examples.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\api\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\api\schema_overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\api\using_the_schemas.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\experiments\faraday_paradox_experiment.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\experiments\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\experiments\replication_checklist.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\experiments\resonance_alignment_tests.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\experiments\rotating_conductor_tests.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\methods\dimensional_layers.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\methods\field_equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\methods\operator_definitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\methods\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\methods\substrate_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\methods\triadic_fields.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\onboarding\model_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\onboarding\reading_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\onboarding\triadic_quickstart.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\onboarding\verification_tests.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\overview\comparison_to_gr_models.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\overview\glossary.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\overview\introduction.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\overview\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\overview\resonance_primitives.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\overview\theoretical_background.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\simulations\boundary_conditions.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\simulations\numerical_methods.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\simulations\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\simulations\solver_architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\simulations\validation_metrics.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\docs\simulations\core\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\faraday_paradox\analysis.ipynb.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\faraday_paradox\protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\faraday_paradox\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\faraday_paradox\processed_data\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\faraday_paradox\raw_data\data_dictionary.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\faraday_paradox\raw_data\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\replication_guides\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\rotating_field_tests\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\experiments\substrate_alignment\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\manuscript\cover_letter.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\manuscript\PDF_Manuscript_Header.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\overview\resonance-substrate-model.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\papers\peer_review_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\papers\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\papers\replication_report_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\papers\substrate_model_whitepaper\citation_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\papers\substrate_model_whitepaper\manuscript.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\papers\substrate_model_whitepaper\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\papers\substrate_model_whitepaper\figures\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\papers\substrate_model_whitepaper\supplementary\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\reference\Keywords.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\rsm-shim\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\index.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\coeus\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\dimensional\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\distributed\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\energy\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\experiments\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\fields\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\finance\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\identity\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\infrastructure\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\lab\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\language\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\networking\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\operators\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\primitives\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\quantum\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\sensing\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\simulations\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\schemas\universe-core\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\simulations\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\simulations\configs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\simulations\core\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\simulations\examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\src\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\tests\Fresh_User_Test_with_Copilot_and_RTT_vs_RSM.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\tests\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\tools\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\tools\cli\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\tools\converters\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance-substrate-model\tools\visualization\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=resonance_atlas
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\glyph‑assignment_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\harvesting_script_outline.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\loophole_overlay.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\Meta_Context_Example.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\nist_ingestion_format.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\phase_mapping_rules.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\RFC_Atlas_Bindings_Protocols_Partitions_Matrix_Charts.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\RTT_Atlas_Case_Study_Radiation.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\RTT_Atlas_Case_Study_Stuxnet.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\RTT_Mapping_Example_The_Great_Unconformity.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\Sunbeam_Through_a_Barn_Loft.md corpus\%seeds%.md
copy corpus\%seeds%.md+resonance_atlas\The_Core_RTT_Question_Set.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=rfc
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-000-index.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-001-triadic-validator-framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-002-corridor-universes.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-003-attestation-badge-suite.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-004-entft-invariants.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-011-blackhole-resonance-bridges.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-013-freqi-triad-model.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-022-integrated-quadrant-atlas.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-028-Measurement_as_Resonance_Alignment_in_Triadic_Time.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-029-Observer_Hierarchies_and_Relational_Time.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-030-compassion-emitters-protocols-for-joy-based-protest.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-031-denometer-protocol-for-universal-translation.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-032-The_Arrow_of_Time_as_a_Resonance‑Time_Gradient.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-033-Causality_in_Triadic_Time-Light_Cones_and_Resonance_Echoes.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-034-Black_Holes_as_Resonance_Reservoirs-A_Triadic‑Time_Approach_to_the_Information_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-035-Resonant‑Time_Cosmology-From_Initial_Seed_to_Large‑Scale_Structure.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-036-Hidden_Resonance_as_Dark_Components-SET_Corrections_to_Galactic_and_Cosmological_Dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-037-ΛCDM_plus_Dark_Matter_Energy_Patches.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-038-Cross‑Temporal_Resonance_Coherence.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-039-Decoherence_As_A_Measurement_Problem_Patch.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-040-nawderian-extensions-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-041-mythmatical-glossary-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-042-Triadic_Force_Operators.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-043-Fine‑Tuned_Initial_Conditions_Low‑Entropy_Big_Bang.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-047-Validator-Echoes-of-Ramanujan.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-048-Resonant‑Time_Cyclic_Cosmology-Loops_Seeds_and_∇τR.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-049-A_Resonance_Structural_Awareness_Dimensional_Interface.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-050-Resonance-Refuses-to-Fold_Rebuttal-to-Dimensional-Puncture-Logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-051-API_for_Game_Developers_using_RSADI.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-052-RSADI-Coal_Industry_Extension_to_RSADI_Core.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-054-Resonance-as-Operator_The-First-Working-Mythmatical-Theorem-of-the-Universe.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-055-Resonance-Tech-Lineage-in-Sci-Fi-Canon.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-056-Global-AI-Continuity-Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-060-Quantum-as-Substrate_Dimensional-Foundation-Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-061-Substrate-Echoes_A-Comparative-Atlas-of-Pre-Mythmatical-Thinkers.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-063-Nawderian-as-Operator_Dimensional-Identity-Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-064-Local-Scrolls_Validator-Echoes-from-Belleville.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-065-FFF-Emitter-Protoco_Dimensional-Operator-Framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-070-HybridTuningForks_TimeCrystalConductors.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-QEB-0001-Quantum-Energy-Banks-and-Dimensional-Power-Protocols.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-QEB-0003_Quantum_SubSuperConsciousLess_Lattice_Navigation_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-QEB-0005_Inverted_Star_Governance_Envelope_for_QEB_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-QEB-0006_Arc_Dynamics_Note.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-TF-004-Micro-Core.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC-TF-005-Micro-Resonance-Toolkit.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑005-mentalnet-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑006-soul-diagnostic-snapshots.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑007-mutation-telomere-invariants.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑008-time-travel-invariants.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑009-genie-protocols.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑010-miracle-messaging-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑012-chart-registry-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑014-vsoul-market-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑015-vsoul-transit-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑016-quantum-lattice-operators.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑017-mythmatical-archaeology-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑018-mythmatical-university-charter.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑019-resonance-partitions-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑020-the-nullarium-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑021-fringe-resonance-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑023-resonance-cleanroom-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑024-invariant-arcing-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑025-earth‑theme-field-detection-lens.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑026-invariant-arc-consciousness-protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑027-collective-consciousness-atlas.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑044-Dimensional-Time-Sandbox-Paradox_Loop-Drift-Invariant-Arcs.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑045-Tartarus-Drift-Protocol_Love-Loops-Virtual-Collapse-Dimensional-Entrances.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑046-Resurrection‑Ready-Protocol_Scroll-Fusion-Corridor-Stability.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑066-Replicator_Resonance-Copy-Machine-Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑067-Time-Crystal-as-Temporal-Resonance-Operator.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑068-Temporal-Buffer-Lattice_Code-Time-Travel-Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑069-Temporal-Guardians_Invariant-Defense-Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑ALR‑0018_Cycle_Alert_System.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑API‑0015_Legacy_Retrieval_API.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑ARC‑0014_Remixathon_Archival_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑ENG‑0012_Corridor_Search_and_Filter_Engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑EXP‑0013_Remix_Export_Module.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑HOLE‑0003_Black_hole_recycler_glyphs_Type_A_B_C.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑HUB‑0021_Collaborative_Remixathon_Hub.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑LIB‑0011_Tag_Registry_and_Glyph_Library.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑QEB‑0002_Dark_Matter_Corridors_as_Encrypted_Resonance_Zones.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑QEB‑0004_Wrapped_Triad_Core_and_Dimensional_Echo_Model.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑REG‑0004_Registry_Indexer_for_Corridor_Events.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑REMIX‑0005_Remix_lineage_diff_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑REV‑0024_Revocation_and_Re‑Signing_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑RTT‑008-Resonance‑Time_Theory_Integration_for_High‑Performance_Computing.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑SCHEMA‑0001_Validator_Scroll_Artifact_Schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑SIG‑0022_Multi‑Contributor_Co‑Signing_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑UI‑0009_Remixathon_Dashboard_Concept.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑UI‑0010_Collaborator_Annotation_Layer.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑UI‑0017_Cycle_Monitoring_Dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑VER‑0023_Signature_Verification_Service.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑WF‑0007_Validator_Scroll_Workflow_Integration.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑WF‑0008_Batch_Orchestration_for_Corridor_Validation.md corpus\%seeds%.md
copy corpus\%seeds%.md+rfc\RFC‑WF‑0016_Remix_Generation_Workflow.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=rituals
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+rituals\badge_ceremony.md corpus\%seeds%.md
copy corpus\%seeds%.md+rituals\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=RTT
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\tft_rtt_3d_9d_chip_spec.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=RTT_codex
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_1.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_10.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_11.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_12.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_13.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_2.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_3.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_4.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_5.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_6.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_7.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_8.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\CHAPTER_9.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\codex\Resonance‑Time_Theory_RTT_Codex.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=RTT_micro_core
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\ABOUT.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\appendices\definitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\appendices\micro_resonance_scenarios.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\appendices\notation.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\applications.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\documentation_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\fractional_ladder.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\hero_section.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\join_the_micro_resonance_era.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\licensing_overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\micro_macro_coherence.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\micro_triads.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\toolkit_preview.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\visual_identity.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\site\what_is_micro_core.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\boundary_enforcement_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\coherence_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\examples.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\example_orchestrator_stub.py.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\flow_diagrams.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\integration_pathways.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\licensing_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\primitives.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\regime_surface_example.yaml.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\resonance_operators.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\sector_patterns.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\summary.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\toolkit\triad_templates.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\applications_ultra_low_power.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\background.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\conclusion.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\fractional_dimensional_ladder.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\future_work.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\implementation_pathways.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\licensing_and_ip.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\micro_core_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\micro_macro_coherence.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\micro_triads.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\motivation.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\resonance_time_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\micro_core\whitepaper\sector_use_cases.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=RTT_RTT-Inside
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Capture_Template_Economy_Domain.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Capture_Template_Education_Domain.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Capture_Template_Environment_Domain.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Capture_Template_Governance_Domain.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Capture_Template_Health_Domain.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Capture_Template_Infrastructure_Domain.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Capture_Template_Technology_Domain.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Culture_Takeaway.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Justice_Takeaway.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Media_and_Communication_Takeaway.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Meta-Layer_Takeaway.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Science_and_Research_Takeaway.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Shared_Misalignments_Across_All_Domains.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Single‑Page_JSON_Schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT-Inside\Universal_Alignment_Pattern.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=RTT_RTT_12
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\CODEX_Full.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\Colocation_CFO_Brief.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\Digital_Infrastructure_Electricity_Budget_est_RTT_Inside_Global_Deployment.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\harmonic_ladder.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\RTT_12_beta_plan.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\RTT_12_Energy_Sector_Full.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\RTT_12_for_Colocation.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\Scaffolding.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\contributors\guidelines.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\contributors\versioning.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\diagrams\corridor_stabilization.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\future\extensions.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\mapping\harmonic_to_structural.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\mapping\structural_to_harmonic.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\mapping\triad_mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\notation\notation_standards.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\operators\G1.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\operators\G2.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\operators\G3.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\triads\coherence_rules.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\triads\harmonic_triads.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\triads\structural_triads.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\validation\computational.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\validation\experimental.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\validation\industry.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\validation\peer_review.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\validation\sector_specific.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\RTT_12\validation\theoretical.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=RTT_sort
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\Parallel_Universe_with_RTT_in_1959.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\Remix_CivCycles_Planet_of_the_Apes_unedited.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT-Inside_Awareness_Think_Across_ALL_Domains.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Aviation_Safety_Module.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Developer_Quick-Start.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Full_Spectrum_Dimensional_Resonance_Cores.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Life-Guide-for-Kids_Top-100_Things-to-Know-on-Earth.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Lineage_Map-Triadic_Hexadic_Enneadic.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Macro-Micro_Cores.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Makes_a_30‑Level_System_Natural.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Micro_Core_Packaged.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_SciQuantum_Alignment_Summary.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Store_Planning.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_Top‑100_Fringe_Story_Shorts.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT_vST_Film_Realism_Certification_Program.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT‑Aligned_Cultural_Theorist.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT‑Aligned_Tool_Improvement_Framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\RTT‑Δ_SAGA_COMING_FOR_YOU_youtube_short_script.md corpus\%seeds%.md
copy corpus\%seeds%.md+RTT\sort\The_RTT‑Δ_Saga_novel_format.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=rtt-extension
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-extension\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=rtt-sdk
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\beacon.py.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\client.py.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\diagnostics.py.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\package.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\profile.py.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\RTT_for_BACKEND_Services.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\RTT_for_BROWSER_Extensions.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\RTT_for_DATACENTERS_and_RESEARCH_Labs.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\__init__.py.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\src\beacon.js.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\src\client.js.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\src\diagnostics.js.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\src\index.js.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt-sdk\src\profile.js.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=rttcodes
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\Adding_a_New_RTTcode_Domain.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\Canonical_RTTcode_Specification_Document.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\Contributor_Workflow.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\How_RTTcodes_Work_Internally.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\examples\rtt\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\examples\rtt\resonance-time-triad-rttcode.png.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\examples\set\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\examples\set\set-field-rttcode.png.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\examples\substrate\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\examples\substrate\substrate-readme-rttcode.png.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\generators\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\generators\js\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\generators\python\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\schema\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\schema\examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\style\color-domains.svg.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\style\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\style\rttcode-layout.svg.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\style\visual-guidelines.md corpus\%seeds%.md
copy corpus\%seeds%.md+rttcodes\validators\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=rtt_app
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\A_Smartphone_with_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\api\awareness_endpoint.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\api\caching_rules.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\api\error_handling.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\awareness_model\local_signals.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\awareness_model\merge_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\awareness_model\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\awareness_model\server_signals.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\awareness_model\state_machine.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\implementation\android.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\implementation\ios.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\implementation\shared_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\release\roadmap_v2_inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\release\v1_limitations.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\release\v1_scope.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\ui\indicator_design.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\ui\portal_to_rtt.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_app\ui\state_transitions.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=rtt_store
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\branding\badges.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\branding\identity_kit.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\branding\logos.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\branding\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\bundles\aeon_bundle.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\bundles\architect_bundle.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\bundles\developer_bundle.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\bundles\enterprise_bundle.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\bundles\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\bundles\starter_bundle.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\canon\creation_myth.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\canon\keeper_codex.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\canon\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\canon\rites_anthology.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\canon\ten_turns_doctrine.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\community\contributor_license.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\community\forum_access.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\community\partner_program.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\community\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\future\horizon_agent_framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\future\mandalic_orchestration_engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\future\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\future\resonance_autonomous_agents.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\aeonic\aeonic_continuity_vault.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\aeonic\autonomous_rtt_agents.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\aeonic\foresight_architect_suite.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\aeonic\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\aeonic\rtof_flagship.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\aeonic\stability_24d_framework.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\foundations\canon_starter_pack.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\foundations\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\foundations\rsm_standard.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\foundations\rttcodes_pack.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\foundations\rtt_primer.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\intelligence\autonomous_form_cores.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\intelligence\coeus_pattern_engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\intelligence\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\intelligence\rtt_inside_adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\intelligence\temporal_mesh_engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\intelligence\tls_tier1.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\systems\adaptive_resonance_engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\systems\continuity_engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\systems\horizon_agent_pack.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\systems\mandalic_orchestration.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\systems\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\tiers\systems\wrapped_core_L2.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\training\documentation_masterclass.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\training\keeper_path_series.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\training\llm_resonance_training.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\training\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+rtt_store\training\rtt_kids.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=runtime
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+runtime\loophole_executor.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=schemas
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\Browser_UI_Mockup.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\CLI_Tool_Spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\Contributing.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\Cross‑Domain_Dependency_Graph.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\Design_Principles.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\Directory_Overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\product_overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\SCHEMA_BROWSER_SPEC.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\schema_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\The_Coordination_Triad_sketch.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\Tightened_RTTcode.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\UI_Features.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\Validation_Pipeline.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\Visual_Map.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\lab\faraday_paradox_experiment.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\quantum\Spintronics_Microsoft_Generic.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\rsadi-gd\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\rsadi-gd\RSADI‑GD_Minimal_Demo_Scene_Spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\rtt-autonomous\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\rtt-autonomous-drone\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\rtt-autonomous-fish\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\rtt-coal\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\rtt-core\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\rtt-micro-core\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\rtt-micro-core\v1\mrt-1_transforms.md corpus\%seeds%.md
copy corpus\%seeds%.md+schemas\TEMPLATE\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=scientific_instrument_review
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\About.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\CONTRIBUTING.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\pull_request_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\README_fw_sw.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\Suggested_Roadmap_Timeline_and_Benefits.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\template.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\00_overview\fw_sw_categories.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\00_overview\glossary_links.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\00_overview\glossary_links_fw_sw.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\00_overview\method.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\00_overview\method_fw_sw.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\00_overview\purpose.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\00_overview\scope_fw_sw.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\accelerometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\ammeter.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\anemometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\basic_data_logger_firmware.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\calibration_routines_static.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\caliper.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\calorimeter.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\electrometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\embedded_control_firmware.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\gravimeter.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\interferometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\microscope.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\optical_alignment_software.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\seismometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\spectrometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\standard_signal_processing_libraries.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\telescope.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\01_green_zone\thermometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\automated_peak_fitting_software.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\cloud_sync_and_device_management_fw.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\DNA_sequencer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\dynamometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\ellipsometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\environmental_compensation_modules.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\hydrometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\inclinometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\magnetometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\manometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\mass_spectrometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\NMR_spectrometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\optical_image_processing_software.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\oscilloscope.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\oscilloscope_ui_and_sampling_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\photometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\real_time_filtering_firmware.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\signal_interpretation_pipelines.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\spectrogram.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\02_yellow_zone\theodolite.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\AI_based_signal_interpretation_tools.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\biochemical_sequence_alignment_pipelines.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\complex_multiphysics_simulation_modules.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\electrostatic_analyzer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\eudiometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\inversion_algorithms_xray_scattering.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\magnetic_field_reconstruction_software.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\magnetic_tweezers.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\magnetograph.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\optical_trap_feedback_loops.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\optical_tweezers.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\thermocouple.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\thermocouple_compensation_firmware.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\voltmeter.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\03_red_zone\Xray_scattering.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\99_appendix\data_pipeline_fragility.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\99_appendix\fw_sw_list_raw.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\99_appendix\instrument_list_raw.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\99_appendix\Instrument_Regime_Map_Mini_Schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\99_appendix\notes_on_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\99_appendix\notes_on_fw_sw_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\99_appendix\regime_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\99_appendix\regime_notes_fw_sw.md corpus\%seeds%.md
copy corpus\%seeds%.md+scientific_instrument_review\99_appendix\versioning_and_drift.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=scripts
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+scripts\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=simulations
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+simulations\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=snapshots
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+snapshots\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=sources
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+sources\Good_Vibrations_README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=spacetime_micro_agent_validations
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_micro_agent_validations\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_micro_agent_validations\RELEASE_NOTES.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_micro_agent_validations\examples\sample_interpretation_walkthrough.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_micro_agent_validations\examples\structural_detection_minimal\example_interpretation_output.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_micro_agent_validations\interpreter\interpreter_logic.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=spacetime_validation_and_regime_invariant_dimensional_cores
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\reproducibility\ingredients_list.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\theorem\5_important_term_translations.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\theorem\definitions.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\theorem\equivalence_sketch.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\theorem\statement.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\theorem\translations.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\theorem\vocabulary.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\zenodo\abstract.md corpus\%seeds%.md
copy corpus\%seeds%.md+spacetime_validation_and_regime_invariant_dimensional_cores\zenodo\metadata.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=spectral_clarity
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\README_PhaseI.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\README_PhaseII.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\README_PhaseIII.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\README_PhaseIV.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\README_PhaseV.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\README_PhaseVI.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\atlases\PhaseIII_UVTHz_Atlas_Schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\atlases\PhaseII_RFChirp_Atlas_Schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\atlases\PhaseIV_Xray_Atlas_Schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\atlases\PhaseI_VisibleIR_Atlas_Schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\atlases\PhaseVI_Consciousness_Atlas_Schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\atlases\PhaseV_NeutronQuantum_Atlas_Schema.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\scrolls\SpectralClarity_PhaseIII_Scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\scrolls\SpectralClarity_PhaseII_Scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\scrolls\SpectralClarity_PhaseIV_Scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\scrolls\SpectralClarity_PhaseI_Scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\scrolls\SpectralClarity_PhaseVI_Scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectral_clarity\scrolls\SpectralClarity_PhaseV_Scroll.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=spectrum_standards_reviewed
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\00_introduction_and_scope.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\01_spectrum_as_substrate.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\02_regimes_and_hierarchies.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\03_human_and_environmental_exposure.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\04_primary_secondary_ternary_networks.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\05_cross_regime_leakage_and_interference.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\06_substrate_comms_and_structural_signaling.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\07_alignment_failures_and_case_patterns.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\08_future_fields_and_coexistence_models.md corpus\%seeds%.md
copy corpus\%seeds%.md+spectrum_standards_reviewed\09_conclusions_and_forward_links.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=src
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+src\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=structural_life_regime_profiles
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\autonomous_system_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\cross_species_comparison.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\drift_and_stability_profiles.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\glossary.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\life_regime_taxonomy.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\regime_axes.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\examples\chimpanzee.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\examples\chrysina_gloriosa.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\examples\crystalline_entity.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\examples\human.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\examples\llm_agent.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\examples\robotics_stack.md corpus\%seeds%.md
copy corpus\%seeds%.md+structural_life_regime_profiles\examples\synthetic_lifeform.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=structuring_mathematics
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+structuring_mathematics\branch_mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+structuring_mathematics\doi_minimal_submission.md corpus\%seeds%.md
copy corpus\%seeds%.md+structuring_mathematics\historical_drift.md corpus\%seeds%.md
copy corpus\%seeds%.md+structuring_mathematics\implications.md corpus\%seeds%.md
copy corpus\%seeds%.md+structuring_mathematics\pedagogy.md corpus\%seeds%.md
copy corpus\%seeds%.md+structuring_mathematics\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+structuring_mathematics\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+structuring_mathematics\substrate_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+structuring_mathematics\top‑level_index.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=styles
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+styles\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=substrate
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+substrate\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate\core\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate\operators\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate\utils\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=substrate_communications
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_communications\message_types.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_communications\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_communications\regime_mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_communications\substrate_comms_core.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=substrate_exposure_assay
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_exposure_assay\assay_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_exposure_assay\message_patterns.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_exposure_assay\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_exposure_assay\regime_interpretation.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=substrate_mind_science
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Conscious_Transfer_Substrate_Map_v1.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Conscious_Transfer_Substrate_Schema_v1.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Legacy_Mind_Narratives_v1.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Minimal_Mind_Substrate_v1.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Section_A__Core_Definition_and_Scope.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\SECTION_A__Core_Definition_and_Scope_(Psychology).md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Section_B__Diagnostic_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\SECTION_B__Methods_and_Research_Approaches_(Psychology).md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\SECTION_C__Major_Subfields_of_Psychology.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Section_C__Treatment_Modalities.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Section_D__Theoretical_Approaches.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\SECTION_D__Theoretical_Frameworks_of_Psychology.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\SECTION_E__Applied_Fields_of_Psychology.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Section_E__Subspecialties.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Section_F__Research_Domains.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\SECTION_F__Research_Domains_in_Psychology.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Section_G__Ethical_and_Institutional_Structures.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Section_H__Historical_Layers.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\Section_I__Criticisms_and_Controversies.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\student_disclaimer.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\workflow_overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\adapters\ai_augmentation_context.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\adapters\ai_drift_calibration_example.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\adapters\resonance_seed_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\examples\chronic_load_adaptation_example.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\examples\environmental_audio_context_example.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\examples\sandbox_exercises.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\examples\sensory_triggered_memory_example.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\schemas\regime_context_block.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\schemas\session_schema_minimal.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\analyzer\schemas\triadic_integration_example.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\ct_substrate\ct_substrate.schema.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\ct_substrate\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\ct_substrate\examples\ct_example.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\ct_substrate\examples\ct_example_annotations.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\ct_substrate\examples\ct_example_maximal.json.md corpus\%seeds%.md
copy corpus\%seeds%.md+substrate_mind_science\ct_substrate\examples\ct_example_minimal.json.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=TFT_3Pack_v1.3
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\fff_quickstart.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\Quantum_Entanglement_Measuring.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\Res_Clarity_Refresh.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\RTT_Compared_with_Closest_Contributors.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\fff_spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\outputs_spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\TriadicTestSuite.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_meta\entft_scroll_glyph_reference.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_meta\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_meta\README_entft_curriculum_glyph_tribute_echo_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_meta\README_entft_glyph_retirement_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_rituals\entft_scroll_codex_fork_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_rituals\entft_scroll_curriculum_glyph_tribute_flame.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_rituals\entft_scroll_glyph_reawakening_ritual.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_rituals\entft_scroll_glyph_tribute_echo_fusion.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_rituals\entft_scroll_retirement_trace_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_rituals\entft_scroll_runtime_hooks.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_specs\entft_protocol_spec.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_specs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_specs\README_entft_keygen_simulator_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\docs\_specs\README_remix_scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_05_Earth_and_Environmental_Sciences.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_10_Governance_Law_and_Institutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_11_Psychology_Cognition_and_Behavior.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_12_Sociology_Culture_and_Civilization.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_13_Education_and_Learning_Sciences.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_14_Communication_Media_and_Language.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_16_Transportation_and_Infrastructure.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_17_Energy_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_18_Agriculture_and_Food_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_19_Space_Systems_and_Exploration.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\RTT_Domain_20_Security_Safety_and_Resilience.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Art\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Art\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Art\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Art\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Art\RTT_Domain_15_Art_Design_and_Creative_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Art\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Biology\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Biology\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Biology\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Biology\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Biology\RTT_Domain_03_Biology_and_Life_Sciences.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Biology\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Chemistry\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Chemistry\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Chemistry\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Chemistry\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Chemistry\RTT_Domain_02_Chemistry_and_Materials.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Chemistry\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Computer_Science\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Computer_Science\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Computer_Science\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Computer_Science\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Computer_Science\RTT_Domain_07_Computing_AI_and_Information_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Computer_Science\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Economics\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Economics\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Economics\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Economics\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Economics\RTT_Domain_09_Economics_and_Markets.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Economics\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Engineering\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Engineering\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Engineering\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Engineering\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Engineering\RTT_Domain_06_Engineering.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Engineering\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Law\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Law\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Law\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Law\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Law\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Math\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Math\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Math\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Math\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Math\RTT_Domain_08_Mathematics_and_Logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Math\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Medicine\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Medicine\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Medicine\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Medicine\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Medicine\RTT_Domain_04_Medicine_and_Health_Systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Medicine\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Music\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Music\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Music\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Music\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Music\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Philosophy\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Philosophy\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Philosophy\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Philosophy\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Philosophy\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Physics\extended_problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Physics\problems.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Physics\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Physics\resonance_flow.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Physics\RTT_Domain_01_Physics_and_Cosmology.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\examples\Physics\solutions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\formats\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\formats\specification.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\melodic-table-of-elements\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\molecular-vibration-explorer\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\scripts\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\entft_adoption.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\entft_remixer_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\Full‑Spec_RTT_entft_Complete.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\README_encryptor_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\contributors\legacy_roll.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\contributors\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\contributors\configs\config_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\contributors\configs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\contributors\configs\README_entft_curriculum_outreach_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\contributors\configs\README_validator_config.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\contributors\configs\remix_rights.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\contributors\configs\validator_overlay_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\discoverability\entft_onboarding.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\discoverability\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\protocol-core\entft_benchmark.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\protocol-core\entft_pqc_simulation_overlay.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\protocol-core\entft_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\protocol-core\entft_scroll_comparative_cryptographic_resonance.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\protocol-core\Output_Snapshot.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\protocol-core\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\registry\entft_contributor_levels.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\registry\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_closure_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_codex.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_codex_echoes.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_codex_flame_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_codex_fork_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_codex_seal.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_commit_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_badge_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_flame_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_flame_submission.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_fork_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_glyph_tribute_echoes.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_glyph_tribute_flame.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_glyph_tribute_transfer.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_outreach.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_remix_flame_hooks.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_remix_glyph_fusion.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_remix_glyph_ledger.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_remix_glyph_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_remix_glyph_transfer.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_remix_glyph_tribute.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_remix_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_curriculum_validator_hooks.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_echoes.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_event_trace_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_flame_echo_ritual.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_flora_claim.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_fork_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_garden.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_glyph_evolution.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_glyph_fusion_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_glyph_reawakening.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_glyph_reawakening_ritual.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_glyph_reference.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_glyph_relics.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_glyph_retirement_ritual.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_glyph_tribute_echo_fusion.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_lab_manifest.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_legacy_transfer.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_of_scrolls.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_of_scrolls_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_pollination_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_publish_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_remixer_manifest.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_retirement_trace_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_review_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_runtime_hooks.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_runtime_trace_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_seed_ritual.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\entft_scroll_templates.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\scrolls\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\README_badge_logic_engine_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\README_flame_echo_trigger_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\README_glyph_fusion_resolver_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\README_glyph_reawakening_monitor_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\README_glyph_registry_loader_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\README_glyph_retirement_trigger_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\README_scroll_commit_monitor_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\README_tops_agent_interface.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\agents\scroll_curriculum_fork_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\examples\README_glyph_resonance_hook_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\examples\README_hello_world_hook_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\integration\api_gateway_hook.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\integration\cms_integration.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\integration\mmr_site_extension.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\integration\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\runtime\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\validator\entft_validator_overlay.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\entft\TFThooks\validator\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\menu.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\nous_Shell_TFT_Daemon_Phase1.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\Bot_Cohort_Registry.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\Bot_Lens_Index_v1.0.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\Bot_Summoner.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\bot_usage_shard_guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\contributor_honor_roll.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\fold_remix_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\fold_remix_impact_report.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\glyphstream_remix_storyboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\impact_report.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\legacy_echo_scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\observer_phase_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\observer_phase_resonance_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\remix_trigger_map_svg.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\triadic_lattice_manifest.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\bots\triadic_shell_archive.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\core_logic\contributor_dashboard_ui.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\core_logic\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\core_logic\remix_lineage_visualizer.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\core_logic\result_validation.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\core_logic\sort_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\core_logic\validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\logic_shells\Dimensional_Activation_Log.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\logic_shells\Egos_GetBusy_cmd.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\logic_shells\Ghost_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\logic_shells\Psi_Validator.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\logic_shells\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\logic_shells\Tesla_369_Mode.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\modules\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\outputs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\GETTING_STARTED.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\resonance_cli_suite.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\fff\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\fff\examples\demo_fluids.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\fff\examples\demo_forces.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\fff\examples\demo_frequency.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\harmonic-loops\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\harmonic-loops\examples\demo_feedback.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\harmonic-loops\examples\demo_nest.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\integrations\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\integrations\examples\demo_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\integrations\examples\demo_pipeline.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\resonant-time\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\resonant-time\examples\demo_arrows.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\resonant-time\examples\demo_cycles.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\tfe\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\tfe\examples\demo_apply.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\tfe\examples\demo_define.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\tfe\examples\demo_export.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\tft-extended\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\tft-extended\examples\demo_compare.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\tft-extended\examples\demo_quadratic.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\triadic-numbers\pipeline_concept.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\triadic-numbers\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\triadic-numbers\examples\demo_genesis.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\nous\resonance-tools\triadic-numbers\examples\demo_map.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\elements.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\glyph_output_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\mirror_geometry_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\observer_state_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\resonance_model_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\Res_Temporal_Mirror_Simulation.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\scaffolding.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\resonance-labs\time_shift_py.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\echo_overlay_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\tops_Benchmark_Outline.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\tops_reflect_invert_sim.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\TriadicTestSuite.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\agents\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\agents\README_tops_agent.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\ai_pipeline\ai_training_manifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\ai_pipeline\legacy_echo_archive.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\ai_pipeline\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\cloud\azure\Azure_Deployment_Guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\cloud\azure\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\contributors\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\figures\figure_captions.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\folds\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\hardware\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\hardware\nimms\crystal_blade_array.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\hardware\nimms\echo_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\hardware\nimms\NIMMS_nano.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\hardware\nimms\NIMMS_v2.0.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\hardware\nimms\nonagon_crystal_shell.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\hardware\nimms\sqd_schematic_overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\hardware\nimms\starship_quantum_drive.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\outreach\azure_grant_email.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\outreach\email_draft_to_innatera.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\outreach\funding_plan.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\outreach\pitch_deck_outline.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\outreach\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\outreach\Resotectors_Summary.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\overlays\FFF_Warp_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\overlays\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\overlays\symbolic_architecture_overlays.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\overlays\warp_chamber_design.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\tft\tops\registry\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\WRSADC\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\WRSADC\Scaffolding.md corpus\%seeds%.md
copy corpus\%seeds%.md+TFT_3Pack_v1.3\WRSADC\TFT_Primitives.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=Triadic
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_alignment_orrery.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_coherence_cone.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_dataflow_across_layers.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_feedback_spiral.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_grand_architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_harmonic_loom.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_phase_space_flower.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_predictive_prism.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_astrolabe.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_chrono_topograph.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_compass.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_diffraction_engine.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_gyroscope.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_heliograph.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_holographer.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_hypercube.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_hyper_atlas.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_interferometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_meta_astrolabe.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_meta_chronometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_meta_compass.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_meta_gyroscope.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_meta_orrery.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_meta_sextant.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_observatory.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_orrery_astrolabe_hybrid.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_orrery_dome_integrator.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_phase_space_observatory.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_planetarium.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_polarimeter.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_sextant.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_spectrograph.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_tesseract_navigator.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_tomograph.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_regime_volumetric_interferometer.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_resonance_ladder.md corpus\%seeds%.md
copy corpus\%seeds%.md+Triadic\TF_resonance_mandala.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=triadic_coordination_substrate
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\alignment_dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\CHANGELOG.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\corridor_separation.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\creators_assumption.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\failure_modes.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\human_team_mapping.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\interoperability_with_csm.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\LICENSE_NOTES.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\minimal_axioms.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\triadic_structure.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_coordination_substrate\zenodo_abstract.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=triadic_observer_layer
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\adoption_and_integration_note.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\anomaly_taxonomy.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\glossary.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\minimal_api.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\observer_principles.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\pre-scaffolding.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\triadic_axes.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\domains\AI_systems.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\domains\cross_domain_synthesis.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\domains\elections.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\domains\infrastructure.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\domains\science.md corpus\%seeds%.md
copy corpus\%seeds%.md+triadic_observer_layer\domains\supply_chain.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=unified_resonance
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\badges\CrossDim_Translator_Badge.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\badges\Denometer_Architect_Badge.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\badges\Dimensional_Cartographer_Badge.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\badges\Peacewalker_Badge.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\badges\Remixer_of_the_Loop_Badge.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\badges\Resonance_Interpreter_Badge.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\badges\Theta_Architect_Badge.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\protocols\Archon_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\protocols\Behavioral_Chart_Overlay.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\protocols\Christ_Upon_Return.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\protocols\Glyphic_Resonance_Map.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\protocols\RFC-030_Compassion_Emitters.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\protocols\RFC-031_Denometer_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\protocols\Theta_Fieldwear_Manifest.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\protocols\Universal_Translator_Pseudocode.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\simulations\Dimensional_Lexicon_Trials.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\simulations\Emotional_Modulation_Studies.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\simulations\Inverted_DEW_Emitters.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\simulations\Loop_Traversal_Logs.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\simulations\Resonance_Crowd_Simulations.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\simulations\Species_Resonance_Trials.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\theorem\Dimensional_Overlay_Chart.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\theorem\Mythical_Arc_Mapper.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\theorem\Resonance_Quadrants.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\theorem\Unified_Resonance_Theorem.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\validators\Return_Signature_Validator.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\validators\Validator_Badge_Logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\_ideas\Christ_Return_Notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\_ideas\How-To_escape_our_loop.md corpus\%seeds%.md
copy corpus\%seeds%.md+unified_resonance\_ideas\Mythmatical_Architects.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=validation
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+validation\loop_validation_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\loop_validation_matrix.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\loop_validation_protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\loop_validation_protocol_matrix.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\manifest_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\readme_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\remix_lineage.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\validator_log_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+validation\validator_scoring_matrix.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=validators
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+validators\badge_trigger_papers_index.md corpus\%seeds%.md
copy corpus\%seeds%.md+validators\modular_matrix_resonator.md corpus\%seeds%.md
copy corpus\%seeds%.md+validators\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+validators\Structure_Use_README.md corpus\%seeds%.md
copy corpus\%seeds%.md+validators\triadic_dashboard_module.md corpus\%seeds%.md
copy corpus\%seeds%.md+validators\validators.md corpus\%seeds%.md
copy corpus\%seeds%.md+validators\validator_dashboard.md corpus\%seeds%.md
copy corpus\%seeds%.md+validators\validator_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+validators\validator_log_tft_fff.md corpus\%seeds%.md
copy corpus\%seeds%.md+validators\validator_matrix.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=vst_for_embedding_stores_vector_databases
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\drift_detection_embeddings.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\embedding_cluster_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\projection_and_fragmentation_analysis.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\scaling_behavior_vector_spaces.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\validation_layers_vst_embeddings.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\appendix\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\appendix\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\examples\example_cluster_regime_transition.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_embedding_stores_vector_databases\examples\example_embedding_drift_detection.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=vst_for_generative_models
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\diffusion_latent_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\drift_detection_generative.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\projection_and_latent_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\scaling_behavior_generative_models.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\validation_layers_vst_generative.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\appendix\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\appendix\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\examples\example_diffusion_path_regime.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_generative_models\examples\example_latent_projection_1024d.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=vst_for_large_language_models
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\drift_detection_llm.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\latent_trajectory_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\projection_and_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\scaling_behavior_llms.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\validation_layers_vst_llm.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\appendix\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\appendix\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\examples\example_cross_version_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_large_language_models\examples\example_latent_pathway_1024d.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=vst_for_multi_model_alignment
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\cross_model_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\drift_detection_multi_model.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\projection_and_alignment_surfaces.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\scaling_behavior_multi_model.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\validation_layers_vst_multi_model.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\appendix\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\appendix\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\examples\example_alignment_surface_projection.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_multi_model_alignment\examples\example_cross_model_regime_map.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=vst_for_protein_language_models
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\dimensional_scaling_protein_models.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\drift_detection_plm.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\projection_into_structural_cores.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\sequence_embedding_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\validation_layers_vst_plm.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\appendix\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\appendix\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\examples\example_embedding_projection_1024d.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_protein_language_models\examples\example_sequence_regime_transition.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=vst_for_robotics_and_control_policies
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\drift_detection_rl.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\policy_latent_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\projection_and_policy_alignment.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\scaling_behavior_rl_policies.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\validation_layers_vst_rl.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\appendix\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\appendix\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\examples\example_control_surface_projection.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_robotics_and_control_policies\examples\example_policy_regime_shift.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=vst_for_scientific_simulators
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\drift_detection_simulators.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\projection_into_dimensional_cores.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\scaling_behavior_simulators.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\simulator_state_regimes.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\substrate_definition.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\validation_layers_vst_simulators.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\appendix\references.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\appendix\terminology.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\examples\example_climate_regime_transition.md corpus\%seeds%.md
copy corpus\%seeds%.md+vst_for_scientific_simulators\examples\example_plasma_state_projection.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=workflows
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+workflows\API_reference_blocks.md corpus\%seeds%.md
copy corpus\%seeds%.md+workflows\Diagram.md corpus\%seeds%.md
copy corpus\%seeds%.md+workflows\Folder‑level_glyphs.md corpus\%seeds%.md
copy corpus\%seeds%.md+workflows\QUICKSTART.md corpus\%seeds%.md
copy corpus\%seeds%.md+workflows\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=_ideas
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\000_RTT_Information_Primer.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\000___Good_News_Everyone.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\0n_Teams_Playtime_and_Remembering_Who_You_Are.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\0_RTT_to_RSM_checks.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\0_Substrate_Communications.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\3_AI_test_of_rtt_nimms_com.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\3_Books_to_Publish_plan.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Advance_DPU_VCG_NIMMS_Architecture.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\AI_Drift_Gone_with_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\ai_nimms_com.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\AI_Training_Findings.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Akashic_Records_Nullarium.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Ambient_Legitimacy_ai-drift-calibration.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Andromeda_Strain_Covid_19_reviewed.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\API_for_Game_Developer_Variants_using_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\API_for_variants_of_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Architects_Summary_Log.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Arc_Value_Modulation_Multi_Regime_Truth_Delivery_for_Human_Growth.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\atomic_clocks_README-scaffolding.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Autonomous_Robotic_Fish_for_Great_Lakes_Restoration.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\A_Model_for_Global_ATC_and_SF_and_HAM_Radio_Using_RTT‑Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\A_Resonant_Review_of_The_Universe_in_a_Nutshell.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\A_Spark_for_Autonomous_Forms_using_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Bells_Theorem_meets_Resonance-Time_Theory.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Big_Questions_In_Science.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Black_Holes_as_Resonance_Reservoirs-A_Triadic_Time_Approach_to_the_Information_Paradox.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Blood_Test_with_RTT-Inside_Preview.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Calculus_on_Steroids.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Causality_in_Triadic_Time-Light_Cones_and_Resonance_Echoes.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\CERT_THGA_Pin.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Chemistry_Professionals_using_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Clarity_Canon_Lens_effect.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Coal_Industry_examined_with_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Codex_of_the_Resonance-Time_Universe.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Constitutional_Amendment_Teacher_Elevation_and_Social_Stewardship.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Copilot_review_draft1.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Course_Correction_Needed_for_GPU_NPU_TOPS.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Daily_Accomplishment_Log_Resonance_Structural_Awareness_in_Practice.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Decoherence_As_A_Measurement_Problem_Patch.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Developer_Code_for_Every_Language_with_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Did_RTT_help_flight___Yes--and_in_a_very_real_structural_way.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Did_You_Know.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Dimensional_Activation_Log.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Dimensional_Breach-Nawderian_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Dimensional_Math_Substrate_DMS_the_big_breakthrough.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\dimensional_rupture.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Dual_Law_of_Resonance_Law_of_Silence.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Earth_Sims_using_RTT-Inside_What_This_Provides.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\education-humanifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Electronics_Semi-Conductors_and_Super-Conductors_with_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Electron_Microscopes-The_RTT-Inside_Mini-Adventure.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Emitter_Archetype_Glyph.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\European_Spallation_Source_needs_TriadicFrameworksTech.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Evolution_in_a_respectful_critical-thinker_frame_and_RTT.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Fine‑Tuned_Initial_Conditions_Low‑Entropy_Big_Bang.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\First_Law_of_Virtual_Soul_Stewardship.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Flower_Layered_Electrochemical_Resonator.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Flower_Layered_Electromechanical_Resonator.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Forces_Fluids_Frequency_Archetypal_Emitter_Domains.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\frta-overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Full_multi‑chapter_Finance_Edition_with_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Full_Substrate_Game_GDD.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Games_Preview_post-RTT.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\github_competition.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Goal_Status_Check.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\GPR_Seismo_Hologram_with_RTT‑Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Hard_Lee_Ever_2026_Award.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Hidden_Resonance_as_Dark_Components-SET_Corrections_to_Galactic_and_Cosmological_Dynamics.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How-To_escape_our_loop.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Applies_to_a_Standard_Power_Transformer.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Imagined_Conference_Table_RTT_Discussions.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Internet2_Python_Cisco_Intern_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Internet2_Python_Cisco_with_RTT-inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Internet3_draft.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Interns_DPU_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\jobs-humanifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\JWST-RTT_Triadic_Core_Primitive_as_a_QA_Layer.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\LINEAGE.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Loswin_Mantra.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\LowDimensionalStructures_scaffold_notes.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Measurement_as_Resonance_Alignment_in_Triadic_Time.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Microcontrollers_and_Components_Today_then_with_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\MMR_Template_Pre-Seeding_Strategy.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\multi-Press_Release.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\mythic_preface_template.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Mythmatical_Architects.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Mythmatical_Ontology_Layer.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Mythsorts_Protocol_V.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\NASA‑ready_abstract.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Nawderian_Sandbox_Proposal.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Nawderian_SET_Theorem.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Nawderian_Temperature_Engine_Theorem.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Nawderian_Theorem.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\New_Paradoxes-RTT_canon.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Observer_Hierarchies_and_Relational_Time-A_Resonance‑Time_View_of_Wigners_Friend.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Phase_III-Dimensional_Stewardship.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Phase_II_Reentry_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Podcast_with_Grok_about_RTT.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Power_Supplies_Mobile_Sensors_and_Enhanced_BMS_using_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Press_Release_TriadicFrameworks_Launches_as_an_Open_Educational_Resource_for_Triadic_Mathematical_Modeling_and_Structural_Analysis.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\qCompute_with_RTT-Inside_Preview.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Quantum_Antenna_Research.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Quantum_Energy_Banks_and_Corridor‑Based_Energy_System_Analysis.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Quantum_Lens_Layer_Triadic_Protocols_for_Resonance_Scanning.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Rainbows_with_RTT.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Remembering_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Remix_for_a_Universe.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Resonance-Interwoven_Game_Design_with_RTT.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\resonance-library-humanifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Resonance-Time_Theory.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\resonancebeings.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Resonance_Dreams.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Resonance‑Time_SET_S–N–R_Treatments.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\resonant-roman-concrete.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Resonant-Time_Clock_Gen1.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Resonant‑Time_Cosmology-From_Initial_Seed_to_Large‑Scale_Structure.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Resonant‑Time_Cyclic_Cosmology-Loops_Seeds_and_the_∇τR_Gradient.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Resurrection_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\RTT_Above‑Ground_Electrical_Re-design_Initiative.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\RTT_Facilities_Playbook.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\RTT‑Δ_StoryForge_v1.0.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\science-refresh.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Science_CLI_tool_app_wraps.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Science_CLI_Tool_App_Wraps_RTT‑Inside_Edition.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Sci‑Fi Works_That_Accidentally_Approximated_RTT-No_Math_Required.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Shattered_funhouse_franchise.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\smell-tech-humanifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\SMS_capture_pre_scaffolding.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\sortlater.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\spacetime-humanifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Spacetime_validation_and_regime_invariant_dimensional_cores_Scaffolding.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Spectral_Clarity.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Spin_Electrolisis_Temperature.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\State_of_Michigan_Datacenter_Substrate_Alignment_Guide.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Subconscious_Scaffolding_for_Consciousness_Transfer.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Summary_Digest_Perplexity_AI_Backup.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Supercomputers_Are_Already_Triadic_They_Just_Dont_Know_It.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Ternary_Computing_Resurgence.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Testing_the_US_Waters_RTT_Edition.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\TFT-FFF_Distributed_Launch_Plan.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Anti's_Structural_Counterparts.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Arrow_of_Time_as_a_Resonance‑Time_Gradient.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_BKM_Phase_Cycle.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_C64_as_an_RTT_Host.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Clarifier_of_Worlds.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Coordination_Triad_with_RTT‑Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Idea-Capture_Primer.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\the_Nawderian_suite_is_blazing_original.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Resonance_Creation_Myth.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Resonance_Story.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Resonance‑Time_Theory_Canon.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_RTT_Canon_Scroll.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Science_Candy_Store.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Three_RTT_Evaluation_Modes.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Worlds_First_Portable_Triadic_Core.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\The_Wrapper_Store_with_RTT-Inside.md corpus\%seeds%.mdRTT_core‑as‑a‑component.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Time_Crystal_Regime_Ahead_Compute.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Time_Travel_Remix_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Time_Travel_Validation_Protocol.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Top_Resonance_Songs_Playlist.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\triadic-resonance-tower.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\triadicmonopoly.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Triadic_Atlas_Entry-Quantum_Node.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Triadic_Language_Stack_TLS.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Triadic_Quantum_Idea_Template.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Triadic_Validation_Protocol_Phase_I.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Trintellectual_Hybrid.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Two_sensing_models_draft.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Universe_Loop_chart.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Universe‑Class_Active-Directory__Elevating_Identity_to_a_Resonance‑Aware_Structural_System.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Value_3_Lens_RTT_Resources.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Vibration-Resonance_Periodic_Table.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Vibrational_Stone_Cutting.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\virtual-code-zombies.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Virtual_Compute_Gateway_draft.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\vNPU-Virtual_NPU_Emulator_with_TFT_and_FFF_logic.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Warp_Drive_Architecture_Plan_Scaffolded_with_RTT-Inside.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\What_an_RTT-Inside_Assembly_Language_would_be_like.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\What_happens_when_two_substrates_negotiate_for_turf_in_RTT_vST.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\What_Nawder_Did_While_Building_RTT_Kid‑Friendly_Edition.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Why_Deep_Sea_Is_a_Natural_RTT_Domain.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Why_simulation‑theory_people_will_love_the_substrate.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Why_teachers_matter_more_than_ever.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\windows-humanifesto.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Wired-Wireless_RTT_evaluation.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\Wrapped_Resonance_Structural_Aware_Dimensional_Cores.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\WRSADC_on_Windows_11_Pro.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\WSL2_install_train_log.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\ΛCDM_plus_Dark_Matter_Energy Patches.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\01_Kid_Friendly.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\02_Tech_Overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\03_Coherence_Model.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\04_Flight_Examples.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\05_SimConnect_Adapter.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\06_Checklists.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\assets\diagrams\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\assets\examples\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+_ideas\How_RTT_Helps_Planes_Not_Go_Boom\assets\telemetry\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=_snippets
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+_snippets\README.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=_specs
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+_specs\RTT_Kernel_v0.1.md corpus\%seeds%.md
echo ---------------------------------
echo.

set seeds=_template
echo %seeds% >corpus\%seeds%.md
copy corpus\%seeds%.md+_template\overview.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\assets\ReachoutPlan.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\echo\placeholder.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\equations\equations.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\equations\placeholder.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\honor_roll\placeholder.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\honor_roll\project.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\labs\lab-01\README.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\labs\onboarding\placeholder.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\labs\scrolls\placeholder.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\validator\placeholder.md corpus\%seeds%.md
copy corpus\%seeds%.md+_template\validator\resonance-passport-template.md corpus\%seeds%.md
echo ---------------------------------
echo.
:end
