def factorial(n):
    """
    Returns the factorial of n

    >>> factorial(2)
    2

    >>> factorial(3)
    6

    >>> factorial(5)
    120

    >>> factorial(14)
    87178291200
    """
    
    result = 1

    for i in range(1,n+1):
        result *= i

    return result

def triangle(n):
    """
    Returns the nth triangle number

    >>> triangle(0)
    0

    >>> triangle(1)
    1

    >>> triangle(2)
    3

    >>> triangle(9)
    45

    >>> triangle(900)
    405450
    """

    accumulator = 0

    for i in range(1,n+1):
        accumulator += i

    return accumulator

def fibonacci(n):
    """
    Returns the nth Fibonacci number

    >>> fibonacci(0)
    0

    >>> fibonacci(1)
    1
    
    >>> fibonacci(2)
    1

    >>> fibonacci(3)
    2
    
    >>> fibonacci(4)
    3
    
    >>> fibonacci(5)
    5
    
    >>> fibonacci(12)
    144
    """

    if n == 0:
        return 0
    if n == 1:
        return 1
        
    previous = 0
    current = 1

    for i in range(n-1):
        previous, current = current, current + previous

    return current

def pow(a, b):
    """ 
    Returns a raised to the b power

    We may assume that b will always be a non-negative integer 

    Note: this algorithm uses many more multiplies than is necessary. Extra 
    credit may be awarded for more efficient.

    >>> pow(2, 0)
    1

    >>> pow(2, 1)
    2

    >>> pow(10, 3)
    1000

    >>> pow(171, 17)
    91397407411741874683083843738640173291
    """

    result = 1

    for _ in range(b):
        result *= a

    return result
