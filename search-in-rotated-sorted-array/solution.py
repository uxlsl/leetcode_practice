# leetcode
# 二分法查找


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        for i,v in enumerate(nums):
            if v == target:
                return i
