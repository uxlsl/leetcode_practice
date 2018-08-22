class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        m = defaultdict(int)
        for i in nums:
            m[i] += 1
            if m[i] == 2:
                a = i
        nums = sorted(m.keys())
        return a
