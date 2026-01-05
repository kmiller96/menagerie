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