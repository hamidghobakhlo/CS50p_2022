import re

# Main function that takes user input for time range and prints the converted result
def main():
    # Ask for user input and pass it to the convert function
    print(convert(input("Hours: ")))

# Function to convert time from AM/PM format to 24-hour format
def convert(s):
    # Regular expression to match time in AM/PM format (e.g., "9 AM to 5 PM")
    regex = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    
    # Search for the pattern "hours:minutes AM/PM to hours:minutes AM/PM"
    match = re.search(r"^" + regex + " to " + regex + "$", s)
    
    if match:
        # If a match is found, standardize both the start and end time to 24-hour format
        from_time = standardize(match.group(1), match.group(2), match.group(3))  # From time
        time = standardize(match.group(4), match.group(5), match.group(6))  # To time
        
        # Return the result in "24-hour format to 24-hour format" form
        return f"{from_time} to {time}"
    else:
        # If no match is found, raise a ValueError (invalid format)
        raise ValueError

# Function to convert a single time value from AM/PM to 24-hour format
def standardize(hr, min, x):
    # If the hour is 12 (special case for AM/PM), handle it separately
    if hr == "12":
        if x == "AM":
            hour = "00"  # 12 AM is midnight, represented as "00"
        else:
            hour = "12"  # 12 PM is noon, represented as "12"
    else:
        # For AM hours, just pad with zero if needed
        # For PM hours, add 12 to convert to 24-hour format
        if x == "AM":
            hour = f"{int(hr):02}"  # Ensure hour is two digits (e.g., "03" instead of "3")
        else:
            hour = f"{int(hr)+12}"  # Convert PM hour to 24-hour format
    
    # If minutes are not provided, default to "00"
    if min == None:
        minute = "00"
    else:
        # Ensure minutes are two digits
        minute = f"{int(min):02}"
    
    # Return the formatted time in 24-hour format
    return f"{hour}:{minute}"

# Call main if this script is executed directly
if __name__ == "__main__":
    main()
