# Your code here
def factorial(n):
    numbers = range(1, n+1)
    total = 1
    for i in numbers:
        total *= i

    return total

print(factorial(3))
