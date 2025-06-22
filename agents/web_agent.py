from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools
from config.settings import OLLAMA_MODEL

model_config = Ollama(id=OLLAMA_MODEL, provider="Ollama")

web_agent = Agent(
    name="Web Agent",
    role="Search for news, insights, and market trends based on user queries",
    model=model_config,
    tools=[DuckDuckGoTools()],
    instructions=[
        "If the user query is vague, identify and summarize major trends in the market",
        "If specific topics, industries, or companies are mentioned, focus the search on those",
        "Use authoritative sources and include publication dates and URLs",
        "Capture both current sentiment and factual data where possible",
        "Adjust your search strategy based on how broad or narrow the question is"
    ],
    show_tool_calls=True,
    markdown=True
)