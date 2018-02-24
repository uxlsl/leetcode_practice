
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_sub = cur = sum(nums[:k])

        for i in range(k, len(nums)):
            cur -= nums[i-k]
            cur += nums[i]

            if max_sub < cur:
                max_sub = cur

        return max_sub/k
