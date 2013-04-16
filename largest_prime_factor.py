def get_factors(n):
    """(int)->list of ints
    Return list of factorials of n.

    >>> get_factors(4)
    [1, 2, 4]
    """
    factors = []
    for num in range(1,n+1):
        if n % num == 0:
            factors.append(num)
    return factors

def prime_factors(n):
    """(int)-> list of int
    Return list of prime factors of n.

    >>> prime_factors(26)
    [2, 13]
    >>> prime_factors(221)
    [13, 17]
    """
    n_factors = []
    n_factors = get_factors(n)
    prime_factors = []
    for factor in n_factors:
        factor_factors = get_factors(factor)
        if len(factor_factors) == 2:
            prime_factors.append(factor)
    return prime_factors
            

def largest_prime_factor(n):
    """(int)-> int
    Return the largest prime factor of n.

    >>> largest_prime_factor(221)
    17
    >>> largest_prime_factor(15)
    5
    """
    return max(prime_factors(n))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
