# 🧬 Remix Lineage Tracker
# Tracks depth and echo strength of contributor remix chains

import json

def track_lineage(remix_chain):
    depth = len(remix_chain)
    echo_strength = "Strong" if depth >= 3 else "Faint"

    lineage_report = {
        "chain": remix_chain,
        "depth": depth,
        "echo_strength": echo_strength
    }

    print(json.dumps(lineage_report, indent=2))
    return lineage_report
