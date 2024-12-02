import sys  # Import the sys module to work with command-line arguments
import requests  # Import the requests module to make HTTP requests

# API endpoint for fetching Bitcoin price in USD
apilink = "https://api.coindesk.com/v1/bpi/currentprice.json"

def main():  
    # Print the converted Bitcoin value formatted to 4 decimal places
    print(f"${coindesk(testinput()):,.4f}")

def testinput():
    """
    Function to validate and process the command-line input.
    Ensures the input is a number and returns it as a float.
    """
    try:
        # Check if a command-line argument is provided
        if len(sys.argv) < 2:
            print("Missing command-line argument")  # Error message for missing input
            sys.exit(1)  # Exit the program with status 1 (error)

        # Check if the argument is a valid number
        elif not float(sys.argv[1]):
            print("Command-line argument is not a number")  # Error message for invalid input
            sys.exit(1)  # Exit the program with status 1 (error)

        else:
            return float(sys.argv[1])  # Convert the argument to float and return it
    except (TypeError, ValueError):  # Catch errors if the input cannot be converted to float
        print("Command-line argument is not a number")  # Error message
        sys.exit(1)  # Exit the program with status 1 (error)

def coindesk(uninput):
    """
    Function to fetch the current Bitcoin price in USD and calculate the equivalent value.
    """
    try:
        # Make a GET request to the API to fetch Bitcoin price data
        response = requests.get(apilink)

        # Parse the response JSON
        a = response.json()

        # Extract the current Bitcoin price in USD
        b = a["bpi"]["USD"]["rate_float"]

        # Multiply the input value (number of Bitcoins) by the price in USD
        c = uninput * b

    except requests.RequestException:  # Catch any request-related errors
        print("CONNECTION ERROR")  # Error message for connection issues
        sys.exit(1)  # Exit the program with status 1 (error)

    return c  # Return the calculated value

if __name__ == "__main__":  # Ensure the script runs only when executed directly
    main()  # Call the main function
