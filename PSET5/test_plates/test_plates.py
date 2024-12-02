from plates import is_valid  # Import the is_valid function from the plates module

# Test case: Plates must start with at least two letters
def test_begintwoletters():
    # Check valid plate: starts with two letters
    assert is_valid("CS") == True
    # Check invalid plate: starts with digits
    assert is_valid("50") == False
    # Check invalid plate: starts with a letter and digit (invalid first character)
    assert is_valid("C5") == False
    # Check invalid plate: only one character
    assert is_valid("5") == False


# Test case: Plates must be between 2 and 6 characters in length
def test_length():
    # Check valid plate: length is within the allowed range
    assert is_valid("HICS50") == True
    # Check valid plate: length is 2 characters
    assert is_valid("CS") == True
    # Check invalid plate: length exceeds 6 characters
    assert is_valid("HELLOCS50") == False


# Test case: Numbers must be at the end of the plate and cannot start with '0'
def test_num():
    # Check valid plate: numbers at the end
    assert is_valid("AAA222") == True
    # Check invalid plate: numbers are in the middle
    assert is_valid("AAA22A") == False
    # Check invalid plate: numbers start with '0'
    assert is_valid("AAA022") == False


# Test case: No punctuation marks, spaces, or special characters allowed
def test_punct():
    # Check invalid plate: contains a special character ('!')
    assert is_valid("CS50!") == False
