#!/usr/bin/env bash
# shellcheck shell=bash
set -u

# Runs opencode in a loop.
#
# The loop will continue until either:
# 1. The user interrupts it (e.g., with Ctrl+C)
# 2. The LLM returns `[[EXIT]]` (all done) or `[[CONTINUE]]` (more work remains)
#    on its own line at the end of its output.
# 3. Max iterations is reached (if specified).
#
# Usage:
#   ./implement.sh [max_iterations]

MAX_ITERATIONS="${1:-0}"
ITERATION=0
EXIT_TOKEN='[[EXIT]]'
CONTINUE_TOKEN='[[CONTINUE]]'

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

while true; do
  ITERATION=$((ITERATION + 1))

  if [[ "$MAX_ITERATIONS" -gt 0 && "$ITERATION" -gt "$MAX_ITERATIONS" ]]; then
    log "$RED" "STOP" "Reached max iterations (${MAX_ITERATIONS})."
    exit 0
  fi

  log "$CYAN" "ITERATION" "${ITERATION}"

  tmpfile=$(mktemp)

  opencode run "Read OVERVIEW.md for full project context, then read TASKS.md and implement exactly ONE currently incomplete task (marked with '- [ ]'). Do not implement more than one task per run. After implementing, update TASKS.md to mark the task as complete (replace '- [ ]' with '- [x]'). At the very end of your response, output exactly one of these tokens on its own line: '${EXIT_TOKEN}' if all tasks are complete, or '${CONTINUE_TOKEN}' if there are still incomplete tasks remaining." 2>&1 | tee "$tmpfile"

  output=$(<"$tmpfile")
  rm -f "$tmpfile"

  if echo "$output" | grep -qF "$EXIT_TOKEN"; then
    log "$GREEN" "DONE" "All tasks complete!"
    exit 0
  elif echo "$output" | grep -qF "$CONTINUE_TOKEN"; then
    log "$MAGENTA" "CONTINUE" "Starting next iteration..."
  else
    log "$RED" "ERROR" "Neither ${EXIT_TOKEN} nor ${CONTINUE_TOKEN} found in output."
    exit 1
  fi
done

