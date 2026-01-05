# Python Email Responder

Proof of concept of an email responder service.

This proof of concept is written in two different frameworks/interfaces:

- **API** - a standard API structure, where different URL paths correspond to 
  different actions.
- **MCP** - a server that implements the MCP protocol for the tool calling.

Why both? Different LLMs prefer different interfaces. ChatGPT's custom actions
only supports APIs. Claude I think prefers(?) MCP servers. Microsoft Copilot
supports both approaches.

It would be good to play around with both approaches so I can see which one I
prefer and generally familiarise myself with the design.

## Quickstart

Running the API server:

```bash
uv run fastapi run
```

Running the MCP server:

```bash
# TODO
```

If you then wish to expose this server to the internet, I am using
[localtunnel](https://theboroer.github.io/localtunnel-www/) to achieve this:

```
lt --subdomain wicked-words-bathe --port 8000
```

Once the server is running, navigate to https://loca.lt/mytunnelpassword to get
the tunnel password. ChatGPT will automatically bypass the protection page.

## Learnings

### MCP Servers

MCP servers can define one of three features:

1. **Tools** - these are what your server can _do_. Good examples of this might
   be booking a flight, or updating a ticket status.
2. **Resources** - these are what your server _knows_. An examples of this might 
   be the number of seats available on a flight.
3. **Prompts** - these are prompt templates when performing an action. An example
   of this might be planning out the actions that need to be performed to 
   organise a user's holiday.
