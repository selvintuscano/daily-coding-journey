def reverse_number(n, rev=0):
    if n == 0:
        return rev
    
    rev = rev * 10 + n % 10
    
    
    return reverse_number(n // 10, rev)

num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print("Reversed number:", reversed_num)
