def main():
    # Prompt the user for input and call the count function to count occurrences of "um"
    print(count(input("Text: ")))

def count(s):
    # Import the re module for regular expressions
    import re

    # Use regular expressions to find all occurrences of "um" as a whole word
    # \b is a word boundary, so it ensures that "um" is a standalone word
    # re.IGNORECASE makes the search case-insensitive
    um_matches = re.findall(r'\bum\b', s, re.IGNORECASE)

    # Count the number of matches found
    um_count = len(um_matches)

    return um_count

if __name__ == "__main__":
    # Run the main function when the script is executed directly
    main()
