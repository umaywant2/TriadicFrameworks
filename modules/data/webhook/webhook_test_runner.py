# 🧪 webhook_test_runner.py

import yaml
import json
from datetime import datetime

# Sample paper metadata
sample_paper = {
    "paper": "Triadic Framework for Quantum Mechanics – Entropy’s Harmonic.docx",
    "status": "✅ Validated",
    "theme": "Quantum",
    "badge": "Quantum Weaver"
}

# Load config
with open("papers/manifest_updater_config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Extract webhook template
webhook = config["ping"]["webhook"]
template = webhook["payload_template"]

# Format payload
payload = template.format(**sample_paper)

# Simulate dry run
print("📡 Dry Run — Webhook Payload:")
print(json.dumps(json.loads(payload), indent=2))
print(f"\n🔗 Would POST to: {webhook['url']} at {datetime.now().isoformat()}")
