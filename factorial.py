def factorial(n: int):
    factor = 1
    for i in range(1, n+1):
        factor *= i
    return factor


print(factorial(4))
