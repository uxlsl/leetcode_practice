# leetcode
# https://leetcode-cn.com/problems/maximal-square/
# 重复的子问题多
# 长度从1开始算


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    m[i, j, 0] = True
                else:
                    m[i, j, 0] = False
        max_l = 0
        L = min(len(matrix), len(matrix[0]))
        for l in range(1, L + 1):
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i + l >= len(matrix) or j + l >= len(matrix[0]):
                        continue
                    if m[i, j, l - 1]:
                        # 检查增加的边是否全为'1'
                        for z in range(l):
                            if (
                                matrix[i + z][j + l] == "0"
                                or matrix[i + l][j + z] == "0"
                            ):
                                m[i, j, l] = False
                                break
                        else:
                            m[i, j, l] = True
                            max_l = max(max_l, l)
                    else:
                        m[i, j, l] = False

        max_l += 1
        return max_l * max_l
