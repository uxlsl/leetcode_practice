class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_cols = [0] * len(grid[0])
        max_rows = [0] * len(grid)
        a = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_rows[i] = max(max_rows[i],grid[i][j])
                max_cols[j] = max(max_cols[j],grid[i][j])
                a += grid[i][j]
        b = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                b += min(max_rows[i], max_cols[j])

        return b - a
