def is_perfect_number(n):
    if n <= 0:
        return False
    
    divisor_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisor_sum += i
    
    return divisor_sum == n

print(is_perfect_number(6))