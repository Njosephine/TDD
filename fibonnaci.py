# Nanyonga && Racheal Abaasa

# Recursive Method : This method takes longer time to execute on large numbers
# def fib(n):
#     if not isinstance(n, int):
#         raise TypeError("Fibonacci is only defined for integers")
#     if n < 0:
#         raise ValueError("Fibonacci is not defined for negative numbers")
#     if n == 0:
#       return 0
#     elif n == 1:
#        return 1
#     else:
#        return fib(n-1) + fib(n-2)

# Using a loop: This method takes short time to execute on large numbers
# def fib(n):
# Input validations
# if not isinstance(n, int):
#    raise TypeError("Fibonacci is only defined for integers")
# if n < 0:
#     raise ValueError("Fibonacci is not defined for negative numbers")

# Base values
# if n == 0:
#   return 0
# elif n == 1:
#     return 1

# Loop to calculate the fibonnaci number
# prev,curr = 0,1
# for _ in range(2, n+1):

#    prev,curr = curr, prev + curr

# return curr

# This method takes shorter time to execute on large numbers

from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if not isinstance(n, int):
        raise TypeError("Fibonacci is only defined for integers")
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
