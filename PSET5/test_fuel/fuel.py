def convert(fraction):
    """
    Converts a fraction in X/Y format to a percentage.
    Raises a ValueError if the input is invalid.
    """
    try:
        # Split the input fraction into two parts: numerator (X) and denominator (Y)
        X, Y = map(int, fraction.split('/'))

        # Check for division by zero (denominator is 0)
        if Y == 0:
            raise ZeroDivisionError

        # Check if the fraction is greater than 1 (invalid fraction, e.g., 5/3)
        if X > Y:
            raise ValueError

        # Calculate the percentage value and round it to the nearest integer
        percentage = round((X / Y) * 100)

        # Ensure the percentage is within the valid range [0, 100]
        if percentage < 0 or percentage > 100:
            raise ValueError

        return percentage  # Return the calculated percentage

    except (ValueError, ZeroDivisionError):
        # Catch any ValueError or ZeroDivisionError and raise a new ValueError with a message
        raise ValueError("Invalid input")

def gauge(percentage):
    """
    Converts a percentage into a fuel gauge reading.
    - If percentage <= 1, return "E" for empty.
    - If percentage >= 99, return "F" for full.
    - Otherwise, return the percentage as a string.
    """
    if percentage <= 1:
        return "E"  # Return "E" if the percentage is 1 or less (empty)
    elif percentage >= 99:
        return "F"  # Return "F" if the percentage is 99 or greater (full)
    else:
        return f"{percentage}%"  # Return the percentage as a string, e.g., "50%"

def main():
    """
    Main function to prompt the user for a fuel fraction and display the gauge reading.
    """
    # Prompt the user to input a fraction in X/Y format (e.g., "3/4")
    fraction = input("Enter a fuel fraction in X/Y format: ")
    try:
        # Convert the input fraction to a percentage
        percentage = convert(fraction)

        # Get the fuel gauge reading based on the percentage
        result = gauge(percentage)

        # Output the fuel gauge reading
        print(f"The gauge reads: {result}")

    except ValueError as e:
        # Handle invalid input (e.g., improper fraction, negative values)
        print(f"Error: {e}")
    except ZeroDivisionError as e:
        # Handle division by zero (denominator is 0)
        print(f"Error: {e}")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
