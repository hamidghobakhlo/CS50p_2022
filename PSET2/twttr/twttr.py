# This program removes vowels from a given input string.

# Step 1: Define a list of vowels
# The `v` list contains all the vowels (both uppercase and lowercase will be handled later).
v = ["a", "o", "u", "i", "e"]

# Step 2: Get user input
# The user is prompted to input a string.
inpt = input("input: ").strip()

# Step 3: Initialize an empty string to store the result
temp = ""

# Step 4: Iterate through each character in the input
for find in inpt:
    # Check if the character is not a vowel (case-insensitive)
    if find.lower() not in v:
        temp += find  # Append non-vowel characters to `temp`

# Step 5: Output the result
# Print the modified string after removing all vowels
print(f"output: {temp}")
