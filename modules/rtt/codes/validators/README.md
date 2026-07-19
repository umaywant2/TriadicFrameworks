# RTTcode Validators

This folder contains tools that verify whether an RTTcode payload is valid,
well‑formed, and compliant with the canonical RTTcode schema.

Validators ensure:

- required fields are present (`domain`, `artifact_type`, `version`, `url`)
- optional triad metadata is correctly typed
- payloads match the JSON Schema in `/schema/rttcode.schema.json`
- RTTcode URLs and tokens follow the standard format

Use these validators when:

- creating new RTTcodes
- integrating RTTcodes into build pipelines
- checking contributor submissions
- testing generators

Each validator is intentionally lightweight and easy to embed into other tools.
