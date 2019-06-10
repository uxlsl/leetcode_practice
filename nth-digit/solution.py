class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 1
        while n > 0:
            if len(str(x)) >= n:
                return int(str(x)[n-1])
            else:
                n -= len(str(x))
            x += 1
