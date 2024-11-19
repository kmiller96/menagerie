"""Runs the same script as 'test.sh' but in Python."""

import subprocess

BEFORE = "rm -rf output && mkdir output"

TAP = "docker run --rm tap-mock"
TARGET = [
    "docker run",
    "--rm",
    "--volume ./output:/app",
    "--workdir /app",
    "--interactive",
    "target-csv",
]

AFTER = "> output/state.json"

response = subprocess.run(
    f"{BEFORE} && {TAP} | {' '.join(TARGET)} {AFTER}",
    shell=True,
    capture_output=True,
)

stdout = response.stdout.decode()
stderr = response.stderr.decode()

print(stdout)
