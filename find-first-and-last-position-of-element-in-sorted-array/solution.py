from bisect import bisect_left


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = bisect_left(nums, target)
        if 0<=l<len(nums) and nums[l] == target:
            h = l
            while h < len(nums) and nums[h] == target:
                h += 1
            return [l,h-1]
        else:
            return [-1,-1]
