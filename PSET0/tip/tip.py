def main(): 
    # Prompt the user to enter the cost of the meal in dollars
    dollars = dollars_to_float(input("How much was the meal? ")) 
    
    # Prompt the user to enter the tip percentage
    percent = percent_to_float(input("What percentage would you like to tip? ")) 
    
    # Calculate the tip amount
    tip = dollars * percent 
    
    # Print the tip amount formatted to two decimal places
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove the leading '$' from the input string and convert it to a float
    d = d.replace('$', '')
    return float(d)

def percent_to_float(p):
    # Remove the trailing '%' from the input string and convert it to a float
    p = p.replace('%', '')
    # Convert the percentage value into a decimal
    return float(p) / 100

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
