class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sub = None # 记录当前最大值
        cur = None # 记录连接端最大值

        for i in nums:
            if max_sub is None:
                max_sub = i
            if cur is None:
                cur = i
            else:
                cur = max(cur+i, i)
                if cur > max_sub:
                    max_sub = cur

        return max_sub
