# leetcode 463
# https://leetcode-cn.com/problems/island-perimeter/

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l = len(grid[0])
        h = len(grid)

        result = 0
        for i in range(h):
            for j in range(l):
                if grid[i][j]:
                    if j == 0 or grid[i][j-1] == 0:
                        result += 1
                    if j == l-1 or grid[i][j+1] == 0:
                        result += 1
                    if i == 0 or grid[i-1][j] == 0:
                        result += 1
                    if i == h-1 or grid[i+1][j] == 0:
                        result += 1
        return result
