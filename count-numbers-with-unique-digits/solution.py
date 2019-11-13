class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        res, muls = 10, 9
        for i in range(1, min(n,10)):
            muls *= 10 - i
            res += muls
        return res
