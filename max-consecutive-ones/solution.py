class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cur = 0
        old = 0

        for i in nums:
            if i == 1:
                cur += 1
                if cur > old:
                    old = cur
            else:
                cur = 0

        return max(old, cur)
