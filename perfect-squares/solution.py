import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        def f(n, mem):
            if n == 0:
                return 0
            x = int(math.sqrt(n))
            count = min([f(n - i * i, mem) + 1 for i in range(1, x + 1)])
            mem[n] = count
            return count

        mem = {}
        return f(n, mem)
