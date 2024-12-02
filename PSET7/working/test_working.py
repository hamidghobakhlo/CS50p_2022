import pytest
from working import convert

# Test valid time conversions from AM/PM to 24-hour format
def test_convert():
    # Test conversion from "9 AM to 5 PM"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"  
    # Test conversion from "9:00 AM to 5:00 PM"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    # Test conversion from "10 PM to 8 AM"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    # Test conversion from "10:30 PM to 8:50 AM"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"

# Test cases for invalid inputs, expecting a ValueError
def test_value_error():
    # Invalid input due to missing spaces between time and AM/PM
    with pytest.raises(ValueError):
        convert("9AM - 5PM")  
    # Invalid input because the format is already 24-hour time, which the function shouldn't accept
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    # Invalid input with an incorrect AM/PM combination (15:00 AM is not valid)
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")
    # Invalid input due to non-existent time (9:60 AM and 5:60 PM)
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
