# Nanyonga && Racheal Abaasa

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
       return fib(n-1) + fib(n-2)
      