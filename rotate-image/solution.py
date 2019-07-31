# leetcode
# 解决方法
import copy


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        shadow = copy.deepcopy(matrix)
        L = len(shadow)

        for i in range(L):
            for j in range(L):
                matrix[j][L-i-1] = shadow[i][j]
