class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]

        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            digits = self.plusOne(digits[:-1])
            digits.append(0)
            return digits