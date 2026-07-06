import math

def distance(point1, point2):
    """
    Calculate the distance between two points in 2D space.

    Parameters:
    point1 (tuple): The first point as a tuple (x1, y1).
    point2 (tuple): The second point as a tuple (x2, y2).

    Returns:
    float: The distance between the two points.
    """
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def area_of_circle(radius):
    """
    Calculate the area of a circle given its radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return math.pi * radius ** 2

def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    Parameters:
    n (int): The non-negative integer for which to calculate the factorial.

    Returns:
    int: The factorial of n.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

def fibonacci(n):
    """
    Calculate the nth Fibonacci number.

    Parameters:
    n (int): The index of the Fibonacci number to calculate.

    Returns:
    int: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
