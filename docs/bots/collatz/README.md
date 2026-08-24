# RTT Collatz Bot

## Purpose

The Collatz Bot is RTT’s **pure ancestry module**.

It has:

- no board  
- no engine  
- no hidden state  
- no randomness  

Just a deterministic sequence on ℤ:

> **n → f(n) → f(f(n)) → … → 1**

This makes Collatz the cleanest possible demonstration of:

- lineage  
- collapse  
- projection-loss  
- continuity  
- drift  
- regime shifts  

## What Collatz Teaches

- **Ancestry:** every step has a lineage (odd → 3n+1, even → n/2).  
- **Collapse:** magnitude collapses toward 1.  
- **Projection-loss:** certain steps destroy long-term continuity.  
- **Drift:** numeric drift is monotonic after a point.  
- **Regime:** local (parity), structural (step type), continuity (trajectory).  
- **Triadic identity:** the entire trajectory has a unified score.

## Files

### `module_collatz.json`
Canonical manifest: pipeline, operators, golden example.

### `module_collatz_schema.json`
JSON Schema for the StateEmitter output.

### `golden/example_input.txt`
A single integer (e.g., 27).

### `golden/example.json`
The full triadic state for that trajectory.

## Pipeline (v1)

1. **Input:** integer n  
2. **Lumen:** parity, magnitude, step type  
3. **Hephaestus:** regime per step  
4. **Aurion:** collapse signatures + projection-loss  
5. **Harmonia:** triadic identity for the entire trajectory  
6. **StateEmitter:** JSON matching `module_collatz_schema.json`

## Scope

- No gameplay  
- No engine  
- No UI beyond schema  
- Pure RTT lineage

Collatz is the **mathematical backbone** of RTT ancestry — the smallest non‑trivial domain where continuity and collapse become visible.
