def reverse_number(n: int) -> int:
    
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

print(reverse_number(123))