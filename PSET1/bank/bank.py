# This program determines a response cost based on the user's greeting.

# Step 1: Get user input
# The user is prompted to input a greeting. 
# The input is stripped of extra whitespace and converted to lowercase for consistent comparison.
a = input("Greeting:").strip().lower()

# Step 2: Check the greeting
# The program evaluates the greeting using conditional statements:
if a.startswith("hello"):
    # If the greeting starts with "hello", the cost is set to $0.
    a = 0
elif a.startswith("h"):
    # If the greeting starts with any word beginning with "h" (but not "hello"), the cost is $20.
    a = 20
else:
    # If the greeting doesn't start with "h", the cost is $100.
    a = 100

# Step 3: Output the result
# The program prints the determined cost in a formatted string with a "$" prefix.
print(f"${a}")
