```python
# __init__.py — RTT SDK package initializer (beta)

from .client import RTTClient
from .beacon import (
    create_session_id,
    collect_structure_snapshot,
    build_beacon_payload
)
from .profile import (
    create_profile,
    validate_profile
)
from .diagnostics import (
    build_validate_payload,
    build_corridor_payload,
    build_topology_payload
)

__all__ = [
    "RTTClient",
    "create_session_id",
    "collect_structure_snapshot",
    "build_beacon_payload",
    "create_profile",
    "validate_profile",
    "build_validate_payload",
    "build_corridor_payload",
    "build_topology_payload"
]
```
