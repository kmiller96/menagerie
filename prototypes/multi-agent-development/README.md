# Multi-Agent Development

Explores how to do multi-agent development using Git worktrees and multiple
codex/claude sessions. In my case I'm using OpenCode, because I don't care if
they train on my data, but in a client environment you should use a paid offering.

## Task

Let's focus on creating a very simple note taking app in Next.js. We will store
the notes in a sqlite database.

## Notes / Learnings

### Architecture

My opinion for how to set this thing up is basically as follows:

1. Setup a task board. I did this by basically creating a folder called `tasks/`
   and putting individual markdown files in there. I explicitly assigned tasks
   to my agents but you could 100% be smarter about this by having the AI figure
   out what to do and/or using a sytem like https://github.com/antopolskiy/kanban-md.
   Alternatively, you could hook up an MCP to Linear/Notion/etc.
2. Setup your agents. I like the idea of setting up "long-living" agents. So you
   create a worktree, setup their development environment (e.g. a local dev
   server), etc. I did this all manually but I can see how you could do this
   with a super simple bootstrapping script e.g. `./new-agent "Bob"`.
3. Run each agent. I, again, managed them manually but there is nothing stopping
   you from running a script e.g. `opencode run "/implement"`. Have the agent
   do the whole engineering lifecycle of implementing, committing, and creating
   a pull request.
4. Either you or, optionally, another agent reviews this agent's work. If it
   looks good you merge!

## Multi-Agent vs. Single Agent vs. Pair Programming?

My initial vibe is that multi-agent works really well in large, established
codebases. Especially when each agent can work on quite distinct parts of the
codebase and requirements are clear and obvious.

For new codebases that are rapidly changing, I would probably prefer having just
a single agent in a loop. That way you can avoid merge conflicts and other
annoying headaches in the early days.

Pair programming still seems like an easy way to 10x an agent's performance. In
a lot of ways it's like sitting down with a junior engineer. They will do a lot
better if you help them through the hardest problems.

## SWEs == Engineering Product Management

In all cases, a huge part of the SWE job is now automated. You don't need to
actually battle with the computer much anymore. You can mostly delegate this work
to an AI.

So what is the job now? You're effectively a product manager. Your job is to
take requirements and covert them into specs that an AI can implement. Done
right, your job becomes mostly creating designs for an AI to implement. And you
can reserve your effort for the last 10% difficult tasks.

### Creating Worktrees

```bash
git worktree add <path>
```

###
