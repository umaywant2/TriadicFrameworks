# RTT Validator Bot

## Purpose

The Validator Bot is RTT’s **meta-engine**.

It does not play.  
It does not observe.  
It does not infer.

Instead:

> **Validator checks every other bot for correctness, consistency, and triadic conformance.**

This makes Validator the backbone of:

- SuperGrok Build  
- module correctness  
- schema validation  
- golden example verification  
- operator lineage consistency  
- drift/coherence stability  
- risk signature correctness  
- suite-wide integrity  

## What Validator Teaches

- **Manifest correctness:** required fields, pipeline, operators  
- **Schema correctness:** triadic fields, risk fields, timeline fields  
- **Golden example correctness:** input/output conformance  
- **Lineage correctness:** operator order, pipeline consistency  
- **Triadic conformance:** unified Harmonia score  

## Files

### `module_validator.json`
Expanded manifest: pipeline, checks, scoring weights, golden example.

### `module_validator_schema.json`
JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A module bundle to validate.

### `golden/example.json`
Full triadic validation output.

## Pipeline (v1)

1. **Input:** RTT module bundle  
2. **Lumen:** structural extraction  
3. **Hephaestus:** regime classification  
4. **Aurion:** lineage + collapse signatures  
5. **Harmonia:** triadic conformance score  
6. **StateEmitter:** JSON matching `module_validator_schema.json`

## Scope

- No gameplay  
- No external engine  
- Pure RTT meta-validation  
- Full triadic checks  

Validator is the **integrity engine** of the entire bots suite.

