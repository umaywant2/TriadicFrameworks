#!/usr/bin/env bash
#
# 3PAK Shell — Profile Loader
# TriadicFrameworks — Resonance‑Time Theory Canon
#
# This script initializes the 3PAK environment when sourced by a shell.
# It provides lightweight, non-intrusive scaffolding for triadic‑aware
# workflows inside the tft‑3pack ecosystem.

# -------------------------------------------------------------
# Environment Setup
# -------------------------------------------------------------

export THREEPAK_HOME="${THREEPAK_HOME:-$HOME/.3pak}"
export THREEPAK_STATE="$THREEPAK_HOME/state"
export THREEPAK_LOG="$THREEPAK_HOME/3pak.log"

# Create directories if missing
mkdir -p "$THREEPAK_HOME"

# -------------------------------------------------------------
# Logging Helper
# -------------------------------------------------------------
_3pak_log () {
    echo "[3PAK] $*" >> "$THREEPAK_LOG"
}

_3pak_log "3PAK shell profile loaded."

# -------------------------------------------------------------
# Core Functions
# -------------------------------------------------------------

threepak_status () {
    echo "📦 3PAK Environment"
    echo "---------------------------"
    echo "Home:   $THREEPAK_HOME"
    echo "State:  $THREEPAK_STATE"
    echo "Log:    $THREEPAK_LOG"
    echo ""
}

threepak_note () {
    local msg="$*"
    echo "$msg" >> "$THREEPAK_STATE"
    _3pak_log "State note added: $msg"
}

threepak_clear () {
    > "$THREEPAK_STATE"
    _3pak_log "State cleared."
    echo "3PAK state cleared."
}

# -------------------------------------------------------------
# Friendly Startup Message
# -------------------------------------------------------------
echo "✨ 3PAK shell environment initialized."

