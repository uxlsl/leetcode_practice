class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        stack = nums[:k]
        result = [max(stack)]
        for i in nums[k:]:
            stack.pop(0)
            stack.append(i)
            result.append(max(stack))
        return result
