#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    ---------------------
    Recursively calculates the factorial of a non-negative integer n.
    Factorial of a number n is the product of all positive integers <= n.
    For example, factorial(4) = 4 * 3 * 2 * 1 = 24.

    Parameters:
    -----------
    n : int
        A non-negative integer for which the factorial is to be calculated.

    Returns:
    --------
    int
        The factorial of the given integer n. Returns 1 if n is 0.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get input from command line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
