def count_digit(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0 
    while n > 0:
        count = count +1
        n = n//10
    return count

print(count_digit(123))
