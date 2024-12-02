def main():
    # Prompt the user for the plate input
    plate = input("Plate: ")
    
    # Check if the plate is valid using the is_valid function
    if is_valid(plate):
        print("Valid")  # If the plate is valid, print "Valid"
    else:
        print("Invalid")  # Otherwise, print "Invalid"


def is_valid(s):
    # Check if the plate length is between 2 and 6 and contains only alphanumeric characters
    if 2 <= len(s) <= 6 and s.isalnum():
        # If the plate is entirely alphabetic, it's valid
        if s.isalpha():
            return True
        # Check if the plate starts with letters and ends with digits
        elif s[:2].isalpha() and s[2:].isdigit():
            # Ensure the first digit is not 0
            if s[2] == "0":  # If the first number is 0, return False
                return False
            # Ensure that no letters come after digits
            for i in range(2, len(s)):
                if s[i].isalpha():  # If there's a letter after the number, return False
                    return False
            return True  # If all checks pass, return True
    return False  # If any condition fails, return False


if __name__ == "__main__":
    main()  # Start the program
