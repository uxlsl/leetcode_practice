# leetcode
# https://leetcode-cn.com/problems/surface-area-of-3d-shapes/
# 解法:
# 求六个方向的表面积


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        area = 0
        # xy 正反面
        for i in range(N):
            h = 0
            v = 0
            for j in range(N):
                if grid[i][j] > 0:
                    area += 2

                if grid[i][j] > h:
                    h = grid[i][j]

                if grid[j][i] > v:
                    v = grid[j][i]

                if j > 0 and j+1 < N and grid[i][j-1] > grid[i][j] < grid[i][j+1]:
                    area +=2*(grid[i][j-1] - grid[i][j])

                if i > 0 and i+1 < N and grid[i-1][j] > grid[i][j] < grid[i+1][j]:
                    area +=2*(grid[i-1][j] - grid[i][j])

            area += 2*v
            area += 2*h

        return area


class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)

        ans = 0
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)

        return ans
