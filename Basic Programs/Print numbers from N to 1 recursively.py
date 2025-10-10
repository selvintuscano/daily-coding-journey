def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)
N = int(input("Enter a number: "))
print_numbers(N)