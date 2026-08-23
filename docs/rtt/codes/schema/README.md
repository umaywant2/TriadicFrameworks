# RTTcode Schema

This folder contains the canonical JSON Schema for RTTcodes.

The schema defines:

- required fields
- optional triad metadata
- allowed domain values
- versioning rules
- structural constraints

Tools in `/validators` and `/generators` rely on this schema for correctness.

If you are building RTTcode tooling, validating payloads, or extending the
standard, this is the authoritative reference.
