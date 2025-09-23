def palindrome(num):

    s = str(num)

    return s==s[::-1]

print(palindrome('122'))

# solution 2 

def palindrome1(n):

    orignal = n
    reversed = 0

    while n > 0:
        digit = n%10
        reversed = reversed * 10 + digit 
        n = n//10

    return orignal == reversed 


