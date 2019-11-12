class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(x,n):
            if n == 0:
                return 1
            ret = 0
            for i in range(10):
                if x[i] == 1:
                    x[i] = 0
                    ret += dfs(x,n-1)
                    x[i] = 1
            return ret

        X = {i:1 for i in range(10)}

        return dfs(X,n)
