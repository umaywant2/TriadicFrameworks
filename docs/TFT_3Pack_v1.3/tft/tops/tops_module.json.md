Your canonical **TOPS `module.json`** is validated and delivered — the largest schema in the cascade so far. Here's the full structural breakdown:

### Module identity

| Field | Value |
|---|---|
| **canon_tag** | `tops` |
| **parent** | `tft-3pack` |
| **layer** | Core Frameworks — Structural Spine |
| **drift_sensitivity** | medium (elevated from WRSADC's "low" — remix lineage, echo agents, legacy archives introduce drift) |
| **regime_sensitivity** | high (agents, cloud deployment, badge logic all operate under regime constraints) |

### Structural grammar highlights

The schema captures three extensions beyond the base `module.schema.json` contract:

- **Triconceptual modes** — `direct_view.py`, `reflective_view.py`, `inversion_logic.py` mapped as the perception triad with engine references   [raw.githubusercontent.com](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/TFT_3Pack_v1.3/tft/tops/README.md)
- **Resonance clarity** — the full `--basetype` switch taxonomy (common/extended/non-integer/speculative) with the `.fff/.json/.parquet/.txt` output contract   [raw.githubusercontent.com](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/TFT_3Pack_v1.3/tft/tops/QUICKSTART.md)
- **Anatomical metaphor** — agents as *hands*, overlays as *eyes*, AI pipeline as *intelligence*, hardware as *body* — drawn directly from the READMEs   [raw.githubusercontent.com](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/TFT_3Pack_v1.3/tft/tops/agents/README.md)  [raw.githubusercontent.com](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/TFT_3Pack_v1.3/tft/tops/overlays/README.md)  [raw.githubusercontent.com](https://raw.githubusercontent.com/umaywant2/TriadicFrameworks/main/docs/TFT_3Pack_v1.3/tft/tops/hardware/README.md)

### Scale comparison across your three schemas

| Module | Files | Submodules | Roles used | Layers covered | Dependency arcs |
|---|---|---|---|---|---|
| **tft-3pack** (parent) | 34 | 8 | 6 | 4 | 0 |
| **wrsadc** | 10 | 0 | 4 | 3 | 4 |
| **tops** | 85 | 12 | 8 | **6/6 ✅** | 12 |

TOPS is the first module to achieve **full analyzer layer coverage** — all six layers (operator, dimensional, regime, drift, coherence, cross-cutting) are represented, with regime (20 files) and dimensional (16 files) as the heaviest concentrations.

### Dependency graph — key chains

```
protocol-core/main.py → tops_session.py → direct_view.py
                                        → reflective_view.py
                                        → inversion_logic.py

agents/badge_logic_engine.py → agents/tops_agent_interface.py
                              → registry/badge_logic.yaml

ai_pipeline/fff_alignment_predictor.py → folds/fold_001_glycine.yaml
ai_pipeline/model_evaluator.py → ai_pipeline/train_ai_on_resonance.py
ai_pipeline/remix_lineage_dashboard.py → ai_pipeline/remix_lineage_log.yaml
```

---

```
{
  "$schema": "https://www.triadicframeworks.org/schemas/module.schema.json",

  "module": {
    "name": "TOPS",
    "path": "docs/TFT_3Pack_v1.3/tft/tops",
    "canon_tag": "tops",
    "version": "1.3",
    "layer": "Core Frameworks — Structural Spine",
    "status": "Active, Canonical",
    "purpose": "Triconceptual simulation engine exploring perception through direct, reflective, and inversion modes with resonance clarity (--basetype lens switching). Orchestrates agents, AI pipelines, overlays, folds, and hardware targets as a unified operator system.",
    "parent": "tft-3pack",
    "url": "https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/TFT_3Pack_v1.3/tft/tops"
  },

  "session_context": {
    "canon": "active (tops ⊂ tft-3pack)",
    "modules_linked": [
      "direct_view.py ↔ reflective_view.py ↔ inversion_logic.py — triconceptual perception triad",
      "tops_session.py → glyph_compare.py → grid_ops.py — session orchestration pipeline",
      "agents/ → overlays/ → ai_pipeline/ — hands → eyes → intelligence of tops",
      "folds/ → ai_pipeline/ → overlays/ — bio-resonance data → prediction → visualization",
      "protocol-core/ → agents/ — protocol execution → agent orchestration",
      "hardware/nimms/ ↔ cloud/azure/ — physical ↔ cloud deployment targets",
      "registry/ → agents/ — badge/glyph state → agent behavior"
    ],
    "drift": "medium (remix lineage tracking, echo/drift agents, legacy archives)",
    "coherence": "stable (triconceptual grammar + .fff/.json/.parquet/.txt output contract)",
    "format": "python + shell + markdown + yaml + json + csv + svg + png + pdf",
    "front_door": "exists (tft/tops/README.md + QUICKSTART.md)",
    "every_page": "stands alone + student-ready + operator-aware + basetype-tagged",
    "audience": ["students", "educators", "developers", "researchers", "AIs"]
  },

  "structural_grammar": {
    "dimensional_envelope": "D3–D9",
    "regime_envelope": "R1–R2",
    "coherence_envelope": "C1–C3",
    "drift_sensitivity": "medium",
    "regime_sensitivity": "high",
    "triconceptual_modes": {
      "direct": {
        "label": "Direct View",
        "engine": "direct_view.py",
        "purpose": "Raw perception — unmediated observation of resonance geometry"
      },
      "reflective": {
        "label": "Reflective View",
        "engine": "reflective_view.py",
        "purpose": "Mirrored perception — symmetry and self-reference in resonance patterns"
      },
      "inversion": {
        "label": "Inversion Logic",
        "engine": "inversion_logic.py",
        "purpose": "Inverted perception — negation, complement, and boundary logic"
      }
    },
    "resonance_clarity": {
      "switch": "--basetype / -b",
      "base_categories": {
        "common": ["binary", "decimal", "hex", "octal", "sexagesimal"],
        "extended": ["negabinary", "negadecimal"],
        "non_integer": ["phi", "pi", "sqrt2", "e"],
        "speculative": ["corridor6.9", "vigquinary20.5", "triadic3phi"]
      },
      "output_contract": [".fff", ".json", ".parquet", ".txt"],
      "metadata_key": "BaseLens"
    },
    "anatomical_metaphor": {
      "hands": "agents/ — orchestrate resonance flows, trigger overlays, extend into distributed contexts",
      "eyes": "overlays/ — make resonance visible, traceable, and remixable",
      "intelligence": "ai_pipeline/ — trains, predicts, and visualizes resonance alignments",
      "body": "hardware/ — grounds orchestration in physical systems"
    }
  },

  "cross_module_propagation": {
    "imports": [
      "tft-3pack (parent module — dimensional envelope, audience, canon context)",
      "rtt-core (resonance-aware structural grammar)",
      "nous (runtime environment for launching pipelines)",
      "entft (protocol layer orchestrated by Thor)"
    ],
    "exports": [
      "triconceptual simulation engine (direct + reflective + inversion)",
      "resonance clarity (--basetype lens switching across all modes)",
      "glyph comparison outputs (.fff, .json, .parquet, .txt)",
      "agent orchestration framework (badge, glyph, scroll, flame agents)",
      "AI resonance pipeline (training, prediction, lineage)",
      "fold bio-resonance registry (protein resonance mappings)",
      "overlay visualization system (dashboards, warp chambers, symbolic maps)",
      "NIMMS hardware target specifications",
      "Azure cloud deployment templates",
      "benchmark results (vs THOR baseline)"
    ]
  },

  "submodules": [
    {
      "name": "Agents",
      "path": "agents/",
      "file_count": 11,
      "role": "engine",
      "purpose": "Thor-specific agents orchestrating resonance, overlays, and integrations — the 'hands' of tops.",
      "manifest": null
    },
    {
      "name": "AI Pipeline",
      "path": "ai_pipeline/",
      "file_count": 22,
      "role": "engine",
      "purpose": "Intelligence layer — trains, predicts, and visualizes resonance alignments across glyphs, folds, and remix lineage.",
      "manifest": null
    },
    {
      "name": "Cloud — Azure",
      "path": "cloud/azure/",
      "file_count": 5,
      "role": "template",
      "purpose": "Azure deployment templates, autoscale configs, and cloud initialization for distributed tops execution.",
      "manifest": null
    },
    {
      "name": "Contributors",
      "path": "contributors/",
      "file_count": 1,
      "role": "reference",
      "purpose": "Contributor guidelines and recognition structure.",
      "manifest": null
    },
    {
      "name": "Figures",
      "path": "figures/",
      "file_count": 4,
      "role": "map",
      "purpose": "Visual assets — badge lineage charts, glyphstream overlays, and resonance maps.",
      "manifest": null
    },
    {
      "name": "Folds",
      "path": "folds/",
      "file_count": 3,
      "role": "profile",
      "purpose": "Bio-resonance registry — protein structures with resonance signatures, dimensional alignments, and glyph overlays.",
      "manifest": null
    },
    {
      "name": "Hardware — NIMMS",
      "path": "hardware/nimms/",
      "file_count": 11,
      "role": "profile",
      "purpose": "NIMMS DPU design notes, crystal blade arrays, quantum drive schematics, and boot glyph configs — the 'body' of tops.",
      "manifest": null
    },
    {
      "name": "Outreach",
      "path": "outreach/",
      "file_count": 7,
      "role": "reference",
      "purpose": "Grant applications, partnership drafts, pitch materials, funding plans, and Resotectors summary.",
      "manifest": null
    },
    {
      "name": "Overlays",
      "path": "overlays/",
      "file_count": 4,
      "role": "map",
      "purpose": "Dashboards, symbolic overlays, and warp chamber designs — the 'eyes' of tops.",
      "manifest": null
    },
    {
      "name": "Protocol Core",
      "path": "protocol-core/",
      "file_count": 2,
      "role": "engine",
      "purpose": "Core protocol execution — gearshift 3-6-9 logic and main entry point.",
      "manifest": null
    },
    {
      "name": "Registry",
      "path": "registry/",
      "file_count": 2,
      "role": "profile",
      "purpose": "Badge logic definitions and glyph state registry.",
      "manifest": null
    },
    {
      "name": "Results",
      "path": "results/",
      "file_count": 1,
      "role": "signature",
      "purpose": "Benchmark outputs and comparison baselines (vs THOR).",
      "manifest": null
    }
  ],

  "files": [

    {
      "filename": "README.md",
      "path": "README.md",
      "purpose": "Module front door — triconceptual overview, resonance clarity introduction, base-type examples, and cross-links to related scrolls.",
      "role": "index"
    },
    {
      "filename": "QUICKSTART.md",
      "path": "QUICKSTART.md",
      "purpose": "Step-by-step quickstart — run sessions, save outputs, compare glyphs, and select base lenses.",
      "role": "reference",
      "analyzer_layer": "operator"
    },
    {
      "filename": "direct_view.py",
      "path": "direct_view.py",
      "purpose": "Direct perception mode — unmediated observation of resonance geometry with --basetype lens switching.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "reflective_view.py",
      "path": "reflective_view.py",
      "purpose": "Reflective perception mode — symmetry and self-reference in resonance patterns with --basetype lens switching.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "inversion_logic.py",
      "path": "inversion_logic.py",
      "purpose": "Inversion perception mode — negation, complement, and boundary logic with --basetype lens switching.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "tops_session.py",
      "path": "tops_session.py",
      "purpose": "Session orchestrator — launches triconceptual simulations in specified mode and base lens, routes outputs via output_manager.",
      "role": "engine",
      "analyzer_layer": "operator",
      "depends_on": ["direct_view.py", "reflective_view.py", "inversion_logic.py"]
    },
    {
      "filename": "glyph_compare.py",
      "path": "glyph_compare.py",
      "purpose": "Cross-mode glyph comparison — visualizes differences across base lenses, producing symbolic overlays (SVG/PNG).",
      "role": "engine",
      "analyzer_layer": "cross-cutting"
    },
    {
      "filename": "grid_ops.py",
      "path": "grid_ops.py",
      "purpose": "Grid operations with base-lens fidelity — dimensional alignment and validator logic for grid overlays.",
      "role": "engine",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "echo_overlay_manifesto.md",
      "path": "echo_overlay_manifesto.md",
      "purpose": "Design manifesto defining the echo overlay philosophy — symbolic persistence, glyph lifecycle, and resonance echo principles.",
      "role": "reference",
      "analyzer_layer": "regime"
    },
    {
      "filename": "tops_Benchmark_Outline.md",
      "path": "tops_Benchmark_Outline.md",
      "purpose": "Benchmark specification outlining test dimensions, success criteria, and comparison methodology (vs THOR baseline).",
      "role": "reference",
      "analyzer_layer": "coherence"
    },
    {
      "filename": "tops_reflect_invert_sim.md",
      "path": "tops_reflect_invert_sim.md",
      "purpose": "Simulation specification for combined reflection-inversion mode — operator pairing rationale and expected output patterns.",
      "role": "reference",
      "analyzer_layer": "operator"
    },
    {
      "filename": "TriadicTestSuite.md",
      "path": "TriadicTestSuite.md",
      "purpose": "Test suite specification — validates triconceptual mode outputs, base-lens consistency, and output format compliance.",
      "role": "diagnostic",
      "analyzer_layer": "coherence"
    },


    {
      "filename": "README.md",
      "path": "agents/README.md",
      "purpose": "Agents overview — resonance clarity coordination, structure (resonance/overlay/integration agents), invocation patterns.",
      "role": "index"
    },
    {
      "filename": "README_tops_agent.md",
      "path": "agents/README_tops_agent.md",
      "purpose": "Detailed agent architecture spec — interface contracts, lifecycle, and agent-to-agent communication patterns.",
      "role": "reference",
      "analyzer_layer": "regime"
    },
    {
      "filename": "tops_agent_interface.py",
      "path": "agents/tops_agent_interface.py",
      "purpose": "Base agent interface — defines the contract all tops agents implement (init, execute, report, teardown).",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "badge_logic_engine.py",
      "path": "agents/badge_logic_engine.py",
      "purpose": "Badge logic agent — evaluates contributor actions against badge criteria from registry and assigns earned badges.",
      "role": "engine",
      "analyzer_layer": "regime",
      "depends_on": ["agents/tops_agent_interface.py", "registry/badge_logic.yaml"]
    },
    {
      "filename": "flame_echo_trigger.py",
      "path": "agents/flame_echo_trigger.py",
      "purpose": "Flame echo agent — detects resonance echo conditions and triggers symbolic persistence events.",
      "role": "engine",
      "analyzer_layer": "drift"
    },
    {
      "filename": "glyph_fusion_resolver.py",
      "path": "agents/glyph_fusion_resolver.py",
      "purpose": "Glyph fusion agent — resolves conflicts when multiple glyphs overlap and produces fused symbolic outputs.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "glyph_reawakening_monitor.py",
      "path": "agents/glyph_reawakening_monitor.py",
      "purpose": "Glyph reawakening agent — monitors retired glyphs for conditions warranting reactivation.",
      "role": "engine",
      "analyzer_layer": "drift"
    },
    {
      "filename": "glyph_registry_loader.py",
      "path": "agents/glyph_registry_loader.py",
      "purpose": "Registry loader agent — reads glyph and badge registries into runtime state for agent consumption.",
      "role": "engine",
      "analyzer_layer": "regime",
      "depends_on": ["registry/badge_logic.yaml"]
    },
    {
      "filename": "glyph_retirement_trigger.py",
      "path": "agents/glyph_retirement_trigger.py",
      "purpose": "Glyph retirement agent — evaluates end-of-life criteria and triggers glyph archival/retirement.",
      "role": "engine",
      "analyzer_layer": "drift"
    },
    {
      "filename": "scroll_commit_monitor.py",
      "path": "agents/scroll_commit_monitor.py",
      "purpose": "Scroll commit agent — monitors scroll (document) commits for structural coherence and triggers validation.",
      "role": "engine",
      "analyzer_layer": "coherence"
    },
    {
      "filename": "scroll_runtime_trace_dashboard.py",
      "path": "agents/scroll_runtime_trace_dashboard.py",
      "purpose": "Runtime trace dashboard — cross-cutting visualization of agent actions, scroll commits, and resonance state.",
      "role": "engine",
      "analyzer_layer": "cross-cutting"
    },


    {
      "filename": "README.md",
      "path": "ai_pipeline/README.md",
      "purpose": "AI Pipeline overview — structure (core scripts, lineage + remix, data manifests), usage workflow, cross-links.",
      "role": "index"
    },
    {
      "filename": "ai_training_manifesto.md",
      "path": "ai_pipeline/ai_training_manifesto.md",
      "purpose": "Training manifesto — principles, ethics, and methodology for training AI models on resonance datasets.",
      "role": "reference",
      "analyzer_layer": "regime"
    },
    {
      "filename": "fff_alignment_predictor.py",
      "path": "ai_pipeline/fff_alignment_predictor.py",
      "purpose": "Resonance alignment predictor — predicts harmonic alignment across glyphs and folds from .fff input data.",
      "role": "engine",
      "analyzer_layer": "dimensional",
      "depends_on": ["folds/fold_001_glycine.yaml"]
    },
    {
      "filename": "train_ai_on_resonance.py",
      "path": "ai_pipeline/train_ai_on_resonance.py",
      "purpose": "Model trainer — trains resonance prediction models on structured datasets (CSV input).",
      "role": "engine",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "model_evaluator.py",
      "path": "ai_pipeline/model_evaluator.py",
      "purpose": "Model evaluator — measures accuracy and harmonic coherence of trained resonance prediction models.",
      "role": "diagnostic",
      "analyzer_layer": "coherence",
      "depends_on": ["ai_pipeline/train_ai_on_resonance.py"]
    },
    {
      "filename": "glyph_overlay_animator.py",
      "path": "ai_pipeline/glyph_overlay_animator.py",
      "purpose": "Glyph overlay animator — generates symbolic visualizations from fold-glyph manifest data.",
      "role": "engine",
      "analyzer_layer": "cross-cutting",
      "depends_on": ["ai_pipeline/fold_glyph_manifest.yaml"]
    },
    {
      "filename": "contributor_badge_generator.py",
      "path": "ai_pipeline/contributor_badge_generator.py",
      "purpose": "Badge generator — creates contributor badges based on remix lineage and contribution patterns.",
      "role": "engine",
      "analyzer_layer": "regime",
      "depends_on": ["ai_pipeline/contributor_badge_log.yaml"]
    },
    {
      "filename": "contributor_badge_log.yaml",
      "path": "ai_pipeline/contributor_badge_log.yaml",
      "purpose": "Badge log — historical record of contributor badge assignments and badge state transitions.",
      "role": "profile",
      "analyzer_layer": "regime"
    },
    {
      "filename": "contributor_echo_log.yaml",
      "path": "ai_pipeline/contributor_echo_log.yaml",
      "purpose": "Echo log — records contributor echo events (resonance propagation through remix lineage).",
      "role": "profile",
      "analyzer_layer": "drift"
    },
    {
      "filename": "contributor_echo_map.py",
      "path": "ai_pipeline/contributor_echo_map.py",
      "purpose": "Echo mapper — visualizes contributor echo propagation patterns across remix lineage.",
      "role": "engine",
      "analyzer_layer": "drift",
      "depends_on": ["ai_pipeline/contributor_echo_log.yaml"]
    },
    {
      "filename": "fold_glyph_generator.py",
      "path": "ai_pipeline/fold_glyph_generator.py",
      "purpose": "Fold-glyph generator — converts protein fold data into glyph overlay specifications.",
      "role": "engine",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "fold_glyph_manifest.yaml",
      "path": "ai_pipeline/fold_glyph_manifest.yaml",
      "purpose": "Fold-glyph manifest — maps fold identifiers to their corresponding glyph overlays and resonance signatures.",
      "role": "profile",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "fold_glyph_overlay.svg",
      "path": "ai_pipeline/fold_glyph_overlay.svg",
      "purpose": "Generated SVG visualization of fold-glyph resonance overlays.",
      "role": "map",
      "analyzer_layer": "cross-cutting"
    },
    {
      "filename": "glyph_overlay_manifest.csv",
      "path": "ai_pipeline/glyph_overlay_manifest.csv",
      "purpose": "Tabular manifest of all glyph overlays with coordinates, resonance values, and base-lens metadata.",
      "role": "profile",
      "analyzer_layer": "cross-cutting"
    },
    {
      "filename": "legacy_echo_archive.md",
      "path": "ai_pipeline/legacy_echo_archive.md",
      "purpose": "Archive of historical echo events from earlier framework versions — preserves resonance lineage.",
      "role": "reference",
      "analyzer_layer": "drift"
    },
    {
      "filename": "legacy_echo_index.csv",
      "path": "ai_pipeline/legacy_echo_index.csv",
      "purpose": "Tabular index into legacy echo archive — enables lookup by echo ID, timestamp, and originating module.",
      "role": "profile",
      "analyzer_layer": "drift"
    },
    {
      "filename": "legacy_echo_visualizer.py",
      "path": "ai_pipeline/legacy_echo_visualizer.py",
      "purpose": "Legacy echo visualizer — renders historical echo patterns for comparison with current resonance state.",
      "role": "engine",
      "analyzer_layer": "drift",
      "depends_on": ["ai_pipeline/legacy_echo_index.csv"]
    },
    {
      "filename": "mythic_badge_manifest.yaml",
      "path": "ai_pipeline/mythic_badge_manifest.yaml",
      "purpose": "Mythic badge manifest — defines special-tier badge criteria for exceptional contributor milestones.",
      "role": "profile",
      "analyzer_layer": "regime"
    },
    {
      "filename": "remix_lineage_dashboard.py",
      "path": "ai_pipeline/remix_lineage_dashboard.py",
      "purpose": "Remix lineage dashboard — cross-cutting visualization of remix chains, contributor badges, and echo propagation.",
      "role": "engine",
      "analyzer_layer": "cross-cutting",
      "depends_on": ["ai_pipeline/remix_lineage_log.yaml"]
    },
    {
      "filename": "remix_lineage_log.yaml",
      "path": "ai_pipeline/remix_lineage_log.yaml",
      "purpose": "Remix lineage log — records each remix event with parent/child references, contributor IDs, and timestamps.",
      "role": "profile",
      "analyzer_layer": "drift"
    },
    {
      "filename": "remix_lineage_tracker.py",
      "path": "ai_pipeline/remix_lineage_tracker.py",
      "purpose": "Remix lineage tracker — appends new remix events to the lineage log and validates parent chain integrity.",
      "role": "engine",
      "analyzer_layer": "drift",
      "depends_on": ["ai_pipeline/remix_lineage_log.yaml"]
    },
    {
      "filename": "remix_trigger_predictor.py",
      "path": "ai_pipeline/remix_trigger_predictor.py",
      "purpose": "Remix trigger predictor — anticipates upcoming remix events based on lineage patterns and contributor activity.",
      "role": "engine",
      "analyzer_layer": "drift"
    },


    {
      "filename": "README.md",
      "path": "cloud/azure/README.md",
      "purpose": "Azure deployment overview — prerequisites, deployment steps, and integration with tops agents.",
      "role": "index"
    },
    {
      "filename": "Azure_Deployment_Guide.md",
      "path": "cloud/azure/Azure_Deployment_Guide.md",
      "purpose": "Full deployment guide — step-by-step Azure setup, resource provisioning, and scaling configuration.",
      "role": "reference",
      "analyzer_layer": "regime"
    },
    {
      "filename": "azure_deploy.yaml",
      "path": "cloud/azure/azure_deploy.yaml",
      "purpose": "Azure deployment manifest — defines container images, networking, and resource allocation.",
      "role": "template",
      "analyzer_layer": "regime"
    },
    {
      "filename": "autoscale_config.json",
      "path": "cloud/azure/autoscale_config.json",
      "purpose": "Autoscale configuration — defines scaling triggers, min/max instances, and cooldown periods.",
      "role": "template",
      "analyzer_layer": "regime"
    },
    {
      "filename": "cloud_init.sh",
      "path": "cloud/azure/cloud_init.sh",
      "purpose": "Cloud initialization script — bootstraps Azure VM instances with tops dependencies and runtime config.",
      "role": "engine",
      "analyzer_layer": "regime"
    },


    {
      "filename": "README.md",
      "path": "contributors/README.md",
      "purpose": "Contributor guidelines — contribution workflow, badge eligibility, and code of conduct.",
      "role": "index"
    },


    {
      "filename": "figure_captions.md",
      "path": "figures/figure_captions.md",
      "purpose": "Caption metadata for all figure assets — maps filenames to descriptive titles and context references.",
      "role": "reference",
      "analyzer_layer": "cross-cutting"
    },
    {
      "filename": "badge_lineage_chart.png",
      "path": "figures/badge_lineage_chart.png",
      "purpose": "Visual chart showing badge lineage and inheritance across contributor generations.",
      "role": "map",
      "analyzer_layer": "cross-cutting"
    },
    {
      "filename": "glyphstream_overlay.png",
      "path": "figures/glyphstream_overlay.png",
      "purpose": "Symbolic overlay visualization of glyph stream flow across resonance dimensions.",
      "role": "map",
      "analyzer_layer": "cross-cutting"
    },
    {
      "filename": "resonance_map.png",
      "path": "figures/resonance_map.png",
      "purpose": "Resonance map visualization showing dimensional alignment across modes and base lenses.",
      "role": "map",
      "analyzer_layer": "cross-cutting"
    },


    {
      "filename": "README.md",
      "path": "folds/README.md",
      "purpose": "Folds overview — bio-resonance registry structure, fields (PDB, signature, alignment, glyphs, lineage), cross-links.",
      "role": "index"
    },
    {
      "filename": "fold_001_glycine.yaml",
      "path": "folds/fold_001_glycine.yaml",
      "purpose": "Glycine protein fold — PDB source, resonance signature, Forci/Flui/Freqi dimensional alignment, glyph overlays.",
      "role": "profile",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "fold_002_custom_ai_remix.yaml",
      "path": "folds/fold_002_custom_ai_remix.yaml",
      "purpose": "Custom AI remix fold — AI-generated resonance profile with remix lineage and contributor badge references.",
      "role": "profile",
      "analyzer_layer": "dimensional"
    },


    {
      "filename": "README.md",
      "path": "hardware/README.md",
      "purpose": "Hardware overview — DPU scaffolding, integration specs, future roadmap for physical deployment.",
      "role": "index"
    },
    {
      "filename": "NIMMS_v2.0.md",
      "path": "hardware/nimms/NIMMS_v2.0.md",
      "purpose": "NIMMS v2.0 specification — full architecture for Nonagon Integrated Micro-Module System.",
      "role": "reference",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "NIMMS_nano.md",
      "path": "hardware/nimms/NIMMS_nano.md",
      "purpose": "NIMMS Nano specification — compact variant for embedded and edge deployment targets.",
      "role": "reference",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "crystal_blade_array.md",
      "path": "hardware/nimms/crystal_blade_array.md",
      "purpose": "Crystal blade array design — resonance-aligned processing element geometry and interconnect topology.",
      "role": "reference",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "nonagon_crystal_shell.md",
      "path": "hardware/nimms/nonagon_crystal_shell.md",
      "purpose": "Nonagon crystal shell design — outer enclosure geometry aligning with 9-fold resonance symmetry.",
      "role": "reference",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "sqd_schematic_overview.md",
      "path": "hardware/nimms/sqd_schematic_overview.md",
      "purpose": "SQD (Starship Quantum Drive) schematic overview — high-level architecture for quantum resonance processing.",
      "role": "reference",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "starship_quantum_drive.md",
      "path": "hardware/nimms/starship_quantum_drive.md",
      "purpose": "Starship Quantum Drive detailed spec — quantum processing elements, resonance cache integration, and drive protocols.",
      "role": "reference",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "boot_glyphs.yaml",
      "path": "hardware/nimms/boot_glyphs.yaml",
      "purpose": "Boot glyph configuration — initial glyph set loaded during NIMMS hardware initialization sequence.",
      "role": "template",
      "analyzer_layer": "regime"
    },
    {
      "filename": "glyph_interrupts.py",
      "path": "hardware/nimms/glyph_interrupts.py",
      "purpose": "Glyph interrupt handler — maps hardware interrupt signals to glyph state transitions in the resonance cache.",
      "role": "engine",
      "analyzer_layer": "operator"
    },
    {
      "filename": "resonance_cache.json",
      "path": "hardware/nimms/resonance_cache.json",
      "purpose": "Resonance cache state — current glyph/fold resonance values held in hardware-local fast storage.",
      "role": "profile",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "echo_log.md",
      "path": "hardware/nimms/echo_log.md",
      "purpose": "Hardware echo log — records resonance echo events at the NIMMS hardware level for diagnostic review.",
      "role": "reference",
      "analyzer_layer": "drift"
    },


    {
      "filename": "README.md",
      "path": "outreach/README.md",
      "purpose": "Outreach overview — partnership strategy, grant targets, and communication templates.",
      "role": "index"
    },
    {
      "filename": "azure_grant_email.md",
      "path": "outreach/azure_grant_email.md",
      "purpose": "Azure grant application email draft — requesting cloud compute credits for tops deployment and research.",
      "role": "reference",
      "analyzer_layer": "regime"
    },
    {
      "filename": "email_draft_to_innatera.md",
      "path": "outreach/email_draft_to_innatera.md",
      "purpose": "Partnership email draft to Innatera — proposing neuromorphic hardware collaboration for NIMMS.",
      "role": "reference",
      "analyzer_layer": "regime"
    },
    {
      "filename": "funding_plan.md",
      "path": "outreach/funding_plan.md",
      "purpose": "Funding plan — budget projections, milestone targets, and revenue/grant strategy for tops development.",
      "role": "reference",
      "analyzer_layer": "regime"
    },
    {
      "filename": "pitch_deck_outline.md",
      "path": "outreach/pitch_deck_outline.md",
      "purpose": "Pitch deck outline — slide-by-slide structure for investor/partner presentations on TriadicFrameworks.",
      "role": "reference",
      "analyzer_layer": "regime"
    },
    {
      "filename": "pitch_deck.pdf",
      "path": "outreach/pitch_deck.pdf",
      "purpose": "Compiled pitch deck — visual presentation for external stakeholders and funding applications.",
      "role": "reference",
      "analyzer_layer": "regime"
    },
    {
      "filename": "Resotectors_Summary.md",
      "path": "outreach/Resotectors_Summary.md",
      "purpose": "Resotectors project summary — overview of resonance-based protection and detection framework capabilities.",
      "role": "reference",
      "analyzer_layer": "regime"
    },


    {
      "filename": "README.md",
      "path": "overlays/README.md",
      "purpose": "Overlays overview — structure (dashboards, symbolic overlays, warp chambers), resonance clarity integration, code scaffolding.",
      "role": "index"
    },
    {
      "filename": "FFF_Warp_Protocol.md",
      "path": "overlays/FFF_Warp_Protocol.md",
      "purpose": "FFF Warp Protocol specification — defines how .fff files are transformed through warp chamber overlays.",
      "role": "reference",
      "analyzer_layer": "dimensional"
    },
    {
      "filename": "symbolic_architecture_overlays.md",
      "path": "overlays/symbolic_architecture_overlays.md",
      "purpose": "Symbolic architecture overlay spec — glyph placement rules, resonance map layering, and visual grammar.",
      "role": "reference",
      "analyzer_layer": "cross-cutting"
    },
    {
      "filename": "warp_chamber_design.md",
      "path": "overlays/warp_chamber_design.md",
      "purpose": "Warp chamber design — experimental visualization scaffold for multi-dimensional resonance field rendering.",
      "role": "reference",
      "analyzer_layer": "dimensional"
    },


    {
      "filename": "main.py",
      "path": "protocol-core/main.py",
      "purpose": "Protocol core entry point — initializes runtime, loads configuration, and dispatches to simulation modes.",
      "role": "engine",
      "analyzer_layer": "operator",
      "depends_on": ["tops_session.py"]
    },
    {
      "filename": "gearshift_369.py",
      "path": "protocol-core/gearshift_369.py",
      "purpose": "Gearshift 3-6-9 engine — implements the triadic gearshift protocol for dimensional phase transitions (D3→D6→D9).",
      "role": "engine",
      "analyzer_layer": "operator"
    },


    {
      "filename": "README.md",
      "path": "registry/README.md",
      "purpose": "Registry overview — badge logic schema, glyph state definitions, and registry update procedures.",
      "role": "index"
    },
    {
      "filename": "badge_logic.yaml",
      "path": "registry/badge_logic.yaml",
      "purpose": "Badge logic definitions — criteria, thresholds, and state transitions for contributor badge assignment.",
      "role": "profile",
      "analyzer_layer": "regime"
    },


    {
      "filename": "benchmark_vs_THOR.csv",
      "path": "results/benchmark_vs_THOR.csv",
      "purpose": "Benchmark results — quantitative comparison of tops simulation outputs against THOR baseline metrics.",
      "role": "signature",
      "analyzer_layer": "coherence"
    }
  ]
}
```
