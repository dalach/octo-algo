def find_sum_of_3_5(n):
    """(int)->int
    Return sum of all the numbers below n that are divided by 3 or 5.
    
    >>> find_sum_of_3_5(10)
    23
    """
    
    sum_of_num = 0
    for num in range(n):
        if num % 3 == 0 or num % 5 == 0:
            sum_of_num += num
    return sum_of_num
