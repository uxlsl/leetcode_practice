# leetcode
# https://leetcode-cn.com/problems/number-of-islands/
# 结果至少有一个
# 多少个连续的1
# 用深度算法

import copy


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def mark(grid, used, i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1' and used[i][j] == False:
                used[i][j] = True
                mark(grid, used, i, j - 1)
                mark(grid, used, i, j + 1)
                mark(grid, used, i - 1, j)
                mark(grid, used, i + 1, j)

        count = 0
        used = copy.deepcopy(grid)
        for i in range(len(used)):
            for j in range(len(used[0])):
                used[i][j] = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and used[i][j] == False:
                    mark(grid, used, i, j)
                    count += 1

        return count
