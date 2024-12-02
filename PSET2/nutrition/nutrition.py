# This program checks the calories of a given fruit from a predefined list of fruits.

# Step 1: Define the fruit list
# The list `fruits` contains dictionaries, where each dictionary represents:
# - "fruit": The name of the fruit.
# - "calories": The calorie count of the fruit.
fruits = [
    {"fruit": "apple", "calories": "130"},
    {"fruit": "avocado", "calories": "50"},
    {"fruit": "banana", "calories": "110"},
    {"fruit": "cantaloupe", "calories": "50"},
    {"fruit": "grapefruit", "calories": "60"},
    {"fruit": "grapes", "calories": "90"},
    {"fruit": "honeydew melon", "calories": "50"},
    {"fruit": "kiwifruit", "calories": "90"},
    {"fruit": "lemon", "calories": "15"},
    {"fruit": "lime", "calories": "20"},
    {"fruit": "nectarine", "calories": "60"},
    {"fruit": "orange", "calories": "80"},
    {"fruit": "peach", "calories": "60"},
    {"fruit": "pear", "calories": "100"},
    {"fruit": "pineapple", "calories": "50"},
    {"fruit": "plums", "calories": "70"},
    {"fruit": "strawberries", "calories": "50"},
    {"fruit": "sweet cherries", "calories": "100"},
    {"fruit": "tangerine", "calories": "50"},
    {"fruit": "watermelon", "calories": "80"},
]

# Step 2: Get user input
# The user is prompted to input the name of a fruit.
# The input is stripped of extra whitespace and converted to lowercase for consistent comparison.
inpt = input("Input: ").strip().lower()

# Step 3: Search for the fruit in the list
# Iterate through the list of fruits to find a match for the user's input.
for find in fruits:
    if inpt == find["fruit"]:
        # If the fruit is found, print its calorie count.
        print(f"Calories: {find['calories']}")
        break  # Exit the loop once the match is found
