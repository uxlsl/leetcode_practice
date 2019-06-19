# leetcode
# 转置矩阵
# https://leetcode-cn.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        h = len(A)
        w = len(A[0])

        result = [[] for i in range(w)]

        for i in range(h):
            for index,j in enumerate(range(w)):
                result[index].append(A[i][j])

        return result

