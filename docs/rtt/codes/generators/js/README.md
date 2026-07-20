# JavaScript RTTcode Generator

This folder contains the Node.js RTTcode generator.

Features:

- schema‑aligned payload validation
- URL+token RTTcode construction
- QR PNG output using the `qrcode` package
- CLI usage for automation

Run:
```
node generate_rttcode.js payload.json output.png
```

Use this generator in JS‑based build pipelines or web tooling.
