from random import randint  # Import randint for generating random numbers

# Define a list of dictionaries where each level maps to a range of numbers
levellist = [{1: [0, 9]}, {2: [10, 99]}, {3: [100, 999]}]

def main():
    """
    Main function to run the math quiz game.
    """
    # Get the difficulty level from the user
    slevel = get_level()
    
    # Generate a set of math problems based on the chosen level
    pset = generate_integer(slevel)

    done = 0  # Counter to track the number of correct answers

    # Loop through each question in the problem set
    for question in pset:
        life = 0  # Counter for incorrect attempts for a single question
        a, b = question.split("+")  # Split the question to extract numbers
        result = int(a) + int(b)  # Calculate the correct answer

        while True:
            try:
                # Prompt the user for their answer
                ans = int(input(f"{question} = "))

                if ans != result:  # If the answer is incorrect
                    life += 1  # Increment the attempt counter
                    print("EEE")  # Display error message
                else:  # If the answer is correct
                    done += 1  # Increment the correct answer counter
                    life = 0  # Reset the life counter
                    break  # Exit the loop for this question

                if life == 3:  # If the user fails 3 attempts
                    print(f"{question} = {result}")  # Show the correct answer
                    break  # Move to the next question
            except ValueError:  # Handle non-integer inputs
                print("EEE")
                life += 1  # Count the invalid attempt
                continue

    # Display the total score at the end of the game
    print(f"Score: {done}")

def get_level():
    """
    Prompt the user to choose a difficulty level (1, 2, or 3).
    :return: The chosen level as an integer
    """
    while True:
        try:
            level = int(input("Level: "))  # Get input and try to convert to an integer
            if 1 <= level <= 3:  # Ensure the level is valid (1, 2, or 3)
                return level  # Return the valid level
            else:
                # If the level is out of bounds, show an error message
                print("Little Professor rejects invalid level")
        except ValueError:  # Handle non-integer inputs
            print("Little Professor rejects invalid level")

def generate_integer(level):
    """
    Generate a list of math problems for the given difficulty level.
    :param level: The chosen level (1, 2, or 3)
    :return: A list of math problems as strings (e.g., "2 + 3")
    """
    pset = []  # Initialize an empty list to store the problems

    # Get the range of numbers for the chosen level
    lower = levellist[level - 1][level][0]
    higher = levellist[level - 1][level][1]

    # Generate 10 random addition problems
    for _ in range(10):
        # Create a problem as a string (e.g., "4 + 7")
        pset.append(f"{randint(lower, higher)} + {randint(lower, higher)}")

    return pset  # Return the list of problems

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
