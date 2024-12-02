# Import the datetime library to handle date manipulation
from datetime import datetime

# List of month names for the second date format (Month Day, YYYY)
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

while True:
    # Prompt the user for a date input
    user_input = input("Enter a date (MM/DD/YYYY or Month Day, YYYY): ")

    try:
        # Remove leading and trailing spaces from the input
        user_input = user_input.strip()

        # Initialize a variable to store the parsed date object
        date_obj = None

        # Try parsing in MM/DD/YYYY format first
        try:
            date_obj = datetime.strptime(user_input, "%m/%d/%Y")
        except ValueError:
            pass  # If this format fails, continue to the next format

        # Try parsing the Month Day, YYYY format
        if date_obj is None:
            for month in months:
                if month in user_input:
                    user_input = user_input.replace(month, "").strip()  # Remove month name
                    # Construct the date string in the expected format
                    date_str = f"{month} {user_input}"
                    date_obj = datetime.strptime(date_str, "%B %d, %Y")
                    break  # Exit loop once date is successfully parsed

        # If a valid date object is created, format and print the result
        if date_obj is not None:
            formatted_date = date_obj.strftime("%Y-%m-%d")  # Format date as YYYY-MM-DD
            print(formatted_date)
            break  # Exit loop once a valid date is processed
        else:
            print("Invalid date format. Please enter a date in MM/DD/YYYY or Month Day, YYYY format.")

    except ValueError:
        # Handle any unexpected errors during date parsing
        print("Invalid date format. Please enter a date in MM/DD/YYYY or Month Day, YYYY format.")
