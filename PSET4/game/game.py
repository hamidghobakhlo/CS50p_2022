import random  # Import the random module for generating random numbers

def get_positive_integer(prompt):
    """
    Prompt the user for a positive integer until a valid input is received.
    :param prompt: The message to display when asking for input
    :return: A positive integer entered by the user
    """
    while True:  # Repeat until a valid input is provided
        try:
            num = int(input(prompt))  # Try to convert the input to an integer
            if num <= 0:  # Check if the number is not positive
                raise ValueError("Please enter a positive integer.")  # Raise an exception for invalid input
            return num  # Return the valid positive integer
        except ValueError:  # Catch invalid input (non-integers or negative numbers)
            print("Invalid input. Please enter a positive integer.")  # Print an error message

def main():
    """
    Main function for the Number Guessing Game.
    """
    print("Welcome to the Number Guessing Game!")  # Print a welcome message

    # Get the difficulty level (upper bound for random number generation)
    level = get_positive_integer("Enter the level (a positive integer): ")

    # Generate a random target number between 1 and the chosen level
    target_number = random.randint(1, level)

    # Inform the user about the range of numbers
    print(f"I'm thinking of a number between 1 and {level}.")

    while True:  # Loop until the user guesses the correct number
        # Prompt the user for their guess
        guess = get_positive_integer("What is your guess? ")

        # Provide feedback based on the guess
        if guess < target_number:  # If the guess is too low
            print("Too small!")
        elif guess > target_number:  # If the guess is too high
            print("Too large!")
        else:  # If the guess is correct
            print("Just right!")
            break  # Exit the loop and end the game

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()  # Call the main function
