#!/usr/bin/env bash
# shellcheck shell=bash
set -u

# Runs opencode in a loop with dual-condition exit detection.
#
# The loop will continue until either:
# 1. The user interrupts it (e.g., with Ctrl+C)
# 2. BOTH conditions are met:
#    a. Completion indicators >= 2 (heuristic keyword detection across loops)
#    b. LLM explicitly sets EXIT_SIGNAL: true in a RALPH_STATUS block
# 3. Max iterations is reached (if specified).
#
# This dual-condition gate prevents premature exits when the LLM sounds
# "done" in natural language but still has work remaining, or vice versa.
#
# Usage:
#   ./implement.sh [max_iterations]

MAX_ITERATIONS="${1:-0}"
ITERATION=0
COMPLETION_INDICATORS=0

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

log() {
  local color="$1" label="$2" message="$3"
  echo -e "${color}${BOLD}[${label}]${NC} ${message}" >&2
}

cleanup() {
  echo
  log "$YELLOW" "EXIT" "Interrupted by user."
  exit 0
}

trap cleanup SIGINT SIGTERM

if ! command -v opencode &>/dev/null; then
  log "$RED" "ERROR" "opencode not found on PATH. Install it first."
  exit 1
fi

# --- Dual-condition exit gate functions ---

# Detect completion keywords in output as heuristic indicators.
completion_keywords=("done" "complete" "finished" "all tasks complete" "nothing to do" "no changes" "already implemented" "up to date")

check_completion_indicators() {
  local output="$1"
  for keyword in "${completion_keywords[@]}"; do
    if echo "$output" | grep -qi "$keyword"; then
      return 0
    fi
  done
  return 1
}

# Parse EXIT_SIGNAL from RALPH_STATUS block in LLM output.
# Supports both formats:
#   1) ---RALPH_STATUS--- ... EXIT_SIGNAL: true ... ---END_RALPH_STATUS---
#   2) Inline RALPH_STATUS: EXIT_SIGNAL: true
parse_exit_signal() {
  local output="$1"
  if echo "$output" | grep -qE -- "^[[:space:]]*(---RALPH_STATUS---|RALPH_STATUS:)"; then
    local sig
    sig=$(echo "$output" | grep "EXIT_SIGNAL:" | tail -1 | cut -d: -f2 | xargs)
    if [[ -n "$sig" ]]; then
      echo "$sig"
      return
    fi
    local status
    status=$(echo "$output" | grep "STATUS:" | tail -1 | cut -d: -f2 | xargs)
    if [[ "$status" == "COMPLETE" ]]; then
      echo "true"
      return
    fi
  fi
  echo ""
}

# Check git for file changes (progress detection).
# Resets completion indicators if the LLM is still modifying files.
has_recent_progress() {
  if command -v git &>/dev/null && git rev-parse --git-dir &>/dev/null 2>&1; then
    {
      git diff --name-only HEAD 2>/dev/null
      git diff --name-only --cached 2>/dev/null
    } | grep -q . && return 0
  fi
  return 1
}

while true; do
  ITERATION=$((ITERATION + 1))

  if [[ "$MAX_ITERATIONS" -gt 0 && "$ITERATION" -gt "$MAX_ITERATIONS" ]]; then
    log "$RED" "STOP" "Reached max iterations (${MAX_ITERATIONS})."
    exit 0
  fi

  log "$CYAN" "ITERATION" "${ITERATION}"

  tmpfile=$(mktemp)

  opencode run "Read OVERVIEW.md for full project context, then read TASKS.md and implement exactly ONE currently incomplete task (marked with '- [ ]'). Do not implement more than one task per run. After implementing, update TASKS.md to mark the task as complete (replace '- [ ]' with '- [x]').

At the very end of your response, include a structured RALPH_STATUS block:

---RALPH_STATUS---
EXIT_SIGNAL: true
STATUS: COMPLETE
---END_RALPH_STATUS---

- Set EXIT_SIGNAL to true only if ALL tasks are complete and the project is done.
- Set STATUS to COMPLETE if all tasks are done, or IN_PROGRESS otherwise.
- If there are still incomplete tasks, set EXIT_SIGNAL to false and STATUS to IN_PROGRESS." 2>&1 | tee "$tmpfile"

  output=$(<"$tmpfile")
  rm -f "$tmpfile"

  # --- Dual-condition exit detection ---

  exit_signal=$(parse_exit_signal "$output")

  # Check for explicit [[EXIT]] / [[CONTINUE]] token (backward compatible)
  explicit_exit=false
  explicit_continue=false
  if echo "$output" | grep -qF '[[EXIT]]'; then
    explicit_exit=true
  fi
  if echo "$output" | grep -qF '[[CONTINUE]]'; then
    explicit_continue=true
  fi

  # Completion indicators: accumulate only when EXIT_SIGNAL is explicitly true
  if [[ "$exit_signal" == "true" ]]; then
    COMPLETION_INDICATORS=$((COMPLETION_INDICATORS + 1))
  elif [[ "$exit_signal" == "false" ]]; then
    # Claude explicitly says keep working — reset indicators
    COMPLETION_INDICATORS=0
  elif check_completion_indicators "$output"; then
    # No explicit signal but keywords found — count as weak indicator
    COMPLETION_INDICATORS=$((COMPLETION_INDICATORS + 1))
  fi

  # Progress detection: if files changed, reset indicators since work continues
  if has_recent_progress; then
    COMPLETION_INDICATORS=0
  fi

  log "$BLUE" "SIGNALS" "EXIT_SIGNAL=${exit_signal:-not_found} completion_indicators=${COMPLETION_INDICATORS}"

  # Safety circuit breaker: force exit after 5 consecutive EXIT_SIGNAL=true
  if [[ "$exit_signal" == "true" && "$COMPLETION_INDICATORS" -ge 5 ]]; then
    log "$YELLOW" "SAFETY" "Force exit after 5 consecutive EXIT_SIGNAL=true (circuit breaker)"
    exit 0
  fi

  # Dual-condition exit gate: BOTH completion_indicators >= 2 AND EXIT_SIGNAL=true
  if [[ "$exit_signal" == "true" && "$COMPLETION_INDICATORS" -ge 2 ]]; then
    log "$GREEN" "DONE" "All tasks complete! (exit_signal=true, indicators=${COMPLETION_INDICATORS})"
    exit 0
  fi

  # Fallback: explicit [[EXIT]] token (backward compat)
  if [[ "$explicit_exit" == "true" ]]; then
    log "$GREEN" "DONE" "All tasks complete! ([[EXIT]] token)"
    exit 0
  fi

  # Error: no relevant signal found
  if [[ "$explicit_continue" == "false" && -z "$exit_signal" ]]; then
    log "$RED" "ERROR" "No RALPH_STATUS block, [[EXIT]], or [[CONTINUE]] found in output."
    exit 1
  fi

  log "$MAGENTA" "CONTINUE" "Starting next iteration..."
done

