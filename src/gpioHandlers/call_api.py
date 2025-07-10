from gpiozero import Button
from signal import pause
from src.geminiHandler.gemini_handler import call_gemini_api
# connecting to the button on the pi
call_api = Button(2)

# when the button is pressed run the function to call the api
def on_press():
    prompt = input("enter your prompt: ")
    answer = call_gemini_api(prompt)
    print("Gemini ->\n")
    print(answer)

call_api.when_pressed = on_press

pause()
