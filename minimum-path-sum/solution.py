class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        record = [
                [0]*len(grid[0])
                for _ in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    record[i][j] = grid[i][j]
                elif i == 0 and j > 0:
                    record[i][j] = record[i][j-1] + grid[i][j] 
                elif i > 0 and j == 0:
                    record[i][j] = record[i-1][j] + grid[i][j] 
                else:
                    record[i][j] = grid[i][j] + min(record[i-1][j], record[i][j-1])

        return record[-1][-1]

