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
