from agno.team import Team
from agents.web_agent import web_agent
from agents.finance_agent import finance_agent
from config.settings import model_config

agent_team = Team(
    mode="coordinate",
    members=[web_agent, finance_agent],
    model=model_config,
    success_criteria=[
        "Answer reflects user's original intent clearly and fully",
        "Includes comprehensive quantitative financial metrics for all relevant companies",
        "All financial metrics are explicitly listed (not summarized)",
        "Relevant web research is contextual and supports financial interpretation",
        "Response is structured with separate sections for financial and market context"
    ],
    instructions=[
        "Step 1: Identify whether the query concerns a specific company, sector, or market trend.",
        "Step 2: Web Agent should search for and report relevant market context, public sentiment, news, and competitive positioning.",
        "Step 3: Finance Agent should extract and report detailed financial metrics for the relevant companies or sectors. This MUST include:",
        "    - Revenue, Net Profit, Operating and Gross Margins",
        "    - Earnings per Share (EPS), Price to Earnings Ratio (PE Ratio)",
        "    - Debt-to-Equity Ratio, Market Capitalization",
        "    - Free Cash Flow, Return on Equity (ROE), Return on Capital Employed (ROCE)",
        "    - Latest Quarterly and Annual performance figures",
        "    - Analyst Ratings (Buy/Hold/Sell), if available",
        "Step 4: Do NOT summarize or omit numerical metrics. Do NOT combine financial insights into one sentence.",
        "Step 5: Present financial metrics in a markdown-formatted table for clarity and readability.",
        "Step 6: Merge the outputs with clear section headers:",
        "    - Use '## 📊 Financial Overview' for the Finance Agent's output",
        "    - Use '## 🌐 Market Context' for the Web Agent's output",
        "Step 7: Ensure the response maintains both detail and structure. Avoid excessive summarization.",
    ],
    show_tool_calls=True,
    markdown=True,
    reasoning_max_steps=8
)
