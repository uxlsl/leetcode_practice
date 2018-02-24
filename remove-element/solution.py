class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        i, j = 0, -1
        while i < len(nums):
            if nums[i] != val:
                j += 1
                nums[j] = nums[i]
            i += 1
        return j + 1
