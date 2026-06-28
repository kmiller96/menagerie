# Agentic Coding

Thought: can I use Notion as my centralised task board for agentic coding?

TL;DR: Yes, you can, but it's not very efficient.

Answer: You can connect opencode to Notion very easily. Setup was like 5 minutes
at most. The issue is that connecting the MCP server just eats up so much of the
context window. You'd be better off managing everything locally and then just
syncing the results to Notion. That way you could read relatively small files
e.g. a single markdown file instead of heaps of JSON.

Here was an example prompt I used which worked well for me:

```
Go to the "Tasks" board under "Engineering" in Notion. Summarise the board and
what tasks are currently in progress.
```
