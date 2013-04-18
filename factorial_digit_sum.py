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


def factorial_digit_sum(n):
    """(int)->int
    Return sum of digits in a factoral of n.

    >>> factorial_digit_sum(4)
    6
    >>> factorial_digit_sum(5)
    3
    """
    number = factorial(n)
    digits_sum = 0
    for char in str(number):
        digits_sum += int(char)
    return digits_sum
