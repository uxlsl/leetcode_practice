# leetcode
# 统计不在边边的1，的数量

class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """

        def f(A, i, j):
            if 0<=i < len(A) and 0<=j < len(A[0]) and A[i][j] == 1:
                A[i][j] = 0
                f(A, i-1, j)
                f(A, i+1, j)
                f(A, i, j-1)
                f(A, i, j+1)

        for i in range(len(A[0])):
            f(A, 0, i)
            f(A, len(A)-1, i)

        for i in range(len(A)):
            f(A, i, 0)
            f(A, i, len(A[0])-1)

        return sum(sum(A[i]) for i in range(len(A)))
