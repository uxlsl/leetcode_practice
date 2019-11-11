# leetcode
# https://leetcode-cn.com/problems/longest-well-performing-interval/


class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """

        far = 0
        cur = 0
        l = 0

        for h in hours:
            if h > 8:
                cur += 1
            else:
                cur -= 1
            if cur > 0:
                l += 1
            else:
                cur = 0
                l = 0
            far = max(far, l)

        return far
