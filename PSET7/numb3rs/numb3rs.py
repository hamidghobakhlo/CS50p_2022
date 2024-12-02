def main():
    # Ask the user to input an IPv4 address
    ip = input("IPv4 Address: ")
    
    # Call the validate function to check if the input is a valid IPv4 address
    result = validate(ip)
    
    # Print the result of the validation (True or False)
    print(result)

def validate(ip):
    # Split the input IP address into its four components using dot as a delimiter
    components = ip.split(".")

    # Check if there are exactly 4 components in the IP address (i.e., "xxx.xxx.xxx.xxx")
    if len(components) != 4:
        return False  # Invalid if there are not exactly 4 components

    for component in components:
        # Check if each component is a valid number (all characters should be digits)
        if not component.isdigit():
            return False  # Invalid if the component contains non-numeric characters

        # Check if the component is within the valid range for each part of the IPv4 address (0-255)
        if not 0 <= int(component) <= 255:
            return False  # Invalid if the component is not between 0 and 255

    # If all checks pass, return True indicating the IP address is valid
    return True

# Ensure the script only runs if it's executed directly (not imported)
if __name__ == "__main__":
    main()  # Execute the main function when the script is run directly
