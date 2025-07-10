# file that gets the input from the user and will send the message to the gemini api and get the response back

# imports
from google import genai
from google.genai import types

_client = genai.Client()

def call_gemini_api(prompt):
    # making the response object
    response = _client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="Respond in one word"
        )
    )
    
    return response.text