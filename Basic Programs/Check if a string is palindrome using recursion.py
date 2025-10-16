def is_palindrome(s):
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome(s[1:-1])

string = input("Enter a string: ").lower().replace(" ", "")  # ignore spaces and case
if is_palindrome(string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
