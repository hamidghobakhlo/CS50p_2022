# Menu dictionary storing food items and their prices
foodsmenu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

# Initialize the total cost to 0
total_cost = 0.00

# Function to display the total cost
def display_total():
    print(f"Total: ${total_cost:.2f}")

# Main program loop
try:
    while True:
        # Prompt the user for an item, strip spaces, and title-case the input
        i = input("Enter an item: \n").strip().title()

        # Check if the item is valid (exists in the menu)
        if i in foodsmenu:
            # Add the item's price to the total cost
            total_cost += foodsmenu[i]
            # Display the updated total
            display_total()
        else:
            # Inform the user if the item is invalid
            print("Invalid item. Please choose an item from the menu.")
except (EOFError, KeyError):
    # If the user presses Ctrl-D (EOF), gracefully exit the loop
    pass

# Display the final total when the user exits
display_total()
