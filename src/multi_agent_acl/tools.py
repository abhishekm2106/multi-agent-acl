from langchain.tools import tool
from tavily import TavilyClient
from dotenv import load_dotenv
import logging

load_dotenv()

tavily_client = TavilyClient()

@tool
def search_web(topic: str) -> str:
    """Search the web for current information on a topic. Returns titles, URLs and short snippets."""
    logging.info(f"Searching the Web for topic: {topic}")
    try:
        response = tavily_client.search(topic, max_results=5)
    except Exception as e:
        return f"Search failed: {e}"
    return "\n\n".join(
        f"{r['title']}\n{r['url']}\n{r['content']}" for r in response["results"]
    )
