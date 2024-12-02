# This program simulates a vending machine transaction where the user inserts coins 
# until the required amount is paid, and any change owed is calculated.

# Step 1: Initialize variables
# `money` is the total cost of the item (50 cents).
# `pay` keeps track of the total amount the user has inserted so far.
money = 50
pay = 0

# Step 2: Process coin insertion using a while loop
# Continue prompting the user for coins until the total inserted amount (`pay`) meets or exceeds the cost (`money`).
while pay < money:
    # Display the amount still owed (negative value of `pay - money`).
    print(f"Amount Due: {money - pay}")
    
    # Prompt the user to insert a coin. The coin must be a valid denomination (25, 10, or 5 cents).
    inpt = int(input("Next coin:").strip())
    
    if inpt == 25 or inpt == 10 or inpt == 5:
        # If the coin is valid, add its value to the total amount paid (`pay`).
        pay += inpt
    else:
        # If the coin is invalid, ignore it and continue the loop.
        continue

# Step 3: Calculate and display the change owed
# Once the loop exits, the user has either met or exceeded the required amount (`money`).
print(f"Change Owed: {pay - money}")
