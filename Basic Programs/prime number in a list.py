def is_prime(n):

    if n < 2:
        return True
    if n == 2:
        return True
    if n % 2==0:
        return False
    
    for i in range(3,int(n**0.5)+1, 2):
        if n%i==0:
            return False
        
    return True

def primes(start,end):
    primes = []
    for i in range(start,end+1):
        if is_prime(i):
            primes.append(i)
    return primes

print(primes(10,30))