rows = int(input("enter number of rows:"))

for i in range(1, rows+1):
    print(' ' * (rows-i) + '*' * i)

