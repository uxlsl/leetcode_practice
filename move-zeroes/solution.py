class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = -1
        while i < len(nums):
            if nums[i] != 0:
                j += 1
                nums[j] = nums[i]
            i += 1
        j += 1
        while j < len(nums):
            nums[j] = 0
            j += 1
