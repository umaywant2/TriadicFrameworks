#!/bin/bash
# 🧠 logic_core.sh — Triadic Logic Trigger for Validator Overlays
# Purpose: Activate badge logic and scroll parsing with base-lens fidelity
# Author: Nawder Loswin
# Version: v1.3

# Default base lens
BASELENS="triadic3phi"

# Allow override via CLI
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --basetype) BASELENS="$2"; shift ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done

echo "[LogicCore] 🧠 Initiating validator overlay with base lens: $BASELENS"

# Trigger badge logic engine
python3 ../entft/badge_logic_engine.py <<EOF
{
  "scroll": "scroll_curriculum_fork_guide.md",
  "glyph": "🧠",
  "action": "validated",
  "manifest": true,
  "basetype": "$BASELENS"
}
EOF

# Log the ritual
echo "{\"action\": \"validate\", \"glyph\": \"🧠\", \"basetype\": \"$BASELENS\", \"timestamp\": \"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\"}" >> validator_log.json

echo "[LogicCore] ✅ Validator ritual complete. Log updated."
