# leetcode
# 算法有名关健字 dp


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        ret = 0
        dp = [[0] * len(B) for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B)):
                if A[i] == B[j]:
                    if i - 1 >= 0 and j - 1 >= 0 and A[i - 1] == B[j - 1]:
                        dp[i][j] = dp[i-1][j-1]+1
                    else:
                        dp[i][j] = 1
                ret = max(ret, dp[i][j])
        return ret
