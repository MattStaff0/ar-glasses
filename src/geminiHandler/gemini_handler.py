# file that gets the input from the user and will send the message to the gemini api and get the response back

# imports
from google import genai
from google.genai import types

client = genai.Client(api_key=)

def call_gemini_api(prompt):
    # making the response object
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="Respond in one word"
        )
    )
    
    return response.text
