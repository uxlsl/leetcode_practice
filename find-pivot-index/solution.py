class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        l = 0
        r = sum(nums) - nums[0]
        if l == r:
            return 0

        for i,v in enumerate(nums[1:], 1):
            l += nums[i-1]
            r -= nums[i]
            if l == r:
                return i

        return -1
