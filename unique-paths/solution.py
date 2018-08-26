class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        record = [
                [0]*m for _ in range(n)
                ]
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    record[i][j] = 1
                else:
                    record[i][j] = record[i-1][j] + record[i][j-1]
        return record[n-1][m-1]
