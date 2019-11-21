class Solution(object):
    def oddCells(self, n, m, indices):
        """
        :type n: int
        :type m: int
        :type indices: List[List[int]]
        :rtype: int
        """
        grid = [[0] * m for _ in range(n)]

        for i, j in indices:

            for x in range(m):
                grid[i][x] += 1

            for x in range(n):
                grid[x][j] += 1

        total = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] % 2 != 0:
                    total += 1

        return total
