# Prompt Queue

Program that runs in a loop, constantly looking to run an opencode instance with a prompt from a queue.

This is a very basic implementation of how you could make an agentic coding loop. In practice you'd probably have a kanban board or some more complex system, but in principle it's just a queue of prompts that you want to run in a loop.

Add `.txt` or `.md` files containing prompts to `queue/01-triage`. The runner processes prompts from that folder and moves them to `queue/03-done` after OpenCode exits. Each invocation is recorded in `logs/`, including the input prompt.

`queue/00-backlog` and `queue/02-doing` are created at startup but are not processed, so they can be used to prepare prompts. `queue/03-done` contains prompts the runner has processed.

Hidden files in `queue/01-triage` are ignored. Other regular files are also ignored, but the runner reports their count at the warning level and reports each path when `RUST_LOG=debug` is enabled.
