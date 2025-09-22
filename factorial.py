# Pair: Nanyonga Josephine && Racheal Abaasa


def factorial(n):
    # Factorial is only defined for non-negative integers
    if n < 0:
        raise ValueError("factorial() not defined for negative values")

    # Start with 1 (since factorial multiplies numbers together,
    # and multiplying by 1 doesn't change the result)
    x = 1

    # Loop from 2 up to n (inclusive), multiplying each number into x
    for num in range(2, n + 1):
        x = x * num

    # Return the final product, which is n!
    return x
