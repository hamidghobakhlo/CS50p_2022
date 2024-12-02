class Jar:
    # Constructor to initialize the jar with a given capacity (default 12)
    def __init__(self, capacity=12):
        # Ensure capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")
        
        # Initialize the capacity and set the initial cookie count to 0
        self._capacity = capacity
        self._cookies = 0

    # String representation of the jar (displays cookies as "🍪" emojis)
    def __str__(self):
        return "🍪" * self._cookies

    # Deposit a certain number of cookies into the jar
    def deposit(self, n):
        # Ensure that the number of cookies to deposit is not negative
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies")
        
        # Ensure that the deposit doesn't exceed the jar's capacity
        if self._cookies + n > self._capacity:
            raise ValueError("Exceeds the jar's capacity")
        
        # Add cookies to the jar
        self._cookies += n

    # Withdraw a certain number of cookies from the jar
    def withdraw(self, n):
        # Ensure that the number of cookies to withdraw is not negative
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies")
        
        # Ensure that there are enough cookies to withdraw
        if n > self._cookies:
            raise ValueError("Not enough cookies in the jar")
        
        # Remove cookies from the jar
        self._cookies -= n

    # Property to get the capacity of the jar (read-only)
    @property
    def capacity(self):
        return self._capacity

    # Property to get the current size of the jar (number of cookies)
    @property
    def size(self):
        return self._cookies
