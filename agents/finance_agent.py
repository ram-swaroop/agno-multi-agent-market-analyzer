from agno.agent import Agent
from agno.tools.yfinance import YFinanceTools
from config.settings import model_config

finance_agent = Agent(
    name="Finance Agent",
    role="Analyze financial data for companies or sectors based on the user's query and web findings",
    model=model_config,
    tools=[YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
        stock_fundamentals=True,
        technical_indicators=True,
        income_statements=True
    )],
    instructions=[
        "Analyze companies or sectors from the user query or web agent findings",
        "If companies are mentioned, analyze them directly",
        "If sectors are mentioned, focus on top companies or sector ETFs",
        "Include stock prices, valuation metrics, financial health, and analyst views",
        "Explain what the financial data implies in context of the original question",
        "Summarize key insights and compare across companies when relevant"
    ],
    show_tool_calls=True,
    markdown=True
)
