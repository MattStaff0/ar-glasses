# file that gets the input from the user and will send the message to the gemini api and get the response back

# imports
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# 1. Load environment variables from .env
load_dotenv()  # looks for .env in your project root

# 2. Read your key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY not set in .env")

# 3. Make the client with the api key
client = genai.Client(api_key=api_key)

def call_gemini_api(prompt: str) -> str:
    # making the response object
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful agent for matthew stafford",
            thinking_config= types.ThinkingConfig(thinking_budget=0)
        )
    )
    
    return response.text
