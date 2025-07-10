# file that brings all the components together for now

# importing the call_api for now just testing this functionality
from src.gpioHandlers.call_api import setup_gpio
from signal import pause

# main function to start the program
def main():
    # 1. intialize the hardware
    button = setup_gpio()

    # 2. print that we are working and awaiting button press
    print("Button connected awaiting button press...")

    # 3. pause so the script can wait for input
    pause()

# run the script if this is the main file ran 
if __name__ == "__main__":
    main()

