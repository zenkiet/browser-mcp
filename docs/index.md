# browser-mcp

`browser-mcp` is an MCP server for browser-driven web actions backed by an LLM.

## What it does

- Exposes a tool to browse the web and execute instructions.
- Runs inside Docker with Playwright Chromium.
- Supports custom OpenAI-compatible endpoints.

## Quick start with Docker

1. Copy `env.example` to `.env` and set your values.
2. Build and run:

```bash
docker compose up --build
```

3. The service starts on port `8000` by default.

## Quick start locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```
