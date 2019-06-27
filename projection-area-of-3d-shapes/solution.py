# leetcode
# https://leetcode-cn.com/problems/projection-area-of-3d-shapes/
# 已知条件 N*N
# 分别求xy,yz,zx的面积
# 横竖的最大值


class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        N = len(grid)

        for i in range(N):
            h = 0
            v = 0
            for j in range(N):
                if grid[j][i] > h:
                    h = grid[j][i]
                if grid[i][j] > v:
                    v = grid[i][j]
                if grid[i][j] > 0:
                    area += 1
            # 竖面积
            area += h
            # 横面积
            area += v

        return area
