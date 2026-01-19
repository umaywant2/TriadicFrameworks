export class RTTClient {
  constructor(options = {}) {
    this.baseUrl = options.baseUrl || "https://www.triadicframeworks.org/api/rtt";
    this.version = "0.1.0";
  }

  async beacon(payload) {
    const res = await fetch(`${this.baseUrl}/beacon`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  }

  async getProfile(site) {
    const res = await fetch(`${this.baseUrl}/profile/${site}`);
    return res.json();
  }

  async setProfile(site, profile) {
    const res = await fetch(`${this.baseUrl}/profile/${site}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(profile)
    });
    return res.json();
  }

  // Diagnostics (reserved)
  async validate(payload) {
    const res = await fetch(`${this.baseUrl}/validate`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  }

  async corridor(payload) {
    const res = await fetch(`${this.baseUrl}/corridor`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  }

  async topology(payload) {
    const res = await fetch(`${this.baseUrl}/topology`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    return res.json();
  }
}
