class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        x = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                y = prices[j] - prices[i]
                if x < y:
                    x = y
        return x
