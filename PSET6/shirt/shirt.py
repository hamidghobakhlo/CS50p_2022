from PIL import Image, ImageOps  # Import Image and ImageOps from PIL (Pillow) for image manipulation
import sys  # Import sys module for handling command-line arguments and exit the program
import os  # Import os module for file path operations

# Main function to handle command-line arguments and initiate the image processing
def main():
    # Check if the number of command-line arguments is correct (exactly 2)
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")  # Exit with an error message if there are not enough arguments
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")  # Exit with an error message if there are too many arguments
    else:
        # Define valid image formats for input and output files
        format = [".jpg", ".jpeg", ".png"]
        
        # Split the input and output filenames and their extensions
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])

        # Check if the output file extension is valid
        if outp[1].lower() not in format:
            sys.exit("Invalid output")  # Exit with an error message if the output extension is invalid

        # Check if the input and output file extensions are the same
        elif inp[1].lower() != outp[1].lower():
            sys.exit("Input and output have different extensions")  # Exit with an error message if the extensions don't match
        else:
            # Call the function to process the image with the specified input and output filenames
            edit_photo(sys.argv[1], sys.argv[2])

# Function to edit the photo: crop and paste a shirt image onto the input photo
def edit_photo(input, output):
    try:
        # Open the shirt image that will be pasted onto the input image
        shirt = Image.open("shirt.png")

        # Open the input image and crop it to match the shirt's size
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)  # Fit the input image to the shirt's size
            input_cropped.paste(shirt, mask=shirt)  # Paste the shirt image onto the input image using the shirt as a mask
            input_cropped.save(output)  # Save the modified image to the output file

    except FileNotFoundError:
        sys.exit(f"Input does not exist")  # Exit with an error message if the input image file is not found

# Ensure the script only runs if it's executed directly (not imported)
if __name__ == "__main__":
    main()  # Execute the main function when the script is run directly
