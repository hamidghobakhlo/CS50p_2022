import pytest
from fuel import convert, gauge  # Import the functions to be tested from the 'fuel' module

# Test cases for the 'convert' function with valid inputs
def test_convert_valid():
    # Test valid fractions and their expected percentage results
    assert convert("1/2") == 50  # 1/2 should return 50%
    assert convert("3/4") == 75  # 3/4 should return 75%
    assert convert("5/5") == 100  # 5/5 should return 100%

# Test cases for the 'convert' function with invalid inputs
def test_convert_invalid():
    # Test invalid inputs and ensure proper exceptions are raised
    with pytest.raises(ZeroDivisionError):  # Expect ZeroDivisionError for denominator 0
        convert("1/0")
    with pytest.raises(ValueError):  # Expect ValueError for fraction greater than 1 (e.g., 2/1)
        convert("2/1")
    with pytest.raises(ValueError):  # Expect ValueError for non-integer values (e.g., 2.5/3)
        convert("2.5/3")
    with pytest.raises(ValueError):  # Expect ValueError for non-integer values (e.g., 3/2.5)
        convert("3/2.5")

# Test cases for the 'gauge' function when percentage is at or below 1% (empty gauge)
def test_gauge_E():
    # Expect "E" (empty) for percentages 0 or below
    assert gauge(0) == "E"  
    assert gauge(1) == "E"  
    assert gauge(0.5) == "E"  # Just below 1% should also show "E"

# Test cases for the 'gauge' function when percentage is at or above 99% (full gauge)
def test_gauge_F():
    # Expect "F" (full) for percentages 99% and above
    assert gauge(99) == "F"  
    assert gauge(100) == "F"  
    assert gauge(101) == "F"  # Just above 100% should also show "F"

# Test cases for the 'gauge' function with valid percentages in the middle range
def test_gauge_percentage():
    # Expect the percentage as a string for values between 1 and 99%
    assert gauge(50) == "50%"  # 50% should return "50%"
    assert gauge(75) == "75%"  # 75% should return "75%"

# Run the tests when the script is executed directly
if __name__ == "__main__":
    pytest.main()  # Calls pytest to run the test cases
