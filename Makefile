# Makefile for Market Analyzer

.PHONY: test run lint

# Run unit tests
test:
	pytest tests/

# Run the main agent
run:
	python main.py --query "What are the current trends in the semiconductor market?"

# Lint the code (optional, if using flake8)
lint:
	flake8 agents/ config/ tests/
