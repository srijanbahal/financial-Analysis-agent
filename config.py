# To use Gemini (Google Generative AI), set your API key as follows:
# import os
# os.environ["GOOGLE_API_KEY"] = "your-google-api-key-here"
import os

OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME", "gpt-3.5-turbo")
SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")
os.getenv("GOOGLE_API_KEY")