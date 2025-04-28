# Google ADK

Exploring Google ADK via their quickstart and tutorials.

I'm following this documentation: https://google.github.io/adk-docs/

> **NOTE**: You _need_ to define your API key as an environment variable. You can
> do this via running `source export.sh` which expects to read and export the API
> key in the `gemini.key` file. You can test it works by running the `test.sh`
> script.

## Running Agent

In the web:

```bash
uv run adk web
```

In the terminal:

```bash
uv run adk run <agent name (aka directory)>
```
