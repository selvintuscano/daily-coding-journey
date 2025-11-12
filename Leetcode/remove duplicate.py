class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # i points to the last unique element
        i = 0

        # j scans through the array
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # length of unique portion is i + 1
        return i + 1
