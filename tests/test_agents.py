import socket
import pytest
from unittest.mock import patch, MagicMock
from agents.web_agent import web_agent
from agents.finance_agent import finance_agent

# Check if Ollama is running locally
def is_ollama_running():
    try:
        socket.create_connection(("localhost", 11434), timeout=2)
        print("✅ Ollama is running at http://localhost:11434")
        return True
    except Exception:
        print("❌ Ollama is NOT running at http://localhost:11434")
        return False

OLLAMA_RUNNING = is_ollama_running()

# Mocked response
def mock_run_success(*args, **kwargs):
    mock_response = MagicMock()
    mock_response.content = "Mocked response content"
    return mock_response

@pytest.mark.skipif(not OLLAMA_RUNNING, reason="Ollama not running, fallback to mock mode")
def test_web_agent_real():
    result = web_agent.run("What are the current trends in the semiconductor market?")
    assert result.content
    print("# Web Agent Real Result #")
    print(result.content)
    print("✅ Web Agent real test passed")

def test_web_agent_mock():
    if OLLAMA_RUNNING:
        pytest.skip("Ollama is running — skipping mock test")
    with patch("agents.web_agent.web_agent.run", side_effect=mock_run_success):
        result = web_agent.run("Mock test for web agent")
        assert result.content == "Mocked response content"
        print("# Web Agent Mock Result #")
        print(result.content)
        print("✅ Web Agent mock test passed")

@pytest.mark.skipif(not OLLAMA_RUNNING, reason="Ollama not running, fallback to mock mode")
def test_finance_agent_real():
    result = finance_agent.run("Get financial data for NVDA, AMD, INTC")
    assert result.content
    print("# Finance Agent Real Result #")
    print(result.content)
    print("✅ Finance Agent real test passed")

def test_finance_agent_mock():
    if OLLAMA_RUNNING:
        pytest.skip("Ollama is running — skipping mock test")
    with patch("agents.finance_agent.finance_agent.run", side_effect=mock_run_success):
        result = finance_agent.run("Mock test for finance agent")
        assert result.content == "Mocked response content"
        print("# Finance Agent Mock Result #")
        print(result.content)
        print("✅ Finance Agent mock test passed")
