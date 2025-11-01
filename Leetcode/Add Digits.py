class Solution:
    def addDigits(self, num: int) -> int:

        while num >= 10:
            sumd = 0 

            while num > 0:
                digit = num%10
                sumd = sumd + digit
                num = num//10
            num = sumd
        return num