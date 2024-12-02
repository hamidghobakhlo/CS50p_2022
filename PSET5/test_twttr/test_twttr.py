import twttr  # Import the twttr module, which contains the shorten function

# Test case: Check behavior when the input string has no vowels
def test_shorten_no_vowels():
    # Check if the vowels ('e' and 'o') are removed from 'hello'
    assert twttr.shorten("hello") == "hll"  # No vowels in the input
    # Check if vowels are removed from 'Python', leaving 'Pythn'
    assert twttr.shorten("Python") == "Pythn"  # Vowels are removed

# Test case: Check behavior when the input string contains only vowels
def test_shorten_only_vowels():
    # Check if all vowels are removed, resulting in an empty string
    assert twttr.shorten("AEIOUaeiou") == ""  # Only vowels in the input

# Test case: Check behavior when the input string is empty
def test_shorten_empty_string():
    # Check if the empty string remains empty after shortening
    assert twttr.shorten("") == ""  # Empty string remains empty

# Test case: Check behavior when the input string has no vowels to remove
def test_shorten_no_changes():
    # 'rhythm' has no vowels, so it should remain unchanged
    assert twttr.shorten("rhythm") == "rhythm"  # No vowels to remove

# Test case: Check behavior when the input string contains mixed-case vowels
def test_shorten_mixed_case():
    # Test mixed case input ('aBiOu'), should remove 'a', 'i', and 'o', leaving 'B'
    assert twttr.shorten("aBiOu") == "B"  # Mix of upper and lower case vowels

# Test case: Check behavior when the input string contains numbers
def test_shorten_numbers():
    # Numbers should not be affected by the vowel-removal process
    assert twttr.shorten("12345") == "12345"  # Make sure numbers are not removed

# Test case: Check behavior when the input string contains punctuation
def test_shorten_punctuation():
    # Punctuation should remain unchanged as it's not affected by the vowel-removal logic
    assert twttr.shorten("!@#$") == "!@#$"  # Make sure punctuation is not removed
