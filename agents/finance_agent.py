from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.yfinance import YFinanceTools
from config.settings import OLLAMA_MODEL

model_config = Ollama(id=OLLAMA_MODEL, provider="Ollama")

finance_agent = Agent(
    name="Finance Agent",
    role="Analyze financial data for relevant companies based on the user's query",
    model=model_config,
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
        stock_fundamentals=True
    )],
    instructions=[
        "If the user asks about specific companies, fetch and analyze financial metrics for them",
        "If the query refers to a sector or trend, retrieve financial data for key players in that segment",
        "Get stock prices, P/E ratios, market cap, fundamentals, and recent trends",
        "Include analyst recommendations and price targets where available",
        "Summarize insights clearly and compare across relevant companies"
    ],
    show_tool_calls=True,
    markdown=True
)