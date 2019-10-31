class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import collections

        n = len(prices)
        max_k = 2
        dp = collections.defaultdict(int)
        dp[(-1,1,0)] = 0
        dp[(-1,1,1)] = -float('inf')
        dp[(-1,2,0)] = 0
        dp[(-1,2,1)] = -float('inf')
        for i in range(0,n):
            for k in range(max_k, 0, -1):
                dp[(i, k, 0)] = max(dp[(i - 1, k, 0)], dp[(i - 1, k, 1)] + prices[i])
                dp[(i, k, 1)] = max(
                    dp[(i - 1, k, 1)], dp[(i - 1, k - 1, 0)] - prices[i]
                )
        return dp[(n - 1, max_k, 0)]
