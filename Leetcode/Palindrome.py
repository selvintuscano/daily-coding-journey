class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        reversed_number = 0 
        original = x

        while x > 0:
            digit = x%10
            reversed_number = reversed_number*10 + digit
            x = x//10

        return original == reversed_number
        