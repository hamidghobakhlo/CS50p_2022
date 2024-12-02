import sys  # Import the sys module for handling command-line arguments
from random import choice  # Import choice to randomly select fonts (not used in this script)
from pyfiglet import Figlet  # Import Figlet from the pyfiglet library for text rendering

def print_usage_and_exit():
    """
    Print an error message for invalid usage and exit the program.
    """
    print("Invalid usage")  # Display error message
    sys.exit(1)  # Exit the program with a non-zero status (indicating an error)

# Create an instance of the Figlet class
fnt = Figlet()

# Retrieve the list of available fonts
fontlist = fnt.getFonts()

# Check the number of command-line arguments provided
if len(sys.argv) == 1:  # If no arguments are provided (besides the script name)
    inpt = input("Input: ").strip()  # Prompt the user for input text and remove any extra spaces
    print(fnt.renderText(inpt))  # Render the text in the default font and print it

elif len(sys.argv) == 3:  # If exactly 3 arguments are provided
    # Check if the first argument is a valid flag and the second is a valid font name
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fontlist:
        inpt = input("Input: ").strip()  # Prompt the user for input text
        fnt.setFont(font=sys.argv[2])  # Set the font based on the user-specified font
        print(fnt.renderText(inpt))  # Render the text in the chosen font and print it
    else:
        print_usage_and_exit()  # If the arguments are invalid, show error and exit
else:
    # If the number of arguments is not 1 or 3, show error and exit
    print_usage_and_exit()
