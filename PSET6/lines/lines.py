import sys  # Import sys module to handle command-line arguments and exit program
import os   # Import os module (although not used in this script, can be helpful for file operations)

# Function to count the lines of code in a Python file
def count_lines(filename):
    try:
        # Open the file for reading
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines in the file

        code_lines = 0  # Initialize a counter for lines of code

        # Loop through each line in the file
        for line in lines:
            stripped_line = line.strip()  # Remove leading and trailing spaces

            # Check if the line is not empty and does not start with a comment '#'
            if stripped_line and not stripped_line.startswith("#"):
                code_lines += 1  # Increment the counter for valid code lines

        return code_lines  # Return the total count of code lines

    except FileNotFoundError:
        # If the file does not exist, exit the program and display an error message
        sys.exit("File does not exist")

# Main function to handle command-line arguments and invoke the line counting function
def main():
    # Check if there is exactly one command-line argument (the filename)
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")  # Exit if incorrect number of arguments

    filename = sys.argv[1]  # Get the filename from the command-line argument

    # Check if the file has a '.py' extension
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")  # Exit if the file is not a Python file

    # Call the count_lines function to get the number of code lines
    lines_count = count_lines(filename)
    
    # Print the result with the filename and the count of code lines
    print(f"Lines of code (excluding comments and blank lines) in '{filename}': {lines_count}")

# Check if the script is being run as the main module
if __name__ == "__main__":
    main()  # Execute the main function
