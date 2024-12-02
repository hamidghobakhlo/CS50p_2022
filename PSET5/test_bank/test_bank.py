import bank  # Import the 'bank' module where the value function is defined

def test_value_hello():
    """
    Test case for greeting starting with "hello" (case-insensitive).
    """
    assert bank.value("Hello, World") == 0  # Should return 0 because it starts with "hello"

def test_value_h():
    """
    Test case for greeting starting with "h" but not "hello".
    """
    assert bank.value("Hi there!") == 20  # Should return 20 because it starts with "h"

def test_value_default():
    """
    Test case for greeting not starting with "h" or "hello".
    """
    assert bank.value("What's up?") == 100  # Should return 100 because it doesn't start with "h"

def test_value_case_insensitive():
    """
    Test case for greeting starting with "hello" in different cases.
    """
    assert bank.value("HELLO, World") == 0  # Should return 0 because it's case-insensitive

# You can add more test cases as needed.
