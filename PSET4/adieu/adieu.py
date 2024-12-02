def main():  # Define the main function
    names = []  # Create an empty list to store names

    # Prompt the user for names until they press Ctrl-D
    try:
        while True:  # Infinite loop to continuously prompt for input
            name = input("Name: ")  # Ask the user to enter a name
            names.append(name)  # Append the entered name to the list
    except EOFError:  # Catch the EOFError when the user presses Ctrl-D
        pass  # Exit the loop gracefully

    # Handle different cases for formatting the farewell message
    if len(names) == 1:  # If there is only one name in the list
        print(f"Adieu, adieu, to {names[0]}")  # Print farewell message for one name
    elif len(names) == 2:  # If there are exactly two names in the list
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")  # Print farewell with "and" between names
    elif len(names) >= 3:  # If there are three or more names in the list
        farewell = ", ".join(names[:-1])  # Join all but the last name with commas
        farewell += f", and {names[-1]}"  # Add "and" before the last name
        print(f"Adieu, adieu, to {farewell}")  # Print the formatted farewell message

if __name__ == "__main__":  # Ensure this script runs only when executed directly
    main()  # Call the main function
