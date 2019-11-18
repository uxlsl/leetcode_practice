# leetcode
# https://leetcode-cn.com/problems/maximum-width-ramp/

class Solution(object):
    def maxWidthRamp1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        val = 0
        for i in range(len(A)):
            for j in reversed(range(i+1+val, len(A))):
                if A[i] <= A[j]:
                    val = max(val, j-i)
                    break

        return val

    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        dp = defaultdict(int)
        dp[0] = 0
        val = 0
        for i in range(1, len(A)):
            # i-1 ... 0
            for j in range(i):
                if A[i] >= A[j]:
                    dp[i] = max(dp[i], dp[j] + i - j)
                    val = max(dp[i],val)
        return val



