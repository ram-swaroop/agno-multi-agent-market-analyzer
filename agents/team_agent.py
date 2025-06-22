from agno.team import Team
from agno.models.ollama import Ollama
from agents.web_agent import web_agent
from agents.finance_agent import finance_agent
from config.settings import OLLAMA_MODEL

model_config = Ollama(id=OLLAMA_MODEL, provider="Ollama")

agent_team = Team(
    mode="coordinate",
    members=[web_agent, finance_agent],
    model=model_config,
    success_criteria=[
        "Relevant market context and financial data based on user's intent",
        "Specific details if the query targets companies or sectors",
        "General overviews if the query is open-ended",
        "Balanced report with qualitative and quantitative insights",
        "All claims backed by data and sources"
    ],
    instructions=[
        "Adapt analysis based on the user's question — whether broad or narrow",
        "Web agent should gather market trends and sentiment",
        "Finance agent should provide data-driven insights on mentioned companies or sectors",
        "Merge both outputs into a clear and cohesive market summary",
        "Ensure relevance, clarity, and traceability to sources"
    ],
    show_tool_calls=True,
    markdown=True,
    reasoning_max_steps=5
)