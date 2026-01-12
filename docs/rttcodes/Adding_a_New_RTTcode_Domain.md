# Adding a New RTTcode Domain

RTTcodes support multiple domains (RTT, SET, Substrate, Observer, Governance,
Docs, Other). You can extend the system by adding a new domain in a structured,
schema‑aligned way.

Follow these steps:

---

## 1. Choose a domain identifier

Use a short, lowercase string:

```
"astro"
"bio"
"ops"
"viz"
```

Avoid spaces and uppercase letters.

---

## 2. Add the domain to the schema

Edit:

```
docs/rttcodes/schema/rttcode.schema.json
```

Add your domain to the `enum` list under `domain`:

```json
"domain": {
  "type": "string",
  "enum": ["rtt", "set", "substrate", "observer", "governance", "docs", "other", "astro"]
}
```

---

## 3. Create a domain folder under examples

Add:

```
docs/rttcodes/examples/astro/
```

Include:

- `payload.json`
- `astro-rttcode.png`
- `README.md` describing the domain’s purpose

---

## 4. Define the visual identity

Add a row to:

```
docs/rttcodes/style/color-domains.png
```

And update:

```
docs/rttcodes/style/visual-guidelines.md
```

Define:

- primary color  
- secondary color  
- accent color  
- domain motifs (e.g., orbital arcs, spectral lines)

---

## 5. Add a generator example (optional)

Place a sample payload in:

```
docs/rttcodes/generators/examples/
```

This helps contributors test the new domain.

---

## 6. Validate the new domain

Run:

```
node generate_rttcode.js payload.json test.png
```

or

```
python generate_rttcode.py payload.json test.png
```

If the schema accepts the payload and the QR is generated, the domain is fully integrated.

---

## 7. Document the domain

Update:

```
docs/rttcodes/README.md
```

Add your domain to the domain list and link to its example folder.

---

## Done

Your new domain is now:

- schema‑valid  
- generator‑compatible  
- visually defined  
- documented  
- ready for use across TriadicFrameworks  
