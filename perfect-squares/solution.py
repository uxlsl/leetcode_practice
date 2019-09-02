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
            if n in mem:
                return mem[n]
            x = int(math.sqrt(n))
            count = min([f(n - i * i, mem) + 1 for i in reversed(range(1, x + 1))])
            mem[n] = count
            return count

        mem = {}
        return f(n, mem)

    def numSquares(self, n):
        dp = [i for i in range(n+1)]

        for i in range(1,n+1):
            j = 1
            while i - j*j >=0:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1

        return dp[n]
