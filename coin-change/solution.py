# leetcode
# https://leetcode-cn.com/problems/coin-change/
# 尽量选择最大的
import functools


class Solution(object):

    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = -1

        @functools.lru_cache(None)
        def f(coins, amount,count):
            nonlocal result
            if amount == 0:
                if result == -1:
                    result = count
                result = min(count,result)
                return
            elif amount < 0:
                return
            else:
                for i in coins:
                    f(coins, amount - i,count+1)

        coins = sorted(coins, reverse=True)
        f(tuple(coins), amount, 0)
        return result

    def coinChange(self, coins, amount):
        max = amount + 1
        dp = [max]*(amount+1)
        dp[0] = 0

        for i in range(1,amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        if dp[amount] <= amount:
            return dp[amount]
        return -1
