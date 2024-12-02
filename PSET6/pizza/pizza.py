import sys  # Import sys module to handle command-line arguments and exit program
import os   # Import os module (though it's not used in this specific script, it's useful for file operations)
import tabulate  # Import the tabulate module for printing data in a table format
import csv  # Import the csv module for reading CSV files

# Function to format a CSV file as a table and return it as a string
def format_csv_as_table(csv_filename):
    try:
        # Check if the file has a '.csv' extension
        if not csv_filename.endswith(".csv"):
            sys.exit("Not a CSV file")  # Exit if the file is not a CSV file

        # Open the CSV file for reading
        with open(csv_filename, newline='') as file:
            csv_reader = csv.reader(file)  # Create a CSV reader object
            headers = next(csv_reader)  # Get the header row (first row)
            data = list(csv_reader)  # Get the remaining rows as data

        # Use tabulate to format the data into a table
        table = tabulate.tabulate(data, headers, tablefmt="grid")

        return table  # Return the formatted table as a string

    except FileNotFoundError:
        sys.exit("File does not exist")  # Exit if the file is not found

# Main function to handle command-line arguments and invoke the table formatting function
def main():
    # Check if there is exactly one command-line argument (the CSV filename)
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")  # Exit if incorrect number of arguments

    csv_filename = sys.argv[1]  # Get the filename from the command-line argument

    # Call the format_csv_as_table function to get the formatted table
    table = format_csv_as_table(csv_filename)

    # Print the formatted table
    print(table)

# Check if the script is being run as the main module
if __name__ == "__main__":
    main()  # Execute the main function
