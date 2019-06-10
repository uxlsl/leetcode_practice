# leetcode
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        ret = 0
        x = None
        i = 1
        while i < len(prices):
            if prices[i-1] > prices[i]:
                if x is not None:
                    ret += prices[i-1] - prices[x]
                    x = None
            elif prices[i-1] < prices[i]:
                if x is None:
                    x = i - 1
            else:
                pass
            i += 1

        if x is not None and x < i-1 and prices[x] < prices[i-1]:
            ret += prices[i-1] - prices[x]

        return ret
