class Solution(object):
    def isPalindrome(self, s):
        l = 0 
        r = len(s)-1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            
            if s[l].upper() != s[r].upper():
                return False

            l += 1
            r -= 1

        return True
            



        
        