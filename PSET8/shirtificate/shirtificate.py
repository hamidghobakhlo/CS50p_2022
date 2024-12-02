from fpdf import FPDF

# Define the certificate class which extends FPDF
class Shirtificate(FPDF):
    
    # Custom header function for the certificate
    def header(self):
        # Set the font for the header (Arial, Bold, size 12)
        self.set_font("Arial", "B", 12)
        # Add a title to the header (centered)
        self.cell(0, 10, "Certificate of Completion", 0, 1, "C")

    # Custom footer function for the certificate
    def footer(self):
        # Position the footer 1.5 cm from the bottom of the page
        self.set_y(-15)
        # Set the font for the footer (Arial, Italic, size 8)
        self.set_font("Arial", "I", 8)
        # Add page number to the footer (centered)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    # Function to generate the certificate with the user's name
    def generate_certificate(self, name):
        # Add the image as background (filename: "shirtificate.png")
        # Set the image dimensions to fit the full A4 page size (210 x 297 mm)
        self.image("shirtificate.png", x=0, y=0, w=210, h=297)
        # Set the font for the name (Arial, Bold, size 24)
        self.set_font("Arial", "B", 24)
        # Add the user's name in the center of the page
        self.cell(0, 60, name, 0, 1, "C")  # Position the name 60mm from the top and center it

# Prompt the user for their name
name = input("Enter your name: ")

# Create a new Shirtificate object (certificate)
certificate = Shirtificate()
# Add a page to the certificate
certificate.add_page()
# Generate the certificate with the provided name
certificate.generate_certificate(name)
# Output the certificate as a PDF file named "shirtificate.pdf"
certificate.output("shirtificate.pdf")
