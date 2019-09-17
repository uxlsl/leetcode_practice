class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def f(grid, visited, x, y):
            if (
                0 <= x < len(grid)
                and 0 <= y < len(grid[0])
                and (x, y) not in visited
                and grid[x][y] == 1
            ):
                visited.add((x, y))
                arounds = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                count = 1
                for i, j in arounds:
                    count += f(grid, visited, x + i, y + j)

                return count
            return 0

        visited = set()
        val = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited:
                    val = max(f(grid, visited, i, j), val)

        return val
