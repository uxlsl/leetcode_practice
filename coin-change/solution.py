class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        cache = {}
        def f(coins,amount):
            if amount < 0:
                return -1
            elif amount == 0:
                return 0
            if amount in cache:
                return cache[amount]
            m = -1
            for coin in coins:
                count = f(coins, amount-coin)
                if count >= 0:
                    if m > 0:
                        m = min(count + 1, m)
                    else:
                        m = count + 1
            cache[amount] = m
            return m
        return f(coins, amount)
