# RSADI Domain Extension Template
### How to Create a New RSADI/RTT‑Inside Domain Module

This folder provides a **boilerplate template** for creating new RSADI domain
extensions. Copy this folder, rename it (e.g., `rtt-atc/`, `rtt-deepsea/`,
`rtt-space/`), and update the schema files to match your domain.

All extensions MUST follow these rules:

---

## 1. Core Invariants

- **Do not modify RSADI Core schemas.**
- **All domain fields MUST be added under `extensions.<domain>`**.
- **Extensions MUST remain optional** so core validators still pass.
- **Use JSON Schema Draft 2020‑12**.
- **Use SI units, ISO‑8601 timestamps, and UUIDv4 IDs**.

---

## 2. Schema Naming Convention

Each extension schema follows:
