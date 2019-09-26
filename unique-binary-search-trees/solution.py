class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        import functools
        @functools.lru_cache(None)
        def f(start, end):
            """
            start,end 实边界
            """
            # 只有一种可能
            if end <= start:
                return 1

            count = 0
            for i in range(start, end + 1):
                count += f(start, i - 1) * f(i + 1, end)
            return count

        return f(0, n - 1)
