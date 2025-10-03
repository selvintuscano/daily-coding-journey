import math
def check_perfect_square(n):
    if n < 0:
        return False
    sqrt = int(math.sqrt(n))
    return sqrt * sqrt == n 

print(check_perfect_square(26))