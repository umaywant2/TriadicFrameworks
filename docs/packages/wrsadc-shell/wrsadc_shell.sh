#!/usr/bin/env bash
# wrsadc_shell.sh
#
# WRSADC shell wrapper for TFT_3Pack_v1.3 tools.
# Tracks dimensions, entities, and states in a simple log file.

WRSADC_CONTEXT="tft-3pack"
WRSADC_LOG="${HOME}/.wrsadc.log"

wrsadc_init() {
  WRSADC_CONTEXT="${1:-tft-3pack}"
  mkdir -p "$(dirname "${WRSADC_LOG}")" 2>/dev/null || true
}

wrsadc_mark() {
  local dimension="$1"
  local entity="$2"
  local state="$3"
  local ts
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  echo "${ts}|${WRSADC_CONTEXT}|${dimension}|${entity}|${state}" >> "${WRSADC_LOG}"
}

wrsadc_summary() {
  echo "[WRSADC] context=${WRSADC_CONTEXT}"

  local total
  total="$(grep "|${WRSADC_CONTEXT}|" "${WRSADC_LOG}" | wc -l | awk '{print $1}')"
  echo "  total_events: ${total}"

  echo "  dimensions:"
  grep "|${WRSADC_CONTEXT}|" "${WRSADC_LOG}" \
    | awk -F'|' '{print $3}' | sort | uniq -c | sort -nr \
    | awk '{printf "    %s (%s)\n", $2, $1}'

  echo "  states:"
  grep "|${WRSADC_CONTEXT}|" "${WRSADC_LOG}" \
    | awk -F'|' '{print $5}' | sort | uniq -c | sort -nr \
    | awk '{printf "    %s (%s)\n", $2, $1}'
}

