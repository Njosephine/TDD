# Nanyonga && Racheal Abaasa

def fib(n):
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers")
    if n == 0:
      return 0
    elif n == 1:
       return 1
    else:
       return fib(n-1) + fib(n-2)
      