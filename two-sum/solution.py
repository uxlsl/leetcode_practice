from collections import defaultdict

class Solution(object):
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        m = defaultdict(list)

        for i, v in enumerate(nums):
            m[v].append(i)

        for v in nums:
            try:
                x = m[v].pop()
                y = m[target - v].pop()
                return sorted([x, y])
            except:
                pass

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target-num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i
