import os
from dotenv import load_dotenv

load_dotenv(".env.example") #replace with your actual .env file if needed

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")

# print(f"Using Ollama model: {OLLAMA_MODEL}")
