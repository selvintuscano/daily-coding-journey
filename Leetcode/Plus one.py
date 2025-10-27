class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and move backward
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1  # add one to the current digit
            
            # if the digit is less than 10, no carry -> return result
            if digits[i] < 10:
                return digits
            
            # if digit becomes 10, set it to 0 and carry 1 to the next iteration
            digits[i] = 0
        
        # if all digits were 9, we need to add a new 1 at the start
        return [1] + digits
