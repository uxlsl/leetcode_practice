class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        from functools import lru_cache

        @lru_cache(None)
        def f(i, S):
            if i == 0:
                count  = 0
                if nums[0] == S :
                    count += 1
                if nums[0] == -S:
                    count += 1
                return count

            return f(i-1, S + nums[i]) + f(i-1, S - nums[i])

        return f(len(nums)-1, S)
