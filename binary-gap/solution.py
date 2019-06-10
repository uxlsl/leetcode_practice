# leetcode 868
# https://leetcode-cn.com/problems/binary-gap/

class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        i = 0
        x = None
        while N > 0:
            if N & 1:
                if x is None:
                    x = i
                else:
                    res = max(res,i-x)
                    x = i
            N = N >> 1
            i += 1

        return res
