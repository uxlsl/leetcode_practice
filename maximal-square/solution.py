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
        max_l = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    max_l = 1
                    m[i, j, 1] = True
                else:
                    m[i, j, 1] = False
        L = min(len(matrix), len(matrix[0]))
        for l in range(2, L + 1):
            can = False
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    if i + l - 1 >= len(matrix) or j + l - 1 >= len(matrix[0]):
                        continue
                    if m[i, j, l - 1]:
                        # 检查增加的边是否全为'1'
                        for z in range(l):
                            if (
                                matrix[i + z][j + l - 1] == "0"
                                or matrix[i + l - 1][j + z] == "0"
                            ):
                                m[i, j, l] = False
                                break
                        else:
                            can = True
                            m[i, j, l] = True
                            max_l = max(max_l, l)
                    else:
                        m[i, j, l] = False

            if not can:
                break

        return max_l * max_l
