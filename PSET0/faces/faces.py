def main():
    # Prompt the user to enter a text
    txt = input("Please enter a text: ")
    
    # Call the convert function to replace emoticons with emojis
    converted_txt = convert(txt)
    
    # Print the converted text
    print("Converted text: ")
    print(converted_txt)

# Function to convert emoticons to emojis
# Replace :) with 🙂 and :( with 🙁 in the original text
def convert(orginal_text):
    converted_txt = orginal_text.replace(":)", "🙂").replace(":(", "🙁")
    return converted_txt

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
