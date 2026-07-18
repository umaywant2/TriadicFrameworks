```python
# beacon.py — helper utilities for RTT beacon events (beta)

import time
import random


def create_session_id():
    return "rtt-" + hex(int(time.time()))[2:] + "-" + hex(random.getrandbits(32))[2:]


def collect_structure_snapshot():
    # Python SDK cannot inspect browser DOM; placeholder shape only.
    return {
        "url": "",
        "title": "",
        "nav_count": 0,
        "main_count": 0,
        "form_count": 0,
        "button_count": 0,
        "dom_nodes": 0
    }


def build_beacon_payload(site, session, event):
    return {
        "site": site,
        "session": session,
        "event": event,
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "structure": collect_structure_snapshot()
    }
```
