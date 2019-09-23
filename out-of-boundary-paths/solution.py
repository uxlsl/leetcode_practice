class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        import functools

        @functools.lru_cache(None)
        def f(i, j, k):
            if (i < 0 or i >= m) or (j < 0 or j >= n):
                return 1
            if k <= 0:
                return 0
            return (
                f(i - 1, j, k - 1)
                + f(i + 1, j, k - 1)
                + f(i, j - 1, k - 1)
                + f(i, j + 1, k - 1)
            )

        return f(i, j, N) % (10 ** 9 + 7)
