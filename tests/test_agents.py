from agents.web_agent import web_agent
from agents.finance_agent import finance_agent

def test_web_agent():
    result = web_agent.run("AI semiconductor market outlook 2024")
    print("# Web Agent Result #")
    print(result.content)
    assert result.content, "Web agent returned empty content"

def test_finance_agent():
    result = finance_agent.run("Get financial data for NVDA, AMD, INTC")
    print("# Finance Agent Result #")
    print(result.content)
    assert result.content, "Finance agent returned empty content"
