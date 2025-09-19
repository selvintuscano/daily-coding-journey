n = int(input('enter a number'))
m = int(input('enter a number'))

n = n+m 
m = n-m
n=n-m

print(n,m)

# method 2

n,m = m,n

print(n,m)