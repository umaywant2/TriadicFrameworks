@echo off
echo Creating 1...
cd vst_for_large_language_models/
copy con README.md
copy con substrate_definition.md
copy con latent_trajectory_regimes.md
copy con scaling_behavior_llms.md
copy con projection_and_alignment.md
copy con validation_layers_vst_llm.md
copy con drift_detection_llm.md
md examples
cd examples
copy con example_latent_pathway_1024d.md
copy con example_cross_version_alignment.md
cd..
md appendix
cd appendix
copy con terminology.md
copy con references.md
cd..
cd..
echo Creating 2...
cd vst_for_protein_language_models
copy con README.md
copy con substrate_definition.md
copy con sequence_embedding_regimes.md
copy con dimensional_scaling_protein_models.md
copy con projection_into_structural_cores.md
copy con validation_layers_vst_plm.md
copy con drift_detection_plm.md
md examples
cd examples
copy con example_sequence_regime_transition.md
copy con example_embedding_projection_1024d.md
cd..
md appendix
cd appendix
copy con terminology.md
copy con references.md
cd..
cd..
echo Creating 3...
cd vst_for_scientific_simulators
copy con README.md
copy con substrate_definition.md
copy con simulator_state_regimes.md
copy con scaling_behavior_simulators.md
copy con projection_into_dimensional_cores.md
copy con validation_layers_vst_simulators.md
copy con drift_detection_simulators.md
md examples
cd examples
copy con example_climate_regime_transition.md
copy con example_plasma_state_projection.md
cd..
md appendix
cd appendix
copy con terminology.md
copy con references.md
cd..
cd..
echo Creating 4...
cd vst_for_robotics_and_control_policies
copy con README.md
copy con substrate_definition.md
copy con policy_latent_regimes.md
copy con scaling_behavior_rl_policies.md
copy con projection_and_policy_alignment.md
copy con validation_layers_vst_rl.md
copy con drift_detection_rl.md
md examples
cd examples
copy con example_policy_regime_shift.md
copy con example_control_surface_projection.md
cd..
md appendix
cd appendix
copy con terminology.md
copy con references.md
cd..
cd..
echo Creating 5...
cd vst_for_embedding_stores_vector_databases
copy con README.md
copy con substrate_definition.md
copy con embedding_cluster_regimes.md
copy con scaling_behavior_vector_spaces.md
copy con projection_and_fragmentation_analysis.md
copy con validation_layers_vst_embeddings.md
copy con drift_detection_embeddings.md
md examples
cd examples
copy con example_cluster_regime_transition.md
copy con example_embedding_drift_detection.md
cd..
md appendix
cd appendix
copy con terminology.md
copy con references.md
cd..
cd..
echo Creating 6...
cd vst_for_generative_models
copy con README.md
copy con substrate_definition.md
copy con diffusion_latent_regimes.md
copy con scaling_behavior_generative_models.md
copy con projection_and_latent_alignment.md
copy con validation_layers_vst_generative.md
copy con drift_detection_generative.md
md examples
cd examples
copy con example_diffusion_path_regime.md
copy con example_latent_projection_1024d.md
cd..
md appendix
cd appendix
copy con terminology.md
copy con references.md
cd..
cd..
echo Creating 7...
cd vst_for_multi_model_alignment
copy con README.md
copy con substrate_definition.md
copy con cross_model_regimes.md
copy con scaling_behavior_multi_model.md
copy con projection_and_alignment_surfaces.md
copy con validation_layers_vst_multi_model.md
copy con drift_detection_multi_model.md
md examples
cd examples
copy con example_cross_model_regime_map.md
copy con example_alignment_surface_projection.md
cd..
md appendix
cd appendix
copy con terminology.md
copy con references.md
cd..
cd..
echo Done!