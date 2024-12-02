# This program converts a string from camelCase to snake_case.

# Step 1: Get user input
# The user is prompted to enter a string in camelCase format.
inp = input("camelcase: ").strip()

# Step 2: Initialize an empty string to store the result
temp = ""

# Step 3: Iterate through each character in the input string
for find in inp:
    if find.isupper():
        # If the character is uppercase, append an underscore followed by the lowercase version of the character
        temp += "_"
        temp += find.lower()
    else:
        # If the character is not uppercase, append it as is
        temp += find

# Step 4: Output the result
# Print the converted string in snake_case format
print(f"snake_case: {temp}")
