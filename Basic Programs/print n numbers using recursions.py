def print_numbers(n: int) -> None:
    """Print numbers from 1 to n (inclusive) using recursion."""
    if n <= 0:          # base case: nothing to print for non-positive n
        return
    print_numbers(n - 1)  # recursive call handles 1..(n-1)
    print(n)              

print(print_numbers(23))