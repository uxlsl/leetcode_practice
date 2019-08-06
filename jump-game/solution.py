# leetcode
# https://leetcode-cn.com/problems/jump-game/
# 用一个数组记录
# 解法超时了


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = len(nums) - 1
        for i in range(lastPos,-1,-1):
            if i + nums[i] >= lastPos:
                lastPos = i

        return lastPos == 0

