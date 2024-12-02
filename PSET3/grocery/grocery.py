from collections import defaultdict

def main():
    # Initialize grocery list with default integer value (0 for non-existent keys)
    grocery_list = defaultdict(int)

    try:
        # Keep reading inputs indefinitely
        while True:
            # Take input, remove leading/trailing whitespace, and convert to lowercase
            item = input().strip().lower()
            # Increment the count of the item in the grocery list
            grocery_list[item] += 1
    except EOFError:
        # Exit loop when end of input (Ctrl+D) is reached
        pass

    # Sort items alphabetically by their name (first element of the tuple)
    sorted_items = sorted(grocery_list.items(), key=lambda x: x[0])

    # Print each item and its count in uppercase
    for item, count in sorted_items:
        print(f"{count} {item.upper()}")

# Start the program if it's being run directly
if __name__ == "__main__":
    main()
