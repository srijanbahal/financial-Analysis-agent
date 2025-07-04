import os
# from crewai.llms import ChatLiteLLM  
from dotenv import load_dotenv
load_dotenv()

from crewai import LLM
# Load .env (make sure OPENROUTER_API_KEY is in there)
print("OpenRouter API Key:", os.getenv("OPENROUTER_API_KEY"))

# Use OpenRouter via LiteLLM
manager_llm = LLM(
    model="openrouter/mistralai/mistral-small-3.2-24b-instruct:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")  # Uses OPENROUTER_API_KEY from env
)

print(type(manager_llm))