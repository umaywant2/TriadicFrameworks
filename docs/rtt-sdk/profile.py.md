```python
# profile.py — helper utilities for RTT site profiles (beta)

def create_profile(version="1.0", supports=None, contact=""):
    if supports is None:
        supports = []
    return {
        "rtt_version": version,
        "supports": supports,
        "contact": contact
    }


def validate_profile(profile):
    if not isinstance(profile, dict):
        return False
    if "rtt_version" not in profile:
        return False
    if "supports" not in profile or not isinstance(profile["supports"], list):
        return False
    return True
```
