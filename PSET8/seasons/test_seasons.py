from seasons import convert  # Assuming the 'convert' function is defined in the 'seasons' module

def test_date():
    # Test Case 1: Convert 10477 minutes into words
    assert convert(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    
    # Test Case 2: Convert 365 minutes into words
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
