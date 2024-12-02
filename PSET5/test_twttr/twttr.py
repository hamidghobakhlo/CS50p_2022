def shorten(word):
    # Define a string containing all vowels (both uppercase and lowercase)
    vowels = "AEIOUaeiou"
    
    # Create a new string by joining characters that are not vowels
    # Iterates through each character in the word and includes it if it's not in the vowels string
    return ''.join(char for char in word if char not in vowels)
