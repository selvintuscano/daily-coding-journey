def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)

# Example: find factorial of 5
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
