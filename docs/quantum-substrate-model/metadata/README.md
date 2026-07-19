# Metadata

This directory contains citation and publication metadata for the Quantum Substrate Model (QSM). These files support archival, citation, and versioning workflows and are not part of the conceptual content of the model.

They exist to ensure that the publication can be referenced, indexed, and updated consistently over time.

---

## Files

### `CITATION.cff`

Defines the canonical citation information for this work. This file is used by GitHub, Zenodo, and other tooling to generate standardized citations.

Update this file only when:
- A new Zenodo version is published
- Author or licensing information changes

---

### `zenodo.json`

Provides structured metadata for Zenodo publication. This file mirrors the information entered during Zenodo upload and supports version lineage tracking.

The `doi` field is added **after** Zenodo assigns a DOI for a given version.

---

## Versioning Notes

- Metadata versions should match the published Zenodo version.
- Minor formatting or typographical corrections do not require metadata updates.
- New Zenodo versions require updating both `CITATION.cff` and `zenodo.json`.

---

## Scope

These metadata files do not define or modify the Quantum Substrate Model itself. They exist solely to support citation, archival stability, and reproducibility of the published artifact.
