from datetime import date  # Import date class from datetime to handle date operations
import inflect  # Import the inflect library to convert numbers to words
import sys  # Import sys for system exit in case of errors
import operator  # Import operator for performing the date difference operation

p = inflect.engine()  # Initialize the inflect engine to convert numbers to words


def main():
    try:
        dob = input("Date of Birth: ")  # Ask the user to input their date of birth
        # date.fromisoformat(dob) will check whether the dob is a valid date format
        difference = operator.sub(date.today(), date.fromisoformat(dob))  # Calculate the difference in days
        print(convert(difference.days))  # Convert the difference in days to minutes and print the result
    except ValueError:
        sys.exit("Invalid date")  # If there's an error in the date format, exit with a message


def convert(time):
    # Convert the time in days to minutes (24 hours * 60 minutes)
    minutes = time * 24 * 60
    # Use inflect's number_to_words method to convert the number of minutes to words, then capitalize it
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"  # Return the result in word format


if __name__ == "__main__":
    main()  # Run the main function when the script is executed
