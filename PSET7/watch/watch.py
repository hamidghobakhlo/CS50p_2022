def parse(s):
    # Search for the src attribute within the HTML string
    start = s.find('src="')
    
    # If 'src="' is not found, return None as there is no source URL
    if start == -1:
        return None

    # Move past the src=" to the start of the URL
    start += 5  # The length of 'src="'
    
    # Find the next '"' which marks the end of the URL
    end = s.find('"', start)
    
    # If there is no closing quote, return None as the URL is invalid
    if end == -1:
        return None

    # Extract the URL from the src attribute
    url = s[start:end]

    # Check if the URL is a YouTube embed URL by looking for 'youtube.com/embed'
    if "youtube.com/embed" in url:
        # Extract the video ID by splitting the URL and getting the last part
        video_id = url.split("/")[-1]

        # Construct the shortened youtu.be URL
        youtu_be_url = f"https://youtu.be/{video_id}"
        
        # Return the shortened YouTube URL
        return youtu_be_url

    # If it's not a YouTube embed URL, return None
    return None

def main():
    # Prompt user for an HTML string input
    html = input("HTML: ")
    
    # Call the parse function with the input HTML
    result = parse(html)
    
    # Print the result, or 'None' if no valid URL was found
    if result:
        print(result)
    else:
        print("None")

# Ensure the script runs only when executed directly
if __name__ == "__main__":
    main()
