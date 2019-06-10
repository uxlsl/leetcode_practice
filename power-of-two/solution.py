# leetcode 231. 2的幂
# https://leetcode-cn.com/problems/power-of-two/

# 2的幂只有一位1

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while n > 1:
            if n == 2:
                return True
            n = float(n) / 2
        return False

