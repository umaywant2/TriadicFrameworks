# RTT Session Bot

## Purpose

The Session Bot is RTT’s **conversation engine**.

It does not play a game.  
It does not evaluate a board.  
It does not run an external engine.

Instead:

> **Session watches dialogue and emits triadic identity across time.**

This makes it the RTT engine for:

- coherence  
- drift  
- regime shifts  
- collapse signatures  
- projection-loss  
- semantic continuity  
- emotional resonance  
- long-arc identity of a conversation  

## What Session Teaches

- **Regime:** local (message-level), structural (topic-level), continuity (session-level)  
- **Drift:** direction + strength of semantic/emotional flow  
- **Collapse:** sudden topic or intent failure  
- **Projection-loss:** inversion of long-term conversational identity  
- **Ancestry:** lineage of topics and intents  
- **Triadic identity:** unified Harmonia score for the entire session  

## Files

### `module_session.json`
Expanded manifest: pipeline, operators, overlays, scoring weights, golden example.

### `module_session_schema.json`
JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A short conversation.

### `golden/example.json`
Full triadic state for that conversation.

## Pipeline (v1)

1. **Input:** sequence of messages  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** collapse + projection-loss  
5. **Harmonia:** triadic identity  
6. **StateEmitter:** JSON matching `module_session_schema.json`

## Scope

- No gameplay  
- No external engine  
- Pure RTT conversation identity  
- Full triadic overlays  

Session is the **coherence backbone** of the entire bots suite.
