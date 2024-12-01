# Dictionary mapping file extensions to MIME types
h = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",  # Corrected "text/pain" to "text/plain"
    "zip": "application/zip"
}

# Prompt the user for a file name, stripping extra spaces and converting to lowercase
p = input("File name: ").strip().lower()

# Check if the input contains a file extension
if p.rfind(".") != -1:
    # Extract the file extension
    index = int(p.rindex(".")) + 1
    b = p[index:]
else:
    # If no extension is found, default to "application/octet-stream"
    print("application/octet-stream")
    exit()  # Exit the program since no valid extension is found

# Check if the file extension exists in the dictionary
if b not in h:
    # If not found, default to "application/octet-stream"
    print("application/octet-stream")
else:
    # Print the corresponding MIME type
    print(h[b])
