from gpiozero import Button
from signal import pause
from src.geminiHandler.gemini_handler import call_gemini_api

# when the button is pressed run the function to call the api
def on_press():
    '''
    Function that defines the on press attribute of the button\n
    Gets the user prompt from input\n
    Calls the Gemini api with the prompt\n 
    Prints the answer to stdout
    
    Args:
        None
        
    Return: 
        None
    '''
    prompt = input("enter your prompt: ")
    answer = call_gemini_api(prompt)
    print("Gemini ->", answer)

def setup_gpio():
    """
    Create the button, wire the handler, and return objects
    in case you need to inspect or clean them up.
    """
    button = Button(2)
    button.when_pressed = on_press
    return button