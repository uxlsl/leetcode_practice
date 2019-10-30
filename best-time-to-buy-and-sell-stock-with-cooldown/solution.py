class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        INT_MIX = -1000
        sold = 0
        rest = 0
        hold = INT_MIX

        for p in prices:
            pre_sold = sold
            sold = hold + p
            hold = max(hold, rest - p)
            rest = max(rest, pre_sold)
        return max(sold, rest)

