from gpiozero import Button
import src.geminiHandler.gemini_handler as gemini

# connecting to the button on the pi
call_api = Button(2)

# when the button is pressed run the function to call the api
def on_press():
    prompt = input("enter your prompt: ")
    answer = gemini.call_gemini_api(prompt)
    print("Gemini ->\n")
    print(answer)

call_api.when_pressed = on_press
