# leetcode
# https://leetcode-cn.com/problems/coin-change-2/
# 说明和coin-change差不多


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dp = defaultdict(lambda :0)
        dp[0] = 1
        # 这个有bug,重复加!

        for i in range(1,amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] += dp[i-coins[j]]

        return dp[amount]
