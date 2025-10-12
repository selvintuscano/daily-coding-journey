def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0  # First Fibonacci number
    elif n == 2:
        return 1  # Second Fibonacci number
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
n = int(input("Enter the position (n): "))
print(f"The {n}th Fibonacci number is: {fibonacci(n)}")
