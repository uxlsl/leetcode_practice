# leetcode
# https://leetcode-cn.com/problems/toeplitz-matrix/
# 解法
# 按意思检查数值是否一致

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """

        h = len(matrix)
        w = len(matrix[0])

        # 开始对角的点
        start = [[0,i] for i in range(w)]
        start += [[i,0] for i in range(h)]

        for x,y in start:
            val = matrix[x][y]

            while x < h and y < w:
                if matrix[x][y] != val:
                    return False
                x += 1
                y += 1
        return True
