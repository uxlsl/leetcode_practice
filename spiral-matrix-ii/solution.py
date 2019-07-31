# leetcode
# https://leetcode-cn.com/problems/spiral-matrix-ii/
# 一圈一圈


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        count = 1
        matrix = [[0] * n for _ in range(n)]
        for i in range((n + 1) // 2):
            L = n - 2 * i
            # 左上角
            x, y = i, i
            while y  < i + L:
                matrix[x][y] = count
                count += 1
                y += 1
            # 右上角
            x, y = i + 1, i +L-1
            while x < i + L-1:
                matrix[x][y] = count
                count += 1
                x += 1

            # 右下角
            x, y = i + L-1, i +L-1
            while y > i:
                matrix[x][y] = count
                count += 1
                y -= 1
            # 左下角
            x, y = i + L-1, i
            while x > i:
                matrix[x][y] = count
                count += 1
                x -=1

        return matrix
