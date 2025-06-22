import os
from dotenv import load_dotenv
from agno.models.ollama import Ollama
from agno.models.google import Gemini

load_dotenv(".env") #refer .env.example to set configuration 

# Model-1: IF using Ollama model, uncomment the following line:
model_config = Ollama(id=os.getenv("OLLAMA_MODEL"), provider="Ollama")

# Model-2: IF using Google Gemini model, uncomment the following lines:
# os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
# model_config = Gemini(id=os.getenv("GEMINI_MODEL"), provider="Google")
