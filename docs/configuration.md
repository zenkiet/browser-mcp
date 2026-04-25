# Configuration

The server reads environment variables from process env or `.env`.

## Required

- `OPENAI_API_KEY`: API key for your OpenAI-compatible provider.
- `OPENAI_BASE_URL` (or `OPENAI_API_BASE`): Base URL for the provider API.

## Optional

- `MODEL_NAME`: Model name, defaults to `gpt-4o-mini`.
- `BROWSER_MCP_PORT`: Container host port mapping in `docker-compose.yml`.

## Example

```env
OPENAI_API_KEY=your-key
OPENAI_BASE_URL=https://api.openai.com/v1
MODEL_NAME=gpt-4o-mini
BROWSER_MCP_PORT=8000
```
