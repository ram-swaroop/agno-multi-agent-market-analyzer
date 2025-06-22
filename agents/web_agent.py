from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from config.settings import model_config


web_agent = Agent(
    name="Web Agent",
    role="Search for news, insights, and market trends based on user query",
    model=model_config,
    tools=[DuckDuckGoTools()],
    instructions=[
        "Search based on user query and provide relevant insights",
        "Prioritize recent news (last 3–6 months)",
        "If companies are mentioned, focus on news about them",
        "If industries are mentioned, summarize key market trends and players",
        "If no specifics, summarize general market sentiment",
        "Highlight important data points, dates, companies, and sources",
        "Summarize findings clearly to help finance agent analyze further"
    ],
    show_tool_calls=True,
    markdown=True
)