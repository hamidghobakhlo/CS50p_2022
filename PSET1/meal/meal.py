def main():
    # Step 1: Define the schedule
    # A list of dictionaries where each dictionary contains:
    # - "meal": The name of the meal (e.g., "breakfast time").
    # - "start hour": The starting hour of the meal time (in 24-hour format).
    # - "end hour": The ending hour of the meal time (in 24-hour format).
    sch = [
        {"meal": "breakfast time", "start hour": 7, "end hour": 8},
        {"meal": "lunch time", "start hour": 12, "end hour": 13},
        {"meal": "dinner time", "start hour": 18, "end hour": 19},
    ]

    # Step 2: Get user input for the time
    # The user is asked to input the current time in the format "HH:MM a.m." or "HH:MM p.m.".
    time = input("What time is it? ")
    time = float(convert(time))  # Convert the input time to a float value in 24-hour format.

    # Step 3: Check which meal time it is
    # Iterate over the meal schedule and determine if the current time falls within any meal time range.
    for h in sch:
        if time >= float(h["start hour"]) and time <= float(h["end hour"]):
            print(h["meal"])  # Print the corresponding meal name if the time is in range.
        else:
            continue  # Skip to the next meal if the time doesn't match.

def convert(time):
    # Step 1: Initialize a variable to adjust for p.m. hours
    c = 0.0
    # Check if the time is in a.m. and remove the "a.m." suffix if present
    if time.rfind(" a.m.") != -1:
        time = time.replace(" a.m.", "")
    # Check if the time is in p.m., remove the "p.m." suffix, and adjust hours for 24-hour format
    elif time.rfind(" p.m.") != -1:
        time = time.replace(" p.m.", "")
        c = 12.0  # Add 12 hours for p.m. times

    # Step 2: Split the time into hours and minutes
    h, m = time.strip().split(":")
    # Convert the time into a float in 24-hour format
    # Formula: hours + (minutes / 60) + adjustment for p.m. (if any)
    t = float(h) + c + (float(m) / 60)

    return t  # Return the converted time

# Entry point for the program
if __name__ == "__main__":
    main()
