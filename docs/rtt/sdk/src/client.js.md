```javascript
// client.js — unified RTT API client (beta)

export class RTTClient {
  constructor(options = {}) {
    this.baseUrl = options.baseUrl || "https://www.triadicframeworks.org/api/rtt";
    this.version = "0.1.0";
  }

  async beacon(payload) {
    return this._post("/beacon", payload);
  }

  async getProfile(site) {
    return this._get(`/profile/${site}`);
  }

  async setProfile(site, profile) {
    return this._post(`/profile/${site}`, profile);
  }

  // Diagnostics (reserved)
  async validate(payload) {
    return this._post("/validate", payload);
  }

  async corridor(payload) {
    return this._post("/corridor", payload);
  }

  async topology(payload) {
    return this._post("/topology", payload);
  }

  // Internal helpers
  async _get(path) {
    const res = await fetch(`${this.baseUrl}${path}`);
    return res.json();
  }

  async _post(path, body) {
    const res = await fetch(`${this.baseUrl}${path}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body)
    });
    return res.json();
  }
}
```
