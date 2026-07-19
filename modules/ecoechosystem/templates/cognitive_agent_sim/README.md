# Cognitive agent simulation template README

Welcome to the **Cognitive Agent Simulation** template set. This directory is where EcoEchoSystem stops being “a world that runs” and becomes “a world that notices.”

City, civilization, and planetary layers describe **external dynamics**: resources, governance, interactions, regimes, collapse, renewal. The cognitive agent layer describes **internal dynamics**: perception, memory, belief, motivation, coordination, and choice—bounded by time, attention, and legitimacy.

An agent here is not a personality. It’s a **constraint‑shaped decision process**.

---

## Purpose

This template set exists to:

- **define agent architecture** compatible with EcoEchoSystem’s substrate-first design
- **standardize cognition primitives** for humans, institutions, and hybrid entities
- **support multi-agent simulation** with bounded rationality and social influence
- **enable AI-assisted exploration** without turning agents into oracles
- **preserve S/E/R coherence** inside minds, not just societies

---

## What belongs in this folder

This directory contains templates for modeling cognition as a system:

- **agent loops** (perceive → interpret → decide → act → learn)
- **memory systems** (short, long, institutional, cultural)
- **belief and narrative dynamics** (legitimacy, ideology, identity)
- **attention and salience** (what gets noticed vs ignored)
- **motivation and utility proxies** (needs, values, status, safety)
- **coordination and trust** (networks, reputation, signaling)
- **conflict and persuasion** (propaganda, misinformation, polarization)
- **time-bounded learning** (habituation, trauma, forgetting, drift)

If a mechanism changes *how agents choose*, it belongs here.

---

## Substrate alignment for cognition

Cognitive models must remain compatible with the EcoEchoSystem substrate:

- **Structure (S):** internal representations, social graphs, roles, institutional scaffolds  
- **Activation (E):** stress, urgency, arousal, persuasion intensity, conflict load  
- **Relational time (R):** attention cycles, memory half-life, learning lag, generational transmission  

Cognition is where **activation meets meaning**.

---

## Agent classes

Use these classes as defaults (extend as needed):

- **Individual agents:** bounded attention, personal memory, local incentives
- **Group agents:** coalitions, factions, movements, identity clusters
- **Institution agents:** bureaucracies, courts, markets, churches, guilds
- **Hybrid agents:** AI-augmented institutions, cybernetic governance, collective intelligence systems

The key distinction is not “human vs AI,” but **where memory lives and how decisions propagate**.

---

## Recommended file map

This README is the entry point. Typical companion templates in this folder include:

- **agent_loop.md:** canonical cognition loop and update rules
- **memory_models.md:** layered memory, decay, rehearsal, institutional persistence
- **belief_narrative_dynamics.md:** legitimacy, ideology, identity, myth engines
- **attention_salience.md:** salience competition, agenda setting, perception filters
- **social_influence_networks.md:** trust graphs, reputation, diffusion, polarization
- **coordination_protocols.md:** norms, contracts, enforcement, cooperation failure modes
- **agent_metrics.md:** observables, instrumentation hooks, diagnostics

If your repo already has different filenames, treat this list as a semantic checklist.

---

## How this connects to other templates

The cognitive agent layer is the coupling tissue between:

- **city simulation:** micro choices → emergent urban behavior
- **civilization simulation:** legitimacy + coordination → regime stability or transition
- **cross-civilization interaction:** diffusion, rivalry, imitation, propaganda
- **planetary simulation:** collective action thresholds, coordination emergence
- **AI-driven exploration:** agents as test subjects, not narrators

Put simply:

> Cities and civilizations don’t “decide.” Agents decide.  
> Regimes are what decisions look like when aggregated over time.

---

## Guardrails

Cognitive agent simulation must avoid these failure modes:

- **omniscient agents:** nobody has the full map
- **perfect rationality:** bounded attention and social bias are primary drivers
- **single-utility collapse:** humans and institutions optimize across competing motives
- **narrative override:** stories explain behavior, but do not replace constraints
- **deterministic outcomes:** path dependence is real; inevitability claims are out-of-scope

Agents are **fallible by design**.

---

## Minimal “hello world” run

A minimal cognitive-agent-enabled run should demonstrate:

- **perception limits:** agents miss signals under load
- **belief drift:** narratives shift with stress and influence
- **coordination thresholds:** cooperation fails/succeeds based on trust and legitimacy
- **feedback coupling:** agent choices shift city/civ metrics, which reshape agent state

If your run doesn’t show feedback, you don’t have cognition yet—you have scripted actors.

---

## Status

Canonical template README for cognitive agent simulation. Designed to be forked, extended, and used as the onboarding gateway for agent-based cognition in EcoEchoSystem.
