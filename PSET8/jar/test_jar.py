from jar import Jar  # Import the Jar class for testing

# Test for the initialization of the Jar class
def test_init():
    jar = Jar()  # Create a new jar with the default capacity
    assert jar.capacity == 12  # Verify the jar's capacity is 12 by default

# Test for the string representation of the Jar class
def test_str():
    jar = Jar()  # Create a new jar
    jar.deposit(3)  # Deposit 3 cookies into the jar
    assert str(jar) == "🍪🍪🍪"  # Verify that the string representation matches 3 cookies (🍪🍪🍪)

# Test for the deposit method of the Jar class
def test_deposit():
    jar = Jar()  # Create a new jar
    jar.deposit(5)  # Deposit 5 cookies into the jar
    assert jar.size == 5  # Verify that the size of the jar is now 5 cookies

    # Test exceeding capacity, which should raise an exception
    try:
        jar.deposit(10)  # Attempt to deposit more cookies than the jar's capacity
    except ValueError as e:
        assert str(e) == "Exceeds the jar's capacity"  # Ensure the correct error message is raised

# Test for the withdraw method of the Jar class
def test_withdraw():
    jar = Jar()  # Create a new jar
    jar.deposit(5)  # Deposit 5 cookies into the jar
    jar.withdraw(2)  # Withdraw 2 cookies from the jar
    assert jar.size == 3  # Verify that the jar now contains 3 cookies

    # Test withdrawing more cookies than are available, which should raise an exception
    try:
        jar.withdraw(4)  # Attempt to withdraw more cookies than available
    except ValueError as e:
        assert str(e) == "Not enough cookies in the jar"  # Ensure the correct error message is raised

# If the script is run directly, execute the tests using pytest
if __name__ == "__main__":
    import pytest  # Import pytest for testing
    pytest.main()  # Run the tests
