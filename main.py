import os
from browser_use import ChatOpenAI
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

# Initialize MCP Server
mcp = FastMCP("browser-use-node", host="0.0.0.0")

# Configure AI
load_dotenv()
CUSTOM_BASE_URL = os.getenv("OPENAI_BASE_URL")
CUSTOM_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

if not CUSTOM_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY in environment.")

if not CUSTOM_BASE_URL:
    raise RuntimeError("Missing OPENAI_BASE_URL in environment.")

if not MODEL_NAME:
    raise RuntimeError("Missing MODEL_NAME in environment.")

llm = ChatOpenAI(
    model=MODEL_NAME,
    api_key=CUSTOM_API_KEY,
    base_url=CUSTOM_BASE_URL,
)

browser = None


def get_browser():
    global browser
    if browser is None:
        from browser_use import BrowserSession

        browser = BrowserSession(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-blink-features=AutomationControlled",
            ],
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        )
    return browser

@mcp.tool(description="Browse the web and perform complex actions.")
async def browse_and_act(instruction: str, url: str = "https://google.com") -> str:
    from browser_use import Agent

    # Hint the browser agent to start at the given URL before executing instruction.
    composed_task = f"Start from {url}. Then: {instruction}"

    agent = Agent(
        task=composed_task,
        llm=llm,
        browser=get_browser(),
    )
    result = await agent.run()
    return str(result.final_result())

if __name__ == "__main__":
    mcp.run(transport="sse")