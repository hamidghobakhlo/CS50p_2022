import csv  # Import the csv module to read and write CSV files
import sys  # Import sys module for handling command-line arguments and exit the program

# Main function to handle command-line arguments and initiate the cleaning process
def main():
    # Check if the number of command-line arguments is correct (exactly 2)
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")  # Exit with an error message if there are not enough arguments
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")  # Exit with an error message if there are too many arguments
    else:
        # Check if the first argument (input filename) ends with ".csv"
        if sys.argv[1][-4:] != ".csv":
            sys.exit("Not a CSV file")  # Exit with an error message if the file is not a CSV file
        else:
            # Call the clean function to process the input and output files
            clean(sys.argv[1], sys.argv[2])

# Function to clean the data in the CSV file and write it to a new CSV file
def clean(input, output):
    try:
        # Open the input CSV file for reading
        with open(input) as input:
            reader = csv.DictReader(input)  # Read the input file using a DictReader to handle rows as dictionaries

            # Open the output CSV file for writing
            with open(output, "w") as output:
                header = ["first", "last", "house"]  # Define the new header for the output file
                writer = csv.DictWriter(output, fieldnames=header)  # Create a DictWriter object for writing to the output file
                writer.writeheader()  # Write the header to the output file

                # Iterate through each row in the input file
                for student in reader:
                    # Split the 'name' field into 'last' and 'first' names
                    last, first = student["name"].split(", ")  # Assume names are in "Last, First" format
                    house = student["house"]  # Retrieve the house from the current row

                    # Write the cleaned data to the output file with the new format
                    writer.writerow({"first": first, "last": last, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {input}")  # Exit if the input file is not found

# Check if the script is being run as the main module
if __name__ == "__main__":
    main()  # Execute the main function when the script is run directly
