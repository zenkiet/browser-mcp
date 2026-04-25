# Browser MCP

MCP server for browser-driven automation using Playwright via HTTP/SSE MCP

## Requirements

- Python 3.11+
- Docker (recommended for runtime parity)

## Configure environment

Copy template:

```bash
cp env.example .env
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## Run with Docker

```bash
docker compose up --build
```

The service listens on port `8000` in the container.

## Documentation

Docs are published via GitHub Pages using MkDocs.
Source files live in `docs/`.

## Changelog

See `CHANGELOG.md`.
