class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        count = 0
        last = None
        for i,v in enumerate(nums):
            if last != v and v + k in nums[i+1:]:
                count += 1
            last = v
        return count
