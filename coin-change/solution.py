class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount < 0:
            return -1
        elif amount == 0:
            return 0
        m = -1
        for coin in coins:
            count = self.coinChange(coins, amount-coin)
            if count >= 0:
                if m > 0:
                    m = min(count + 1, m)
                else:
                    m = count + 1
        return m
