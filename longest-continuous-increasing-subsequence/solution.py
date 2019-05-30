# leetcode 674
# https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        m_l = 1 # 记录最长的递增长度
        cur = 1 # 记录当前最长的递增长度
        a = nums[0]

        for i in nums[1:]:
            if a < i:
                cur += 1
                m_l = max(m_l,cur)
            else:
                cur = 1
            a = i

        return m_l
