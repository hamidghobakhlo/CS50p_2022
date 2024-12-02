# Define a dictionary to map codes and aliases to emojis
emoji_dict = {
    ":thumbs_up:": "👍",  # Map ":thumbs_up:" to the thumbs-up emoji
    ":thumbsup:": "👍",  # Alias for thumbs-up
    ":1st_place_medal:": "🥇",  # Map ":1st_place_medal:" to the gold medal emoji
    ":money_bag:": "💰",  # Map ":money_bag:" to the money bag emoji
    ":smile_cat:": "😸",  # Map ":smile_cat:" to the smiling cat emoji
    ":candy:": "🍬"  # Map ":candy:" to the candy emoji
    # Add more mappings as needed
}

def emojize(input_str):
    """
    Function to replace emoji codes or aliases in a string with the corresponding emojis.
    :param input_str: A string that may contain emoji codes
    :return: The input string with codes replaced by emojis
    """
    # Loop through the dictionary and replace codes or aliases with emojis
    for code, emoji in emoji_dict.items():
        input_str = input_str.replace(code, emoji)  # Replace each code with its corresponding emoji

    return input_str  # Return the modified string

# Prompt the user for input
user_input = input("Enter a string in English: ")  # Get a string from the user

# Call the emojize function to convert emojis
emojized_string = emojize(user_input)  # Convert any emoji codes in the input to emojis

# Output the emojized string
print("Output:", emojized_string)  # Print the string with emojis

# Example of using the "emoji" library for comparison (commented out)
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
