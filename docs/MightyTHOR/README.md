# MightyTHOR
![mightythor-hammer-icon](../images/mightythor-hammer-icon.png)

The **MightyTHOR** package is the orchestration layer of the TFT 3‑Pack.  
- The TFT 3Pact coordinates agents, overlays, and integrations that extend TFTincryption inside the agent‑shell.

## Structure
- **protocol-core/** → Thor runtime specs and overlays
- **agents/** → MightyTHOR‑specific agents and interfaces
- **overlays/** → UI dashboards, symbolic overlays, warp chamber designs
- **registry/** → Thor registries and badge logic
- **hardware/** → DPU scaffolding and future hardware integrations
- **outreach/** → grant proposals, outreach scrolls
- **cloud/azure/** → Azure integrations and cloud overlays
- **ai_pipeline/** → AI Resonance Pipeline (predictive orchestration + MMR integration)
- **folds/** → protein resonance + symbolic overlays
- **contributors/** → honor rolls and configs

## Purpose
MightyTHOR orchestrates TFTincryption inside the [agent‑shell](../agent_shell/).  
It extends into cloud and hardware environments, and provides dashboards and overlays for developers.

## Cross‑links
- [TFTincryption](../TFTincryption/) → protocol layer orchestrated by Thor
- [folds](folds/) → bio‑resonance data consumed by Thor agents and AI pipeline
- [agent‑shell](../agent_shell/) → runtime environment for Thor agents
