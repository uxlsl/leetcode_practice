class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def f(nums, prev, curpos):
            if len(nums) == curpos:
                return 0
            taken = 0
            if nums[curpos] > prev:
                taken = 1 + f(nums, nums[curpos], curpos+1)

            notaken = f(nums, prev, curpos+1)
            return max(taken, notaken)

        return f(nums,-1,0)
