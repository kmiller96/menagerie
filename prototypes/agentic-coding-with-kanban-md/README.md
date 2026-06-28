# Agentic Coding with `kanban-md`

Given using Notion eats up too many tokens, could we instead use `kanban-md`?

## Quickstart

To setup the board:

```bash
brew install antopolskiy/tap/kanban-md
kanban-md init
kanban-md skill install  # NOTE: This installed into the root of the repo, not here. I manually copied it here. Also it doesn't support opencode but that was a small fix.
```

The prompt I used in opencode to play around with this was:

```
You are a software engineer. You are to claim a task from the board and complete
it. You can find tasks with the `kanban-md` CLI tool.

When you're done, make sure you handoff.
```

This worked perfectly.

## Lessons

### Skills force a single approach

The skills are awesome, but they enforce a very specific approach to how you do
things. You would have to tweak this if you wanted to install this into your
own environment.

This isn't a bad thing. In fact, with engineers, you kinda want this to be the
case. But I think it would go a long way to allow this workflow to be a bit
easier to customise or, alternatively, strip back that skill to be a bit more
generic.

### Could we make a similar CLI that is backed by Notion?

Crazy thought. Rather than have it be Notion's MCP or this local setup, could we
just create a very simple CLI tool that uses Notion as a backend? That would
give us the best of both worlds: a simple, token-efficient CLI interface but
it still has a Notion backend for persistence and collaboration.

Hell, you could make an equivalent of `kanban-md` that uses any generic backend.
So it could use Notion, Jira, ClickUp, Trello, local files, API server, etc.

### You could make a product / service out of this

You could 100% build a product/service out of this. You could setup a process for
easy integration between coding agents and a more standard engineering process.
Have a TUI, a CLI (for agents or scripters), an API/MCP, and a simple web
interface for non-technical users.

This would make a lot of sense in my future vision of PAI and having it that
custom software is written using AI primarily and my job is oversight and
management.
