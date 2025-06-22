# 📊 Market Analyzer

This project uses LangGraph-compatible agents from [`agno`](https://pypi.org/project/agno/) to analyze market and financial trends using:

- Web search via DuckDuckGo
- Financial data from Yahoo Finance (yfinance)
- LLM-powered coordination via Ollama

---

## 📁 Project Structure

```
market-analyzer/
├── agents/
│   ├── web_agent.py
│   ├── finance_agent.py
│   └── team_agent.py
├── config/
│   ├── __init__.py
│   └── settings.py
├── tests/
│   ├── __init__.py
│   └── test_agents.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
├── Makefile
├── main.py
└── README.md
```

---

## 🚀 Quick Start

### ▶️ Run with Python

```bash
# 1. Install dependencies (requires Python 3.12.8)
pip install -r requirements.txt

# 2. Run analysis
python main.py --query "What are the current trends in the semiconductor market?"

# 3. Run tests
pytest
```

### 🛠️ Developer Shortcuts

Use the included `Makefile`:

```bash
make run    # Run the app with a default query
make test   # Run all tests
make lint   # Lint the code (if flake8 is installed)
```

### 🐳 Docker Support

Run the entire app in a containerized environment:

```bash
docker-compose build
docker-compose up
```

This uses:
* `python:3.12.8-slim` as the base image
* `OLLAMA_MODEL` as an environment variable (see `.env.example`)

---

## ✅ Python Version

This project uses and expects **Python 3.12.8**.

For consistent results, make sure to use the same version locally, in Docker, and in CI.

---

## 🧪 Continuous Integration

GitHub Actions will:
* Install dependencies
* Run all unit tests (`pytest`)

Workflow config is located in `.github/workflows/ci.yml`.

---

## 📄 License

MIT