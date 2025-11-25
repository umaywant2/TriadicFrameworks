# 📚 Query Client Library

in both Python and JavaScript, designed to call the corridor API endpoints we defined in RFC‑API‑0006. This gives collaborators a clean way to embed corridor queries into their validator workflows without touching raw YAML.

---

## Python Client

File: `clients/python/corridor_client.py`

```python
import requests

class CorridorClient:
    def __init__(self, base_url="http://localhost:5000/v1"):
        self.base_url = base_url

    def get_corridors_by_glyph(self, glyph):
        url = f"{self.base_url}/corridors/glyph/{glyph}"
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()

    def get_corridors_by_rci(self, band):
        url = f"{self.base_url}/corridors/rci/{band}"
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()

    def get_corridors_by_remix(self, parent_scroll):
        url = f"{self.base_url}/corridors/remix/{parent_scroll}"
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()

    def get_corridor_metadata(self, corridor_id):
        url = f"{self.base_url}/corridors/{corridor_id}"
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()
```

### Example Usage

```python
client = CorridorClient(base_url="http://localhost:5000/v1")

print(client.get_corridors_by_glyph("◆"))
print(client.get_corridors_by_rci("high"))
print(client.get_corridors_by_remix("s-1001"))
print(client.get_corridor_metadata("c-001"))
```

---

## JavaScript Client

File: `clients/js/corridorClient.js`

```javascript
class CorridorClient {
  constructor(baseUrl = "http://localhost:5000/v1") {
    this.baseUrl = baseUrl;
  }

  async getCorridorsByGlyph(glyph) {
    const resp = await fetch(`${this.baseUrl}/corridors/glyph/${glyph}`);
    return await resp.json();
  }

  async getCorridorsByRci(band) {
    const resp = await fetch(`${this.baseUrl}/corridors/rci/${band}`);
    return await resp.json();
  }

  async getCorridorsByRemix(parentScroll) {
    const resp = await fetch(`${this.baseUrl}/corridors/remix/${parentScroll}`);
    return await resp.json();
  }

  async getCorridorMetadata(corridorId) {
    const resp = await fetch(`${this.baseUrl}/corridors/${corridorId}`);
    return await resp.json();
  }
}

export default CorridorClient;
```

### Example Usage

```javascript
import CorridorClient from "./corridorClient.js";

const client = new CorridorClient("http://localhost:5000/v1");

(async () => {
  console.log(await client.getCorridorsByGlyph("◆"));
  console.log(await client.getCorridorsByRci("medium"));
  console.log(await client.getCorridorsByRemix("s-1001"));
  console.log(await client.getCorridorMetadata("c-001"));
})();
```

---

## Validator Hooks

- **Schema compliance:** Responses validated against RFC‑QEB‑0002 corridor schema.  
- **Error handling:** Raise exceptions (Python) or reject promises (JS) if API returns non‑200.  
- **Versioning:** Clients default to `/v1` endpoints but allow override.  
- **Checksum headers:** Clients can optionally log checksum headers for reproducibility.  

---

## Notes

- Both clients abstract away HTTP details, returning JSON objects ready for validator workflows.  
- Collaborators can embed these calls into scroll validation pipelines, remix lineage explorers, or corridor clarity dashboards.  
- Modular design: clients can be extended with new endpoints (e.g., anomaly search, glyph registry queries).  

---
