def value(greeting):
    """
    This function checks the input greeting and returns an integer based on its contents.
    - Returns 0 if the greeting starts with "hello" (case-insensitive).
    - Returns 20 if the greeting starts with "h" but not "hello".
    - Returns 100 for all other cases.
    """
    greeting_lower = greeting.lower()  # Convert the greeting to lowercase for case-insensitive comparison
    
    if greeting_lower.startswith("hello"):  # Check if the greeting starts with "hello"
        return 0  # Return 0 if the greeting starts with "hello"
    elif greeting_lower.startswith("h"):  # Check if the greeting starts with "h" (but not "hello")
        return 20  # Return 20 if the greeting starts with "h"
    else:
        return 100  # Return 100 for all other cases
