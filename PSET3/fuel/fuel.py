def calculate_fuel_percentage(fraction_str):
    """
    Convert a fraction string (e.g., "X/Y") into a fuel percentage.
    Return 'E' if the fuel level is nearly empty (≤1%), and 'F' if nearly full (≥99%).
    """
    try:
        # Split the input string into numerator and denominator
        numerator, denominator = map(int, fraction_str.split('/'))

        # Check for invalid inputs
        if denominator == 0 or numerator > denominator:
            raise ValueError

        # Calculate the percentage of fuel
        percentage = (numerator / denominator) * 100

        # Round the percentage to the nearest integer
        percentage = round(percentage)

        # Check if the tank is essentially empty or full
        if percentage <= 1:
            return 'E'
        elif percentage >= 99:
            return 'F'
        else:
            return f'{percentage}%'
    except (ValueError, ZeroDivisionError):
        # Handle invalid fraction or zero division gracefully
        return None

# Main program to continuously prompt for valid input
while True:
    fraction_input = input("Enter a fraction (X/Y): ").strip()
    result = calculate_fuel_percentage(fraction_input)
    if result is not None:
        print(result)
        break  # Exit the loop when valid input is provided
    else:
        print("Invalid input. Please try again.")
