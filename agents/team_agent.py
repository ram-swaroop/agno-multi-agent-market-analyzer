from agno.team import Team
from agents.web_agent import web_agent
from agents.finance_agent import finance_agent
from config.settings import model_config

agent_team = Team(
    mode="coordinate",
    members=[web_agent, finance_agent],
    model=model_config,
    success_criteria=[
        "Combined market context and financial insights",
        "Relevant web research and accurate financial analysis",
        "Answer reflects user's original intent clearly and fully"
    ],
    instructions=[
        "Determine whether the query is about companies, sectors, or general trends",
        "Have Web Agent find relevant market context and entities",
        "Have Finance Agent analyze financials for those entities",
        "Merge findings into a cohesive, insightful response",
        "Ensure balance between qualitative and quantitative insights"
    ],
    show_tool_calls=True,
    markdown=True,
    reasoning_max_steps=8
)
