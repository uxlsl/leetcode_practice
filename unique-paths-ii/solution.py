class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        record = [
                [0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))
                ]
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 or j == 0:
                    if obstacleGrid[i][j] == 1:
                        record[i][j] = 0
                    else:
                        if i > 0:
                            record[i][j] = record[i-1][j]
                        elif j > 0:
                            record[i][j] = record[i][j-1]
                        else:
                            record[i][j] = 1
                else:
                    if obstacleGrid[i][j] == 1:
                        record[i][j] = 0
                    else:
                        record[i][j] = record[i-1][j] + record[i][j-1]
        return record[-1][-1]
