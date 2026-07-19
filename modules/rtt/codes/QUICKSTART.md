# ⚡ Quickstart

RTTcodes are QR‑compatible identifiers that bind any artifact to its canonical
TriadicFrameworks metadata. To generate one:

### 1. Create a payload file

```json
{
  "domain": "rtt",
  "artifact_type": "paper",
  "version": "v2.1.0",
  "triad": {
    "f_R": "1.00",
    "tau_R": "144ms",
    "Q_R": "0.97"
  },
  "url": "https://triadicframeworks.org/_ideas/Resonance-Time_Theory.html"
}
```

Save as:

```
payload.json
```

### 2. Generate the RTTcode (QR PNG)

**JavaScript:**

```
node generate_rttcode.js payload.json out.png
```

**Python:**

```
python generate_rttcode.py payload.json out.png
```

### 3. Use the RTTcode

Embed the PNG in:

- READMEs  
- PDFs  
- diagrams  
- print materials  
- onboarding docs  

Every RTTcode encodes a URL+token that points to the artifact’s canonical home.
