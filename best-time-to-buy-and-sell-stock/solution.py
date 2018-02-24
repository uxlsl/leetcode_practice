class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        val = 0
        x = prices[0] # 记录当前区间最低值

        for i in prices[1:]:
            if x > i:
                x = i
            val = max(val, i-x)

        return val

