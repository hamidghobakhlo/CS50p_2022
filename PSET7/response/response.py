import validators  # Import the validators module to validate the email address

def main():
    # Prompt the user for an email address and validate it
    print(validate(input("What's your email address? ")))  # Ask for email and print validation result

def validate(s):
    # Use the 'validators' module to check if the input is a valid email address
    if validators.email(s) == True:
        return f"Valid"  # Return "Valid" if the email is valid
    else:
        return f"Invalid"  # Return "Invalid" if the email is not valid

if __name__ == "__main__":
    main()  # Call the main function when the script is executed directly
