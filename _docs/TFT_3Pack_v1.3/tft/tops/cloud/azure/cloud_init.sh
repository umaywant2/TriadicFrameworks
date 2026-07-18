#!/bin/bash
echo "🌀 Initializing TFT Agent Container..."
mkdir -p /app/logs
touch /app/logs/remix_trace.log
touch /app/logs/badge_handshake.txt
touch /app/logs/glyphstream_pulse.log
echo "✅ Logs initialized. Agent ready to echo."
python3 /app/main.py

