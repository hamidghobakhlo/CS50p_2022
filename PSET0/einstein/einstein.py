def main():
    # Prompt the user for mass in kilograms
    kgmass = int(input("Please enter mass in kilograms: "))

    # Speed of light in meters per second (constant value)
    speed_of_light = 300000000

    # Calculate energy using Einstein's equation E = mc^2
    energyjoules = kgmass * speed_of_light ** 2

    # Display the equivalent energy in Joules
    print("Equivalent energy in Joules:", energyjoules)

# Execute the main function when the script is run directly
if __name__ == "__main__":
    main()
