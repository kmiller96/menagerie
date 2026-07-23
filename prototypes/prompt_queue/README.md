# Prompt Queue

Program that runs in a loop, constantly looking to run an opencode instance with a prompt from a queue.

This is a very basic implementation of how you could make an agentic coding loop. In practice you'd probably have a kanban board or some more complex system, but in principle it's just a queue of prompts that you want to run in a loop.

Add `.txt` or `.md` files containing prompts to `queue/todo`. The runner atomically moves a prompt to `queue/doing` before invoking OpenCode, then moves it to `queue/done` after OpenCode exits. Each invocation is recorded in `logs/`, including the input prompt.

Other regular files in `queue/todo` are ignored. The runner reports their count at the warning level and reports each path when `RUST_LOG=debug` is enabled.
