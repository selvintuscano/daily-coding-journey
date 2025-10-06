a = int(input("enter a number"))
b = int(input("enter a number"))

maxm = max(a,b)

while(True):
    if maxm%a == 0 and maxm%b ==0:
        break
    maxm = maxm + 1

print(f"the lcm is {maxm}")
