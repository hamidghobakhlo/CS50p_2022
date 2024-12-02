# This program checks if a given license plate string is valid based on a set of rules.

# Step 1: Define a list of invalid symbols
# The `symbols` list contains characters that are not allowed in a valid license plate.
symbols = [" ", ".", "?", "!", ",", ":", ";", "(", ")", "[", "]", "'", "-", '"', "/", "\\", "`", "@", "#", "*"]

# Step 2: Define the main function
# The main function handles user input and output.
def main():
    plate = input("Plate: ").strip()  # Get the license plate input and remove leading/trailing spaces
    if is_valid(plate):  # Check if the plate is valid using the `is_valid` function
        print("Valid")  # Print "Valid" if the plate passes all checks
    else:
        print("Invalid")  # Print "Invalid" if any check fails

# Step 3: Define the validation function
# The `is_valid` function contains the rules for determining if a license plate is valid.
def is_valid(s):
    validated = ""  # This will store the "cleaned" version of the input for comparison
    numcheck = 0  # A counter to track whether numeric characters have started appearing

    # Rule 1: The length of the license plate must be between 2 and 6 characters.
    if len(s) >= 2 and len(s) <= 6:
        # Rule 2: The first two characters must be alphabetic.
        if s[0].isalpha() and s[1].isalpha():
            # Process each character in the input string
            for ch in s:
                # Rule 3: Symbols from the `symbols` list are not allowed.
                if ch not in symbols:
                    # Rule 4: Numbers are allowed only after the first non-numeric character.
                    if ch.isnumeric() and numcheck == 0 and ch != "0":
                        numcheck += 1  # Start counting numeric characters
                        validated += ch
                    elif ch.isnumeric() and numcheck > 0: 
                        numcheck += 1  # Continue counting numeric characters
                        validated += ch
                    # Rule 5: Alphabetic characters are allowed until numeric characters begin.
                    elif ch.isalpha() and numcheck == 0:
                        validated += ch

    # Compare the "cleaned" string with the original input. If they match, the plate is valid.
    if validated == s:
        return True
    else:
        return False

# Step 4: Run the main function
main()
