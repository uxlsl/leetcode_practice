class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def isMag(grid, i, j):
            s = set()
            for x in range(3):
                for y in range(3):
                    s.add(grid[i+x][j+y])
            if s == set(range(1,10)):
                return (
                    # 列
                    grid[i][j] + grid[i + 1][j] + grid[i + 2][j]
                    == grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1]
                    == grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2]
                    ==
                    # 行
                    grid[i][j] + grid[i][j + 1] + grid[i][j + 2]
                    == grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2]
                    == grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2]
                    # 对角线
                    ==
                    grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]
                    == grid[i + 2][j] + grid[i + 1][j + 1] + grid[i][j + 2]
                )
            else:
                return False


        count = 0
        H = len(grid)
        L = len(grid[0])
        for i in range(H - 2):
            for j in range(L - 2):
                if isMag(grid, i, j):
                    count += 1

        return count
