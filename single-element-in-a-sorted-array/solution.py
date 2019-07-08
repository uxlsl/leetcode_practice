# leetcode
# https://leetcode-cn.com/problems/single-element-in-a-sorted-array/
# 考虑用二分法

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        i = 0
        while i < len(nums) -1:
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]

        return nums[-1]
