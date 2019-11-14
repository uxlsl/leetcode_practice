class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 超时，考虑线性算法
        # score = 0
        # for i in range(len(A)):
        # for j in range(i + 1, len(A)):
        # score = max(score, A[i] + A[j] + i - j)

        score = 0
        num = A[0]

        for i in range(1, len(A)):
            num -= 1
            score = max(score, num + A[i])
            num = max(A[i], num)
        return score
