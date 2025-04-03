def add(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def fibonacci(n: int) -> int:
    """ using recursion """
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
