class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        cache = {}
        for i in range(0, len(nums)):
            if i == 0:
                cache[0] = nums[0]
            elif i == 1:
                cache[1] = max(nums[0], nums[1])
            else:
                cache[i] = max(cache[i-1], cache[i-2] + nums[i])
        return cache[len(nums)-1]
