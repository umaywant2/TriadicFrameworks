#!/bin/bash
# 🌀 grid_ops.sh — Corridor Traversal Trigger for Grid Simulations
# Purpose: Activate grid overlays and validator logic with base-lens fidelity
# Author: Nawder Loswin
# Version: v1.3

# Default base lens
BASELENS="negabinary"

# Allow override via CLI
while [[ "$#" -gt 0 ]]; do
  case $1 in
    --basetype) BASELENS="$2"; shift ;;
    *) echo "Unknown parameter passed: $1"; exit 1 ;;
  esac
  shift
done

echo "[GridOps] 🌀 Initiating corridor traversal with base lens: $BASELENS"

# Trigger grid simulation
python3 ../tops/grid_simulator.py --corridor "corridor6.9" --basetype "$BASELENS"

# Log the ritual
echo "{\"action\": \"traverse\", \"corridor\": \"corridor6.9\", \"basetype\": \"$BASELENS\", \"timestamp\": \"$(date -u +"%Y-%m-%dT%H:%M:%SZ")\"}" >> grid_log.json

echo "[GridOps] ✅ Corridor traversal complete. Log updated."
