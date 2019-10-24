# leetcode

# 数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

# 如果满足以下条件，则称子数组(P, Q)为等差数组：

# 元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dp = [0]*len(A)
        total = 0

        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = 1+dp[i-1]
                total += dp[i]

        return total
