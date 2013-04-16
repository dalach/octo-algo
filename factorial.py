def factorial(n):
    """(int) -> int
    Return factorial of n.

    >>> factorial(5)
    120   
    """
    if n > 1:
        return n * factorial(n-1)
    else:
        return n
