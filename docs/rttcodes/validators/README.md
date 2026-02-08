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

- [rttcodes README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/README.md)
- [rttcodes style README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/style/README.md)
- [rttcodes schema README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/schema/README.md)
- [rttcodes schema examples README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/schema/examples/README.md)
- [rttcodes generators README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/generators/README.md)
- [rttcodes generators js README](https://github.com/umaywant2/TriadicFrameworks/tree/main/docs/rttcodes/generators/js/README.md)
- [rttcodes generators python README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/generators/python/README.md)
- [rttcodes examples README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/examples/README.md)
- [rttcodes examples rtt README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/examples/rtt/README.md)
- [rttcodes examples set README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/examples/set/README.md)
- [rttcodes examples substrate README](https://github.com/umaywant2/TriadicFrameworks/blob/main/docs/rttcodes/examples/substrate/README.md)
