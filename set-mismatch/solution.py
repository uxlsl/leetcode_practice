class Solution:
    def findErrorNums(self, nums):
        S = sum(set(nums))
        return [sum(nums)-S ,len(nums)*(len(nums)+1)//2-S]

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

        for i in range(1,len(nums)+1):
            if i not in m:
                return a, i

