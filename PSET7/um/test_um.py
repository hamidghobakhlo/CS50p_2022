import um  # Import the um module (which should contain the count function)

def test_count():
    # Test cases to verify the count function works correctly
    assert um.count("um") == 1  # "um" appears once
    assert um.count("Hello, um, world") == 1  # "um" appears once
    assert um.count("This is, um... CS50.") == 1  # "um" appears once
    assert um.count("Um... what are regular expressions?") == 1  # "Um" appears once
    assert um.count("Um, thanks, um, regular expressions make sense now.") == 2  # "Um" appears twice
    assert um.count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2  # "Um" appears twice

if __name__ == "__main__":
    test_count()  # Run the test_count function when the script is executed directly
