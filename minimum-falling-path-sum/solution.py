class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        import copy
        B = copy.deepcopy(A)

        for i in range(1,len(A)):
            for j in range(len(A[0])):
                B[i][j] = A[i][j] + B[i-1][j]
                if j - 1 >= 0:
                    B[i][j] = min(B[i][j], A[i][j] + B[i-1][j-1])
                if j+1 < len(A[0]):
                    B[i][j] = min(B[i][j], A[i][j] + B[i-1][j+1])

        return min(B[-1])
