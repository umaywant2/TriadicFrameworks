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
