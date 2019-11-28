# leetcode
# 一个工人都最多只能安排一个工作，但是一个工作可以完成多次。
# 优化问题!
# 官方比这个实现好
# https://leetcode-cn.com/problems/most-profit-assigning-work/solution/an-pai-gong-zuo-yi-da-dao-zui-da-shou-yi-by-leetco/


class Solution(object):
    def maxProfitAssignment1(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        total = 0
        m = {}
        for w in worker:
            x = 0
            if w in m:
                x = m[w]
            else:
                for d, p in zip(difficulty, profit):
                    if w >= d:
                        x = max(x, p)
                m[w] = x
            total += x

        return total

    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """

        dp = [[i, j] for i, j in zip(difficulty, profit)]
        dp = sorted(dp, key=lambda x: x[0])

        v = dp[0][1]

        # 排能力和最大收益

        for i in dp[1:]:
            if v < i[1]:
                v = i[1]
            else:
                i[1] = v

        worker = sorted(worker)
        total = 0
        cur = 0

        for w in worker:
            if w < dp[cur][0]:
                continue
            while cur < len(dp) - 1:
                if w < dp[cur + 1][0]:
                    break
                cur += 1
            if w > dp[-1][0]:
                cur = len(dp) - 1
            total += dp[cur][1]

        return total
