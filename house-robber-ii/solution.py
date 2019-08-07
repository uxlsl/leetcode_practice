class Solution(object):
    def _rob(self, nums):
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

    def rob(self, nums):
        # 第一个和最后一个不能共存
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[1:]),
                self._rob(nums[:-1]),
                )
