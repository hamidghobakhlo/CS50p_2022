"""In deep.py, implement a program that prompts the user for the answer to the Great Question of Life,
 the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. 
 Otherwise output No."""

# Create a list of valid answers to the Great Question
list_ans = ["42", "forty-two", "forty two"]

# Prompt the user for their answer to the Great Question and normalize input (remove extra spaces and convert to lowercase)
qt = input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip().lower()

# Check if the user's answer matches any of the valid answers
if qt in list_ans:
    # If the answer is correct, print "Yes"
    print("Yes")
else:
    # If the answer is incorrect, print "No"
    print("No")

