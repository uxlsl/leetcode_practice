class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        while n > 1:
            if n == 4:
                return True
            n = float(n) / 4
        return False
