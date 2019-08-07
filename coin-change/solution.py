# leetcode
# https://leetcode-cn.com/problems/coin-change/
# 尽量选择最大的


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def f(coins, amount):
            if amount == 0:
                return True
            elif amount < 0:
                return False
            else:
                for i in coins[::-1]:
                    if f(coins, amount - i):
                        return True
                return False

        return f(coins, amount)
