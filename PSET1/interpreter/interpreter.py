# This program is a simple calculator that takes a mathematical expression 
# as input, evaluates it, and prints the result with one decimal place.

# Step 1: Input the expression
# The user is prompted to enter a mathematical expression in the format "x y z",
# where x and z are numbers, and y is an operator (+, -, *, or /).
x, y, z = input("Enter an expression: ").strip().split()

# Step 2: Match the operator
# Using a match-case block, the program checks the operator (y) and performs 
# the corresponding arithmetic operation on the numbers (x and z).
match y:
    case "+":
        answer = float(x) + float(z)  # Addition
    case "-":
        answer = float(x) - float(z)  # Subtraction
    case "*":
        answer = float(x) * float(z)  # Multiplication
    case "/":
        answer = float(x) / float(z)  # Division

# Step 3: Output the result
# The result of the calculation is printed with one decimal place.
print(f"{answer:.1f}")

"""
-----------------------------OR--------------------------------
# Alternative implementation using if-elif statements
# This is functionally equivalent to the match-case approach.
if y == "+":
    answer = float(x) + float(z)  # Addition
elif y == "-":
    answer = float(x) - float(z)  # Subtraction
elif y == "*":
    answer = float(x) * float(z)  # Multiplication
elif y == "/":
    answer = float(x) / float(z)  # Division

# Output the result with one decimal place.
print(f"{answer:.1f}")
"""
