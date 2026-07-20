```python
import requests
import json

class RTTClient:
    def __init__(self, base_url="https://www.triadicframeworks.org/api/rtt"):
        self.base_url = base_url
        self.version = "0.1.0"

    def beacon(self, payload):
        r = requests.post(f"{self.base_url}/beacon", json=payload)
        return r.json()

    def get_profile(self, site):
        r = requests.get(f"{self.base_url}/profile/{site}")
        return r.json()

    def set_profile(self, site, profile):
        r = requests.post(f"{self.base_url}/profile/{site}", json=profile)
        return r.json()

    # Diagnostics (reserved)
    def validate(self, payload):
        r = requests.post(f"{self.base_url}/validate", json=payload)
        return r.json()

    def corridor(self, payload):
        r = requests.post(f"{self.base_url}/corridor", json=payload)
        return r.json()

    def topology(self, payload):
        r = requests.post(f"{self.base_url}/topology", json=payload)
        return r.json()
```
