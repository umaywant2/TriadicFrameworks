# Substrate Communications — Core Concepts  
_Version 1.0.0_

## 1. Purpose

Substrate Communications defines a minimal, structural messaging layer for systems that cannot rely on continuous, high‑bandwidth telemetry. Instead of streaming raw data, assets emit **summaries** that describe:

- drift against invariants  
- paradox between signals  
- coherence across a mesh  

This enables long‑range, low‑bandwidth, substrate‑aware communication.

## 2. Assets and Invariants

An **asset** is any monitored entity:

- industrial device  
- ecological node  
- spacecraft subsystem  
- planetary region  

An **invariant** is a structural expectation (e.g., temperature band, nutrient flux, radiation range).  
Drift is evaluated relative to invariants.

## 3. Drift

**Drift** is deviation from an invariant over a time window.  
It is not failure — it is **movement through state space**.

Drift is summarized using `STATE_SUMMARY` messages.

## 4. Paradox

A **paradox** occurs when:

- sensors disagree  
- models conflict  
- proxies diverge  

Paradox is preserved using `PARADOX_SUMMARY` messages.

## 5. Mesh‑Level Coherence

Substrate Communications scales from single assets to **meshes**:

- industrial networks  
- forest‑scale ecological meshes  
- multi‑probe deep‑space constellations  
- planetary‑scale sampling regimes  

Across a mesh, drift and paradox summaries reveal:

- stress fronts  
- anomalies  
- coherence patterns  
- life‑regime signatures  

The same grammar applies at all scales.
