# import os



# key1 = get_openai_api_key()

# print(get_openai_api_key())
# print(get_serper_api_key())


from dotenv import load_dotenv
import os

# Load from .env file
load_dotenv()
def get_google_api_key():
    return os.getenv("GOOGLE_API_KEY")

def get_serper_api_key():
    return os.getenv("SERPER_API_KEY")

# # Access variables
# openai_key = os.getenv("OPENAI_API_KEY")
# serper_key = os.getenv("SERPER_API_KEY")

# # Example usage in function
# def call_apis():
#     print("OpenAI Key:", openai_key)
#     print("Serper Key:", serper_key)

# call_apis()


print("OpenRouter API Key:", os.getenv("OPENROUTER_API_KEY"))
