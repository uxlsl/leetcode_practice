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
        can = [False] * len(nums)
        # 表示第一个位置能够到达
        can[0] = True

        for i in range(len(nums)):
            if can[-1]:
                return True
            if can[i]:
                for j in range(nums[i]+1):
                    if i+j<len(nums):
                        can[i+j] = True
            else:
                break
        return can[-1]
